# Reporte Final de Implementacion

## 1. Resumen Ejecutivo de la Solucion

El proyecto implementa un chatbot web para responder consultas frecuentes de CORADIR Movilidad Electrica sobre vehiculos, autonomia, carga, precios, agencias, garantias y condiciones comerciales. El objetivo fue transformar la idea inicial de la propuesta en un MVP funcional, reproducible localmente y validado con un benchmark de preguntas del dominio.

La version final adopta un enfoque hibrido:

- base de conocimiento cerrada y curada a partir de `dataset/dataset_movilidad.json`
- preprocesamiento para convertir el JSON original en documentos mas recuperables
- recuperacion por embeddings con `Chroma`
- soporte para modelos open source locales via `Ollama`
- capa extractiva previa al LLM para reducir alucinaciones en preguntas factuales

Esta decision responde directamente al feedback recibido:

- se limpio y reproyecto la base de conocimiento antes de indexarla
- se reemplazo la dependencia obligatoria de OpenAI por una configuracion open source local
- se habilito el uso de variantes de prompt (`baseline`, `sales`, `strict`) para comparar comportamiento

## 2. Arquitectura del Sistema y Tecnologias Utilizadas

La arquitectura final del MVP queda organizada en los siguientes bloques:

1. Interfaz web de chat
   - Archivos en `chat_assets/`
   - Conexion en tiempo real mediante WebSocket

2. Backend de aplicacion
   - `FastAPI` en `api/main.py`
   - Manejo de sesiones, WebSocket, tokenizacion y endpoints de salud

3. Logica conversacional
   - `api/chat_service.py`
   - Memoria corta por usuario
   - Clasificacion de relevancia
   - Recuperacion de contexto
   - Respuesta extractiva y/o generativa

4. Persistencia
   - `SQLite` local por defecto mediante `sqlalchemy`
   - `Chroma` para el indice vectorial

5. Integraciones opcionales
   - `n8n` por webhook para captura de leads
   - flujo de audio existente como extension, no como nucleo del MVP academico

Tecnologias principales:

- `FastAPI`
- `SQLAlchemy`
- `Chroma`
- `LangChain`
- `Ollama`
- `gemma3:1b` como modelo de chat local
- `nomic-embed-text` como modelo de embeddings local

## 3. Datos y Preprocesamiento

### Fuente de datos

La fuente principal del dominio es `dataset/dataset_movilidad.json`, que contiene:

- informacion institucional de CORADIR
- catalogo de vehiculos
- especificaciones tecnicas
- precios actualizados
- infraestructura de carga
- agencias oficiales
- preguntas frecuentes
- datos de contacto

### Problemas detectados

Durante la implementacion se detectaron dos problemas de calidad relevantes:

1. El dataset original estaba en formato JSON jerarquico, util para administracion pero no ideal para recuperacion semantica directa.
2. Parte del contenido presentaba problemas de codificacion de caracteres, por ejemplo textos con mojibake.

### Solucion de preprocesamiento

Se implemento `scripts/prepare_dataset.py`, que:

- lee el dataset original
- corrige problemas de codificacion cuando aparecen
- normaliza espacios y claves
- genera documentos textuales mas pequenos y semanticamente coherentes
- exporta la base resultante a `dataset/knowledge_base_movilidad.jsonl`

Resultado del preprocesamiento:

- 111 documentos indexables para RAG
- un documento por FAQ, ficha tecnica, precio, agencia o subseccion relevante

Nota sobre OCR:

En esta version del MVP no fue necesario aplicar OCR porque la base de conocimiento final usada para el benchmark es textual. De incorporarse fuentes futuras en PDF escaneado, imagenes o catalogos visuales, el pipeline deberia ampliarse con una etapa de OCR previa al indexado.

## 4. Modelo / Logica del Sistema

La logica final no depende de un unico paso generativo. Se implemento un pipeline hibrido:

1. Validacion de configuracion y carga de modelo/embeddings
2. Carga o creacion del indice vectorial en `Chroma`
3. Deteccion de preguntas fuera de dominio
4. Busqueda lexical por palabras clave sobre la base preprocesada
5. Respuesta extractiva para consultas factuales
6. Si la capa extractiva no alcanza, uso de RAG generativo con contexto recuperado
7. Sanitizacion de salida para evitar markdown y reducir ruido

### Decision tecnica clave

El feedback del profesor sugeria evaluar modelos open source para evitar costos. La implementacion final permite dos modos:

- `Ollama` local
- `OpenAI` opcional

Para el MVP se eligio `Ollama + gemma3:1b + nomic-embed-text`, porque:

- evita costo por consulta
- se puede ejecutar sin servicios externos
- hace reproducible la demo en una notebook local

### Variantes de prompt

Se agrego `PROMPT_VARIANT` con tres opciones:

- `baseline`: tono informativo general
- `sales`: tono mas orientado a beneficios comerciales
- `strict`: prioriza precision factual y minimiza inferencias

Esto permitio comparar prompts sobre el mismo benchmark sin cambiar la arquitectura.

## 5. Evaluacion y Validacion

Se construyo una base de validacion en `dataset/evaluacion_mvp.json` con 15 casos representativos del dominio:

- autonomia y carga
- precios
- capacidad de vehiculos
- garantia
- servicio tecnico y reclamos
- leasing
- beneficios por discapacidad
- agencias
- condiciones de reserva y entrega

Se implemento un script de evaluacion reproducible:

- `scripts/run_benchmark.py`

Configuracion usada para la validacion principal:

- `LLM_PROVIDER=ollama`
- `CHAT_MODEL_NAME=gemma3:1b`
- `EMBEDDING_PROVIDER=ollama`
- `EMBEDDING_MODEL_NAME=nomic-embed-text`

Metricas consideradas:

- exactitud por coincidencia de palabras clave esperadas
- latencia promedio por consulta

## 6. Resultados y Analisis

Resultados obtenidos sobre 15 casos:

- `docs/benchmark_sales.json`: 15/15 correctos, exactitud 100.0%, latencia promedio 0.82 s
- `docs/benchmark_strict.json`: 15/15 correctos, exactitud 100.0%, latencia promedio 0.83 s

Analisis:

- Se supero la meta original de la propuesta, que planteaba 80% de precision sobre un set de prueba.
- La latencia promedio tambien quedo por debajo del objetivo de 5 segundos.
- La mejora principal no vino solo del prompt, sino del cambio estructural en el pipeline:
  - preprocesamiento de la base
  - recuperacion mas granular
  - capa extractiva para datos factuales

Conclusion operativa:

- Para una demo academica, `strict` es la variante recomendada porque mantiene la misma exactitud que `sales` pero esta mejor alineada con el alcance original de preguntas frecuentes.

## 7. Limitaciones y Trabajo Futuro

Limitaciones actuales:

- El benchmark esta construido sobre un dominio cerrado y todavia no mide conversaciones reales de usuarios externos.
- El flujo de audio sigue dependiendo de OpenAI y no forma parte del nucleo open source del MVP.
- Persisten warnings tecnicos en librerias de LangChain/Chroma que convendria actualizar en una siguiente iteracion.
- La evaluacion actual prioriza exactitud factual; aun no mide satisfaccion de usuario ni robustez ante consultas ambiguas extensas.

Trabajo futuro recomendado:

- incorporar logs reales anonimizados para una validacion mas amplia
- agregar OCR para futuras fuentes no textuales
- migrar a componentes mas nuevos de `langchain-chroma`
- sumar tests automaticos de regresion para preguntas frecuentes
- conectar formalmente la salida comercial con CRM o automatizaciones si el caso de uso lo requiere

## 8. Guia de Ejecucion y Demo

### Preparacion

1. Instalar dependencias:
   `pip install -r requirements.txt`
2. Copiar `.env.example` a `.env`
3. Descargar modelos locales:
   `ollama pull gemma3:1b`
   `ollama pull nomic-embed-text`
4. Generar la base de conocimiento:
   `python scripts/prepare_dataset.py`

### Ejecucion

1. Levantar la API:
   `python run.py --host 0.0.0.0 --port 8851`
2. Abrir el chat o probar el backend desde el frontend existente

### Demo sugerida

Consultas recomendadas para presentar:

- "¿Cuánta autonomía tiene el TITO S5 y cómo se carga?"
- "¿Cuál es el precio del TITO S5-300 AA?"
- "¿Dónde hago un reclamo o pido servicio técnico?"
- "¿Tienen agencia oficial en San Luis?"
- "¿Cómo funciona la reserva y la entrega inmediata?"

### Reproduccion del benchmark

`python scripts/run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model gemma3:1b --embedding-provider ollama --embedding-model nomic-embed-text`

## 9. Alcance Esperado de la Implementacion (MVP)

### Incluido en el MVP final

- chat web de texto funcional
- backend FastAPI con WebSocket
- base de conocimiento cerrada del dominio
- preprocesamiento reproducible del dataset
- RAG con embeddings locales
- configuracion open source local
- benchmark reproducible para validacion

### Fuera de alcance del MVP academico

- CRM productivo
- orquestacion comercial completa
- flujo de audio open source de punta a punta
- OCR productivo para documentos escaneados
- despliegue cloud multiusuario con observabilidad completa

## Cierre

La implementacion final evidencia la transicion desde una idea conceptual hacia un sistema funcional. El MVP no solo responde consultas del dominio, sino que ademas queda documentado, parametrizado y validado con evidencia empirica reproducible. Desde el punto de vista academico, el proyecto cumple con la guia de implementacion y con las recomendaciones del feedback recibido.
