# Evaluacion de Retrieval sobre Dataset Extendido

## Resumen ejecutivo

Se agrego una medicion especifica de retrieval sobre el dataset extendido de 64 casos. Esta evaluacion no mide si la respuesta final contiene palabras clave, sino si el sistema recupera las fuentes esperadas para cada pregunta.

El resultado principal es que `nomic-embed-text-v2-moe:latest` mejora claramente la busqueda vectorial frente a `nomic-embed-text:latest`. Sin embargo, el mejor resultado global sigue estando en el modo hibrido, que combina busqueda por palabras clave con busqueda vectorial.

La mejora fue productiva porque ahora se puede distinguir entre fallas de recuperacion y fallas de generacion/respuesta.

## Cambio aplicado

Se extendio `scripts/run_benchmark.py` para soportar evaluacion de retrieval:

- lectura de `expected_sources` desde los casos de evaluacion
- recuperacion de documentos por modo `keyword`, `vector` o `hybrid`
- calculo de metricas de retrieval
- ejecucion opcional `--skip-response` para medir retrieval sin llamar al LLM
- salida JSON con documentos recuperados por pregunta

Comando base:

```powershell
py scripts\run_benchmark.py --cases dataset\evaluacion_rag_extendida.json --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text-v2-moe:latest --retrieval-top-k 5 --retrieval-mode hybrid --skip-response --output docs\benchmark_retrieval_extendido_hybrid_v2_moe_fresh.json
```

## Metricas usadas

| Metrica | Que mide |
|---|---|
| Precision@5 | Proporcion de documentos recuperados en top 5 que coinciden con fuentes esperadas |
| Recall@5 | Proporcion de fuentes esperadas encontradas dentro del top 5 |
| MRR | Que tan arriba aparece la primera fuente relevante |
| Top-1 source accuracy | Porcentaje de casos donde la primera fuente recuperada es relevante |

## Resultados

| Modo | Embedding | Precision@5 | Recall@5 | MRR | Top-1 source accuracy |
|---|---|---:|---:|---:|---:|
| keyword | `nomic-embed-text-v2-moe:latest` | 0.3187 | 0.8984 | 0.7589 | 0.6562 |
| vector | `nomic-embed-text:latest` | 0.1344 | 0.4375 | 0.3018 | 0.2031 |
| vector | `nomic-embed-text-v2-moe:latest` | 0.2281 | 0.7891 | 0.6542 | 0.5469 |
| hybrid | `nomic-embed-text:latest` | 0.2594 | 0.8281 | 0.7448 | 0.6562 |
| hybrid | `nomic-embed-text-v2-moe:latest` | 0.2937 | 0.9062 | 0.7609 | 0.6562 |

## Lectura tecnica

### Lo que funciono

El modo `hybrid` con `nomic-embed-text-v2-moe:latest` obtuvo el mejor balance general:

- mayor Recall@5: 0.9062
- mejor MRR: 0.7609
- misma exactitud Top-1 que keyword: 0.6562

Esto indica que la combinacion de keyword y vector aumenta la probabilidad de incluir la fuente esperada dentro del contexto.

### Lo que no funciono como se esperaba

La busqueda vectorial pura con el embedding clasico fue debil:

- Precision@5: 0.1344
- Recall@5: 0.4375
- MRR: 0.3018
- Top-1: 0.2031

Esto confirma que no conviene depender solo del vector store para este dataset. La estructura de datos contiene muchos nombres propios, codigos, precios, modelos y direcciones; esos elementos suelen favorecer busqueda lexical o hibrida.

### Resultado sobre `v2-moe`

Con medicion de retrieval, `nomic-embed-text-v2-moe:latest` si muestra una mejora clara sobre `nomic-embed-text:latest`:

- en vector puro, Recall@5 sube de 0.4375 a 0.7891
- en vector puro, MRR sube de 0.3018 a 0.6542
- en hibrido, Recall@5 sube de 0.8281 a 0.9062
- en hibrido, MRR sube de 0.7448 a 0.7609

## Incidencias durante la prueba

Hubo dos hallazgos operativos:

1. Un vector store previo tenia metadatos vacios, lo que produjo una medicion vectorial invalida con metricas en cero.
2. Una corrida paralela de reconstruccion de Chroma genero un error SQLite de migracion.

Decision tomada:

- no se considero valida la medicion con metadatos vacios
- se reconstruyo un indice limpio usando `VECTORSTORE_BASE_DIR=.\chroma_db\retrieval_eval_fresh`
- las corridas posteriores se hicieron de forma secuencial para evitar conflictos de Chroma/SQLite

Estos incidentes quedan asentados porque forman parte del proceso de mejora y validacion.

## Conclusion academica

La mejora de evaluacion fue productiva. Antes solo se sabia que el benchmark extendido tenia 35/64 respuestas correctas por keywords. Ahora se sabe que el retrieval hibrido recupera fuentes esperadas en 90.62% de los casos dentro del top 5.

Eso permite una interpretacion mas precisa:

- si una respuesta falla pero la fuente estaba en top 5, el problema esta en extraccion/redaccion
- si la fuente no aparece en top 5, el problema esta en recuperacion
- si la fuente aparece tarde, hay que mejorar ranking

## Proximo paso

Analizar los casos fallidos del benchmark de respuesta cruzandolos con estas metricas de retrieval:

1. fallos con fuente esperada recuperada
2. fallos sin fuente esperada recuperada
3. aciertos con retrieval debil
4. categorias con bajo Top-1

Ese cruce va a indicar si conviene mejorar el preprocesamiento, el ranking, la capa extractiva o las keywords esperadas.
