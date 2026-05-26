# 02a EDA Visualización

- Fuente: `02a_EDA_Visualización.pdf`
- Paginas extraidas: 28
- Fecha de extraccion: 2026-05-20

> Documento generado automaticamente a partir del texto extraido del PDF. Puede requerir ajustes manuales de formato cuando el PDF contiene columnas, imagenes o elementos visuales.

## Pagina 1

DIPLOMATURA EN IA · UBA · TRABAJO FINAL
Clase 2 · EDA y
Visualización
Análisis Exploratorio + Reglas de visualización + Tu
proyecto
Boletín Oficial Salta · seaborn / matplotlib · datos reales
Teoria → Ejemplo practico → Tu proyecto

## Pagina 2

Agenda de hoy
01
Teoria
Que es EDA. La regla de oro. Tipos de variables.
15MIN
02
Reglas de visualizacion
Tabla de decision: que grafico para que tipo de dato. 8
reglas con ejemplos.
20MIN
03
Ejemplo practico
Aplicamos las 8 reglas al Boletin Oficial Salta N 21.922 con
datos reales.
15MIN
04
Tu proyecto
Cada uno aplica el EDA a su propio dataset. Ronda de
presentacion.
25MIN

## Pagina 3

Parte I · Teoria
Que es EDA y por que hacerlo antes de modelar
1
Cargar datos
2
Explorar estructura
3
Identificar problemas
4
Visualizar relaciones
5
Documentar hallazgos
EDA, o Exploratory Data Analysis, es el proceso de explorar y resumir un dataset para entender su estructura y calidad
antes de modelar. Es esencial porque permite detectar patrones, tendencias y anomalías desde el inicio, evitando errores y
decisiones basadas en supuestos incorrectos.
Tambien ayuda a identificar problemas como valores faltantes, outliers, variables mal codificadas, distribuciones sesgadas
y relaciones inesperadas entre variables.

## Pagina 4

La regla de oro del EDA
EDA es el proceso de examinar los datos ANTES de modelar. No se trata de confirmar hipotesis, sino de descubrir
la estructura real, las anomalias y las relaciones que existen en los datos.
01
Mira ANTES de modelar
El 80% de los problemas del modelo se detectan en el EDA.
Un grafico vale mas que mil supuestos.
02
Documenta cada hallazgo
Cada grafico necesita 1 oracion debajo explicando que
encontraste y que implica para el modelo.
03
Cuestiona lo obvio
Los datos gubernamentales tienen errores reales. 'Este dato
no tiene sentido' es una hipotesis valida.
04
Baseline antes de modelo complejo
El baseline mide el punto cero. Sin baseline no sabes si tu
modelo agrega valor.

## Pagina 5

Tipos de variables: la base para elegir el grafico
Numerica continua
Ej: Precio, edad, longitud de texto, IPC
Numerica discreta
Ej: Cantidad de articulos, palabras por documento
Categorica nominal
Ej: Tipo de documento, ministerio, especie
Categorica ordinal
Ej: Clase del barco 1a/2a/3a), nivel de severidad
Binaria
Ej: Sobrevivio / no sobrevivio * activo / inactivo
Texto libre
Ej: Contenido del decreto, transcripcion, comentario
Antes de cada grafico: identifica el tipo de cada variable involucrada.

## Pagina 6

Ejemplo de Dataset: Todos los Tipos de Variables
Para consolidar la comprensión de los tipos de variables, a continuación se presenta un ejemplo de una fila de datos que incluye cada
uno de los tipos:
Numerica
Continua
Numeric
a
Discreta
Categorica
Nominal
Categorica
Ordinal
Binaria
Texto Libre
150.75
3
Producto
Alto
Si
Descripción detallada del producto con
características únicas y componentes
innovadores.
Este ejemplo demuestra cómo una misma entrada de datos puede contener diferentes formatos, cada uno requiriendo un enfoque
específico para su análisis y visualización.

## Pagina 7

Parte II · Reglas de visualización
Qué gráfico para que tipo de dato
Importancia
Elegir el gráfico correcto es clave para comunicar ideas con claridad. Una
visualización equivocada puede ocultar patrones importantes, exagerar
diferencias o incluso llevar a interpretaciones erróneas. En cambio, el gráfico
adecuado permite identificar tendencias, comparaciones y relaciones casi
de inmediato, haciendo que el mensaje sea más fácil de entender y más
convincente.
Consejos prácticos
Para usar bien la tabla de decisión, comienza identificando el tipo de variables que tienes: numéricas, categóricas, temporales o mixtas. Después, busca en la
tabla la combinación que mejor encaja con tus datos y, sobre todo, piensa en la pregunta que quieres responder. No es lo mismo querer comparar categorías,
mostrar una evolución en el tiempo o analizar una relación entre variables; la intención de análisis debe guiar la elección del gráfico.
8 reglas
A continuación se presentan 8 reglas de visualización que te ayudarán a tomar mejores decisiones. Cada regla mostrará un escenario específico, acompañado
de ejemplos de código y buenas prácticas para aplicarlo correctamente en casos reales.

