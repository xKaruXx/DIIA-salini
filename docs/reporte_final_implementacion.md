# Reporte Final de Implementacion

## 1. Resumen Ejecutivo de la Solucion

El proyecto implementa un chatbot web para responder consultas frecuentes de CORADIR Movilidad Electrica sobre vehiculos, autonomia, carga, precios, agencias, garantias y condiciones comerciales. El objetivo consistio en transformar la idea inicial de la propuesta en un MVP funcional, reproducible localmente y validado mediante un benchmark de preguntas del dominio.

La version final adopta un enfoque hibrido compuesto por:

- base de conocimiento cerrada y curada a partir de `dataset/dataset_movilidad.json`
- preprocesamiento del JSON original para convertirlo en documentos mas recuperables
- recuperacion por embeddings con `Chroma`
- soporte para modelos open source locales mediante `Ollama`
- capa extractiva previa al LLM para reducir alucinaciones en preguntas factuales

Esta decision responde a la retroalimentacion recibida durante la evaluacion de la propuesta:

- se limpio y reproyecto la base de conocimiento antes del indexado
- se reemplazo la dependencia obligatoria de OpenAI por una configuracion open source local
- se habilito el uso de variantes de prompt (`baseline`, `sales`, `strict`) para comparar comportamiento sobre el mismo sistema

## 2. Arquitectura del Sistema y Tecnologias Utilizadas

La arquitectura final del MVP se organiza en los siguientes bloques:

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
- `qwen3.5:4b` como modelo de chat local
- `nomic-embed-text:latest` como modelo de embeddings local

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

1. El dataset original estaba en formato JSON jerarquico, util para administracion, pero no ideal para recuperacion semantica directa.
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

En esta version del MVP no fue necesario aplicar OCR porque la base de conocimiento utilizada para el benchmark es textual. En caso de incorporar fuentes futuras en PDF escaneado, imagenes o catalogos visuales, el pipeline deberia ampliarse con una etapa de OCR previa al indexado.

## 4. Modelo / Logica del Sistema

La logica final no depende de un unico paso generativo. Se implemento un pipeline hibrido:

1. Validacion de configuracion y carga de modelo y embeddings
2. Carga o creacion del indice vectorial en `Chroma`
3. Deteccion de preguntas fuera de dominio
4. Busqueda lexical por palabras clave sobre la base preprocesada
5. Respuesta extractiva para consultas factuales
6. Si la capa extractiva no alcanza, uso de RAG generativo con contexto recuperado
7. Sanitizacion de salida para evitar markdown y reducir ruido

### Decision tecnica clave

La retroalimentacion recibida sugirio evaluar modelos open source para evitar costos. La implementacion final permite dos modos de ejecucion:

- `Ollama` local
- `OpenAI` opcional

Para el MVP se eligio `Ollama + qwen3.5:4b + nomic-embed-text:latest` por los siguientes motivos:

- evita costo por consulta
- puede ejecutarse sin servicios externos
- favorece la reproducibilidad local de la demostracion

### Variantes de prompt

Se agrego `PROMPT_VARIANT` con tres opciones:

- `baseline`: tono informativo general
- `sales`: tono mas orientado a beneficios comerciales
- `strict`: prioriza precision factual y minimiza inferencias

Esto permitio comparar prompts sobre el mismo benchmark sin modificar la arquitectura.

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

Configuracion utilizada para la validacion principal:

- `LLM_PROVIDER=ollama`
- `CHAT_MODEL_NAME=qwen3.5:4b`
- `EMBEDDING_PROVIDER=ollama`
- `EMBEDDING_MODEL_NAME=nomic-embed-text:latest`

Metricas consideradas:

- exactitud por coincidencia de palabras clave esperadas
- latencia promedio por consulta

## 6. Resultados y Analisis

Resultados obtenidos sobre 15 casos:

- `docs/benchmark_sales.json`: 15/15 correctos, exactitud 100.0%, latencia promedio 0.01 s
- `docs/benchmark_strict.json`: 15/15 correctos, exactitud 100.0%, latencia promedio 0.01 s

Analisis:

- se supero la meta original de la propuesta, que planteaba 80% de precision sobre un conjunto de prueba
- la latencia promedio quedo por debajo del objetivo de 5 segundos
- la mejora principal no dependio exclusivamente del prompt, sino del cambio estructural del pipeline:
  - preprocesamiento de la base
  - recuperacion mas granular
  - capa extractiva para datos factuales

Conclusion operativa:

- en las pruebas realizadas, la variante `strict` resulto adecuada para el alcance de preguntas frecuentes definido en el proyecto, manteniendo la misma exactitud que `sales`

## 7. Limitaciones y Trabajo Futuro

Limitaciones actuales:

- el benchmark esta construido sobre un dominio cerrado y todavia no mide conversaciones reales de usuarios externos
- el flujo de audio sigue dependiendo de OpenAI y no forma parte del nucleo open source del MVP
- persisten advertencias tecnicas en librerias de LangChain y Chroma que deberian actualizarse en una siguiente iteracion
- la evaluacion actual prioriza exactitud factual; aun no mide satisfaccion de usuario ni robustez ante consultas ambiguas extensas

Trabajo futuro:

- incorporar logs reales anonimizados para una validacion mas amplia
- agregar OCR para futuras fuentes no textuales
- migrar a componentes mas nuevos de `langchain-chroma`
- sumar pruebas automaticas de regresion para preguntas frecuentes
- conectar formalmente la salida comercial con CRM o automatizaciones, si el caso de uso lo requiere

## 8. Guia de Ejecucion y Demo

### Preparacion

1. Instalar dependencias:
   `pip install -r requirements.txt`
2. Copiar `.env.example` a `.env`
3. Descargar modelos locales:
   `ollama pull qwen3.5:4b`
   `ollama pull nomic-embed-text`
4. Generar la base de conocimiento:
   `python scripts/prepare_dataset.py`

### Ejecucion

1. Levantar la API:
   `python run.py --host 0.0.0.0 --port 8851`
2. Abrir el chat o probar el backend desde el frontend existente

### Consultas de prueba

Consultas de ejemplo:

- "Cuanta autonomia tiene el TITO S5 y como se carga?"
- "Cual es el precio del TITO S5-300 AA?"
- "Donde hago un reclamo o pido servicio tecnico?"
- "Tienen agencia oficial en San Luis?"
- "Como funciona la reserva y la entrega inmediata?"

### Reproduccion del benchmark

`python scripts/run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:4b --embedding-provider ollama --embedding-model nomic-embed-text:latest`

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

La implementacion final evidencia la transicion desde una idea conceptual hacia un sistema funcional. El MVP responde consultas del dominio y, al mismo tiempo, queda documentado, parametrizado y validado con evidencia empirica reproducible. En ese sentido, el proyecto cumple con la guia de implementacion y atiende las observaciones surgidas durante la devolucion de la propuesta inicial.
