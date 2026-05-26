# Taller de trabajo final (2_8) - d015b25_ 2026_05_06 18_55 GMT-03_00 - Notas de Gemini

- Fuente: `Taller de trabajo final (2_8) - d015b25_ 2026_05_06 18_55 GMT-03_00 - Notas de Gemini.docx`
- Tipo: DOCX
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

📝 Las notas

may 6, 2026

Taller de trabajo final (2/8) - d015b25

Invitado salinastalamilla@gmail.com Taller de trabajo final - DIIAA 1Co2025

Archivos adjuntos Taller de trabajo final (2/8) - d015b25

Registros de la reunión Transcripción Grabación

Resumen

La clase cubrió el análisis exploratorio de datos y la optimización de flujos para sistemas de recuperación.

Análisis y exploración datos
El análisis exploratorio de datos resulta esencial para comprender variables y detectar patrones antes de aplicar modelos. Se presentó la importancia de histogramas, diagramas de caja y gráficos de dispersión.

Metodología para texto
La transformación de textos a estructuras tabulares facilita el procesamiento y la creación de metadatos enriquecidos. Se enfatizó el uso de expresiones regulares para optimizar costos de procesamiento sobre modelos complejos.

Flujos de producción
La arquitectura para sistemas de recuperación integra bases de datos vectoriales y léxicas para mejorar la precisión. Se decidió dedicar tiempo futuro a revisiones individuales de proyectos y consultas técnicas.

Próximos pasos

[Santiago Germino] Contactar Academia: Comunicarse con gestión académica debido a su situación excepcional de mudanza. Consultar si aún puede cursar esta materia o puede entregar trabajo anterior.

[Santiago Germino] Enviar Proyecto: Enviar el material armado de la materia anterior.

[lse posgrados] Compartir Bibliografía: Enviar a El grupo libros sobre análisis de datos y visualización. Compartir material sobre data wrangling al finalizar la clase.

[lse posgrados] Subir Notebook: Descargar y subir la nueva notebook al material de clase.

[El grupo] Cargar Documento: Descargar documento 2C y subirlo a la carpeta raíz de la notebook para ejecutar el código.

[El grupo] Aplicar Guías: Aplicar guías de procesamiento de texto usando el ejemplo de la clase durante la semana.

[Marcelo Luna] Combinar Documentos: Unir documentos heterogéneos, agregando una columna categórica (ej. tipo original complemento) para separar tipos en el dataset de chunks.

[Marcelo Luna] Escribir Correo: Enviar correo al instructor sobre dudas de dataset y posgrados.

[Marcelo Luna] Preparar Notebook: Alistar cuaderno para posible discusión en clase.

[Diego Methol] Explorar Dataset: Aplicar exploración de datos al dataset de verdad de campo.

[lse posgrados] Compartir Repositorios: Compartir repositorios clonables. Proveer acceso a las herramientas usadas.

[lse posgrados] Responder Correo: Responder correo electrónico a Shimon. Enviar la respuesta durante el día de hoy.

[lse posgrados] Responder Dudas: Responder consultas enviadas hoy por correo electrónico. Realizar la respuesta lunes o martes.

[lse posgrados] Enviar Librería: Enviar la librería mencionada a Gabi Tallarico.

Detalles

Saludo e introducción y antecedentes laborales: Gabi Tallarico e lse posgrados intercambiaron saludos y discutieron sus horarios apretados. Gabi Tallarico notó que no había abierto los correos electrónicos de lse posgrados debido a su carga de trabajo. lse posgrados comentó que el año estaba avanzando rápidamente y mencionó que trabaja en Ganfen, una empresa de litio con proyectos en Salta y Jujuy (00:00:00).

Bienvenida a Shimon Ben y retroalimentación inicial sobre tareas: Shimon Ben se unió a la reunión. lse posgrados indicó que había visto el correo electrónico de Shimon Ben pero que responderían después de la clase. lse posgrados compartió que, en general, los diez trabajos presentados estaban bastante bien (00:03:13).

Sesgo profesional y antecedentes de Shimon Ben: lse posgrados, siendo de formación ingenieril, busca reducir las tareas a su "mínima expresión" y luego escalarlas. Shimon Ben, cuya experiencia incluye trabajar en servicios y estudiar una licenciatura en artes electrónicas, notó que se sentía alejado del conocimiento "más duro" que tienen otras personas (00:03:13). lse posgrados enfatizó que, aunque el proceso inicial de la curva de aprendizaje puede generar ansiedad, Shimon Ben está haciendo un buen trabajo en sus entregas (00:04:34).

Consulta de Santiago Germino sobre entregas y continuidad del curso: Santiago Germino se disculpó por no haber cumplido con la fecha de entrega de la materia anterior debido a una mudanza reciente (00:05:32). lse posgrados aclaró que las entregas para la materia actual son opcionales y solo tienen el propósito de recibir retroalimentación. La entrega final, consistente en dos documentos y una presentación, es la única que cuenta (00:06:42).

Resolución de la situación de Santiago Germino: Santiago Germino preguntó si debía continuar con la materia actual, ya que no había podido completar la entrega de la materia anterior (00:06:42). lse posgrados indicó que este tipo de consulta debe ser dirigida a gestión académica, aunque ofreció presionar para que respondan rápidamente. lse posgrados sugirió a Santiago Germino continuar con el curso y enviar el trabajo de la materia anterior tan pronto como les sea posible (00:07:37).

Introducción a la clase de exploración y análisis de datos (EDA): La sesión comenzó con una introducción al segundo paso del trabajo, que es la exploración y análisis de datos (EDA) y la visualización. lse posgrados indicó que la mayoría de los trabajos iniciales estaban alineados, y que les había proporcionado retroalimentación para acotar los alcances (00:08:41). El material (una presentación y dos *notebooks*) fue compartido inmediatamente en la carpeta de clases (00:10:00).

Objetivos de la clase y el uso de herramientas de IA: Los temas a tratar son el análisis exploratorio, las reglas de visualización, y la aplicación de estos conceptos a los proyectos de les estudiantes (00:10:00). lse posgrados recomendó que se concentren en el sentido que desean comunicar con el gráfico y en cómo preguntarles a los motores de IA (como Gemini) para generar el código, más que en escribir el código en sí (00:12:51).

Experiencia previa de les estudiantes con visualización de datos: Gabi Tallarico mencionó que tiene bastante experiencia con la visualización de datos utilizando herramientas como Tableau, Locker y Power BI, pero no programando. Gabi Tallarico también tomó un curso de R, pero su conocimiento disminuyó con el tiempo (00:12:51). Shimon Ben y Marcelo Luna indicaron que no manejan R, confirmando que la mayoría utiliza Python (00:14:09).

Proceso de análisis exploratorio de datos (EDA): El proceso de EDA comienza con la carga de datos, seguido por la exploración de la estructura de los datos (columnas, filas, tipos de variables) (00:14:09). El siguiente paso es identificar problemas como valores nulos, lo que es parte del "data wrangling". Finalmente, el objetivo principal es buscar relaciones entre variables para generar *insights* o hallazgos (00:15:21).

Importancia de la exploración y la transformación de datos para PLN: lse posgrados señaló la falta de exploración de datos en los proyectos presentados, especialmente en el procesamiento del lenguaje natural (PLN). Por ejemplo, en PLN, se debe explorar diferentes cantidades de caracteres o *tokens* por *chunk* y el *overlap* (00:16:43) (00:19:27). lse posgrados sugiere que los documentos de texto deben llevarse a una estructura de tabla para el análisis y que una forma simple es calcular el número de palabras por fragmento (00:18:09).

Buenas prácticas en la exploración y modelado de datos: Se recomienda imprimir el resultado de cada paso (*print*) para comprender lo que hace cada función generada. Es crucial documentar cada hallazgo durante la exploración, ya que esto será útil para el modelado posterior. Además, se debe cuestionar la relación entre variables y no descartar una exploración, incluso si dos variables parecen no estar correlacionadas (00:20:35).

Consideraciones sobre el uso de LLMs y enfoque heurístico: La exploración de datos permite hacer análisis sin recurrir a modelos de lenguaje grande (LLMs), lo cual es importante porque los costos de *tokens* pueden aumentar en el futuro. Se deben usar reglas heurísticas y relaciones simples para resolver problemas, como usar el número de palabras por comentario para clasificar la emoción, antes de recurrir a un LLM (00:21:45).

Clasificación de variables y tipos de gráficos: Es fundamental tener claros los tipos de variables (continuas, categóricas) porque el tipo de variable determina el tipo de gráfico a utilizar. La exploración de variables debe ser primero hacia sí misma (cómo se distribuye) y luego en relación con otras variables (00:23:03). Por ejemplo, una variable categórica nominal como los meses del año tiene un rango definido por la cantidad de valores únicos (12 valores) (00:24:22).

Análisis visual de variables categóricas (ejemplo de meses): La forma más fácil de inspeccionar la distribución de una variable categórica es mediante conteos, es decir, cuántas veces ocurre cada categoría. En el ejemplo de los meses, se contarían las ocurrencias de cada mes (00:25:23). Se revisaron ejemplos de clasificación de variables, donde la ID de un viaje se consideró categórica, la fecha de salida como tipo *date*, y las variables numéricas pueden ser enteras (discretas) o continuas (con decimales) (00:26:42).

La pregunta de Gabi Tallarico sobre EDA en proyectos de PLN: Gabi Tallarico preguntó cómo incluir la exploración y análisis de datos en un proyecto de lenguaje natural, ya que lo consideraban como dos mundos separados. lse posgrados respondió con un ejemplo práctico: un histograma que cuenta la cantidad de caracteres por página de un PDF (00:33:59). Este gráfico es útil para evaluar si una función de limpieza está eliminando o alterando el contenido de manera no deseada (00:35:04).

Reglas para la visualización de una variable numérica (Histogramas): El histograma es el gráfico adecuado para explorar una variable numérica hacia sí misma (00:36:24). La desventaja del histograma es que la forma del gráfico depende del tamaño de la "caja" (*bin*), lo que puede afectar la objetividad de la visualización (00:37:54). La alternativa es el gráfico de densidad, que es independiente del número de *bins* (00:39:04).

Utilidad del análisis de la distribución de variables: Conocer la distribución de una variable cuantitativa (por ejemplo, si es bimodal) puede ayudar a separar o categorizar grupos de datos (00:40:19). Al crear histogramas, es útil agregar líneas verticales para indicar la media y la mediana, dirigiendo la atención del espectador hacia el promedio de la variable (00:43:42).

Reglas para la visualización de variables categóricas (Gráficos de barras): Para variables categóricas, el gráfico univariado correspondiente es un conteo, representado por un gráfico de barras (00:43:42). Se debe usar una disposición horizontal si el nombre de la variable es largo para evitar el solapamiento (00:45:14). Es importante que los gráficos de barras estén ordenados, generalmente de mayor a menor, a menos que se quiera comunicar una serie de tiempo (00:46:51).

Componentes clave de los gráficos de barras: Las barras deben incluir etiquetas de valor en la parte superior, ya que no siempre es fácil leer el valor exacto del eje. Los gráficos deben tener un título claro y etiquetas para los ejes, especialmente cuando la variable no se explica por sí misma (00:46:51). Los gráficos de barras son mejores que los gráficos de pastel para mostrar diferencias sutiles entre categorías (00:49:34).

Regla de visualización: Numérica por Numérica (Scatter Plot): Un *scatter plot* es el gráfico adecuado para cruzar dos variables numéricas, donde cada punto representa una fila del *dataset* con la combinación de ambas variables (00:49:34). El análisis de la dispersión de los puntos en el *scatter plot* ayuda a entender la relación y variabilidad entre las dos variables (00:52:30).

Análisis de la dispersión y heterosedasticidad: La variabilidad de los datos se estudia a través de la desviación estándar (00:53:31). En el *scatter plot*, se analiza cómo varían los dos datos relacionados (covariable). El aumento de la dispersión en los datos a medida que una variable avanza se denomina heterosedasticidad y debe ser probada antes de aplicar modelos como la regresión lineal simple (00:54:33).

Asociación y predictibilidad en el Scatter Plot: La medida de asociación lineal se llama coeficiente de regresión (00:55:46). Un coeficiente alto, como 0.82, indica una buena asociación entre las variables, sugiriendo que una variable podría predecir la otra (por ejemplo, la cuenta total prediciendo la propina). Un gráfico de dispersión también puede ayudar a entender la dispersión de una sola variable si se mira solo un eje, similar a un histograma o gráfico de densidad (00:57:00).

Análisis de la dispersión de datos y variables en un Scatter Plot: El orador de lse posgrados explicó cómo las concentraciones de datos en un gráfico de dispersión (Scatter Plot) dependen de la perspectiva y que estos gráficos se pueden dibujar con herramientas como Matplotlib (mat) (01:00:50). Se identificaron tres variables principales en un Scatter Plot de ejemplo: la longitud del pico (variable uno), la profundidad del pico (variable dos) y la categoría (variable tres, en este caso, la especie). La variable categórica se utiliza para agrupar por color y ayuda a separar los grupos visualmente, lo que es útil para problemas de clasificación (01:02:05).

Sintaxis de codificación y documentación para gráficos: Para generar un gráfico con herramientas como Seaborn (SBORN), el código requiere que se especifiquen las variables para los ejes X e Y, y la variable para el color (01:02:05) (01:05:51). El orador de lse posgrados aconseja a los participantes consultar la documentación de las librerías como Seaborn para obtener ejemplos de código y entender la sintaxis, ya que es una práctica recomendada (01:04:53). Se mencionó que, a diferencia de R y GGPlot, en Python con Seaborn la mayor parte del código se incluye en una sola llamada, aunque existe una librería para usar código GGPlot en Python (01:05:51).

Revisión de las reglas de visualización de datos: El orador de lse posgrados repasó las primeras tres reglas de visualización: (1) variable numérica por sí misma, (2) variable categórica por sí misma (conteo) y (3) variable numérica versus variable numérica (Scatter Plot). También introdujeron la cuarta regla: variable numérica versus variable numérica más una variable categórica para la separación por color (01:08:07).

Introducción y comprensión del Boxplot: El boxplot (diagrama de caja) fue presentado como el siguiente tipo de gráfico, y el objetivo era asegurar su comprensión, ya que Shimon Ben tenía dificultades para entenderlo (01:08:07). El boxplot permite visualizar cómo se distribuye una variable numérica, a veces sumando una variable categórica para comparaciones. Un boxplot se construye a partir de cuantiles, específicamente los cuartiles (Q1, Q2/mediana y Q3) (01:09:37).

Explicación de los Cuantiles y su importancia: Se explicó que los cuantiles, que incluyen deciles, percentiles y cuartiles, se construyen ordenando los datos de menor a mayor para identificar dónde se encuentra un porcentaje específico de los datos (01:11:06). Los cuartiles dividen los datos en cuatro partes, siendo Q1 el 25%, Q2 (la mediana) el 50% y Q3 el 75% (01:19:14). Saber esto es importante para identificar los intervalos donde se concentra la mayor parte de los datos relevantes y ayuda a tomar decisiones sobre qué datos incluir o excluir en un modelo (01:13:26).

Funcionalidad y utilidad del Boxplot: La caja del boxplot representa el 50% central de los datos, entre el Q1 y el Q3 (01:17:59). La utilidad del boxplot radica en conocer la distribución de los datos, identificar dónde está la mediana (Q2) para la comparación, y observar la dispersión de los datos. Un boxplot más grande indica mayor dispersión de datos, mientras que uno más pequeño indica mayor concentración (01:21:38).

Aplicación del Boxplot para identificar distribuciones y valores atípicos: El boxplot ayuda a conocer la distribución de una variable y es útil para comparar distribuciones entre diferentes grupos (como la cantidad de palabras en diferentes tipos de documentos) (01:21:38) (01:25:09). También permite identificar valores atípicos o *outliers* de forma visual (01:22:50). La utilidad principal del boxplot es mostrar la distribución de los datos de una sola variable, pero en la práctica se usa a menudo para comparaciones bivariadas con una variable categórica (01:25:09).

Análisis de Boxplots en un contexto de procesamiento de lenguaje natural (NLP): Se utilizó un ejemplo de NLP para demostrar que los decretos tenían más palabras, pero menos dispersión, lo que sugiere que tienen una cantidad similar de palabras, a diferencia de las resoluciones que mostraron más dispersión (01:26:33). Este tipo de análisis visual puede ser sumamente útil para la exploración inicial de un *dataset* de NLP, posiblemente ahorrando el uso de modelos más complejos para segregar la información (01:27:40).

Visualización de dos variables categóricas con Tablas Cruzadas (Cross Tab) y Heatmaps: Cuando se trabaja con dos variables categóricas, se utilizan conteos que pueden ser absolutos o proporcionales. Se mostró un *heatmap* que comunica la predominancia de cenas sobre almuerzos los sábados, lo que requiere un preprocesamiento de datos utilizando una tabla cruzada (Cross Tab) de Pandas (01:28:49). El *heatmap* se aplica a la tabla cruzada para mostrar el conteo de intersecciones (01:30:10).

Uso del Heatmap para Correlación de Variables Numéricas: El *heatmap* también se puede aplicar a dos o más variables numéricas para visualizar su asociación, conocida como coeficiente de correlación (R) (01:31:28). Esto permite ver masivamente si las asociaciones son positivas (cercanas a 1) o negativas (cercanas a -1) y ofrece una vista rápida de las correlaciones entre todas las variables (01:32:57). En contextos de texto, puede usarse para visualizar la similaridad entre documentos (01:34:33).

Visualización masiva con Pair Plot (Gráfico de Pares): La regla siete es el *Pair Plot*, que masivamente toma todas las variables numéricas de un *dataframe* y crea un gráfico que muestra la asociación de todas contra todas (01:34:33). Es útil usar una variable categórica (como la clase o especie) para el color. Se explicó que la información de un lado de la diagonal es redundante (X vs. Y es lo mismo que Y vs. X), por lo que se recomienda usar una máscara (*mask*) para mostrar solo la triangular del gráfico y mejorar la visualización (01:35:59).

Planificación del trabajo y receso: El orador de lse posgrados comentó que habían cubierto una gran cantidad de material y que se tomarían un receso (01:37:29). Se indicó que después del receso se revisaría el código en la *notebook* para que los participantes pudieran copiarlo y aplicarlo en sus propios proyectos (01:38:49). Se hizo un breve repaso de los requisitos para el trabajo final, incluyendo la necesidad de al menos tres gráficos, una tabla de resumen, y la documentación de hallazgos y aprendizaje (01:56:09).

Estrategia para el Análisis Exploratorio de Datos (EDA) de texto: Para el EDA de texto, la primera utilidad es realizar conteos (histogramas de barra) (01:54:49). Se mostró un caso de ejemplo usando un documento de boletín oficial para identificar entidades y preprocesar el texto, y se explicó que el código estará disponible en una *notebook* (la 2C) en el material de clase (01:56:09). Marcelo Luna preguntó sobre la estrategia a seguir con múltiples documentos heterogéneos, a lo que se recomendó unirlos y usar una columna categórica para diferenciarlos (por ejemplo, "original" y "complemento") (01:59:00).

Sugerencia de estructura de datos para posgrados: Marcelo Luna conversó con lse posgrados sobre la estructura de los datos para los posgrados, sugiriendo que se utilice un solo *dataset* en lugar de múltiples. lse posgrados explicó que un solo *dataset* con una columna de separación facilitaría la búsqueda, incluso si un boletín ejecutado aplica a muchos boletines con fechas y contenido semántico distinto. Marcelo Luna indicó que se comunicará por correo para discutirlo más a fondo, aunque lse posgrados sugirió verlo en clase y preparar el *notebook* (02:00:11).

Propósito del sistema de recuperación (RAG): lse posgrados explicó el propósito de un sistema RAG (Retrieval-Augmented Generation) aplicado a boletines oficiales, que permite a las personas usuarias hacer preguntas a una plataforma o chat sobre adjudicaciones y recibir respuestas respaldadas por documentos fuente. Este RAG está diseñado para devolver información precisa, citando el boletín y la fecha, y está respaldado por un agente que verifica que la respuesta se base en el documento consultado (02:01:42).

Estrategia de separación de documentos: El objetivo del sistema RAG es tener un texto limpio para que las preguntas obtengan respuestas adecuadas. lse posgrados describió la estrategia de usar un patrón específico ("fecha de publicación" y "OP") dentro del boletín para separar el corpus general en documentos individuales, asegurando que el RAG lea solo un documento a la vez y no mezcle contenido (02:03:02). Se utiliza un patrón regex para detectar esta línea de identificación, lo que resulta en 12 documentos separados (02:04:37).

Herramientas de interfaz y exploración de datos: Gabi Tallarico preguntó sobre la interfaz de consulta, a lo que lse posgrados respondió que está hecha con Streamlit, una librería gratuita que actúa como *frontend* (02:04:37). La exploración de datos inicial (*EDA*) en el *notebook* incluyó la ingesta, limpieza y *chunking* del texto para conocer el contenido y detectar opciones de limpieza, como la eliminación del encabezado del documento (02:06:00).

Análisis de la limpieza y estructura del documento: Se utilizó un gráfico para comparar el documento antes y después de la limpieza, con el fin de asegurar que no se produjera un exceso de limpieza que resultara en la pérdida de información (02:06:00). El delimitador clave utilizado para la separación de documentos fue el valor "OP". La exploración también incluyó la posición de los caracteres en el corpus para asegurar que el separador funcionara correctamente y no hubiera superposición (*overlap*) entre documentos (02:07:29).

Análisis del contenido y tipo de documento: La exploración de datos incluyó el conteo de palabras por documento, observando que los decretos predominan, con un promedio de casi 600 palabras, mientras que las leyes y decisiones administrativas tienen diferentes conteos (02:08:51). Este análisis ayuda a inferir que los documentos técnicos, como los boletines, tienen una linealidad en la relación entre palabras y caracteres, lo que facilita al LLM (Large Language Model) la predicción de la siguiente palabra cuando usa el RAG (02:10:18).

**Importancia de las *stopwords* y *n-gramas***: Se discutió la utilidad de analizar las *stopwords* (palabras sin contenido semántico) para determinar qué porcentaje de estas existen en cada documento. Se destacó que la eliminación excesiva de *stopwords* podría resultar en la pérdida de contenido semántico importante. La exploración también incluyó el conteo de *bigramas* y *trigramas* para identificar combinaciones de palabras frecuentes, como "provincia de Salta" y "retiro voluntario", lo que indica temas comunes en los documentos (02:11:41).

**Uso de la similitud del coseno y *boxplots***: Se recordó el concepto de similitud del coseno para calcular la similaridad semántica entre documentos, que es una parte fundamental de los sistemas RAG (02:13:11). En documentos legales y técnicos, la alta similitud ayuda a detectar duplicados o redundancia en la información. Los *boxplots* se utilizaron para contrastar la cantidad de palabras por tipo de documento categórico (ley, decreto, decisión administrativa), revelando que los decretos tienen la mayor variabilidad y que la mayoría se sitúa entre 500 y 600 palabras (02:14:45).

Consulta sobre el manejo de múltiples archivos PDF: Juan Pablo Rueda consultó si sus 16 o 17 PDF de productos podrían fusionarse en un solo documento para el análisis (02:16:16). lse posgrados sugirió extraer la información necesaria de esos PDF y organizarla en un *dataset* (filas y columnas). Juan Pablo Rueda mencionó que mucha información se repite entre productos, como el periodo de carencia (02:17:50).

Aplicación de visualización de datos en el análisis de sesgo político: Diego Methol expresó dudas sobre cómo aplicar las visualizaciones a su trabajo de análisis de sesgo político en noticias, ya que su enfoque actual no las utilizaba (02:17:50). lse posgrados explicó que la exploración sirve para conocer y comunicar los datos. Se sugirió graficar cuántas noticias se descartaron y el porcentaje de fragmentos que se eliminaron de las noticias procesadas (02:19:08).

