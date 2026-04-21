# Chatbot CORADIR Movilidad

PoC/MVP de un chatbot web para consultas frecuentes de CORADIR Movilidad Electrica.

## Stack actual

- `FastAPI` para la API y WebSocket del chat
- `Chroma` como vector store
- `Ollama` o `OpenAI` como proveedor configurable de LLM y embeddings
- `SQLite` local por defecto para facilitar la demo
- `n8n` opcional para webhooks de contacto

## Configuracion recomendada para el MVP

1. Instala dependencias:
   `pip install -r requirements.txt`
2. Copia `.env.example` a `.env`
3. Si vas a usar el stack open source local:
   `ollama pull qwen3.5:4b`
   `ollama pull nomic-embed-text`
4. Genera la base de conocimiento preprocesada:
   `python scripts/prepare_dataset.py`
5. Inicia la API:
   `python run.py --host 0.0.0.0 --port 8851`

La configuracion por defecto ya queda apuntando a:

- `LLM_PROVIDER=ollama`
- `CHAT_MODEL_NAME=qwen3.5:4b`
- `EMBEDDING_PROVIDER=ollama`
- `EMBEDDING_MODEL_NAME=nomic-embed-text:latest`
- `DATABASE_URL=sqlite:///./chatbot_movilidad.db`

## Benchmark

Casos de validacion:

- `dataset/evaluacion_mvp.json`

Ejecucion:

`python scripts/run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:4b --embedding-provider ollama --embedding-model nomic-embed-text:latest`

Resultados generados:

- `docs/benchmark_strict.json`
- `docs/benchmark_sales.json`

## Guia de uso

Para levantar el proyecto y abrir la interfaz web del chat:

- `docs/guia_uso_y_demo.md`

## Variables de entorno principales

- `DATABASE_URL`: por defecto usa SQLite local
- `LLM_PROVIDER`: `ollama` u `openai`
- `CHAT_MODEL_NAME`: nombre del modelo de chat
- `EMBEDDING_PROVIDER`: `ollama` u `openai`
- `EMBEDDING_MODEL_NAME`: nombre del modelo de embeddings
- `OLLAMA_BASE_URL`: URL del servidor Ollama si no corre en el default
- `PROMPT_VARIANT`: `baseline`, `sales` o `strict`
- `RAG_DATASET_PATH`: base de conocimiento JSONL preprocesada
- `RAW_DATASET_PATH`: dataset JSON original
- `VECTORSTORE_BASE_DIR`: carpeta base para los indices Chroma
- `N8N_WEBHOOK_URL`: opcional
- `OPENAI_API_KEY`: solo si se usa OpenAI

## Notas

- El flujo de audio sigue siendo opcional y no forma parte del nucleo del MVP academico.
- Si cambias el dataset preprocesado, conviene regenerarlo con `python scripts/prepare_dataset.py`.
