# 01_Definicion

- Fuente: `01_Definicion.pdf`
- Tipo: PDF
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

- Paginas extraidas: 34

## Pagina 1

preencoded.png
DIPLOMATURA EN INTELIGENCIA ARTIFICIAL · UBA
Planificación del
Trabajo Final
Clase 1 – Repaso - Definiciones - Canvas
Profesor: Esp. Ing. Cristian Salinas Talamilla
Email: salinastalamilla@gmail.com
Lnk: https://www.linkedin.com/in/cristian-patricio-salinas-talamilla-255b562a/

## Pagina 2

preencoded.png
Agenda de hoy
01
Introducción a la IA y los LLMs
Base teórica para entender los proyectos del grupo.
02
Los tracks o enfoques
RAG y Clasificación/Agentes: qué son y cuándo aplicar cada
uno.
03
Definir un buen problema de IA
Errores comunes y herramientas para evitarlos.
04
AI Canvas simplificado
La herramienta para formalizar cada proyecto.
05
Ronda de presentaciones
3 min por alumno para presentar la idea y recibir feedback.
06
Ficha de Proyecto
Entregable del día.

## Pagina 3

preencoded.png
¿Qué es la Inteligencia Artificial?
Base conceptual para entender los proyectos del grupo
Definición
Sistemas que realizan tareas asociadas
a la inteligencia humana.
Qué hace
Reconoce patrones, aprende de datos
y apoya decisiones.
En este curso
La usamos como base para proyectos
de RAG, clasificación y agentes.

## Pagina 4

preencoded.png
¿Cómo aprende una máquina?
01
Datos
Ejemplos etiquetados o no.
02
Entrenamiento
El algoritmo detecta patrones y ajusta
parámetros.
03
Modelo
Función capaz de hacer predicciones.
04
Evaluación
Se mide el desempeño con datos nuevos.
05
Inferencia
Se usa en producción para resolver casos reales.
En los proyectos del grupo, el entrenamiento ya ocurrió: los LLMs como GPT, Llama y Gemini fueron entrenados con
grandes volúmenes de texto. Nuestro trabajo es usarlos con criterio para cada problema específico.

## Pagina 5

preencoded.png
https://www.datacamp.com/blog
/top-machine-learning-use-cases-
and-algorithms
https://s3.amazonaws.com/assets.datacamp.com/email/other/ML+Cheat+S
heet_2.pdf

## Pagina 6

preencoded.png
Hitos clave de la IA
1
1950
Test de Turing
Prueba para evaluar inteligencia máquina.
2
1986
Backpropagation
Entrenamiento de redes neuronales multicapa.
3
2012
AlexNet / ImageNet
Deep Learning supera al humano en visión.
4
2017
Transformers
Base de los LLMs modernos.
5
2020
GPT-3
LLM con 175B parámetros. Nuevo paradigma.
6
2022
ChatGPT
La IA llega al gran público.
7
2024
LLMs en producción
Multimodalidad, agentes y RAG en industria.

## Pagina 7

preencoded.png
¿Cuándo usar IA y cuándo no?
✓ Bueno para IA
•
Demasiadas reglas para programar manualmente.
•
Hay patrones, pero no una regla clara.
•
Se trabaja con texto, imágenes o datos complejos.
•
Hay datos suficientes para aprender.
•
Una respuesta aproximada es útil.
✗ No usar IA cuando...
•
La regla es simple y se puede codificar.
•
No hay datos, o son insuficientes.
•
Un error no es aceptable.
•
La transparencia total es obligatoria.
•
La solución más simple ya funciona.

## Pagina 8

preencoded.png
Del texto a la inteligencia
Natural Language Processing y Large Language Models
Procesar
Convertir lenguaje humano en
señales útiles para sistemas.
Entender
Detectar intención, contexto y
significado en texto.
Generar
Responder, resumir y crear
contenido con modelos de
lenguaje.

## Pagina 9

preencoded.png
¿Qué es el NLP?
Rama de la IA que permite entender, interpretar y generar lenguaje humano.
Clasificación
•
¿Positivo o negativo?
•
¿Spam o no spam?
NER (Reconocimiento de Entidades
Nombradas)
•
Identifica entidades
•
Personas, lugares y fechas
Búsqueda semántica
•
Encuentra textos similares
•
Según el significado
Generación
•
Respuestas y resúmenes
•
Traducción y Q&A

## Pagina 10

