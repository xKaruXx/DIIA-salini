# 02b_EDA_NLP & RAG

- Fuente: `02b_EDA_NLP & RAG.pdf`
- Tipo: PDF
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

- Paginas extraidas: 13

## Pagina 1

EDA para NLP & RAG
V2  VERSIÓN 2
BOLETÍN OFICIAL DE SALTA · EDICIÓN N° 21.922 · 31/03/2025
Segmentación por Patrón OP N° — Pipeline RAG para Documentos Legales de la Provincia de Salta
📄 Corpus
Boletín Oficial de Salta — Edición N° 21.922  31/03/2025
🔍 Patrón
OP N°: SAXXXXXX — marcador de FIN de documento (robusto, invariante)
📦 Resultado
12 documentos extraídos 0 filtros manuales — totalmente automático)
🔑 Mejora clave
OP N° disponible como metadata indexable → filter(op_numero='SA100050312')
F3 Chunking
F2 Limpieza
F1 EDA
F0 Ingesta

## Pagina 2

Fase 0.1  Extracción de Texto del PDF con pdfplumber
¿Qué hace pdfplumber?
01
Acceso por página
Abre el PDF y accede a cada página como objeto independiente
02
Extracción de texto
Extrae texto con page.extract_text() preservando saltos de línea
03
Limpieza de cabecera
Aplica regex para eliminar la cabecera repetida en cada página
04
Corpus lineal
Concatena el texto limpio en un corpus lineal continuo
HEADER_RE = re.compile(
r'Edición N\[°º\] \[\\d\\.\]+\\n'
r'Salta, \[^\\n\]+\\n'
r'Decreto Reglamentario\[^\\n\]+\\n',
re.IGNORECASE
)
for page in pdf.pages:
raw = page.extract_text()
clean = HEADER_RE.sub('', raw)
corpus += clean + '\\n'

## Pagina 3

Fase 0.2  Segmentación por OP N°: Marcador de FIN de Documento V2
NUEVO V2
Estructura del Boletín Oficial
┌──────────────────────────────────────────┐
│ Edición N° 21.922 ← BOILERPLATE│
│ Salta, lunes 31 de marzo ← BOILERPLATE│
│ Decreto Reglamentario N°.. ← BOILERPLATE│
├──────────────────────────────────────────┤
│ │
│ DECRETO Nº 168 │
│ MINISTERIO DE SEGURIDAD... │
│ VISTO el pedido de Retiro... │
│ ...cuerpo del documento... │
│ │
│ SÁENZ - Solá Usandivaras │
│ Fechas de publicación: 31/03/2025 │
│ OP N°: SA100050312 ◄── DELIMITADOR │
└──────────────────────────────────────────┘
✅ Invariante
Mismo formato en todos los boletines
✅ Único por doc
Nunca aparece en el cuerpo del
documento
✅ 12 docs extraídos
vs 11 de V1 (sin filtros ad-hoc)
✅ Filtros RAG directos
op_codigo y op_numero disponibles como
filtros
✅ Etiquetas OP
En todos los gráficos EDA para trazabilidad
PATRON_OP = re.compile(
r'OP\\s\*N\[°º\]:\\s\*\[A-Z\]\*\\d{6,}',
re.IGNORECASE
)
prev_end = 0
for op_match in PATRON_OP.finditer(corpus):
bloque = corpus[prev_end : op_match.end()]
op_cod = op_match.group()
op_num = re.search(r'\\d{6,}', op_cod).group()
prev_end = op_match.end()

## Pagina 4

SEPARADOR DE DOCUMENTOS
PATRON

## Pagina 5

Fase 0.3  Mapa Posicional del Corpus por OP N° (exclusivo
V2
Cada barra = un documento. Ancho = tamaño en chars. Etiqueta = código OP oficial.

## Pagina 6

EDA 1.1  Distribución de Longitud (eje = OP N°)
F1  EDA
1. Distribución de Carga (Izquierda): Los Decretos
(azul) son los documentos más extensos, superando
frecuentemente el límite crítico de 500 palabras. Esto
confirma que no podemos procesarlos como piezas
únicas y que la segmentación (chunking) es obligatoria
para evitar la pérdida de contexto en los modelos de
lenguaje.
2. Correlación Morfológica (Centro): Existe
una relación lineal perfecta entre palabras y
caracteres en todos los tipos de documentos.
El dataset es sumamente predecible, lo que
nos permite automatizar el procesamiento
con total confianza. El lenguaje legal aquí
tiende a palabras largas (promedio de 6.3
caracteres).
3. Estabilidad del Ratio (Derecha): El ratio de
0.158 pal/char es uniforme, sin importar si es
una Ley o una Decisión Administrativa. Esta
"constante" es nuestra regla de oro: nos
permite fijar un chunk size de ~3,165
caracteres para garantizar fragmentos de 500
palabras, optimizando así la precisión de las
búsquedas y el costo de tokens.

## Pagina 7

EDA 1.2  Densidad de Stop-words en el Corpus Legal
1. Prevalencia de Stop-words (Izquierda): El
análisis muestra que aproximadamente el 40% de
cada documento está compuesto por palabras
funcionales (stop-words). Esta densidad es
notablemente estable en todas las categorías
(Leyes, Decretos y Decisiones Administrativas), lo
que indica que casi la mitad del volumen de texto
no aporta carga semántica directa, pero es vital
para la estructura sintáctica.
2. Identificación de Ruido vs. Contexto (Derecha): El ranking
de las 20 palabras más frecuentes está liderado por conectores
básicos ("de", "la", "el"). Sin embargo, el análisis destaca una
distinción crítica para el dominio legal: términos como "no" o
"será" (marcados para preservar) no deben ser eliminados. En el
contexto normativo, una stop-word estándar como "no" cambia
radicalmente el sentido de una obligación o prohibición.
Implicancia para el Modelo: Debido a esta alta densidad, se recomienda no utilizar listas de
stop-words genéricas. Para este motor de búsqueda, mantendremos las palabras que
definen lógica jurídica (negaciones y tiempos verbales de mandato) para asegurar que el
modelo entienda correctamente las jerarquías y obligaciones legales.

## Pagina 8

EDA 1.3  NGramas: Frases Compuestas del Dominio Legal
F1  EDA
Las frases en rojo configuran los separadores negativos del Recursive
Split: nunca cortar 'retiro voluntario'
•
'retiro voluntario' aparece 12x — frase compuesta crítica que no debe
dividirse
•
'suboficial principal/mayor' — cargo + rango → preservar unidad
semántica
🔑 N-gramas detectados → configuran los SEPARADORES del Recursive
Split para garantizar integridad semántica en el chunking

## Pagina 9

EDA 1.4  Similitud TFIDF (eje Y  OP N°)
F1  EDA

## Pagina 10

EDA 1.5  Outliers de Longitud (eje = OP N°)
F1  EDA
🔴 Outlier corto
SA100050326 Decreto 188 renuncia): más corto → revisar contenido
🟢 Rango óptimo
10 de 12 documentos en rango óptimo 80600 palabras para chunking

