# Plan de Mejoras del Sistema

## 1. Resumen ejecutivo

Este documento registra las mejoras aplicadas y planificadas sobre el chatbot de CORADIR Movilidad Electrica. Su objetivo es dejar trazabilidad academica y tecnica de cada cambio relevante, siguiendo el criterio trabajado en clase: toda mejora debe estar asociada a un problema, una decision tecnica, una evidencia y una metrica de comparacion.

El sistema actual ya cuenta con un MVP funcional de chat web, backend FastAPI, base de conocimiento cerrada, preprocesamiento reproducible, recuperacion RAG y benchmark automatizado. La prioridad inmediata no es agregar mas funcionalidades, sino documentar con claridad que mejoras ya existen, que impacto tuvieron y que nuevas mediciones faltan para robustecer la evaluacion.

La mejora central del proyecto fue pasar de una base JSON jerarquica, poco conveniente para recuperacion semantica directa, a una base de documentos mas pequenos y semanticamente coherentes. Sobre esa base se agregaron recuperacion hibrida, capa extractiva para consultas factuales, variantes de prompt y validacion automatizada con casos representativos.

## 2. Criterio tomado del material de clases

El material de clases insiste en cuatro principios que guian este plan:

1. Definir un baseline antes de afirmar que existe una mejora.
2. Comparar cada mejora contra metricas o evidencia observable.
3. Documentar cada hallazgo y explicar que implica para el modelo.
4. Separar resumen ejecutivo de detalle tecnico.

En particular, los materiales de RAG simple vs. RAG mejorado muestran que la mejora no debe describirse solo como "se cambio el sistema", sino como una comparacion entre dos versiones:

- version simple o baseline
- version mejorada
- metrica comparativa
- explicacion del cambio que produjo la diferencia

El material incorporado de clase 4 agrega un criterio adicional para este proyecto: separar explicitamente las fallas de retrieval de las fallas de generacion, y revisar la calidad del corpus antes de indexarlo mediante controles como TTR, MATTR, longitud de chunks, densidad informacional y metadata disponible. El detalle de estas mejoras queda registrado en `docs/mejoras_derivadas_clase_4.md`.

## 3. Estado actual del sistema

### 3.1 Componentes principales

El MVP actual esta compuesto por:

- interfaz web de chat en `chat_assets/`
- backend `FastAPI` en `api/main.py`
- logica conversacional y RAG en `api/chat_service.py`
- base de conocimiento original en `dataset/dataset_movilidad.json`
- base preprocesada en `dataset/knowledge_base_movilidad.jsonl`
- script de preprocesamiento en `scripts/prepare_dataset.py`
- benchmark reproducible en `scripts/run_benchmark.py`
- resultados de evaluacion en `docs/benchmark_strict.json` y `docs/benchmark_sales.json`

### 3.2 Configuracion validada

La validacion documentada se realizo con:

- proveedor LLM: `ollama`
- modelo de chat por defecto: `qwen3.5:0.8b`
- modelo de chat fallback: `qwen3.5:latest`
- proveedor de embeddings: `ollama`
- modelo de embeddings: `nomic-embed-text:latest`
- variantes de prompt evaluadas: `strict` y `sales`
- casos de evaluacion: 15

### 3.3 Baseline actual documentado

El baseline operativo actual se toma como la version del MVP evaluada con `scripts/run_benchmark.py`.

| Elemento | Valor actual |
|---|---:|
| Casos de prueba | 15 |
| Documentos RAG generados | 111 |
| Accuracy `strict` | 100.0% |
| Accuracy `sales` | 100.0% |
| Latencia promedio `strict` | 0.01 s |
| Latencia promedio `sales` | 0.01 s |
| Metrica actual | coincidencia de palabras clave esperadas |

Importante: este baseline valida que la respuesta final contenga palabras clave esperadas. Todavia no mide en forma separada la calidad del retrieval, la posicion del documento correcto, la fidelidad factual completa ni la satisfaccion del usuario.