## Pagina 8

Tabla de decision: el grafico correcto
Esta tabla resume qué visualización conviene usar según el tipo de datos y la combinación de variables que tengas. Cada gráfico está pensado para
responder preguntas distintas, así que sirve como guía rápida para elegir la opción más adecuada según la situación que quieres analizar.
Úsala como referencia práctica: identifica si tus variables son numéricas, categóricas o mixtas, y luego elige el gráfico que mejor se adapte a la pregunta
que quieres responder.
Situacion
Grafico
Codigo seaborn
1 Numerica
Histograma + KDE
sns.histplot(kde=True)
1 Categorica
Barras horizontales
sns.countplot() / ax.barh()
Numerica x Numerica
Scatter plot
sns.scatterplot() / sns.regplot()
Numerica x Categorica
Boxplot + Stripplot
sns.boxplot() + sns.stripplot()
Categorica x Categorica
Heatmap de conteos
pd.crosstab() + sns.heatmap()
Comparar distribuciones
KDE superpuestas / ECDF
sns.kdeplot(hue=...)
Muchas variables numericas
Heatmap correlacion
df.corr() + sns.heatmap()
Vista exploratoria general
Pairplot
sns.pairplot(hue=...)
Texto / NLP
Barras de frecuencia
Counter() + ax.barh()

## Pagina 9

NUMERICA
Regla 1 · Una variable numerica: Histograma + KDE
Usa SIEMPRE las dos capas: histograma (exacto) + KDE (suavizado). Un
histograma solo puede enganar si bins esta mal elegido.
sns.histplot(df['palabras'],
bins=30, kde=True, color='teal')
\# Lineas de tendencia central
plt.axvline(df['palabras'].median(),
color='tomato', linestyle='--',
label='Mediana')
plt.axvline(df['palabras'].mean(),
color='navy', linestyle='--',
label='Media')
\# Para comparar grupos:
sns.kdeplot(grupo_A, fill=True, alpha=0.35)
sns.kdeplot(grupo_B, fill=True, alpha=0.35)
Evitar: histograma solo sin KDE. El numero de bins cambia la forma
percibida.

## Pagina 10

CATEGORICA
Regla 2 · Una variable categorica: Barras
\# Siempre ordenar de mayor a menor
conteo = df['tipo'].value_counts()
.sort_values()
\# Horizontal si las etiquetas son largas
ax.barh(conteo.index, conteo.values,
color=colores, alpha=0.85)
\# Agregar valores al costado
for bar, val in zip(ax.patches, valores):
ax.text(val+0.3,
bar.get_y()+bar.get_height()/2,
str(val), va='center',
fontweight='bold')
+ Barras horizontales
Etiquetas largas o muchas categorias
+ Countplot vertical
Pocas categorias con etiquetas cortas
x Pie chart
Solo 23 categorias. Evitar siempre si es
posible.
x Barplot de medias
Nunca: oculta la distribucion completa.

## Pagina 11

NUM X NUM
Regla 3 · Numerica x Numerica: Scatter plot
\# Basico con correlacion
ax.scatter(df['x'], df['y'],
alpha=0.5, edgecolors='white', s=50)
r = df[['x','y']].corr().iloc[0,1]
ax.text(0.05, 0.92, f'r = {r:.2f}',
transform=ax.transAxes, fontsize=13)
\# Con color por grupo + regresion
for grupo, color in grupos.items():
mask = df['tipo'] == grupo
ax.scatter(df[mask]['x'], df[mask]['y'],
color=color, label=grupo, alpha=0.6)
sns.regplot(data=df, x='x', y='y',
scatter=False, linestyle='--')
r < 0.3
Correlacion debil
0.30.7
Correlacion moderada
r > 0.7
Correlacion fuerte
N  5.000
Usar hexbin (overplotting)

## Pagina 12

NUM X CAT
Regla 4 · Numerica x Categorica: Boxplot
\# La combinacion ideal: estructura + puntos
sns.boxplot(data=df, x='tipo', y='palabras',
palette=colores, showfliers=False, width=0.5)
sns.stripplot(data=df, x='tipo', y='palabras',
color='black', alpha=0.3, size=3, jitter=True)
ax.set_yscale('log') # cuando rango > 10x
boxplot
Primera exploracion
violinplot
Cuando la forma importa
stripplot
N  100 (ver puntos)

## Pagina 13

