# Speech Demo Day — Chatbot RAG CORADIR (10 minutos)

> Guion palabra por palabra, sincronizado con `presentacion_demo_day.pptx`.
> ~1.350 palabras ≈ 10 minutos a ritmo de exposición (135 palabras/min).
> Los **números en negrita** son los que hay que decir exactos.
> Para ensayar sin leer: usar el mapa mental (`mapa_mental_speech.png`).

---

## Slide 1 — Título · 0:00–0:40

Buenas. Soy Carlos Salini y este es mi proyecto final del track A: un chatbot
RAG para CORADIR Movilidad Eléctrica.

En una frase: tomé la base de conocimiento administrativa de una fábrica de
vehículos eléctricos y la convertí en un sistema de consulta en lenguaje
natural que es **medible, trazable y corre cien por ciento local**, sin un
solo servicio pago.

En los próximos diez minutos les voy a mostrar el problema, la solución, y
sobre todo la evidencia: qué medí, qué falló y qué decidí con cada medición.

*(Transición: "Empiezo por el problema.")*

## Slide 2 — Problema · 0:40–1:40

CORADIR fabrica los vehículos eléctricos TITO, TITA y CHIKI, y tiene agencias
en unas diez provincias. Toda su información comercial —precios,
especificaciones, direcciones de agencias, preguntas frecuentes— vive en
**un único JSON interno y jerárquico**.

Eso genera tres problemas. Uno: no se puede consultar en lenguaje natural;
ventas y los visitantes del sitio dependen de búsqueda manual. Dos: cero
trazabilidad; nadie puede auditar qué fuente respalda cada respuesta. Y
tres, el que condiciona todo el diseño: acá los datos son exactos. Un precio
en dólares o una dirección "aproximada" es **peor que no responder**.

