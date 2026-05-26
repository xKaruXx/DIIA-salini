# Mejoras Derivadas del Material de Clase 4

## Resumen

El material nuevo de clase 4 refuerza una idea importante para este proyecto: un sistema RAG no debe evaluarse solamente por si la respuesta final contiene ciertas palabras clave. Tambien hay que separar la calidad de la recuperacion, la calidad de la generacion y la calidad del corpus indexado.

En el estado actual, el proyecto ya tiene un MVP funcional, un benchmark inicial y un dataset extendido con `expected_sources`. A partir del material nuevo, las mejoras mas defendibles para hacer y documentar son las siguientes.

## 1. Evaluacion de retrieval con fuentes esperadas

### Motivacion

La clase 4 distingue dos tipos de falla:

- falla de retrieval: el sistema recupera documentos incorrectos o incompletos
- falla de generacion: el sistema recupera el documento correcto, pero redacta una respuesta no respaldada

Hoy el benchmark valida principalmente palabras clave en la respuesta final. Eso no permite saber si un caso fallo porque el documento correcto no fue recuperado o porque la respuesta final no uso bien el contexto.

### Mejora propuesta

Extender `scripts/run_benchmark.py` para registrar, por cada pregunta:

- documentos recuperados en el top K
- `source_path`, `section` y `title` de cada documento
- posicion del primer documento esperado
- coincidencia entre `expected_sources` y fuentes recuperadas

### Metricas a documentar

- `Precision@K`: proporcion de documentos relevantes dentro del top K
- `Recall@K`: proporcion de fuentes esperadas recuperadas
- `MRR`: posicion del primer documento relevante
- `NDCG`: opcional, si se agrega relevancia graduada

### Evidencia esperada

Nuevo reporte JSON con un bloque similar a:

```json
{
  "retrieval": {
    "top_k": 5,
    "retrieved_sources": ["vehiculos_detalles.TITO", "precios.TITO"],
    "expected_sources": ["vehiculos_detalles.TITO"],
    "precision_at_k": 0.2,
    "recall_at_k": 1.0,
    "reciprocal_rank": 1.0
  }
}
```

## 2. Golden dataset mas completo

### Motivacion

El material de clase 4 remarca que las metricas RAG dependen de un conjunto de referencia curado. El dataset extendido ya dio un paso importante al agregar `expected_sources`, pero todavia puede fortalecerse.

### Mejora propuesta

Ampliar gradualmente `dataset/evaluacion_rag_extendida.json` con:

- `expected_sources`: ya incorporado
- `ideal_answer`: respuesta breve esperada redactada manualmente
- `answerability`: `answerable` o `not_answerable`
- `relevance_grade`: relevancia por fuente, por ejemplo 0, 1 o 2
- `failure_notes`: campo opcional para explicar ambiguedades del caso

### Beneficio

Esto permite evaluar no solo si el sistema recupera documentos, sino tambien si la respuesta final es fiel, relevante y suficientemente concisa.

## 3. Revision de faithfulness

### Motivacion

El material nuevo presenta `Faithfulness` como metrica clave para detectar respuestas que suenan bien pero no estan respaldadas por el contexto.

### Mejora propuesta

Completar `docs/matriz_revision_factual.md` con 10 casos criticos:

- precios
- autonomia
- garantia
- agencias
- beneficios por discapacidad
- condiciones de reserva y entrega

Para cada caso, documentar:

- respuesta generada
- fuente recuperada
- afirmaciones principales de la respuesta
- veredicto: `OK`, `Parcial`, `Riesgo` o `Falla`
- observacion concreta

### Evidencia esperada

Una tabla manual que permita afirmar que las respuestas no solo aciertan palabras clave, sino que estan respaldadas por documentos concretos.

## 4. Medicion de concision y relevancia de respuesta

### Motivacion

La clase 4 tambien separa factualidad, relevancia y concision. En este proyecto ya se detecto que algunas respuestas extractivas pueden incluir informacion adicional correcta pero no pedida.

### Mejora propuesta

Agregar al benchmark indicadores simples:

- longitud de respuesta en caracteres o tokens
- cantidad de lineas devueltas
- tasa de respuestas con informacion adicional marcada manualmente
- comparacion de concision entre `sales` y `strict`

