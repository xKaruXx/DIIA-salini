# Chatbot CORADIR Movilidad

PoC/MVP de un chatbot web para consultas frecuentes de CORADIR Movilidad Electrica.

## Stack actual

- `FastAPI` para la API y WebSocket del chat
- `Chroma` como vector store
- `Ollama` o `OpenAI` como proveedor configurable de LLM y embeddings
- `SQLite` local por defecto para facilitar la demo
- `n8n` opcional para webhooks de contacto

## Configuracion de ejecucion del MVP

### Inicio rapido para la presentacion final

Desde PowerShell, en la carpeta del repo:

```powershell
cd C:\Repositorios\DIIA-salini
pip install -r requirements.txt
Copy-Item .env.example .env
python scripts\prepare_dataset.py
powershell -ExecutionPolicy Bypass -File scripts\start_presentation_demo.ps1
```

Ese ultimo comando verifica Ollama, descarga si faltan el modelo de chat configurado en `.env` y el modelo de embeddings, levanta FastAPI en el puerto `8851` y abre la presentacion final en el navegador.

Para preparar tambien la comparacion de modelos de prueba de la presentacion, usar:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\start_presentation_demo.ps1 -PullComparisonModels
```

Con `-PullComparisonModels`, el script descarga automaticamente los modelos de prueba que no esten instalados en Ollama.

### Ejecucion manual

1. Instala dependencias:
   `pip install -r requirements.txt`
2. Copia `.env.example` a `.env`
3. Si vas a usar el stack open source local:
   `ollama pull qwen3.5:4b`
   `ollama pull nomic-embed-text-v2-moe`
4. Genera la base de conocimiento preprocesada:
   `python scripts/prepare_dataset.py`
5. Inicia la API:
   `python run.py --host 0.0.0.0 --port 8851`

La configuracion por defecto ya queda apuntando a:

- `LLM_PROVIDER=ollama`
- `CHAT_MODEL_NAME=qwen3.5:4b` en `.env.example` (`qwen3.5:0.8b` queda como fallback liviano si no se define variable)
- `EMBEDDING_PROVIDER=ollama`
- `EMBEDDING_MODEL_NAME=nomic-embed-text-v2-moe:latest`
- `DATABASE_URL=sqlite:///./chatbot_movilidad.db`

## Modelos Ollama usados

Modelo principal para la demo:

```powershell
ollama pull qwen3.5:4b
ollama pull nomic-embed-text-v2-moe
```

Modelos de chat usados para pruebas y comparacion:

```powershell
ollama pull gemma3:270m
ollama pull granite4:350m
ollama pull lfm2.5-thinking:1.2b
ollama pull qwen3.5:0.8b
ollama pull deepseek-r1:1.5b
ollama pull llama3.2:3b
ollama pull granite4.1:3b
ollama pull nemotron-3-nano:4b
ollama pull qwen3.5:4b
ollama pull qwen3.5:latest
ollama pull gemma4:e4b
```

Embeddings evaluados localmente:

```powershell
ollama pull nomic-embed-text
ollama pull embeddinggemma
ollama pull qwen3-embedding:0.6b
ollama pull nomic-embed-text-v2-moe
```

## Benchmark

Casos de validacion:

- `dataset/evaluacion_mvp.json`

Ejecucion:

`python scripts/run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text-v2-moe:latest`

Resultados generados:

- `docs/benchmark_strict.json`
- `docs/benchmark_sales.json`
- `docs/benchmark_real_strict_qwen35_latest.json`
- `docs/benchmark_real_sales_qwen35_latest.json`

## Guia de uso

Documentacion de ejecucion local y acceso a la interfaz web del chat:

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
- Si se actualiza el dataset preprocesado, debe regenerarse con `python scripts/prepare_dataset.py`.