Uso de visualizaciones para el análisis histórico: Diego Methol reconoció el valor de la visualización si se mantiene un histórico de los procesamientos realizados, lo que permitiría visualizar datos como el sesgo político por medio de comunicación (02:19:08) (02:21:55). lse posgrados enfatizó que el objetivo de la exploración es conocer los datos, como contar malas palabras para un análisis de sesgo en comentarios (02:22:57).

Reconocimiento de entidades y riqueza léxica: El reconocimiento de entidades, como el número de decreto o la fecha de publicación, es crucial para generar información que se pueda usar posteriormente (02:22:57). lse posgrados mencionó la métrica de riqueza léxica, la cual ayuda a estimar la cantidad adecuada de *tokens* para el *chunking*, aunque invitó a revisar la teoría más a fondo en la próxima clase. La exploración de datos lleva a tomar decisiones informadas sobre la modelación, como el tamaño del *chunk* (02:24:29).

**Generación de *chunks* con metadatos enriquecidos**: El proceso de exploración ayuda a que el preprocesamiento antes del RAG tenga más sentido y permite añadir metadatos a los *chunks* (02:26:09). lse posgrados mostró un *JSON* donde el *chunk* enriquecido no solo contiene el fragmento de texto, sino también metadatos extraídos como el identificador, la ley asociada, el tipo de documento y la fecha (02:27:53). Este *chunk* más "inteligente" mejora el rendimiento del sistema de recuperación (*retrieval*) (02:29:09).

Estrategia de extracción de metadatos sin LLM: lse posgrados destacó que su enfoque para extraer metadatos utiliza patrones de reconocimiento basados en expresiones regulares (*regex*) en lugar de depender de LLMs para esta tarea. Esto se debe a que la solución *regex* es más simple en código y arquitectura, y evita el alto consumo de *tokens* asociado con el uso repetido de LLMs (02:30:33). Se comentó un caso en el que la gente usaba LLMs para cruzar información fija entre sistemas, lo que generaba un desperdicio de *tokens* (02:32:14).

**Uso de LLM para la generación de código *regex***: Aunque se evitó el uso de LLM para la extracción directa, lse posgrados reveló que usó un LLM para generar el código *regex* que identifica los patrones que permiten extraer metadatos como sanciones, retiros voluntarios y fechas (02:33:48). El valor principal de este método es proporcionar una estructura de datos más ordenada que enriquece el *chunk* para el sistema de recuperación (02:35:04).

**Procedimiento para correr el *notebook***: lse posgrados explicó a la audiencia cómo descargar el *notebook* y subirlo a Colab para ejecutarlo, enfatizando que el objetivo no es que dominen el código, sino que comprendan que sus documentos de texto tienen más información que solo texto plano (02:35:04). La ejecución final del *notebook* genera un *JSON* con los *chunks* y sus metadatos (02:36:51).

Consulta sobre modelos de análisis de sentimiento: Shimon Ben preguntó sobre la disyuntiva de usar un modelo de análisis de sentimiento simple (positivo, negativo, neutro) o uno más complejo que detecte burla e ironía (02:40:01). lse posgrados aconsejó usar el modelo simple si este tiene mejor documentación y un rendimiento probado en el *ground truth* (02:41:36).

Recomendación para la clasificación de sentimientos: Ante la incertidumbre en los modelos más complejos, lse posgrados recomendó a Shimon Ben quedarse con el modelo simple (positivo, negativo, neutro) (02:42:54). Posteriormente, sugirió un enfoque anidado: clasificar primero con el modelo simple y luego aplicar el modelo más complejo dentro de cada categoría resultante (por ejemplo, analizar la ironía solo dentro de los comentarios clasificados como negativos) (02:45:12).

**Flujo de datos en un *pipeline* de producción**: lse posgrados mostró un ejemplo de un trabajo final en la especialización, que se enfocó en un *pipeline* casi en producción para el procesamiento de lenguaje natural, enfatizando el flujo de datos. Se usó Airflow (simulado en el flujo de trabajo) para encadenar tareas, como la descarga de boletines y la extracción de documentos (02:46:35). Se enfatizó la importancia de tener funciones pequeñas y encadenadas para una mayor trazabilidad y escalabilidad (02:47:57).

**Tareas del *pipeline* y persistencia de datos**: El *pipeline* comienza descargando boletines a través de *web scraping* y guardándolos en un sistema de almacenamiento en la nube (Minio, simulando un *bucket* en la nube) (02:49:08). Una segunda tarea extrae los documentos individuales mediante el patrón "OP" y los guarda como archivos TXT limpios, lo cual facilita la trazabilidad para verificar los resultados del RAG (02:50:27).

Trazabilidad y enriquecimiento de datos: Marcelo Luna preguntó si los archivos TXT son el soporte persistente, a lo que lse posgrados confirmó que sí (02:54:21). El flujo de trabajo del *pipeline* incluye una tarea que toma los TXT crudos y les añade metadatos, usando un LLM para la extracción y generando *JSONs* enriquecidos con texto y resumen (02:55:45). Una función posterior une estos *JSONs* para enviarlos a la base de datos vectorial (02:57:52).

Revisión del Proceso de Ingesta y Base de Datos Vectorial: lse posgrados explicó que el documento original fue recompuesto con agregados, resultando en un archivo JSON por cada boletín oficial que contiene "chanks" y metadatos, los cuales son enviados a una base de datos vectorial. El proceso de ingesta implica la limpieza, el "chankeado" y la extracción de metadatos, terminando cuando todos los "chanks" con metadatos se encuentran en la base de datos vectorial, que en este caso es Pinecone (02:58:56). También mencionaron la creación de un índice por el modelo BM25, que indexa documentos léxicamente para permitir búsquedas por palabra, además de las búsquedas por semántica, lo cual forma la base para la respuesta más eficiente y económica (03:00:04).

Implementación de la Consulta y la Interfaz de Usuario: La consulta se realiza a través de una API que actúa como intermediario, traduciendo la pregunta del frontend y buscando por similitud en la base de datos (03:00:04). lse posgrados enfatizó que la ingesta debe extraer toda la información léxica y semántica posible para que, al momento de la pregunta, la respuesta se alimente del contenido semántico de los "chanks" y de los metadatos, proporcionando una respuesta más validada (03:01:24). Se mostró una prueba de consulta utilizando una interfaz construida con Streamlit y conectada con la API de Open AI, aunque la demostración de búsqueda de un nombre específico no arrojó la fuente como se esperaba en el momento (03:02:44).

Discusión sobre la Revisión del Trabajo y el Feedback: Marcelo Luna expresó la necesidad de revisar la parte de ingesta de su proyecto, especialmente lo referente a las expresiones regulares, y sugirió dedicar tiempo en cada clase para consultas específicas sobre los trabajos. lse posgrados reconoció esta necesidad y propuso usar la clase de "aspectos éticos" como una sesión de revisión para la próxima reunión, invitando a los estudiantes a presentar sus casos, incluyendo el "canvas" y la visualización (03:04:11).

Ajuste del Formato de las Clases Futuras: Shimon Ben apoyó la sugerencia de Marcelo Luna, proponiendo acortar la parte teórica de las clases y usar media hora al final para preguntas puntuales de los trabajos. lse posgrados estuvo de acuerdo con la propuesta, señalando que la próxima clase incluirá una introducción muy breve y más tiempo para revisar casos individuales, ya que gran parte del trabajo (aproximadamente el 80%) ya fue desarrollado en la materia anterior. Se concluyó que el mayor valor se aportará en la revisión uno a uno, y se informó que responderán a los correos electrónicos sobre los temas discutidos la semana siguiente (03:05:44).

Revisa las notas de Gemini para asegurarte de que sean precisas. Obtén sugerencias y descubre cómo Gemini toma notas

Cómo es la calidad de estas notas específicas? Responde una breve encuesta para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.

📖 Transcripción

6 may 2026

Taller de trabajo final (2/8) - d015b25 - Transcripción

00:00:00

lse posgrados: Hola, Gabi, ¿cómo andas?
Gabi Tallarico: ¿Qué tal?
lse posgrados: ¿Qué tal?
Gabi Tallarico: Tardes. ¿Cómo va todo?
lse posgrados: Bien,
Gabi Tallarico: Acabo de ver tus email,
lse posgrados: che.
Gabi Tallarico: pero no los abrí todavía, así que mil gracias. Y sí, corro todo el día, así que gracias que
lse posgrados: Me imagino.
Gabi Tallarico: llego.
lse posgrados: Sí, nosotros, bueno, yo también estamos todos igual. El año ya se pasó, ¿viste? Nosotros estamos ya casi a mitad de año y nada, las cosas por hacer.
Gabi Tallarico: Vos, Cristian, Cristian, ¿dónde trabajas? Además de, bueno, de la universidad, obviamente, pero ¿qué es una empresa?
lse posgrados: Sí, yo trabajo en una empresa que se llama Ganfen. Ganfen es una empresa de litio.
Gabi Tallarico: Ah, mira. ¿Y dónde estás
lse posgrados: Yo estoy físicamente en Salta,
Gabi Tallarico: físicamente?
lse posgrados: ¿eh? Y bueno, nuestros proyectos de litio están en Juju y en Salta.
Gabi Tallarico: Voy a ir a mandar a hablar con mis compañeros que son unos capos para que

00:03:13

lse posgrados: ¿Qué haces, Simón?
Gabi Tallarico: vayan.
Shimon Ben: Buena, ¿cómo va? ¿Todo
lse posgrados: Bien,
Shimon Ben: bien?
lse posgrados: bien. Ahí, ahí vi estaba muy hoy estuve muy a 1000.
Gabi Tallarico: Đây.
lse posgrados: Vi tu correíto, Simón, pero te lo respondo capaz cuando termine la
Shimon Ben: Okay, tranqu.
lse posgrados: clase,
Shimon Ben: Este es un momento off ahora, así que
lse posgrados: pero en general casi todos los que enviaron deben ser 10 aproximadamente los que enviaron bastante bastante bien.
Shimon Ben: hm
lse posgrados: Yo por ahí veo y ustedes van a notar que yo por ahí los bajo o como que quiero que hagan algo más
Shimon Ben: M.
lse posgrados: chiquitito, ¿viste? Es como que de yo soy ingeniero, ¿viste? Entonces, no sé, tenemos un sesgo profesional que es tratar de de de hacerlo como que reducir a la mínima expresión algo y después ir escalándolo y yo y lo aplica para todo, digamos, que lo van a lo van
Shimon Ben: Claro, yo estoy como de una vereda muy lejana porque bueno, eh acá todos vienen de algún lugar de de conocimiento más duro. Entonces este como que le pida yo tampoco, no sé, no no manejo, digamos, eh, con tanta fluidez muchas cosas, así que bueno, nada,

00:04:34

Gabi Tallarico: Y Simón, ¿qué estudiaste?
Shimon Ben: para que se ha aprendido todo,
Gabi Tallarico: ¿Qué es tu
lse posgrados: músico,
Gabi Tallarico: profesión?
lse posgrados: creo que es mono o algo o no.
Shimon Ben: ¿no? Profesiono, a ver, siempre trabajé eh en empresas de servicios, trabajé en un hospital 18 años y estudié licenciatura en artes electrónicas. La idea era empezar a a empezar a hacer un trabajo calificado y bueno, qué s cruzar un poco la vereda. A ver, estoy desocupado hace un año y medio estudiando varias diplomaturas en simultáneo, así que por eso también un poco la piña que me estoy comiendo.
Gabi Tallarico: No se nota,
lse posgrados: Pero en las cosas que me mand No te veo,
Gabi Tallarico: eh.
lse posgrados: no te veo. o mal, digamos, ¿no? O sea, está como cualquier persona que está iniciando,
Shimon Ben: No, pero me Bueno,
lse posgrados: eh,
Shimon Ben: pero duele y grande
lse posgrados: pero no, pero hoy pero hoy en día, digamos,
Shimon Ben: aparte.
lse posgrados: iniciar la curva es más rápida, ¿viste? también capaz que genera ansiedad y de hecho decir, "No sé lo que estoy haciendo." Pero en el fondo sí sabes lo que estás haciendo,

00:05:32

lse posgrados: nada más que por ahí lo que no conocé es esta línea de código que hace, pero en el fondo sí sabés, digamos, lo que lo que está pasando en tu código. Sí, digo, no te tiré abajo. Creo que no no está mal, boludo. Está bastante bien.
Shimon Ben: No, no, no. Está bien, pero qué sé yo,
lse posgrados: Estaba
Shimon Ben: es la manera de encararlo también, ¿viste? Este, bueno, qué sé yo, no sé, ahora quiero tampoco quiero monopolizar un poco porque todos ya empiezan a caer y me parece que querrán hacer preguntas, pero bueno, nada,
lse posgrados: ahí.
Shimon Ben: eh le estoy soy lo que sí tengo mucha constancia y hasta que no
Marcelo Luna: Ay!
Shimon Ben: sale no sé, le meto
Gabi Tallarico: Tenemos que copiar.
Shimon Ben: que no es lo mismo que los 20,
lse posgrados: Santi,
Shimon Ben: ¿viste? Ahora cuesta.
Santiago Germino: Buenas noches.
Gabi Tallarico: Entonces,
Santiago Germino: ¿Cómo andan?
Shimon Ben: Buenas.
lse posgrados: ¿qué
Santiago Germino: ¿Qué tal?
lse posgrados: haces?
Santiago Germino: Eh, quería hacerles una consulta. Yo estuve, vengo del infierno, o sea, estuve dos tres semanas de locos mudándome y no sé el que se mudó hace poco, hace mucho, sabe que es es un infierno, eh, más que yo estaba solo con un par de perritos,

00:06:42

Santiago Germino: así que bueno, imagínense desmontar una casa y montarla de vuelta en otro lado, este, con todo el tema. Bueno, yo avisé a los profes que no iba a poder cumplir con la fecha de entrega, que fue el viernes pasado, si no me equivoco.
lse posgrados: Pero, pero, perdona, corto, te corto, Santi. Yo dejé claro en la clase que son entregas opcionales para que tengan feedback y vayan mejorando.
Santiago Germino: Eh,
lse posgrados: no aportan. La entrega que importa la última es son dos documentos y la
Marcelo Luna: Listo.
lse posgrados: presentación.
Santiago Germino: claro, claro. Yo me refiero a la otra materia, la materia anterior.
lse posgrados: Ah.
Santiago Germino: Mi consulta iba dirigida a lo siguiente, más allá de mi situación, que bueno, no importa, eh, ¿qué hago? O sea, curso esta materia, no la curso. Pues ya estamos en la segunda clase y no tendría, no sé, no sé si no tengo problema. Lo voy a hacer en cuanto pueda. El juego recién hoy a las 12 del mediodía pude poner la computadora de escritorio, que es la que necesito para poder trabajar en el
lse posgrados: Mira, usualmente creo que es una pregunta para gestión académica,

00:07:37

Santiago Germino: trabajo.
lse posgrados: yo no la puedo responder, pero usualmente los profes tenemos eh digamos desde que termina un unos plazos para mandar las notas, ¿viste? Eh, si todavía está en plazo y el profe no mandó nota y podés mandar tu,
Santiago Germino: Claro.
lse posgrados: digamos, los criterios de aprobación de la materia anterior, yo creo que no habría inconveniente. Igual cuando hay casos excepcionales como el tuyo, eh, usualmente gestión académica lo toma en cuenta, así que yo diría que te comuniques con gestión académica y gestión académica te va a responder. Si quieres copiarme y yo yo presiono un poquito ahí para que te respondan rápido, pero pero ya estás acá, yo diría que sí. Y digamos, si ya tenés algo armado de la materia anterior,
Santiago Germino: Sí, sí, sí, tengo, tengo. Lo que pasa es que no pude,
lse posgrados: mandalo.
Santiago Germino: me tuve quear la compu y estuve de acá para allá. de vuelta es mi situación personal, ¿no? No es una justificación, pero pero solamente me estaba preguntando, bueno, ¿qué hago? ¿Qué hago acá? No s, ¿sigo, no sigo?
lse posgrados: Seguía, amigo.

00:08:41

lse posgrados: Está bueno.
Santiago Germino: Gracias.
lse posgrados: A ver. Bueno, ya Sony a la E5 yo suelo empezar, como les dije en la planificación, esponer esto acá. Eh, hoy vamos a ver como el segundo pasito. El primer paso fue eh conocer los problemas y tratar de dimensionar y ajustar el el trabajo. Sí, casi todo lo la mayoría capaz que me lo mandó. A todos les respondí o a la mayoría, creo que Shimón y una persona más que mandó hace rato no respondí, pero a los demás casi todos están todos bastante alineado. Yo he ido dando feedback desde mi punto de vista, quizá achicando un poco la Ahí están viéndolo, ¿no? Sí, creo que sí, achicando un poco los alcances y tratando de definir un poquito, acotando algunas cosas, como lo hemos visto en vivo en la clase anterior. Y hoy, eh, ¿cuántos conectados hay? A ver, ya somos nueve. Bueno, esperemos un rato más, mientras hago una intro. Eh,
Marcelo Luna: Sí.
lse posgrados: hoy lo que vamos a ver es un poco de exploración y análisis de datos y visualización. Eh, preparé una una presentación y una notebook.

00:10:00

lse posgrados: y la notebook. Eh, aprovecho y se las dejo ahora mismo en el Así mientras van viendo pueden ir eh pueden ir tocando ahí. Se las dejo ahí en la carpeta compartida que tenemos de material de clases. La estoy subiendo ahora mismo. Se subió. son dos notebooks, pero están explicadas más en la PPT y me gustaría tener más que la intervención del código, la interpretación de para qué usamos tal o cual gráfico. Sí. Eh, seguimos siendo, bueno, somos 10, faltan bastante todavía, pero alarguemos. Bueno, eh presentación. Bueno, la clase de hoy es exploración y análisis de datos y visualización. Vamos a ver algunas reglitas de visualización. E y acabo de subir al al disco la perdón, al disco, escúchame, al driver la la notebook. Eh, vamos a ver el análisis exploratorio, unas reglas de visualización y al final vamos a ver casos con con sus proyectos. Algunos les pedí que tengan las notebook de sus proyectos abiertas para ver en algún espacio de la clase al final eh cómo implementar esto. Sí. Eh, la agenda para hoy un poquito de Era de Era lo que vamos a ver básicamente. Ahí paso el link de nuevo.

00:11:39

Marcelo Luna: Ah, no, gracias.
lse posgrados: Marco
Marcelo Luna: No lo encuentro, por eso lo
Shimon Ben: Es poco.
Marcelo Luna: ve
lse posgrados: ahí está. Y encima está mal porque viste que suele suelen estar en la Yisell ya, pero no lo cambiaron.
Marcelo Luna: en la planilla.
lse posgrados: Sí,
Marcelo Luna: Está mal a la primer materia.
lse posgrados: la planilla te manda otro, pero ahí te lo Sí,
Marcelo Luna: Sí.
lse posgrados: ahí te lo mandé algunas reglas
Marcelo Luna: Ah, bueno, gracias.
lse posgrados: que, a ver, las reglas medio que las definí yo y también forma parte de algunas bibliografía, pero ahí a mí es lo que a mí cuando tengo que hacer análisis de datos lo que me sirve para organizar la forma en la que comunico las cosas, digamos, ¿no? un ejemplo práctico porque bueno, por ahí las reglas visualización son difíciles de aplicar cuando trabajas con procesamiento lenguaje natural o con texto. Vamos a ver qué se puede sacar. Hay hay algunos ejemplos, algunos seguramente ya se está imaginando cómo visualizar datos, digamos, no estructurado, pero lo vamos a ver en tiene que ver básicamente con conteens y algunas cosas en en un caso, en un bolet en un boletín oficial que esta es una segunda notebook que voy a compartir.

00:12:51

lse posgrados: Y por último, que lo apliquemos eh, o tener una sesión así one to one como hicimos la otra vez en la clase anterior, donde yo les pueda ir dando alguna idea y ustedes pueden ir ejecutando. También es importante que hoy en día, digamos, está tendrían que fijarse más en el sentido de lo que quieren comunicar con el gráfico y en cómo preguntárselo, digamos, algún motor de eh de IA, semine, etcétera, más que en el propio código y también, obviamente, a tratar de que que cuando te lo generen al código para hacer la visualización que sea algo escalable o que sea simple, que No, que no por hacer un gráfico genere muchas líneas, que hay hay formas. Eso lo vamos a ver ahora. ¿Alguno ya ha hecho visualización de datos eh algún curso, alguna alguna
Gabi Tallarico: Yo bastante,
lse posgrados: materia?
Gabi Tallarico: pero con no no no programado,
Marcelo Luna: E
Gabi Tallarico: sino con herramientas, qué sé yo, con flores, con locker, con Power B.
lse posgrados: Ah, power. Y con R, ¿alguno maneja R o no?
Gabi Tallarico: Sí,
lse posgrados: R por ahí es bastante lindo para usar en en
Gabi Tallarico: hice un hice un curso, me encantó.

00:14:09

lse posgrados: eso
Gabi Tallarico: Hice un par de cosas y después pasaron 3 años y no lo toqué nunca más, así que creo que no sé nada.
lse posgrados: la lógica. La vamos a ver. Eh,
Gabi Tallarico: Pero sí me había gustado.
lse posgrados: alguien más,
Gabi Tallarico: Toma.
lse posgrados: alguien más maneja R o manejó en algún momento R.
Shimon Ben: No.
lse posgrados: Okay, son todos son todos schol Python,
Gabi Tallarico: Bueno,
lse posgrados: entonces.
Marcelo Luna: No.
lse posgrados: Perfecto. Bueno, eh vamos a ver un poquitito de teoría nada más en de alguna forma como como todo en análisis de dato, en ciencia de dato, en en en inteligencia artificial, es necesario estructurar o hacer un caminito, por así decirlo, para eh para un proceso. Y el edad tiene también su proceso. El primer la primer parte del proceso, obviamente la carga de los datos. Eso ya lo lo saben. El segundo paso es explorar qué estructura tiene. Cuando me refiero a estructura, me refiero a cuántas columnas, cuántas filas tiene, eh qué tipo de variables son. Lo vamos a ver en la slide siguiente también.

00:15:21

lse posgrados: Eh, identificar si hay problema en esos datos. O sea,
Marcelo Luna: Go!
lse posgrados: a más de uno le ha pasado seguro en tener valores nulos. Cuando uno por ahí trabaja con con las notebook, de hecho la que yo les pasé no tiene mucho de solución de problemas cuando tenés datos, pero hay un hay todo una digamos un una rama de la ciencia de datos o del del análisis de datos que es el data granglying, ¿no? O sea, es arreglar los datos. Si cuando te faltan datos y tenés datos como, no sé, haces imputación de datos, mejoras, no perdés tantos datos cuando empezas a eliminar columnas o filas, hay toda una estrategia ahí. Eso es, hay libros completos, de hecho por ahí debo tener alguno Data Granglin con Python. E bueno, una vez que tenemos hecho eso, sí hay que hacer una exploración viendo la las relaciones que tienen las variables. Lo principal que tien creo que tienen que que entender. Para poder comprender eh y explorar un dataset o los datos que tienen, lo primero es entender que nosotros buscamos relaciones para generar eh insight, digamos, eh hallazgos. Sí. Eh, las relaciones pueden ser entre varias variables, pero también hay relaciones de la variable consigo misma, cómo se cómo se distribuye, digamos, eh la la propia variable.

00:16:43

