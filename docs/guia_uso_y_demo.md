# Guia de Uso y Demo

Esta guia explica como levantar el proyecto localmente, abrir la interfaz web del chat y ejecutar una demostracion funcional.

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
ollama pull qwen3.5:0.8b
ollama pull nomic-embed-text
```

Para comparar modelos en vivo desde la presentacion, descarga tambien los candidatos que quieras mostrar:

```powershell
ollama pull granite4:350m
ollama pull lfm2.5-thinking:1.2b
ollama pull deepseek-r1:1.5b
ollama pull granite4.1:3b
ollama pull qwen3.5:4b
```

Ollama debe quedar corriendo antes de abrir la demo. En Windows normalmente se inicia con la aplicacion de Ollama; si hace falta levantarlo manualmente:

```powershell
ollama serve
```

Genera la base de conocimiento preprocesada:

```powershell
python scripts\prepare_dataset.py
```

## 3. Levantar el backend

Para la presentacion final, la forma mas simple es usar el lanzador local:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\start_presentation_demo.ps1
```

Ese comando verifica Ollama, descarga los modelos principales si faltan, levanta FastAPI en el puerto `8851` y abre la presentacion en el navegador.

Si tambien queres descargar los modelos livianos para la comparacion en vivo:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\start_presentation_demo.ps1 -PullComparisonModels
```

Modo manual:

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

La interfaz del chat ya viene incluida en el proyecto.

El chat requiere un token temporal. La forma mas simple de abrirlo localmente es:

```powershell
$token = (Invoke-RestMethod -Headers @{ Referer = 'http://localhost' } -Uri 'http://127.0.0.1:8851/generate-token').token
Start-Process "http://127.0.0.1:8851/chat?token=$token"
```

Eso hace dos cosas:

1. solicita un token temporal al backend
2. abre la interfaz del chat en el navegador

Si el navegador muestra `Token invalido o expirado`, vuelve a ejecutar ese bloque para generar uno nuevo.

## 5. Flujo de demo local

Secuencia de ejecucion:

1. abre una terminal y deja corriendo `python run.py --host 127.0.0.1 --port 8851`
2. abre `http://localhost:8851/health` para mostrar que la API esta viva
3. ejecuta el bloque de PowerShell que genera el token y abre el chat
4. deja listas 3 o 4 preguntas de ejemplo

Preguntas de ejemplo:

- `Cual es el precio del TITO S5-300 AA?`
- `Cuanta autonomia tiene el TITO S5 y como se carga?`
- `Tienen agencia oficial en San Luis?`
- `Como funciona la reserva y la entrega inmediata?`
- `Donde hago un reclamo o pido servicio tecnico?`

## 6. Benchmark reproducible

Para mostrar validacion tecnica durante la presentacion:

```powershell
python scripts\run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:0.8b --embedding-provider ollama --embedding-model nomic-embed-text:latest
```

Resultados disponibles en:

- `docs/benchmark_strict.json`
- `docs/benchmark_sales.json`
- `docs/benchmark_real_strict_qwen35_latest.json`
- `docs/benchmark_real_sales_qwen35_latest.json`

## 6.1 Revision manual de modelos

Para comparar calidad real de respuestas entre modelos locales, se agrego una matriz para revision manual del autor con 21 preguntas balanceadas: 7 factuales claras, 7 ambiguas y 7 fuera de dominio/no respondibles. Esta etapa es distinta de la primera evaluacion sintetica/automatica por keywords y latencia:

```powershell
py scripts\run_manual_model_evaluation.py --models gemma3:270m granite4:350m qwen3.5:0.8b lfm2.5-thinking:1.2b llama3.2:3b granite4.1:3b nemotron-3-nano:4b qwen3.5:4b --timeout 120
```

Salidas:

- `docs/evaluacion_manual_modelos_respuestas.json`
- `docs/evaluacion_manual_modelos_matriz.csv`
- `docs/evaluacion_manual_modelos_matriz.md`

El script completa respuestas, estado, latencia y un score preliminar `assistant_score_1_5`. El CSV se completa manualmente con `manual_correct`, `manual_score_1_5` y `manual_notes`.

Para modelos Qwen o modelos `thinking`, el script usa `think: false`, remueve bloques `<think>...</think>` si aparecen y marca `thinking_removed`. Si no queda una respuesta final evaluable, el estado queda como `thinking_only`.

La presentacion final usa esa salida para mostrar tres graficos:

- ranking de respuestas aceptables por modelo (`score 4 o 5`)
- medicion por criterio: factuales claras, ambiguas y fuera de dominio
- tradeoff operativo: acierto, latencia promedio y peso local aproximado

En la corrida actual, `qwen3.5:latest` queda primero por acierto bruto y `qwen3.5:4b` queda como candidato de compromiso por calidad, latencia y peso. Esa seleccion se debe confirmar con la revision manual.

## 7. Presentacion con chat embebido

La presentacion final incluye una seccion de demo que puede cargar el chat real dentro del HTML.

Con la API levantada, abrir:

```powershell
Start-Process "http://localhost:8851/docs/presentacion_final_chatbot_coradir.html"
```

Luego ir a la seccion "Demo en vivo" y presionar `Cargar chat`.

Importante: si se abre el HTML directamente desde el explorador de archivos, el chat embebido no puede pedir token local. Para la demo interactiva conviene abrirlo desde `http://localhost:8851/docs/presentacion_final_chatbot_coradir.html`.

El boton `Cargar chat` no puede levantar el backend por si mismo si la presentacion se abrio como archivo local. El navegador no tiene permiso para ejecutar procesos del sistema. Por eso el flujo recomendado es ejecutar primero `scripts\start_presentation_demo.ps1`, que deja todo listo y abre la URL correcta.

La misma seccion incluye una comparacion local de modelos:

1. presionar `Cargar modelos`
2. seleccionar hasta 4 modelos disponibles en Ollama
3. escribir una pregunta
4. presionar `Comparar respuestas`

Esto ejecuta la misma pregunta contra los modelos seleccionados usando el mismo contexto RAG. No cambia el modelo configurado para el chat principal.

## 8. Problemas comunes

### El chat no abre

Verifica primero:

- que `python run.py --host 127.0.0.1 --port 8851` siga corriendo
- que `http://localhost:8851/health` responda
- que Ollama este levantado
- que la presentacion se haya abierto desde `http://localhost:8851/docs/presentacion_final_chatbot_coradir.html`, no como archivo local

### Error de modelo en Ollama

Vuelve a descargar los modelos:

```powershell
ollama pull qwen3.5:0.8b
ollama pull nomic-embed-text
```

### Token expirado

Los tokens del chat son temporales. Reejecuta:

```powershell
$token = (Invoke-RestMethod -Headers @{ Referer = 'http://localhost' } -Uri 'http://127.0.0.1:8851/generate-token').token
Start-Process "http://127.0.0.1:8851/chat?token=$token"
```

## 9. Interfaz incluida en el proyecto

El MVP incluye:

- backend propio en FastAPI
- interfaz web propia
- comunicacion en tiempo real por WebSocket