*(Transición: "Con ese requisito de exactitud, la solución no podía ser un
LLM parafraseando.")*

## Slide 3 — Solución · 1:40–2:50

La solución es un chatbot web RAG con una particularidad: la respuesta es
extractiva primero, generativa después.

El pipeline: el JSON se convierte en **111 documentos atómicos**, cada uno
con su ruta de origen —su `source_path`— como metadato. Se indexan en Chroma
y se recuperan con búsqueda híbrida: léxica más vectorial, top cinco. Y antes
de pedirle nada al LLM, una capa extractiva intenta devolver el dato literal
del documento recuperado, en **una centésima de segundo**. Solo si eso no
alcanza, entra el modelo generativo: un qwen3.5 corriendo local vía Ollama,
con un prompt estricto que le prohíbe inventar.

*(Si hay demo en vivo: "Lo vemos: le pregunto cuánta autonomía tiene el TITO
S5... y responde con el dato literal y la fuente.")*

*(Transición: "Nada de esto se decidió por intuición. Arrancó por los datos.")*

## Slide 4 — Los datos / EDA · 2:50–4:00

El EDA del corpus definió el diseño. Tres hallazgos.

Primero: los documentos son muy cortos. **Mediana de 24 tokens**, 67 de los
111 documentos tienen menos de 30. Por eso decidí **no hacer chunking** por
tamaño: fragmentar documentos que ya son atómicos solo rompía unidades de
significado. El documento es la unidad de indexado.

Segundo: el JSON jerárquico trae rutas naturales. Por eso cada documento
conserva su `source_path`, y eso después me permitió algo clave: definir
**fuentes esperadas por caso de evaluación** y auditar el retrieval contra
ellas.

Tercero: la riqueza léxica —MATTR de **0,85**— no justificaba lematización
agresiva. Por eso preservé los valores literales: "USD 17.731,25" tiene que
salir exactamente así.

La regla que apliqué es la de la cátedra: cada gráfico del EDA termina en
"...y por eso decidimos".

## Slide 5 — Arquitectura · 4:00–4:50

La arquitectura completa, en dos bandas. Offline: el JSON pasa por
`prepare_dataset.py`, sale el JSONL de 111 documentos trazables, y se indexa
en Chroma con embeddings nomic v2.

Online: la pregunta entra por WebSocket a FastAPI, pasa por guardrails de
dominio, y va a la ruta extractiva. Si hay dato exacto, responde ahí, con
fuente. Si no, retrieval híbrido top cinco más el LLM con prompt estricto.
El historial queda en SQLite.

Criterio de calidad: otro equipo puede reproducir el sistema con el repo y
esta sección del informe. Todos los benchmarks que siguen son comandos
versionados.

*(Transición: "Y ahora lo importante: qué pasó cuando lo medí.")*

## Slide 6 — El hallazgo clave · 4:50–6:00

Primera evaluación seria: 64 casos con keywords y fuentes esperadas. El
baseline dio **35 de 64**: 54,7%. Mal.

La reacción intuitiva era "el retrieval falla, hay que cambiar el modelo de
embeddings". Pero como medía respuesta y retrieval por separado, pude cruzar
los datos. Y de los **29 fallos, 24 ya tenían la fuente correcta en el top
cinco**. Solo 5 eran fallos reales de retrieval.

O sea: el sistema encontraba el documento correcto y fallaba al extraer el
campo puntual. El problema no era de búsqueda, era de selección de líneas.

Por eso la decisión fue mejorar la capa extractiva —términos de foco, ranking
por entidad, presupuesto de líneas— **antes** que cambiar embeddings o
agregar reranking. Este es, para mí, el hallazgo del proyecto: sin medir por
partes, hubiera optimizado el componente equivocado.

## Slide 7 — Decisión de modelo · 6:00–6:50

La otra decisión grande: qué LLM local usar. Evalué **11 modelos** con las
mismas 21 preguntas: factuales, ambiguas y fuera de dominio. 231 respuestas.

Ganó qwen3.5: la versión grande puntúa **4,29 sobre 5**, y la de 4B,
**4,19**. Elegí la de 4B para la demo: cede una décima de score a cambio de
**26% menos latencia** —3,8 segundos— y la mitad de memoria.

Y descarté con evidencia, no por prejuicio: gemma3 de 270M devolvía
respuestas vacías, y el modelo "thinking" de LiquidAI nunca emitió respuesta
final, solo razonamiento.

## Slide 8 — Evidencia: retrieval · 6:50–7:40

Métricas finales de retrieval, auditadas chunk por chunk: **257 chunks**
revisados contra fuentes esperadas.

Recall arroba cinco: **0,97**. MRR: **0,92** —el primer documento relevante
aparece, en promedio, en la posición **1,2**. Top-1: **0,88**.

¿Y la Precision arroba cinco de **0,32**? No es un bug: es el trade-off que
acepté con el corpus atómico. Documentos muy cortos meten vecinos "extra" en
el top cinco. Hoy lo absorbe la capa extractiva; si mañana el sistema se
vuelve más generativo, ese ruido hay que atacarlo.

## Slide 9 — Evidencia: end-to-end · 7:40–8:40

El resultado de punta a punta. Tres iteraciones de mejora extractiva, sin
tocar índice ni embeddings: de **54,7%** a 71,9%, a 89,1%, a **64 de 64: cien
por ciento**. Con faithfulness media de **0,89** y costo cero por consulta.

Y acá va el asterisco honesto, porque un cien por ciento sin asterisco es
sospechoso: ese set de 64 casos lo usé para diagnosticar y corregir entre
iteraciones. Así que el cien por ciento mide **cobertura del benchmark, no
generalización**. La validación con consultas reales nuevas es el primer
punto del trabajo futuro. Prefiero reportarlo así a inflar el número.

## Slide 10 — Errores documentados · 8:40–9:20

Dos fallas que enseñaron más que los aciertos.

"¿Qué agencia hay en Moreno?" El sistema respondía "Buenos Aires" genérico.
Causa raíz: el documento de agencias de Buenos Aires es de los más largos del
corpus y las stopwords interrogativas subían FAQs genéricas. Corrección:
prioridad a la localidad específica.

"¿Precio de la TITA S2 300?" Devolvía las variantes con furgón y omitía la
versión base. Corrección: penalizar variantes no solicitadas.

Y un bonus: mi propia mejora introdujo **dos regresiones** —se perdió el "500
kilos" de capacidad de carga. Las documenté y las corregí verificando contra
el baseline completo antes de congelar la versión.

## Slide 11 — Cierre · 9:20–10:00

Cierro con lo que esta experiencia demuestra: una base de conocimiento
administrativa puede volverse consultable y auditable con un stack cien por
ciento local. Lo que limita al sistema lo dije con números: riesgo de
sobreajuste al benchmark, precisión baja por corpus atómico, reglas atadas al
dominio. Y lo que sigue sale de esas limitaciones: validación held-out,
reevaluar embeddings, faithfulness en producción.

La idea que me llevo: **medir por partes fue lo que permitió mejorar**. El
informe técnico y todos los benchmarks reproducibles están en el repo.
Gracias.

---

# Preguntas probables (preparar respuesta de ~30 s)

**"¿100%? ¿No está sobreajustado?"**
Sí, y está declarado en el informe: el set se usó para iterar, así que mide
cobertura, no generalización. Lo que sí es robusto: la mejora aísla la capa
extractiva (mismo índice, mismos embeddings) y no hay regresiones contra el
baseline. El paso siguiente es un held-out con consultas reales del chat.

**"¿Por qué no usaron reranking con cross-encoder?"**
Porque el ranking no era el problema: el primer documento relevante ya llega
en posición media 1,22, y 24 de 29 fallos tenían la fuente en el top-5. Un
reranker agregaba latencia y memoria para atacar el componente que ya
funcionaba.

**"¿Por qué nomic v2 si embeddinggemma mide mejor?"**
Decisión de secuenciamiento: cuando tuve esa matriz, la mejora extractiva ya
había llevado el benchmark a 64/64 con el índice existente. Cambiar embedding
era reindexar y revalidar todo para atacar 5 fallos de 29. Queda como
candidato medido para la próxima iteración.

**"¿Esto escala a otro corpus / otra empresa?"**
El pipeline sí (JSON → JSONL trazable → índice → benchmark con fuentes
esperadas es genérico); las reglas extractivas no: están calibradas a este
dominio. Es la limitación 3 del informe, y la propuesta es volverlas
configuración declarativa.

**"¿Latencia real con el LLM?"**
Extractiva: 0,01 s. Generativa: 3,8 s promedio con qwen3.5:4b en mi hardware
local. La mayoría de las consultas factuales del dominio resuelven por la
extractiva.

---

# Reglas de ensayo

1. Cronometrar cada bloque con los rangos de arriba; si a la slide 6 llegás
   después de 5:10, recortar la slide 7 (decir solo "elegí qwen3.5:4b por
   equilibrio score-latencia") y recuperar 30 s.
2. Los tres números que NO se pueden dudar: **35→64 de 64**, **24 de 29
   fallos con fuente recuperada**, **Recall@5 0,97**.
3. La frase ancla de cada slide está en negrita en el mapa mental; memorizar
   esas 11 frases, no el guion.
4. Regla del docente: todo número dicho en voz alta tiene respaldo en el
   informe (sección 5) — si una pregunta pide un número que no recordás,
   responder "está en la tabla X del informe" es mejor que improvisar.