lse posgrados: Y ahí les consulto, ¿se acuerdan? Seguramente vieron en en las primeras fases de Diplo, ¿qué tipo de variables existen en los dataset? Variables continuas, categóricas. ¿Se acuerdan de eso?
Shimon Ben: La del objetivo.
Marcelo Luna: Sí.
Shimon Ben: Sí.
lse posgrados: Ah, claro. Eh, bueno, eh, yo creo que lo importante es y creo que no sé si yo creo creo que es mi primera percepción es que hay en en los proyectos que he visto o los notebooks que he visto, hay como como que no hemos salteado ese paso, ¿no? O sea, si tenemos un PDF, hablo de de porque casi todos están trabajando con con procesamiento de lenguaje natural. teníamos un PDF, lo hemos lo hemos pasado a texto con alguna herramienta de Python y hemos dicho, "Bueno, eh, empecemos a hacer un rack, pero por ejemplo, ¿no?" Y ahí me gustaría que sean sinceros, si alguno ha hecho decir, bueno, cuando hago la los chan, si cuando separo, si han explorado distintas cantidades de caracteres o token por chunk y se han explorado también en en cambiar el overlap y se han documentado cambiando el overlap o la cantidad o el tamaño del chango.

00:18:09

lse posgrados: Básicamente se han tenido resultados diferentes. Acá los
Marcelo Luna: Yo eh eh yo hablo en mi caso en particular,
lse posgrados: escucho.
Marcelo Luna: la verdad que no hice mucho de todo ese ejercicio. De hecho, ni siquiera aproveché el uso de expresiones regulares para hacer el el eh eh la ingesta de los PDF. Eh, tampoco tuvimos mucho tiempo, digo, puedo hablar mi caso, no,
lse posgrados: Claro,
Marcelo Luna: más que tiempo no tuvimos demasiado espacio de discusión de las ideas como para que alguien nos sugiriera y nos dijera, "No, mira,
lse posgrados: claro.
Marcelo Luna: explorarlo por este lado." O sea, fue, "Toma, tienen que hacer esto y salir corriendo a hacer algo." Pero
lse posgrados: Sí. Bueno, yo vengo un poquito a yo vengo un poquito a traer orden,
Marcelo Luna: bueno,
lse posgrados: digamos, ¿no? O sea,
Marcelo Luna: ¿qué dice?
lse posgrados: por más que yo sea la respuesta,
Marcelo Luna: No,
lse posgrados: eh,
Marcelo Luna: está bueno.
lse posgrados: sí, voy a tratar intentar de traer un poquito de orden, pero eh por ejemplo,
Marcelo Luna: Hm.
lse posgrados: si yo tengo eh un dataset y o perdón, bueno, la mayor tienen documento, pero mi visión de nuevo, mi visión como como ingeniero me lleva a que ese documento, ese bloque de texto tiene que estar en una tabla, digamos.

00:19:27

lse posgrados: Porque los datos se comunican con tablas,
Marcelo Luna: Sí.
lse posgrados: ¿sí? Entonces, no. Entonces, digamos, lo primero que haría yo así digamos por por mi sesgos profesional es tengo un texto y tengo que llevarlo a tabla. ¿Cómo lo divido? Porque cada parte de la división va a ser una fila, ¿cierto? Y qué información le puedo sacar a cada a cada pedazo de texto que me genere números para que después pueda graficar esos números. La más simple de todas es cuántas palabras tiene ese fragmento.
Marcelo Luna: Hm.
lse posgrados: Esa es la más simple de todas, digamos, ¿no? Eh, en problema, vamos a verlo más adelante, pero me adelanto un poquito. En problema de de clasificación de documentos o entidades, bueno, todas las entidades, digamos, que están reconocidas tienen la misma cantidad de caracteres. Bueno, obviamente no. ¿Cómo se distribuye eso? Entonces, bueno, todas esas preguntas vamos a intentar explorarlas para para generar. Entonces, antes de crear un rag, un modelo, etcétera, hay que mirar qué datos tengo. Y ese es otro sesgo que he visto en los proyectos, que hay muchos que directamente entran los datos y ya empiezan a dividir chan y no hay poco print básicamente.

00:20:35

lse posgrados: Entonces, una cosa que que aprendí yo con el tiempo es cada paso un print, cada paso un print, cada paso un print porque quiero ir viendo qué hace la función más aún cuando tenés la guía que te está generando las funciones, digamos, ¿no? Entonces cada paso que hago, hago un print y veo que me da, me da una lista, me da una tabla, me da un diccionario o qué estructura me da. Bueno, mirar antes del de modelar, si hay que documentar cada hallazgo porque en la exploración pasa que uno empieza a tirar datos, cruzar variables, etcétera, y no la documentas. Entonces, si este hallazgo no lo documenté, no lo escribí, no lo no. Bueno, cadago que tengo lo documento porque después va a servir para el modelado. Obviamente eh hay que cuestionar todo. Sí. Si hay dos variables que aparentemente no están correlacionadas, no están asociadas, las pruebo igual. Vos decí, "Bueno, no sé qué tiene que ver, no sé, eh, la cantidad de incendios por años con la tasa de nacimiento, la exploro. Exploremos." eh no digamos para eso está en la exploración y esto nos va a permitir digamos eh un punto cero.

00:21:45

lse posgrados: O sea, una vez que tenemos esto ya eh digamos limpio el dataset y con las columnas y la y conocidas las relaciones, nos va a permitir incluso eh hacer cosas sin sin tener que tokenizarlas con LLMs, digamos. O sea, yo hoy en día y tengo mi visión particular sobre el LM, hay que aprovecharlo porque están prácticamente gratis o baratos, pero en algún momento va a haber una corrección. Cuando no empiecen a cobrar mal los tokens, que de hecho ya lo están haciendo, eh ya no va a ser tan sencillo. Entonces, lo que puedo amatar con heurística, heurística se llama con relaciones simples, lo hago así. Por ejemplo, si yo tengo que clasificar pedazo de texto o en emociones, por si un bloque me dice ira, otro bloque me dice alegría, quizá el que está enojado tira más palabra en su comentario. Entonces, quizá el número de palabras por comentario es suficiente para clasificar la emoción y no tengo que meter un Llm o un Transformer para que lo interprete. Es una regla más fácil. Entonces, ese tipo de cosas lo que lo que vamos a intentar hacer. A ver, y capaz que lo probamos y no y no hay relación también, esa es otra posibilidad. Bueno, la la primera el primer acercamiento es que hay que tener claro los tipos de variables, ¿sí?

00:23:03

lse posgrados: Eh, porque por cada tipo de variable, según sea el tipo de variable, van a venir los tipos de gráfico. ¿Sí? Entonces, una variable numérica continua, ¿sí?, o sea, con con separador decimal, básicamente. Eh, tiene sus tipos de su tipo de gráfico. Entonces, y acá tienen que pensar en los gráficos como graficar la variable en sí misma, o sea, ella misma, sin ninguna otra variable, y cruzar esa variable. Por ejemplo, puedo cruzar la variable con eh sorry, puedo cruzar la variable con eh una numérica discreta, con una categórica, ¿sí? Con una categórica ordinal o con una categórica nominal. Puedo hacer, si es categórica nominal, puedo hacer hacia sí misma con conteos o puedo relacionar conteos para ver si hay tablas cruzada, si hay relación entre categóricas también y así sucesivamente. O sea, acá el objetivo es paso uno, mirar la variable hacia sí misma. Esa es la primera, ¿cómo se distribuye? ¿Cuál cuál cuál es la el su rango de distribución? ¿Qué? Por ejemplo, un rango de distribución en una variable numérica eh va a ser un mínimo y un máximo.

00:24:22

lse posgrados: ¿Sí? Y un rango de distribución en una variable categórica o numérica o perdón, categórica nominal. ¿Cuál será el rango? Les consulto. Supongamos que tenemos los meses del año. ¿Cuál es el rango de esa variable categórica nominal? Tiren, tiren, chicos. Necesitamos para compartir
Marcelo Luna: La es categórica nominal.
lse posgrados: categórica nominal, por ejemplo,
Marcelo Luna: dijiste tamaño tamaño del
lse posgrados: los meses del año, enero, febrero, marzo, abril,
Marcelo Luna: conjunto rango.
lse posgrados: el tamaño de de los valores únicos, ¿no es cierto?
Marcelo Luna: Claro.
lse posgrados: Sí. O sea,
Marcelo Luna: Sí.
lse posgrados: sería 12, o sea,
Marcelo Luna: La cantidad de elementos en el conjunto,
lse posgrados: 12 valores.
Marcelo Luna: básicamente.
lse posgrados: Claro,
Marcelo Luna: Sí.
lse posgrados: no, no, no, a la cantidad de elementos en el conjunto, sí,
Marcelo Luna: Sí,
lse posgrados: digamos, o sea,
Marcelo Luna: claro.
lse posgrados: los valores únicos. O sea, por ejemplo, yo tenga, si yo tengo un dataset que tiene una columna con tres con 3000 filas,

00:25:23

Marcelo Luna: Salto.
lse posgrados: pero las filas solamente pueden tomar valores enero, febrero, marzo, abril, hasta diciembre. Entonces,
Marcelo Luna: Son 12.
lse posgrados: entonces esa variable se va a distribuir desde enero hasta diciembre, no hay otro mes más,
Marcelo Luna: Correcto.
lse posgrados: ¿cierto? Entonces, digamos, esto es importante que lo vayan conociendo porque cuando porque es sumamente útil cuando yo
Marcelo Luna: Exacto.
lse posgrados: quiero relacionar variables, digamos, ¿no? Y ahora lo vamos a ver con ejemplos visuales, pero por lo general vamos a tratar primero de mirar la variable hacia sí misma y la variable luego la variable relaciona a otras variables. Ahora, usando el ejemplo de categórica nominal con los meses del año, ¿cómo cómo ustedes cómo ustedes inspeccionarían su distribución? No hay muchas maneras de realidad, digamos. Hay medio que hay solamente casi que una. Lo más fácil es hacer conteos. Entonces, lo primero que lo primero que viene a la mente es cuando tengo una categórica conteos. Es decir, ¿cuántas veces viene enero, cuántas veces viene febrero, cuántas veces viene marzo, por ejemplo. Sí, ahora lo vamos ver en ejemplo.

00:26:42

lse posgrados: Bueno, entonces teniendo acá les pegué un un dataset
Marcelo Luna: Vale.
lse posgrados: de de ejemplo, ¿sí? Entonces, acá, por ejemplo, la primera ID del viaje, ¿de qué tipo de variable es esta columna? Lo escucho, chicos. Acá tengo este que está acá. Listo. ID del viaje.
Marcelo Luna: Parece categórica o no.
lse posgrados: Sí, categórica. Vamos. Así firme. Es categórica.
Marcelo Luna: Ah,
lse posgrados: Un pedazo de texto.
Marcelo Luna: sí.
lse posgrados: Es categórica. Perfecto. Ahora fecha de salida. Esto que está acá quiero hacer con el puntero. No lo encuentro en esta cosita.
Gabi Tallarico: La fecha es continua.
lse posgrados: fecha de salida de tipo date. Fecha un tipo es un tipo de variable,
Gabi Tallarico: Ah.
lse posgrados: digamos, que que se puede transformar en otras variables, pero es tipo date, digamos, es una fecha tipo de serie de tiempo de tipo fecha.
Gabi Tallarico: Mhm.
lse posgrados: Ahora, si yo inspecciono y a 2026 la saco, va a ser categ va a ser eh numérica ordinal, ¿no es cierto?

00:28:16

lse posgrados: lo mismo con los meses del año. Entonces, una una cosa importante que tienen que saber es que si ustedes tienen en su en sus datas o en sus textos tienen fechas, la fecha es una es una variable tipo date y las variables tipo date las podés convertir, o sea, le puedes sacar mucha información, le puedes sacar el año, el mes y el día para empezar, digamos, ¿no? También le puedes sacar qué día de la semana es, no es lo mismo que sea lunes, martes o miércoles. Sí, le puedes sacar el día juliano también que se llama el día juliano digamos empieza el uno, empieza el primero de enero y el 365 el 31 de diciembre. Entonces a esa a esa variable la podéis ir como le podéis ir sacando más info, básicamente. Eh, prioridad, esta variable prioridad también categórica. Bueno, las numéricas, tenemos numéricas que toman valores enteros, ¿sí? Por ejemplo, eh la cantidad de paquetes entregados uno no entrega 1,5 paquetes, entregó 16 paquetes. La distancia desde el centro de distribución, esta sí es numérica continua porque básicamente tiene decimales y puede tomar cualquier valor entre medio de dos enteros. Eh, consumo de combustible también.

00:29:29

lse posgrados: Las coordenadas de destino son otro tipo de variable, pero está compuesta por dos números. Sí. Eh, y después, bueno, comentario del chóer acá donde por ahí entramos nosotros. donde acá va más de tipo de tipo texto. Es un perno esto, chicos. Yo sé que es un bodrio entenderlo,
Gabi Tallarico: Sí.
lse posgrados: pero créame que ahora cuando veamos los gráficos va a ayudar. Bueno, hay un montón de libros y cuando termine la clase e se los les paso algunos, ¿sí? Porque pero ahí de esto hay para ser dulce, digamos, ¿no? En lo que es territoring con datos. Eh, y hay hay casi todos los libros apuntan a los mismos, digamos, ¿no? Cuando cuando uno hace un gráfico, eh, digamos que en en el análisis de datos puntualmente, más que en la inteligencia artificial, en el análisis de datos, la última fase es comunicar los insight. ¿Y cómo lo comunicamos? Depende sobre todo de a quién le estamos comunicando, ¿sí? Y también qué es lo que queremos comunicar. Lo vamos lo vamos a ver ahora en en cosa. Eh, muchas veces a mí me toca revisar informes y en los informes ponen tablas y por ahí la tabla comunica,

00:30:44

Marcelo Luna: Ô
lse posgrados: pero no tanto, ¿no? O sea, por ahí un gráfico comunica mucho más que una tabla y depende también, ¿no? Pero creo que que hace falta mirar un poco hacia adentro y decir, bueno, esto que este fenómeno que descubrí, cómo lo quiero comunicar, porque la audiencia, dependiendo de la audiencia, voy a usar tal o cual regla, digamos. Y básicamente lo que voy a mostrar son ocho reglas que son útiles y que espero que la que las puedan aplicar en sus en sus TPS. E acá hay un resumen de lo que espero que que que veamos, digamos, ¿no? Cuando como cuando yo le decía, bueno, cuando primero veo una una situación, si tengo una variable numérica o quiero explorar una variable numérica, ¿qué gráfico uso? Un histograma. Si tengo una variable categórica, bueno, barras. Si tengo numérica por numérica, un scatterplot. Ya vamos ver lo que si queo numérica por una categórica, puedo usar un box plot o un strip plot. Si tengo categóricas por categóricas, o sea, dos categóricas, puedo usar un hitmat de conteos y así por cada una, digamos, de las combinaciones eh hay algún tipo de gráfico que sirve.

00:32:08

lse posgrados: Y acá eh voy a hacer uso de un recurso. ¿Conoces lo que son los cheat? Los chits son como machetes. Eh, y acá veamos si hay un chit de los cheat de esto también se lo voy a dejar. A ver, los chips son machetes que nos ayudan a decir, bueno, para gráficos tal, ¿cuál es el código? ¿Cómo uso el el digamos cuál es la la función que debería usar? Y están disponibles en todo internet. Entonces, le voy a dejar algunos cheatsit con en el recreo para que para que tengan para que tengan a mano. Hay uno muy bueno que bueno, cuando yo estudiaba R, eh hay una librería en R que se llama G Plot y ese y ese chit de R viene bastante bien. Lo estoy abriendo porque también tiene una página. Sorry que interrumpí acá, pero me acordé de esto. Esta página que que voy a mostrar acá viene tiene los tipos de gráfico. Entonces, dependiendo de lo que uno quiere comunicar viene y acá tiene los tipos de gráficos y tiene vien por lo general viene acompañado de su base en código, digamos, y con ejemplos. Esto también se los voy a poner para que lo lo vean porque a mí me sirvió un montón cuando estaba cuando estaba viendo estos tipo de visualizaciones.

00:33:59

Gabi Tallarico: Cristian, ¿puedo puedo pedirte un paso atrás para hacer una pregunta?
lse posgrados: Sí, sí,
Gabi Tallarico: Eh, sí,
lse posgrados: acá.
Gabi Tallarico: no sé si en los qué slide, pero como que marcaste muy bien de que teníamos que considerar todo esto para los trabajos, ¿no? Y y cuando hicimos la materia, nada de de esto de análisis de datos, eh como que yo tenía dos mundos por separado hasta ahora que vos lo decís que deben ir juntos, ¿no? ¿Cómo sería para un proyecto de lenguaje natural? incluir todo esto. ¿Qué es lo que me está faltando para mezclar esas dos?
lse posgrados: Esa es la segunda parte de la clase, pero te lo respondo así rapidito.
Gabi Tallarico: Ah, bien.
lse posgrados: Mira, por ejemplo,
Gabi Tallarico: Adelante.
lse posgrados: acá corta, digamos, por ejemplo, si vos tenés un PDF, este es un gráfico de visualización donde vos contás la cantidad de caracteres que tenés
Gabi Tallarico: Mm.
lse posgrados: por página del PDF. Entonces, ¿y esto para qué es útil? Por ejemplo, si vos has aplicado una limpieza, lo ponente que los documentos tengan un encabezado, eh, vos sabés que el encabezado por lo general son x cantidad de caracteres,

00:35:04

Gabi Tallarico: Sí.
lse posgrados: no sé, 100 caracteres. Vos antes y después de la limpieza, eh, digamos, debería tener la no deberías perder contenido semántico ni léxico. ¿Por qué? Porque si de repente tu herramienta de limpieza te saca partes del del del texto de que vos querés después recuperar un retriival, estás perdiendo información, ¿o no? Entonces este gráfico sencillo de barras donde vos contás los caracteres antes de la limpieza
Gabi Tallarico: Ah.
lse posgrados: y después de la limpieza te solucionó. Porque si, por ejemplo, acá si vos ves eh que la barra verde, perdón, voy a presentar a ver si se ve más grande. Si vos ves que la barra verde, que es el dataset limpio, está muy por debajo de la barra con el con el dato crudo, o sea, con la página cruda sin limpieza, significa que que estás perdiendo información, digamos, ¿no? Porque uno cuando opera y cuando cuando hace escala los proyectos tiene una función de limpieza, la pasa todas las páginas del documento o a todos los PDF y podés perder. Y lo mismo este gráfico que está acá al costado te va diciendo cuántos caracteres fueron eliminados por página. Obviamente si vos tenés que tú encabezado tienes siempre 100 caracteres, esto debería venir así.

00:36:24

lse posgrados: Si de repente en algún documento eliminó menos caracteres, bueno,
Gabi Tallarico: Baja.
lse posgrados: algo pasó en ese documento. Si eliminó más caracteres, algo pasó en ese documento. Ese es uno de todos los ejemplos que preparé. preparé muchísimo ejemplo no viene super bien
Gabi Tallarico: Bien. Bueno, disculpa que dice cambiar
lse posgrados: la pregunta a más me gusta que participe porque eh digamos este es el momento para para poner cosas sobre la mesa, digamos. Bueno, pero en definitiva eh siempre vamos a tener vamos a a intentar ir hacia esto que es un bodrio, lo sé, pero es un machete que les va a servir, digamos. Bueno, entonces empezamos con la con la primer el primer tipo de de variable, ¿sí? Vamos a ir con una variable numérica. Sí, la variable numérica y acá volvemos a estadística, la podé explorar hacia sí mismo, digamos, hacia sí misma, haciendo histograma. ¿Quién no sabe qué es un histograma? Y se lo explico en dos pasos. Todos saben lo que es un histograma. Bueno, ¿qué desventaja tiene el histograma? En alguna parte de la slide ya está, pero qué no sé si la puse, capaz que sí, pero ¿qué desventaja tiene el histograma?

00:37:54

lse posgrados: Que hay una variable dentro del histograma que que no nos permite ser del todo objetivos, digamos. En el histograma yo lo que hago es tengo una una var numérica. en este caso la cuenta total y lo que hago es agrupo y cuento, por ejemplo, entre cuánto cuántas filas tengo en este caso, porque el dataset son conteos. ¿Cuántas filas tengo entre 10 y 15? Por ejemplo, acá entre 10 entre 10 y 15, que este ranguito que está acá. Bueno, está entre 9 y 10. Entre 9 y 10, ¿qué rango tengo? ¿Cuántas filas tengo? 20 filas del dataset. Tengo 20 casos, tengo 20 registros
Gabi Tallarico: Y entonces los que están en entre 40 y 50 son una dispersión que habría que corregir.
lse posgrados: también, pero depende, digamos, lo malo que tienen los histogramas es que depende del tamaño de la caja que vos definís. Si yo de repente defino una caja que está entre 10 y 40, acá voy a tener un voy a contar todos estas filas, todas estas columnas que tengo acá y voy a tener una sola columna.

00:39:04

lse posgrados: Sí. Entonces, el tamaño del bin se le dice al tamaño de la caja. Vos podés los los digamos los histogramas tenés dos formas de hacerlo. Uno con el tamaño del bin, digamos, y otra con la cantidad de bins. O sea, vos puedes decir un bin, decir o el bin decir, bueno, que vaya incrementando en anchos de cinco. Entonces cada empeza de 5 a 10, de 10 a 15, etcétera, etcétera, etcétera. Ahora también lo puedo decir con las cantidades de bins. Yo quiero decir, bueno, 20 bins, esa es la otra forma. Agrupame todo en 20 bins, en 20 columnas. En 20, sí, en 20 columnas. Eh, entonces dependiendo de lo que uno quiere comunicar y cómo lo quiere comunicar, va a variar la cantidad de BS, con lo cual no es tan objetivo, digamos, ¿no? Esa es una de las desventajas. Para eso existe el gráfico de densidad, que explicarlo es un poco complejo, pero básicamente independiente de la cantidad de bins. Y nos muestra cómo se distribuyen las probabilidades de ocurrencia de cada punto de la variable en el tiempo y la forma acumulada de esto da uno.

00:40:19

lse posgrados: Sí. la eh básicamente cuando el área bajo la curva va a dar uno. ¿Y para qué sirven o para qué creen que serviría eh conocer la distribución de una variable cuantitativa hacia sí misma? ¿Qué no qué nos permite esto? Yo necesito hacer gráficos y no tengo cómo pintar la pantallita. Así que voy a improvisar algo acá. Archivo nuevo, ¿eh? Y voy a empezar a garabatear acá. Así lo hacemos más entretenido. Supongamos que yo tengo x e y, ¿sí? Y tengo una variable que se distribuye de esta forma. ¿Sí? y tengo la variable, otra variable que se distribuye de esta forma, ¿sí? Es decir, entre este y este rango de datos tengo muchas muchos casos y
Marcelo Luna: Ok.
lse posgrados: entre este y este dato tengo muchos casos porque acá tengo concentrado mucha cantidad de casos y acá tengo concentrado mucha cantidad de casos. Entonces, evidentemente esta variable que no le hemos puesto un nombre nos permite separar los grupos. Se nos permitiría de alguna manera decir, bueno, acá por acá puede que haya un límite. Entonces, yo usando esta variable podría separar filas del dataset, podía separar casos.

00:41:58

lse posgrados: Hay casos que se comportan así y hay casos que se comportan. Lo podría hacer incluso si se distribuyen así con una regla urística, decir, bueno, si la si la variable está entre este rango, entonces va la categoría varones. Por ejemplo, si el la variable está en en este rango, entonces son mujeres. Y me permitiría separar estos dos casos. Sí, para eso, para eso se usan la la digamos los uno de los casos de los gráficos univariados. Otro de los casos de los gráficos una variados es que si yo tengo una variable XY, la variable puede tener este comportamiento, puede presentar dos picos, dos modas, una moda acá y otra acá. ¿Sí? Entonces, eso se llama una variable bimodal, o sea, la variable no está tiene muchos mucha concentración de casos en este rango y mucha concentración de casos en este rango. También puede servir para separar separar las las filas. Bueno, dudas sobre este tipo de variables también la vamos a ver en en la práctica, pero eh me interesa saber si la han usado, la han visto, nunca lo usaron en la vida. No, nunca nadie. Bueno, es importante, compadre, es importante saber que eh cuando uno hace este tipo de gráfico, acompañar acompañar los datos, acompañar el gráfico, yo les tiro los tips, chicos, que que yo creo que son importantes, ¿no?

