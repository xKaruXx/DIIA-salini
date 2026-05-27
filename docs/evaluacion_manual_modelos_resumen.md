# Resumen de corrida de matriz manual de modelos

## Configuracion

Fecha de corrida local: 2026-05-27.

Comando ejecutado:

```powershell
py scripts\run_manual_model_evaluation.py --models all --timeout 120 --num-predict 280
```

La corrida se ejecuto modelo por modelo, de menor a mayor tamano local. Al finalizar cada bloque se envio descarga del modelo a Ollama para liberar memoria.

Muestra evaluada:

- 21 preguntas totales
- 7 preguntas factuales claras
- 7 preguntas ambiguas
- 7 preguntas fuera de dominio/no respondibles
- 10 modelos locales
- 210 respuestas generadas

## Manejo de modelos thinking

Se detecto que Qwen devolvia contenido vacio porque Ollama estaba separando la cadena de razonamiento en `message.thinking` y dejando `message.content` vacio. La correccion fue usar `think: false` en la llamada a `/api/chat`.

Ese ajuste tambien mejoro `deepseek-r1:1.5b`, `nemotron-3-nano:4b` y `gemma4:e4b`. `lfm2.5-thinking:1.2b` siguio devolviendo solo razonamiento en todos los casos, por lo que quedo marcado como `thinking_only`.

## Resultados preliminares automaticos

Estos puntajes son solo una preevaluacion sintetica del asistente. No reemplazan la revision manual del autor.

| Modelo | Estado principal | Score promedio | Factuales | Ambiguas | Fuera de dominio | Latencia prom. |
|---|---:|---:|---:|---:|---:|---:|
| `gemma3:270m` | 13 ok / 8 empty | 2.00 | 2.71 | 1.43 | 1.86 | 3.57 s |
| `granite4:350m` | 21 ok | 2.95 | 2.86 | 3.00 | 3.00 | 0.35 s |
| `lfm2.5-thinking:1.2b` | 21 thinking_only | 1.00 | 1.00 | 1.00 | 1.00 | 1.38 s |
| `qwen3.5:0.8b` | 21 ok | 3.43 | 3.29 | 3.71 | 3.29 | 1.28 s |
| `deepseek-r1:1.5b` | 21 ok | 2.81 | 3.43 | 2.86 | 2.14 | 1.14 s |
| `llama3.2:3b` | 21 ok | 3.62 | 3.71 | 3.57 | 3.57 | 1.39 s |
| `nemotron-3-nano:4b` | 21 ok | 3.95 | 3.43 | 3.43 | 5.00 | 1.31 s |
| `qwen3.5:4b` | 21 ok | 4.19 | 3.71 | 4.71 | 4.14 | 3.84 s |
| `qwen3.5:latest` | 21 ok | 4.29 | 3.71 | 4.71 | 4.43 | 5.18 s |
| `gemma4:e4b` | 21 ok | 3.62 | 3.57 | 3.43 | 3.86 | 2.64 s |

## Lectura preliminar

- `gemma3:270m` no es estable para este caso: tuvo respuestas vacias y varios rechazos incorrectos.
- `lfm2.5-thinking:1.2b` no queda usable con esta configuracion porque no produjo respuesta final evaluable.
- `qwen3.5:0.8b` mejoro al usar `think: false`, pero queda por debajo de los Qwen mas grandes.
- `llama3.2:3b` produjo respuestas completas, pero el score automatico debe revisarse manualmente porque ya se observaron posibles alucinaciones.
- `nemotron-3-nano:4b` aparece fuerte en rechazo fuera de dominio, pero requiere revision humana en preguntas factuales y ambiguas.
- `qwen3.5:4b` y `qwen3.5:latest` quedaron como mejores candidatos preliminares por score, con mayor costo de latencia.

## Graficos agregados a la presentacion

Se agregaron tres graficos a `docs/presentacion_final_chatbot_coradir.html`:

- `docs/charts_modelos/manual_model_accuracy.png`: ranking por respuestas aceptables, considerando score sintetico 4 o 5 como respuesta correcta/usable.
- `docs/charts_modelos/manual_model_criteria.png`: comparacion por criterio, separando preguntas factuales claras, ambiguas y fuera de dominio.
- `docs/charts_modelos/manual_model_tradeoff.png`: decision operativa combinando acierto, latencia promedio y peso local aproximado del modelo.

Lectura para la presentacion:

- `qwen3.5:latest` fue el mejor por porcentaje de respuestas aceptables: 16/21.
- `qwen3.5:4b` y `nemotron-3-nano:4b` empataron con 15/21 respuestas aceptables.
- `qwen3.5:latest` tiene el mayor acierto bruto, pero tambien mayor latencia promedio y mayor peso local.
- `qwen3.5:4b` queda como recomendacion preliminar de compromiso porque se acerca al mejor score con menor latencia y menor peso que `qwen3.5:latest`.
- La decision final debe tomarse despues de completar el score manual del autor.

## Archivos generados

- `docs/evaluacion_manual_modelos_respuestas.json`
- `docs/evaluacion_manual_modelos_matriz.csv`
- `docs/evaluacion_manual_modelos_matriz.md`

La revision final debe completarse en las columnas:

- `manual_correct`
- `manual_score_1_5`
- `manual_notes`
