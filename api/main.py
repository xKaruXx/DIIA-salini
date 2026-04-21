from fastapi import FastAPI, Response, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import logging
import os
from .chat_service import ChatService
from .db import ChatMessage, ChatSession, SessionLocal, User, get_or_create_chat_session, save_chat_message, get_or_create_user, update_user_info
from jose import jwt # type: ignore
from datetime import datetime, timedelta
import secrets
from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import APIKeyHeader
from typing import Optional
import base64
from openai import OpenAI
from pathlib import Path
import uuid
from .webhook_service import WebhookService

# Clave secreta para firmar los tokens - genera una clave fuerte aleatoria
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Duración del token: 30 minutos
active_connections_per_ip = {}
MAX_CONNECTIONS_PER_IP = 5  # Ajusta según necesidades

def create_access_token(data: dict, request: Request, expires_delta: timedelta = None):
    """Crear token vinculado al navegador específico del usuario"""
    to_encode = data.copy()
    
    # Establecer tiempo de expiración (reducido para mayor seguridad)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # 30 minutos
    
    # Extraer datos del cliente que serán verificados
    ip_address = request.client.host
    user_agent = request.headers.get("user-agent", "")
    
    # Crear huella digital simple del navegador
    import hashlib
    browser_fingerprint = hashlib.md5(f"{user_agent}".encode()).hexdigest()
    
    # Incluir datos de verificación en el token
    to_encode.update({
        "ip": ip_address,
        "fp": browser_fingerprint[:12],  # Versión truncada del fingerprint
        "jti": str(uuid.uuid4()),  # ID único
        "exp": expire
    })
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """Verificar un token JWT"""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return None

# Esquema para verificar el token en las peticiones API
api_key_header = APIKeyHeader(name="X-Chat-Token", auto_error=False)

async def get_token_header(api_key: str = Depends(api_key_header)):
    if api_key:
        payload = verify_token(api_key)
        if payload:
            return payload
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado"
    )

# Configurar logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Coradir Chatbot API")

# Añade esta configuración CORS, son permisos de accesos que la API otorga a otros clientes 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3015", # Local
        "http://localhost:3000",
        "http://10.0.0.187:3015", # Local en mi red
        "https://energia.coradir.com.ar", # dirección de la página web de Coradir energia
        "https://botener.coradir.ai",
        "http://localhost", # Esto es por wordpress
        "http://10.0.0.187", # Agregue esto para permitir el acceso desde la IP local, en mi red
        "https://test.coradir.ai", 
        "https://testbotmov.coradir.ai",
        "https://botmov.coradir.ai",
        "https://movilidad.coradir.com.ar"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta de assets para el chat si existe
chat_assets_dir = "chat_assets"
if not os.path.exists(chat_assets_dir):
    os.makedirs(chat_assets_dir, exist_ok=True)
    
app.mount("/chat_assets", StaticFiles(directory=chat_assets_dir, html=True), name="chat_assets")

# Crear una instancia del servicio de chat
chat_service = ChatService()

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}
        
    async def connect(self, websocket: WebSocket, client_id: str):
        # Obtener IP del cliente
        client_ip = websocket.client.host
        
        # Verificar límite de conexiones por IP
        if client_ip in active_connections_per_ip:
            if active_connections_per_ip[client_ip] >= MAX_CONNECTIONS_PER_IP:
                logger.warning(f"Límite de conexiones excedido para IP: {client_ip}")
                await websocket.close(code=1008, reason="Límite de conexiones excedido")
                return False
            active_connections_per_ip[client_ip] += 1
        else:
            active_connections_per_ip[client_ip] = 1
            
        # Aceptar la conexión
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"Cliente {client_id} conectado desde {client_ip}. Total conexiones: {len(self.active_connections)}")
        return True
        
    def disconnect(self, client_id: str, client_ip=None):
        # Reducir contador de conexiones por IP
        if client_ip and client_ip in active_connections_per_ip:
            active_connections_per_ip[client_ip] -= 1
            if active_connections_per_ip[client_ip] <= 0:
                del active_connections_per_ip[client_ip]
                
        self.active_connections.pop(client_id, None)
        logger.info(f"Cliente {client_id} desconectado. Total conexiones: {len(self.active_connections)}")
        
    async def send_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            websocket = self.active_connections[client_id]
            await websocket.send_text(message)