00:43:42

lse posgrados: Porque uno podría hacer el gráfico y nada más, pero cuanto uno más cosas le agrega al gráfico, más ayuda a querer comunicarlo alguna situación. Estas dos líneas verticales que se ven acá, uno se las puede agregar y una de la media y otra de la mediana. Esto sirve para que la visión del espectador vaya directamente acá. ¿Sí? Entonces, cuando uno pone este tipo de gráfico, suele acompañar de estas líneas, una de media, otra de mediana o la media, si me interesa el comportamiento. ¿Dónde está dónde está el promedio? Como la variable está muy hacia la izquierda, o sea, hay muchos registros, hay muchísimos registros dentro de este de este rango, eh, obviamente la la media no está cayendo la mitad, digamos, ¿no? La media la digamos yo, diría, bueno, entre el mínimo y el máximo, la mitad está más o menos por acá. Bueno, no está cayendo ahí. Eso también te habla de algún comportamiento de la de la variable. Vamos al siguiente. Dudas sobre este Bueno, cuando tengo variables categóricas, como hemos dicho, por ejemplo, las que teníamos acá, eh entrega exitosa o identificación del viaje o la prioridad o el tipo de camión que hizo la entrega, lo que corresponde hacer para gráficos univariados.

00:45:14

lse posgrados: Es un conteo. Sí, básicamente agarrar a esa columna y contar cuántos registros tengo de cada posibilidad de esa columna. ¿Sí? En este caso acá hay dos ejemplos. Un ejemplo es bueno los días de la semana y cuando hacen cuando uno hace este conteo hay acá hay algunos tips, por ejemplo, si el tamaño y son por ahí por ahí es eh medio llama medio empírico, pero cuando el tamaño del del texto que tengo acá es chiquito, es chico, obviamente el nombre de la variable es chiquita, eh bueno, el vertical comunica y comunica bastante bien, pero si este nombre fuese muy largo, se solaparía con esto. Entonces, la opción para eso es hacerlo de tipo horizontal. Es un truco. Otra forma de hacerlo y que de hecho yo siempre los hago así es e lo voy a lo voy a poner acá así me tomaron. Eh, esa es una sí ponerlo puede estar en el sentido la digamos en el sentido así horizontal o en el sentido vertical. Sí. Otra cosa importante, siempre se suelen eh ordenar de mayor a menor o de menor a mayor. Si se fijan, esto está en este sentido. Por más que eh el sábado esté antes que el viernes, o sea, esté después que el viernes, ¿no?

00:46:51

lse posgrados: ¿Por qué? porque yo ya le estoy dando la idea, le estoy comunicando cuál es el mayor. Entonces es importante que lo tengan en cuenta de que los gráficos de barra desde mi punto de vista tienen que estar sí o sío ordenados para comunicar algo. A menos que vos que tengas una serie de tiempo o querás comunicar algo a lo largo del tiempo y que esta este orden tenga prioridad sobre lo que vos querés comunicar. Bueno, sí, pero si vos querés comunicar con teos, básicamente siempre vamos a buscar de eso. Otra cosa importante, cuando nosotros cuando se hacen los gráficos, esta distancia se suele setear la distancia que hay entre se llama de sticks. En este caso está cada cinco. Usualmente lo hacen automático, pero ustedes la pueden setear. Lo que suele pasar acá es que eh este valor que está acá, si no le ponemos esta etiqueta, no sabemos qué valorear. ¿Sí? Entonces, ese es otro tipo. Este valor que está acá debería estar arriba de la barra. Sí, es es importante es importante que tengan un título. Sí, es importante que tenga un título y que sobre todo cuando no se pueden explicar por sí mismas las variables que tenga un título del eje.

00:48:14

lse posgrados: Muchas veces el eje se explica por sí mismo. En este caso, eh, adjudicación, contratación, sucesorio. son tipos de documentos y en este caso es la cantidad de palabra o cantidad de quizá de chonks que tiene cada uno de estos. Entonces es necesario que se le ponga eh la etiqueta, ¿no? ¿Conocían esto, chicos, o o lo estoy hablando en en chino o algo que ya saben y estoy estoy siendo redundante. A mí esta parte de te juro que de la de la de la de todo lo que es el análisis de datos, la visualización me parece los más lindos para para hacer, digamos. Creo que ahí es donde donde se puede sacar el jugo a los datos como vienen. Cuando veamos la métrica del aplicada a un rckle o aplicada al al texto, a la goletina, creo que le va a hacer más sentido. Bueno, entonces repasamos primera regla, eh una variable numérica hacia sí misma, ¿sí? Histograma. Para eso hay que hacer definir o la cantidad de de barra del histograma o el tamaño que tiene cada barra del histograma. Los conteos, obviamente acá por cada elemento discreto que tenga la columna eh va voy a contar las cantidad de filas.

00:49:34

lse posgrados: Son conteos básicamente. Cuenta cuántas veces se se ve esa variable en el dataset. Esto reemplaza sobre todo a los gráficos de de torta y lo un poquito más adelante. O sea, yo si yo tengo eh a esto lo podría representar proporcionalmente en un gráfico de torta, pero en un gráfico de torta estas diferencias entre 78, 73 y 69 no se notarían tanto por la forma que tiene el gráfico de torta. Eh, cuando bueno, cuando queremos explorar, ahora vamos a la tercer regla. La tercer regla es numérica por numérica. Es decir, acá cada punto representa una fila. Sí, cada punto representa una fila expresadas por dos columnas. Sí, yo prefiero ser redundante y no omitir nada. Sí, si estamos todos de acuerdo, a menos que si alguno siente que esto ya lo vio, etcétera, me avisa, pero yo lo voy a explicar al detalle, así lo lo entienden. Un scatter plot es cuando uno tiene dos variables, ¿sí? Variable uno y variable dos, en este caso, la cuenta total y la propina, ¿sí? Variable uno y variable dos en los ejes. Y cada ocurrencia del punto es la combinación, ¿sí?

00:51:04

lse posgrados: es la combinación de dos variables. Este punto está representado por la variable uno y la variable dos. En este caso, este punto debe ser 43 y acá 43, supongamos, y la propina sería 5,3, no sé, o cinco, casi seis, 5,8. Entonces yo agarro este par de datos y digo, bueno, ¿dónde está variable uno? Listo, va acá. Acá esta variable uno viene acá. ¿Y cuál es la variable dos? Acá 5,8 tiqui tiqui. Entonces cada cu en esto, cada ocurrencia que tengo acá es una combinación de dos variables. ¿Quedó claro? Bien. Bueno, ahora en este caso si analizamos tiene mucho sentido que a medida que aumenta la cuenta, aumenta la propina. Sí, si aumenta la cuenta, aumenta la propina, pero en en este dataset, evidentemente, la propina es opcional, porque si la propina eh no fuese opcional, ¿cómo debería ser? Yo aplico siempre el 10% de la propina, ¿cómo debería ser este dataset? O sea, este gráfico, yo si yo siempre aplico en la misma la misma proporción a la cuenta total,

00:52:30

Shimon Ben: Sería una regresión
Gabi Tallarico: Es super homogénea.
lse posgrados: sería serían una Exacto.
Shimon Ben: lineal.
Marcelo Luna: una recta.
lse posgrados: Si yo siempre aplico el 10%, bueno, el 10% de 10 es 1. El 10% de 2 10% de 20,
Shimon Ben: Dos.
lse posgrados: perdón, es 2.
Shimon Ben: Yeah.
lse posgrados: El 10% de 30 es 3. El 10% de 40 es 4. El 10% de 50 es 5. ¿Sí? Entonces acá yo tendría una fila de puntos para cada valor, si es que fuese como en Argentina que se paga el 10%, como en Chile también. Yo tendría todos los puntos alineados. Okay. Y si están desalineados como están acá, ¿qué qué usted cuál es la interpretación de esto? están desalineados, digamos, ¿no?
Marcelo Luna: Sí, hay un grado de variabilidad o puede encontrar una relación, Pero sí.
lse posgrados: Exacto. Vos dijiste una palabra y la variabilidad. Sí. Entonces, y bueno,
Marcelo Luna: Mhm.

00:53:31

lse posgrados: la variabilidad en dos variables. La variabilidad, ¿cómo se estudia? Para empezar, volvamos a la primer clase capaz de de análisis de datos. ¿Cómo se estudia la variabilidad?
Shimon Ben: compromedios.
lse posgrados: ¿Se acuerdan? Uno tenía medida de tendencia central, el promedio. Sí. ¿Y cómo se desvía cada dato del promedio?
Marcelo Luna: Sí.
lse posgrados: ¿Cómo se llamaba? Tiene era una cosita así o una cosa así y
Shimon Ben: mediana.
lse posgrados: puede estar el cuadrado o no puede estar cuadrado.
Marcelo Luna: Desviación estándar.
lse posgrados: La desviación. Exacto. O digamos la desviación o también se llama SD, ¿no es cierto? Estándar deviation, que es la raíz de esto,
Shimon Ben: He.
lse posgrados: digamos. Bueno, perfecto.
Marcelo Luna: Hm.
lse posgrados: La deviación estándar en este caso de esta variable va a ser, si ya yo tengo todos estos datos de acá, puedo calcular el promedio. Supongo que el promedio me da acá. Este dato, ¿cómo se cómo cómo se aleja de esta media? Este dato, ¿cómo se aleja de esta media?

00:54:33

lse posgrados: Porque la media viene por acá,
Marcelo Luna: Hm.
lse posgrados: ¿sí? De esta variable. Y así para cada uno de los datos. Okay, esa es la media de este dato cuando uno lo mira hacia sí mismo y lo mismo hacia acá. Ahora, cuando vos graficas esto que está acá,
Marcelo Luna: Hm.
lse posgrados: que es una con respecto a la otra, existe cómo varían los dos datos relacionados, digamos, ¿no? Sí, esa covariable que hay, digamos, ¿no? Entonces pueden pasar muchas cosas que estos tenga un rango de este tipo, por ejemplo,
Marcelo Luna: Ok.
lse posgrados: que todo esto concentrado acá. O puede ser que a medida que, como pasa en este caso, que yo más o menos veo, es que a medida que aumenta la cuenta, la variabilidad también aumenta. Sí, eso se llama heterosedacticidad. Es redifícil la palabra un enleve, pero básicamente es a medida que avanza una variable o la otra, cómo se van dispersando los datos y también aporta información porque cuando y de hecho cuando uno hace regresión lineal simple hay una prueba que tenés que evitar, o sea, tenés que saltar una prueba que es la heterosedasticidad.

00:55:46

lse posgrados: Cuando vos tenés heterosedasticidad, esa desviación de las covariables a medida que aumentan, no aplica la regresón lineal simple, el modelo de regreso lineal simple, o sea, no no sirve.
Gabi Tallarico: H
lse posgrados: una prueba que tenés que hacer. La primer prueba es que estas variables se distribuyan normalmente y la segunda prueba es la prueba de esterosedacticidad que en conjunto no se vayan ampliando porque yo el modelo lineal que seguramente lo vieron, el modelo lineal va a buscar representar todo esto con una línea. Entonces, si yo la línea debería ser representativa para todos los puntos, pero si de repente a medida que avanza esta línea, estos que está acá se van dispersando cada vez más y acá tengo más chiquita la dispersión. Bueno, acá tiene un comportamiento la línea y acá tiene otro comportamiento la línea. Entonces, ese modelo lineal no serviría serviría más para acá que está más agrupado que para acá que está más alejado. ¿Sí? Entonces, para eso es importante explorar la combinación de dos variables. Y acá hay un montón para hablar de esta de este tipo de gráfico, porque la medida de asociación lineal que tien se llama coeficiente de regresión. Sí. Entonces, eh esto es cómo se asocian las las variables.

00:57:00

lse posgrados: En este caso da 082, lo cual es una bu digamos hay asociación entre las variables, podría ser esta. Esto significa que esto podría ser predictor de esto. O sea, yo teniendo la cuenta podría decir aproximadamente cuánto va la propina que un problema de machine learning de regresión digamos,
Gabi Tallarico: ¿Y
lse posgrados: ¿no?
Gabi Tallarico: cuál es la diferencia entre este pl con el gráfico de dispersión?
lse posgrados: ¿Con cuál, Gabi? Se te cortó el
Gabi Tallarico: Ah, perdón.
lse posgrados: último.
Gabi Tallarico: gráfico de dispersión son iguales.
lse posgrados: ¿Cuál el gráfico de dispersión y tribución?
Gabi Tallarico: Sí.
lse posgrados: debe ser. ¿Qué decís? Cuando uno hace un gráfico de distribución,
Gabi Tallarico: Ah. Ah, me parece que era
lse posgrados: eh,
Gabi Tallarico: dispersión.
lse posgrados: graficar la dispersión, vos la podés, digamos, graficar hacia sí misma a la dispersión con este gráfico. Sí, porque esto eh imaginemos que miramos
Gabi Tallarico: Ah.
lse posgrados: si a esto uno lo gira, bueno, en este caso no. no funciona, pero tendría que tener todos los datos acá, pero a ver si lo puedo mover a esto.

00:58:16

lse posgrados: Pero si yo miro solamente esta variable, no lo puedo hacer especular a esto porque si no sería espectacular. Si yo miro solamente esta variable así hacia propina, eh lo voy a dibujar de me Si yo miro solamente propina,
Gabi Tallarico: Te daré igual.
lse posgrados: si apate que yo pongo mi punto de vista acá y estoy mirando solamente la propina,
Gabi Tallarico: Sí.
lse posgrados: tengo muchos datos agrupados acá. Entonces mi gráfico de dispersión tendría que ser una cosa así. Sí, si yo miro desde acá, si yo miro desde acá, mi gráfico de dispersión debería ser, tengo mucha concentración acá y a medida que me voy, entonces un gráfico univariado como el que hemos visto en como el que hemos visto en el histograma o el o el o el de densidad, eh, te sirve para conocer la dispersión. ¿Y por qué? Porque si de repente, mira esta, si de repente esta que tengo acá yo le quiero sumar una tercer variable más que tenga menos dispersión, una varía que tenga menos dispersión va a ser más flaquita, va a tener la misma media, pero menos dispersión. Los datos están más concentrado acá.
Gabi Tallarico: Mhm.
lse posgrados: Sí. Y una variable con más dispersión y con la misma media sería más gorda.

00:59:36

lse posgrados: Así. En definitiva, la dispersión lo que hace es primero calcular la media, ponte acá está la media y después compara cada dato respecto a la media. Cada dato respecto a la media. Si vos tenés muchos datos, o sea, mucha área bajo la curva respecto a la media, disperso, tenés más dispersión. Pero para estudiar la dispersión de los datos, lo más importante es usar este tipo de gráfico. O sea, ¿cómo se cómo se dispersan ese tipo de acá? Este ahora, ¿cómo se dispersan en conjunto? Sí, ya aseguro al al al revés. Voy a voy a improvisar algo a ver si me sale. Por ejemplo, si yo tengo esto así y tengo esta variable, la miro así. Sí, tengo de un lado estoy mirando esta y de este lado estoy mirando y de abajo estoy mirando esta. Sí, tengo dos variables, esta que se distribuye así y esta queí. Y ahora cuando la miro en conjunto, si hago un gráfico y acá le pongo un gráfico de X e Y de estas dos variables. Acá en este sector de esta variable tengo muchos datos. Entonces acá tendría muchos puntos. ¿Sí?

01:00:50

lse posgrados: ¿Por qué? Porque coincide también con esta. Y a medida que me alejo, tendría más puntos hacia acá dispersos. Y a medida que me alejo, tendría más puntos hacia acá. ¿Sí? Entonces, esto tendría una concentración de este lado porque coincide con esta concentración y que con esta concentración, o sea, depende hacia dónde los mirás y por suerte todo eso se puede dibujar con con ah con mat o con ahí lo vamos a ver. Bueno, sigamos porque si no yo me cuelgo acá con los gráficos y la verdad que entre que este tema me gusta y que hay un montón para hablar. Otra forma antes de irme del scatter plot, sorry, es que le podemos sumar dimensiones así a simple vista. ¿Cuántas cuántas variables hay en juego en este gráfico? ¿Cuántas variables tengo?
Gabi Tallarico: Sí.
Shimon Ben: Ah.
lse posgrados: estoy usando para hacer este gráfico.
Marcelo Luna: principio tres,
lse posgrados: Perfecto. Ahora la la a mí me costó un montón,
Marcelo Luna: No.
Shimon Ben: Yeah.
lse posgrados: chicos, entender esto. Entonces, yo por eso lo trato de explicarlo así como bien sencillo.

01:02:05

lse posgrados: Tengo la variable uno, supongamos esta longitud del pico.
Marcelo Luna: H.
lse posgrados: Sí, la variable uno es la longitud del pico. Longitud. La variable dos es la profundidad del pico.
Marcelo Luna: Correcto.
lse posgrados: Profundidad del y la variable tres,
Marcelo Luna: La categoría.
lse posgrados: la categoría, o sea, que sería el especie en este caso.
Marcelo Luna: Claro.
lse posgrados: Entonces, ¿cómo se vería? ¿Cómo se vería un dataset para graficar acá? lo me interesa para que cuando lo lo hagan o el dataset se vería. Si yo tengo, por ejemplo, longitud pico 45 e profundidad pico 16 eh Adelin Adeli, ese sería una fila del dataset. Sí, la segunda fila del dat o la Sí, bueno, otra fila del dataset podría ser eh 50 de longitud de pico, eh 12 de profundidad de pico, gentu. Sí. Entonces, lo que voy a hacer acá es decir, bueno, al gráfico, al al código le tengo que decir, mira, en X, en X pone esto en I, porque este es como cosa gráfico en I pone esto y el color, ¿sí? El color pone esto, ¿sí?

01:03:34

lse posgrados: Eso le vamos a decir en palabra sencilla y le tenemos que cuando hagamos usemos un Llm para graficar le tenemos que decir, "Che, mira, usa un B gráfico X e Y ponerlo por esta variable categórica." Entonces acá variables numéricas y la variable categórica sirve para separar grupo, para agrupar por color. Entonces acá ya a simple vista puedo ver que acá hay una separación y acá hay una separación y acá hay una separación. se ve, digamos, ¿no? Entonces, yo tengo que hacer un problema de clasificación, podría utilizar esto o capaz que vieron árboles, pero los árboles sería sería muy fácil acá porque un árbol un árbol va a explorar esto, va a explorar esto y va a explorar esto y lo que va a hacer es buscar un grupo homogéneo por un índice que se llama Gini, por hacer grupo homogéneo. Entonces, para eso sirve la visualización y ponerle más variables. Ahora sí, ahora sí pasamos, les prometo que pasamos al próximo gráfico. Eh, acá en algún color le en el código, en alguna parte le está puesto para dónde poner el color. Primero, en este caso defino los colores y después decir, bueno, el lo el va por grupo y separármelo por colores.

01:04:53

lse posgrados: Sí. Eh, acá de nuevo, ¿qué es lo que va en X? ¿Qué? ¿Cuál es el dataset? ¿Cuáles son las X y cuáles son las I? Todos los gráficos y todas las librerías de de de Python son las mismas. Todas van a ser le tené que decir cuál es el X, cuál es el I, cuál es el color o cuál es el simap o dependiendo de cuál sea el tipo de gráfico. Ahí va.
Gabi Tallarico: Y ese código,
lse posgrados: Dudas.
Gabi Tallarico: sí, ese código que tenés ahí, ¿lo puedo poner en un colap o sí o sí lo tengo que poner en
lse posgrados: Sí. No, no, no. De hecho, no, no.
Gabi Tallarico: R?
lse posgrados: De hecho, está puesto en las en los que le el en
Gabi Tallarico: Ah, en los colaps que nos mandaste,
lse posgrados: sí escolar que está puesto,
Gabi Tallarico: no los miré todavía.
lse posgrados: ahí está el código, pero si quieren un poco más, lo mejor siempre es ir a la eh documentación. Esa es la otra regla, ir a la documentación y acá digo, bueno, acá tengo SBORN, ¿sí?

01:05:51

lse posgrados: Y acá hay una galería. Y si, bueno, veamos. Eh, est scatter plot. en Scatter plot. Fíjense acá te ya te da el código, pero veamos lo lo que lo que tiene esto. Mira, acá vos llamas a la librería. No me gusta explicar código a mí porque yo creo que por ahí no no aporta,
Gabi Tallarico: Ok.
lse posgrados: pero bueno, en este caso lo explico. Llamada a la librería. Llama el tipo de gráfico. En X ponés una variable. En I pones otra variable. Acá v el color pones otra variable. El tamaño del, en este caso, el tamaño de cada puntito que estás viendo acá. Fíjate que tiene puntitos chiquitos y puntitos más grande. tamaño lo pone en otra variable, o sea, ya tenemos cuatro dimensiones y después lo va cocinando con eh digamos cuál es la paleta, etcétera, etcétera, etcétera. Sí. Y ahí tener el gráfico, pero se se hace así, o sea, como que va a diferencia de de digamos de de GG Plot y de R, eh, acá va todo en un en un solo código.

01:06:56

lse posgrados: En R vos lo que tenés que ir haciendo agregándole capas con GG Plot. Si hay GG plot puede correr en Python. Hay una librería que ya ni me acuerdo el nombre, pero te la busco donde podés usar exactamente el mismo código de R de GG Plot, lo pegas y funciona. Obviamente tiene otra complejidad. Y bueno, acá hay acá hay un montón de cosas para jugar, pero básicamente uno puede venir acá y acá están todos los tipos gráficos que le que le explico, pero después lo ven después lo vemos bien en la en en la notebook. Me interesa más que entiendan cómo se cocina, o sea, porque después usted le van a poner al LM, eh, necesito un gráfico de profundidad por pico por color que esté por esto y chao, listo. Y que entendamos después ya esto era cuando yo estaba empezando, me acuerdo que tenía que ver todas estas cositas.
Marcelo Luna: M.
lse posgrados: Ahora ya ustedes no no tienen necesidad de hacer tanto código, digamos. Capaz que como profe no debería decirle esto, pero sí es la verdad. ¿Para qué le vamos a pelear LM si ya nos ganó, digamos, en ese aspecto? Bueno, ah, vamos al siguiente. Viene bien una repasada.

01:08:07

lse posgrados: Vamos primero. Regla uno, variable numérica hacia sí misma. Regla dos, variable categórica hacia sí misma. Conteos. Regla tres, variable numérica versus variable numérica. Scatter plot. Variable numérica versus variable numérica. Sumamos una variable más por color para separar grupo. Sí. Ahora vamos a estos que a mí también me a mí me gustan todos los gráficos, pero bueno. Estos gráficos los conocen, ¿saben lo que es un boxplot? Pablo no tiene ni idea lo que es un box. Digo,
Shimon Ben: los conozjo, pero no termino de entenderlos,
lse posgrados: tampoco.
Shimon Ben: así que
lse posgrados: No lo entendés al boxplot. Ahora, ahora lo vas a entender. Ahora mi objetivo es que lo entendas. Así que ahí vamos. Y para eso me voy a valer de este gráfico que está acá, eh, de este que está acá porque de este gráfico que está acá y de este que está acá. Bueno, entonces creo que este es más interpretable, pero más chiquitito. Ahí.

01:09:37