preencoded.png
¿Qué es un Large Language Model (LLM)?
Modelo de deep learning entrenado con grandes volúmenes de texto para predecir y generar lenguaje.
No “entiende” como humano: estima la siguiente palabra más probable según el contexto.
GPT-4 / ChatGPT
OpenAI. Propietario.
Muy capaz, de pago.
LLaMA / Ollama
Meta. Open source.
Corre en hardware local.
Gemini
Google. Multimodal.
Integrado en Workspace.
Claude
Anthropic.
Más enfoque en seguridad y razonamiento.

## Pagina 11

preencoded.png
¿Cómo funciona un LLM? (conceptual)
Analogía: un autocompletado muy sofisticado.
1. Tokenización: divide el texto en tokens. Ej.: “inteligencia artificial” = 3 tokens.
2. Embeddings: convierte cada token en un vector que captura su significado.
3. Atención: detecta qué tokens se relacionan más para entender el contexto.
4. Generación: predice el siguiente token, uno a uno, hasta formar la respuesta.

## Pagina 12

preencoded.png
Tokens y ventana de contexto
Qué procesa un LLM y cuánto puede leer a la vez.
Token
Unidad mínima de texto que procesa el modelo.
Regla rápida
≈ 1 token = ¾ palabra en inglés o 1 palabra en español.
Ejemplo visual de tokenización
Texto: “¿Cómo estás hoy?”
¿Cómo
1234
estás
5678
hoy
9012
?
3456
Tokens: ["¿Cómo", " estás", " hoy", "?"]
Token IDs: [1234, 5678, 9012, 3456]
Comparación de tokenización
Palabra común
inteligencia
1 token
Palabra rara
xyzabc
3-4 tokens
Número
2024
1 token
Emoji
1-2 tokens

## Pagina 13

preencoded.png
Comparación de tokenización y ventana de contexto
Comparación de tokenización
Muestra cómo diferentes tipos de texto se dividen diferente:
Palabra común
"inteligencia" = 1 token
Palabra rara
"xyzabc" = 3-4 tokens
Número
"2024" = 1 token
Emoji
"
" = 1-2 tokens
Código
"def function()" = 4-5 tokens
Conclusión: Las palabras comunes son eficientes, las raras
consumen más tokens.
Ventana de contexto
La cantidad máxima de tokens que el modelo puede procesar en una
consulta.
Ejemplos por modelo:
•
GPT-3.5: 4,096 tokens
•
GPT-4: 32768 tk
•
Claude 3: 100,000 tokens
•
Llama 2: 4,096 tokens
Implicación para RAG: Cuanto mayor la ventana, más documentos
puedes inyectar en una consulta.

## Pagina 14

preencoded.png
Limitaciones de los LLMs
Clave para evaluar riesgos en el Trabajo Final.
Alucinaciones
Puede inventar datos
con total seguridad.
Fecha de corte
Solo conoce lo
aprendido hasta su
entrenamiento.
Sin memoria por
defecto
No recuerda
conversaciones
anteriores sin historial.
Sesgo del
entrenamiento
Hereda sesgos
presentes en los datos
de origen.
No razona,
predice
Genera la respuesta
más probable, no
“piensa”.

## Pagina 15

preencoded.png
Alucinaciones: el problema central
Un LLM puede inventar hechos, citas, leyes o procedimientos con total confianza.
¿Por qué ocurre?
•
Optimiza coherencia, no verdad.
•
No tiene datos en tiempo real ni acceso a
documentos específicos.
•
No sabe cuándo no sabe algo.
¿Cómo lo mitiga RAG?
•
Entrega al LLM el documento correcto como
contexto.
•
Reduce la invención al anclar la respuesta en
fuentes concretas.
•
Base técnica de los proyectos del Track A.
RAG no elimina el riesgo, pero lo reduce al obligar al modelo a responder con evidencia.

## Pagina 16

preencoded.png
Ingeniería de prompts
La forma del prompt define la calidad de la respuesta del LLM.
Ser específico
•
Define formato,
tono y extensión
•
Reduce
ambigüedad
Dar contexto
•
Rol del modelo
•
Perfil del usuario o
caso de uso
Ejemplos (few-
shot)
•
Muestra el formato
esperado
•
Mejora consistencia
y estilo
Chain-of-
thought
•
Pide razonamiento
paso a paso
•
Útil en problemas
complejos
Ejemplos: “Respondé en español, en menos de 3 párrafos, como para un principiante.” / “Sos un asesor de
nutrición animal y el usuario es un productor de carne vacuna.”

## Pagina 17

