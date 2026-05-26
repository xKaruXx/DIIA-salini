# Comparacion de Modelos de Embedding

## Resumen ejecutivo

Se compararon `nomic-embed-text:latest` y `nomic-embed-text-v2-moe:latest` con el benchmark actual del chatbot. En este conjunto de 15 preguntas, ambos modelos obtuvieron el mismo resultado: 15/15 casos correctos en las variantes `strict` y `sales`.

Con el benchmark extendido y metricas de retrieval, `nomic-embed-text-v2-moe:latest` si muestra una mejora observable frente a `nomic-embed-text:latest`, especialmente en busqueda vectorial pura y en recall del modo hibrido.

## Diferencias reportadas por Ollama

| Modelo | Arquitectura | Parametros | Contexto | Dimension embedding | Tamaño local |
|---|---|---:|---:|---:|---:|
| `nomic-embed-text:latest` | `nomic-bert` | 137M | 2048 | 768 | 274 MB |
| `nomic-embed-text-v2-moe:latest` | `nomic-bert-moe` | 475.29M | 512 | 768 | 957 MB |

## Resultados del benchmark local

| Embedding | Prompt | Casos aprobados | Accuracy | Latencia promedio | Longitud media respuesta |
|---|---|---:|---:|---:|---:|
| `nomic-embed-text:latest` | `strict` | 15/15 | 100.0% | 0.01 s | 365.5 caracteres |
| `nomic-embed-text:latest` | `sales` | 15/15 | 100.0% | 0.01 s | 365.5 caracteres |
| `nomic-embed-text-v2-moe:latest` | `strict` | 15/15 | 100.0% | 0.01 s | 365.5 caracteres |
| `nomic-embed-text-v2-moe:latest` | `sales` | 15/15 | 100.0% | 0.01 s | 365.5 caracteres |

## Lectura tecnica

`nomic-embed-text-v2-moe:latest` es mas moderno y mas grande. Segun la ficha de Ollama, esta orientado a retrieval multilingue y usa arquitectura Mixture of Experts. Eso lo vuelve un buen candidato para una base en español y para futuras fuentes heterogeneas.

Pero en el benchmark actual no hay diferencia medible porque:

- el dataset es chico y cerrado
- las preguntas son frecuentes y relativamente directas
- la capa extractiva y busqueda por palabras clave ya resuelven gran parte de los casos
- la metrica actual evalua palabras clave en la respuesta final, no ranking de documentos

## Recomendacion

Para la demo corta, cualquiera de los dos funciona. Si se prioriza simplicidad y menor peso local, `nomic-embed-text:latest` es suficiente.

Para el trabajo final, conviene adoptar `nomic-embed-text-v2-moe:latest` como mejora candidata documentada:

- baseline: `nomic-embed-text:latest`
- mejora: `nomic-embed-text-v2-moe:latest`
- evaluacion de respuesta: empate en accuracy
- evaluacion de retrieval: mejora en Recall@5 y MRR

## Evidencia adicional de retrieval

| Modo | Embedding | Precision@5 | Recall@5 | MRR | Top-1 |
|---|---|---:|---:|---:|---:|
| vector | `nomic-embed-text:latest` | 0.1344 | 0.4375 | 0.3018 | 0.2031 |
| vector | `nomic-embed-text-v2-moe:latest` | 0.2281 | 0.7891 | 0.6542 | 0.5469 |
| hybrid | `nomic-embed-text:latest` | 0.2594 | 0.8281 | 0.7448 | 0.6562 |
| hybrid | `nomic-embed-text-v2-moe:latest` | 0.2937 | 0.9062 | 0.7609 | 0.6562 |

## Proximo paso recomendado

Cruzar los casos fallidos del benchmark de respuesta con el reporte de retrieval para separar fallas de recuperacion de fallas de extraccion/redaccion.