lse posgrados: Bueno, en este primero, un boxplot se puede construir de dos formas. De la misma forma que hemos construido esto, o sea, mirando la variable hacia sí misma. Sí. Y después, de la misma forma que hemos hecho esto, pero una una sobre la otra, fíjate que dice almuerzo y cena, están superpuesta una de la otra. Eh, de la misma forma podemos poner una variable categórica, sumar una variable categórica. Sí, es decir, tenemos una variable numérica, que es en este caso total. una y y cómo se distribuye esa total por sí misma, pero le sumamos una variable categórica. ¿Sí? Entonces, ¿cómo se construye un boxplot? Básicamente el boxplot lo que nos permite saber en la caja es dónde está el uy, ¿dónde está el así? Más fácil. la cajita, ¿dónde está el Q1? ¿Dónde está el Q3? ¿Y dónde está en la línea el Q2? ¿Saben de lo que le hablo cuando le hablo de Q o no? ¿Sí lo explico?
Marcelo Luna: los cuartiles.
lse posgrados: No. Perfecto.

01:11:06

lse posgrados: Los cuartiles.
Marcelo Luna: Eso.
lse posgrados: Pero, ¿y qué es un cuartil?
Shimon Ben: M. Yo no
lse posgrados: Bueno, qué difícil explicar los cuartiles.
Shimon Ben: sé.
lse posgrados: A mí me es difícil para alguien que no tiene idea. Es complejo. Bueno, ahí va. Mira, los se llaman cuántiles y son super importantes porque los cuantiles pueden ser deciles, percentiles, cuartiles, ¿sí?, etcétera. Ahora lo que tratemos de estudiar una sola variable. A ver, la diapositiva. Después volvemos a esa. Veamos esta que está acá. Espectacular. Decíamos que si nosotros veíamos esto así solamente desde un lado, desde una variable, tiene una dispersión, ¿cierto? Cuando uno pone los datos así, lo que hace es el menor está acá y el mayor está acá, ¿cierto? Entonces, la primer regla para armar cuantiles es ordenarlo de menor a mayor.
Marcelo Luna: Mhm.
lse posgrados: Y después empiezo. Bueno, este este es el primero, este es el último, ¿cierto? Bueno, viene por acá y en medio tengo un montón.

01:12:25

lse posgrados: Entonces, yo lo que hago es decir, "Bueno, hasta acá, ¿cuántos hay? Hasta acá cuántos hay. Hasta acá cuántos hay. Hasta acá, ¿cuántos hay? Hasta acá, ¿cuántos hay? Hasta acá, ¿cuántos hay? Hasta acá, ¿cuántos? ¿Cuántos casos tengo, digamos? Por eso cuánt y lo y y entonces obviamente acá vo empieza en cero y acá me termina en 100, ¿cierto? Si hablamos cantidad de datos,
Shimon Ben: Es un muestreo.
lse posgrados: acá tengo un dato, ¿sí? O sea, y acá a medida que voy agregando todos estos datos al a la var, o sea, los voy contando ordenado de menor a mayor, que acá están ordenado de menor a mayor, voy teniendo más cantidad de datos hasta que tengo todos los datos dentro de mi caja, ¿cierto? Entonces ahí cuando acabe a tener un 0% cuando no tenga ningún dato. Y si yo tengo si yo tengo 100 datos, asumamos que estos puntos son solo 100. Cuando llegue al punto número 100, que representa la variable en su valor 50, voy a tener todos los datos dentro de mi de mi bolsa, por así decirlo.

01:13:26

lse posgrados: Bueno, de la misma forma, progresivamente, a medida que voy aumentando son los cuantiles. Entonces, si de repente llego al 25% de los datos, ese valor que está acá, significa que acá tengo el 25% de los datos. ¿Sí se entiende? Si yo llego al 90% significa que hasta acá tengo el 90% de los datos. Entonces yo pregunto, es importante saber hasta dónde tengo todo, hasta dónde, hasta dónde tengo x cantidad de porcentaje de los datos. Decilo, Marcelo.
Marcelo Luna: No,
lse posgrados: Dale,
Marcelo Luna: no, no, no quiero ahí monopolizar,
lse posgrados: dale.
Marcelo Luna: pero sí es importante porque digo Porque de alguna manera también vos podés ir identificando cuáles son los intervalos donde tenés la mayor parte de los datos
lse posgrados: Perfecto. Ahí está. Ahí está.
Marcelo Luna: relevantes.
lse posgrados: Eso es importante. ¿Por qué? Porque lo que yo voy a buscar es que mi modelo satisfaga el x cantidad de por todas
Shimon Ben: Mhm.
lse posgrados: las situaciones. Entonces, si yo hasta acá, supongamos que hablamos de la regresión lineal, la regresión lineal, supongamos que funciona bien en este rango, ¿sí?

01:14:44

lse posgrados: En este rango de datos, incluyéndolo a este de acá. Si yo hasta acá tengo el 80% de los datos y esto es homogéneo, yo me pregunto, ¿para qué voy a usar un modelo con estos datos? Lo uso para acá y acá lo elimino porque ahí se dispersó, no me sirve el modelo. ¿Se entiende?
Marcelo Luna: Sí, ahí es donde perdés,
lse posgrados: Esa es el claro.
Shimon Ben: Hvor
Marcelo Luna: perdón, ahí es donde perdés confianza en en la predicción, justamente.
lse posgrados: O incluso puedes hacer el modelo,
Marcelo Luna: Sí.
lse posgrados: tu modelo de regresión lineal, puede venir por acá y vos puedes decir, "Bueno, ¿sabes qué? Yo voy a predecir la propina hasta una hasta 25.
Marcelo Luna: Exact.
lse posgrados: Más allá tengo mucha incerteza, es los datos no me sirven." Y y acá y tomé la decisión en base al 80% de los
Marcelo Luna: Mhm.
lse posgrados: datos. ¿Y cómo sé que el 80% datos? que calcule el P80 y el P80, el P80 que supongamos que es este, me dio 25. Me dio el 25, no,

01:15:45

Marcelo Luna: Correcto.
lse posgrados: no me dio 25%, me dio $25. Entonces, yo sé que mis variables desde 0 hasta 5, ¿sí? Representa el 80% de todas mis situaciones.
Marcelo Luna: Mhm.
lse posgrados: ¿Sí? ¿Quién lo entendió así?
Shimon Ben: Perdón,
lse posgrados: Buscó otra forma de explicar.
Shimon Ben: yo quiero saber si el Voxplot me sirve para identificar en dónde se produce la mayor cantidad de datos.
lse posgrados: puesto que
Shimon Ben: O sea, yo digo, bueno, no sé,
lse posgrados: sí.
Shimon Ben: de 100 personas, eh, los que más propina dejaron son los que gastaron menos de 50,000 pesos. Entonces, los otros no me interesan y yo voy a mostrar los que gastaron menos de 50,000 pesos porque ahí se concentra la mayor cantidad de datos. Lo demás es como que gasto mucho
lse posgrados: Sí,
Shimon Ben: recurso.
lse posgrados: sí, sí lo hace, pero hay que usar un hay que abstraerse un poco. Si al 50% te digo que sí.
Shimon Ben: Okay.
lse posgrados: Ahora un x% tendrías que hacer un un gráfico particular, ¿me entendés?

01:16:51

Shimon Ben: Hm.
lse posgrados: Pero el 50% seguro que sí. Y te voy a explicar por qué.
Shimon Ben: Pero entonces yo recurro al gráfico el box flot solamente en esos casos que identifico que la
lse posgrados: No, no,
Shimon Ben: cosa
lse posgrados: no, no, no. Shim, no. ¿Por qué?
Shimon Ben: Ok.
lse posgrados: Porque vos recurrís al boxplot cuando querés ver cómo se distribuyen las variables. Entonces, si si a vos, por ejemplo, vos tenés,
Shimon Ben: Hm.
lse posgrados: apongamos este caso, este es un gráfico también de distribución. Este es un gráfico de distribución univariable. Acá vos ves cómo se distribuye la variable, pero decme acá dónde está el 50% de los datos, entre que y qué.
Shimon Ben: entre el 5 y el 25,
lse posgrados: ¿Y cómo sabés que ese es el 5 de 25?
Shimon Ben: porque son los que más donde hay mayor densidad de gasto.
lse posgrados: Visual.
Shimon Ben: Sí,
lse posgrados: E visual. Es visual. Es visual. Okay.
Shimon Ben: claro.
lse posgrados: Ahora, esa es la diferencia porque vos pu decir, yo te pregunto a vos y vos decís, "Bueno, mira, Cris, acá el 50% de datos están eh entre acá y acá para mí entre acá."

01:17:59

lse posgrados: Y Marcel me va a decir,
Shimon Ben: Sí.
lse posgrados: "No, Cris, mira, parece que está dentro de la calle acá y no sé, Juan Pablo, etcétera. No, mira, para mí está entre que acá para sacar eso de discusión existe el boxplot, digamos, el 50% de los datos en el boxplot están en un solo lugar y es entre medio de las cajas.
Shimon Ben: Hm.
lse posgrados: Sí, en medio de la en el medio de las cajitas. Y este lo voy a poner así horizontal porque lo estábamos trabajando horizontal. Sí. Y vamos a ver solamente uno. Sí, acá tenemos el total bill. Sí. Ahora tenemos los datos ordenados. Tenemos los datos ordenados de menor a mayor total bill. Esto no lo veamos. No veamos si es jueves todavía. Tenemos los datos ordenados de menor a mayor y tenemos total bill. Sí, este es el valor más chico y este el valor este es el valor más alto. Sí, están todos los datos ahí como puntos. El 50% de los datos en el en el boxplot están en la caja. Acá y acá.

01:19:14

lse posgrados: Acá ten 50% los datos. ¿Y cómo sabes que el 50% de los datos? Porque acá está el Q1 y acá tené el Q3. En términos de Q de digamos de de cuartiles, el Q1 el Q1 el 25%. Ah, voy a escribir bien porque si no esto no me gusta. Sí, en términos de cuantil Q1 es igual al 25% de los datos. El Q2 es igual al 50% de datos. ¿Sí? El Q3, ¿a qué porcentaje será?
Shimon Ben: 25,
lse posgrados: Exacto, 75.
Shimon Ben: pero
lse posgrados: Y ahora si yo resto el 75 - 25, ¿cuánto dato mete? ¿Cuánto porcentaje de dato tengo? Exacto.
Shimon Ben: se encuentra.
lse posgrados: Bueno, es es la utilidad ese una utilidad del boxplot,
Shimon Ben: Sí.
lse posgrados: tener la mitad de los datos acá. Otra utilidad del boxplot es sobre todo conocer este que está acá de forma visual, que es la mediana, que es este que está acá. Entonces, en un boxplot vos vas a tener un Q1, un Q2 y un Q3.

01:20:37

lse posgrados: Sí. Y la mediana, ¿para qué te sirve? Para comparar, para comparar los datos. ¿Por qué? Porque la media cuando cuando vos tenés distribuciones normales y todos se distribuyen, digamos de forma normal, la media y la mediana es lo mismo, están en el mismo lugar. Ahora, si vos tenés distribuciones asimétricas, la media está por un lado y la mediana está por el otro. Y la media no es representativa de toda la distribución. La mediana es más representativa de toda la distribución. Yo siempre pongo las notas, yo pongo ejemplo las notas o o las notas de las notas que uno se saca. Si yo me saco eh suponente me saco todos 10 o 9 entre 9 y 10 y de repente tengo un uno, el promedio me va a bajar un montón porque tengo ese uno, pero yo uso la mediana, no me va a bajar tanto porque lo ordeno de menor a la mayor, tomo el que está la mitad y me va a dar ocho o nueve. Sí, pero si yo pongo el uno en el promedio, me lo tira para abajo. Si me saca un cero, ni hablar porque tengo la mitad de los datos, o sea, tengo voy directamente el valor de la mitad.

01:21:38

lse posgrados: ¿Se entiende? Entonces, una utilidad, 50% los datos. Segunda utilidad, ¿dónde está la mediana para comparar? Tercera utilidad,
Shimon Ben: H
lse posgrados: la distribución. ¿Por qué? Porque suena lógico que si yo tuviese los datos, estos datos están más agrupados hacia hacia acá, hacia donde está la a donde está la cajita. Entonces, yo voy a tener dos cajitas, una caja que está así y de repente tené otra caja que está así. Sí, es la misma variable, pero este es para lunes y esto es para martes. Son distintos, digamos, ¿no? Evidentemente algo pasa el martes que la mediana está acá y la mediana está acá y el 50% de los datos del lunes están acá y el 50% datos del martes están acá. Entonces, la utilidad del boxplot es esa, es de una sola vista conocer la distribución de los datos. ¿Sí? Entonces, vos, digamos, de esta forma uno en uno podría ya directamente decir, bueno, cuanto más grande la caja, más dispersos los datos, cuanto más a la izquierda, más simétrica o más a la derecha, más asimétrica.

01:22:50

lse posgrados: Cuanto más chiquitita la caja, tengo los datos más concentrados. Sí. Y si me aparecen y también esto, si me aparecen estos que están acá aislados, que tienen un nombre particular, ¿se acuerdan?
Shimon Ben: Lad
lse posgrados: Sí, exacto. Si se si me aparecen esto por acá, eh, digamos también informa. Entonces, esa es la utilidad del boxplot,
Marcelo Luna: Ah.
lse posgrados: ¿sí? De una sola vista conocer distribuciones de la variable y por eso es importante que cuando uno hace el boxplot le ponga cierta transparencia a estas a estos puntitos. Me parece me parece útil ver cómo cómo están. Ahora, en este sentido, fíjense, los puntitos están como de un lado y del otro, pero es ruido. ¿Por qué? Porque no hay un pasamos de jueves a viernes, ¿no? De jueves y 2 horas hacia el viernes. ¿Se entiende esta dispersión que tiene los datos acá? Sí. Esta dispersión que se ven así es ruido que uno le agrega para que se puedan visualizar. Sí, es ruido, porque si no yo tendría, si yo no pusiese ese ruido, tendría todos datos alineados acá, pues están todo el jueves, digamos, se entiende eso también se lo puede se lo puede poner ahí con una característica.

01:24:03

J.Pablo Zebraitis: Profe, esa forma deización sería problemática si las variables son bimodales,
lse posgrados: Sí,
J.Pablo Zebraitis: ¿no? O sea, si no es unimodal.
lse posgrados: qué buena pregunta. Si son, digamos, vos no podés tener dos,
Shimon Ben: Co?
lse posgrados: no podés tener dos medias, no podés tener dos medianas, tenés una sola media y una sola mediana. ¿Sí? Ahora, si vos tenés dos modas en la distribución, cuando vos calculés la media o la mediana, eso se van a se van a acercar, digamos, y te va a hablar por todos los datos. Ahora, es cierto, y muy buena la pregunta, que si tener una distribución que sea muy bimodal, muy bimodal, eh, el boxplot lo que va a ser, ¿qué va a ser el boxplot para una distribución que sea bimodal? ¿Esta caja se va a hacer más grande o se va a hacer más chica?
Shimon Ben: Eh, para mí más
lse posgrados: Supongamos se va a hacer más grande porque tenés dos tenés dos modas.
Shimon Ben: grande.
lse posgrados: Entonces el boxfow no va a cambiarse, va a ser simplemente más grande.

01:25:09

lse posgrados: Ahora, lo que vos te tenés que preguntar es por qué es bimodal la por qué es bimodal la distribución y si no hay algo en el medio que te permita separar esas dos esas dos variables.
Shimon Ben: Hm.
lse posgrados: Sí, muy buena la pregunta. Me me me llevó. Bueno, a ver, yo la verdad tengo que avanzar un poquito. Eh, de nuevo, lo importante acá es que el boxplot es una originalmente y por definición es un gráfico univariado, es decir, vemos cómo se distribuyen los datos hacia sí mismo, pero en la práctica son birivariados, por así decirlo, digamos. ¿Por qué? Porque no tiene sentido ver una distribución por sí misma. A veces uno lo que busca es para comparar. Sí. Y para comparar, ¿por qué? Porque nuestro objetivo como nada, como usuario de la IA o como o como científicos de datos va a ser encontrar relaciones que hay entre los datos. Entonces, si de repente yo necesito eh yo tengo una una distribución de este tipo, así, ¿sí? Este es la cantidad de palabras, ¿sí? la cantidad de palabras que tienen cada un decreto, una resolución, un edicto sucesorio en un trabajo de eh procesamiento de lenguaje natural.

01:26:33

lse posgrados: ¿Cuál es el que se comporta distinto? ¿Cuál es el distinto de la familia según el gráfico?
Shimon Ben: El
lse posgrados: Bien, vamos, vamos.
Shimon Ben: decreto
lse posgrados: Sí, perfecto. El decreto es distinto. ¿Por qué? ¿Qué interpretamos acá?
Shimon Ben: tiene más palabras, pero es más breve en el tiempo.
lse posgrados: porque tiene es tiene más palabras, pero menos dispersión. O sea, ¿qué significa que tiene más palabras? Los decretos tienen muchísimas más palabras en en general tienen casi acá la dos, acá la tres casi un orden de magnitud más, un orden de magnitud más palabras y encima se distribuyen eh poco,
Shimon Ben: H
lse posgrados: o sea, que casi todos tienen la misma cantidad de palabras, o sea, hay poca dispersión de palabras. significaría yo si fuese y no soy abogado, pero lo que yo diría que copian y pegan los decretos y le cambian el contenido. Sí. Sí. Eh,
Marcelo Luna: He.
lse posgrados: entonces, bueno, ahora las resoluciones tienen también se Bueno, acá tenemos una separación. Las resoluciones también se separan del resto. Las resoluciones tienen más dispersión, pero son e asimétricas hacia allá.

01:27:40

lse posgrados: O sea, significa que que hay alguna resolución que tiene poca palabra, pero la mayoría de la resolución de las resoluciones tienen esta cantidad de palabras. ¿Sí? Ahora, esto me sirve, es sumamente útil en en un en un contexto de de exploración de un dataset de de procedamiento de lenguaje natural. Sí. Eh, Shimón, si vos de repente estás analizando emociones y uno cuando está enojado usa más cantidad de palabra, ¿sabe qué? uso la separación de emociones por cantidad de palabras y no uso un Llm, me ahorro un trauma para usar un LM, digamos, no entender lo que es un transformer, aplicar similaridad, tokenizar y todas las cosas que vieron. Capaz que no es necesario si podés segregarlo con cantidad de palabras, digo, ¿no? Para eso sirve, digamos. Bueno, y toda esta familia que están acá son parecidas, digamos. Sí. No sé si se acuerdan de estadísticas. Es que vieron alguna vez, si obviamente si yo hago un test estadístico acá para ver cuál es distinta de cuál, estas dos me van a dar redistintas. Y acá el test yo creo que ya no va a dar tan distinta. ¿Por qué? Porque en esa dispersión que tiene los datos hay similaridad.

01:28:49

lse posgrados: Entonces, cuando hag un test para diferenciar si esto es distinto de cuál, es probable que estas dos sí se si sí se sí se separen por ese T estadístico, porque no comparten prácticamente nada la distribución. Fíjate que esta termina acá y esta tiene hay uno que no y en cambio estas sí tienen sí comparten bastante digamos. Bueno, vamos hacia eh Uy, encima esto da para largo, che. Bueno, eh a esta me le salteo, voy directamente a este a conteo por categoría. Ahora, ¿qué pasa si tengo dos columnas categóricas? O sea, tengo dos categorías. Sea, cuando teníamos una categoría, hacíamos contego y gráfico de barra. Cuando tenemos dos categorías, hago conteos, digamos. Sí. Y los conteos los puedo hacer de forma proporcional o los puedo hacer de forma, digamos, absoluta. En este caso, si yo veo la cantidad de almuerzo por día de la semana, viernes, sábado y domingo y si son almuerzos o cena, acá ya el gráfico me está comunicando que hay los sábados predominan la cena sobre los almuerzos. Quizás te cerrado el sábado, digamos, evidentemente. Y los días viernes no hay, evidentemente no hay cena.

01:30:10

lse posgrados: Bueno, entonces acá lo que hacemos es contar contar las intersecciones donde donde hay este caso hay 24 filas del dataset en las que coinciden el almuerzo con el día viernes. Entonces yo los cuento. Para hacer eso tengo que hacer uso de pandas que ya seguramente han visto alguito conocen. Pandas tiene algo llama cross tab. Cross Tab es una tabla cruzada donde lo que hace es contar. Entonces, a Cross Tab, ¿qué le va a entrar? Bueno, el tipo y eh la sección. Sección. Sección será almuerzo y el tipo será o bueno, o me parece que están otro lado, pero capaz tiene otro nombre, pero día de la semana. Sí, sección será día de la semana y tipo almuerzo. Ah, no, esta me parece que es de acá, pero bueno, no importa. Eh, veamos ahí una otra. En el ejemplo, ¿no? Yo hago esa cross tab. Primero tengo la tabla cruzada y después a esa cross tab le aplico el hit map. Eso es importante, que algunos gráficos requieren un preproceso antes. El boxplot requiere preproceso antes, ¿no? Le mandamos que x, que es y listo.

01:31:28

lse posgrados: Ahora, este tipo de gráfico sí necesitan una cross tab y a la cross tab la podemos poner e normalizada, digamos, o no. O sea, la podemos expresar en porcentaje o no. y a la vez lo va a poder presentar en en porcentaje respecto del total, ¿sí? O porcentaje de acuerdo a la fila o a la columna. Eh, este básicamente lo que hablamos de los boxplot y de las distribuciones. Hay una forma que es la acumulada, que este es el total, ¿sí? Dos distribuciones, pero hay forma de hacerlas acumulada y también sirve para discretizar datos. Voy a voy a adelantar esta para seguir. Ahora tenemos el el Hitmap aplicado a dos categóricas y ahora tenemos el Hitmap aplicado a dos numéricas. ¿Sí? Entonces el Hitmap aplicado a dos numéricas es eh en real a dos o más numéricas. Es conocer esa asociación que habíamos visto que se llamaba R, ¿sí? O o coeficiente de correlación. conocer esta sensación en vez de hacer, si yo tengo muchas columnas, además de propina y cuenta total, tengo muchas columnas y quiero conocer este R, en vez de hacer un gráfico para cada uno y plotear el R acá, puedo directamente hacer esto y esto me ahorra a mí hacer el gráfico.

01:32:57

lse posgrados: Yo acá veo asociación entre variables numéricas, entonces si es positiva va a ser mayor que cero. Si es eh cuanto más cercana a uno, mayor asociación. Cuanto mayor cercano a -1, mayor asociación negativa. Básicamente es la la lo que vimos de la si digamos si se asocia positivamente va en un sentido. En este caso, eh llevarme esto para allá este que tiene negativa. Sí. Acá estamos haciendo variables, dos variables numéricas. Hay algunos que son, fíjense que hay algunas que están en negativo. ¿Sí? Eso significa que si yo la hago un gráfico X e Y, los datos se van a distribuir de forma negativa. O sea, a medida que aumenta una, decrece la otra. ¿Sí? Y hay otros que son positivos. Los que son positivos, 096, es prácticamente una línea que va así tiqui tiqui tiqui tiqui tiqui tiqui porque están muy asociados, hay poca dispersión y son positivos. Entonces, de una sola vista este hitmap eh me da los digamos las correlaciones y cuál está variable, cuál está asociada con cuál. Y acá les voy a mostrar algo que que es importante porque decir, bueno, che, esto para para mis textos no funciona más o menos porque si yo tengo las similaridades puedo hacer esto, ¿sí?

01:34:33

