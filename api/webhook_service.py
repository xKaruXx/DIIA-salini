import aiohttp
import logging
import os
from typing import Dict, Any, Optional
import json

logger = logging.getLogger(__name__)

class WebhookService:
    def __init__(self):
        # URL del webhook de n8n (configurar en variables de entorno)
        self.n8n_webhook_url = os.getenv("N8N_WEBHOOK_URL", "")
        self.timeout = 10  # timeout en segundos
        
    async def send_webhook(
        self, 
        action_type: str,
        user_data: Dict[str, Any], 
        conversation_data: Dict[str, Any] = None
    ) -> bool:
        """
        Envía webhook unificado a n8n 
        
        Args:
            action_type: Tipo de acción ("send_email_newsletter" o "send_whatsapp")
            user_data: Datos del usuario (email, phone, name, user_id, etc.)
            conversation_data: Datos completos de la conversación
            
        Returns:
            bool: True si se envió exitosamente, False en caso contrario
        """
        try:
            # Preparar payload unificado para n8n
            payload = {
                "action_type": action_type,
                "user_data": {
                    "user_id": user_data.get("user_id", ""),
                    "client_id": user_data.get("client_id", ""),
                    "email": user_data.get("email"),  # Puede ser None
                    "phone": user_data.get("phone"),  # Puede ser None
                    "name": user_data.get("name"),    # Puede ser None
                    "timestamp": user_data.get("timestamp", "")
                },
                "conversation_data": conversation_data or {},
                "source": "chatbot_movilidad"
            }
            
            # Validar datos según acción
            if action_type == "send_email_newsletter" and not payload["user_data"]["email"]:
                logger.warning("No se puede enviar webhook de email: email vacío")
                return False
                
            if action_type == "send_whatsapp" and not payload["user_data"]["phone"]:
                logger.warning("No se puede enviar webhook de WhatsApp: teléfono vacío")
                return False
                
            # Validar que tenemos URL de webhook
            if not self.n8n_webhook_url:
                logger.warning("N8N_WEBHOOK_URL no configurada")
                return False
            
            contact_info = payload["user_data"]["email"] or payload["user_data"]["phone"]
            logger.info(f"Enviando webhook {action_type} para usuario: {contact_info}")
            
            # Enviar webhook de forma asíncrona
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.n8n_webhook_url,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=self.timeout),
                    headers={"Content-Type": "application/json"}
                ) as response:
                    
                    if response.status == 200:
                        logger.info(f"Webhook {action_type} enviado exitosamente para {contact_info}")
                        return True
                    else:
                        response_text = await response.text()
                        logger.error(f"Error en webhook {action_type}. Status: {response.status}, Response: {response_text}")
                        return False
                        
        except aiohttp.ClientTimeout:
            logger.error(f"Timeout enviando webhook {action_type}")
            return False
        except Exception as e:
            logger.error(f"Error enviando webhook {action_type}: {str(e)}")
            return False

    # Métodos de conveniencia que usan el webhook unificado
    async def send_email_newsletter_webhook(
        self, 
        user_data: Dict[str, Any], 
        conversation_data: Dict[str, Any] = None
    ) -> bool:
        """Envía webhook para email newsletter"""
        return await self.send_webhook("send_email_newsletter", user_data, conversation_data)
    
    async def send_whatsapp_webhook(
        self, 
        user_data: Dict[str, Any], 
        conversation_data: Dict[str, Any] = None
    ) -> bool:
        """Envía webhook para WhatsApp"""
        return await self.send_webhook("send_whatsapp", user_data, conversation_data)
    
    async def test_webhook_connection(self) -> bool:
        """
        Testa la conexión con el webhook de n8n
        
        Returns:
            bool: True si la conexión es exitosa
        """
        try:
            if not self.n8n_webhook_url:
                logger.error("N8N_WEBHOOK_URL no configurada")
                return False
                
            test_payload = {
                "action_type": "test_connection",
                "source": "chatbot_movilidad",
                "timestamp": "test"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.n8n_webhook_url,
                    json=test_payload,
                    timeout=aiohttp.ClientTimeout(total=5),
                    headers={"Content-Type": "application/json"}
                ) as response:
                    
                    if response.status == 200:
                        logger.info("Conexión con webhook n8n exitosa")
                        return True
                    else:
                        logger.error(f"Error probando conexión webhook. Status: {response.status}")
                        return False
                        
        except Exception as e:
            logger.error(f"Error probando conexión webhook: {str(e)}")
            return False