## Pagina 11

EDA 1.6  NER Entidades para Filtros
RAG
🔑 Validación
El campo OP_CODIGO aparece exactamente 12 veces
→ confirma que la segmentación es correcta 1 OP
por doc)
📌 DNI  Legajo
10+ ocurrencias por decreto → metadata de persona
indexable directamente en Chroma/Pinecone
1. Distribución de Entidades (Izquierda): El modelo
NER identifica el "NÚMERO_DECRETO" como la
entidad predominante (76 ocurrencias), seguida por
"MINISTERIO" y "RANGO_POLICIAL". Esta jerarquía
define nuestras prioridades para la extracción
automática de datos: estos campos son los candidatos
naturales para convertirse en los filtros principales de
búsqueda.
2. Especificidad por Documento (Derecha): Se
observa una alta concentración de entidades en los
Decretos (DEC), mientras que las Leyes (LEY) y
Decisiones Administrativas (DA) muestran una
densidad mucho menor. Esto sugiere que los Decretos
actúan como "nodos conectores" en el sistema,
vinculando personas (DNI), instituciones (MINISTERIO)
y procesos (EXPEDIENTE).
Nota clave para la slide: "La extracción de estas entidades transforma texto no estructurado en una base de
conocimiento navegable, permitiendo cruzar normativas con datos duros como números de legajo o DNI."

## Pagina 12

EDA 1.7  TTR / Lexical Richness + EDA 1.8  Unicode
F1  EDA
1. Diversidad de Vocabulario (Izquierda): Al comparar el TTR simple
(Type-Token Ratio) con el MATTR (Moving Average TTR),
observamos que la riqueza léxica real es significativamente alta (>0.7).
Esto indica que los documentos no son repetitivos, sino que utilizan un
vocabulario jurídico técnico muy variado, lo que justifica un análisis
más profundo de las raíces de las palabras.
2. Consistencia en la Complejidad (Derecha): El gráfico de MATTR vs
Tokens muestra que, independientemente de la extensión del documento
(desde 300 hasta 1200 tokens), la riqueza léxica se mantiene estable. Los
Decretos (azul) tienden a ser los documentos léxicamente más densos,
lo que aumenta la dificultad para que una búsqueda por "palabra exacta"
encuentre resultados relevantes.
"La alta sofisticación del lenguaje legal detectada exige normalización (lematización) para asegurar que la
riqueza del vocabulario no se convierta en una barrera para la recuperación de información."

## Pagina 13

Próximos Pasos — Indexación y Evaluación RAG
Pipeline V2 listo para producción
from sentence_transformers import SentenceTransformer
import chromadb, json
# 1. Cargar JSONL generado en Fase 3
with open('boletin_salta_chunks.jsonl') as f:
records = [json.loads(l) for l in f]
# 2. Embeddings multilingüe
model = SentenceTransformer(
'intfloat/multilingual-e5-large'
)
embeddings = model.encode(
[r['texto'] for r in records],
show_progress_bar=True
)
# 3. Indexar en Chroma con metadatos
client = chromadb.Client()
col = client.create_collection('boletin_salta')
col.add(
embeddings = embeddings.tolist(),
documents = [r['texto'] for r in records],
metadatas = [{k:v for k,v in r.items() if k!='texto'} for r in records],
ids = [r['chunk_id'] for r in records]
)
# 4. Query con filtro OP — EXCLUSIVO V2
results = col.query(
query_texts = ['Retiro voluntario policial Salta'],
where = {'op_numero': 'SA100050312'},
n_results = 5
)
01
JSONL exportado
boletin_salta_chunks.jsonl con op_codigo + 7 flags de metadatos
02
Embeddings
multilingual-e5-large o text-embedding-3-small para vectorización
03
Chroma / Pinecone
Indexar con metadatos completos — OP N° como filtro directo en queries
04
RAGS Evaluation
Métricas: faithfulness, answer_relevancy, context_recall por tipo de documento
Pipeline V2 completamente operativo: segmentación automática, metadatos OP N°
indexables y evaluación RAG lista para producción.