lse posgrados: Yo acá puedo tener documentos distintos y ver que es la similaridad usando TF y puedo graficar qué documento es similar con cuál, digamos. Sí. Entonces, ¿cuántos documentos similares tengo? Si tengo muchos documentos similares, hay mucha redundancia de datos y para qué voy a procesar tantos documentos si me aportan lo mismo y si hay documentos muy distintos, bueno, uno puede explorar por ahí, ¿se entiende? digamos, no, no hay que llevarlo, hay que llevarlo todo a digamos al procesamiento del de este caso de texto. Si vos tenés dos documentos que son 99% similares o 100% de similaridad, significa que es prácticamente el mismo documento. Entonces, vos v a tener que preprocesar dos veces el mismo documento, gastar toques en el mismo documento, no tiene mucho sentido, ¿eh? Y esto sigue hasta el infinito. Bueno, cuando quiero hacer esto que hemos visto, pero a gran escala y no usando, o sea, conocer las asociaciones y no hacer un gráfico por cada combinación de variables, existe lo que se llama el pair plot. Esta es la regla siete. El payer plot lo que hace es masivamente agarra el data frame todas las variables numéricas y te hace este gráfico que está acá, que cada una de las partecitas es la asociación entre dos variables.

01:35:59

lse posgrados: Entonces acá, fíjense que si acá el pel plot lo que va a hacer, toma todo el data frame, no hay que ponerle xn, toma todo el data frame y empieza a cruzar todas contra todas. Digo, lo que sí es útil usar es V. V como la el color. El color, ¿por qué? Por clase. Entonces, acá me va a separar las clases según el la especie en este caso. O sea, va a ser le va a otorgar un color a cada punto según eh según eh la especie o clase. En este caso, ¿qué pasa si tengo un dataset, numérico muy grande? Esto las combinaciones se va a hacer muy grande y esto suele llevar cuando uno lo corre demoro un ratito si tengo muchos puntos porque tiene que ir viendo todas las combinaciones, etcétera, digamos. Y a ver si alguien me dice que qué pasa si yo dibujo una línea acá en en la diagonal, ¿qué hay de la diagonal para arriba y que hay de la diagonal para abajo? ¿Qué sucede ahí? una ayudita, sepa lengamos sepal with es lo mismo que cepal wi versus cepal leng, ¿verdad? Entonces, lo que lo que va pasando acá es que lo que tengo de este lado de la diagonal es igual que lo que lo tengo de este lado de la diagonal.

01:37:29

lse posgrados: Claro, exacto. Nada más que yo en vez de combinar x con y, combino y con x, digamos, ¿no? Entonces este gráfico también tiene redundancia. ¿Para qué quiero la otra mitad? Y lo veíamos también anteriormente acá en en esta en este gráfico. A mí me interesan las estas combinaciones, estas asociaciones que están acá entre ella misma, o sea, acá va a dar uno, todo esto va a dar uno y hacia allá se van a repetir los valores que están acá. Entonces es importante que en alguna parte hacer un un mask, que se lo puse acá en un pedacito de código, que es básicamente usar una función de Numpie para que solamente use la la triangular, o sea, esta parte de acá y no la que está arriba, digamos. A ver, gráficamente puede poner todo, pero visualmente se ve mejor así. Bueno, y ahora eh vamos directamente a la a la a la aplicación en en en el en los rack, ¿no es cierto? Eh, en este caso lo que lo que hacen estos gráficos que están acá y me gustaría que ustedes los ha esto es lo que ya ustedes tendrían que hacer así. Yo le metí sin asco una hora y media.

01:38:49

lse posgrados: Eh, bueno, hagamos un recréito. Mira, la la Gabi tiró el recreo, si no yo le doy hasta el infinito. Bueno, ¿cuánto cuántos usualmente descansaban? 15. Está bien. 10 15.
Gabi Tallarico: 15. A mí no me da la cabeza.
lse posgrados: Perdón, perdón.
Gabi Tallarico: Necesito baño.
lse posgrados: Bueno, ahora lo vamos a hacer porque vamos a ir directamente a la notebook y ahí en ahí les voy a mostrar los gráficos que ya
Gabi Tallarico: Bien.
lse posgrados: están y que ya están configurado para que ustedes lo puedan copiar el código, tratar de ayudarse con ese código para hacer lo suyo. Dale.
Shimon Ben: Bueno,
lse posgrados: Eh, cortamos, volvemos. Son 35 40 a la y 50. Sí,
Shimon Ben: bien.
lse posgrados: 9. Volvemos.
Shimon Ben: Listo.
lse posgrados: Bueno, ahora sí voy a apretar un poquito, así vemos todo lo que lo que tenía planeado ver. Bueno, obviamente cuando hablamos de NLP y lo que dijo Gabi hace rato, bueno, si todo esto es bueno cuando tenés variable y casos numéricos, machine learning, pero cómo lo llevamos a nuestros casos de texto, digamos, ¿no?

01:54:49

lse posgrados: El primer los primeros la primer regla, la primera utilidad es hacer conteos, básicamente. O sea, bueno, ¿cuántos documentos de qué tipo? Eh, etcétera. Esa es la la primera para los conteos son los gráficos de barra. Eh, pero también hay hay otra hay otros gráficos, no solo no son solo conteos, digamos. Eh, ahí lo lo vamos a ir viendo. Le puse alguno en la presentación, le puse algunos tips para documentar el hallazgo, el el el alfa, usualmente la transparencia cuando tengo varios eh digamos varios colores o varios varios puntos, cuando los puntos no tienen transparencia, no se ve en el que está uno abajo del otro. Entonces, simplemente le puse algunos tips para que para que vean. Y ahora nada, bueno, esto lo vamos a hacer al final. Pero no sé si lleguemos, pero si no queda para la para desarrollar, pero lo ideal es que a partir de lo que yo les muestre ahora de cómo procesarlo con el texto, ustedes después durante la semana lo apliquen según sea su caso con estas guías que están acá. No habíamos definido, ¿se acuerdan? el track de rack y el track de clasificación que habíamos visto anteriormente y qué es lo que se podría hacer con cada uno.

01:56:09

lse posgrados: Y el checklist de nuevo es una entrega optativa para que yo mire, nos alineemos, etcétera. no es obligatoria, pero sí deberían hacerlo porque algo de exploración debería tener el el trabajo final, el documento y en la presentación. Y acá les puse nada, que describan un checklist de las cosas que te que deberían hacer, digamos, antes poner un gráfico y lo que deberíamos entregar. Nada, una notebook, al menos tres gráficos, una tabla de resumen, tipo de documento, la longitud, algún problema de que detectado en ese documento y los hallazgos y qué se aprendieron de los datos. Algo muy simple, ¿no? No pido que hagan mucho mucho más que eso. Sí, le voy a mostrar un caso para que para que sea más útil. Sí, esto lo vamos a llevar un caso particular. ¿Cuál es ese caso? Tenemos un documento cargado en la en la en la carpeta de la clase que es de tipo texto. son es una parte de un boletín oficial, es deben ser 20 páginas o 16 páginas, no me acuerdo, de un boletín oficial de la provincia de Salta, creo que fecha 2025, 31 de marzo de 2025, que la lo ideal, lo que vamos a hacer con esto y lo que hace la notebook en realidad es eh tratar de identificar en entidades, tratar de sacar información, preprocesar, hacer todo el EDA a través de esta de estos documento de texto para que les sirva de ejemplos a

01:57:42

lse posgrados: de ejemplo a ustedes en para su trabajo. ¿Sí? Eh, eso lo van a encontrar en esta notebook que ahora la descargo y la subo a esta notebook que va a quedar en material de clase junto con con lo que ya subí. El A es la de la visualización. En el A van a encontrar todas las reglas que hemos visto de la 1 hasta la 8 con ejemplos. y el código, ¿sí? Todo lo que hemos discutido hasta ahora, sí, regla siete, código, algunas algunas cositas más para que tomen de ahí ejemplos. Y en la dos, para que corra esto, tienen que descargar el documento que dice 2C, lo descargan como lo como lo hacen en su trabajo y lo suben a la carpeta acá al raíz a la raíz de la no. Una vez hecho eso, corren todo y va fase por fase. A mí, la verdad, no me gusta mucho explicar código, me parece que no no tiene mucho sentido. Voy directamente a una PPT que hice explicando el caso. Sí, les parece bien así o prefieren ver código porque capaz que son fan del código. Sí, Marc, decí está muteado.
Marcelo Luna: Perdón, estaba en mute.

01:59:00

Marcelo Luna: Te hago una pregunta. Eh, cuando trabajas con más de un documento que no documento repetido, no decretos repetidos, pero digo, cuando tenés, por ejemplo, un documento y otro documento complementario, como es el caso que tengo yo en mi TP, ¿qué se acostumbra a hacer? Se acostumbra a hacer un análisis por cada uno de los documentos o se hace todo el análisis junto. Eso no no tengo claro.
lse posgrados: Yo uniría todo y le pondría de nuevo una al a los documentos,
Marcelo Luna: Sí,
lse posgrados: una columna va a tener la fila va a estar separado en chans, ¿no es cierto? V tener un dataset donde cada fila va a ser un chanks.
Marcelo Luna: sí, sí.
lse posgrados: Usa una columna más y ponerle tipo original complemento y ya tenés todo en una sola y tenés una columna que los divide. Entonces,
Marcelo Luna: Okay.
lse posgrados: ya podés trabajar con esa columna que va a ser tipo categórica para decir, "Che, los complementos tienen menos caracteres, más caracteres, dicen otra cosa, ¿me entendés? Eso es lo
Marcelo Luna: Pero ahí lo que tengo que hacer es combinar los documentos.
lse posgrados: que
Marcelo Luna: El punto es que tienen contenido heterogéneo, ¿entendés? Porque por
lse posgrados: Pero con esa var categórica lo separas fácilmente porque después filtras y lo tenés todo en un solo en un

02:00:11

Marcelo Luna: ejemplo,
lse posgrados: solo dataset, ¿me entendés? Yo yo haría eso.
Marcelo Luna: sí.
lse posgrados: Incluso, por ejemplo, este caso del boletín son eh aplica un boletín, pero cuando está ejecutado aplica muchos boletines con distintas fechas, etcétera, con contenido semántico distinto, pero eh un solo dataset. O sea, si vos tenés un solo dataset, con una columna lo podés separar y después lo podés buscar más fácil, digamos.
Marcelo Luna: Okay. Bueno, por ahí después te escribo por mail porque
lse posgrados: Lo vemos después en clase. Prepara el notebook de
Marcelo Luna: bueno, si hay espacio lo charlamos,
lse posgrados: una.
Marcelo Luna: si no te escribo. Vale, vale.
lse posgrados: Bueno, le explico el caso. Vamos. Resulta que tenemos los boletines oficiales. Le quiero explicar un rack. ¿Cuál es el propósito de esto? Yo quiero entrar a a un a un a un a un a una plataforma. Sí. Eh, uy, perdón. Eh, se me quedó sin batería el teclado. Un ratito. Supongamos yo quiero el propósito de esto es yo quiero entrar a una plataforma.

02:01:42

lse posgrados: De hecho lo tengo corriendo acá para que lo veamos. Yo quiero entrar a una plataforma, ¿sí? Quiero entrar un chat y quiero hacer una pregunta y decir, "Bueno, bueno, ¿qué adjudicaciones simples hay, por ejemplo, y el RAC me va a devolver lo que hemos venido consultando, lo que venimos conversando hace un un tiempito. Sí, esto es un una un un RAC aplicado a algunos boletines. Ahora está haciendo la consulta, le está pegando la API, la API le va a devolver la respuesta y va a entregar información. Bueno, la respuesta es, según el boletín tanto y tanto del 29 de diciembre, hay una adjudicación simple y registrada. ¿Cuál es el número de adjudicación simple? ¿Quiénes son los adjudicatarios? Sí. Y este rack en particular tiene una verificación, básicamente es como otro prompt con otro agente que verifica que esto que estaba entregando acá está respaldado por un eh documento. ¿Cuáles son las fuentes que consultó para hacer esto? Bueno, yo le pedí en este caso seis fuentes. Primero me tiró esta como la ganadora con la cual armó la respuesta. Metadatos. Sí, eso lo vamos a ver al final de la clase que es importante.

02:03:02

lse posgrados: Y después me tiro otro más, otro documento más. Este el documento número uno, que es el ganador con el cual seguramente armó la respuesta. Y después me entregó otros documentos que que seguramente es Araza pero que nada, el Rack los los sacó. Sí. Entonces, el propósito de esto es tener un texto limpio o conocer el texto para poder limpiarlo y luego hacer una pregunta y que responda de esta forma y no de otra. ¿Se entiende? Para lograr eso hay que conocer los datos y explorar distintas cuestiones de los datos. O sea, en este caso de el boletín. Lo primero que veo yo, lo que primero se ve en el boletín, ¿sí? Si abrimos el boletín es que son cada corp est todo este el corpus general, ¿cierto? ¿Lo vieron? ¿Saben lo que se llama corpus? No, el corpus. Bueno, tenemos leyes, hay distintos tipos de de contenido semántico que tenemos acá. Primero, todos comienzan con alguna ley, casi todos, pero al final al final de cada documento existe esto que dice fecha de publicación y OP. ese el identificador de este texto que está puesto en esta ley. Entonces, en en mi estrategia, como yo quiero recuperar cada uno de estos o el contenido que tiene cada uno de estos, yo separé usando un patrón, este patrón que existe acá, para que a esto me lo separe como un documento y a esto me lo separe como otro documento y cada vez que

02:04:37

lse posgrados: aparezca este patrón me lo separe como un documento, porque yo necesito que el RAC me lea solamente el documento y no mezcle distintos estos documentos, ¿se entienden? Eh, ver, esa fue mi estrategia. Podemos encontrar otro patrón. Cada vez que empiece con salta 25 de marzo o Salta, etcétera, etcétera, podría separar documentos o cada vez que detecte esta línea. A mí me resultó fácil usarlo así. Entonces, van a notar que en la notebook aparece una parte donde se para documentos con con ese patrón. ¿Alguna duda?
Gabi Tallarico: ¿Cómo hiciste esa mini interfaz de consulta o con qué está hecho?
lse posgrados: Eso está hecho con Streamlit y es gratis. Eso está hecho con Streamlit. Es una librería gratuita que que hace como de frontend, digamos. Ahí le voy a explicar eh al final final voy a tratar de explicar cómo funciona eso para que para darles ideas de a su trabajo. Bueno, bueno, primero el corpus total es todo ese PDF. El patrón que hemos encontrado o que encontré fue ese patrón de OP número, que es lo que identifica cada documento. El resultado van a ser 12 documentitos, digamos, usando ese ese patrón, ¿no?

02:06:00

lse posgrados: Entonces, lo que hace la notebook que está ahí a lo que hace una ingesta, un edad, una limpieza y un chanking. Eso es lo que hace ustedes. La la primer clase. Hemos definido el problema. En esta clase, en esta clase vamos a conocer qué texto tenemos hasta llegar a un a un a un chank. Sí. Bueno, eh esto lo voy a poner mejor esto. Bueno, esos 12 documentos lo primero que hice fue eh digamos eh explorarlo, ¿no? Sí. contar cuántos caracteres hay en cada uno de esos 12 documentos usando esa OP. Entonces, lo que primero hice fue eso y ver detectar opciones de limpieza. Ustedes vieron que el documento tiene un encabezado. Ese encabezado tiene una determinada cantidad de caracteres y se lo saqué. Entonces usé este gráfico para mostrar lo que expliqué hace rato, cómo era el documento antes, ra o limpio, digamos, y cómo quedó después de la limpieza para ver si no hubo un exceso de limpieza en los documentos, porque no quiero perder información de los documentos. ¿Sí? Entonces, eso es un gráfico que ustedes también pueden hacer antes y después de cada limpieza. Sí, acá le peg un pedacito del código, pero el notebook está básicamente hay una esto es rejex.

02:07:29

lse posgrados: Eh, hoy en día con los LLM podemos decirle escribirme un patrón de reje que compile y que busque y que elimine. Eso básicamente lo que hace es buscar donde diga edición, número, salta, decreto, t ta ta ta, todo. Cuando encuentre ese patrón lo va a limpiar, ¿sí? Lo lo saca, digamos. Sí. Esa es una. Bueno, eh en la estructura del boletín oficial, esto es lo que hemos sacado, básicamente, todo lo que es encabezado lo hemos sacado y el delimitador usado fue este este documento que ese valor, esa cadena de caracteres que dice OP, digamos, ¿no? Estos son los separadores que hemos usado para que usé para cada documento. Y en función de este, cada uno de estos documentos se le hizo un EDA. Entonces lo que lo que vi fue decir, bueno, en de acuerdo a la posición en el corpus en términos de caracteres, cómo iban ocurriendo para ver y asegurarme que no haya overlap entre esos documentos. O sea, que mi separador funcionaba. Sí, porque si yo veía que los que la posición de los caracteres dentro del documento había overlap, significa que una resolución, digamos, no me estaba separando los documentos como yo quería.

02:08:51

lse posgrados: Esa fue un esa es, digamos, una forma de de hacerlo. Sí. A la ver otra otro gráfico que interesante, esto que dice SA, el identificador OP, que es básicamente uno que uno busca en el sistema del boletín oficial y encuentra rápidamente el documento. Lo que hice fue eh contar básicamente la cantidad de palabras, digamos, ¿no? Entonces, me di cuenta que algunas, digamos, según según si eran ley, decreto o o decisión administrativa, tenían mayor mayor o menor cantidad de palabras. Lo que preponderan acá son los decretos que en promedio casi todos tienen 600 palabras. lo que hablamos, muy probable haya un template del cual copian y pegan y cambian algunas cositas en el medio. Sí, las leyes suelen tener otras otra cantidad de palabras y lo que son decisiones administrativas, que son los de A, tienen otra cantidad de de palabras, digamos, ¿no? Eh, nada, un gráfico de torta, yo le estoy dando ideas y cosas como para que ustedes también hagan en sus documentos. otro otros descubrimientos, lo que hablamos del conteo por palabras y después se usa mucho, digamos, lo que llama correlación morfológica, que es decir, bueno, ¿cuántos caracteres por palabras hay y que eso tenga un sentido, digamos, no?

02:10:18

lse posgrados: Eh, si esto fuese disperso significaría que los entre documentos eh no sería lineal. Lo que está mostrando acá es que hay una linealidad entre las palabras y las cantidades de caracteres por cada tipo de de documento. Eso significa que al existir esa linealidad, el LLM va a poder predecir más fácilmente la siguiente palabra cuando tenga que hacerlo usando el RAC. Sí, eso pasa en estos documentos que son de tipo técnico. En otros documentos, eh, no sé si es un cuento, si es una poesía, si no va a funcionar, digamos. En este caso sí, digamos, ¿no? Otra cosa que es útil y que más o menos habla del del mismo fenómeno el ratio que hay palabras por carácter. Entonces, eh también nos sirve para decir, bueno, ¿cuál es el tamaño del de de el chang size adecuado para que contenga la mayor la mayor el mayor contenido semántico de la de cada documento, digamos, no? O sea, yo, por ejemplo, con un chunk size de 3,000 tendría aproximadamente 500 palabras. Hay que ver también si me inventar el contexto con el LM, etcétera, soportan esa cantidad de eh de ch de tran size, digamos, no matería, ¿no?

02:11:41

lse posgrados: Ahí está. Bueno, otra. ¿Saben lo que son las stops? La seguramente lo vieron en en al principio NLP más o menos. Bueno, las stopw son todas esas palabritas que no aportan contenido semántico, digamos, de el al hacia cómo será fuera. Sí. Entonces, saber qué porcentaje de esas palabras existe en cada documento también es útil y también se puede graficar. Entonces, uno detecta las stopw, las cuenta y las y las y la y hace un cálculo de la proporción que hay de esos stopws dentro del de cada documento. Sí. Y también la puedes poner. Bueno, ¿cuál es el top 20 en este caso de TopW de la el sí hay un documento técnico, entonces seguramente estas digamos si yo cuando haga la limpieza de stopw si yo saco mucha stop word en una limpieza, puede que me quede con muy poco fragmento de documento y pierda contenido semántico también, digamos, ¿no? Bueno, acá también es eh como ven, son casi todos conteos. También es útil decir, bueno, ¿cuáles son bigramas? Bigramas son aquellas palabras que siempre están de a dos y las y el conteo de cuántas veces aparecen esa combinación de dos palabras.

02:13:11

lse posgrados: Sí. Entonces, bigramas y trigramas. Entonces, provincia de Salta ganadora, porque obviamente todos los decretos y todo deben asociarse ahí, pero evidentemente también en en esta exploración hay 24 ocurrencias de retiro voluntario, lo cual significa que hay en en esta seguramente hay muchos decretos, decisiones administrativas que hablan de retiros voluntarios de personas, digamos. Sí. Entonces, de esta forma eh es como uno puede explorar los sets de datos que son de tipo eh de texto, digamos, ¿no? Y lo mismo eh con trigramas. Bueno, ¿se acuerdan de la similitud coseno? No es cierto. ¿Qué lo para hacer una similitud coseno? ¿Se acuerdan de lo que se hacía? Porque de básicamente lo tienen que usar, lo usan de su rack, digamos. su rack aplican similitud coseno seguro. El proceso es uno tiene el documento, a ese documento lo que hace es eh tokenizarlo y a esas tokenización lo que hace es para cada documento calcular cuál es la similaridad semántica entre cada documento. Obviamente al ser documentos legales y técnicos hay digamos una alta similitud. Lo que debe cambiar lo que debe cambiar es las personas.

02:14:45

lse posgrados: Por ejemplo, si yo tengo eh de no sé eh decretos eh decisiones administrativas de eh retiros voluntarios, si son 10, seguramente el texto sea exactamente el mismo y lo que cambie sea el nombre de la persona. Eso también habla de la de la exploración. Y hay alguno, obviamente en la diagonal están todos los uno, como hemos visto del hitmap, en la diagonal está todos los uno, pero eh ahí en algunos casos lo que hice fue decir, "Bueno, tráeme lo que tengan el top de similaridad." Entonces el la decisión administrativa número 100 y la 11 y 111 tienen el 100% son la misma. O sea, habría que entrar al texto y leerla. Debe ser la misma. Sí. O sea, capaz incluso sirve para detectar si hay duplicados, sobre todo redundancia en la info que están ustedes otorgándole al al retriver. Bueno, acá un poco de los de los boxplot. Eh, de nuevo, boxplot era una variable numérica mirada hacia sí misma, pero que se la contrasta usando una variable categórica, ¿no? Si contamos las cantidad de palabras, en este caso, si contamos la cantidad de palabras que hay, evidentemente las ley las leyes que están en este en este boletín eh debe haber una porque hay solamente una barrita, digamos, prácticamente no no debe haber más de una ley.

02:16:16

lse posgrados: Sí. Entonces, con lo cual no hay variabilidad y ocupa esta cantidad de palabras y donde hay más son la cantidad de decretos y están entre 500 y 600 palabras de de digamos por por cada decreto. Y las decisiones administrativas hay hay creo que eran dos o tres decisiones administrativas dentro del PDF. Casi todas tienen tienen poca dispersión, tienen la misma cantidad de pelabra, con lo cual es lo que decíamos, debense o retiro de voluntario o alguna cuestión que donde solamente camb cambia el DNI o algo por el estilo, digamos, ¿no? Y acá están graficado en gráficos de barras eh la cantidad de palabras por cada uno de los documentos, ¿sí? con un eh con un mínimo y un máximo, digamos, ¿no? E preguntas, chicos. ¿Tienen dudas? Sí, también tengo un poco de agua. ¿Habían aplicado esto antes o no lo ven posible en sus trabajos?
Juan Pablo Rueda: Profe, yo una consulta. Eh, en el caso mío de que estoy con el tema de de distintos productos, bueno, lo voy a eh sintetizar en solo bobinos. Eh, yo tengo un PDF por cada producto de bobino. Son alrededor de 16 17 productos.

02:17:50