### Beneficio

Esto permite justificar por que la variante `strict` es mas adecuada para preguntas factuales, aunque `sales` pueda sonar mejor comercialmente.

## 5. EDA de chunks y riqueza lexica

### Motivacion

El material sobre TTR, MATTR y lematizacion aporta una mejora nueva para documentar la calidad del corpus antes de indexarlo. La idea central es que chunks demasiado repetitivos o poco densos pueden degradar la recuperacion.

### Mejora propuesta

Crear un analisis de calidad de documentos/chunks sobre `dataset/knowledge_base_movilidad.jsonl`:

- tokens por documento
- cantidad de documentos muy cortos o muy largos
- TTR por documento
- MATTR por documento o por ventana
- deteccion de chunks con baja densidad informacional

### Decision tecnica esperada

Documentar si conviene:

- conservar el texto actual
- subdividir documentos largos
- enriquecer metadatos
- normalizar sinonimos del dominio
- evaluar lematizacion solo si el corpus muestra mucha flexion/repeticion

Para este proyecto, la lematizacion no deberia asumirse automaticamente. Como se usan embeddings densos y un dominio comercial-tecnico con nombres propios, versiones y modelos, primero conviene medir TTR/MATTR y despues decidir.

## 6. Chunking y metadatos mas explicitos

### Motivacion

El notebook de RAG simple vs mejorado muestra que el chunking y los metadatos pueden impactar directamente en retrieval. El proyecto ya genera documentos con `section`, `title` y `source_path`, pero puede mejorar la metadata de dominio.

### Mejora propuesta

Agregar metadatos derivados durante `scripts/prepare_dataset.py`, por ejemplo:

- `entity_type`: vehiculo, precio, agencia, faq, condicion_comercial
- `vehicle_name`: TITO, TITA, CHIKI, etc.
- `province`: para agencias
- `topic`: garantia, carga, reserva, leasing, beneficios
- `answer_type`: precio, especificacion, contacto, condicion

### Beneficio

Con esa metadata se pueden probar filtros pre-ranking o re-ranking simple. Por ejemplo, si la pregunta menciona San Luis, priorizar documentos de agencias en San Luis; si menciona precio, priorizar seccion `precios`.

## 7. Casos sin respuesta en el corpus

### Motivacion

El material de clase propone probar preguntas que no tienen respuesta para verificar si el sistema admite la falta de informacion o alucina.

### Mejora propuesta

Agregar casos `not_answerable` al benchmark:

- preguntas fuera del dominio CORADIR
- consultas sobre datos no presentes en la base
- consultas legales o financieras no cubiertas
- preguntas sobre disponibilidad actual si no hay dato actualizado

### Evidencia esperada

Medir tasa de rechazo correcto o derivacion correcta. Esto fortalece la presentacion porque muestra control de riesgo, no solo aciertos en preguntas conocidas.

## Priorizacion recomendada

| Prioridad | Mejora | Estado actual | Motivo |
|---:|---|---|---|
| 1 | Retrieval con Precision@K, Recall@K y MRR | Parcialmente preparado | Ya existe `expected_sources`, falta capturar top K |
| 2 | Faithfulness manual | Matriz creada, sin completar | Es la evidencia mas fuerte contra alucinaciones |
| 3 | EDA de chunks con TTR/MATTR | No implementado | Conecta directamente con el material nuevo de riqueza lexica |
| 4 | Metadatos de dominio mas explicitos | Parcial | Puede mejorar retrieval y explicar fallas |
| 5 | Casos sin respuesta | Parcial | Evalua robustez y rechazo responsable |
| 6 | NDCG / relevancia graduada | Pendiente | Util cuando haya grados de relevancia por fuente |

## Como contarlo en la presentacion

La narrativa recomendada es:

1. El MVP ya funciona y responde correctamente el benchmark inicial.
2. La clase 4 muestra que eso no alcanza para auditar un RAG.
3. Por eso se amplio el dataset con fuentes esperadas.
4. El siguiente paso es medir retrieval y faithfulness por separado.
5. El proyecto queda mejor defendido porque reconoce sus limites y propone metricas adecuadas para verificarlos.

