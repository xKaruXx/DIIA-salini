# Presentacion Final - Chatbot RAG CORADIR

## Trabajo final - Chatbot RAG para CORADIR Movilidad Electrica

El proyecto no se centro solo en hacer responder a un LLM: transformo una base administrativa en un corpus RAG medible, recuperable y auditable.

- Base de conocimiento cerrada, curada y reprocesada.
- Corpus JSONL con documentos mas chicos, trazables y orientados a retrieval.
- Benchmark reproducible con metricas de respuesta y metricas de recuperacion.
- La mejora de respuesta aparece como consecuencia del trabajo sobre datos, retrieval y guardrails.

## 1. Problema - La informacion existia, pero no era evidencia recuperable

El punto critico era de datos: el contenido estaba disponible, pero no estaba preparado para que un RAG encontrara la fuente correcta y respondiera sin mezclar informacion.

### Formato administrativo

El JSON original servia para almacenar catalogo, precios, agencias y FAQs, pero no para recuperar fragmentos semanticos precisos.

### Riesgo factual

Modelos, precios, autonomias y condiciones comerciales podian mezclarse si el contexto llegaba con ruido o demasiado amplio.

### Necesidad de evidencia

La defensa no podia depender de una demo aislada: hacia falta medir corpus, retrieval, respuesta final y limites.

## 2. Datos - Del JSON jerarquico a un corpus RAG auditable

La primera mejora fue convertir datos administrativos en documentos indexables: unidades mas chicas, con sentido propio y con fuente trazable.

### Antes

dataset/dataset_movilidad.json concentraba FAQs, fichas tecnicas, precios, agencias, contactos y condiciones comerciales en una estructura jerarquica.

### Proceso

scripts/prepare_dataset.py normaliza claves, corrige codificacion, separa subsecciones y genera documentos textuales coherentes.

### Despues

dataset/knowledge_base_movilidad.jsonl deja 111 documentos indexables, cada uno orientado a una consulta o dato del dominio.

### Impacto

El retrieval recibe menos ruido, las respuestas quedan mas trazables y los errores pueden diagnosticarse por fuente.

## 3. Documentacion - Decisiones tomadas sobre la documentacion

El trabajo principal fue convertir informacion comercial y tecnica en evidencia recuperable, sin perder trazabilidad hacia la fuente original.

### Granularidad

No indexamos el JSON completo: separamos FAQs, precios, fichas tecnicas, agencias, contactos y condiciones en documentos mas chicos.

### Trazabilidad

Cada chunk conserva `section`, `title` y `source_path`; eso permite saber exactamente que fuente recupero cada pregunta.

### Normalizacion prudente

Corregimos codificacion y espacios, pero no aplicamos lematizacion global porque el EDA no justificaba perder terminos comerciales exactos.

### Evaluacion con fuentes

El dataset extendido agrega `expected_sources`; asi medimos si el retrieval trae el chunk correcto, no solo si la respuesta suena bien.

## 4. EDA - Medimos el corpus antes de cambiar chunking o normalizacion

El EDA permitio decidir con evidencia: no aplicar lematizacion global todavia y priorizar metadata, retrieval y revision de documentos extremos.

- 111 documentos analizados desde knowledge_base_movilidad.jsonl.
- Promedio de 44.21 tokens por documento; mediana de 24 y p90 de 105.
- MATTR promedio: 0.8538, sin senales de baja densidad lexica general.
- Hallazgo: revisar documentos muy largos o muy cortos por seccion antes de fusionar o partir mas chunks.

## 5. Arquitectura - El pipeline queda gobernado por datos, no por prompt

La solucion final recupera evidencia, aplica reglas de alcance y usa generacion solo cuando el contexto ya esta acotado.

- Chroma conserva el indice vectorial local sobre el corpus curado.
- La busqueda lexical ayuda con nombres propios, modelos, precios, telefonos y agencias.
- La capa extractiva resuelve datos factuales antes de delegar al LLM.
- Ollama permite reproducibilidad local sin depender de servicios pagos para la demo.

Flujo: Usuario -> FastAPI -> Clasificacion -> Keyword + vector -> Capa extractiva -> LLM -> Respuesta

## 6. Evaluacion - El benchmark mostro que responder bien no alcanza

La primera medicion validaba el MVP, pero el dataset extendido obligo a separar errores de datos, retrieval, extraccion y redaccion.

- Benchmark MVP: 15/15 casos correctos en variantes strict y sales.
- Benchmark extendido inicial: 35/64 casos correctos.
- El descenso fue util: revelo consultas mas exigentes sobre vehiculos, agencias e informacion institucional.
- Decision metodologica: medir recuperacion de fuentes, no solo keywords en la respuesta.

## 7. Metricas RAG - Medimos retrieval antes de confiar en la respuesta

La decision no se tomo por intuicion: cada pregunta tiene fuentes esperadas y se mide si los chunks recuperados contienen esa evidencia.

### Precision@5

Cuantos de los cinco chunks recuperados son fuentes esperadas. Si baja, hay ruido en contexto.

### Recall@5

Si la fuente esperada aparece en el top 5. Si baja, falta evidencia y hay que corregir retrieval o datos.

### MRR / Top-1

Que tan temprano aparece el chunk correcto. Si baja, el problema es ranking, no necesariamente generacion.