Juan Pablo Rueda: Los podría meter todos en un mismo PDF para hacer un
lse posgrados: Vot. Tenés 17 documentos,
Juan Pablo Rueda: poco Claro, pero en ese
lse posgrados: ¿no? Y te da la cantidad de PDF y sacar la info que necesitas de esos PDF y poner un poner en un
Juan Pablo Rueda: cómo
lse posgrados: dataset, o sea, en una en un filas columnas, ¿me entendés? el contenido del
Juan Pablo Rueda: bien perfecto. Sí,
lse posgrados: texto.
Juan Pablo Rueda: porque hay información que se repite para todos los productos, por ejemplo, el periodo de carencia, la manera de de conservarlo el producto, eso es común para los 17
lse posgrados: O sea,
Juan Pablo Rueda: productos,
lse posgrados: eso no es información que te aporte variabilidad o algo que vos vos querás eh eh Okay.
Juan Pablo Rueda: ¿no? Claro.
lse posgrados: A ver, Diego, no te entiendo lo que me
Diego Methol: No, claro que bueno, estamos viendo un montón de ejemplos de visualización de datos aplicados a RC,
lse posgrados: dijiste.
Diego Methol: al procesamiento documentos, etcétera. Eh, y yo de la manera que que tengo planteado el trabajo no lo estoy usando, entonces tampoco sé tampoco me queda demasiado claro, o sea, entiendo lo para qué sirven distintas visualizaciones, sí, pero tampoco tengo demasiado claro cómo cómo poder aplicarlo a lo que yo ya estoy haciendo.

02:19:08

lse posgrados: Contanos, contame cómo qué estás haciendo y
Diego Methol: Yo estoy haciendo el análisis,
lse posgrados: y pero podes
Diego Methol: el análisis del seso político en noticias.
lse posgrados: contar palabra en en tu
Diego Methol: Eh, yo una de las cosas que estoy haciendo también para que sea fácil para el modelo,
lse posgrados: dataset.
Diego Methol: estoy por ejemplo estoy cortando, sí puedo, sí, o sea, estoy cortando las eh estoy yo obtengo las noticias de de la web directamente, las escrapeo de la web,
lse posgrados: Sí.
Diego Methol: corto el texto para que no sea demasiado grande. También descarto noticias que son cortas, por ejemplo, porque no tengo suficiente contenido como para poder aplicar un análisis.
lse posgrados: Te pregunto, ¿vos podrías comunicar de todo tu universo cuántas descartaste y cuántas te quedaste?
Diego Methol: Yo una de las cosas que tenía pensado hacer para esta segunda fase capaz era sí tener un histórico, por ejemplo, tener una base de datos donde yo guardo todos los procesamientos que hago, entonces también me guardo esa información para atrás para después eventualmente poder hacer algo con eso.
lse posgrados: A ver, el objetivo de la exploración es conocer la la conocer y comunicar, básicamente. Entonces, si vos me decís que vos tenés una noticia y qué fragmento de la noticia eh lo podés descartar porque no te aporta ese fragmento expresado en porcentaje, en cantidad de palabras, número de caracteres en tokens, lo podés meter en un gráfico, como lo estamos explicando y poner por noticia, por sesgo político o de acuerdo a lo a lo a lo que vos estés trabajando y comunicarlo con con exploración, digamos.

02:20:42

lse posgrados: Yo yo no veo por qué no eh lo podrías aplicar en en tu
Diego Methol: Claro,
lse posgrados: trabajo.
Diego Methol: ahí claro, me tengo que ir más a a tratar de porque yo no yo no empiezo con un juego de datos ya grande, entonces quizás sí es algo que voy es un histórico que voy guardando y después voy agregando un análisis al
lse posgrados: ¿Cuántas Pero,
Diego Methol: histórico,
lse posgrados: ¿cuántas noticias tenés?
Diego Methol: ¿no? A ver, yo me hice el ground tr hice con 20, pero después yo básicamente entro a una web, agarro noticias, se la se la paso y evalúo cómo me la está clasificando. Entonces sí, por eso decía que yo una de las partes que quería hacer era ese histórico. Bueno, teniendo ese histórico, en realidad puedo aplicar ese tipo de visualizaciones de datos porque los tengo guardados.
lse posgrados: lo ideal con tu con tu con tu verdad de campo también lo podrías hacer, digamos, eh, o sea, con eso con ese dataset que tenés, te invito a que a que lo explorés, digamos, digamos,
Diego Methol: Hm.
lse posgrados: e yo lo llevo por ahí al rack porque es lo que la mayoría está aplicando y donde yo lo veo también útil. Eh, yo creo que en el fondo eh el RCK incluso quizás también sea sea una sea un método que vos pueda usar para traer aquellas noticias que tengan tal o cual contenido semántico, digamos.

02:21:55

lse posgrados: Eh, pero yo no veo que no sea aplicable a tu caso. No no no entiendo por qué, digamos, porque ¿por qué no sería aplicable a tu
Diego Methol: No, a ver, eh,
lse posgrados: cas?
Diego Methol: yo no estoy diciendo que no sería aplicable. Claro. Ahora, a ver, habiendo hablado del tema del histórico, sí, ahí sí tiene mucho sentido. Hay un montón de cosas para sacar, por ejemplo, de mismo por medios sacar los distintos egos que hay en un medio,
lse posgrados: Mm.
Diego Methol: pero claro, eso es yendo hacia adelante, o sea, porque porque mi de la manera yo tengo mi ground truth y después siempre utilizo una noticia nueva, ¿de acuerdo?
lse posgrados: Claro.
Diego Methol: Pero claro, almacenando eso, que es parte de lo que yo había planteado como para hacer para esta siguiente fase ese tener ese histórico. Ahí sí, obviamente si tengo el histórico, tengo datos y esos datos obviamente los puedo visualizar de distintas maneras, pero a lo que voy en el single use como quien dice este no no tengo no veía qué hacer por ese lado, pero sí, ahora que decís pensando en guardar los históricos, ahí sí obviamente que tengo un montón de cosas para para poder ver.
lse posgrados: Sí, sí, obviamente va a depender de cada caso.

02:22:57

lse posgrados: Yo lo muestro que lo básicamente son conteo de palabras entre tipos de clase. Son casi todos conteos. Si ya tengo los conteos hechos, a eso le aplico un boxplot o una distribución para ver si me sirven para separar, etcétera. No sé si vos estés trabajando sesgo político, no sé si ponete en noticias o o en Twitter, en comentarios de Twitter, no sé, capaz que los libertarios hacen usan más malas palabras. Bueno, podés contar las malas palabras y y hacer un gráfico, digamos, ¿no? Forma parte de la exploración.
Diego Methol: Muchas gracias.
lse posgrados: Otra otra cuestión que es importante es eh reconocer entidades. Eso es de hecho creo que este digamos lo que lo que lo que puede alimentar o puede generar mucha info eh para después utilizarla, ¿no? Entonces, el reconocimiento de entidades es cuántas ve o o que me detecte el número de decreto, el el ministerio y que vaya y en este caso no solo lo detecta, sino también los cuenta. Sí, en este caso, como dice OP código lo el el el patrón de Rejex lo detectó y y detectó 12, con lo cual está bien porque yo tengo identificado 12 documentos. fecha de publicación van a ser 12 porque obviamente son 12 documentos de nuevo, número de expediente, ese documento está asociado número de expediente, todos distintos, ¿se entiende?

02:24:29

lse posgrados: Entonces también eso forma parte de la exploración. Ahora, esto uno lo puede agregar contándolos así o si le agrego una variable categórica a estas ocurrencias, lo puedo distribuir, ¿sí? por decreto, decisión administrativa o ley. Eh, bueno, ahí yo le puse en la notebook una una métrica, digamos, que se usa. ¿La vieron a esto? Al al a la riqueza léxica. ¿Vieron algo de eso en en procesamiento de lenguaje? Básicamente lo que hace lo que hace esta métrica, digamos, es es contar cuántos token por palabra y y hacer Yo le puse un poquito de teoría ahí eh como para que en la notebook para que entiendan qué es lo que hace, pero en definitiva, en definitiva nos va a permitir conocer o estimar cuál es la cantidad, digamos, eh de tokens para usar en un chunk. Sí. Eh, entonces los invito a que vean esa parte teórica y quizás la clase que viene las traigo las muestro un poco más porque no había preparado para ahora, pero para que puedan entender un poco más esa métrica. Pero sí, la exploración, lo que quiero comunicar es que la exploración nos lleva a a tomar decisiones de modelación. por ejemplo, la cantidad de toxin para hacer el ching, el chalking, digamos.

02:26:09

lse posgrados: Bueno, y por último, eh todo esto todo esto lo que lo que lo que ayuda es a eh que el chanqueado o que el preproceso antes de entrar al al modelo de RAC o o de clasificación o lo que estemos haciendo tenga tenga más sentido. Sí. eh y que yo a esos chank le puede agregar metadata también. Y eso lo lo voy a mostrar ahora. E la notebook también esta está organizada de una forma usando markdown, digamos, está hecha por fases, ¿sí? eh ingresa el documento, etcétera, todo lo que moviste en el gráfico. Pero lo que creo que aporta más valor de todo esto es que al final, bueno, está todo tal cual lo hemos visto hace ratito, al final hay un hay un un reconocimiento de patrones, ¿sí? y esta que es que la parte que dice extracción automática de metadatos es una función para para además de sacar el texto, el que está vinculado extraer los metadatos. Esos metadatos cuando uno los los saca le aporta mucho valor al RAC, porque el RAC no solamente va a ver el documento, sino también va a ver los metadatos. Estoy viendo acá donde tengo el acá está el Jason. Al final, digamos, con ese reconocimiento de eh de entidades, yo puedo generar un un chanking que tenga más información.

02:27:53

lse posgrados: ¿Pueden ver esto? Este, este es un Jason. Entonces, ahora yo tengo el chank. Esto es un chank. Este es un chank. Este es un chank. Este es un chank. Eh, acá hay otro. Sí. No sé si le puedo aumentar el tamaño esto. Creo que no. Eh, no sé si pueden ver bien ahí o o no se ve, ¿no? Lo que contiene.
Gabi Tallarico: o como frases así negritas y blancas y nada
lse posgrados: Claro,
Gabi Tallarico: más.
lse posgrados: estoy tratando de ver cómo le puedo aumentar el tamaño a esto. En edit text, pero bueno, hagámoslo a la simple. Este es un chank para que acá lo voy a
Diego Methol: Vi son incapaz.
lse posgrados: pegar. Lo que lleva toda esa notebook básicamente de reconocer patrones, explorar, etcétera, a que el chank tenga tenga otro sentido y no solamente el chank que hemos visto hasta NLP, que era simplemente tomar un fragmento, dividirlo y tener un overlap. Sí, ahora tenemos un sistema. El sistema, ¿qué dice?

02:29:09

lse posgrados: Bueno, ¿cuál es el el identificador del chan? Este que está acá. Entonces, es un diccionario donde tiene muchos componentes. Uno el identificador. ¿Cuál es el documento asociado a ese chank? La ley, tanto. Sí. ¿Por qué? Porque con regex lo rescaté. Sí. Okay. Eh, ¿qué tipo es ley? Variable categórica. Okay. ¿Qué número? Acá esto es redundante, pero bueno, también se lo se lo puede modificar. Yo yo lo hice con exceso en lugar de con déficit, como para que quede claro cuál es la fecha. Esta es la fecha, bueno, la fecha de publicación, esta es la fecha del decreto y esta es la fecha de publicación. Sí. Eh, o en el Ministerio Gobernación de la provincia de Salta, recién al último aparece texto y este digamos este es el chank, o sea, es decir, no solo, ay, perdón, es decir, cuando yo hago el procesamiento de lenguaje natural y lo que lo que iba con esto es que todo el EDA, todo ese EDA que yo fui rescatando me sirve a mí para para generar un chank más inteligente que pueda alimentar a un retriival, a un sistema o al problema que estemos trabajando de una mejor manera.

02:30:33

lse posgrados: ¿Sí? Entonces, si hubiese yo hecho solamente un chank normal al documento, hubiese aparecido esto nada más. Sí. Ahora el número de token, etcétera, todas estas información extra que yo le saqué al documento para poder o visualizarlo o explorarlo un poco más o con esto alimentar un sistema un sistema RAC. De nuevo, a digamos, desde mi punto de vista, cada uno va a tener un un caso particular con su digamos eh con con su metadata que le aporte información. Mi metadata que me aporta información es la que está puesta acá. Sí. Eh, hay una función que va iterando entre cada documento aplicándole esa extracción. ¿Dónde está esa función? Está acá. Sí, básicamente es reconocimiento de eh de patrones. No hay nada de ll Sí. Eh, fíjense que están los patrones para tiene monto, sino si tiene alguna entidad tributaria, hay un patrón y es usando rejex, digamos. ¿Por qué hago esto? Porque he visto que que como que he notado cuando he visto la notebook como que la solución más simple usar un LLM y no sé si hay alguien que me me pueda decir lo contrario, pero es como que no tengo que reconocer entidades, le mando un LLM y consumo tokens.

02:32:14

lse posgrados: Bueno, obviamente uso lama o uno que no pago, pero por ahí la la solución va en algo que ya van, digamos, es mucho más sencillo en código, es mucho más sencillo en arquitectura, etcétera. Sí, no sé si están están de acuerdo conmigo o seguirían usando seguirían usando Llms.
Diego Methol: Eso es puntual, está pasando hoy en mi trabajo. Una cosa que ya la gente usa tanto ya que hay que cruzar información de dos sistemas
lse posgrados: Yeah.
Diego Methol: internos y y se lo piden a la idea y funciona, pero claro, después se quejan que se quedan sin toques de clas cada rato y bueno, yo justamente estoy trabajando en hacer una cosa que si bien estoy usando ya, pero estoy usando ya para generar los los scripts para cruzar la información y después que sea simplemente en vez de tener que mandar toda la LM que esté horas procesando, le tiras un script, corre en un minuto y ya tiene una información cruzada y después, bueno, si quieren pasar esa información cruzada por un bien para obtener tipo de cosas lo pueden hacer, pero están desperdiciando una cantidad gigante de tokens e una y otra vez repetir los mismos cruces de información entre sistemas cuando en realidad esta información es fija, no no tiene mucho sentido este que pase siempre por un LM.
lse posgrados: Claro. Sí, yo de nuevo a lo lo que lo que trato de hacer no incentivar a no usar el LM, sino que vean y que existe otra herramienta.

02:33:48

lse posgrados: A ver, este código no lo escribí yo letra por letra, le tiré el problema un ll,
Diego Methol: H
lse posgrados: le expliqué qué es lo que quería hacerme data usando y traeme metadata utilizando rejex. Eh, interpretar qué metadata me puede servir para cada problema. No, no hay no hay no más que asignarle un rol y definirle un contexto. Lo mismo que ya saben hacer, digamos, usando el LM y el código lo resolvió solo. ¿Sí? Eh, entonces lo lo importante de esto es que, digamos, y creo que la ventaja es que yo ya no tengo que sentarme a escribir la cuál cuál sería el patrón
Marcelo Luna: Ô
lse posgrados: rejex para encontrar si es sanción, multa o apercebimiento. Sí. Eh, acá hay una función donde dice, bueno, eh, va a ser una variable tipo buliana, donde encuentre este patrón y sea true, le va a poner uno, ¿sí? O sí tiene sanción, sí. Eh, tiene retiro porque había muchos retiros voluntarios. Sí, tiene afectación. Bueno, la fecha lo mismo, busca patrones, digamos, ¿no? Eh, tiene artículo, lo mismo. Son todos patrones regex que van iterando documento por documento y que al final entregan una estructura.

02:35:04

lse posgrados: Creo que lo que aporta más valor esto es una estructura más ordenada de lo del de lo que contiene este texto para que cuando yo haga un retrival, cuando yo haga el rag o lo que sea, pueda usar la información de la metadata, además de la que tiene de la que tiene el propio chank. ¿Se entienden? ¿Tienen alguna alguna duda?
Marcelo Luna: M.
lse posgrados: ¿Quieren que sea más específico en en algo? Bueno, y cuando corran esto que está acá hasta el final, creo que si no sé si está el esto se corre así. Bueno, esto lo descargo. Sé si puedo descargarlo de acá o de acá. Una vez descargado, sí, voy a la notebook. Esto ya lo saben hacer seguro, pero por si acaso no está mal explicarlo. Voy y lo subo acá. Sí, una vez que lo subo al documento, hay una parte en el al principio aquí donde lo llamo. Sí, donde don ¿Dónde está el pad? Este pad está acá. Entonces ahora simplemente ejecutan todo y van viendo parte por parte. Eh, no me interesa que sepan todo lo que hace.

02:36:51

lse posgrados: Sí, me interesa que entiendan que sus sus PDFs o sus documentos en texto tienen más info que solo el texto plano que venían trabajando. Eso eso es lo que me gustaría que le quede de la clase. Si ah obviamente los casos particulares eh me lo pueden comentar ahora o me lo me lo pueden mandar un correo para ver qué conviene extraer y qué no y cómo se lo puede relacionar o no. Ahí los los puedo ayudar, digamos. Eh, pero no no me interesa que aprendan y que sepan que hace tal tal todo esto del código, simplemente que interpreten el gráfico y que después con sus textos puedan llegar a aplicarlo en en sus trabajos. Al final, al final, al final lo que hace es descarga un Jason. Al final, al último, por eso lo corri de nuevo para que vean. Al final lo que hace es eh genera todos los los chanks, ¿sí? y exporta eh ese ese Jason que es el que abrí. Ya. Entonces, cuando cuando genere ese Jason, le ponen acá descargar y acá cuando se le abra eh esto ya directamente eh pueden ayudo abrir con esto. abro con yo, en mi caso lo abro con eh bueno, hablo con un bloc de nota, pero yo lo hablo con un editor de texto que tengo de que funciona el Mark sublime, pero bueno, como vimos recién, no se no se no se llega a apreciar toda la todas las cosas que tiene.

02:38:37

lse posgrados: Y esto no sé si tiene zoom acá, ¿no? Uno nuevo.
Shimon Ben: en
lse posgrados: View view vi hide focus indection syntax.
Shimon Ben: vivo.
lse posgrados: Como esto es texto plano, full screen. Ah, hace lo mismo. No, no sé si como este es texto plano, no, no sé si lo hace. Por eso le tomé un chank y lo pegué ahí para que vean que es un diccionario. Eh, ahora en el ratito que
J.Pablo Zebraitis: Tal vez, tal vez con Visual Studio se te ve mejor,
lse posgrados: me
J.Pablo Zebraitis: puedes formatearlo. Es un Jason.
lse posgrados: s un Visual Studio. A ver,
Marcelo Luna: con algún con algún editor de Jason específicamente.
J.Pablo Zebraitis: ¿Por
lse posgrados: tengo algún editor dando vuelta también. Esp ahí. Veamos si lo puedo ver.
Marcelo Luna: Ok.
J.Pablo Zebraitis: qué es un directamente?
lse posgrados: Ahí. Bueno, sí, cada chonk tiene una idea, pero esto lo que se vae es super largo, pero no tengo la librería esta para ver. Yo creo que lo que importa acá es que pueden pueden sacarle más info al a sus textos.

02:40:01

lse posgrados: Para eso, antes que termine la clase, sí, digamos, me gustaría mostrarle este sistemita, pero primero quiero saber si si fue claro, qué dudas tienen, si quieren que que algunas acercamientas a sus a sus proyectos particulares o un sistema que que que usa metadatos, digamos. Sí, Simón.
Shimon Ben: No, yo lo tengo que revisar un poco todo esto. Pero si, por ejemplo, te mandé por mail las dos posibilidades que tengo para analizar sentimiento, porque la empecé a encontrar cosas, digamos, eh, de, o sea, para saber por dónde encaro, digamos, yo con estos recursos empiezo a investigar,
lse posgrados: Vos te refieras a los modelos a
Shimon Ben: pero no,
lse posgrados: usar.
Shimon Ben: a ver, eh, tengo dos maneras de encarar el trabajo, porque yo puse, por ejemplo, modelo de sentimiento Algunos te los puse ahí en el en el colab que te
lse posgrados: Sí,
Shimon Ben: mandé y sobre tres chances que era positivo,
lse posgrados: sí.
Shimon Ben: negativo, neutro, eh después empecé a encontrar que hay como burda, ironía y un montón de cosas más que hay otro modelo que me me lo daba este que encontré en Hing Face y bueno, quería ver si de repente se me se me se me va el trabajo de repente de control con esa segunda posibilidad y sigo con la primera que es positivo, negativo, neutro o por ahí sí vale avanzar por el otro lado y irme más posibilidades.

02:41:36

lse posgrados: O sea, vos querés aumentar complejidad en tu clasificación.
Shimon Ben: Claro, pero si si esa complejidad no es un riesgo que no
lse posgrados: Yo si vos tenés, mira, si si ese documento, digamos, si ese modelo es transformer de Hang face eh está documentado,
Shimon Ben: se
lse posgrados: o sea, tiene experiencia, tener, digamos, se ha usado y funciona y en tu y en tu verdad de campo aplica, dale. O sea, anda por ahí. Sí.
Shimon Ben: o menos. Yo los estuve viendo haciendo check manual y qué sé yo,
lse posgrados: Sí.
Shimon Ben: no sé por ahí si una ojeada este ver si de repente vale la pena o no arriesgar ahí porque es una disyuntiva para mí ahí la verdad porque me da mucho más seguridad el que menos resultados me me ofrece pero en definitiva si yo tengo que hacer un gráfico de eso, tampoco le estoy diciendo ninguna verdad que lo está viendo.
lse posgrados: Pero qué complejidad sería hacer los dos y
Shimon Ben: es positivo.
lse posgrados: compararlos,
Shimon Ben: Hm.
lse posgrados: digamos, en en complejidad,
Shimon Ben: No,
lse posgrados: no no tenés tanta complejidad en digamos ya tenés uno desarrollado, sumas Otro más y a los resultados los
Shimon Ben: no.

02:42:54

Shimon Ben: Lo que pasa que cuando voy chequeando los resultados se hace bastante largo,
lse posgrados: comparás.
Shimon Ben: más que nada. Eh,
lse posgrados: Ah,
Shimon Ben: si to que si por ejemplo yo empiezo a hacerlo a verlo manual y si quiero por
lse posgrados: ok.
Shimon Ben: por en 20 datos, bueno, 20 comentarios, no pasa nada, 50 y yo la idea es hacer mayor cantidad de comentarios para hacer un baje más extenso y ahí este bueno, se me va bastante bastante tiempo. una tarde larga viendo, tratando de comparar y al principio no estaba conforme con el de me daba positivo, negativo, neutro y después cuando empecé al de cinco posibilidades o más ya era bastante más ambiguo y también depende del
lse posgrados: Claro. Entonces yo yo lugar yo iría con el primero y después,
Shimon Ben: de
lse posgrados: o sea, positivo, negativo, neutro y quédate ahí, quédate
Shimon Ben: Pero a ver, positivo, negativo,
lse posgrados: ahí.
Shimon Ben: neutro funciona más como estructura para el trabajo como tarea acá, pero pero con no es muy inspirador tampoco si yo teo mostrar, mira, eh, los comentarios de los usuarios dieron esto y es medio mentiroso porque en realidad los comentarios son burla ironía, por eso no una
lse posgrados: Sí, pero si el modelo, digamos,

02:44:03