CAT X CAT
Regla 5 ·
Categorica x Categorica:
Heatmap de conteos
\# Paso 1: tabla de contingencia
ct = pd.crosstab(df['tipo'], df['seccion'])
\# Paso 2: heatmap de conteos
sns.heatmap(ct, annot=True, fmt='d',
cmap='YlOrRd', linewidths=0.5)
\# Paso 3: normalizado por fila
ct_norm = ct.div(ct.sum(axis=1), axis=0)
sns.heatmap(ct_norm, annot=True,
fmt='.0%', cmap='Blues',
vmin=0, vmax=1)
annot=True
Siempre activar — numero hace el
grafico autoexplicativo
fmt='d'
Enteros. Usar '.0%' para porcentajes
cmap='RdBu_r'
Diverging: para proporciones
centradas en 50%
Mostrar ambos
Conteos Y proporciones dan
perspectivas distintas

## Pagina 14

Regla 6 · Comparar distribuciones: KDE y ECDF
\# KDE superpuestas — la mas facil de leer
for grupo, color in zip(grupos, colores):
subset = df[df['grupo']==grupo]['valor']
sns.kdeplot(subset, label=grupo,
fill=True, alpha=0.35, linewidth=2)
\# ECDF — sin bins, sin parametros
subset_sorted = subset.sort_values()
n = len(subset_sorted)
y_ecdf = np.arange(1, n+1) / n
ax.step(subset_sorted, y_ecdf,
label=grupo, linewidth=2)
KDE
+ Visual, fácil de leer
- Bandwidth puede engañar
ECDF
+ Sin parámetros, leer cuartiles directo
- Menos intuitiva
Hist. apilados
+ Muestra conteos reales
- Difícil comparar grupos

## Pagina 15

Regla 7 · Muchas variables: Heatmap de correlacion
\# Siempre con mascara del triangulo superior
corr = df[num_cols].corr()
mask = np.triu(np.ones_like(corr,
dtype=bool))
sns.heatmap(corr,
mask=mask, # triangulo inferior
annot=True,
fmt='.2f',
cmap='RdBu_r', # diverging
center=0, # 0 en el centro
vmin=-1, vmax=1) # escala completa
mask=np.triu(...)
Oculta triangulo superior — sin este,
la info se duplica
cmap='RdBu_r'
Rojo = negativa, Azul = positiva,
Blanco = 0
center=0
Garantiza que 0 quede en color
neutro
vmin=-1, vmax=1
Fuerza rango completo aunque
datos no lleguen a extremos

## Pagina 16

Regla 7b · Pairplot: vista exploratoria completa
Que muestra el pairplot
•
Diagonal: distribucion por variable
•
Off-diagonal: scatter de cada par
•
Color: separacion por clase
•
De un vistazo: correlaciones + clusters
Codigo
sns.pairplot(
df, hue='clase',
diag_kind='hist',
plot_kws={'alpha':0.5,
's':30},
height=2.2
)
Limitacion: ilegible con mas de 67 variables.

## Pagina 17

Regla 8 · Texto y NLP: frecuencias de términos
from collections import Counter
import re
STOP = {'de','la','el','en','y','a','los','se',...}
def tokenizar(texto):
texto = re.sub(r'[^a-zaeiouun\s]', ' ',
texto.lower())
return [t for t in texto.split()
if len(t)>3 and t not in STOP]
freq = Counter(tokenizar(texto))
top = freq.most_common(7)
ax.barh([t for t,_ in top][::-1],
[v for _,v in top][::-1],
color=color)
Hallazgo clave
Los vocabularios son muy distintos entre tipos de documento. Decreto vs.
Sucesorio vs. Adjudicacion tienen terminos completamente diferentes. → Alta
separabilidad semantica → TFIDF  LR puede ser suficiente para Track B.

## Pagina 18

Errores mas comunes de visualizacion

## Pagina 19

Principios de diseño: graficos que comunican
1
Titulo = el hallazgo
Malo: 'Longitud' Bueno: 'Los decretos son 15x mas largos que los edictos'
2
Ejes con unidades
Malo: 'y' Bueno: 'Palabras por documento' o 'USD' o 'Tokens BPE'
3
Alpha para superposicion
Cuando los puntos se superponen: alpha=0.4. Sin alpha: informacion oculta.
4
Un gráfico = un hallazgo
Si el grafico necesita 3 parrafos para explicarse, dividilo en dos.
5
Ordenar categorias
Siempre de mayor a menor. La posición importa para la lectura visual.
6
Grid suave
alpha=0.3 en el grid. Fondo blanco limpio. Los spines top y right, apagados.

## Pagina 20

Parte III · Ejemplo práctico
Las 8 reglas aplicadas al Boletín Oficial Salta N 21.922

## Pagina 21

Panel EDA completo — Boletin Oficial Salta N° 21.922

## Pagina 22

