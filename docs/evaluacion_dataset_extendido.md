# Evaluacion con Dataset Extendido

## Resumen ejecutivo

Se amplio el benchmark de 15 a 64 muestras usando informacion ya presente en `dataset/dataset_movilidad.json`. El nuevo archivo es:

- `dataset/evaluacion_rag_extendida.json`

El objetivo no fue construir un set facil, sino aumentar cobertura y sensibilidad para detectar fallas reales del sistema. El resultado cambio de 100.0% en el benchmark MVP a 54.7% en el benchmark extendido.

Esto es una mejora metodologica: ahora el benchmark permite ver limites que antes quedaban ocultos.

## Estructura del nuevo dataset

Cada muestra contiene:

- `id`: identificador estable del caso
- `category`: categoria funcional
- `question`: pregunta de usuario
- `expected_keywords`: palabras clave que deben aparecer en la respuesta
- `expected_sources`: fuentes esperadas dentro de la base de conocimiento

El campo `expected_sources` prepara el dataset para una futura medicion de retrieval con Precision@K y MRR.

## Distribucion de casos

| Categoria | Casos |
|---|---:|
| vehiculos | 22 |
| precios | 12 |
| agencias | 6 |
| compra | 5 |
| empresa | 5 |
| carga | 4 |
| posventa | 2 |
| movilidad | 2 |
| app | 2 |
| comercial | 1 |
| beneficios | 1 |
| contacto | 1 |
| sitios_web | 1 |
| **Total** | **64** |

## Resultados comparativos

Se ejecuto el benchmark extendido con `qwen3.5:latest`, prompt `strict` y dos modelos de embeddings.

| Embedding | Casos aprobados | Accuracy | Latencia promedio |
|---|---:|---:|---:|
| `nomic-embed-text:latest` | 35/64 | 54.7% | 0.01 s |
| `nomic-embed-text-v2-moe:latest` | 35/64 | 54.7% | 0.01 s |

Reportes generados:

- `docs/benchmark_extendido_strict_qwen35_nomic_text.json`
- `docs/benchmark_extendido_strict_qwen35_nomic_v2_moe.json`

Graficos generados:

- `docs/evaluacion_visual_benchmark_extendido.md`
- `docs/charts_extendido/`

## Resultados por categoria

| Categoria | Aprobados | Total | Accuracy |
|---|---:|---:|---:|
| agencias | 1 | 6 | 16.7% |
| app | 0 | 2 | 0.0% |
| beneficios | 1 | 1 | 100.0% |
| carga | 3 | 4 | 75.0% |
| comercial | 1 | 1 | 100.0% |
| compra | 3 | 5 | 60.0% |
| contacto | 1 | 1 | 100.0% |
| empresa | 2 | 5 | 40.0% |
| movilidad | 0 | 2 | 0.0% |
| posventa | 2 | 2 | 100.0% |
| precios | 11 | 12 | 91.7% |
| sitios_web | 1 | 1 | 100.0% |
| vehiculos | 9 | 22 | 40.9% |

## Lectura tecnica

El empate entre embeddings indica que, con la metrica actual, el problema no esta principalmente en elegir `nomic-embed-text` o `nomic-embed-text-v2-moe`.

Las fallas aparecen sobre todo en:

- preguntas de vehiculos con detalles muy especificos
- agencias puntuales por ciudad/provincia
- informacion institucional o de apps
- condiciones de compra expresadas con frases exactas

Esto sugiere tres hipotesis:

1. La capa extractiva y la busqueda por keywords no recuperan bien todos los segmentos nuevos.
2. Algunas respuestas pueden ser correctas parcialmente, pero no contienen exactamente las keywords esperadas.
3. Hace falta medir retrieval directamente para saber si falla la recuperacion o la redaccion final.

## Decision recomendada

Mantener ambos benchmarks:

- `dataset/evaluacion_mvp.json`: benchmark corto para demo y regresion rapida.
- `dataset/evaluacion_rag_extendida.json`: benchmark exigente para detectar mejoras reales.

No conviene ajustar el sistema para "pasar" el benchmark extendido sin analizar antes cada falla. El valor de este dataset es mostrar donde el sistema todavia necesita trabajo.

## Proximos pasos

1. Agregar al benchmark la captura de documentos recuperados por consulta.
2. Calcular Precision@K y MRR usando `expected_sources`.
3. Revisar manualmente los casos fallidos para separar:
   - falla de retrieval
   - respuesta parcial
   - keyword demasiado estricta
   - dato ausente o mal segmentado
4. Mejorar el pipeline de recuperacion y volver a ejecutar el benchmark extendido.