### Overlap y soporte

Se cruza chunk contra pregunta, keywords y respuesta para justificar si el dato usado estaba realmente en contexto.

## 8. Generacion - Clase 6: medimos si la respuesta es correcta y trazable

Sumamos metricas de generacion sobre el benchmark final: Token Overlap confirma la cobertura factual y Context Faithfulness detecta respuestas que conviene revisar por trazabilidad.

- Token Overlap promedio: 1.0 sobre 64 casos, consistente con el 64/64 por keywords.
- Context Faithfulness promedio: 0.8949 contra el contexto recuperado.
- 51/64 casos quedaron en el cuadrante sistema OK: respuesta correcta y respaldada por contexto.
- 13/64 casos mantienen keywords correctas pero requieren revision por contexto no trazado o informacion adicional.

## 9. Retrieval - Auditoria de chunks: que esta recuperando el sistema

Para cada pregunta guardamos top chunks, score/rank, contenido, tokens y si el source_path coincide con la fuente esperada.

- 61/64 casos tienen todas las fuentes esperadas dentro del top 5.
- 63/64 casos tienen al menos una fuente esperada dentro del top 5.
- 56/64 casos tienen una fuente esperada en el primer chunk recuperado.
- Precision@5 promedio: 31.9%; Recall@5 promedio: 96.9%; MRR: 91.6%.
- El CSV permite filtrar chunks con expected_keyword_overlap=0 o matches_expected_source=false.

## 10. Decisiones - Como decidimos ajustes a partir de los chunks

La lectura de metricas separa tres problemas distintos: falta de evidencia, ruido en contexto y respuesta con informacion no trazada.

- Recall alto + Precision baja: el sistema encuentra el dato, pero trae ruido; conviene mejorar ranking y filtros, no cambiar primero el LLM.
- Top-1 de 56/64: la mayoria queda bien ordenada; los casos restantes se marcan como ranking_review.
- Casos missing_expected_source: revisar expected_sources, metadata del corpus o cobertura del dataset.
- Context Faithfulness bajo: revisar capa extractiva para evitar datos adicionales o contexto no trazado.

## 11. Embeddings - Los embeddings se evaluaron por retrieval, no por intuicion

La comparacion local mostro que cambiar embeddings puede mejorar la recuperacion, pero la decision debe validarse contra accuracy final.

- qwen3-embedding:0.6b obtuvo el mejor Recall@5: 81.2%.
- embeddinggemma obtuvo el mejor MRR: 69.5% y Top-1: 60.9%.
- nomic-embed-text fue el mas liviano, pero quedo bajo en retrieval vectorial puro.
- Lectura: el embedding no se elige por marca o tamano, sino por fuentes recuperadas.

## 12. Respuesta - La respuesta mejora porque el contexto llega mejor preparado

El foco no fue maquillar el texto final: se corrigio el camino que lleva evidencia al modelo y se agrego extraccion para datos factuales.

- El benchmark extendido paso de exponer fallas a guiar mejoras concretas del pipeline.
- La mejora de extraccion contextual final llego a 64/64 casos correctos en la corrida documentada.
- La causa tecnica no fue solo prompt: fue corpus granular, fuentes recuperadas y reglas para datos factuales.
- El resultado queda defendible porque se puede rastrear desde pregunta hasta fuente y respuesta.

## 13. Guardrail - Tambien mejoramos cuando decidimos no responder

Los casos por fuera del corpus se resolvieron antes del LLM: si la pregunta no pertenece al dominio o no hay dato disponible, se rechaza de forma controlada.

- Antes del guardrail, la capa extractiva podia traer contexto irrelevante.
- Despues del guardrail, todos los candidatos evaluados lograron 6/6.
- La latencia queda en 0.0 s porque no se llama al LLM.
- Esto reduce alucinaciones y muestra que parte de la calidad viene del diseno del dato y del flujo.

## 14. Demo - Demo: mostrar pregunta, fuente y respuesta

La demo debe reforzar la historia: no probar solo que el bot responde, sino que la respuesta sale de una base curada y de un retrieval medido.

- Preguntar: Cuanta autonomia tiene el TITO S5 y como se carga?
- Preguntar: Cual es el precio del TITO S5-300 AA?
- Preguntar: Donde hago un reclamo o pido servicio tecnico?
- Para preparar la demo completa en Windows, ejecutar scripts/start_presentation_demo.ps1.
- Si el chat no carga, verificar API en http://localhost:8851/health y Ollama en http://127.0.0.1:11434.
- Cerrar mostrando EDA del corpus, Recall@5, MRR y como eso sostiene la respuesta final.

## 15. Conclusiones - La mejora de respuesta fue consecuencia del trabajo sobre datos

El resultado defendible no es solo un chatbot funcionando: es un pipeline con datos curados, medicion de corpus, retrieval auditable, guardrails y evaluacion reproducible.

### Dato trabajado

El JSON original se transformo en 111 documentos RAG con mejor granularidad y trazabilidad.

### Retrieval medido

Se calcularon Precision@5, Recall@5, MRR y Top-1 para saber si aparece la fuente correcta.

### Respuesta controlada

La capa extractiva y los guardrails reducen alucinacion y hacen que el LLM dependa menos de improvisar.