manager = ConnectionManager()

# Rutas 
@app.get("/generate-token")
async def generate_token(request: Request):
    """
    Genera un token para incrustar el chat.
    Este debe ser llamado desde dominios autorizados.
    """
    client_host = request.client.host
    referer = request.headers.get("referer", "")
    
    logger.info(f"🔑 Token solicitado: IP={client_host}, Referer={referer}")
    
    # Lista de orígenes permitidos con URLs completas
    allowed_origins = [
        "http://localhost:3015", # Local
        "http://localhost:3000",
        "http://10.0.0.187:3015", # Local en mi red
        "https://energia.coradir.com.ar", # dirección de la página web de Coradir energia
        "https://botener.coradir.ai",
        "https://botmov.coradir.ai",
        "https://movilidad.coradir.com.ar",
        "https://test.coradir.ai", 
        "https://testbotmov.coradir.ai",
        "http://localhost"
    ]
    
    # Verificar si el Referer comienza con alguno de los orígenes permitidos
    is_allowed = any(referer.startswith(origin) for origin in allowed_origins)
    
    # También permitir solicitudes desde dominios específicos (verificación más flexible)
    allowed_domains = ["energia.coradir.com.ar", "localhost", "10.0.0.187", "botener.coradir.ai","botmov.coradir.ai","movilidad.coradir.com.ar","testbotmov.coradir.ai","test.coradir.ai"]
    is_allowed_domain = any(domain in referer for domain in allowed_domains)
    
    if not (is_allowed or is_allowed_domain):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado"
        )
    
    # Generar token con información del origen
    token_data = {
        "domain": referer,
        "client_ip": client_host,
    }
    
    token = create_access_token(token_data, request=request)
    
    return {"token": token, "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60}

@app.get("/embed.js")
async def get_embed_script():
    """Sirve el script para incrustar el chat en otros sitios"""
    embed_js_path = os.path.join("chat_assets", "js", "chat-embed.js")
    
    if os.path.exists(embed_js_path):
        with open(embed_js_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content=content, media_type="application/javascript")
    else:
        logger.error("No se encontró el archivo chat-embed.js")
        return Response(
            content="console.error('Error: Script de chat no disponible');",
            media_type="application/javascript"
        )

@app.get("/chat_assets/css/{file_name}")
async def get_css_file(file_name: str):
    """Sirve archivos CSS del chat"""
    css_file_path = os.path.join("chat_assets", "css", file_name)
    
    if os.path.exists(css_file_path) and file_name.endswith('.css'):
        with open(css_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content=content, media_type="text/css")
    else:
        logger.error(f"No se encontró el archivo CSS: {file_name}")
        return Response(
            content="/* CSS file not found */",
            media_type="text/css",
            status_code=404
        )

@app.get("/chat_assets/js/{file_name}")
async def get_js_file(file_name: str):
    """Sirve archivos JavaScript del chat"""
    js_file_path = os.path.join("chat_assets", "js", file_name)
    
    if os.path.exists(js_file_path) and file_name.endswith('.js'):
        with open(js_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content=content, media_type="application/javascript")
    else:
        logger.error(f"No se encontró el archivo JS: {file_name}")
        return Response(
            content="console.error('JavaScript file not found');",
            media_type="application/javascript",
            status_code=404
        )

@app.get("/chat_assets/images/{file_name}")
async def get_image_file(file_name: str):
    """Sirve archivos de imagen del chat"""
    image_file_path = os.path.join("chat_assets", "images", file_name)
    
    if os.path.exists(image_file_path):
        # Determinar el tipo MIME basado en la extensión
        mime_types = {
            '.svg': 'image/svg+xml',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        
        file_extension = os.path.splitext(file_name)[1].lower()
        mime_type = mime_types.get(file_extension, 'application/octet-stream')
        
        with open(image_file_path, "rb") as f:
            content = f.read()
        return Response(content=content, media_type=mime_type)
    else:
        logger.error(f"No se encontró el archivo de imagen: {file_name}")
        return Response(content="", status_code=404)


@app.get("/chat", response_class=HTMLResponse)
async def get_chat_page(
    request: Request,
    token: Optional[str] = None,
    chat_token: Optional[str] = Cookie(None)
):
    """
    Sirve la página del chat solo con un token válido.
    El token puede venir como parámetro de consulta o como cookie.
    """
    # Verificar token (de cookie o query param)
    final_token = token or chat_token
    
    if not final_token:
        logger.warning(f"Intento de acceso sin token desde: {request.headers.get('referer', '')}")
        return HTMLResponse(content="<h1>Acceso no autorizado</h1>", status_code=403)
    
    payload = verify_token(final_token)
    if not payload:
        logger.warning(f"Intento de acceso con token inválido desde: {request.headers.get('referer', '')}")
        return HTMLResponse(content="<h1>Token inválido o expirado</h1>", status_code=403)
    
    # Continuar con el código existente
    chat_html_path = os.path.join("chat_assets", "chat.html")
    
    if os.path.exists(chat_html_path):
        with open(chat_html_path, "r", encoding="utf-8") as f:
            content = f.read()
        return HTMLResponse(content=content)
    else:
        logger.error("No se encontró el archivo chat.html")
        return HTMLResponse(content="<h1>Error: Servicio no disponible</h1>")

def get_real_client_ip(websocket: WebSocket):
    """Obtiene la IP real del cliente considerando proxies y Docker"""
    
    # 1. Intentar obtener IP desde headers (más confiable)
    headers = dict(websocket.headers)

    # 🔍 LOG TEMPORAL PARA DEBUG
    logger.info(f"🔍 Headers recibidos: {headers}")
    logger.info(f"🔍 WebSocket client.host: {websocket.client.host}")
    
    # Cloudflare
    if 'cf-connecting-ip' in headers:
        return headers['cf-connecting-ip']
    
    # Proxy general (X-Forwarded-For puede tener múltiples IPs)
    if 'x-forwarded-for' in headers:
        # Tomar la primera IP (la más externa)
        ips = headers['x-forwarded-for'].split(',')
        return ips[0].strip()
    
    # Nginx u otros proxies
    if 'x-real-ip' in headers:
        return headers['x-real-ip']
    
    # Headers adicionales que pueden contener IP real
    if 'x-client-ip' in headers:
        return headers['x-client-ip']
    
    if 'x-forwarded' in headers:
        return headers['x-forwarded']
    
    # 2. Fallback: IP directa del WebSocket (puede ser proxy)
    return websocket.client.host

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    # Verificar el token en los parámetros de consulta
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008, reason="Token requerido")
        return
    
    # CON este nuevo bloque (que contiene la lógica anti-suplantación):
    try:
        # Decodificar token directamente
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extraer datos actuales del cliente
        ip_address = websocket.client.host
        user_agent = websocket.headers.get("user-agent", "")
        
        # Regenerar fingerprint para comparar
        import hashlib
        browser_fingerprint = hashlib.md5(f"{user_agent}".encode()).hexdigest()[:12]
        
        # Verificar IP con tolerancia para redes móviles/dinámicas
        token_ip = payload.get("ip", "")
        ip_mismatch = False
        
        # Para IPs de tipo IPv4, comparar solo los primeros dos octetos
        # Esto permite cierta flexibilidad para IPs dinámicas pero previene abusos
        if "." in token_ip and "." in ip_address:
            token_ip_parts = token_ip.split(".")[:2]
            current_ip_parts = ip_address.split(".")[:2]
            ip_mismatch = token_ip_parts != current_ip_parts
        else:
            # Para IPv6 u otros formatos, verificación directa
            ip_mismatch = token_ip != ip_address
            
        # Verificar fingerprint del navegador
        token_fp = payload.get("fp", "")
        fp_mismatch = token_fp != browser_fingerprint
        
        # Registrar intento sospechoso pero permitir pequeñas variaciones
        if ip_mismatch or fp_mismatch:
            logger.warning(f"Posible intento de suplantación - ClientID: {client_id}, "
                         f"IP en token: {token_ip}, IP actual: {ip_address}, "
                         f"FP en token: {token_fp}, FP actual: {browser_fingerprint}")
            
            # Si ambos valores no coinciden, rechazar la conexión
            if ip_mismatch and fp_mismatch:
                await websocket.close(code=1008, reason="Sesión inválida o expirada")
                return
            
    except Exception as e:
        logger.error(f"Error verificando token: {str(e)}")
        await websocket.close(code=1008, reason="Token inválido")
        return
    
    # Obtener IP del cliente
    real_ip = get_real_client_ip(websocket)
    client_ip = websocket.client.host

    # Intentar conectar con limitación
    connection_accepted = await manager.connect(websocket, client_id)
    if not connection_accepted:
        return  # La conexión ya fue cerrada por el límite excedido
        
    db = SessionLocal()
    
    try:
        # Primero, obtener o crear el usuario para este client_id
        user = get_or_create_user(db, client_id)
        logger.info(f"Usuario identificado: ID={user.id}, client_id={client_id}")

        # Guardar IP del cliente si no existe
        if not user.ip_address:
            update_user_info(db, client_id, ip_address=real_ip)
            logger.info(f"IP guardada para usuario {client_id}: {real_ip}")
        
        # Obtener o crear sesión de chat vinculada a este usuario
        chat_session = get_or_create_chat_session(db, client_id)
        logger.info(f"Sesión de chat: ID={chat_session.id}, user_id={chat_session.user_id}")
        
        chat_service.reset_off_topic_counter(client_id) # Reiniciar contador de preguntas irrelevantes
        
        # Mensaje de bienvenida (diferente según si es usuario nuevo o recurrente)
        welcome_message = {
            "sender": "bot",
            "message": "Hola 👋 Soy Cora, tu asistente virtual. ¿En qué te ayudo hoy? ",
            "type": "message"
        }
            
        await manager.send_message(json.dumps(welcome_message), client_id) # Se envia mensaje al front-end
        
        # Guardar mensaje de bienvenida en la BD
        save_chat_message(db, chat_session.id, "bot", welcome_message["message"])
        
        # Loop principal para recibir mensajes
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            
            # Verificar si el mensaje es de audio o texto
            if isinstance(data, dict) and data.get("message_type") == "audio":
                # Procesar mensaje de audio
                try:
                    # Extraer datos de audio (Base64)
                    audio_data = data.get("audio_data", "")
                    
                    # Eliminar la parte inicial del data URL (por ejemplo: "data:audio/webm;base64,")
                    if "," in audio_data:
                        audio_data = audio_data.split(",")[1]
                    
                    # Decodificar Base64
                    audio_bytes = base64.b64decode(audio_data)
                    
                    # Crear directorio temporal si no existe
                    temp_dir = Path("./temp_audio")
                    temp_dir.mkdir(exist_ok=True)
                    
                    # Guardar audio en archivo temporal
                    temp_file = temp_dir / f"audio_{client_id}_{datetime.now().timestamp()}.webm"
                    with open(temp_file, "wb") as f:
                        f.write(audio_bytes)
                    
                    # Transcribir audio usando OpenAI
                    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                    
                    with open(temp_file, "rb") as audio_file:
                        transcription = client.audio.transcriptions.create(
                            model="gpt-4o-transcribe",
                            file=audio_file,
                            language="es"
                        )
                    
                    # Convertir el audio a texto
                    user_message = transcription.text
                    
                    # Eliminar archivo temporal
                    if temp_file.exists():
                        temp_file.unlink()
                
                except Exception as e:
                    logger.error(f"Error al transcribir audio: {str(e)}")
                    error_message = {
                        "sender": "bot", 
                        "message": "Lo siento, no pude procesar tu mensaje de voz. ¿Podrías intentarlo de nuevo o escribir tu consulta?",
                        "type": "message"
                    }
                    await manager.send_message(json.dumps(error_message), client_id)
                    
                    # Habilitar controles en el cliente
                    enable_input = {
                        "sender": "system",
                        "type": "enable_input"
                    }
                    await manager.send_message(json.dumps(enable_input), client_id)
                    continue  # Saltar el resto del procesamiento
            else:
                # Mensaje de texto normal
                user_message = data.get("message", "")
            
            logger.info(f"Mensaje recibido de {client_id}: {user_message}")
            
            # Guardar mensaje del usuario en la BD
            save_chat_message(db, chat_session.id, "user", user_message)
            
            # Enviar señal de "escribiendo..."
            typing_message = {
                "sender": "bot",
                "message": "",
                "type": "typing"
            }
            await manager.send_message(json.dumps(typing_message), client_id)
            
            # Procesar mensaje con el servicio de chat
            response = await chat_service.process_message(user_message, client_id, real_ip)
            
            # Verificar si es una señal para terminar la sesión
            if isinstance(response, str) and response.startswith("SESSION_TERMINATE||"):
                # Extraer el mensaje para el usuario
                termination_message = response.split("||")[1]
                
                # Enviar mensaje final al usuario
                response_message = {
                    "sender": "bot",
                    "message": termination_message,
                    "type": "message"
                }
                await asyncio.sleep(0.5)
                await manager.send_message(json.dumps(response_message), client_id)
                
                # Guardar respuesta del bot en la BD
                save_chat_message(db, chat_session.id, "bot", termination_message)
                
                # Eliminar sesión y datos de usuario
                try:
                    # Eliminar mensajes de la sesión
                    db.query(ChatMessage).filter(ChatMessage.session_id == chat_session.id).delete()
                    # Eliminar la sesión
                    db.query(ChatSession).filter(ChatSession.id == chat_session.id).delete()
                    # Eliminar el usuario (esto forzará volver a recolectar datos)
                    db.query(User).filter(User.client_id == client_id).delete()
                    db.commit()
                    
                    # También eliminar la memoria en ChatService
                    if client_id in chat_service.memories:
                        del chat_service.memories[client_id]
                    
                    # También eliminar el contador de mensajes irrelevantes
                    if client_id in chat_service.off_topic_consecutive:
                        del chat_service.off_topic_consecutive[client_id]

                    logger.info(f"Sesión terminada para {client_id} por preguntas irrelevantes")
                except Exception as e:
                    logger.error(f"Error al eliminar datos: {str(e)}")
                
                # Cerrar la conexión WebSocket
                await websocket.close(code=1000, reason="Sesión terminada por preguntas irrelevantes")
                break

            # Enviar respuesta
            response_message = {
                "sender": "bot",
                "message": response,
                "type": "message"
            }
            await asyncio.sleep(0.5)
            await manager.send_message(json.dumps(response_message), client_id)
            
            # Guardar respuesta del bot en la BD
            save_chat_message(db, chat_session.id, "bot", response)
            
    except WebSocketDisconnect:
        manager.disconnect(client_id, client_ip)
    except Exception as e:
        logger.error(f"Error en la conexión WebSocket: {str(e)}")
        manager.disconnect(client_id, client_ip)
    finally:
        db.close()

@app.get("/test-webhook")
async def test_webhook():
    """
    Endpoint para probar la conexión con n8n webhook
    """
    webhook_service = WebhookService()
    
    # Probar conexión
    connection_ok = await webhook_service.test_webhook_connection()
    
    if connection_ok:
        return {"status": "success", "message": "Webhook conectado correctamente"}
    else:
        return {"status": "error", "message": "No se pudo conectar con webhook n8n"}

@app.post("/test-email-webhook")
async def test_email_webhook():
    """
    Endpoint para probar envío de webhook de email
    """
    webhook_service = WebhookService()
    
    # Datos de prueba
    test_user_data = {
        "user_id": "test_user_123",
        "client_id": "test_user_123", 
        "email": "test@ejemplo.com",
        "name": "Usuario Prueba",
        "timestamp": "2024-01-01T10:00:00"
    }
    
    test_conversation = {
        "full_conversation": [
            {"role": "user", "message": "Hola, me interesa información sobre vehículos eléctricos"},
            {"role": "bot", "message": "¡Hola! Me llamo Cora. Te puedo ayudar con información sobre nuestros vehículos TITO, TITA y CHIKI."},
            {"role": "user", "message": "¿Cuánto cuesta el TITO S5?"},
            {"role": "bot", "message": "El TITO S5-300 cuesta USD 16.981,25 y con aire acondicionado USD 17.731,25"},
            {"role": "user", "message": "Mi email es test@ejemplo.com para recibir novedades"}
        ],
        "total_messages": 5,
        "conversation_start": "2024-01-01T09:45:00",
        "last_interaction": "2024-01-01T10:00:00"
    }
    
    # Enviar webhook
    webhook_sent = await webhook_service.send_webhook(
        action_type="send_email_newsletter",
        user_data=test_user_data,
        conversation_data=test_conversation
    )
    
    if webhook_sent:
        return {"status": "success", "message": "Webhook de email enviado correctamente"}
    else:
        return {"status": "error", "message": "Error enviando webhook de email"}

@app.post("/test-whatsapp-webhook")
async def test_whatsapp_webhook():
    """
    Endpoint para probar envío de webhook de WhatsApp
    """
    webhook_service = WebhookService()
    
    # Datos de prueba
    test_user_data = {
        "user_id": "test_user_456",
        "client_id": "test_user_456", 
        "phone": "+541123456789",
        "name": "Juan Pérez",
        "timestamp": "2024-01-01T10:00:00"
    }
    
    test_conversation = {
        "full_conversation": [
            {"role": "user", "message": "Hola, necesito información sobre vehículos para delivery"},
            {"role": "bot", "message": "¡Perfecto! Para delivery te recomiendo la TITA S2, nuestra pickup eléctrica."},
            {"role": "user", "message": "¿Qué autonomía tiene?"},
            {"role": "bot", "message": "La TITA S2-300 tiene 300km de autonomía y puede cargar 500kg."},
            {"role": "user", "message": "¿Cuánto cuesta?"},
            {"role": "bot", "message": "La TITA S2-300 cuesta USD 16.981,25 y con AA USD 17.731,25"},
            {"role": "user", "message": "Mi teléfono es +541123456789 para que me contacten"}
        ],
        "total_messages": 7,
        "conversation_start": "2024-01-01T09:30:00", 
        "last_interaction": "2024-01-01T10:00:00"
    }
    
    # Enviar webhook
    webhook_sent = await webhook_service.send_webhook(
        action_type="send_whatsapp",
        user_data=test_user_data,
        conversation_data=test_conversation
    )
    
    if webhook_sent:
        return {"status": "success", "message": "Webhook de WhatsApp enviado correctamente"}
    else:
        return {"status": "error", "message": "Error enviando webhook de WhatsApp"}

# Ruta para verificar el estado de la API
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API funcionando correctamente"}