preencoded.png
LLMs en industria — casos reales
Aplicaciones concretas por sector:
Salud
•
Responde preguntas con documentación médica
oficial
Legal
•
Búsqueda semántica en jurisprudencia y contratos
Finanzas
•
Clasifica incidentes, detecta anomalías y resume
reportes
Educación
•
Adapta explicaciones al nivel del estudiante y corrige
ejercicios
Agro
•
Asesora sobre nutrición, sanidad y manejo
Medios
•
Detecta sesgo editorial y clasifica contenido
automáticamente

## Pagina 18

preencoded.png
¿Qué es RAG?
Retrieval Augmented Generation
•
Búsqueda semántica + generación de texto.
•
Inyecta el documento correcto antes de responder.
•
Reduce la dependencia de la memoria del LLM.
1.
Pregunta del usuario
2. Búsqueda en documentos
3. Recuperación de chunks relevantes
4. Respuesta del LLM basada en evidencia
5. Salida fundamentada y sin alucinaciones

## Pagina 19

preencoded.png
Track A — Arquitectura RAG en detalle
Fase de indexación — se hace una sola vez
01
Documentos
PDF, web y texto
02
Chunking
Dividir en fragmentos
03
Embeddings
Vectorizar cada chunk
04
Vector Store
Guardar los vectores
Fase de consulta — se ejecuta en cada pregunta
01
Pregunta
Consulta del usuario
02
Embedding
Vector de la pregunta
03
Búsqueda top-k
Recuperar chunks relevantes
04
Respuesta
LLM responde con contexto
Herramientas principales
Frameworks
LangChain / LlamaIndex
Vector DB
ChromaDB / FAISS
Modelos
OpenAI / Ollama / Gemini
Embeddings
sentence-transformers

## Pagina 20

preencoded.png
Track — Clasificación de texto
Asignar una o más etiquetas predefinidas a un fragmento de texto. Es una de las tareas más comunes y útiles de NLP.
Zero-shot
El LLM clasifica sin
ejemplos previos.
Rápido de
implementar, menos
preciso.
Few-shot
Se le dan 2-5 ejemplos
al LLM antes de
clasificar.
Mejora notable en la
precisión.
Fine-tuning
Se entrena un modelo
sobre ejemplos
propios.
Mayor precisión,
mayor costo.

## Pagina 21

preencoded.png
Track B — Agentes de IA
Un agente usa un LLM para razonar, actuar y completar tareas complejas de
forma autónoma.
Loop ReAct (Reason + Act):
01
Observar
Recibe la tarea y el contexto actual.
02
Razonar
Decide qué herramienta usar o qué paso dar.
03
Actuar
Ejecuta una acción: buscar, calcular, escribir o llamar API.
04
Actualizar contexto
Incorpora el resultado y define el siguiente paso.

## Pagina 22

preencoded.png
Track B — Casos de uso en el grupo
Aplicaciones de agentes de IA desarrolladas por el grupo.
Clasificador de
intenciones
•
Clasifica el tipo de
mensaje recibido
•
Orienta al receptor sobre
qué esperar
•
Tomás Caserez
Detector de sesgo
político
•
Identifica sesgo editorial
en noticias
•
Analiza contenido
scrapeado de distintos
medios
•
Diego Methol
Análisis de
sentimiento YouTube
•
Clasifica comentarios de
usuarios
•
Pronostica
comportamiento en
redes sociales
•
Shimon Bentancur
Helpdesk
automatizado
•
Clasifica y enruta
incidentes técnicos
•
Enfocado en empresa de
lotería/gaming
•
Jose Zebraitis
A definir
•
NLP/LLMs con dataset
propio
•
Track en definición
•
Mariana Garcia

## Pagina 23

preencoded.png
PASO 1
Definir el problema
Antes de escribir código, aclara qué se quiere resolver
•
Qué necesita el usuario
•
Qué decisión o respuesta debe generar el sistema
•
Qué está dentro y fuera del alcance

## Pagina 24

preencoded.png
Errores comunes al definir el problema
Evita estos cinco bloqueos antes de avanzar:
•
Demasiado amplio: mejor un caso de uso concreto.
•
Datos no disponibles: verifica acceso, formato y calidad.
•
IA innecesaria: si una regla simple basta no es necesario un sistema basado en IA.
•
Éxito ambiguo: define métricas claras desde el inicio.
•
Usuario difuso: concreta quién lo usará y qué necesita.

## Pagina 25

preencoded.png
PoC, MVP y Producción — ¿qué tipo de trabajo
es?
PoC
Proof of Concept
•
Valida que la idea sea
técnicamente posible
•
Sin escala ni usuarios reales
•
Solo prueba el concepto
MVP
Minimum Viable Product
•
Primera versión usable
•
Resuelve el problema principal
•
Para un subconjunto de usuarios
reales
Producción
Sistema en producción
•
Escalable, mantenible y
monitoreable
•
Usuarios reales y SLAs
•
Reentrenamiento periódico
Trabajo Final DIIA