La evidencia ejecutiva del benchmark ejecutado localmente el 2026-05-20 queda documentada en `docs/evidencia_benchmark_actual.md`. Los reportes generados son:

- `docs/benchmark_real_strict_qwen35_latest.json`
- `docs/benchmark_real_sales_qwen35_latest.json`

## 4. Tabla general de mejoras

| Mejora | Estado | Archivo principal | Evidencia actual | Metrica actual | Proxima metrica recomendada |
|---|---|---|---|---|---|
| Preprocesamiento JSON a JSONL | Implementada | `scripts/prepare_dataset.py` | `dataset/knowledge_base_movilidad.jsonl` | 111 documentos generados | cobertura por seccion y duplicados removidos |
| Recuperacion granular de contexto | Implementada | `api/chat_service.py` | respuestas correctas en benchmark | accuracy por palabras clave | Precision@K y MRR |
| Capa extractiva factual | Implementada | `api/chat_service.py` | respuestas breves con datos concretos | casos benchmark aprobados | faithfulness manual y tasa de alucinacion |
| Variantes de prompt | Implementada | `api/chat_service.py` | `benchmark_strict.json`, `benchmark_sales.json` | accuracy comparada | evaluacion de tono, concision y riesgo comercial |
| Stack local open source | Implementada | `README.md`, `api/chat_service.py` | configuracion Ollama documentada | reproducibilidad local | tiempo de instalacion y uso de recursos |
| Benchmark reproducible | Implementada | `scripts/run_benchmark.py` | reportes JSON generados | accuracy y latencia | metricas RAG por documento recuperado |
| Dataset extendido de evaluacion | Implementada | `dataset/evaluacion_rag_extendida.json` | 64 casos con fuentes esperadas | accuracy extendida 54.7% | Precision@K, MRR y analisis de fallas |
| Evaluacion RAG avanzada | Implementada | `scripts/run_benchmark.py` | `docs/evaluacion_retrieval_extendida.md` | Precision@5, Recall@5, MRR, Top-1 | cruce retrieval vs respuesta |
| Analisis respuesta vs retrieval | Implementada | `docs/analisis_fallas_respuesta_vs_retrieval.md` | 24 de 29 fallas tenian fuente en top 5 | clasificacion de fallas | mejorar capa extractiva |
| Extraccion contextual por bloques | Implementada | `api/chat_service.py` | `docs/mejora_extraccion_contextual.md` | accuracy extendida 100.0% en 64 casos | validar con muestras nuevas |
| EDA de chunks y riqueza lexica | Implementada | `scripts/analyze_rag_corpus.py` | `docs/eda_corpus_rag.md` | TTR, MATTR, longitud y densidad por documento | revisar outliers y metadata |
| Metadatos de dominio para retrieval | Pendiente | `scripts/prepare_dataset.py` | `section`, `title`, `source_path` | trazabilidad basica | filtros por entidad, provincia, topico y tipo de respuesta |
| Casos sin respuesta en el corpus | Implementada parcial | `dataset/evaluacion_no_respondibles.json` | `docs/evaluacion_no_respondibles.md` | dataset y reporte retrieval-only | tasa de rechazo correcto con LLM activo |
| Evaluacion de modelos livianos | Implementada parcial | `scripts/run_model_efficiency_matrix.py` | `docs/evaluacion_modelos_livianos.md` | 100% en benchmark MVP para modelos locales | validar no respondibles y casos ambiguos |
| Guardrail para casos por fuera | Implementada | `api/chat_service.py` | `docs/evaluacion_modelos_fuera_dominio.md` | 100% en dataset no respondible | ampliar casos ambiguos reales |
| Evaluacion de embeddings locales | Implementada | `scripts/run_embedding_efficiency_matrix.py` | `docs/evaluacion_embeddings_locales.md` | Recall@5, MRR y Top-1 vectorial | repetir benchmark final con embedding elegido |
| Revision de codificacion de reportes | Implementada | `docs/benchmark_strict.json`, `docs/benchmark_sales.json` | textos de benchmark legibles | marcadores mojibake removidos | mantener verificacion al regenerar benchmarks |

