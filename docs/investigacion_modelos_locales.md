# Investigacion de Modelos Locales para Evaluacion

## Objetivo

Se relevaron los modelos disponibles localmente en Ollama para justificar una evaluacion de eficiencia. La pregunta principal es si el proyecto puede mantener calidad aceptable usando menos hardware.

La estrategia es separar dos decisiones:

- **modelo de chat**: redacta o completa la respuesta cuando la capa extractiva no alcanza
- **modelo de embeddings**: indexa y recupera documentos del corpus RAG

## Inventario local

Salida de `ollama list`:

| Modelo | Tipo | Tamano local | Uso propuesto |
|---|---|---:|---|
| `qwen3.5:latest` | chat | 6.6 GB | baseline de calidad |
| `qwen3.5:0.8b` | chat | 1.0 GB | candidato liviano principal |
| `deepseek-r1:1.5b` | chat/razonamiento | 1.1 GB | candidato liviano con razonamiento |
| `lfm2.5-thinking:1.2b` | chat/razonamiento | 731 MB | candidato sub-2B orientado a baja huella |
| `granite4:350m` | chat/instruct | 708 MB | limite inferior de hardware |
| `gemma4:e4b` | chat multimodal | 9.6 GB | comparador de calidad, no optimizacion de memoria |
| `nomic-embed-text:latest` | embedding | 274 MB | baseline liviano actual |
| `embeddinggemma:latest` | embedding | 621 MB | embedding compacto de Google |
| `qwen3-embedding:0.6b` | embedding | 639 MB | embedding multilingue compacto |
| `nomic-embed-text-v2-moe:latest` | embedding | 957 MB | embedding multilingue MoE mas capaz |

## Metadata local extraida con `ollama show`

| Modelo | Parametros | Contexto | Embedding length | Cuantizacion | Capacidades |
|---|---:|---:|---:|---|---|
| `qwen3.5:latest` | 9.7B | 262144 | 4096 | Q4_K_M | completion, vision, tools, thinking |
| `qwen3.5:0.8b` | 873.44M | 262144 | 1024 | Q8_0 | completion, vision, tools, thinking |
| `deepseek-r1:1.5b` | 1.8B | 131072 | 1536 | Q4_K_M | completion, thinking |
| `lfm2.5-thinking:1.2b` | 1.2B | 128000 | 2048 | Q4_K_M | completion, tools, thinking |
| `granite4:350m` | 352.38M | 32768 | 1024 | BF16 | completion, tools |
| `gemma4:e4b` | 8.0B | 131072 | 2560 | Q4_K_M | completion, vision, audio, tools, thinking |
| `nomic-embed-text:latest` | 137M | 2048 | 768 | F16 | embedding |
| `embeddinggemma:latest` | 307.58M | 2048 | 768 | BF16 | embedding |
| `qwen3-embedding:0.6b` | 595.78M | 32768 | 1024 | Q8_0 | embedding |
| `nomic-embed-text-v2-moe:latest` | 475.29M | 512 | 768 | F16 | embedding |

## Justificacion por modelo de chat

### `qwen3.5:latest`

Se mantiene como baseline porque es la configuracion ya documentada en el MVP. Localmente ocupa 6.6 GB y `ollama show` reporta 9.7B parametros. La pagina de Ollama lista `qwen3.5:latest` con ventana de 256K y entrada texto/imagen; tambien lista variantes mas chicas como `qwen3.5:0.8b`, `2b` y `4b`, lo que permite comparar dentro de la misma familia. Fuente: Ollama Qwen3.5.

Uso en la evaluacion:

- baseline de calidad
- referencia para medir perdida aceptable al bajar de tamano

### `qwen3.5:0.8b`

Es el candidato liviano mas directo porque pertenece a la misma familia que el baseline, pero localmente ocupa 1.0 GB. Ollama lo lista con la misma ventana de contexto de 256K que las variantes mayores. Esto lo vuelve ideal para medir si el pipeline RAG permite bajar mucho el tamano del modelo sin perder respuestas factuales.

Uso en la evaluacion:

- candidato principal para optimizacion
- comparar contra `qwen3.5:latest` reduciendo cambio de familia

### `deepseek-r1:1.5b`

Ollama identifica `deepseek-r1:1.5b` como un modelo destilado `DeepSeek-R1-Distill-Qwen-1.5B`. La documentacion de Ollama indica que la serie incluye modelos destilados y que DeepSeek-R1 esta orientado a razonamiento. Localmente ocupa 1.1 GB.

Uso en la evaluacion:

- probar si un modelo chico con orientacion a razonamiento mejora respuestas que requieren interpretar condiciones comerciales
- controlar si el modo reasoning introduce verbosidad o latencia innecesaria para FAQ factuales

### `lfm2.5-thinking:1.2b`

La pagina de Ollama describe LFM2.5-1.2B-Thinking como modelo general de texto, sub-2B, orientado a despliegue en dispositivo. Localmente ocupa 731 MB. Es interesante porque busca calidad razonable con baja huella.

Uso en la evaluacion:

- candidato de bajo hardware para respuestas cortas
- comparar contra DeepSeek 1.5B y Qwen 0.8B

