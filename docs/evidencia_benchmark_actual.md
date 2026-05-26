# Evidencia de Benchmark Actual

## Resumen ejecutivo

El benchmark actual fue ejecutado localmente el 2026-05-20 sobre 15 consultas representativas del dominio CORADIR Movilidad Electrica. Las variantes de prompt `strict` y `sales` aprobaron todos los casos, con accuracy de 100.0% y latencia promedio registrada de 0.01 segundos.

Esta evidencia demuestra que el MVP responde correctamente el conjunto cerrado de preguntas definido para la validacion inicial. Sin embargo, la medicion actual verifica palabras clave en la respuesta final; todavia no mide calidad de retrieval, orden de documentos recuperados ni fidelidad factual completa.

## Configuracion evaluada

| Elemento | Valor |
|---|---|
| Fecha de ejecucion | 2026-05-20 |
| Casos de prueba | 15 |
| Dataset de evaluacion | `dataset/evaluacion_mvp.json` |
| Script de evaluacion | `scripts/run_benchmark.py` |
| Modelo de chat | `qwen3.5:latest` |
| Proveedor LLM | `ollama` |
| Modelo de embeddings | `nomic-embed-text:latest` |
| Proveedor embeddings | `ollama` |
| Reporte ejecutado `strict` | `docs/benchmark_real_strict_qwen35_latest.json` |
| Reporte ejecutado `sales` | `docs/benchmark_real_sales_qwen35_latest.json` |

## Modelos disponibles en Ollama

Al momento de la evaluacion, `ollama list` informo:

| Modelo | Tamaño aproximado | Uso en esta evaluacion |
|---|---:|---|
| `qwen3.5:latest` | 6.6 GB | chat |
| `gemma4:e4b` | 9.6 GB | disponible, no usado |
| `nomic-embed-text:latest` | 274 MB | embeddings |
| `nomic-embed-text-v2-moe:latest` | 957 MB | disponible, no usado |

## Resultados globales

| Variante | Casos aprobados | Accuracy | Latencia promedio |
|---|---:|---:|---:|
| `strict` | 15/15 | 100.0% | 0.01 s |
| `sales` | 15/15 | 100.0% | 0.01 s |

La vista grafica del benchmark esta disponible en `docs/evaluacion_visual_benchmark.md`.

Comandos ejecutados:

```powershell
py scripts\run_benchmark.py --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text:latest --output docs\benchmark_real_strict_qwen35_latest.json
py scripts\run_benchmark.py --prompt-variant sales --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text:latest --output docs\benchmark_real_sales_qwen35_latest.json
```

Durante la ejecucion aparecieron advertencias de telemetria de Chroma y deprecaciones de LangChain/Chroma. No impidieron la ejecucion ni generaron casos fallidos, pero quedan como deuda tecnica para una iteracion posterior.

## Casos evaluados

| # | ID | Categoria | Pregunta | Resultado `strict` | Resultado `sales` |
|---:|---|---|---|---|---|
| 1 | `tito_s5_autonomia_carga` | vehiculos | ¿Cuanta autonomia tiene el TITO S5 y como se carga? | OK | OK |
| 2 | `tito_s5_aa_precio` | precios | ¿Cual es el precio del TITO S5-300 AA? | OK | OK |
| 3 | `tita_s2_capacidad` | vehiculos | ¿Que capacidad de carga y de pasajeros tiene la TITA S2-300? | OK | OK |
| 4 | `tita_furgon_refrigerado_precio` | precios | ¿Cuanto cuesta la TITA S2 300 AA con furgon refrigerado? | OK | OK |
| 5 | `chiki_autonomia_velocidad` | vehiculos | ¿Que autonomia y velocidad maxima tiene el CHIKI de litio? | OK | OK |
| 6 | `barre_tita_capacidad` | vehiculos | ¿Cual es la capacidad de trabajo y el tanque de agua de la BARRE-TITA? | OK | OK |
| 7 | `garantia` | posventa | ¿Que garantia tienen los vehiculos? | OK | OK |
| 8 | `reclamos_servicio` | posventa | ¿Donde hago un reclamo o pido servicio tecnico? | OK | OK |
| 9 | `leasing_suspendido` | comercial | ¿Tienen leasing o alquiler con opcion a compra? | OK | OK |
| 10 | `beneficio_discapacidad` | beneficios | ¿Como es el tramite por beneficio de discapacidad? | OK | OK |
| 11 | `agencia_san_luis` | agencias | ¿Tienen agencia oficial en San Luis? | OK | OK |
| 12 | `carga_rapida` | carga | ¿Que ventaja ofrece la carga rapida? | OK | OK |
| 13 | `instalacion_carga` | carga | ¿Necesito una instalacion especial para cargar un vehiculo? | OK | OK |
| 14 | `reserva_entrega` | compra | ¿Como funciona la reserva y la entrega inmediata? | OK | OK |
| 15 | `telefono_ventas` | contacto | ¿Cual es el telefono de ventas de movilidad electrica? | OK | OK |

## Lectura de resultados

El benchmark cubre las areas principales del dominio:

- vehiculos y fichas tecnicas
- precios
- posventa
- condiciones comerciales
- beneficios
- agencias
- carga
- compra y contacto

La aprobacion de todos los casos indica que el sistema encuentra y devuelve los datos esperados para las preguntas frecuentes priorizadas. Esto respalda las mejoras ya documentadas: preprocesamiento de la base, recuperacion granular, capa extractiva factual y variantes de prompt.

## Limitaciones de esta evidencia

La evidencia actual no debe interpretarse como una evaluacion completa de produccion. Sus limites principales son:

- el conjunto de prueba es cerrado y pequeno
- las preguntas fueron definidas manualmente
- la validacion se basa en palabras clave esperadas
- no se registra el documento recuperado por consulta
- no se mide si el documento correcto aparece en la posicion 1
- no se calcula Precision@K, Recall@K ni MRR
- no hay evaluacion formal de faithfulness
- no se prueban conversaciones largas ni ambiguedad de usuarios reales

## Mejoras de evaluacion recomendadas

Para alinear mejor la evidencia con el material de clases, el siguiente benchmark deberia agregar:

| Mejora de evaluacion | Objetivo |
|---|---|
| `expected_sources` por caso | Saber que documento deberia recuperarse |
| Top-K de documentos recuperados | Auditar el retrieval |
| Precision@K | Medir ruido en el contexto |
| MRR | Medir si el primer documento relevante aparece arriba |
| Casos fuera de dominio | Validar rechazos correctos |
| Revision manual de faithfulness | Verificar si cada afirmacion esta respaldada por fuente |

## Conclusion

El benchmark actual es suficiente como evidencia inicial de MVP: demuestra que el sistema responde correctamente preguntas frecuentes representativas. Para una evaluacion academica mas robusta, el proximo paso es separar la medicion de respuesta final de la medicion de retrieval, siguiendo el enfoque del material de clase sobre RAG simple vs. RAG mejorado.
