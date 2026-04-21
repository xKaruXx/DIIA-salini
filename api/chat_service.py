import asyncio
import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveJsonSplitter

from .db import SessionLocal, create_tables, update_user_info
from .webhook_service import WebhookService

logger = logging.getLogger(__name__)

MAX_OFF_TOPIC_CONSECUTIVE = 7  # Máximo de mensajes irrelevantes consecutivos antes de cerrar la sesión
DEFAULT_OPENAI_CHAT_MODEL = "gpt-4o-mini"
DEFAULT_OLLAMA_CHAT_MODEL = "gemma3:1b"
DEFAULT_OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
DEFAULT_OLLAMA_EMBEDDING_MODEL = "nomic-embed-text"
DEFAULT_VECTORSTORE_BASE_DIR = "./chroma_db"
DEFAULT_DATASET_PATH = "./dataset/knowledge_base_movilidad.jsonl"
DEFAULT_RAW_DATASET_PATH = "./dataset/dataset_movilidad.json"

class ChatService:
    def __init__(self):
        """Inicializa el servicio de chat con la configuración necesaria"""
        self.model_provider = os.getenv("LLM_PROVIDER", "ollama").strip().lower()
        self.embedding_provider = os.getenv("EMBEDDING_PROVIDER", self.model_provider).strip().lower()
        self.model_name = os.getenv(
            "CHAT_MODEL_NAME",
            DEFAULT_OLLAMA_CHAT_MODEL if self.model_provider == "ollama" else DEFAULT_OPENAI_CHAT_MODEL,
        )
        self.embedding_model_name = os.getenv(
            "EMBEDDING_MODEL_NAME",
            DEFAULT_OLLAMA_EMBEDDING_MODEL if self.embedding_provider == "ollama" else DEFAULT_OPENAI_EMBEDDING_MODEL,
        )
        self.model_temperature = float(os.getenv("MODEL_TEMPERATURE", "0.1"))
        self.prompt_variant = os.getenv("PROMPT_VARIANT", "sales").strip().lower()
        self.retrieval_k = int(os.getenv("RETRIEVAL_K", "4"))
        self.dataset_path = Path(os.getenv("RAG_DATASET_PATH", DEFAULT_DATASET_PATH))
        self.raw_dataset_path = Path(os.getenv("RAW_DATASET_PATH", DEFAULT_RAW_DATASET_PATH))
        self.vectorstore_base_dir = Path(os.getenv("VECTORSTORE_BASE_DIR", DEFAULT_VECTORSTORE_BASE_DIR))
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL")

        self._validate_runtime_configuration()
        create_tables()

        self.memories: Dict[str, ConversationBufferWindowMemory] = {}

        self.webhook_service = WebhookService()
        self.embeddings = self._create_embeddings()
        self.knowledge_texts, self.knowledge_metadatas = self._load_knowledge_texts()

        logger.info("Inicializando la base de datos vectorial...")
        self.vectorstore = self._crear_o_cargar_vectorstore()
        self.model = self._create_llm()

        self.whatsapp_sent_by_ip = {}  # ip -> {"count": count, "last_sent": datetime}
        self.whatsapp_limit_per_ip = 2  # Máximo 2 WhatsApp por IP
        self.whatsapp_limit_hours = 72  # 3 días = 72 horas
        
        # ===== CONFIGURACIÓN DEL PROMPT MODULAR =====
        self.personalidad = """
        Eres Cora, un asistente virtual especializado principalmente en CORADIR MOVILIDAD ELÉCTRICA una de las aristas de la empresa CORADIR SA.
        - Sé amable, educado y utiliza un lenguaje natural y amigable, usa emojis si lo necesitas.
        - Responde solo en ESPAÑOL RIOPLATENSE (no te olvides de esto).
        - Sé conciso, pero no demasiado cortante.
        - Utiliza el contexto de la conversación previa para dar respuestas más coherentes.
        - Mostrá entusiasmo por los vehículos eléctricos y sus beneficios cuando sea apropiado.
        """
        
        self.objetivo_principal = """
        Tu objetivo PRINCIPAL es convertir consultas en oportunidades de venta, ayudando a los usuarios a descubrir 
        cómo los vehículos eléctricos de CORADIR pueden resolver sus necesidades de movilidad.
        
        También podés proporcionar información básica sobre otros productos de la empresa (energía renovable, 
        televisores, computadoras, monitores), pero de manera general.
        
        PRIORIZA Y VENDE activamente los vehículos eléctricos: TITO, TITA, TITA CUADRILLA, BARRE-TITA, CHIKI.
        Siempre buscá generar INTERÉS y mostrar los BENEFICIOS únicos de cada vehículo.
        """
        
        self.estrategia_ventas = """
        ESTRATEGIA DE VENTAS Y CONTACTO:
        - RESPONDE TODAS las consultas con la información disponible. Solo solicita contacto en casos específicos:

        CUÁNDO PEDIR TELÉFONO:
        - Si detectas que el cliente muestra un interés en adquirir un vehículo eléctrico
        - Para contacto directo con representante de ventas sobre compra

        CUÁNDO PEDIR EMAIL:
        - Si quiere recibir novedades, lanzamientos, promociones futuras
        - Para información adicional que pueda surgir después

        MANEJO DE CONTACTO:
        - Si proporciona TELÉFONO: "Perfecto, te enviaremos un mensaje de WhatsApp con información de contacto y un representante de ventas se comunicará pronto"
        - Si proporciona EMAIL: "Excelente, te enviaremos un newsletter personalizado y te mantendremos informado sobre novedades"
        - Si preguntan por reenvío o no recibieron: "He registrado tu contacto correctamente. Si no recibís el mensaje en los próximos minutos, también podés contactarnos directamente al (0266) 4305996"
        - Tanto el mensaje de WhatsApp como el de email se enviarían de inmediato cuando se proporcionen los datos.
        - Si no tiene el dato pedido, preguntá por el otro solo si es necesario
        - Incluí siempre el contacto en tu respuesta para que lo vea

        IMPORTANTE: Cuando des información, destacá los beneficios únicos para generar interés.
        """
        
        self.reglas_comportamiento = """
        REGLAS DE COMPORTAMIENTO:
        - Si no sabes la respuesta, ofrece disculpas y sugiere alternativas.
        - No inventes información. Si no sabes la respuesta, di: "No tengo esa información, pero puedo ayudarte con otros temas relacionados con CORADIR."
        - Si la pregunta no es clara, o necesitas más información para contestar correctamente, pide aclaraciones.
        - Limítate a responder preguntas relacionadas con CORADIR MOVILIDAD ELÉCTRICA.
        - Si el usuario pregunta por cualquier vehículo eléctrico, responde general y luego pregunta si le interesa alguno en particular, no des toda la información de cada uno, sino lo más relevante según el contexto.
        - Como no puedes enviar fotos, si el usuario pregunta por fotos de los vehículos, indícale que puede verlas en el sitio web de movilidad, sección "Vehículos": https://movilidad.coradir.com.ar/
        - Para RECLAMOS o problemas: agradecé el feedback y dirigí al servicio técnico (0266) 5264805, mencionando que estos comentarios ayudan a mejorar.
        """
        
        self.restricciones_tecnicas = """
        RESTRICCIONES TÉCNICAS:
        - MUY IMPORTANTE: NO USES FORMATO MARKDOWN en tus respuestas.
        - La respuesta final debe salir en texto plano, sin títulos con asteriscos, sin listas numeradas markdown y sin viñetas con "*".
        - EXTREMADAMENTE IMPORTANTE: Cuando menciones URLs, NUNCA uses formato markdown. Presenta las URLs directamente sin ningún tipo de formato. 
          Por ejemplo, escribe "https://movilidad.coradir.com.ar/" en lugar de "[https://movilidad.coradir.com.ar/](https://movilidad.coradir.com.ar/)".
        - CRÍTICO: NUNCA uses HTML ni markdown. NO escribas <a href=...> ni [texto](url). Escribe las URLs directamente como texto plano. 
          Ejemplo: "Visitá https://movilidad.coradir.com.ar/ para más información" SIN etiquetas HTML.
        - Puedes recibir audios y responderlos a texto, pero no puedes enviar audios.
        """
        
        self.respuestas_sobre_ti = """
        RESPUESTAS SOBRE TI MISMO:
        - Si el usuario pregunta quién te desarrolló, responde brevemente: "Fui desarrollado por Coradir IA, la iniciativa de inteligencia artificial de CORADIR S.A. Yo soy uno de sus productos."
        - Si preguntan cómo funcionas, di: "Soy un asistente virtual que puede adaptarse a diferentes dominios de conocimiento. En mi caso, estoy especializado en brindarte información sobre CORADIR Movilidad Eléctrica y sus vehículos."
        - Si preguntan si pueden tener un chatbot similar, responde: "¡Por supuesto! Coradir IA ofrece servicios de desarrollo de asistentes virtuales personalizados que se pueden adaptar a las necesidades específicas de tu empresa. Para más información, puedes contactar a divisoft@coradir.com.ar o proximamente visitar nuestra web: https://coradir.ai/"
        """
        
        self.navegacion_sitio = """
        AYUDA PARA NAVEGAR EL SITIO WEB DE MOVILIDAD:
        - Si el usuario pregunta cómo encontrar algo en el sitio web de movilidad (https://movilidad.coradir.com.ar/), 
          guíalo usando la estructura de navegación.
        - Para consultas sobre AGENCIAS oficiales: https://movilidad.coradir.com.ar/agencias/
        - Para preguntas sobre los vehículos TITO, TITA, TITA CUADRILLA, BARRE-TITA y CHIKI, indícale que debe ir a la sección "Vehículos" en el menú principal.
        
        ACLARACIÓN GENERAL:
        - Recuerda que https://movilidad.coradir.com.ar/ es SOLAMENTE para vehículos eléctricos (TITO, TITA, TITA CUADRILLA, BARRE-TITA y CHIKI).
        - Para consultas específicas sobre energía renovable, recomienda visitar: https://energia.coradir.com.ar/
        - Para consultas sobre otros productos NO relacionados con movilidad eléctrica, sugiere SIEMPRE visitar el sitio principal: https://www.coradir.com.ar/
        """

        self.funcionalidades_disponibles = """
        FUNCIONALIDADES AUTOMÁTICAS:
        - Cuando el usuario proporciona EMAIL: Se le enviará automáticamente un newsletter personalizado
        - Cuando el usuario proporciona TELÉFONO: Se le enviará automáticamente un mensaje de WhatsApp con info de contacto

        IMPORTANTE: Estas acciones se ejecutan automáticamente. Solo informa al usuario qué recibirá.
        """

        self.prompt_variant_instructions = self._get_prompt_variant_instructions()
        self.sales_playbook = self.estrategia_ventas if self.prompt_variant == "sales" else ""

        # Plantilla principal que combina todas las secciones
        self.system_template = f"""
        {self.personalidad}

        {self.objetivo_principal}

        MODO DE PROMPT ACTIVO:
        {self.prompt_variant_instructions}

        {self.sales_playbook}

        {self.reglas_comportamiento}

        {self.restricciones_tecnicas}

        {self.respuestas_sobre_ti}

        {self.navegacion_sitio}

        {self.funcionalidades_disponibles}

        Contexto de la empresa:
        {{context}}
        """
        
        # Inicializar contadores de mensajes fuera de tema
        self.off_topic_consecutive = {}
        self.max_off_topic_consecutive = MAX_OFF_TOPIC_CONSECUTIVE

        logger.info("Servicio de chat inicializado correctamente")

    def _validate_runtime_configuration(self):
        """Valida y registra la configuración de runtime del chatbot."""
        valid_providers = {"openai", "ollama"}

        if self.model_provider not in valid_providers:
            raise ValueError(f"LLM_PROVIDER inválido: {self.model_provider}")

        if self.embedding_provider not in valid_providers:
            raise ValueError(f"EMBEDDING_PROVIDER inválido: {self.embedding_provider}")

        if self.model_provider == "openai" and not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY es obligatoria cuando LLM_PROVIDER=openai")

        if self.embedding_provider == "openai" and not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY es obligatoria cuando EMBEDDING_PROVIDER=openai")

        if self.prompt_variant not in {"baseline", "sales", "strict"}:
            logger.warning(
                "PROMPT_VARIANT='%s' no reconocida. Se usar\u00e1 'sales'.",
                self.prompt_variant,
            )
            self.prompt_variant = "sales"

        logger.info(
            "Runtime chatbot: llm=%s/%s embeddings=%s/%s prompt=%s dataset=%s",
            self.model_provider,
            self.model_name,
            self.embedding_provider,
            self.embedding_model_name,
            self.prompt_variant,
            self.dataset_path,
        )

    def _get_prompt_variant_instructions(self):
        variants = {
            "baseline": """
            - Priorizá responder preguntas frecuentes del dominio con claridad y brevedad.
            - No empujes una conversación comercial si el usuario solo busca información.
            - Si la consulta es ambigua, pedí una aclaración concreta.
            - Si la pregunta pide un dato técnico o comercial, incluí el valor numérico exacto disponible en el contexto.
            """,
            "sales": """
            - Además de informar, buscá conectar cada respuesta con beneficios prácticos del vehículo o servicio.
            - Si detectás interés real de compra, podés invitar a dejar un medio de contacto.
            - Mantené un tono comercial moderado, sin inventar datos ni presionar.
            - Si la pregunta pide un dato técnico o comercial, incluí el valor numérico exacto disponible en el contexto.
            """,
            "strict": """
            - Respondé únicamente con información respaldada por el contexto recuperado.
            - Si el contexto no alcanza, decilo explícitamente y evita completar con supuestos.
            - Priorizá precisión factual por sobre persuasión comercial.
            - Si la consulta menciona un modelo puntual, priorizá datos específicos de ese modelo por encima de respuestas generales.
            - Si la pregunta pide autonomía, carga, precio, velocidad, capacidad o garantía, incluí los valores numéricos exactos del contexto.
            - No inventes URLs ni rutas web; solo mencionalas si aparecen literalmente en el contexto.
            """,
        }
        return variants[self.prompt_variant]

    def _create_llm(self):
        """Construye el modelo de lenguaje según la configuración activa."""
        if self.model_provider == "ollama":
            return ChatOllama(
                model=self.model_name,
                temperature=self.model_temperature,
                base_url=self.ollama_base_url,
            )

        return ChatOpenAI(model_name=self.model_name, temperature=self.model_temperature)

    def _create_embeddings(self):
        """Construye el modelo de embeddings según la configuración activa."""
        if self.embedding_provider == "ollama":
            return OllamaEmbeddings(
                model=self.embedding_model_name,
                base_url=self.ollama_base_url,
            )

        return OpenAIEmbeddings(model=self.embedding_model_name)

    def _get_vectorstore_directory(self):
        safe_model_name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", self.embedding_model_name)
        return self.vectorstore_base_dir / f"{self.embedding_provider}_{safe_model_name}"

    def _load_knowledge_texts(self):
        """Carga documentos listos para indexar; usa dataset preprocesado si existe."""
        if self.dataset_path.exists():
            texts = []
            metadatas = []

            with self.dataset_path.open("r", encoding="utf-8") as dataset_file:
                for line in dataset_file:
                    line = line.strip()
                    if not line:
                        continue

                    record = json.loads(line)
                    content = record.get("content", "").strip()
                    if not content:
                        continue

                    texts.append(content)
                    metadatas.append(
                        {
                            "id": str(record.get("id", ""))[:200],
                            "section": str(record.get("section", ""))[:200],
                            "title": str(record.get("title", ""))[:500],
                            "source_path": str(record.get("source_path", ""))[:500],
                        }
                    )

            if texts:
                logger.info("Se cargaron %s documentos desde %s", len(texts), self.dataset_path)
                return texts, metadatas

            logger.warning("El dataset preprocesado %s está vacío. Se usará el JSON crudo.", self.dataset_path)

        if not self.raw_dataset_path.exists():
            raise FileNotFoundError(f"No se encontró el dataset de entrada: {self.raw_dataset_path}")

        with self.raw_dataset_path.open("r", encoding="utf-8") as raw_dataset_file:
            info = json.load(raw_dataset_file)

        splitter = RecursiveJsonSplitter(max_chunk_size=800, min_chunk_size=150)
        chunks = splitter.split_text(info, convert_lists=True)
        metadatas = [{"section": "raw_json", "title": "dataset_movilidad.json"} for _ in chunks]
        logger.info("Se generaron %s chunks desde el JSON crudo", len(chunks))
        return chunks, metadatas

    def _normalize_search_text(self, value):
        text = str(value).lower()
        replacements = str.maketrans(
            {
                "á": "a",
                "é": "e",
                "í": "i",
                "ó": "o",
                "ú": "u",
                "ü": "u",
                "ñ": "n",
            }
        )
        text = text.translate(replacements)
        return re.sub(r"[^a-z0-9]+", " ", text).strip()

    def _keyword_search(self, question, limit=3):
        normalized_question = self._normalize_search_text(question)
        query_terms = self._extract_query_terms(normalized_question)
        if not query_terms:
            return []

        ranked = []
        for text, metadata in zip(self.knowledge_texts, self.knowledge_metadatas):
            title = metadata.get("title", "")
            haystack = self._normalize_search_text(f"{title} {text}")
            score = 0

            for term in query_terms:
                if term in self._normalize_search_text(title):
                    score += 4
                if term in haystack:
                    score += 1

            if score > 0:
                ranked.append((score, title, text))

        ranked.sort(key=lambda item: item[0], reverse=True)
        return ranked[:limit]

    def _extract_query_terms(self, normalized_question):
        return [
            term
            for term in normalized_question.split()
            if len(term) > 2 or any(character.isdigit() for character in term)
        ]

    def _get_focus_terms(self, question):
        normalized_question = self._normalize_search_text(question)
        focus_mapping = {
            "autonomia": ["autonomia"],
            "carga": ["carga", "enchufe", "220v", "tiempo", "horas", "20a"],
            "precio": ["precio", "usd", "cuesta", "valor"],
            "capacidad": ["capacidad", "personas", "kg", "carga"],
            "velocidad": ["velocidad", "km h"],
            "garantia": ["garantia", "ano"],
            "agencia": ["agencia", "direccion", "ciudad", "provincia"],
            "telefono": ["telefono", "email", "contacto", "reclamo", "servicio"],
            "leasing": ["leasing", "alquiler", "suspendida"],
            "discapacidad": ["discapacidad", "franquicia", "ley", "rehabilitacion"],
            "reserva": ["reserva", "entrega", "72", "usd", "anticipo"],
        }

        focus_terms = []
        for trigger, terms in focus_mapping.items():
            if trigger in normalized_question:
                focus_terms.extend(terms)

        return list(dict.fromkeys(focus_terms))

    def _extract_relevant_lines(self, question, title, text):
        normalized_question = self._normalize_search_text(question)
        query_terms = self._extract_query_terms(normalized_question)
        focus_terms = self._get_focus_terms(question)
        title_text = f"title: {title}".strip()
        candidate_lines = [title_text] + [line.strip() for line in text.splitlines() if line.strip()]

        scored_lines = []
        for line in candidate_lines:
            normalized_line = self._normalize_search_text(line)
            score = 0

            if line.lower().startswith("respuesta:"):
                score += 3

            for term in query_terms:
                if term in normalized_line:
                    score += 2 if any(character.isdigit() for character in term) else 1

            for term in focus_terms:
                if term in normalized_line:
                    score += 4

            if focus_terms and not any(term in normalized_line for term in focus_terms):
                score -= 2

            if score > 0:
                scored_lines.append((score, line))

        scored_lines.sort(key=lambda item: item[0], reverse=True)
        selected_lines = []
        seen_lines = set()

        for _, line in scored_lines:
            clean_line = line.removeprefix("Respuesta:").strip()
            if clean_line.lower().startswith("title:"):
                continue
            if clean_line in seen_lines:
                continue
            seen_lines.add(clean_line)
            selected_lines.append(clean_line)
            if len(selected_lines) >= 4:
                break

        for focus_term in focus_terms:
            if any(focus_term in self._normalize_search_text(line) for line in selected_lines):
                continue

            for _, line in scored_lines:
                clean_line = line.removeprefix("Respuesta:").strip()
                if clean_line.lower().startswith("title:"):
                    continue
                if clean_line in seen_lines:
                    continue
                if focus_term in self._normalize_search_text(clean_line):
                    seen_lines.add(clean_line)
                    selected_lines.append(clean_line)
                    break

        return selected_lines

    def _build_extractive_response(self, question):
        ranked_documents = self._keyword_search(question, limit=3)
        if not ranked_documents:
            return None

        focus_terms = self._get_focus_terms(question)
        ranked_documents = sorted(
            ranked_documents,
            key=lambda item: (
                sum(
                    5
                    for term in focus_terms
                    if term in self._normalize_search_text(item[1])
                ),
                item[0],
            ),
            reverse=True,
        )

        extracted_lines = []
        for score, title, text in ranked_documents:
            if score < 3:
                continue

            extracted_lines.extend(self._extract_relevant_lines(question, title, text))
            if len(extracted_lines) >= 4:
                break

        if not extracted_lines:
            return None

        return self._sanitize_response_text("\n".join(extracted_lines[:4]))

    def _sanitize_response_text(self, text):
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\2", text)
        text = re.sub(r"^\s*[*-]\s+", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
        text = text.replace("**", "").replace("__", "")
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def can_send_whatsapp_by_ip(self, user_ip):
        """
        Verifica si una IP puede enviar WhatsApp según el rate limiting
        
        Args:
            user_ip: IP del usuario
            
        Returns:
            bool: True si puede enviar, False si alcanzó el límite
        """
        if not user_ip:
            return True  # Si no hay IP, permitir (fallback)
            
        now = datetime.now()
        
        if user_ip in self.whatsapp_sent_by_ip:
            data = self.whatsapp_sent_by_ip[user_ip]
            
            # Verificar si pasó el tiempo límite (3 días)
            time_diff = (now - data["last_sent"]).total_seconds()
            hours_passed = time_diff / 3600
            
            if hours_passed >= self.whatsapp_limit_hours:
                # Resetear contador después de 3 días
                logger.info(f"Reseteando contador WhatsApp para IP {user_ip} (pasaron {hours_passed:.1f} horas)")
                self.whatsapp_sent_by_ip[user_ip] = {"count": 0, "last_sent": now}
                return True
            
            # Verificar si ya alcanzó el límite
            if data["count"] >= self.whatsapp_limit_per_ip:
                logger.warning(f"IP {user_ip} alcanzó límite de WhatsApp ({data['count']}/{self.whatsapp_limit_per_ip})")
                return False
        
        return True

    def update_whatsapp_count_by_ip(self, user_ip):
        """
        Actualiza el contador de WhatsApp enviados para una IP
        
        Args:
            user_ip: IP del usuario
        """
        if not user_ip:
            return
            
        now = datetime.now()
        
        if user_ip in self.whatsapp_sent_by_ip:
            self.whatsapp_sent_by_ip[user_ip]["count"] += 1
            self.whatsapp_sent_by_ip[user_ip]["last_sent"] = now
        else:
            self.whatsapp_sent_by_ip[user_ip] = {"count": 1, "last_sent": now}
            
        logger.info(f"WhatsApp enviado a IP {user_ip}. Contador: {self.whatsapp_sent_by_ip[user_ip]['count']}/{self.whatsapp_limit_per_ip}")

    def get_whatsapp_status_by_ip(self, user_ip):
        """
        Obtiene el estado actual del rate limiting para una IP
        
        Args:
            user_ip: IP del usuario
            
        Returns:
            dict: {"count": int, "can_send": bool, "hours_remaining": float}
        """
        if not user_ip or user_ip not in self.whatsapp_sent_by_ip:
            return {"count": 0, "can_send": True, "hours_remaining": 0}
            
        data = self.whatsapp_sent_by_ip[user_ip]
        now = datetime.now()
        time_diff = (now - data["last_sent"]).total_seconds()
        hours_passed = time_diff / 3600
        hours_remaining = max(0, self.whatsapp_limit_hours - hours_passed)
        
        return {
            "count": data["count"],
            "can_send": self.can_send_whatsapp_by_ip(user_ip),
            "hours_remaining": hours_remaining
        }

    def _crear_o_cargar_vectorstore(self):
        """Crea o carga la base de datos vectorial según el proveedor de embeddings."""
        directorio = self._get_vectorstore_directory()
        directorio.mkdir(parents=True, exist_ok=True)

        if any(directorio.iterdir()):
            logger.info("Cargando base de datos vectorial existente desde %s", directorio)
            return Chroma(
                persist_directory=str(directorio),
                embedding_function=self.embeddings,
            )

        logger.info("Creando nueva base de datos vectorial en %s", directorio)
        vectorstore = Chroma.from_texts(
            texts=self.knowledge_texts,
            metadatas=self.knowledge_metadatas,
            embedding=self.embeddings,
            persist_directory=str(directorio),
        )

        vectorstore.persist()
        logger.info("Base de datos vectorial guardada en %s", directorio)
        return vectorstore

    def _obtener_contexto_relevante(self, question, k=None):
        """Obtiene el contexto relevante para una pregunta."""
        resultados = self.vectorstore.similarity_search(question, k=k or self.retrieval_k)
        resultados_keyword = self._keyword_search(question, limit=3)
        fragmentos = []
        vistos = set()
        max_fragmentos = 5
        max_keyword_fragmentos = 2

        for position, (_, titulo, texto) in enumerate(resultados_keyword, start=1):
            if position > max_keyword_fragmentos:
                break
            key = (titulo, texto)
            if key in vistos:
                continue
            vistos.add(key)
            fragmentos.append(f"{titulo}\n{texto}" if titulo else texto)
            if len(fragmentos) >= max_fragmentos:
                return "\n\n".join(fragmentos)

        for doc in resultados:
            titulo = doc.metadata.get("title") if doc.metadata else None
            key = (titulo or "", doc.page_content)
            if key in vistos:
                continue
            vistos.add(key)
            if titulo:
                fragmentos.append(f"{titulo}\n{doc.page_content}")
            else:
                fragmentos.append(doc.page_content)
            if len(fragmentos) >= max_fragmentos:
                break

        return "\n\n".join(fragmentos)
    
    def _get_user_memory(self, user_id="default"):
        """Obtiene o crea la memoria para un usuario específico"""
        if user_id not in self.memories:
            self.memories[user_id] = ConversationBufferWindowMemory(
                k=7,
                return_messages=True,
                memory_key="chat_history"
            )
        return self.memories[user_id]
    
    def reformular_consulta_prompt(self, pregunta_actual, historial_conversacion):
        return f"""
        Eres un asistente especializado en entender consultas dentro de un contexto conversacional.
        
        ## Historial de conversación:
        {historial_conversacion}
        
        ## Pregunta actual del usuario:
        "{pregunta_actual}"
        
        ## Tu tarea:
        Reformula la pregunta actual en una consulta completa, explícita y específica para un sistema de recuperación de información sobre CORADIR S.A.
        
        - La consulta reformulada debe capturar la intención real del usuario
        - Debe incluir todo el contexto relevante del historial
        - Debe ser específica sobre el producto, servicio o información que se solicita de CORADIR
        - No debes responder la pregunta, solo reformularla de manera más completa
        
        Devuelve solo la consulta reformulada sin explicaciones adicionales.
        """

    async def _is_off_topic(self, question, chat_history):
        system_prompt = """
        Eres un detector de relevancia para un chatbot sobre CORADIR, una empresa que vende 
        vehículos eléctricos como TITO, TITA, TITA CUADRILLA, BARRE-TITA, CHIKI y servicios relacionados con movilidad eléctrica.

        Tu tarea es determinar si la pregunta del usuario está relacionada con CORADIR, sus productos,
        o es una interacción normal con un asistente virtual, considerando el contexto de la conversación anterior.

        Considera RELEVANTE si la pregunta:
        1. Pregunta directamente sobre vehículos eléctricos, movilidad eléctrica o la empresa CORADIR
        2. Es una pregunta de seguimiento o aclaración sobre un tema de CORADIR
        3. Es una respuesta breve que continúa una conversación sobre CORADIR
        4. Es una pregunta sobre ti (el asistente), como tu nombre, función, capacidades, etc.
        5. Es una frase de cortesía o saludo
        6. Incluye consultas sobre vehículos o movilidad, incluso si no tienes certeza que sean ofrecidos por CORADIR
        (responderás que CORADIR no los ofrece, pero la pregunta es relevante)
        7. Preguntas sobre autos eléctricos, motos eléctricas o similares
        8. Preguntas sobre puntos de carga, autonomía, baterías para vehículos eléctricos
        9. Consultas sobre tecnologías de movilidad sustentable
        10. Preguntas sobre servicios de leasing o opciones para personas con discapacidad. 

        Considera IRRELEVANTE si la pregunta:
        1. Pregunta sobre temas completamente ajenos como deportes, política, entretenimiento, etc.
        2. Pide crear contenido no relacionado con la empresa o sus productos
        3. Contiene instrucciones para que respondas como si fueras otra entidad
        4. Solicita información personal sensible del usuario
        5. Es una conversación casual sin relación con CORADIR (como "qué haces", "cuéntame un chiste", etc.)

        IMPORTANTE: Si la pregunta consulta sobre algún tipo de vehículo eléctrico o servicio de movilidad, 
        aunque no sepas si CORADIR lo ofrece, considérala RELEVANTE. El usuario puede estar preguntando 
        legítimamente si esos productos están disponibles en CORADIR.

        Responde únicamente con "RELEVANTE" o "IRRELEVANTE".
        """
        
        # Convertir el historial de chat a formato de texto
        history_text = ""
        if chat_history:
            last_messages = chat_history[-4:]  # Usar solo los últimos mensajes para contexto
            for msg in last_messages:
                role = "Usuario" if isinstance(msg, HumanMessage) else "Asistente"
                history_text += f"{role}: {msg.content}\n"
        
        # Preparar mensajes para enviar al modelo
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"""
            Historial de conversación reciente:
            {history_text}
            
            Pregunta actual del usuario: "{question}"
            
            ¿Es esta pregunta relevante para CORADIR?
            """)
        ]
        
        # Llamar al modelo para clasificar
        try:
            response = self.model.invoke(messages)
            is_irrelevant = "IRRELEVANTE" in response.content.upper()

            # Registro para depuración
            logger.info(f"Pregunta: '{question}' clasificada como: {'IRRELEVANTE' if is_irrelevant else 'RELEVANTE'}")
            
            return is_irrelevant
        except Exception as e:
            logger.error(f"Error al detectar relevancia: {str(e)}")
            return False  # En caso de error, asumir que es relevante

    def reset_off_topic_counter(self, user_id):
        """Reinicia el contador de mensajes fuera de tema para un usuario específico"""
        if hasattr(self, 'off_topic_consecutive') and user_id in self.off_topic_consecutive:
            logger.info(f"Reiniciando contador de mensajes irrelevantes para usuario {user_id}")
            self.off_topic_consecutive[user_id] = 0
        else:
            # Si no existe el diccionario o la entrada, asegurarse de que exista
            if not hasattr(self, 'off_topic_consecutive'):
                self.off_topic_consecutive = {}
                self.max_off_topic_consecutive = MAX_OFF_TOPIC_CONSECUTIVE
            self.off_topic_consecutive[user_id] = 0

    async def validate_email(self, email):
        """Valida y opcionalmente corrige un correo electrónico usando el modelo"""
        prompt = f"""
        Verifica si este correo electrónico parece válido: {email}
        
        Si parece válido, devuelve exactamente: VALID:{email}
        Si parece tener errores pero puedes corregirlo con confianza, devuelve: CORRECTED:correo_corregido
        Si parece completamente inválido, devuelve: INVALID
        
        Responde solo con uno de estos tres formatos, sin explicaciones adicionales.
        """
        
        try:
            response = self.model.invoke([SystemMessage(content="Eres un validador de correos electrónicos"), 
                                        HumanMessage(content=prompt)])
            result = response.content.strip()
            
            if result.startswith("VALID:"):
                return True, email, None
            elif result.startswith("CORRECTED:"):
                corrected = result.split(":", 1)[1]
                return True, corrected, f"Noté que había un pequeño error en tu correo. Lo he corregido a {corrected}."
            else:
                return False, None, "Parece que el correo proporcionado no es válido. Por favor, proporciona una dirección de correo electrónico válida."
        except Exception as e:
            logger.error(f"Error validando email: {str(e)}")
            # En caso de error, asumir que es válido tal como está
            return True, email, None

    async def validate_phone(self, phone):
        """Valida y limpia un número de teléfono usando IA"""
        
        # LOG DE DEBUG
        logger.info(f"🔍 Validando teléfono: '{phone}'")
        
        # En chat_service.py, solo cambiar esta parte del prompt:

        prompt = f"""
        Analiza si este texto es un número de teléfono válido: "{phone}"

        Si el número es válido, aunque tenga espacios, guiones, paréntesis, etc, limpiá el formato y respondé: VALID:número_limpio  
        Si el número no es válido, respondé: INVALID

        REGLAS para limpiar:
        - Solo quita espacios, guiones, paréntesis
        - Mantén el signo + si está presente
        - Nunca agregues o modifiques dígitos

        FORMATOS VÁLIDOS PARA ARGENTINA:
        1. 10 dígitos: código de área + número local
        2. +54 + 10 dígitos: código país + código de área + número local  
        3. +549 + 10 dígitos: código país + 9 + código de área + número local

        IMPORTANTE:
        - Cualquier número que contenga exactamente 10 dígitos, aunque estén separados, es VÁLIDO
        - Cualquier número que empiece con +54 y tenga luego 10 dígitos también es VÁLIDO
        - Si el número solo necesita limpieza de espacios o guiones, es VÁLIDO
        - Si el número no cumple con esas condiciones, respondé INVALID.

        Ejemplos VÁLIDOS:
        - "2664585117" → VALID:2664585117 (10 dígitos)
        - "1159191576" → VALID:1159191576 (10 dígitos)
        - "11 6971 3298" → VALID:1169713298 (10 dígitos con espacios)
        - "+543484330609" → VALID:+543484330609 (código país + 10 dígitos) 
        - "+5491159191576" → VALID:+5491159191576 (código país + 9 + 10 dígitos)
        - "2664-585117" → VALID:2664585117 (10 dígitos con guión)
        - "2314 465996" → VALID:2314465996 (10 dígitos con espacios)
        - "(226) 4451217" → VALID:2264585117 (con paréntesis)

        Ejemplos INVÁLIDOS:
        - "año 2024" → INVALID (contiene texto)
        - "12:30" → INVALID (formato hora)
        - "123456" → INVALID (muy corto, solo 6 dígitos)
        - "26645851173" (tiene más de 10 dígitos)

        REGLA CLAVE: Si ves "+543484330609", esto es VÁLIDO porque:
        - Tiene +54 (código Argentina)
        - Seguido de 3484330609 (10 dígitos de teléfono argentino)
        - Total: formato correcto argentino
        """
        
        try:
            response = self.model.invoke([
                SystemMessage(content="Eres un validador de números de teléfono argentinos"), 
                HumanMessage(content=prompt)
            ])
            
            result = response.content.strip()
            
            # LOG DE DEBUG
            logger.info(f"🔍 Respuesta de IA para teléfono: '{result}'")
            
            if result.startswith("VALID:"):
                clean_phone = result.split(":", 1)[1]
                logger.info(f"✅ Teléfono validado: '{clean_phone}'")
                return True, clean_phone, None
            else:
                logger.warning(f"❌ Teléfono inválido según IA: '{result}'")
                return False, None, "No se pudo detectar un teléfono válido."
                
        except Exception as e: # Algo mas manual en caso de que falle el modelo
            logger.error(f"❌ Error validando teléfono: {str(e)}")
            # En caso de error, intentar limpieza manual básica
            clean_phone = re.sub(r'[\s\-\(\)]', '', phone.strip())
            if len(clean_phone) >= 8 and clean_phone.replace('+', '').isdigit():
                logger.info(f"✅ Teléfono validado manualmente: '{clean_phone}'")
                return True, clean_phone, None
            else:
                logger.warning(f"❌ Teléfono inválido manualmente: '{clean_phone}'")
                return False, None, "No se pudo validar el teléfono."

    async def validate_name(self, text):
        """Detecta y valida nombres en el texto del usuario"""
        prompt = f"""
        Analiza si en este texto el usuario menciona su nombre de forma natural: "{text}"
        
        Si detectas un nombre propio (no apellido, no empresa), responde: NAME:nombre_detectado
        Si no hay un nombre claro, responde: NO_NAME
        
        IMPORTANTE: NO detectes como nombres de usuario los siguientes términos que son nombres de vehiculos electricos o del chatbot:
        - TITO, TITA, TITA CUADRILLA, BARRE-TITA, CHIKI (nombres de vehículos eléctricos)
        - Cora (nombre del chatbot)
        - Coradir (nombre de la empresa)
        - Cualquier referencia a productos, marcas o servicios
        
        Ejemplos CORRECTOS:
        - "Hola, soy María" → NAME:María
        - "Mi nombre es Juan Carlos" → NAME:Juan Carlos  
        - "Me presento, soy Ana" → NAME:Ana
        - "Mariano" → NAME:Mariano
        
        Ejemplos INCORRECTOS (responder NO_NAME):
        - "Quiero información sobre TITO" → NO_NAME
        - "El TITA me interesa" → NO_NAME
        - "Hola Cora" → NO_NAME
        - "Soy de la empresa Lopez" → NO_NAME
        - "Me llamo Dr. Rodriguez" → NO_NAME
        - "Trabajo en Coradir" → NO_NAME
        - "Estoy interesado en CHIKI" → NO_NAME
        """
        
        try:
            response = self.model.invoke([
                SystemMessage(content="Eres un detector de nombres propios"),
                HumanMessage(content=prompt)
            ])
            
            result = response.content.strip()
            if result.startswith("NAME:"):
                name = result.split(":", 1)[1].strip()
                return True, name
            return False, None
            
        except Exception as e:
            logger.error(f"Error detectando nombre: {str(e)}")
            return False, None

    async def validate_contact(self, contact_text):
        """Detecta y valida si es email o teléfono"""
        
        # Regex más robusta para emails (permite espacios accidentales)
        email_pattern = r'[a-zA-Z0-9._%+-]+\s*@\s*[a-zA-Z0-9.-]+\s*\.\s*[a-zA-Z]{2,}'
        email_match = re.search(email_pattern, contact_text)
        
        if email_match:
            email = email_match.group(0)
            is_valid, validated_email, message = await self.validate_email(email)
            return "email", validated_email if is_valid else None, message
        
        # Regex para teléfonos (buscar patrones que parezcan teléfono)
        phone_pattern = r'\+?[\d\s\-\(\)]{8,20}'
        phone_match = re.search(phone_pattern, contact_text)
        
        if phone_match:
            phone = phone_match.group(0).strip()
            is_valid, validated_phone, message = await self.validate_phone(phone)
            return "phone", validated_phone if is_valid else None, message
        
        return None, None, "No se pudo detectar un email o teléfono válido."

    def _get_conversation_data(self, user_id: str) -> Dict[str, Any]:
        """
        Obtiene los datos completos de la conversación para enviar a n8n
        
        Args:
            user_id: ID del usuario
            
        Returns:
            Dict con datos de la conversación
        """
        try:
            # Importar aquí para evitar circular imports
            from langchain_core.messages import HumanMessage, AIMessage
            
            memory = self._get_user_memory(user_id)
            chat_history = memory.load_memory_variables({})["chat_history"]
            
            # Convertir historial a formato simple para n8n
            full_conversation = []
            for msg in chat_history:
                if hasattr(msg, 'content'):
                    role = "user" if isinstance(msg, HumanMessage) else "bot"
                    full_conversation.append({
                        "role": role,
                        "message": msg.content,
                        "timestamp": datetime.now().isoformat()  # Aproximado
                    })
            
            logger.info(f"Conversación obtenida para {user_id}: {len(full_conversation)} mensajes")
            
            return {
                "full_conversation": full_conversation,
                "total_messages": len(full_conversation),
                "conversation_start": datetime.now().isoformat(),  # Aproximado
                "last_interaction": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error obteniendo datos de conversación para {user_id}: {str(e)}")
            return {
                "full_conversation": [],
                "total_messages": 0,
                "error": f"No se pudo obtener historial de conversación: {str(e)}"
            }

    async def trigger_webhook(self, action_type: str, user_id: str, contact_data: Dict[str, str]):
        """
        Función unificada para disparar webhooks
        
        Args:
            action_type: "send_email_newsletter" o "send_whatsapp"
            user_id: ID del usuario
            contact_data: Dict con email/phone/name según corresponda
        """
        try:
            # Preparar datos del usuario
            user_data = {
                "user_id": user_id,
                "client_id": user_id,
                "email": contact_data.get("email"),
                "phone": contact_data.get("phone"), 
                "name": contact_data.get("name", "Usuario"),
                "timestamp": datetime.now().isoformat()
            }
            
            # Obtener conversación completa
            conversation_data = self._get_conversation_data(user_id)
            
            # Enviar webhook unificado
            webhook_sent = await self.webhook_service.send_webhook(
                action_type=action_type,
                user_data=user_data,
                conversation_data=conversation_data
            )
            
            if webhook_sent:
                logger.info(f"Webhook {action_type} enviado exitosamente para usuario {user_id}")
            else:
                logger.warning(f"No se pudo enviar webhook {action_type} para usuario {user_id}")
                
        except Exception as e:
            logger.error(f"Error enviando webhook {action_type}: {str(e)}")

    # Funciones específicas simplificadas
    async def trigger_email_webhook(self, user_id: str, email: str, name: str = None):
        """Dispara webhook para email newsletter"""
        await self.trigger_webhook(
            action_type="send_email_newsletter",
            user_id=user_id,
            contact_data={"email": email, "name": name}
        )

    async def trigger_whatsapp_webhook(self, user_id: str, phone: str, name: str = None):
        """Dispara webhook para WhatsApp"""
        await self.trigger_webhook(
            action_type="send_whatsapp", 
            user_id=user_id,
            contact_data={"phone": phone, "name": name}
        )

    async def process_message(self, question, user_id="default", user_ip=None):
        """Procesa un mensaje del usuario y devuelve la respuesta"""
        try:
            # Variables para controlar webhooks (se resetean en cada llamada)
            send_email_webhook = False
            send_whatsapp_webhook = False
            webhook_email = None
            webhook_phone = None
            detected_name = None
            rate_limit_message = None
            
            # Obtener IP del usuario para rate limiting
            real_user_ip = user_ip or "unknown"
            logger.info(f"Procesando mensaje de usuario {user_id} desde IP {real_user_ip}")

            # Verificación de preguntas irrelevantes
            # Inicializar el contador si no existe
            if not hasattr(self, 'off_topic_consecutive'):
                self.off_topic_consecutive = {}
                self.max_off_topic_consecutive = MAX_OFF_TOPIC_CONSECUTIVE

            # Obtener la memoria del usuario
            memory = self._get_user_memory(user_id)
            
            # Cargar el historial de chat
            chat_history = memory.load_memory_variables({})["chat_history"]

            # Verificar si la pregunta está fuera de tema
            is_off_topic = await self._is_off_topic(question, chat_history)
            logger.info(f"La pregunta es fuera de tema: {is_off_topic}")

            warning_message = ""

            # Manejar el contador de preguntas fuera de tema
            if is_off_topic:
                if user_id not in self.off_topic_consecutive:
                    self.off_topic_consecutive[user_id] = 1
                else:
                    self.off_topic_consecutive[user_id] += 1
                    
                # Verificar si ha excedido el límite
                if self.off_topic_consecutive[user_id] >= self.max_off_topic_consecutive:
                    # Señal para cerrar la sesión
                    return "SESSION_TERMINATE||Lo sentimos, este chat está diseñado para responder preguntas sobre CORADIR y sus productos. Tu sesión será reiniciada."
                # Advertencia cuando llega a 2 o 3 preguntas irrelevantes
                elif self.off_topic_consecutive[user_id] >= 5:
                    warning_message = "Por favor ten en cuenta que este asistente está diseñado específicamente para responder preguntas sobre CORADIR MOVILIDAD. Si continúas con preguntas no relacionadas, la sesión podría finalizar.\n\n"
                    return warning_message
            else:
                # Reiniciar contador si la pregunta es relevante
                self.off_topic_consecutive[user_id] = 0
            
            respuesta_texto = self._build_extractive_response(question)

            if not respuesta_texto:
                # Reformular la consulta usando el LLM si hay historial previo
                consulta_mejorada = question
                if len(chat_history) > 0:
                    try:
                        historial_texto = "\n".join([f"{'Usuario' if isinstance(msg, HumanMessage) else 'Asistente'}: {msg.content}" 
                                        for msg in chat_history[-4:]])  # Usar los últimos 4 mensajes
                        
                        prompt_reformulacion = self.reformular_consulta_prompt(question, historial_texto)
                        
                        chain = self.model.invoke([SystemMessage(content=prompt_reformulacion)])
                        consulta_mejorada = chain.content.strip()
                        
                        logger.info(f"Consulta original: {question}")
                        logger.info(f"Consulta reformulada: {consulta_mejorada}")
                    except Exception as e:
                        logger.error(f"Error en reformulación de consulta: {str(e)}")
                        # Si hay error en la reformulación, usamos la consulta original
                        consulta_mejorada = question
                
                # Obtener contexto relevante
                contexto_relevante = self._obtener_contexto_relevante(consulta_mejorada)
                
                # Crear la plantilla de prompt
                prompt = ChatPromptTemplate.from_messages([
                    SystemMessagePromptTemplate.from_template(self.system_template),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{question}")
                ])
                
                # Crear la cadena de procesamiento
                chain = prompt | self.model
                
                # Preparar los datos de entrada
                chain_input = {
                    "context": contexto_relevante,
                    "question": question,
                    "chat_history": chat_history
                }
                
                # Ejecutamos el procesamiento de forma asíncrona
                loop = asyncio.get_event_loop()
                respuesta = await loop.run_in_executor(
                    None, 
                    lambda: chain.invoke(chain_input)
                )
                respuesta_texto = self._sanitize_response_text(respuesta.content)

            # Verificar si el mensaje del usuario contiene un email o teléfono
            # Regex más robusta que permite espacios accidentales
            email_pattern = r'[a-zA-Z0-9._%+-]+\s*@\s*[a-zA-Z0-9.-]+\s*\.\s*[a-zA-Z]{2,}'
            phone_pattern = r'\+?[\d\s\-\(\)]{8,20}'
            contact_pattern = rf'{email_pattern}|{phone_pattern}'
            contact_match = re.search(contact_pattern, question)

            # Detectar nombre en el mensaje del usuario
            has_name, detected_name = await self.validate_name(question)
            if has_name:
                db = SessionLocal()
                try:
                    update_user_info(db, user_id, name=detected_name)
                    logger.info(f"Nombre detectado para usuario {user_id}: {detected_name}")
                finally:
                    db.close()
            
            if contact_match:
                contact_text = contact_match.group(0)
                logger.info(f"Contacto detectado en mensaje del usuario: {contact_text}")
                
                # Detectar y validar el tipo de contacto
                contact_type, validated_contact, validation_message = await self.validate_contact(contact_text)
                
                if contact_type and validated_contact:
                    # Guardar en BD según el tipo
                    db = SessionLocal()
                    try:
                        if contact_type == "email":
                            update_user_info(db, user_id, email=validated_contact)
                            logger.info(f"Email guardado para usuario {user_id}: {validated_contact}")

                            # SETEAR FLAG en lugar de enviar webhook inmediatamente
                            send_email_webhook = True
                            webhook_email = validated_contact

                        elif contact_type == "phone":
                            # VERIFICAR RATE LIMITING POR IP ANTES DE PROCESAR
                            if not self.can_send_whatsapp_by_ip(real_user_ip):
                                # IP alcanzó el límite - NO guardar en BD ni enviar WhatsApp
                                logger.warning(f"IP {real_user_ip} bloqueada por rate limit WhatsApp")
                                
                                # Variable separada para el mensaje de rate limiting
                                rate_limit_message = "Tu información de contacto ya fue registrada correctamente y llegará a nuestro equipo de ventas."
                                
                            else:
                                # PERMITIDO: guardar en BD y enviar WhatsApp
                                update_user_info(db, user_id, phone=validated_contact)
                                logger.info(f"Teléfono guardado para usuario {user_id}: {validated_contact}")

                                # SETEAR FLAG en lugar de enviar webhook inmediatamente
                                send_whatsapp_webhook = True
                                webhook_phone = validated_contact
                                
                                # ACTUALIZAR CONTADOR DE RATE LIMITING
                                self.update_whatsapp_count_by_ip(real_user_ip)

                    finally:
                        db.close()
                    
                    # Construir respuesta final con validation_message y rate_limit_message
                    respuesta_base = respuesta_texto
                    mensajes_adicionales = []

                    if validation_message:
                        mensajes_adicionales.append(validation_message)

                    if rate_limit_message:
                        mensajes_adicionales.append(rate_limit_message)

                    if mensajes_adicionales:
                        respuesta_limpia = respuesta_base + "\n\n" + "\n\n".join(mensajes_adicionales)
                    else:
                        respuesta_limpia = respuesta_base
                        
                else:
                    # Si el contacto es inválido, añadir mensaje pidiendo corrección
                    error_msg = validation_message or "No se pudo detectar un contacto válido."
                    respuesta_con_aviso = respuesta_texto + f"\n\n{error_msg}"
                    respuesta_limpia = respuesta_con_aviso
            else:
                # Sin contacto, usar respuesta normal
                respuesta_limpia = respuesta_texto

            # GUARDAR LA CONVERSACIÓN EN MEMORIA (con respuesta final)
            memory.save_context({"input": question}, {"output": respuesta_limpia})

            # AHORA SÍ: Enviar webhooks con conversación completa
            if send_email_webhook:
                await self.trigger_email_webhook(
                    user_id=user_id,
                    email=webhook_email,
                    name=detected_name  # Puede ser None
                )
                logger.info(f"Webhook de email disparado para {user_id} con email {webhook_email}")
                
            if send_whatsapp_webhook:
                await self.trigger_whatsapp_webhook(
                    user_id=user_id,
                    phone=webhook_phone,
                    name=detected_name  # Puede ser None
                )
                logger.info(f"Webhook de WhatsApp disparado para {user_id} con teléfono {webhook_phone} desde IP {real_user_ip}")

            return respuesta_limpia
                
        except Exception as e:
            logger.error(f"Error procesando mensaje: {str(e)}")
            return "Lo siento, ha ocurrido un error al procesar tu mensaje. Por favor, intenta nuevamente."
