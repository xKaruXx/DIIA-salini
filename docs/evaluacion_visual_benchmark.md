# Evaluacion Visual del Benchmark

## Resumen ejecutivo

Se generaron visualizaciones a partir de los reportes reales ejecutados localmente con Ollama. Todas las variantes evaluadas aprobaron los 15 casos del conjunto de prueba.

| Variante | Casos aprobados | Accuracy | Latencia promedio | Modelo chat | Modelo embeddings |
|---|---:|---:|---:|---|---|
| `sales / text` | 15/15 | 100.0% | 0.01 s | `qwen3.5:latest` | `nomic-embed-text:latest` |
| `strict / text` | 15/15 | 100.0% | 0.01 s | `qwen3.5:latest` | `nomic-embed-text:latest` |

## Graficos

### Accuracy por variante

![Accuracy por variante](charts/benchmark_accuracy_by_variant.svg)

### Latencia por caso

![Latencia por caso](charts/benchmark_latency_by_case.svg)

### Longitud de respuesta por caso

![Longitud de respuesta por caso](charts/benchmark_response_length_by_case.svg)

### Accuracy por categoria

![Accuracy por categoria](charts/benchmark_accuracy_by_category.svg)

### Cobertura por caso y variante

![Cobertura por caso y variante](charts/benchmark_case_coverage.svg)

## Lectura rapida

- El accuracy permite comparar rapidamente la cobertura de palabras clave esperadas.
- La latencia promedio registrada por el script ayuda a controlar regresiones de performance.
- La longitud de respuesta ayuda a revisar concision: casos con respuestas mas largas deberian revisarse en la matriz factual.
- La cobertura por categoria muestra donde se concentran los aciertos y las fallas.

## Distribucion de casos

| Categoria | Casos |
|---|---:|
| agencias | 1 |
| beneficios | 1 |
| carga | 2 |
| comercial | 1 |
| compra | 1 |
| contacto | 1 |
| posventa | 2 |
| precios | 2 |
| vehiculos | 4 |

## Limitacion

Estos graficos visualizan el benchmark actual, que valida palabras clave en la respuesta final. Todavia falta incorporar metricas especificas de retrieval como Precision@K, Recall@K y MRR.