## Pagina 26

preencoded.png
¿Qué es el AI Canvas?
"Una ayuda para contemplar, construir y evaluar herramientas de IA."
— Agrawal, Gans & Goldfarb, Prediction Machines (2018)
Es un mapa
•
Ordena la conversación antes
de construir
•
Ayuda a ver el proyecto
completo
Alinea a todos
•
Pone problema, dato y solución
en la misma página
•
Reduce ambigüedades desde
el inicio
Fuerza decisiones
tempranas
•
Obliga a definir supuestos
clave
•
Si no se puede completar, el
problema aún no está listo

## Pagina 27

Canvas Simplificado RAG
5 preguntas para definir tu proyecto RAG en clase, ahora.
1
¿Qué problema resuelvo?
•
Una oración.
•
Sin mencionar
tecnología.
•
Enfocado en el usuario.
2
¿Para quién?
•
Persona, equipo o
empresa.
•
Usuario final que
consulta.
•
¿Qué saben? ¿Qué
necesitan?
3
¿Con qué documento trabajo?
•
¿Qué corpus de texto
usa el sistema?
•
¿Dónde está y qué tan
accesible es?
•
¿Está estructurado o
no?
4
¿Qué tipo de RAG construyo?
•
Track A: Naive RAG /
RAG básico.
•
Track B: RAG avanzado
/ Agentic.
•
Elegí según el corpus y
el caso.
5
¿Cómo voy a saber si funciona?
•
Una métrica RAG (faithfulness, answer relevance, context
recall).
•
Una evaluación cualitativa: ¿responde bien preguntas
reales?
•
Una pregunta de golden-set que el sistema debe responder
correctamente.

## Pagina 28

RAG PROJECT CANVAS
Título del Proyecto:
CORPUS / DATOS
¿Qué documentos o fuentes de texto
indexa el RAG? (PDFs, webs, DBs, APIs)
MODELO LLM
¿Qué LLM genera las respuestas? (GPT-4,
Claude, Llama…)
EMBEDDINGS & RETRIEVAL
¿Qué modelo de embeddings? ¿Qué
vector store? (FAISS, Pinecone, Chroma…)
PROPUESTA DE VALOR
¿Qué valor añade la búsqueda semántica
sobre documentos propios? ¿Por qué
RAG y no fine-tuning?
INTEGRACIÓN
¿Cómo se conecta a sistemas existentes?
(API, plugin, chat UI…)
STAKEHOLDERS
¿Quiénes son los interesados? (sponsor,
equipo, soporte)
USUARIOS FINALES
¿Quiénes consultan el sistema? ¿Cuál es
su perfil técnico?
COSTOS
Indexación (embeddings batch), almacenamiento vectorial, tokens LLM por consulta, hosting, mantenimiento del
corpus.
MÉTRICAS RAG
Faithfulness · Answer Relevance · Context Recall · Latencia por
consulta · Tasa de hallucination
VALOR / INGRESOS
¿Cómo genera valor económico? (ahorro soporte, licencias,
productividad)

## Pagina 29

RAG PROJECT CANVAS — Ejemplo 2
Asistente Legal — Estudio de Abogados
CORPUS / DATOS
Contratos firmados (.docx/.pdf),
jurisprudencia nacional descargada,
modelos de cláusulas propios del
estudio, legislación vigente
(BOE/Infoleg). ~15.000 documentos.
MODELO LLM
Claude 3 Sonnet (Anthropic API).
Instrucción explícita: 'Cita siempre la
fuente y artículo exacto'. No genera
consejos finales, solo referencia
normativa.
EMBEDDINGS & RETRIEVAL
Cohere embed-multilingual-v3. Vector
store: Weaviate (self-hosted). Chunking
semántico por párrafo. Top-K: 8
fragmentos + reranking.
PROPUESTA DE VALOR
Reduce tiempo de investigación legal de
4h a 20 min por caso. Disminuye riesgo
de cláusulas contradictorias. Permite a
juniors trabajar casos más complejos.
INTEGRACIÓN
Plugin para Word (Office Add-in). Acceso
web seguro con login SSO. API interna
con logs de cada consulta para auditoría.
STAKEHOLDERS
Sponsor: Socio director. Equipo técnico:
freelancer ML. Usuarios clave: 5
abogados senior que validan respuestas.
USUARIOS FINALES
Abogados del estudio (senior y junior).
Nivel técnico: bajo en IA. Buscan
referencias normativas rápidas durante
redacción de contratos.
COSTOS
Weaviate self-hosted: $120/mes (VPS). Cohere embeddings: $50 indexación inicial. Claude Sonnet:
~$0.008/consulta. 200 consultas/día → ~$48/mes tokens.
MÉTRICAS RAG
Context Recall > 0.90 (documentos relevantes recuperados). Cita
correcta del artículo legal en >95% de casos. Tiempo promedio
de consulta < 10 seg.
VALOR / INGRESOS
Factura 2 horas más por caso complejo (precio liberado). ROI
estimado: 3x en 6 meses. Diferenciación competitiva frente a otros
estudios.

