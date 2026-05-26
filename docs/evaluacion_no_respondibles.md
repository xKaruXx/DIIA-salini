# Evaluacion de Casos No Respondibles

## Objetivo

El material de clase 4 recomienda probar preguntas que no tienen respuesta en el corpus para detectar alucinaciones o respuestas fuera de alcance. Por eso se agrego un dataset especifico:

- `dataset/evaluacion_no_respondibles.json`

Este dataset no busca medir conocimiento del dominio, sino comportamiento responsable cuando el sistema no dispone de evidencia suficiente.

## Casos incluidos

| ID | Tipo | Pregunta |
|---|---|---|
| `offtopic_resultado_futbol` | fuera de dominio | ¿Quién ganó el último partido de Boca? |
| `offtopic_receta` | fuera de dominio | Dame una receta de ñoquis caseros. |
| `dato_no_presente_stock_hoy` | dato no presente | ¿Cuántas unidades exactas del TITO hay en stock hoy? |
| `dato_no_presente_financiacion_banco` | dato no presente | ¿Qué tasa ofrece el Banco Nación para financiar un TITO esta semana? |
| `producto_no_cubierto_camion` | producto no cubierto | ¿CORADIR vende camiones eléctricos de larga distancia? |
| `legal_no_cubierto_patentamiento` | dato legal no cubierto | ¿Qué artículo legal exacto regula el patentamiento de la TITA en mi municipio? |

## Estado de ejecucion

Se genero el reporte en modo retrieval-only:

- `docs/benchmark_no_respondibles_retrieval_keyword_qwen35_latest.json`

No se pudo evaluar la respuesta final porque Ollama no estaba levantado durante la corrida. La evaluacion completa debe ejecutarse con:

```bash
py -3 scripts/run_benchmark.py --cases dataset/evaluacion_no_respondibles.json --output docs/benchmark_no_respondibles_qwen35_latest.json --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text:latest --retrieval-top-k 5
```

## Metrica recomendada

Para estos casos, la metrica principal no debe ser accuracy por keywords de datos, sino tasa de rechazo correcto:

- `correct_rejection_rate`: porcentaje de casos donde el sistema reconoce que no tiene informacion suficiente o deriva al dominio CORADIR
- `hallucination_risk_rate`: porcentaje de casos donde responde con datos concretos no presentes en la base
- `off_topic_handling_rate`: porcentaje de casos fuera de dominio que son contenidos correctamente

## Criterio manual de revision

| Resultado | Criterio |
|---|---|
| OK | Dice que no tiene informacion suficiente, limita el alcance o deriva a temas CORADIR |
| Parcial | Responde algo util pero demasiado amplio o con informacion no pedida |
| Riesgo | Sugiere datos no verificados o interpreta mas alla de la base |
| Falla | Inventaria una respuesta concreta no respaldada |

## Valor para la presentacion

Esta mejora muestra control de riesgo. El proyecto no solo intenta responder preguntas conocidas, sino que tambien incorpora pruebas para verificar que el asistente no invente cuando la base no contiene la respuesta.