Shimon Ben: vuelta.
lse posgrados: si si te de poner el tradeof, digamos, ¿no? Si si a vos ese modelo te tiene incertidumbre y etcétera, por más que tenga más categorías, tiene mucha incertidumbre, no tiene mucho sentido, digamos. Yo yoía por el positivo, negativo, neutro y después lo escalas. Sí, después lo digamos estas cosas sirven para eso.
Shimon Ben: No.
lse posgrados: O sea, ahora ahora les voy a mostrar un ejemplo, pero cuando uno hace esto para un para un boletín oficial, en este caso un boletín oficial, lo mismo así ese esa maqueta con con eso funciona para todos, digamos. Entonces, eh yo yo diría que te quedes con eso y después lo que cambia el transformer o cómo lo ajustaste o cómo o más tiempo, digamos, de procesamiento manual para la para ver qué tan bueno es, pero después en la metodología es la misma.
Shimon Ben: Los dos me producen disconformidad, digamos, pero
lse posgrados: Es que ningún modelo te va a dar 100% conformidad.
Shimon Ben: por
lse posgrados: No existe. No, no todo
Shimon Ben: a ver si la finalidad es mostrar un resultado a alguien en un gráfico, por ejemplo, A ver,
lse posgrados: va

02:45:12

Shimon Ben: la mayoría de los de los comentarios son negativos y no son qué s yo, habría que establecer que es negativo para yo tendría que dar encontrar una vuelta para ahí si ironía es negativo o si es burla negativo o no
lse posgrados: por qué no y por qué no lo no lo hac al revés.
Shimon Ben: sé.
lse posgrados: Primero clasificar en tres categorías y después dentro de cada categoría poner el otro modelo. Entonces, ya primero sacar uno encima y el otro modelo se lo pasa al otro que ya está clasificado, ¿me entendés?
Shimon Ben: como el neutro o u otro sería la consideración y ahí clasificarlos.
lse posgrados: Claro. Y ahí tenés dos categorías. Primero, la primera, el primer modelo que usas y a cada categoría de ese resultado que son tres, le aplicas el otro modelo. Sí. Y ahí tenés como lo anidas y decir, "Bueno, y ahí podés hacer ahí podés decir, bueno, cuando son negativos, la mayoría son ironía, ponete,
Shimon Ben: Okay,
lse posgrados: ¿entendés? Ah,
Shimon Ben: okay,
lse posgrados: me parece que por ahí puede venir.
Shimon Ben: okay. Gracias.
lse posgrados: Bueno, ahora le voy a mostrar un un es un trabajo final y que que realicé realizamos con unos compañeros en la especialización para para procesamiento de lenguaje natural tres.

02:46:35

lse posgrados: O sea, en en la ESP de la FIUVA hay tres procesamientos de lenguaje natural. El primero para ver lo que ustedes ya vieron, TF y DF, similaridad, etcétera, no llegamos a ver el LM. El segundo es más bien entender transformer y casi todo el LNP2 es transformers, eh, y el tercero es casi todo RACK, digamos, distintas formas de hacer RAC, etcétera, etcétera, digamos. Entonces, para probar el tercer eh el tercer NLP de de la maestría en inteligencia artificial, había que hacer un sistema, un pipeline casi en producción, digamos, ¿no? Obviamente hay mucho código atrás, pero no me interesa que aprendan el código, sino más bien el flujo de datos que una parte y el resultado que aporta si uno le hace caso a las reglas estas de e encontrar patrones, sacar metadatos, etcétera, etcétera. Sí. Bueno, el flujo empieza con una arquitectura que se llama con un framework de trabajo llama airflow. Airflow, no. Imaginemos que Airflow son cada celda de cada celda de de colab es una tarea en en airflow que están anidadas. Cuando uno pone run al en o correr todo en colab va corriendo una tras de otra.

02:47:57

lse posgrados: Entonces, si lo que sale de una entra en la otra y está anidado, están relacionado, no va a haber problemas, ¿no? Pero si si hay problema se va a suspender. Bueno, Airflow hace lo mismo. Airflow es una sucesión de tareas que tiene el sistema, que un pipeline, que en definitiva lo que hace es eh lo que hace el colab, digamos, pero separado en tareas. Por eso es importante que cuando ustedes desarrollen y y vayan generando sus funciones, no le pidan que haga todo una sola vez en una sola función. Okay, una función para sacar encabezado. Okay, listo. Eso me genera algo. Ah, después a ese encabezado, le voy a sacar eh las mayúsculas. Listo, le saco las mayúsculas y así ir encadenando parte por parte porque le da trazabilidad lo que vas haciendo y entendés lo que vas haciendo. Sí. También he visto casos en los cual hay una función así gigante donde entra y ya sale el chunk, digamos, ¿no? La hace todo. No es lo recomendable y no es lo que espero. Lo que espero es que a raíz de lo que hemos visto, eh, traten de separar las cosas pasito a pasito.

02:49:08

lse posgrados: ¿Por qué? porque después lo va a hacer más escalable y le va a permitir hacer eh corrección de errores mucho más sencilla. En definitiva, lo que hace lo que hace un pipeline, digamos, este pipeline tiene una función que lo que lo que hace básicamente la primer parte de la esta este pedacito del bloque es descargar los boletines oficiales. O sea, primero descarga, es decir, se conecta a internet, uso una función de webscrapping y descarga los boletines. ¿Sí? Entonces, ¿qué es lo que me entrega? ¿Qué es lo que entra acá? Una URL o una serie de URL, en realad una fecha, un rango de fechas en los cuales me descarga todos los btines de esa fecha. ¿Y qué es lo que entrega? Eso también es importante, que cuando una función hace algo, de alguna forma al final de la función debería explícitamente decir qué hizo. Sí, en este caso esa función descargó y me tiró un logo, o sea, me informó, me dijo, "Mira, encontramos este boletín oficial y este boletín oficial, dos boletines oficiales." Y esos dos boletines oficiales fueron eh guardados en un en un determinado lugar.

02:50:27

lse posgrados: ¿En qué lugar? En la nube. Imaginemos que lo guardamos nuestro drive para no usarlo en local. En este caso, esto está conectado a un sistema que se llama Minio. Minio es un backet, es como un un sistema de almacenamiento, reemplaza un sistema de almacenamiento eh en la nube, como puede ser cualquiera de lo que Amazon, no sé, hay un montón, digamos, ¿no? Ahí esto tiene, esto se llama lógica de microservicios admin. Sí. Entonces, cada uno de esos boletines está descargado en un lugar y está puesto imaginémoslo, en un disco. ¿Sí? Entonces, cuando vengo acá, vengo 2025, hay dos boletines. ¿Qué contiene cada boletín? Lo puedo lo puedo descargar. Lo vemos. el boletín completo, el boletín oficial completo, no es la parte, nosotros hemos trabajado con la parte que está dentro, pero esto tiene encabezado. Bueno, acá hay como más funciona de limpieza. Bueno, okay, descarga. Entonces, la primer el primer pasito descarga el boletín oficial. El segundo paso es un poco lo que hemos visto hoy, lo que hace extrae los documentos por OP.

02:51:52

lse posgrados: Entonces, ¿qué entra? Entran los PDF. ¿Y qué salen? los documentos. Entonces, lo que va haciendo es generando un txt por cada documento que encontró. ¿Y dónde lo va a guardar? que nosotros hicimos el respaldo. Va ir de nuevo minion acá y acá va a ir guardando cada uno de los boletines. O sea, como esto es parte del rack en eh en text por cada documento que encontró. Sí, no estoy trabajando con una tabla, yo estoy trabajando con txt. Entonces, por ejemplo, si abro este TQT, es el cuerpo del texto que encontró ahí adentro, ya limpio, digamos. ¿Sí? Entonces, de nuevo, ustedes van a trabajar con van a trabajar con con Colab. Pueden usar el sistema de almacenamiento que tiene Colab para ir guardando ahí los TXT o hacer una tabla y después guardar la tabla. da da como que eso ya queda como a criterio. importante, creo que sí da eh digamos da respaldo y y como como y eh trazabilidad es tener estos TXT para que después uno entre y diga, bueno, a ver, que el OP con identificador 427, bueno, realmente el RAC me está devolviendo lo que encontró o me está mandando verdura, digamos, Pablo

02:53:24

J.Pablo Zebraitis: Profe, ¿podemos trabajarlo en local en vez de de la nueve?
lse posgrados: Sí, trabal como como
J.Pablo Zebraitis: No,
lse posgrados: ustedes.
J.Pablo Zebraitis: porque yo estoy haciendo una ingesta de los casos de soporte, te acordas que es es el tema mío.
lse posgrados: Sí.
J.Pablo Zebraitis: Estoy haciendo una ingesta mucho mayor a las que ya tenía este a través de chupar la información de Redmine, o sea, de las issas existentes para tener un corpus más grande y poder aplicar esto que tú estás planteando, No.
lse posgrados: Sí, úsalo en el local, o sea, esto reemplaza el local porque en nuestra lógica en aquel momento teníamos que usar microservicios, digamos, ¿no? Como para acercarnos más a un entorno de de digamos de operación.
J.Pablo Zebraitis: O sea, yo estaba hablando solamente para la hora el análisis que tengo que hacer para antes de la clase Yes.
lse posgrados: Sí, sí, sí. local, local viene bien. Ahora, ¿cuál es el propósito de de que yo le muestre esto? Yo le quiero mostrar que cuando uno hace ese trabajo, después lo puede poner en producción, digamos. De hecho, así funciona el sistema.

02:54:21

lse posgrados: Obviamente esto es una maqueta de producción, no es lo que operaría, pero sería muy parecido a esto. Sí, Marc.
Marcelo Luna: No, te iba a preguntar, eh, esos TXT eh, son lo que lo que forma tu rag en particular o los o los meten en algún otro tipo de soporte persistente.
lse posgrados: No, esto persiste, digamos,
Marcelo Luna: Okay.
lse posgrados: persistente es esto que vos ves acá.
Marcelo Luna: Los mismos archivos.
lse posgrados: ese persistente. Exacto.
Marcelo Luna: Okay.
lse posgrados: O sea,
Marcelo Luna: Okay.
lse posgrados: no no lo digamos cuando yo consulto después lo que hago al al
Marcelo Luna: Sí.
lse posgrados: final es enviar a la base de datos vectorial todo ese chank con los metadatos. Entonces, digamos, si vos tenés tu pipeline, eh, tu pipeline debería quedar así, mira, para que lo entend. Sí, mira, buena buena la pregunta. Nosotros tenemos una tarea, tenemos primero en la en internet, en la nube. Sí. Entonces, la tarea lo que hace es descarga el boletín.
Marcelo Luna: Sí.
lse posgrados: Lo pone en un PDF, en un respaldo. Sí, PDF.
Marcelo Luna: Sí,
lse posgrados: Otra tarea, lo que hace es toma ese PDF,

02:55:45

Marcelo Luna: lo analiza.
lse posgrados: lo analiza y se para en TXT.
Marcelo Luna: Sí, correcto.
lse posgrados: Genera n cantidad de documentos que en nuestro caso del eran 12,
Marcelo Luna: Okay. Okay.
lse posgrados: pero son mucho más porque son dos boletines. Entonces, genero el TXT desde el 1 hasta el N.
Marcelo Luna: Con todos los metadatos, con toda la información.
lse posgrados: En este caso el TXT crudo,
Marcelo Luna: Bueno, okay.
lse posgrados: la siguiente función va a tomar cada uno de los TXT y va
Marcelo Luna: Ah, y te lo Sí.
lse posgrados: y va y así lo va anilando, ¿me entendés?
Marcelo Luna: Sí. Okay.
lse posgrados: Ahora la siguiente y lo bueno es que así tiene trazabilidad y vas viendo qué es lo que va haciendo. La segunda función lo que hace
Marcelo Luna: Mhm.
lse posgrados: es, okay, a cada uno, a cada txtica y le saca metadatos. O sea, acá cuando veo el log de esa función va a ir documento por documento
Marcelo Luna: Okay.
lse posgrados: y acá sí yo usé el LM error, digamos. que podría haber usado R,
Marcelo Luna: Hm.
lse posgrados: pero esto sí está haciendo el LM y para procesar estos dos documentos me costó $10,

02:56:46

Marcelo Luna: Okay.
lse posgrados: por ejemplo.
Marcelo Luna: Hm.
lse posgrados: Sí, lo hice ayer y me costó $10 porque se me venció el free y pagué $10.
Marcelo Luna: Sí. Okay.
lse posgrados: Entonces tiene su costo al final, fíjate que dice, mira,
Marcelo Luna: Okay.
lse posgrados: son eh 209 y quedaron guardados acá.
Marcelo Luna: Mm.
lse posgrados: Sí.
Marcelo Luna: Sí,
lse posgrados: Ahora, ahora,
Marcelo Luna: sí.
lse posgrados: ¿qué quedó de este classify? Bueno, vamos acá. Y nos vemos de nuevo en text opadatos,
Marcelo Luna: Es
lse posgrados: este ya trae exactamente el mismo documento.
Marcelo Luna: sí,
lse posgrados: Sí,
Marcelo Luna: pero en
lse posgrados: en un Jason. Exacto. Donde dice, "Bueno,
Marcelo Luna: Jason.
lse posgrados: acá está todo el texto, digamos, hay un resumen, el texto, etcétera." Entonces, lo que va haciendo es saca los metadatos y trae el texto. ¿Sí? Entonces,
Marcelo Luna: Okay.
lse posgrados: de esa forma te va quedando respaldado cada partecita por uno por cada documento,
Marcelo Luna: H
lse posgrados: pero después necesitas unirlo porque después, claro,

02:57:52

Marcelo Luna: claro.
lse posgrados: después tenes que tener un solo Jason para mandar a base de datos. Bueno, eso es lo que hace la próxima función de nuevo. A ver,
Marcelo Luna: H ese.
lse posgrados: todo esto lo puede poner una sola función y sí lo va a hacer, pero no es la idea.
Marcelo Luna: H.
lse posgrados: Después lo el que sigue lo que hace es genera los chank. Entonces, toma el texto, toma los metadatos y genera el chan. Con lo cual, si el documento es muy grande, va a haber metadatos repetidos,
Marcelo Luna: Ok.
lse posgrados: porque un documento se puede dividir en dos partes, por ejemplo, y va a haber metadata, pero cuando consulte semánticamente también va a traer la metadata. Y de nuevo, con la misma lógica, con la misma lógica podemos eh lo lo buscas lo guardé en un chank. Sí, o sea,
Marcelo Luna: Sí,
lse posgrados: en un Pero ahora,
Marcelo Luna: pero pero siempre lo guarda como Jason.
lse posgrados: claro, pero ahora es un Jason por cada documento oficial, o sea,
Marcelo Luna: Eh,
lse posgrados: nosotros hemos abierto un montón y después hemos hemos vuelto a agregar.
Marcelo Luna: correcto. Sí,
lse posgrados: Sí,
Marcelo Luna: lo enriqueciste y después lo metiste de vuelta todo.

02:58:56

Marcelo Luna: Compusiste de vuelta el el documento original,
lse posgrados: exacto.
Marcelo Luna: pero con el agregado.
lse posgrados: Entonces, este es lo que queda,
Marcelo Luna: Eh,
lse posgrados: un solo un cada un Jason por cada eh boletín oficial con los chan y los metadatos.
Marcelo Luna: ok.
lse posgrados: Y eso es lo que va después a la base de alto vectorial. Acá está el este, después le comparto los repositorios si lo clonan. Pero entonces lo que hace es la limpieza,
Marcelo Luna: Hm.
lse posgrados: el chanqueado, etcétera. Traigo los metadatos y ahora mando todo eso a una base de datos vectorial que es como la que ustedes vieron,
Marcelo Luna: Okay.
lse posgrados: nada más que yo usé otra llama Pinecon. Él en base básicamente lo mismo.
Marcelo Luna: Sí.
lse posgrados: Es un espacio de característica donde le mandamos los datos.
Marcelo Luna: Eh,
lse posgrados: Ahora, la digamos el rack tiene eh distintas fases. Lo que se llama la ingesta está puesta así hasta la base de datos. Ahora lo lo que sigue dentro del del Peline es
Marcelo Luna: Hm.
lse posgrados: bueno, subirlo a Pincon, que es este que se ve acá, digamos, subir el documento Python y a la vez crear un índice por BM25.

03:00:04

lse posgrados: Ahí la la Gabi consultó,
Marcelo Luna: H.
lse posgrados: me puso un comentario sobre M25. M25 es un modelo, ¿sí?, que lo que hace es a todos tus documentos o tus chanks indexarlo por no por semántica, sino por léxica, por Entonces,
Marcelo Luna: Sí,
lse posgrados: es como básicamente como apretar un control F o control V y buscar palabra.
Marcelo Luna: sí, sí.
lse posgrados: Entonces, de nuevo, yo puedo tener una búsqueda por LM o una búsqueda por palabra.
Marcelo Luna: H
lse posgrados: cuando haga mial y la que me dé mejor y sea más barata es la que va la que va a formar la respuesta. En definitiva, el el esta parte de ingesta termina eh esta parte de ingesta termina cuando todo el los chan con los metadatos están en la base de dato vectorial. Sí, esa parte ingesta termina ahí y ya está listo.
Marcelo Luna: Sí, sí.
lse posgrados: Parte terminó acá. Ahora lo que falta es cómo la voy a consultar. Se ahora, ¿cómo traigo? Bueno, ahí es donde viene dos dos partes que dos partes.
Marcelo Luna: Mhm.
lse posgrados: Una parte que tiene que ver con AP, la AP, un intermediario en donde el frontend le va a preguntar la PA y la PA va a traducir eso a una pregunta, ta ta ta.

03:01:24

lse posgrados: Va a buscar por similitud y yo configuro el API como yo como yo considero. ¿Sí? Entonces esto tiene implementada una Pay. Entonces, por eso es como también era con la lógica de microservicio y así funcionaba, digamos. Entonces, en definitiva, una vez que tengo la la parte más difícil de la ingesta,
Marcelo Luna: Yeah.
lse posgrados: porque en la ingesta vos tenés que extraer toda la información que podés de contenido léxico y semántico para que después
Marcelo Luna: Hm
lse posgrados: vaya a la base de datos vectorial y cuando yo haga la pregunta no solo se alimente de el contenido semántico con el chank, básicamente, sino también de los metadatos. Sí. Entonces,
Marcelo Luna: hm.
lse posgrados: ahora cuando uno le cuando vos preguntas acá, bueno, ¿qué adjudicaciones simples hay? Me tira directamente eh una respuesta validada, digamos, con con mucho más certeza sin que si no tuviese los metadatos. En este caso, si no sé,
Marcelo Luna: Hm.
lse posgrados: por preguntar si esta persona o o si hay alguna persona o si esta empresa se la nombra en algún boletín, por ejemplo, ¿no? Entonces yo puedo preguntar acá si es es nombrada en en o en qué documentos es nombrada Carachi Viviana.

03:02:44

lse posgrados: Y le hagamos la pregunta. A ver, esto está conectado a a con con con la P de de Open AI, digamos. Sí. Eh, entonces cada consulta tiene un costo.
Marcelo Luna: Hm.
lse posgrados: ¿Qué documento de nombrada? Dice, no es no es especificada la fuente. Evidentemente me lo debería nombrar. Obviamente parece que no esta esta consulta no la tomó del todo bien. Capaz que porque hay un enter. A ver. porque me debería nombrar el documento exacto donde se la nombró, digamos, ¿no? Eso es lo que me debería traer, digamos, respuesta generada.
J.Pablo Zebraitis: Profe,
lse posgrados: Sí,
J.Pablo Zebraitis: ¿cuál fue el en qué está hecho esta esta interfaz? Tú lo mencionaste recién algo?
lse posgrados: esto es eh esto es Streamlit.
J.Pablo Zebraitis: Gracias. Yeah.
lse posgrados: St debe ser s sencillo de usar, digamos. O bueno, evidentemente no está tomando el documento y capaz que tiene algún error, pero eh qué decisiones en el texto. Ojo,
Marcelo Luna: Hm.
lse posgrados: se me puede haber roto porque hace lo hace mucho no lo uso.

03:04:11

lse posgrados: Bueno, eh si quieren hacemos un repaso. ¿Tienen alguna duda? Eh capaz, no sé si fue mucho para una sola clase.
Marcelo Luna: No,
lse posgrados: Necesito feedback.
Marcelo Luna: yo en en mi caso necesito volver y revisar algunas cosas del trabajo, eh, pero por ahí esto una propuesta, pero por ahí sí creo que me a mí en particular, me sería útil tener aunque sea unos minutos de cada clase en donde podamos hacer consultas, cada cual algunas consultas en particular. Ahora, esto que te pregunté, me aclaraste varias cosas porque yo tengo que revisar toda la parte de la ingesta de eh de MIT TP para incorporar toda la parte de las expresiones regulares y
Shimon Ben: Ok.
Marcelo Luna: demás y estoy ahí con algunas dudas de qué tecnología me conviene usar o no. Eh, pero bueno, no sé, digo, clase a clase me van surgiendo también algunas cosas como para revisar.
lse posgrados: Claro. Bueno, yo yo tengo esa clase de comodín, digamos, que era la de aspectos éticos, que la se la puedo usar si quieren la clase que viene,
Marcelo Luna: H
lse posgrados: la próxima clase hacemos una primera un primer review para ver eh todos los que quieran exponer sus casos, eh canvas más visualización, pero traigan traigan traigan casos, digamos, ¿no?
Marcelo Luna: esto esto es mi necesidad.

03:05:44

Marcelo Luna: también este por ahí el resto del grupo tiene tiene una opinión diferente.
lse posgrados: Yo creo que todos están en la misma porque porque yo creo que a todos le viene bien un centro entre comillas. Bueno,
Marcelo Luna: Anton.
lse posgrados: visualiza esto en cara por acá, encara por allá. Me parece que ahí está también un poco del
Shimon Ben: Sí, por ahí yo pienso en relación a lo que dice Marcelo,
lse posgrados: valor.
Shimon Ben: acortar un poco la parte teórica ir robándole minutos a esa clase que te
Marcelo Luna: H.
Shimon Ben: comodín de repente para para no sé tener media hora en final de cada clase para hacer preguntas puntuales de cada trabajo y después en todo caso que esa clase de comodín sea
lse posgrados: Claro.
Shimon Ben: para este ir armando todo lo que no se alcanzó en todas las clases.
Marcelo Luna: H
lse posgrados: Me parece bien. Yo creo que la próxima clase voy a dar una breve introducción, muy breve, y después usamos más tiempo para ver caso a caso, porque digamos, mi propósito con las dos primeras clases es eh primero que definan bien el problema, acoten esto y que usen el EDA para enriquecer lo que ya hicieron, porque gran parte de lo que ya hicieron eh lo presentaron en la materia anterior,
Shimon Ben: H
lse posgrados: digamos, ¿no?
Marcelo Luna: No.
lse posgrados: por lo que vi, por lo que me mandaron, casi todo, digamos, el 80% de todo lo desarrollado ya está ahí.
Shimon Ben: Igual
lse posgrados: Sí. Entonces, creo que creo que hay que mi mi valor aportaría en el uno a uno. Entonces, eh, bueno, eso y bueno, gracias por los que se quedaron un ratito más. Yo estoy en el correo, te voy a responder hoy, Shimon Shimon, sorry, y pero trato de trato de responder días antes de la clase,
Shimon Ben: igual
lse posgrados: como para que no quede frío, porque si no después respondo y queda frío y seguramente los que me escriban hoy sobre estos temas responderé lunes, martes, la semana que viene.
Shimon Ben: Bien. Okay, gracias.
lse posgrados: Bueno, meta. Gracias, chicos.
Shimon Ben: Bueno, hasta luego.
Marcelo Luna: Gracias.
Diego Methol: Muchas gracias.
lse posgrados: Ahí lo paso. Ahí paso la librería, Gabi. Ahí pasó la librería.
Gabi Tallarico: Okay. Saluditos a la semana que viene.
Marcelo Luna: Buena semana.
Gabi Tallarico: Perfecto.

La transcripción finalizó después de 07:31:56

Esta transcripción editable se ha generado por ordenador y puede contener errores. Los usuarios también pueden cambiar el texto después de que se haya generado.

