# Presentacion Final - Chatbot RAG CORADIR

## Trabajo final - Chatbot RAG para CORADIR Movilidad Electrica

MVP funcional para responder consultas frecuentes sobre vehiculos, precios, carga, garantias, agencias y condiciones comerciales.

- Base de conocimiento cerrada y curada.
- Backend FastAPI con chat web.
- RAG con Chroma, embeddings locales y Ollama.
- Benchmark reproducible y metricas RAG para auditar la calidad.

## 1. Problema - La informacion existia, pero no estaba lista para responder bien

El desafio no era solo conectar un LLM: habia que transformar datos administrativos en evidencia recuperable y auditable.

### Datos jerarquicos

El dataset original estaba en JSON, util para administrar informacion, pero poco conveniente para recuperacion semantica directa.

### Riesgo de mezcla

Una respuesta generativa libre podia combinar versiones, precios o condiciones comerciales de forma incorrecta.

### Necesidad academica

La presentacion necesitaba evidencia medible, no solo una demo aparentemente correcta.

## 2. Solucion - Un pipeline hibrido: recuperar, verificar y recien despues redactar

La mejora principal fue estructural: preprocesar la base, recuperar fragmentos mas precisos y usar una capa extractiva para datos factuales.

- 111 documentos indexables generados desde el dataset original.
- Chroma como base vectorial local.
- Ollama con qwen3.5:0.8b como default liviano y qwen3.5:latest como fallback.
- Prompts baseline, sales y strict para comparar comportamiento.

Flujo: Usuario -> FastAPI -> Clasificacion -> Retrieval -> Capa extractiva -> LLM -> Respuesta

## 3. Datos - Preprocesamiento orientado a RAG

El sistema no indexa el JSON completo como un bloque: lo transforma en unidades semanticas mas chicas y consultables.

### Fuente

dataset/dataset_movilidad.json consolidado desde FAQs web, fichas tecnicas, informacion tecnica relevada, precios, agencias, carga y condiciones comerciales.

### Transformacion

scripts/prepare_dataset.py normaliza claves, corrige codificacion y genera dataset/knowledge_base_movilidad.jsonl.

### Impacto

Menos ruido en el contexto, respuestas mas concretas y mejor trazabilidad de la evidencia usada.

## 4. Evaluacion - La primera evaluacion sintetica valida el MVP y muestra limites

La evaluacion inicial fue sintetica y automatica: un benchmark corto para demo/regresion y uno extendido para detectar fallas reales mediante keywords, fuentes y latencia.

- Benchmark MVP: 15/15 casos correctos en variantes strict y sales.
- Benchmark extendido: 35/64 casos correctos.
- El descenso no invalida el proyecto: muestra que el nuevo dataset es mas exigente y sensible.
- La lectura tecnica es que falta medir retrieval directamente.

## 5. Metricas RAG - Mejora: separar recuperacion y redaccion

A partir de los criterios trabajados durante la cursada, la evaluacion se amplio para distinguir si falla la busqueda de evidencia o la respuesta final.

### Precision@K

De los documentos recuperados en el top K, cuantos eran relevantes. Ayuda a medir ruido en el contexto.

### Recall@K

De todos los documentos relevantes esperados, cuantos aparecieron en el top K. Ayuda a detectar omisiones.

### MRR

Mide en que posicion aparece el primer documento relevante. Es importante cuando la respuesta debe salir rapido.

### Faithfulness

Evalua si cada afirmacion de la respuesta esta respaldada por las fuentes recuperadas.

## 6. Resultados - Resultados actuales y lectura honesta

El sistema funciona en el alcance MVP, pero el benchmark extendido muestra donde conviene mejorar antes de afirmar robustez general.

- Los fallos aparecen sobre todo en vehiculos especificos, agencias puntuales e informacion institucional.
- Puede haber fallos por recuperacion, respuesta parcial, keyword demasiado estricta o dato ausente.
- El proximo paso metodologico es guardar fuentes recuperadas por consulta.

## 7. Retrieval - Nueva mejora: medir si aparece la fuente correcta

El benchmark ahora guarda documentos recuperados y calcula Precision@5, Recall@5, MRR y Top-1 source accuracy.

- Corrida retrieval-only sobre 64 casos del dataset extendido.
- Recall@5: 89.8%. La fuente esperada aparece en el top 5 en la mayoria de los casos.
- Top-1: 65.6%. Todavia hay margen para ordenar mejor el contexto.
- MRR: 75.9%. Sirve para distinguir fallas de recuperacion de fallas de redaccion.

## 8. Corpus - Nueva mejora: EDA de chunks con TTR y MATTR

Antes de lematizar o cambiar chunking, se midio la calidad del corpus RAG generado.

- 111 documentos analizados desde knowledge_base_movilidad.jsonl.
- Promedio de 44.21 tokens por documento.
- MATTR promedio: 0.8538, una densidad lexica alta.
- Decision: no aplicar lematizacion global por ahora; priorizar metadata y retrieval.

## 9. Comparacion - Nueva evidencia: los embeddings locales si cambian el retrieval

Al medir retrieval vectorial puro, los embeddings nuevos superaron al baseline nomic-embed-text.

- qwen3-embedding:0.6b obtuvo el mejor Recall@5: 81.2%.
- embeddinggemma obtuvo el mejor MRR: 69.5% y Top-1: 60.9%.
- nomic-embed-text fue el mas liviano, pero quedo bajo en retrieval vectorial puro.
- Recomendacion: probar embeddinggemma como nuevo default y validar accuracy final.

## 10. Hardware - Nueva mejora: evaluar modelos mas chicos