## 5. Reportes ejecutivos por mejora

### Mejora 01 - Preprocesamiento de la base de conocimiento

#### Resumen ejecutivo

La base original estaba organizada como un JSON jerarquico util para administracion, pero poco conveniente para un sistema RAG. Se implemento un proceso de transformacion que genera documentos textuales mas pequenos, independientes y semanticamente coherentes. Esto permite que el sistema recupere fragmentos mas precisos y reduzca el ruido enviado al modelo.

#### Problema detectado

El archivo `dataset/dataset_movilidad.json` contiene informacion institucional, vehiculos, precios, agencias, preguntas frecuentes y condiciones comerciales dentro de una estructura anidada. Si esa estructura se indexa de forma directa, una consulta puede recuperar bloques demasiado grandes o mezclar informacion de temas distintos.

#### Cambio implementado

Se implemento `scripts/prepare_dataset.py`, que:

- lee el dataset original
- normaliza claves y contenido textual
- transforma secciones del JSON en documentos independientes
- genera identificadores y rutas de origen
- exporta el resultado a `dataset/knowledge_base_movilidad.jsonl`

#### Evidencia actual

El proceso genera 111 documentos indexables. Cada documento conserva titulo, seccion, contenido y ruta de origen, lo que mejora la trazabilidad del contexto usado por el chatbot.

#### Limitaciones

La mejora todavia no tiene una metrica especifica de calidad de retrieval. Actualmente se infiere su impacto a partir del benchmark final de respuestas.

#### Proximo paso

Agregar una evaluacion que indique, para cada pregunta, que documento deberia recuperarse y en que posicion aparece.

### Mejora 02 - Recuperacion granular de contexto

#### Resumen ejecutivo

El sistema utiliza documentos mas chicos y enfocados para recuperar informacion de forma mas precisa. Esta mejora busca que el modelo reciba contexto relevante y no bloques extensos con informacion mezclada.

#### Problema detectado

En un RAG, si el contexto recuperado incluye ruido, el modelo puede responder con informacion incompleta, mezclar datos de modelos distintos o agregar texto innecesario. Esto es especialmente riesgoso en consultas de precios, autonomia, garantia, agencias y condiciones comerciales.

#### Cambio implementado

La logica de `api/chat_service.py` combina busqueda por palabras clave y contexto recuperado sobre la base preprocesada. La recuperacion trabaja sobre los documentos generados en `knowledge_base_movilidad.jsonl`, en lugar de depender del JSON jerarquico completo.

#### Evidencia actual

El benchmark actual valida 15 preguntas representativas y ambas variantes evaluadas, `strict` y `sales`, obtienen 15/15 casos aprobados.

#### Limitaciones

La metrica actual evalua si la respuesta contiene palabras clave esperadas, pero no registra que documentos fueron recuperados ni si el documento correcto aparecio primero.

#### Proximo paso

Extender `scripts/run_benchmark.py` para guardar documentos recuperados por consulta y calcular:

- Precision@K
- MRR
- Top-1 del documento esperado

### Mejora 03 - Capa extractiva para consultas factuales

#### Resumen ejecutivo

Se agrego una capa extractiva previa al uso generativo del LLM para responder consultas factuales con lineas directamente tomadas del contexto. Esta mejora reduce el riesgo de alucinacion en datos concretos, como precios, autonomia, telefonos, tiempos de carga o condiciones comerciales.

#### Problema detectado

Los LLMs pueden redactar respuestas convincentes pero incorrectas. En este caso de uso, una cifra mal respondida puede afectar una consulta comercial o tecnica.

#### Cambio implementado

En `api/chat_service.py` existen funciones orientadas a busqueda por terminos, extraccion de lineas relevantes y armado de respuesta extractiva. El flujo intenta producir una respuesta factual antes de depender completamente de la generacion libre.

#### Evidencia actual

Los casos de benchmark sobre precios, autonomia, garantia, carga, agencias y telefonos pasan la validacion por palabras clave.

#### Limitaciones

