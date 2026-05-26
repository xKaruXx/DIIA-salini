# Optimizacion de Hardware y Evaluacion de Modelos Livianos

## Objetivo

El objetivo de esta mejora es verificar si el chatbot puede usar modelos de respuesta mas chicos sin perder demasiada calidad. La motivacion es reducir uso de hardware, memoria, tiempo de respuesta y dependencia de equipos potentes.

Esta mejora no reemplaza la evaluacion de retrieval. La complementa: primero se valida si el sistema recupera buen contexto, y despues se mide cuanto modelo generativo hace falta para redactar una respuesta correcta.

## Baseline actual

La configuracion final recomendada del MVP usa:

- modelo de chat por defecto: `qwen3.5:0.8b`
- modelo fallback: `qwen3.5:latest`
- embeddings: `nomic-embed-text:latest`
- prompt principal para evaluacion: `strict`
- dataset MVP: `dataset/evaluacion_mvp.json`

Resultados disponibles del baseline:

| Reporte | Casos | Accuracy | Latencia promedio |
|---|---:|---:|---:|
| `docs/benchmark_real_strict_qwen35_latest.json` | 15 | 100.0% | 0.01 s |
| `docs/benchmark_real_sales_qwen35_latest.json` | 15 | 100.0% | 0.01 s |
| `docs/benchmark_extendido_strict_qwen35_0_8b.json` | 64 | 54.7% | 0.01 s |

La latencia reportada corresponde a la ruta evaluada localmente y debe interpretarse junto con el tipo de respuesta generada. Para comparar modelos livianos, lo importante es repetir exactamente el mismo benchmark con cada modelo.

## Hipotesis

Como el proyecto usa una base cerrada, preprocesamiento, retrieval y capa extractiva, es posible que muchas preguntas frecuentes no requieran un modelo grande. Un modelo chico podria alcanzar si:

- la fuente correcta aparece en el contexto
- la respuesta esperada es factual y breve
- el prompt `strict` evita razonamientos largos
- la capa extractiva resuelve precios, autonomia, carga, garantias y contactos

Los modelos chicos podrian fallar mas en:

- preguntas ambiguas
- sintesis de varias fuentes
- rechazo de preguntas no respondibles
- redaccion comercial
- explicaciones largas

## Matriz de modelos propuesta

Los modelos concretos se ajustaron a lo que esta disponible en Ollama local. La matriz preparada por defecto incluye:

| Rol | Modelo candidato | Motivo |
|---|---|---|
| Baseline | `qwen3.5:latest` | configuracion actual documentada |
| Candidato chico | `qwen3.5:0.8b` | misma familia que el baseline, mucha menor huella local |
| Razonamiento liviano | `deepseek-r1:1.5b` | modelo destilado pequeno orientado a razonamiento |
| Sub-2B liviano | `lfm2.5-thinking:1.2b` | pensado para despliegue en dispositivo |
| Minimo instruct | `granite4:350m` | limite inferior de hardware para preguntas factuales |
| Comparador alternativo | `gemma4:e4b` | familia alternativa, no necesariamente mas liviana en este equipo |

La lista no debe entenderse como definitiva. Si un tag no existe localmente, se reemplaza por otro modelo instalado o disponible en Ollama.

## Script agregado

Se agrego:

- `scripts/run_model_efficiency_matrix.py`

Uso sugerido:

```bash
py -3 scripts/run_model_efficiency_matrix.py --cases dataset/evaluacion_mvp.json --prompt-variant strict --continue-on-error
```

Para una prueba mas rapida o sin LLM:

```bash
py -3 scripts/run_model_efficiency_matrix.py --cases dataset/evaluacion_mvp.json --prompt-variant strict --skip-response --continue-on-error
```

Para definir una lista manual:

```bash
py -3 scripts/run_model_efficiency_matrix.py --models qwen3.5:latest qwen3.5:0.8b deepseek-r1:1.5b lfm2.5-thinking:1.2b granite4:350m --continue-on-error
```

Los reportes se guardan en:

- `docs/benchmarks_modelos_livianos/`

Para embeddings se agrego una matriz separada:

```bash
py -3 scripts/run_embedding_efficiency_matrix.py --cases dataset/evaluacion_rag_extendida.json --continue-on-error
```

Embeddings evaluables:

- `nomic-embed-text:latest`
- `embeddinggemma:latest`
- `qwen3-embedding:0.6b`
- `nomic-embed-text-v2-moe:latest`

Los reportes se guardan en:

- `docs/benchmarks_embeddings/`

## Metricas de comparacion

Cada modelo se debe comparar con:

| Dimension | Metrica | Fuente |
|---|---|---|
| Calidad de respuesta | accuracy por keywords | `scripts/run_benchmark.py` |
| Recuperacion | Precision@5, Recall@5, MRR | `scripts/run_benchmark.py` |
| Velocidad | latencia promedio | reporte JSON |
| Verbosidad | longitud media de respuesta | reporte JSON o graficos |
| Robustez | tasa de rechazo correcto | `dataset/evaluacion_no_respondibles.json` |
| Costo operativo | memoria/VRAM aproximada | observacion local del entorno |

## Criterio de decision

Un modelo chico se considera aceptable si cumple:

- accuracy MVP al menos 90%
- no degrada respuestas criticas de precios, garantia, autonomia y contacto
- mantiene rechazo correcto en casos no respondibles
- reduce de forma observable el consumo de hardware o mejora latencia

Si el modelo chico conserva accuracy pero empeora redaccion, puede usarse solo en rutas factuales/extractivas. Si falla en rechazo o ambiguedad, conviene mantener el baseline para esas rutas.

## Optimizaciones recomendadas antes de cambiar de modelo

1. Mantener `strict` como prompt por defecto para preguntas factuales.
2. Priorizar respuesta extractiva cuando el dato aparece directamente en el contexto.
3. Reducir `retrieval_k` si Precision@K mejora y no cae Recall@K.
4. Enriquecer metadata para que el top 1 sea mas estable.
5. Usar benchmark corto de 15 casos para iteracion rapida y extendido de 64 casos para validacion final.
6. Evitar lematizacion global mientras el EDA del corpus no lo justifique.
7. Separar rutas: modelo chico para FAQ factual, modelo mayor para sintesis o consultas ambiguas.

## Estado de ejecucion

Los modelos locales fueron relevados y justificados en `docs/investigacion_modelos_locales.md`.

Estado actualizado:

- matriz de chat ejecutada sobre `dataset/evaluacion_mvp.json`: todos los modelos obtuvieron 15/15
- matriz de embeddings ejecutada sobre `dataset/evaluacion_rag_extendida.json` en modo vector-only
- resultados consolidados en `docs/evaluacion_modelos_livianos.md` y `docs/evaluacion_embeddings_locales.md`

Queda pendiente completar la evaluacion de casos no respondibles y consultas ambiguas antes de cambiar el modelo de chat por defecto.

## Como contarlo en la presentacion

La mejora puede presentarse asi:

1. El sistema ya reduce carga del LLM porque recupera contexto y usa una capa extractiva.
2. Por eso tiene sentido evaluar modelos mas chicos.
3. Se preparo una matriz reproducible para comparar calidad, latencia y robustez.
4. La decision no se toma por tamano del modelo, sino por evidencia: accuracy, MRR, rechazo correcto y consumo.
5. Si un modelo chico alcanza para preguntas factuales, se puede reservar el modelo mayor para casos complejos.