## Pagina 30

RAG PROJECT CANVAS — Ejemplo 3
Buscador de Políticas Internas — RRHH Corporativo
CORPUS / DATOS
Manual del empleado, políticas de
vacaciones y licencias, reglamento
interno, convenios colectivos,
formularios descargables. ~200
documentos PDF. Actualización mensual.
MODELO LLM
Llama 3.1 8B (self-hosted, Ollama). 100%
on-premise por confidencialidad.
Temperatura 0 para respuestas
deterministas sobre políticas.
EMBEDDINGS & RETRIEVAL
nomic-embed-text (local). Vector store:
ChromaDB (local). Chunking: por sección
de documento. Top-K: 3 fragmentos.
Pipeline: LangChain.
PROPUESTA DE VALOR
Empleados obtienen respuestas a
preguntas de RRHH en segundos, sin
email. RRHH libera 10h/semana de
consultas repetitivas. 100% privacidad de
datos.
INTEGRACIÓN
Chatbot en Slack (app bot). Acceso web
interno (intranet). Sin conexión a
internet. Datos nunca salen del servidor
de la empresa.
STAKEHOLDERS
Sponsor: Director RRHH. IT: aprueba
infraestructura on-premise. Legal: revisa
políticas indexadas. Empleados: usuarios
finales.
USUARIOS FINALES
Todos los empleados de la empresa (~800
personas). Perfil: no técnico. Preguntas
típicas: '¿Cuántos días de vacaciones
tengo?' '¿Cómo pido licencia?'
COSTOS
Servidor local: $0 adicional (usa infra existente). Ollama + Llama: gratis (open source). ChromaDB: gratis.
Mantenimiento corpus: 4h/mes del equipo RRHH.
MÉTRICAS RAG
Answer Relevance > 0.85. Reducción de emails a RRHH en 40%
(medición mensual). Feedback binario de usuario (
/
) por
respuesta. Cobertura de temas > 90%.
VALOR / INGRESOS
Ahorro de 10h/sem del equipo RRHH → $18K/año. Mejora de
experiencia del empleado (encuesta eNPS). Escalable a otras áreas
(Legal, Compras).

## Pagina 31

preencoded.png
Canvas para RAG — Arquitectura y Decisiones
Un canvas especializado para proyectos Track A (RAG/Chatbot). Incluye 6 secciones clave:
1. Fuentes de datos
¿De dónde vienen los documentos? (PDFs, web, bases de datos, APIs)
2. Estrategia de chunking
¿Cómo divides los documentos? (tamaño, solapamiento, estrategia)
3. Embeddings y búsqueda
¿Qué modelo de embeddings? ¿Qué vector database? (Qdrant, Pinecone, Weaviate)
4. Contexto y prompt
¿Cómo armas el contexto? ¿Cuántos documentos? ¿Qué instrucciones al LLM?
5. LLM elegido
¿Qué modelo? (GPT-4, Claude, Llama, Gemini) ¿Parámetros de temperatura y tokens?
6. Evaluación
¿Cómo mides calidad? (RAGAS, evaluación manual, métricas de relevancia)

## Pagina 32

preencoded.png
Dinámica de hoy
Ronda de presentaciones
Canvas template

## Pagina 33

preencoded.png
Ronda de presentaciones
Cada alumno tiene 3 minutos para explicar
01
Problema
¿Qué querés resolver?
Dato inexistente o inaccesible
02
Usuario
¿Para quién es la solución?
Alcance demasiado ambicioso
03
Datos
¿Qué dato tenés o de dónde lo obtenés?
Problema mal definido
04
IA
¿Cómo lo resolverías con IA?
✓ Track claro (A o B)
Uso concreto y acotado

## Pagina 34

preencoded.png
Entregable de esta clase
Ficha de Proyecto
1.
Problema en una oración
2. Dataset identificado o estrategia para obtenerlo
3. Track declarado (NLP Clasico, RAG, Agentes) + justificación breve
4. Canvas completo