Algunas respuestas pueden incluir mas lineas de las necesarias. Por ejemplo, una respuesta factual puede traer informacion complementaria que tambien estaba cerca del fragmento recuperado.

#### Proximo paso

Agregar una revision manual de faithfulness para 10 respuestas:

| Consulta | Respuesta | Fuente recuperada | Fiel a la fuente | Observacion |
|---|---|---|---|---|

La matriz inicial para esa revision queda preparada en `docs/matriz_revision_factual.md`.

### Mejora 04 - Variantes de prompt

#### Resumen ejecutivo

El sistema permite comparar distintos comportamientos conversacionales sin modificar la arquitectura. Esto separa la evaluacion del prompt de la evaluacion del pipeline.

#### Problema detectado

Un mismo sistema puede necesitar distintos tonos segun el objetivo: informacion neutral, orientacion comercial o precision estricta. Si el tono esta fijo en el codigo, no se puede comparar el impacto del prompt.

#### Cambio implementado

Se incorporo la variable `PROMPT_VARIANT` con tres valores:

- `baseline`: respuesta general informativa
- `sales`: respuesta con orientacion comercial
- `strict`: respuesta orientada a precision factual

#### Evidencia actual

Existen reportes de benchmark para:

- `docs/benchmark_sales.json`
- `docs/benchmark_strict.json`

Ambos obtienen 15/15 casos aprobados con accuracy de 100.0%.

#### Limitaciones

La evaluacion actual no distingue si una variante es mas clara, mas concisa o menos riesgosa en terminos comerciales. Solo mide presencia de palabras clave.

#### Proximo paso

Agregar una tabla cualitativa de comparacion:

| Variante | Precision factual | Tono comercial | Concision | Riesgo de exageracion |
|---|---|---|---|---|

### Mejora 05 - Stack local open source

#### Resumen ejecutivo

El MVP puede ejecutarse localmente con Ollama, evitando dependencia obligatoria de servicios pagos para la demo academica. Esto mejora reproducibilidad, control de costos y autonomia tecnica.

#### Problema detectado

Una solucion dependiente solo de APIs externas puede presentar costos, requisitos de credenciales o fallas de disponibilidad durante una demostracion.

#### Cambio implementado

La configuracion actual permite usar:

- `qwen3.5:latest` como modelo de chat
- `nomic-embed-text:latest` como modelo de embeddings
- `Ollama` como proveedor local

#### Evidencia actual

El README y la guia de demo documentan los comandos necesarios para descargar modelos, generar la base de conocimiento y ejecutar el sistema localmente.

#### Limitaciones

El flujo de audio sigue fuera del nucleo open source del MVP. Ademas, el rendimiento local depende del equipo donde se ejecute.

#### Proximo paso

Registrar tiempos de instalacion, consumo aproximado y requerimientos minimos para demo.

### Mejora 06 - Benchmark reproducible

#### Resumen ejecutivo

Se implemento un benchmark automatizado con 15 casos representativos del dominio. Esto permite repetir la evaluacion despues de cada cambio y detectar regresiones.

#### Problema detectado

Sin benchmark, la evaluacion del chatbot queda sujeta a pruebas manuales aisladas. Eso dificulta demostrar mejoras o detectar si una modificacion empeora respuestas previas.

#### Cambio implementado

El script `scripts/run_benchmark.py` ejecuta los casos de `dataset/evaluacion_mvp.json`, valida palabras clave esperadas, calcula accuracy y latencia promedio, y guarda un reporte JSON.

#### Evidencia actual

Resultados registrados:

- `strict`: 15/15 casos aprobados, 100.0% accuracy, 0.01 s de latencia promedio
- `sales`: 15/15 casos aprobados, 100.0% accuracy, 0.01 s de latencia promedio

El resumen legible de estos resultados se encuentra en `docs/evidencia_benchmark_actual.md`. Esta evaluacion fue ejecutada con `qwen3.5:latest` y `nomic-embed-text:latest` sobre Ollama local.

#### Limitaciones

El benchmark todavia no evalua:

