# Guia de Uso y Demo

Esta guia explica como levantar el proyecto localmente, abrir la interfaz web del chat y preparar una demo simple para una presentacion por Zoom.

## 1. Requisitos

- Python 3.11 o superior
- Ollama instalado y en ejecucion
- Acceso a una terminal en Windows PowerShell

## 2. Preparacion inicial

Desde la carpeta del repo:

```powershell
cd C:\Users\Charly\Documents\Repositorios\DIIA-salini
pip install -r requirements.txt
Copy-Item .env.example .env
```

Descarga los modelos que usa el MVP:

```powershell
ollama pull qwen3.5:4b
ollama pull nomic-embed-text
```

Genera la base de conocimiento preprocesada:

```powershell
python scripts\prepare_dataset.py
```

## 3. Levantar el backend

Inicia el servidor FastAPI:

```powershell
python run.py --host 127.0.0.1 --port 8851
```

Si todo esta bien, la API queda disponible en:

- `http://127.0.0.1:8851`
- `http://localhost:8851`

Chequeo rapido de salud:

- `http://localhost:8851/health`

La respuesta esperada es un JSON con estado `ok`.

## 4. Abrir el chat web

La interfaz del chat ya viene incluida en el proyecto. No hace falta Gradio.

El chat requiere un token temporal. La forma mas simple de abrirlo localmente es:

```powershell
$token = (Invoke-RestMethod -Headers @{ Referer = 'http://localhost' } -Uri 'http://127.0.0.1:8851/generate-token').token
Start-Process "http://127.0.0.1:8851/chat?token=$token"
```

Eso hace dos cosas:

1. solicita un token temporal al backend
2. abre la interfaz del chat en el navegador

Si el navegador muestra `Token invalido o expirado`, vuelve a ejecutar ese bloque para generar uno nuevo.

## 5. Flujo recomendado para una demo por Zoom

Antes de entrar a la videollamada:

1. abre una terminal y deja corriendo `python run.py --host 127.0.0.1 --port 8851`
2. abre `http://localhost:8851/health` para mostrar que la API esta viva
3. ejecuta el bloque de PowerShell que genera el token y abre el chat
4. deja listas 3 o 4 preguntas de ejemplo

Preguntas recomendadas:

- `Cual es el precio del TITO S5-300 AA?`
- `Cuanta autonomia tiene el TITO S5 y como se carga?`
- `Tienen agencia oficial en San Luis?`
- `Como funciona la reserva y la entrega inmediata?`
- `Donde hago un reclamo o pido servicio tecnico?`

## 6. Benchmark reproducible

Para mostrar validacion tecnica durante la presentacion:

```powershell
python scripts\run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:4b --embedding-provider ollama --embedding-model nomic-embed-text:latest
```

Resultados disponibles en:

- `docs/benchmark_strict.json`
- `docs/benchmark_sales.json`

## 7. Problemas comunes

### El chat no abre

Verifica primero:

- que `python run.py --host 127.0.0.1 --port 8851` siga corriendo
- que `http://localhost:8851/health` responda
- que Ollama este levantado

### Error de modelo en Ollama

Vuelve a descargar los modelos:

```powershell
ollama pull qwen3.5:4b
ollama pull nomic-embed-text
```

### Token expirado

Los tokens del chat son temporales. Reejecuta:

```powershell
$token = (Invoke-RestMethod -Headers @{ Referer = 'http://localhost' } -Uri 'http://127.0.0.1:8851/generate-token').token
Start-Process "http://127.0.0.1:8851/chat?token=$token"
```

## 8. Comentario sobre Gradio

En clase se sugirio Gradio para pruebas rapidas, pero en este proyecto no es necesario porque el MVP ya incluye:

- backend propio en FastAPI
- interfaz web propia
- comunicacion en tiempo real por WebSocket

Para la entrega y la defensa conviene mostrar esta interfaz, porque corresponde al sistema implementado y no a un envoltorio extra de demo.
