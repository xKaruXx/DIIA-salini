# Evaluacion Visual del Benchmark

## Resumen ejecutivo

Se generaron visualizaciones a partir de los reportes reales ejecutados localmente con Ollama. El conjunto evaluado contiene 64 casos y permite comparar cobertura, fallas y longitud de respuesta.

| Variante | Casos aprobados | Accuracy | Latencia promedio | Modelo chat | Modelo embeddings |
|---|---:|---:|---:|---|---|
| `strict / text-v2-moe` | 35/64 | 54.7% | 0.01 s | `qwen3.5:latest` | `nomic-embed-text-v2-moe:latest` |
| `strict / text` | 35/64 | 54.7% | 0.01 s | `qwen3.5:latest` | `nomic-embed-text:latest` |

## Graficos

### Accuracy por variante

![Accuracy por variante](charts_extendido/benchmark_accuracy_by_variant.svg)

### Latencia por caso

![Latencia por caso](charts_extendido/benchmark_latency_by_case.svg)

### Longitud de respuesta por caso

![Longitud de respuesta por caso](charts_extendido/benchmark_response_length_by_case.svg)

### Accuracy por categoria

![Accuracy por categoria](charts_extendido/benchmark_accuracy_by_category.svg)

### Cobertura por caso y variante

![Cobertura por caso y variante](charts_extendido/benchmark_case_coverage.svg)

## Lectura rapida

- El accuracy permite comparar rapidamente la cobertura de palabras clave esperadas.
- La latencia promedio registrada por el script ayuda a controlar regresiones de performance.
- La longitud de respuesta ayuda a revisar concision: casos con respuestas mas largas deberian revisarse en la matriz factual.
- La cobertura por categoria muestra donde se concentran los aciertos y las fallas.

## Distribucion de casos

| Categoria | Casos |
|---|---:|
| agencias | 6 |
| app | 2 |
| beneficios | 1 |
| carga | 4 |
| comercial | 1 |
| compra | 5 |
| contacto | 1 |
| empresa | 5 |
| movilidad | 2 |
| posventa | 2 |
| precios | 12 |
| sitios_web | 1 |
| vehiculos | 22 |

## Limitacion

Estos graficos visualizan el benchmark actual, que valida palabras clave en la respuesta final. Todavia falta incorporar metricas especificas de retrieval como Precision@K, Recall@K y MRR.