- documento recuperado correcto
- orden del ranking
- fidelidad completa de la respuesta
- consultas ambiguas
- consultas fuera de dominio con expectativa explicita
- calidad de redaccion

#### Proximo paso

Crear una version extendida del benchmark que guarde evidencia de retrieval y permita calcular metricas RAG.

## 6. Mejoras pendientes priorizadas

### Prioridad 1 - Medir retrieval

Agregar al dataset de evaluacion un campo opcional con documentos o secciones esperadas:

```json
{
  "id": "tito_s5_autonomia_carga",
  "expected_sources": ["vehiculos_detalles.TITO"]
}
```

Luego extender el benchmark para guardar los documentos recuperados y calcular si el documento esperado aparece en el top K.

Estado actualizado: implementado parcialmente. `scripts/run_benchmark.py` ya guarda `retrieved_documents` y calcula `Precision@K`, `Recall@K`, `MRR` y `Top-1 source accuracy` cuando el caso incluye `expected_sources`. La primera corrida en modo retrieval-only queda documentada en `docs/evaluacion_retrieval.md`.

### Prioridad 2 - Mantener codificacion legible en reportes

Los reportes `docs/benchmark_strict.json` y `docs/benchmark_sales.json` fueron normalizados para dejar preguntas y respuestas legibles. La recomendacion queda como control de calidad para futuras regeneraciones de benchmark.

Accion recomendada:

- revisar que no reaparezcan marcadores como `Ã`, `Â` o `â`
- regenerar los reportes si se actualiza el dataset de evaluacion
- mantener preguntas y respuestas legibles para anexos ejecutivos

### Prioridad 3 - Agregar revision manual de faithfulness

Seleccionar 10 preguntas criticas y documentar:

- respuesta del sistema
- fuente recuperada
- si cada afirmacion esta respaldada por la fuente
- observacion manual

### Prioridad 4 - Evaluar consultas fuera de dominio

Agregar casos donde el sistema debe rechazar o derivar correctamente:

- preguntas no relacionadas con CORADIR
- consultas legales no cubiertas
- pedidos de informacion no presente en la base

### Prioridad 5 - Reducir respuestas con informacion adicional innecesaria

Algunas respuestas extractivas pueden incluir datos correctos pero no pedidos. La mejora buscaria respuestas mas concisas, especialmente para precios, garantia y autonomia.

### Prioridad 6 - Analizar riqueza lexica y calidad de chunks

El material de clase 4 sobre TTR, MATTR y lematizacion permite agregar una mejora nueva: medir la calidad del corpus preprocesado antes de indexarlo. La accion recomendada es generar un reporte sobre `dataset/knowledge_base_movilidad.jsonl` con longitud por documento, TTR, MATTR y deteccion de documentos demasiado cortos, demasiado largos o redundantes.

La decision de lematizar no deberia asumirse automaticamente. En este dominio hay nombres propios, modelos, versiones y terminos comerciales donde una normalizacion agresiva podria dañar la precision. Primero conviene medir y luego decidir si hace falta lematizacion, subdivision de documentos o enriquecimiento de metadatos.

Estado actualizado: implementado. El script `scripts/analyze_rag_corpus.py` genera `docs/eda_corpus_rag.md`, `docs/eda_corpus_rag.json` y graficos en `docs/charts_corpus/`.

### Prioridad 7 - Enriquecer metadata para filtros de retrieval

El proyecto ya conserva `section`, `title` y `source_path`. A partir del material de RAG simple vs. RAG mejorado, conviene documentar como mejora futura la incorporacion de metadatos de dominio:

- tipo de entidad: vehiculo, precio, agencia, FAQ o condicion comercial
- nombre de vehiculo cuando aplique
- provincia o localidad para agencias
- topico principal: garantia, carga, reserva, leasing, beneficios
- tipo de respuesta esperada: precio, especificacion, contacto o condicion

Esto permitiria probar filtros pre-ranking o re-ranking simple antes de enviar contexto al LLM.

### Prioridad 8 - Agregar casos no respondibles