Hallazgos del EDA — lo que aprendimos de los datos
1
Distribucion muy asimetrica
Mediana 120 palabras, media 380. Skewness positivo. Escala log necesaria. Los decretos tiran la media hacia arriba.
2
Adjudicaciones + contrataciones dominan
65% del corpus. Son documentos cortos y repetitivos. Para RAG: aportan poco contexto. Para Track B: clase mayoritaria.
3
La longitud discrimina fuertemente
Decretos 1.200 palabras vs. adjudicaciones 90 palabras (ratio 13x). Un clasificador con solo esta feature ya tiene poder
predictivo.
4
73% de OPs caben en 512 tokens
La mayoria de documentos no necesitan chunking. El retriever va a recuperar OPs completas en la mayoria de los casos.
5
Vocabularios muy distintos por tipo
Los terminos de decretos, sucesorios y adjudicaciones casi no se solapan. → TFIDF  LR puede ser suficiente para Track B.

## Pagina 23

PARTE IV
Tu proyecto
Aplica las 8 reglas a tu propio dataset

## Pagina 24

Dinamica: EDA de tu proyecto — 25 minutos
\# TEMPLATE — completar para cada visualización
\# ─────────────────────────────────────────────────────
\# Variables: [nombre y tipo: numerica / categorica / texto]
\# Pregunta: [que quieres saber?]
\# Grafico elegido: [histplot / boxplot / scatter / heatmap / etc.]
\# Justificacion: [por que ESTE grafico? consulta la tabla de decisión]
fig, ax = plt.subplots(figsize=(10, 5))
\# sns.GRAFICO(data=tu_df, x='...', y='...', palette='Set2', ...)
\# ax.set_title('Titulo = el HALLAZGO, no el nombre de la variable')
plt.show()
\# Hallazgo: [1 oracion con lo que encontraste]
\# Impacto en modelo: [como afecta a tu RAG o clasificador?]
Minimo: 3 graficos de tipos distintos segun la tabla de decision.
Cada grafico = 1 pregunta + 1 hallazgo documentado en markdown.
Track A RAG
Distribucion de longitud | Tipos de documento | % que cabe en 512 tokens |
Calidad del texto
Track B Clasificacion)
Balance de clases | Longitud por clase (boxplot) | KDE superpuestas |
Vocabulario discriminante

## Pagina 25

TRACK A · RAG
Guia de EDA  Track A RAG
? Cual es la distribucion de
longitud de mis documentos?
HISTOGRAMA  KDE
Impacto: Define la estrategia de
chunking
? Hay tipos distintos de
documentos en mi corpus?
BARRAS
HORIZONTALES
Impacto: Indexar todo o segmentar
por tipo?
? La longitud varia
significativamente por tipo?
BOXPLOT POR TIPO
Impacto: Chunking diferenciado por
tipo
? Que porcentaje cabe en 512
tokens?
BARRAS POR
CATEGORIA
Impacto: Factor de expansion
chunks/docs
? Hay documentos con muy
poco texto (< 20 palabras)?
HISTOGRAMA  UMBRAL
Impacto: Filtrar antes de indexar

## Pagina 26

TRACK B · CLASIF.
Guia de EDA  Track B Clasificacion)
¿ Cuantos ejemplos hay por
clase? ¿Hay desbalance?
BARRAS ORDENADAS
¿ La longitud separa las
clases?
Impacto: Feature discriminante para el
modelo
BOXPLOT POR CLASE
¿ Las distribuciones de
longitud se solapan?
Impacto: Solapamiento alto = modelo
mas dificil
KDE SUPERPUESTAS
¿ Hay features numéricas
correlacionadas?
Impacto: Evitar features redundantes
HEATMAP CORRELACION

## Pagina 27

Checklist antes de entregar
REQUERIDO
Identifique el tipo de cada variable (numerica / categorica / texto)
Elegi el grafico usando la tabla de decision
El titulo describe el HALLAZGO, no solo el nombre de la variable
Los ejes tienen labels con unidades cuando corresponde
Use alpha para evitar el overplotting en scatter plots
El heatmap tiene mascara de triangulo y cmap diverging centrado en 0
OPCIONAL
Hay un markdown debajo de cada grafico con 1 oracion de hallazgo
El hallazgo tiene un impacto claro en la estrategia del modelo
Al menos 3 graficos de tipos distintos segun la tabla de decision
Celda de resumen completada con los hallazgos del EDA

## Pagina 28

Entregable — antes de la Clase 3
1
Notebook Colab con EDA ejecutado sobre tu propio dataset
2
Al menos 3 gráficos de tipos distintos + hallazgo en markdown
3
Tabla resumen: tipo de doc | longitud media | problemas detectados
4
Celda de hallazgos completada: que aprendiste de tus datos?
El notebook de visualización (tips, titanic, penguins, iris, NLP) esta disponible como referencia.