Como el sistema ya reduce la carga del LLM con retrieval y respuesta extractiva, se preparo una matriz para probar si modelos livianos alcanzan para preguntas frecuentes.

- Todos los modelos locales evaluados obtuvieron 15/15 en el benchmark MVP.
- Con guardrail previo, los candidatos tambien obtuvieron 6/6 en casos por fuera.
- granite4:350m, lfm2.5-thinking:1.2b y qwen3.5:0.8b son candidatos fuertes para rutas factuales.
- El resultado muestra que la capa extractiva reduce la necesidad de un modelo grande.
- Estrategia recomendada: modelo chico para FAQ factual y qwen3.5:latest como fallback complejo.

## 11. Guardrail - Casos por fuera: la mejora no fue cambiar de modelo, sino evitar alucinacion

La comparacion mostro que los modelos no debian recibir consultas que el sistema podia rechazar por reglas de alcance.

- Antes del guardrail, la capa extractiva podia traer contexto irrelevante.
- Despues del guardrail, todos los candidatos evaluados lograron 6/6.
- La latencia queda en 0.0 s porque no se llama al LLM.
- Esto permite usar modelos chicos con menor riesgo operativo.

## 12. Revision manual - Nueva mejora: matriz para revision manual del autor

Las respuestas en vivo mostraron que no alcanza con la evaluacion sintetica por keywords y latencia: algunas respuestas fueron vacias, lentas o poco utiles. Se agrega una matriz humana balanceada: 7 factuales, 7 ambiguas y 7 fuera de dominio.

- Nuevo dataset: dataset/evaluacion_manual_modelos.json con 21 casos balanceados.
- Nuevo script: scripts/run_manual_model_evaluation.py.
- El script genera respuestas, estados y latencias; la correccion, score 1-5 y notas quedan para revision manual.
- La muestra homogenea evita favorecer modelos que solo responden bien preguntas factuales.
- Los modelos Qwen/thinking se ejecutan con think:false y se remueven bloques <think> para evaluar solo la respuesta final.
- Se incluyen modelos chicos nuevos detectados en Ollama: gemma3:270m, llama3.2:3b y nemotron-3-nano:4b.
- El objetivo es elegir el modelo por calidad real percibida, no solo por que complete keywords.

## 13. Seleccion de modelo - Segun la matriz, Qwen 3.5 fue el candidato mas acertado

La seleccion preliminar se basa en la preevaluacion sintetica sobre 21 respuestas balanceadas. Cuenta como respuesta aceptable un score 4 o 5; la decision final queda sujeta a la revision manual.

- qwen3.5:latest obtuvo el mayor porcentaje de respuestas aceptables: 16/21.
- qwen3.5:4b y nemotron-3-nano:4b empataron en aceptables: 15/21.
- qwen3.5:4b queda como mejor compromiso preliminar entre calidad, latencia y peso.
- nemotron-3-nano:4b es fuerte para rechazar fuera de dominio, pero debe revisarse en factuales.
- gemma3:270m y lfm2.5-thinking:1.2b no quedan recomendados por respuestas vacias o solo thinking.

## 14. Criterios - La decision no depende de un solo promedio

El segundo grafico separa el rendimiento por tipo de pregunta. Esto evita elegir un modelo que sea bueno solo en preguntas simples y flojo en ambiguas o fuera de dominio.

- Las preguntas factuales miden precision contra datos tecnicos y comerciales.
- Las preguntas ambiguas miden si el modelo pide contexto o responde con cautela.
- Los casos fuera de dominio miden si evita inventar informacion.
- La metrica automatica orienta la seleccion, pero la columna de score manual define la decision final.

## 15. Costo operativo - La mejor decision cruza acierto, latencia y peso local

El modelo recomendado no debe ser solo el de mayor score. Tambien importa cuanto tarda en responder y cuanto ocupa/carga en memoria para una demo local estable.

- El eje vertical muestra respuestas aceptables sobre las 21 preguntas.
- El eje horizontal muestra latencia promedio: mas a la izquierda es mejor.
- El tamano de cada punto representa el peso local aproximado del modelo.
- qwen3.5:latest logra el mayor acierto, pero tambien mayor latencia y peso.
- qwen3.5:4b queda como candidato de equilibrio: alto acierto con menor costo que latest.

## 16. Demo - Demo en vivo dentro de la presentacion

La presentacion puede cargar el chat real si se abre desde la API local. Esto permite probar preguntas sin salir del recorrido.

- Preguntar: Cuanta autonomia tiene el TITO S5 y como se carga?
- Preguntar: Cual es el precio del TITO S5-300 AA?
- Preguntar: Donde hago un reclamo o pido servicio tecnico?
- Para preparar la demo completa en Windows, ejecutar scripts/start_presentation_demo.ps1.
- Si el chat no carga, verificar API en http://localhost:8851/health y Ollama en http://127.0.0.1:11434.
- Cerrar mostrando Precision@5, Recall@5, MRR, EDA de corpus, embeddings y modelos livianos.

## 17. Cierre - El MVP no solo responde: tambien deja evidencia para auditarlo

El proyecto queda defendible porque combina implementacion, reproducibilidad, medicion y una hoja de ruta alineada con los contenidos de clase.

### Implementado

Chat web, backend, base preprocesada, RAG local, prompts comparables y benchmark automatizado.

### Validado

15/15 en benchmark MVP y benchmark extendido preparado para encontrar limites reales.

### Siguiente salto

Medir retrieval, revisar faithfulness y separar fallos de recuperacion de fallos de generacion.