### `granite4:350m`

Granite 4 350M es el limite inferior de la prueba. IBM/Hugging Face lo describe como modelo instruct liviano, pensado para despliegues on-device, con capacidades de instruction following, QA y RAG. Localmente ocupa 708 MB.

Uso en la evaluacion:

- prueba de minima capacidad
- verificar si la capa extractiva permite usar un modelo extremadamente chico
- detectar limite inferior: donde empieza a caer calidad, rechazo correcto o redaccion

### `gemma4:e4b`

Ollama describe `gemma4:e4b` como un modelo edge de "effective 4B", orientado a despliegues en dispositivos. Localmente ocupa 9.6 GB, mas que `qwen3.5:latest`, por lo que no se considera optimizacion de memoria en este entorno. Se incluye como comparador alternativo de calidad o robustez multimodal, no como candidato principal de ahorro.

Uso en la evaluacion:

- comparador de familia alternativa
- validar si un modelo mayor/edge justifica su costo local

## Justificacion por embedding

### `nomic-embed-text:latest`

Es el baseline actual. Ollama lo describe como un embedding abierto de alto rendimiento con ventana de contexto grande. Localmente es el mas liviano de los embeddings instalados: 274 MB.

Uso en la evaluacion:

- baseline de bajo costo
- primera opcion si la calidad de retrieval es suficiente

### `embeddinggemma:latest`

Ollama lo describe como un modelo de embedding de Google de 300M parametros. Localmente ocupa 621 MB y usa embeddings de 768 dimensiones. Es candidato porque mantiene tamano moderado y permite comparar contra Nomic en un modelo de otra familia.

Uso en la evaluacion:

- alternativa compacta a Nomic
- verificar si mejora retrieval sin crecer demasiado

### `qwen3-embedding:0.6b`

Ollama indica que Qwen3 Embedding esta disenado especificamente para tareas de embedding y ofrece tamanos 0.6B, 4B y 8B. La variante local `0.6b` ocupa 639 MB, tiene contexto de 32K y embedding length de 1024.

Uso en la evaluacion:

- candidato multilingue compacto
- interesante para corpus en espanol y consultas con variaciones de redaccion
- comparar si el mayor contexto y dimension mejoran MRR/Top-1

### `nomic-embed-text-v2-moe:latest`

La ficha de Nomic v2 MoE lo presenta como embedding multilingue MoE orientado a retrieval, con soporte para alrededor de 100 idiomas y arquitectura Mixture of Experts. Localmente ocupa 957 MB, bastante mas que `nomic-embed-text`, pero puede ser candidato si mejora ranking o recall.

Uso en la evaluacion:

- candidato de mayor calidad para retrieval multilingue
- comparar si su mayor costo local mejora Precision@5, Recall@5, MRR o Top-1

## Plan de evaluacion

### Modelos de chat

Ejecutar:

```bash
py -3 scripts/run_model_efficiency_matrix.py --cases dataset/evaluacion_mvp.json --prompt-variant strict --continue-on-error
```

Modelos incluidos por defecto:

- `qwen3.5:latest`
- `qwen3.5:0.8b`
- `deepseek-r1:1.5b`
- `lfm2.5-thinking:1.2b`
- `granite4:350m`
- `gemma4:e4b`

### Embeddings

Ejecutar:

```bash
py -3 scripts/run_embedding_efficiency_matrix.py --cases dataset/evaluacion_rag_extendida.json --continue-on-error
```

Embeddings incluidos por defecto:

- `nomic-embed-text:latest`
- `embeddinggemma:latest`
- `qwen3-embedding:0.6b`
- `nomic-embed-text-v2-moe:latest`

## Criterio de decision

Para chat:

- aceptar modelo chico si mantiene al menos 90% de accuracy en benchmark MVP
- revisar manualmente precios, autonomia, garantia, contacto y condiciones comerciales
- si falla rechazo correcto, usarlo solo en rutas factuales/extractivas

Para embeddings:

- mantener el embedding mas liviano que no degrade `Recall@5` ni `MRR`
- priorizar `Top-1 source accuracy` si se busca reducir ruido enviado al LLM
- si dos embeddings empatan, elegir el de menor tamano local y menor tiempo de indexado

## Fuentes consultadas

- Ollama Qwen3.5: https://registry.ollama.com/library/qwen3.5
- Ollama DeepSeek-R1: https://ollama.com/library/deepseek-r1
- IBM Granite 4.0 H 350M en Hugging Face: https://huggingface.co/ibm-granite/granite-4.0-h-350m
- Ollama LFM2.5 Thinking: https://ollama.com/library/lfm2.5-thinking
- Ollama Gemma4: https://ollama.com/library/gemma4
- Ollama EmbeddingGemma: https://ollama.com/library/embeddinggemma
- Ollama Qwen3 Embedding: https://ollama.com/library/qwen3-embedding
- Ollama Nomic Embed Text: https://ollama.com/library/nomic-embed-text
- Nomic Embed Text v2 MoE: https://www.ollama.com/toshk0/nomic-embed-text-v2-moe