La clase 4 recomienda probar preguntas que no tienen respuesta en el corpus para verificar si el sistema rechaza o deriva correctamente. El benchmark extendido deberia sumar casos con `answerability=not_answerable` para medir tasa de rechazo correcto y riesgo de alucinacion.

Estado actualizado: implementado parcialmente. Se agrego `dataset/evaluacion_no_respondibles.json` y la metodologia queda documentada en `docs/evaluacion_no_respondibles.md`. Falta correr la evaluacion completa de respuesta cuando Ollama este disponible.

### Prioridad 9 - Evaluar modelos livianos y costo de hardware

Para exprimir mejor el recurso local, se agrega una mejora orientada a eficiencia: comparar el modelo actual contra candidatos mas chicos usando exactamente el mismo benchmark. La hipotesis es que, como el sistema ya usa recuperacion de contexto y capa extractiva, muchas preguntas frecuentes podrian resolverse con un modelo de menor tamano.

Se agrego `scripts/run_model_efficiency_matrix.py` para ejecutar una matriz de modelos de Ollama y guardar reportes en `docs/benchmarks_modelos_livianos/`. La metodologia y criterios de decision quedan documentados en `docs/optimizacion_hardware_modelos.md`.

Estado actualizado: implementado sobre el benchmark MVP. Todos los modelos locales evaluados obtuvieron 15/15 casos correctos, lo que sugiere que las rutas factuales pueden funcionar con modelos chicos. La evidencia queda en `docs/evaluacion_modelos_livianos.md`.

Tambien se agrego un guardrail para casos fuera de dominio o no presentes en el corpus. Despues de esa mejora, los modelos candidatos obtuvieron 6/6 en el dataset de no respondibles. La evidencia queda en `docs/evaluacion_modelos_fuera_dominio.md`.

### Prioridad 10 - Evaluar embeddings locales

Se agrego `scripts/run_embedding_efficiency_matrix.py` para comparar embeddings locales en modo vector-only. Esta evaluacion permite medir directamente la calidad del retrieval semantico sin que la busqueda lexical o la respuesta final oculten diferencias.

Estado actualizado: implementado. `embeddinggemma:latest` obtuvo el mejor `MRR` y `Top-1`, mientras que `qwen3-embedding:0.6b` obtuvo el mejor `Recall@5`. La evidencia queda en `docs/evaluacion_embeddings_locales.md`.

## 7. Plan de trabajo recomendado

| Orden | Paso | Resultado esperado |
|---:|---|---|
| 1 | Consolidar este documento como bitacora viva | mejoras trazables |
| 2 | Mantener codificacion legible en benchmarks | reportes presentables |
| 3 | Regenerar benchmarks actuales si cambia el dataset | baseline limpio |
| 4 | Agregar fuentes esperadas por caso | base para Precision@K y MRR |
| 5 | Extender `run_benchmark.py` con retrieval | metricas RAG |
| 6 | Crear tabla de faithfulness manual | evidencia cualitativa |
| 7 | Crear EDA de chunks con TTR/MATTR | control de calidad del corpus |
| 8 | Enriquecer metadata de dominio | filtros y diagnostico de retrieval |
| 9 | Agregar casos no respondibles | medir rechazo correcto |
| 10 | Evaluar modelos livianos | reducir hardware sin perder calidad |
| 11 | Evaluar embeddings locales | mejorar retrieval vectorial |
| 12 | Integrar resumen en `reporte_final_implementacion.md` | informe final mas robusto |

## 8. Criterio de cierre academico

El proyecto queda mejor alineado con el material de clases si el informe final puede responder, para cada mejora:

- cual era el problema inicial
- cual fue el baseline
- que se cambio
- que evidencia demuestra la mejora
- que metrica se uso
- que limitacion queda pendiente

Con la documentacion actual, el MVP ya tiene evidencia funcional. El siguiente salto de calidad es separar la evaluacion de respuesta final de la evaluacion de retrieval, porque esa distincion permite explicar con mas rigor por que el sistema responde bien y donde podria fallar.
