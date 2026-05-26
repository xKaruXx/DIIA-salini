# Taller de trabajo final (1_8) - d015b25_ 2026_04_29 18_38 GMT-03_00 - Notas de Gemini

- Fuente: `Taller de trabajo final (1_8) - d015b25_ 2026_04_29 18_38 GMT-03_00 - Notas de Gemini.docx`
- Tipo: DOCX
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

📝 Las notas

abr 29, 2026

Taller de trabajo final (1/8) - d015b25

Invitado salinastalamilla@gmail.com Taller de trabajo final - DIIAA 1Co2025

Archivos adjuntos Taller de trabajo final (1/8) - d015b25

Registros de la reunión Transcripción Grabación

Resumen

La clase estructuró proyectos individuales mediante el uso de herramientas de diseño Canvas y metodología técnica.

Metodología del curso
El curso se organiza en 8 sesiones enfocadas en la arquitectura conceptual y la implementación de sistemas mediante el uso de herramientas como el Canvas de proyectos.

Revisión de proyectos
Se evaluaron diversas propuestas de inteligencia artificial donde se acordó acotar el alcance de los desarrollos para asegurar entregables escalables y medibles. Se enfatizó la importancia de la calidad en la documentación y la definición de una arquitectura clara sobre la ejecución técnica pura.

Tareas de implementación
Los participantes deben preparar sus datos para la exploración en la próxima clase y compartir sus borradores de Canvas para recibir retroalimentación. Se priorizará el análisis de métricas y la estructura de los sistemas RAG.

Próximos pasos

[lse posgrados] Conversar Proyecto: Conversar con la persona responsable del proyecto de visión por computadora. Convencer para enfocar la solución en LLM.

[J.Pablo Zebraitis] Configurar Repositorio: Poner repositorio de GitHub en modo privado. Compartir acceso como visor o comentarista a lse posgrados.

[Carlos Salini] Configurar Repositorio: Poner repositorio de código en modo privado. Compartir acceso con lse posgrados.

[lse posgrados] Preparar Ejemplo: Traer ejemplo sencillo sobre transformers y embeddings para la próxima clase.

[El grupo] Conectar API: Intentar conectarse a una API key de modelos LLM más grandes.

[lse posgrados] Enviar Material: Enviar material sobre las métricas utilizadas en los sistemas RAG.

[Aquellos que no tengan proyecto] Iniciar Proyecto: Avisar al profesor para recibir el enlace del PDF del Boletín Oficial. Empezar a trabajar en un sistema RAG.

[El grupo] Entregar Canvas: Entregar el canvas de proyecto completo y desarrollado antes de la próxima clase.

[J.Pablo Zebraitis] Completar Canvas: Completar el canvas de proyecto hasta el alcance definido. El alcance debe cubrir ingesta, procesamiento de imagen a JSON y clasificación.

[Fabrizio De Luca] Documentar Avance: Poner en un documento la justificación del proyecto, la detección del bounding box y la aplicación de YOLO.

[Fabrizio De Luca] Compartir Demo: Enviar el video o la demostración del trabajo actual por correo a lse posgrados.

[Shimon Achtung] Preparar Dataset: Preparar tabla para exploración del dataset en la próxima clase, incluyendo URL, comentarios, clasificación y dimensión embedding. Automatizar el pipeline para extraer comentarios de 10 videos de distintas temáticas.

[Marcelo Luna] Mejorar RAG: Modificar el sistema RAG para incluir una ventana visual que muestre los documentos de reglas recuperados. Esto permite explorar qué documentos se están usando antes de generar la respuesta final.

[Gabi Tallarico] Convertir Tablas: Encontrar método automático (LM/rejex) para transformar tablas PDF a formato JSON. Si son pocos documentos, realizar la conversión manualmente.

[lse posgrados] Enviar Métricas: Enviar métricas RAC a los estudiantes esta semana. Mostrar un ejemplo de RAC con métricas la próxima clase.

[juan ignacio sinopoli] Generar Datos: Usar un prompt para generar 100 o 200 datos sintéticos de mensajes de usuarios.

[Lorna Pons] Probar Fórmulas: Probar con fórmulas y resoluciones matemáticas durante la semana. Si la medición es complicada, pivotar al análisis de texto.

[El grupo] Compartir Canvas: Compartir el PDF o documento Word del canvas del proyecto por correo electrónico.

[El grupo] Preparar Dataset: Crear datasets, tablas y archivos TXT con lógica de chunk para la exploración de datos. Traer Colabs para revisar los textos y la ingesta la próxima clase.

Detalles

Consulta sobre disponibilidad en el curso y coordinación de proyectos: Carlos Salini planteó una preocupación sobre su disponibilidad, ya que solo podía asistir aproximadamente la primera hora de la clase los miércoles y debía retirarse antes de las 7:40 p.m. debido a otra reunión (00:00:00). lse posgrados propuso iniciar la revisión de proyectos con Carlos Salini rápidamente durante los primeros 30 minutos de clase, asegurando al menos 15 minutos de atención individual, y ofreció coordinar interacciones personales adicionales si fuera necesario (00:01:41).

Expectativas de la clase y metodología: lse posgrados explicó que el curso consta de ocho clases, cada una con un objetivo, y la metodología consistirá en revisiones individuales o por grupo (si se detecta sinergia) (00:00:00). El formato de la clase incluirá una introducción, una parte técnica y un espacio para la implementación asistida, además de que todas las interacciones y clases serán grabadas (00:01:41).

Detalles de la participación y los proyectos: Se mencionó que hay 24 inscritos, con aproximadamente 15 a 17 personas activas o conectadas. La mayoría de las ideas de proyecto están enfocadas en Modelos de Lenguaje Grandes (LLM) o procesamiento de lenguaje natural (NLP) con aplicaciones (00:02:46). Solo un proyecto está enfocado en visión por computadora, lo que podría requerir acomodación o reconsideración para alinearse con el enfoque de LLM de la mayoría de los participantes (00:04:07).

Avance en los proyectos y alineación de expectativas: lse posgrados notó una variabilidad en el nivel de avance de los proyectos, con algunos en etapas más desarrolladas y otros comenzando a perfilar sus ideas. La primera clase tiene el objetivo de alinear a los participantes y establecer un entendimiento común. Shimon Achtung comentó que empezó sin conocimientos previos y que la información disponible es caótica y carece de gradualidad (00:05:29).

Requisitos del proyecto final y enfoque conceptual: Se aclaró que el trabajo no requiere código obligatorio, sino más bien requisitos conceptuales centrados en el diseño de un *pipeline* (00:06:42). lse posgrados buscará nivelar el conocimiento, pidiendo a aquellos con más experiencia que se enfoquen en la conceptualización y arquitectura, más que en la implementación completa (*deploy*). El objetivo es que los estudiantes al menos comprendan las herramientas y la arquitectura de las soluciones de inteligencia artificial (00:07:55).

Manejo de la ambición de los proyectos: Gabi Tallarico expresó que las expectativas iniciales de su proyecto eran muy ambiciosas, pero que las redujo al darse cuenta de sus limitaciones en programación y experiencia en informática (00:09:09). lse posgrados sugirió bajar las expectativas iniciales para enfocarse en hacer algo pequeño, escalable y reproducible, lo que permitirá concentrarse en la calidad de un módulo antes de escalarlo a un volumen mayor de datos (00:10:20).

Naturaleza de la materia y presentación del instructor: Shimon Achtung preguntó si la materia se centraría en la presentación de requisitos o en el dictado de teoría (00:11:29). lse posgrados respondió que la materia se centrará en la definición de tres "caminos" o *tracks* para los proyectos, con el objetivo final de producir un "producto comprensible", incluyendo una arquitectura conceptual, un informe en PDF y una presentación en PowerPoint (00:12:48).

Criterios y contexto de la evaluación de proyectos: Se mencionó que los perfiles de los estudiantes son heterogéneos, incluyendo docentes, desarrolladores y arquitectos de *software*. Los criterios de la materia enfatizan la clara definición del problema de negocio, la comprensión de una arquitectura simple y la presentación de evidencia de mejora respecto a una línea base (*benchmark*) (00:14:20). La calidad de la documentación final (PPT y PDF) también será altamente valorada (00:17:07).

Estructura y entregables de las ocho clases: Se detalló el calendario de las ocho clases, comenzando con una nivelación. La Clase 2 se centrará en la exploración de datos (*EDA*) (00:18:25). La Clase 3 se enfocará en definir la arquitectura. Las Clases 4 y 5 se orientarán a la construcción, el funcionamiento y la mejora del modelo (00:19:45). La Clase 6 será una sesión flexible de análisis de riesgo y ética, que puede ser movida o eliminada según el avance. La Clase 7 será para refinar el informe y la presentación, y la Clase 8 para la demostración final (00:20:58).

Gestión de entregables opcionales y el feedback: Los entregables de cada clase no serán obligatorios ni evaluativos, pero su envío es fundamental para recibir retroalimentación y asegurar la alineación (00:20:58). Los entregables incluyen la exploración de datos, diagramas de arquitectura y el código (*Colab*) (00:22:41). Se sugirió a los estudiantes avanzados, como J. Pablo Zebraitis y Carlos Salini, que compartieran su trabajo en GitHub en modo privado y colaboraran con sus compañeros (00:23:53).

Análisis de riesgo y presentación final: La Clase 6 abordará el análisis de riesgo y la ética, que consiste en identificar y mitigar entre tres y cinco riesgos éticos aplicados al proyecto (00:26:06). La presentación final en PowerPoint es obligatoria, con una duración estimada de 5 a 10 minutos por persona, con el objetivo de comunicar el problema de negocio, la solución y la experiencia (*storytelling*) (00:27:39).

**Uso del *Canvas* como herramienta de formalización**: Para la primera clase, se introducirá un *Canvas* simplificado adaptado para LLM como herramienta para formalizar las ideas de proyecto (00:30:10). El entregable de la Clase 1 será el *Canvas* diligenciado con un texto explicativo para obtener *feedback* (00:31:55).

Experiencia de los estudiantes con IA y productividad: Shimon Achtung compartió que utiliza interfaces como ChatGPT Plus, estableciendo roles y contexto en las indicaciones (00:33:24). Marcelo Luna comentó que en su empresa usan varias herramientas (Cloud, Cursor, Gemini) para automatizar tareas repetitivas, como generar diagramas de arquitectura a partir de repositorios de código (00:34:46). Se concluyó que el uso de IA ha aumentado la productividad, ya que las plataformas ayudan a generar código y resolver problemas de forma más dinámica y con mayor calidad (00:38:00) (00:40:28).

El papel de la IA en la reducción de tareas de bajo valor: Se discutió que la IA está reemplazando tareas que antes no aportaban tanto valor, liberando a las personas para centrarse en discusiones y nuevas medidas (00:39:15) (00:43:01). lse posgrados enfatizó que, si bien la IA acelera la producción, es crucial no perder las bases conceptuales, ya que todavía está al servicio de las personas (00:41:41) (00:50:06).

Reflexión sobre el uso de herramientas generalistas versus arquitecturas propias: Gabi Tallarico planteó la duda de cuándo usar *Notebook LM* o herramientas pre-hechas en lugar de construir un *pipeline* propio con *chunks* y *rags* (00:52:48). lse posgrados explicó que herramientas como *Notebook LM* podrían no ser adecuadas para escalar a cientos o miles de PDF, mientras que la arquitectura diseñada por el estudiante, aunque *naiv* inicialmente, tiene potencial de escalabilidad (00:53:57). Se enfatizó que comprender la arquitectura básica permite controlar mejor el sistema y saber qué solicitar a un desarrollador (00:56:26).

Evaluación de Modelos de Lenguaje y Análisis de Costos: J.Pablo Zebraitis compartió la conclusión de su proyecto de evaluar modelos de lenguaje, incluyendo los que corren localmente con Oyama y las API de Gemini, en términos de costos y tiempo [i]. Determinó que implementar una solución interna (in-house) no era viable ni rentable debido al volumen de casos a analizar, el tiempo que tardaría y el alto costo, especialmente cuando se compara con las soluciones basadas en API de bajo costo o "free-tier" [i, 45]. Se reconoció que, para fines prácticos, las soluciones basadas en API suelen tener un costo muy bajo o nulo (00:59:00).

Orientación y Herramientas de la Diplomatura: lse posgrados recibió comentarios sobre la futura incorporación de herramientas en las ediciones de la diplomatura. Se sugirió que el enfoque de la diplomatura debe centrarse en comprender el funcionamiento de los sistemas de lenguaje y en la conceptualización, en lugar de orientarse hacia el diseño y la ejecución de sistemas a nivel de producción. El objetivo principal es capacitar a los estudiantes para que puedan dialogar con expertos en el campo (01:00:42).

Experiencia con el Uso Local y el Costo del LLM: Santiago Germino relató su experiencia usando modelos de lenguaje localmente para evitar los costos de los tokens que se dispararon al usar servicios como Copilot sin una guía constante (01:00:42). Explicaron que, sin supervisión humana, los modelos pueden consumir tokens rápidamente, lo que genera gastos elevados (01:02:06). Se planteó que la mejor solución es combinar la aceleración de la IA con la dirección de una persona con experiencia en el área (01:03:13).

Análisis de Costos de Hardware vs. Pago por Servicio: La discusión se centró en la variable económica y la viabilidad de utilizar modelos locales versus modelos en la nube, especialmente para casos de uso específicos. Santiago Germino mencionó que el *hardware* es un factor importante, ya que una inversión de miles de dólares en equipo podría no ser rentable en comparación con el pago de una tarifa mensual por servicios. J.Pablo Zebraitis agregó que para casos de uso con pocas llamadas específicas que involucran datos multimodales (imágenes y texto), la inversión local no podría amortizarse (01:03:13).

Heterogeneidad y Estructura de la Diplomatura: J.Pablo Zebraitis proporcionó retroalimentación sobre la orientación de la diplomatura, señalando la gran heterogeneidad entre los participantes. Sugirió que podrían existir dos tipos de diplomaturas: una enfocada en los aspectos técnicos y matemáticos, y otra orientada a la práctica, al uso de modelos existentes y a la resolución de problemas reales. lse posgrados agradeció el *feedback* y reafirmó el propósito de encontrar un punto intermedio entre participantes con experiencia y aquellos que recién están comenzando (01:04:55).

Conceptos Básicos de Procesamiento de Lenguaje Natural (NLP): lse posgrados revisó los conceptos de NLP que se cubrieron en la materia anterior, incluyendo la clasificación de texto, el reconocimiento de entidades, la búsqueda semántica y la generación de texto. Se confirmó que se entiende cómo se pueden resolver problemas básicos de NLP y que los *RAGs* (Generation-Augmented Retrieval) son una solución común (01:06:00). Se solicitó a los participantes que compartieran sus *canvas* en los últimos 30 minutos de la clase para fomentar la interacción y la comparación de proyectos (01:07:19).

**Conexión a Modelos de Lenguaje y *API Keys***: Se consultó a los participantes sobre el uso de *API Keys* para conectarse a modelos de lenguaje en lugar de usar modelos locales. lse posgrados explicó que una *API Key* permite que el código se conecte a través de Internet para enviar y devolver información, evitando el trabajo con un modelo local. También se destacó que servicios como Gemini ofrecen una opción *free-tier* que facilita su uso (01:08:54).

**Concepto y Mecanismo del *Embedding***: La discusión se centró en el concepto de *embedding* y su función en el NLP (01:10:11). Manuel Babuglia definió un *embedding* como un vector multidimensional que representa palabras o frases en un espacio, donde las palabras similares mantienen ciertas relaciones espaciales (01:12:36). lse posgrados elaboró esta definición explicando que el *embedding* transforma el *token* en una concatenación de números (vector) en un espacio multidimensional, lo que permite que el LLM entienda las relaciones entre las palabras (01:14:09).

**Mecanismos de los *Large Language Models* (LLM)**: lse posgrados explicó que el LLM funciona dividiendo las palabras en *tokens*, llevándolos a un espacio multidimensional y utilizando la función de atención (*attention*) de los *Transformers* para detectar las relaciones complejas entre las palabras (01:15:35). Esto permite que el LLM genere la palabra siguiente basándose en la probabilidad, lo que da sentido a la respuesta (01:17:13). Se reiteró que los LLM predicen basándose en probabilidades y no razonan (01:22:37).

**Ventana de Contexto y *RAGs***: Se revisó la ventana de contexto, que es la cantidad de *tokens* que los modelos toleran entre la pregunta y la respuesta (01:18:37). Santiago Germino agregó que, en los *chatbots*, cuando la ventana de contexto se agota por una serie de preguntas, el sistema debe "sumarizar" o "compactar" la comunicación para que el significado permanezca y el contexto continúe (01:20:08). lse posgrados señaló que una ventana de contexto más grande es beneficiosa para los sistemas *RAG* porque permite inyectar más documentos para la consulta (01:21:21).

**Arquitectura y Fases de los Sistemas *RAG***: Se explicó que un sistema *RAG* tiene distintos componentes y se destacaron sus fases: la ingesta de documentos sin preprocesamiento, la fragmentación (*chunking*) para adaptarse a la ventana de contexto, y la conversión a un espacio vectorial (*embedding*) para almacenarlos en una base de datos vectorial (01:24:03). Cuando un usuario pregunta, la pregunta también pasa por el mismo modelo de *embedding* para generar un vector que, por similaridad, recupera los documentos relacionados. Luego, el LLM usa esos documentos recuperados para generar una respuesta fundamentada (01:25:17) (01:31:51).

**Mejora de la Calidad en *RAGs* y Métrica**: lse posgrados explicó que se puede mejorar la calidad de un *RAG* al agregar metadatos (como el reconocimiento de entidades) a los fragmentos de texto antes de generar el *embedding* (01:28:04). La calidad de un *RAG* se mide, por ejemplo, por la cantidad de documentos relevantes que aporta a la respuesta (01:29:21). Además, el uso de ingeniería de *prompts* puede mejorar la calidad del *RAG* (01:30:40).

**Niveles de Desarrollo (*POC* y *MVP*) y Enfoque de la Clase**: Se delinearon los dos niveles de trabajo esperados: la prueba de concepto (*POC*) y el producto mínimo viable (*MVP*) (01:33:19). lse posgrados busca que los participantes no utilicen soluciones *end-to-end* preexistentes (como las ofrecidas por Cloud), sino que trabajen paso a paso para desarrollar una prueba de concepto bien argumentada y detallada. Se espera que los participantes más avanzados compartan sus desarrollos (01:34:45).

**Uso del *Canvas* como Herramienta de Diseño**: Se introdujo el *Canvas* como una herramienta visual para mapear problemas de negocio, entradas, salidas y actores en la fase de diseño (01:34:45). El objetivo es alinear los proyectos a la mínima expresión posible y definir lo que se va a hacer y lo que no, respondiendo a preguntas clave como: ¿Qué problema resuelvo? ¿Para quién? ¿Con qué documentos trabajo? y ¿Cómo voy a evaluar si funciona (01:36:06)?

**Requisitos y Plazos del *Canvas***: Se presentó el formato del *template* del *Canvas* que incluye secciones sobre el corpus, los modelos (*LLM* y *embedding*), la base de datos vectorial, la propuesta de valor, los costos y las métricas de mejora (01:38:48). Se indicó que el *Canvas* es un punto de partida para la presentación de hoy, pero el desarrollo completo debe entregarse antes de la próxima clase (01:42:36). Se sugirió no dedicar demasiado esfuerzo a las secciones de costo e ingresos en este momento, ya que pueden cambiar (01:41:17).

Dinámica de la Clase y Estado de los Proyectos: Se confirmó que la mayoría de los participantes tienen proyectos individuales, aunque se ofrecieron oportunidades para unirse a proyectos abiertos a colaborar (01:43:55) (01:46:24). Después de un descanso de 10 minutos, la clase continuará con la revisión de cada proyecto individualmente, para lo cual se recomienda preparar el *template* del *Canvas* y las *notebooks* previamente presentadas (01:41:17) (01:47:43).

Definición de Salas y Recorrido de Grupos: lse posgrados informó sobre la intención de crear cuatro salas al azar para sesiones separadas de trabajo en grupo. Se planeó recorrer los grupos secuencialmente para mantener un orden en la interacción (01:48:55).

Solicitud de Presentación de J.Pablo Zebraitis: J.Pablo Zebraitis solicitó ser el primero en compartir debido a un compromiso de trabajo que requería su retiro de la sesión. lse posgrados aceptó su solicitud para que presentara su proyecto antes de la apertura de las salas (01:48:55).

Descripción del Proyecto de J.Pablo Zebraitis (Optimización de Incidentes): El proyecto de J.Pablo Zebraitis busca optimizar el ciclo de vida de la entrada de incidentes para una empresa que ofrece servicios de juegos y sistemas *backend* con alcance regulatorio en Uruguay. Actualmente, los usuarios envían incidentes a través de WhatsApp (mensajes de texto e imágenes) en lugar de utilizar herramientas de seguimiento como Redmine (02:03:20).

Alcance del Proyecto de J.Pablo Zebraitis (Captación de Incidentes): La captación inicial de la información (si se utilizará WhatsApp pago u otras tecnologías) está fuera del alcance inmediato del proyecto (02:04:42). El objetivo es automatizar el registro de todos los incidentes (02:03:20).

**Definición del *Dataset* de J.Pablo Zebraitis**: El *dataset* está compuesto por 18 casos concretos de soporte, que son principalmente imágenes de WhatsApp, tales como fotos de *tickets* o de pantallas de sistemas (02:04:42). No hay un patrón definido en las imágenes (02:06:08).

Estructura de Datos por Caso de J.Pablo Zebraitis: Cada caso en el *dataset* de J.Pablo Zebraitis está compuesto por una o dos imágenes, generalmente acompañadas de texto, o puede consistir solo en texto (02:07:08). Para el contexto de la materia, los casos de prueba son exclusivamente imágenes, que a su vez pueden contener otras imágenes dentro (02:08:01).

**Propuesta de *Pipeline* de Ingesta para J.Pablo Zebraitis**: Para abordar la ingesta, se sugirió que la primera parte sea iterar sobre un directorio, procesar la imagen (si existe) extrayendo el texto con OCR o una herramienta de detección de texto, y luego generar un *dataset* (TXT o JSON) con el texto extraído y el texto acompañante del caso (02:08:01).

Funcionalidad Prevista del Sistema de J.Pablo Zebraitis: El sistema propuesto debe tomar la imagen, identificar el origen del incidente (cuál cliente reporta el problema), clasificar el problema basado en el contenido de la imagen (por ejemplo, identificando boletas o sorteos), y generar una entrada en un clasificador para etiquetar la información y crear un *issue* en Redmine (02:08:57).

Recomendación de Acotación del Alcance para J.Pablo Zebraitis: lse posgrados recomendó acotar el proyecto para que no abarque todo el ciclo completo. El alcance se limitaría a leer el contenido de la imagen, procesarlo, y crear un sistema RAG para consultas relevantes y simplificar la identificación de casos por características (día, semana, mes) (02:10:03).

Definición del Problema de Clasificación de J.Pablo Zebraitis: El problema se definió como uno de clasificación, donde el resultado final sería una salida JSON con la clasificación de los incidentes (02:11:16). Se sugiere que esta clasificación podría alimentar otro proceso posterior (02:12:12).

**Modelos de Referencia (*Benchmark*) y Uso de LLM para J.Pablo Zebraitis**: J.Pablo Zebraitis probó dos enfoques: utilizar Ollama para clasificación, lo cual tuvo un rendimiento deficiente, y usar la API de Gemini. Los valores obtenidos con Gemini fueron considerados bastante aceptables, sugiriendo que la solución real podría involucrar una clave API de Gemini para clasificar los 18 casos de prueba en 30 segundos, lo cual es funcional para el *pipeline* de soporte (02:12:12).

Instrucciones Finales para J.Pablo Zebraitis: Se acordó acotar el *pipeline* hasta el punto de la clasificación con el LLM y documentar este proceso, evitando añadir complejidad relacionada con la arquitectura y la conexión de sistemas. También se le pidió completar el *canvas* con la definición actual del proyecto (02:13:13).

Consulta sobre el Proyecto de Fabricio De Luca (Cojeras en Vacas): Fabricio De Luca indicó que tiene una idea y un *dataset*, aunque no está disponible en la máquina actual. Su proyecto trata sobre la detección de cojeras en vacas lecheras (02:15:02).

**Definición del *Input* para Fabricio De Luca (Detección de Cojera)**: El proyecto de Fabricio De Luca implica utilizar visión por computadora para determinar si una vaca tiene problemas de cojera a partir de videos. Actualmente, el *dataset* consta de aproximadamente 80 videos etiquetados personalmente por Fabricio De Luca (02:16:01).

Avance en el Proyecto de Fabricio De Luca (Estimación de Pose): Fabricio De Luca mencionó que tiene avanzado el proyecto hasta la estimación de poses (*pose estimation*), que consiste en etiquetar puntos de referencia en la vaca a partir de los 80 videos (02:17:19).

**Resultados Deseados y Desafíos de *Dataset* de Fabricio De Luca**: La idea es lograr un puntaje de cojera (*score*), o al menos distinguir entre una vaca sana y una renga, ya que identificar los grados de cojera intermedios (grado 2 y 3) es más difícil (02:18:24). El desafío principal es que los videos están etiquetados solo para la estimación de poses, no para determinar si la vaca está sana o enferma, y se necesitan más videos etiquetados para el entrenamiento (02:19:41).

Recomendación de Acotación del Proyecto de Fabricio De Luca (Transfer Learning): lse posgrados sugirió acotar el proyecto a la mínima expresión posible, recomendando el uso de *transfer learning* con modelos de visión por computadora ya existentes, como Yolo, para la detección de la caja delimitadora (*bounding box*) de la vaca en los *frames* (02:19:41).

Alcance Final del Proyecto de Fabricio De Luca: Se considera que documentar la justificación del proyecto, la aplicación del *bounding box*, la detección de vacas con Yolo, y la fase de *pose estimation* es suficiente para los fines de la materia (02:20:53). Se sugirió centrarse en algo explicable y medible, como la identificación, sin la necesidad de entregar el modelo final de renguera (02:22:06).

Definición del Proyecto de Shimon Achtung (Análisis de Sentimiento de Comentarios de YouTube): El proyecto de Shimon Achtung, llamado "Decime qué se siente", consiste en tomar la URL de videos de YouTube y analizar los comentarios (02:23:15). El *dataset* es el texto de los comentarios (02:24:16).

Funcionalidad del Sistema de Shimon Achtung: El sistema utiliza una interfaz Gradio para cargar la URL de un video de YouTube y devuelve métricas sobre los comentarios, clasificándolos como positivos, negativos, o raros/imprevistos (02:24:16). El usuario obtendría un cuadro que indica la proporción de comentarios positivos y negativos (02:26:47).

**Propuesta de *Benchmark* y Mejora del Modelo de Shimon Achtung**: Se propuso que el modelo más sencillo (*benchmark*) consista en un *dataset* de muchos comentarios etiquetados manualmente por Shimon Achtung, utilizando un modelo de clasificación supervisada de Scikit-learn (02:28:52). La mejora del modelo sería la segunda versión, aplicando un LLM para la clasificación, lo que permitiría comparar los resultados (02:29:53).

**Desafío de Exploración de *Dataset* para Shimon Achtung**: Se recomendó que Shimon Achtung explore y prepare el *dataset* para la próxima clase, lo que implica tener una tabla con la URL, los comentarios, la clasificación y la dimensión del *embedding* (02:29:53). También se sugirió automatizar el proceso de extracción de comentarios (el *pipeline*) para obtener la tabla que luego podría etiquetar (02:30:57).

Definición del Proyecto de Marcelo Luna (Asistente de Regatas): Marcelo Luna presentó un prototipo de asistente para analizar incidentes en regatas. El sistema utiliza el reglamento internacional de regatas y los relatos de incidentes (protestas) para identificar las reglas aplicables y llegar a una conclusión sobre posibles penalizaciones (02:33:30).

Estructura y Proceso Sugerido para el Proyecto de Marcelo Luna: Se sugirió conceptualizar el sistema utilizando un modelo RAG que incorpore el reglamento (un PDF) (02:34:56). El proceso incluiría el preprocesamiento del texto del reglamento y, para las pruebas, utilizar 10 a 15 relatos de casos reales (el *ground truth*) (02:36:10).

Avances y Modelos Utilizados por Marcelo Luna: Marcelo Luna ha estado trabajando en la recuperación semántica de la información y en la aplicación de expresiones regulares para el procesamiento del reglamento RAG (02:36:10). Está utilizando modelos locales, específicamente un modelo Qwen en Ollama, y ha probado diferentes estrategias de *prompting*, encontrando mejores resultados con *few-shot* que con *chain-of-thought* (02:37:30).

Recomendación de Acotación del Alcance para Marcelo Luna (Decisión Humana): lse posgrados sugirió que el sistema RAG solo proporcione las reglas relacionadas con el incidente, pero que la decisión final (la penalización) recaiga en el humano (jurado o juez) en lugar de en el LLM (02:38:49). El sistema debe ser un sistema de apoyo a las decisiones (02:41:14).

Argumentación de Marcelo Luna sobre el Valor Agregado: Marcelo Luna explicó que la mayoría de los jueces internacionales ya conocen las reglas. El valor del sistema es proporcionar una base para el análisis (identificando hechos, reglas y un *rationale*), especialmente cuando las decisiones de los jueces no están alineadas, sirviendo como una orientación (02:40:05).

Áreas de Mejora para el Proyecto de Marcelo Luna: Se recomendó refinar el preprocesamiento del *corpus* y el sistema de *embedding* (02:42:28). Además, para la exploración del modelo, se sugirió incluir una ventana o un lugar en el sistema para que Marcelo Luna visualice qué documentos está recuperando el RAG al tomar una respuesta, lo cual es útil para la depuración y para entender por qué el modelo elige ciertas reglas (02:43:44).

Comentario de Usuario Final (Challengear la Protesta): Fabrizio De Luca sugirió que el sistema podría ser utilizado por los competidores para evaluar su protesta antes de presentarla, sirviendo como una herramienta para "challengear" su propio relato de incidente (02:45:48).

Definición del Proyecto de Gabi Tallarico (Agente de Asesoramiento Técnico): Gabi Tallarico está trabajando en un agente inteligente de asesoramiento técnico. La idea es integrar una fuente bibliográfica seleccionada (documentación validada) para que el *chatbot* responda preguntas sobre enfermedades productivas y modalidades de producción o cuidado (02:46:45).

Análisis de Corpus y Desafíos de Procesamiento de Tablas: Gabi Tallarico presentó su análisis de corpus, que consiste en fichas técnicas con texto, tablas y fotos para su trabajo sobre enfermedades y plagas (02:47:55). Un desafío técnico es cómo procesar las tablas, ya que una máquina no las lee fácilmente. El instructor sugirió convertir las tablas a formato JSON, una estructura que las máquinas entienden rápidamente, proponiendo esto como un desafío para Gabi Tallarico para esa semana (02:49:13).

Estrategia para el Procesamiento de Datos del Corpus: Se discutió la conveniencia de procesar las tablas manualmente o de forma automática, dado que inicialmente solo hay alrededor de 12 a 30 documentos (02:49:13). Aunque Gabi Tallarico planea escalar el prototipo a otras cadenas de producción (como la cebolla) lo que requeriría automatización, para el trabajo actual con la producción de ajo, que está más acotado, se sugirió el procesamiento manual para aportar mayor valor (02:50:21). El desafío de Gabi Tallarico es mejorar el *pipeline* de ingesta y probar si las métricas de *Retrieval Augmented Generation* (RAG) mejoran con el texto mejorado (02:51:28).

Discusión sobre la Extracción de Entidades y el Uso de Dataset Sintéticos: Juan Ignacio Sinopoli presentó su trabajo, que inicialmente se enfoca en la extracción de entidades de mensajes de centros de atención al cliente (02:52:38). Identificó la necesidad de un *dataset* más grande, ya que su punto de partida era de solo 15 mensajes, lo que podría generar un sesgo. Se le recomendó generar datos sintéticos, pidiendo a un *Large Language Model* (LLM) que generara 100 o 200 ejemplos para ampliar su corpus (02:54:00).

Recomendaciones para el Producto Final y Clasificación de Mensajes: Se definió que el *output* del sistema de Juan Ignacio Sinopoli debería ser un documento estructurado, probablemente un JSON, que interprete mensajes coloquiales y los estructure en casilleros definidos (02:55:05). Aunque se consideró la generación de respuestas, se sugirió centrarse en el reconocimiento de entidades y la clasificación de los mensajes, ya que el sistema ya tenía definidas 13 categorías de problemas (02:57:27). Se concluyó que el trabajo debería centrarse en la complejidad del reconocimiento de entidades y la clasificación, sin avanzar a la generación de texto de respuesta si esa parte aún no está clara (02:58:49).

Propuesta de un Asistente de Corrección para Matemáticas: Lorna Pons presentó su idea para una extensión de un asistente de corrección, un sistema RAG para trabajos de matemáticas, después de haber tenido éxito con un asistente de corrección para trabajos de tecnología basados en texto (02:59:57). Su propuesta incluye tomar la propia resolución del ejercicio y otras tres o cuatro resoluciones generadas por un LLM como base para la corrección. El instructor expresó cautela ante la complejidad cognitiva y semántica de los problemas de matemáticas, pero recomendó a Lorna Pons que probara durante la semana la coherencia de las fórmulas y resoluciones matemáticas generadas por el modelo (03:01:33). Si las métricas de similaridad no resultan coherentes, se le sugirió volver a centrarse en mejorar su trabajo previo basado en texto (03:03:01).

**Solicitud de *Feedback* y Tareas para la Próxima Sesión**: Para asegurar el alineamiento de todos, el instructor pidió a los estudiantes que compartieran el *canvas* de su proyecto, o un documento simple similar, por correo. También solicitó *feedback* honesto sobre la dinámica de la clase para realizar ajustes si fuera necesario, y la dinámica fue bien recibida por los participantes (03:05:20). Para la próxima sesión, se solicitó a los estudiantes traer datos, *colabs*, tablas y textos, haciendo hincapié en la necesidad de tener *datasets* listos para un análisis exploratorio de datos (EDA) (03:06:37).

Consejos sobre Organización de Datos y Continuidad del Proyecto: El instructor recomendó que todos los que trabajen con texto generen una tabla o un archivo TXT por fragmento de texto (*chunk*) dentro del *colab* para almacenar datos y facilitar la escalabilidad (03:06:37). La próxima clase se enfocará en las métricas RAG y en un ejemplo de RAG, y el instructor asumió el compromiso de revisar los *colabs* para proveer retroalimentación específica y recursos adicionales. Gabi Tallarico expresó su aprecio por la dinámica de compartir los *colabs* de otros para aprender diferentes enfoques y detectar posibles errores (02:52:38) (03:08:07).

Revisa las notas de Gemini para asegurarte de que sean precisas. Obtén sugerencias y descubre cómo Gemini toma notas

Cómo es la calidad de estas notas específicas? Responde una breve encuesta para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.

📖 Transcripción

29 abr 2026

Taller de trabajo final (1/8) - d015b25 - Transcripción

00:00:00

lse posgrados: Hola,
Carlos Salini: Buenas tardes.
lse posgrados: chicos. ¿Cómo están?
Carlos Salini: E ya que estamos acá, de paso quería hacerte una consulta. Perdona que mira,
lse posgrados: Sí, sí, dale.
Carlos Salini: sabes que eh bueno,
lse posgrados: la
Carlos Salini: ¿qué tal? Eh,
lse posgrados: cab.
Gabi Tallarico: Hola,
Carlos Salini: yo tenía programado este los miércoles para otro tipo de actividad y como cambiaron, teníamos al principio teníamos los martes, bueno, yo había separado el los miércoles para otra actividad. Em, yo estoy puedo estar nada más casi la primera hora del curso, entonces quería saber más o menos. sé que es como que vas a ir como, no sé si viendo proyecto por proyecto, no sé cómo vamos a hacer en cada en cada una de las clases, pero quería saber cómo podría yo quizás coordinar eh para ver el tema del proyecto o algo eh con respecto a eso, porque yo puedo estar hasta las 7:30 más tarde, 7:40 porque ya me tengo que ir a otra reunión.
lse posgrados: Sí, mira la Bueno, después lo repito cuando entren los demás,
Carlos Salini: M.
lse posgrados: pero son bueno, como saben, son ocho clases en casi todas hay como un objetivo, digamos, todas hay un objetivo y la idea es sí ir one by one o por grupo, si es que lo si es que hay sinergia en grupos.

00:01:41

lse posgrados: Ahí est sondeando también eso, pero sí, ese es el objetivo. En todo caso, si tus compañeros no tienen problema, comenzamos con vos al principio, lo doy rápido y y descuidar que por ahí también si es que hace falta alguna interacción personal coordinamos, ¿no? No, ni te preocupes, digamos, en ese sentido. Así que sí, yo creo que por ahí la la voy a tratar de que de que de hacer la los primeros 30 minutos, cosa que tener al menos 15 minutos con vos en cada clase, digamos,
Marcelo Luna: Ok.
lse posgrados: ahí en esa parte. Si, me parece que que puede ser por ahí, o sea, yo todas las clases las tengo pensadas así como una introducción de qué es lo que vamos a hacer, un poquito de de técnica, la parte técnica y después ya ir uno por uno para que vayan implementando, ayudándolos,
Carlos Salini: Bien. Sí, igual en todo caso hoy,
lse posgrados: etcétera.
Carlos Salini: por ejemplo, hoy justamente tengo esa ese problema en particular, ¿no? Hoy sí o sí me tendría que ir un ratón, pero quizás para las próximas clase y demás ya podría coordinar y quedarme un poco más de tiempo.
lse posgrados: Okay.

00:02:46

lse posgrados: Bueno, sí,
Carlos Salini: Pero más que nada hoy
lse posgrados: iguales grabadas y y las interacciones van a quedar grabadas porque al final también hay un está planificado un espacio donde donde digamos no sé si todos porque son muchos muchos proyectos, pero sí algunos que puedan ser representativos de la gama de proyectos que hay, compartan el avance, etcétera, digamos. Hm. E bueno, hay 24 inscriptos, si mal no recuerdo, eh 17 preguntas respondidas de la encuesta, con lo cual creo que habrá 15, 17 personas que se conecten. El resto quizás están medio offline o se van conectando
Mariana García: Yeah.
lse posgrados: mientras eh mientras avanza la clase. Así que yo diría que esperemos un ratito más. Son recién las 7. Sí, estuve, creo que ya se está grabando esto. Sí, estuve viendo la las respuestas, eh, con algunos compartí y vuelta algunos correítos. Em recuerdo bien con con todos, pero eh sí, con algunos sí compartí algunas cuestiones. Eh, muy muy buenas las ideas, la verdad que está está piola. Casi todos están eh muy enfocados en los que son LLM o

00:04:07

Shimon Achtung: M.
lse posgrados: procedimiento de lenguaje natural con alguna aplicación. Hay solamente uno que que está para cuestión de visión por computadora, que bueno lo deberíamos conversar porque bueno, Justo respondió hoy. Entonces es a ese no lo tenía no lo tenía en el radar hasta que bueno, apareció un visión por computadora y bueno, no estaba en las planificaciones, pero bueno, lo lo acomodamos. Sí. O vemos si lo podemos convencer para que haga algo de de LLM como todo lo demás y nos mantenemos todo ahí. Pero bueno, ahí ahí lo vamos viendo. Eh, ya somos 10.
Marcelo Luna: He.
Shimon Achtung: Buenas a todos. Shimon.
lse posgrados: Hola, Simón. ¿Cómo andas?
Manuel Babuglia: Ok.
lse posgrados: ¿Sos Simón o Shimon? Shimon. Okay, Shimon.
Shimon Achtung: Shimon.
lse posgrados: Okay. Ah, bueno, no sé si quieren quieren aprovechemos 5 minutitos hasta que a las 7:5 alargamos. ¿Me quieren comentar cómo le fue con procedamiento de lenguaje natural? Vi algunos proyectos. Gabi mandó, me puso en copia de la entrega, lo pude ver, vi casi todos los GIDHub que me comentaron en la en la encuesta, lo cual está algunos están digamos hay distintos esquemas.

00:05:29

lse posgrados: están algunos más avanzados en cuestión de desarrollo y otros empezando como a desarrollar una idea, digamos. Entonces, creo que viene bien esta esta primer clase como para que como para que nos alineemos. No sé si alguno quiere comentar algo sobre cómo le fue en en procesamiento lenguaje natural, les fue útil, ¿qué les parece? ¿Ya tenían algún conocimiento del tema?
Shimon Achtung: Yo arranco de cero en todo, pero no sé algunos comentarios de otros compañeros gustaría escuchar todo el descargo por mail,
lse posgrados: Pero a me interesa el tuyo, Shimon, porque digamos Sí,
Shimon Achtung: me parece.
lse posgrados: sí, sí, lo leí en detalle, pero digamos vos no conocías la herramienta, digamos,
Shimon Achtung: A ver, estamos invadidos por un montón de información que aparece y todo está de mencionado de una manera
lse posgrados: No.
Shimon Achtung: superficial, como que bueno, se puede utilizar para esto, para otro, pero es como que eh te dan un mapa, pero o te te nombran, es como que te nombran en ciudades y no te dicen para dónde agarrar el primer paso, ¿viste? Entonces, eh no no hay un GPS que te diga, "Bueno, ahora primero este paso, después el otro y no hay una gradualidad, no hay por dificultad. Es bueno es como que yo te enseñé a tocar el dio,

00:06:42

lse posgrados: Bueno,
Shimon Achtung: mira, dos remis y dos, ahora tocas la sinfonía y estás muy ahí perdido. Entonces yo empiezo a con las herramientas de inteligencia artificial a buscar,
lse posgrados: claro,
Shimon Achtung: bueno, ¿qué información debería buscar?" y esto muy muy caótico y bueno,
lse posgrados: sí,
Shimon Achtung: qué sé yo,
lse posgrados: hay de todo encima, ¿no? No hay nada, aunque esté muy estructurado. Bueno, yo voy a intentar poner un poco en orden eso en el sentido de que digamos no voy a tratar de no meterme en código, o sea, no hay requisitos de código en este trabajo. Si hay requisitos conceptuales, es decir, diseñar un pipeline después de todas las materias que han que han tenido, o sea, qué es lo que entra, qué es lo que sale, qué es lo que espero que entre. ¿Qué es lo que espero que salga? Y describirlo se puede hacer, digamos, de una manera conceptual, sin tanto código y es lo que digamos en el el va a ser la base. Ahora, aquellos grupos que estén más avanzados, que ya hayan avanzado en código, etcétera, bienvenidos. Si quieren meter un poco más de complejidad se puede, digamos.

00:07:55

lse posgrados: Pero sí, digamos, la idea mía también es de alguna forma nivelar eh digamos un poco hacia abajo aquellos que están muy avanzados, tendrán que hacer algo más conceptual y no no digamos no llegar al deploy, digamos, al deploy es cuando uno sea sirve directamente el el proyecto para que alguien lo consuma. eh no llegar a un deploy, pero sí esquematizarlo, hacer una maqueta, etcétera. Digamos, ese es mi objetivo porque, bueno, sí, esta brecha que hay entre los alumnos la anoté en la encuesta. Entonces, es uno de mis objetivos, ojalá lo cumpla, tratar de llevar un poco de la mano aquellos que están más atrás lo que es código y concepto, etcétera, y tratar de orientar un poquiz en arquitectura, en soluciones, en eso, aquello que está más avanzado, digamos, ¿no? Pero tratar de llegar a un nivel más o menos como que creo que al final de la diplomatura es bueno saber que existen,
Marcelo Luna: He.
lse posgrados: no sé, que que para clasificar imágenes tenés algunas herramientas para clasificar texto tenés herramientas y métodos también. más o menos saber a dónde a dónde apuntarle y que si en algún momento, no sé si desarrollarlo vos, pero si tenés que contratar a alguien para que lo haga, sepan de lo que están hablando, digamos, ¿sí?

00:09:09

lse posgrados: O sea, si tenemos que hacer, no sé, búsqueda de texto, etcétera, bueno, si tengo que implementar un retrival, sé lo que está hablando y y el consultor de alguna forma no me va, digamos, no me va a hacer algo más complejo de lo que yo espero, digamos. Ese ese es mi objetivo. Después vi muy en detalle por ahí algunos otros como el el de Gabi. Está bueno el proyecto. Creo que hay hay cosas interesantes ahí en tu proyecto, Gabi.
Gabi Tallarico: No, por ahí comentarles un poco que que la idea realmente es mucho más grande de la que por
lse posgrados: Claro.
Gabi Tallarico: ahí siento que podría ser yo como que me me la diplomatura en cuando la comencé suponía que iba a poder a tener ese proyecto como acabado, pero me doy cuenta que digo, yo no soy, digo, no soy programadora,
Shimon Achtung: Bueno,
Gabi Tallarico: no vengo del palo de la informática. Entonces me doy cuenta que digo, nada, cada vez que hacíamos una entrega era como que le reducía un poco las expectativas a lo que que iba logrando. Digo, nada, no voy a llegar a ser el proyecto que se requiere.
Marcelo Luna: He.
Gabi Tallarico: Es más, digo, no es un proyecto inventado, sino un requerimiento de una demanda interna.

00:10:20

Gabi Tallarico: Entonces, para las siento como que esto va a contribuir, pero que no me va a solucionar el eh la demanda que teníamos, ¿no? Que eso lo fui cambiando en el transcurso de que íbamos transitando las distintas materias, ¿no? Eh, cuando empezamos esto en marzo, o abril del año pasado, suponía que iba a terminar todo.
Shimon Achtung: Ya.
Gabi Tallarico: cada vez recorte más mis expectativas y de código,
Shimon Achtung: Ah.
Gabi Tallarico: obviamente que Sí,
lse posgrados: Bueno, hoy creo que también en esta clase vamos también a porque vi que algunas descripciones de las cosas que se quieren hacer como que son muy ambiciosas.
Gabi Tallarico: ahí
lse posgrados: Por ahí hay que bajarlas quizás un poco más y hacer algo más que escalable, digamos, ¿no? O sea, lo chiquito, escalable, reproducible, que después, no sé, en tu caso, Gabi, por ejemplo, vos trabajaste, no sé, con 12 PDF. Bueno, capaz que si hacemos que uno que uno sea super bueno, después lo escalamos hacia hacia otros más. Sí. Entonces es un poco ir desarmando y bueno, ahí yo la la ya somos ya somos 13 alumnos han comigo hay 12 más o menos la mitad de la clase.

00:11:29

lse posgrados: Así que yo yo voy a empezar eh con la con la presentación. Si alguno quiere decir algo más respecto de lo que ha pasado, digamos, las clases de la materia, etcétera, tienen dos tres minutos para decirlo ahora, si no
Shimon Achtung: Me imagino que cada uno le irá apareciendo la las inquietudes.
lse posgrados: empiezo.
Shimon Achtung: Yo solamente lo que no sé si es este último bimestre algo más eh como que nosotros vamos presentando cosas por mail a vos y nos vas pidiendo requerimientos o es dictado de teoría,
lse posgrados: No, no. Ah, ahí lo voy a explicar bien ahora. Justo me diste me diste el pie para que lo explique. Bueno, ahí voy a compartir pantalla e pantalla
Shimon Achtung: No.
lse posgrados: completa acá. Me avisan si se ve, por favor. Perfecto. Bueno, esto sacó. Ahí se ve, ¿cierto? Okay, perfecto. Yo no no estoy viendo sus cámaras,
Shimon Achtung: Sí.
lse posgrados: así que como está en modo presentación, no veo solo más que la presentación. Bueno, me presento. Soy Cristian Salinas, soy ingeniero en recursos naturales y medio ambiente, no soy del palo de la programación.

00:12:48

lse posgrados: Terminé la especialidad e en inteligencia artificial en noviembre, creo, del año pasado, octubre, noviembre del año pasado. Eh, la verdad que estuvo est bueno. Se les recomiendo si si es que después de esto si quieren seguir indagando. Les pongo, les dejé ahí mi LinkedIn por si quieren conocer un poco más sobre lo a lo que me dedico. Básicamente trabajo en la parte ambiental de empresas mineras, digamos, en en explotación de litio y de metales en el norte de la Argentina, eh dirigiendo equipos de medio ambiente y de protección ambiental y a los cuales le hemos sumado un poquito de tecnología que ido aprendiendo, sensores remotos, imágenes satelitales y algunas de las cosas que ustedes también vieron en la en la Diplo. Bueno, son ocho clases. Yo más o menos distinguí dos o tres tracks, digamos, tracks serían como caminos por los cuales van a seguir los los equipos o o los proyectos. Y el objetivo final es tener un producto comprensible, ¿sí? O sea, va a ser, lo voy a detallar a continuación, pero básicamente es una arquitectura, sí, conceptualizada en tu, digamos, de principio a fin, eh, que va a tener que va a tener, digamos, un informe en PDF con determinados contenidos y que eh también va a tener una presentación en PowerPoint donde ustedes expresan y comunican a los compañeros qué es lo que esperan, digamos, y cómo funcionaría esto para tener feedback de digamos de por parte del equipo.

00:14:20

lse posgrados: Eh, esto lo armé con los que me habían respondido las preguntas hasta ayer aproximadamente. Hay perfiles heterogéneos, lo sé, hay docentes, desarrolladores, arquitectos de software, hay de todo un poco. A casi el 99.9% están todos enfocados en su proyecto respecto de trabajo de procesamiento lenguaje natural y uso de LLMs. Está está buenísimo porque es lo que más se usa hoy en día. Eh, hay una sola persona eh que que respondió la encuesta hoy diciendo, bueno, que va a ser un bot de visión por la por computadora respecto de algo vinculado a la ganadería. Eso después cuando termine de presentarlo me gustaría conversar un poquito con él también cuando vaya por uno por uno. E yo diría que también aquellos que no que no tienen trabajo definido, tengo una propuesta. Sí, es eh además de de digamos lo que el NLP clásico que clasificación de sentimiento o identificación de algunos patrones del texto, hay algunos, la mayoría son racks, digamos, algo más aplicado y hay un par que son de agentes autónomos que es tiene cierta complejidad también lo vamos a ver un poquito en detalle con cada uno a medida que avancemos. Bueno, este es el contexto en el que estamos. Veamos, los criterios de esta materia, sobre todo, es definir claramente cuál es el problema de negocio y cuál es la solución, una comprensión de alguna arquitectura simple que yo los voy a ayudar a armar.

00:15:49

lse posgrados: Ustedes créanme que con lo que han visto en la diplomatura ya la pueden realizar o la pueden al menos esquematizar. Sí, tiene que tener un componente de evidencia de mejora, es decir, lo que se plantee, digamos, se tiene que plantear lo que se llama eh y seguramente vieron o conocen una línea base o un benchmark, es decir, una solución sencilla, aplicable que después pueda ser mejorada. La mejora debería estar documentada al final, digamos, de del materia. Eh, doy un ejemplo en esto. Mejora es, por ejemplo, si yo armaba un rack y directamente hacía el chanking sin ningún criterio, sino decía, bueno, hasta esta cantidad de de tokens o estos primeros caracteres es un un chunk, un bloque de texto. Eh, hay formas de mejorarlo, hay formas de extraerle más info a ese chank, darle un poquito más de contexto para que las respuestas mejoren. esa aplicación ya es una evidencia de mejora en en no sé, por ejemplo, en modelos de regresión, el un benchmark posible si queremos predecir alguna variable cuantitativa, no sé, el promedio. Bueno, es el benchmark, digamos, si yo quiero predecir, no sé, la producción eh neta de forraje en un en un predio, bueno, puedo calcular el promedio del último año y ese es un el benchmark.

00:17:07

lse posgrados: Después yo puedo decir, "Bueno, yo aplico un modelo." Bueno, ¿cuánto respecto de de aquel de aquel aquel modelo que me es más fácil aplicar? No tengo ningún costo. ¿Cuánto mejor estoy respecto de lo que planteado originalmente? También vamos a valorar mucho la calidad documental, digamos, los entregables finales son una PPTA en la clase, en la última clase y un PDF, un documento en PDF con una determinada cantidad de contenido. El colabitub va a ser opcional, ¿sí? para aquellos que se digamos estén más adelantados y quieran quieran presentarlo y exponerlo. Y bueno, obviamente la presentación eh final tiene cierto criterio de evaluación también. Bueno, e como mencioné son tres entregables, uno opcional, el primero, un documento explicativo que tiene siete secciones. en la PPT un poco más antes, da más detalles, pero básicamente un resumen ejecutivo, una justificación del problema, que es más o menos lo que vamos a ver hoy, y así clase a clase iremos incrementando y desarrollando, al menos conceptualmente eh cada una de estas fases del informe para que ustedes después durante la semana terminen de acomodar y de desarrollar para que al final al final de la de la cursada tengan el producto final, digamos, ¿no?

00:18:25

lse posgrados: La presentación también, digamos, hay una presentación al final, una diapositiva, la arquitectura, la explicación en to end, los resultados y las métricas que se usaron, la métrica versus el baseline. Si no se mejora es una conclusión también, si empeora también es una conclusión. Así que en ese sentido no se preocupe, no estamos exigiendo que lo que se aplique mejor el Baseline. Y por último, bueno, un código que esté documentado y que tenga cierta explicabilidad para que podamos valorar, digamos, ¿no? Este último no tiene no tiene carácter evaluativo, es más que nada para que se comprenda en el caso de que se entregue y para mí para que le quede de base a ustedes como un portfolio por por futuras publicaciones o lo que ustedes decidan. Bueno, son ocho clases. La primera va a ser una una nivelación. Vamos a fijar el rumbo, objetivo y base del proyecto, que es lo que estamos hablando ahora. La segunda clase eh ya tendrían que traer los datos eh, digamos, al menos las bases de datos o los dataset para que lo encamine o ustedes ya me muestren y yo los ayude a ver cómo encarar un un EDA. Me gustaría que me digan ahora si saben lo que es UNEDA, como para si no para esa clase dar alguna presentación rápida de lo que es Uneda, pero básicamente una exploración de los datos.

00:19:45

lse posgrados: Me imagino vieron algo de esto en en la Exacto.
Gabi Tallarico: En la primera materia lo
lse posgrados: Perfecto.
Gabi Tallarico: vimos.
lse posgrados: Eh, básicamente es conocer los datos con los que tenemos. En el caso de texto será lo que contiene la cantidad de caracteres, la cantidad de PDF, la forma en la cual puedo trabajar internamente dentro de ese PDF para que los chan me aporten claridad semántica para que después un rag pueda aplicar mejor y buscar mejor por por similidad semántica. La clase tres va a ser eh digamos cuál va a ser la arquitectura, es decir, desde lo que ingresa, cómo lo voy transformando, digamos, un dato crudo o los PDF crudos o una imagen cruda, una tabla cruda, cómo lo puedo ir cambiando y estructurando desde el final hasta lo que decida que va a ser la salida, digamos, del modelo. Eso lo vamos a definir hoy también. La clase cuatro, eh, básicamente ya va a ser la construcción. Vamos a estar orientados ya a construirlo y tratar de al menos en algo más chiquitito, una maqueta, una función, un par de bloques en en colab o una descripción de qué es lo que esperamos que entre y que salga y cómo esperamos que entre y que salga cada parte del pipeline.

00:20:58

lse posgrados: El la clase cinco va a ser para ya ver cómo funciona o o esperar cómo funciona esto y cómo se podría llegar a mejorar. Sí. La clase seis, esta es una clase media comodín donde si nos atrasamos con alguna de las anteriores, esta parte de análisis de riesgo y ética la podemos mover para el final o eliminar para según cómo vayamos avanzando, pero básicamente el análisis ético y esto tiende a ir a un digamos un análisis de riesgo entre lo que yo voy a aportar como solución y algunos criterios éticos aplicados a la inteligencia artificial. Eh, la clase siguiente ya directamente es eh tiempo para que refinen el informe, consulten qué parte está floja con se puede agregar un poco más y también la preparación de la PPT y en la clase ocho la la demostración directamente ya eh hacemos eh la presentación. Eh, ¿das? Bueno, esto fue lo lo que fui detallando. Cada parte de esto tiene un entregable esperado. Estos entregables no forman parte de lo evaluativo, pero yo espero que me lo manden para que usted y ustedes también deberían enviármelo para que podamos tener feedback. Acá digamos, si un alumno no envía, no pasa nada. Al final cuando cuando hacemos la evaluación final, si no tuvo feedback y alineación con lo que yo fui dando, con lo que fuimos viendo, nada, quizá queda un poco desalineado, pero lo ideal sería que cada fase o cada clase tengan un entregable, lo mínimo que lo mínimo que se pueda hacer en la clase o en la semana.

00:22:41

lse posgrados: O sea, no no no acá en este entregable no hay no hay un criterio evaluativo, digamos, más que nada para que tengamos feedback. en la clase dos, bueno, eleda un documentito que explique cómo fue la exploración, qué datos tenemos, cómo vienen los datos, etcétera. la arquitectura, al menos un diagrama en la clase tres, al menos un diagrama escrito hecho en algunas de las aplicaciones online o con o con o con Word o con el propio PowerPoint. Hay miles de formas para hacer diagramas. el eh la clase cuatro, un colab, si es que se se animaron a ejecutarlo o una descripción de qué es lo que esperamos como núcleo del modelo. Si si están haciendo preguntas, pregunte directamente porque no puedo ver la puedo ver el el el chat.
J.Pablo Zebraitis: Profe, no sé si me escucha este,
lse posgrados: Sí.
J.Pablo Zebraitis: bueno, yo me me equivoqué y ya casi que avancé mucho el proyecto. Pensé que el 30 cuando dijeron que había que entregar, me apresuré mucho en el proyecto. Este y tengo algo bastante avanzado, tengo algo en GitHub. Eh, una pregunta concreta es, eh, yo tengo este repo abierto, me gustaría que no estuviera.

00:23:53

J.Pablo Zebraitis: Digo, ¿podemos hacer que el repo pasarle o linkquearlo a usted como profesor o a lo que sean para no tenerlo?
lse posgrados: Sí, o sea, me mandas o yo te mando una solicitud y me aproba para que lo pueda ver,
J.Pablo Zebraitis: Dale, está okay.
lse posgrados: No,
J.Pablo Zebraitis: Perfecto.
lse posgrados: no hay drama
J.Pablo Zebraitis: Pues yo lo tengo bastante avanzado, ya tengo armado los pip decisiones,
lse posgrados: con
J.Pablo Zebraitis: todo lo demás. cuando quieras lo lo voy a cerrar el proyecto para que no esté público.
lse posgrados: de una. Sí, sí, sí.
J.Pablo Zebraitis: Está
lse posgrados: Ahí en mi correo electrónico me pod agregar como comentador. No me acuerdo si creo que si me agreg al menos como visor, digamos,
J.Pablo Zebraitis: Sí,
lse posgrados: para que lo pueda ver.
J.Pablo Zebraitis: porque si si tú tenés este cuenta de GitHub te la agrego y listo.
lse posgrados: Okay, buenísimo.
J.Pablo Zebraitis: A
Carlos Salini: Bueno, aprovecho yo también que estoy en la misma situación que que Pablo,
lse posgrados: Sí,
Carlos Salini: así que bueno, también voy a hacer lo mismo, lo voy a poner en privado y y después compartir de alguna manera el Loí ya,

00:24:49

lse posgrados: sí. Bueno,
Carlos Salini: Gra.
lse posgrados: al sería bueno que los que están avanzados también ayuden a los, digamos, a los compañeros y sí les voy a pedir feedback cuando estemos en esa etapa para que expliquen también cómo cómo conceptualizaron eso y de alguna forma sea más colaborativo el trabajo. Sí, yo he visto por los desarrollos que me han mandado, algunos están bastante avanzados, eh, con lo cual, digamos, serviría mucho que más o menos vayan compartiendo en clase en el momento, al final de la clase hay un momento donde podemos compartir. comenten, digamos, cada clase lo que aplica cada a cada proyecto, no sé, en la clase 3 arquitectura o en la clase 4, el núcleo del modelo y lo vamos pidiendo, pero que se ofrezcan, digamos, si ustedes ya lo tienen hecho, sirve un montón. Bueno, clase 5, refinamiento y métricas, digamos, de lo que lo que hablamos de nuevo, el el al menos el entregable sería una comparación, un texto diciendo, bueno, el Baseland dio tanto con este modelo espero tanto o dio este resultado que mejoró o empeoró solamente eso. La clase seis, esto que hablamos de la de la ética sería un análisis de riesgo.

00:26:06

lse posgrados: En anális de riesgo buscamos básicamente ver qué cuestiones éticas pueden pueden afectar al proyecto. No sé si por ejemplo estamos hablando de sistema de salud o como algunos sistemas, no sé, por ejemplo, veterinarios o o cuestiones que puedan tener o legales que puedan tener alguna repercusión en en el usuario, etcétera, si es bueno hacer el análisis de riesgo y tomar una medida una medida, digamos, de precaución o de mitigación. para para el riesgo, no se no se va a pedir mucho más que que se analicen entre tres y cinco riesgos previo a la medida y postmedida de mitigación y una simplemente simplemente eso, digamos, como para cerrar esta clase va a ser medio comodín si nos atrasamos en las clases anteriores desarrollo, ustedes sean compartir o más feedback conmigo. La clase es la que vamos a usar de comodim, digamos, la vamos a trasladar hacia el final y obviamente se va a quitar el requerimiento de si es que no no llegamos con el tiempo. Bueno, la clase siete va a estar enteramente dedicada a ver cómo van con el texto y con la presentación, digamos. Eh eh como dije, son siete secciones las que hay que hablar y el y el el borrador de PPT también tiene que tener cierta estructura. Hoy en día con los LLMs, digamos, con seguramente ustedes han usado, están usando para generar código, para generar documentos, eh realmente con con buen prompt, etcétera, la la las presentaciones se se mejoran un montón.

00:27:39

lse posgrados: Así que bueno, bienvenido el uso para de esa herramienta para esto, digamos. Sí, por la cantidad de trabajo, etcétera, capaz que no sé, tengan 5 o 10 minutos por alumno en la presentación final porque hay muchos trabajos individuales, entonces hay que ser bastante bastante breve en eso.
J.Pablo Zebraitis: Sí, profe.
lse posgrados: Consulta.
J.Pablo Zebraitis: Este, a ver, yo en general como estructuré la cosa son markdowns en el gitub este de documentos, o sea, igual hay que lo que tú exiges es hacer un PPT o podemos ir en la presentación mostrando los documentos directamente en GitHub.
lse posgrados: No, no, PPT, PPT. O sea,
J.Pablo Zebraitis: Okay,
lse posgrados: si busco que aprendan a comunicar en esa parte,
J.Pablo Zebraitis: perfecto.
lse posgrados: busco que sepan resumir cuál es el problema de negocio, la solución y un poquito la lo que llama el camino del héroe, digamos, el storytelling, decir, bueno, tuvimos esto, tuvimos estos riesgos, limitaciones, lo resolvimos así, la métrica nos dio tanto y se resuelve de esta forma, digamos, que compartan esa experiencia, digamos,
J.Pablo Zebraitis: Ah, perfecto. El público objetivo podría ser técnico, podría ser este gerencial o el estilo.

00:28:46

lse posgrados: Sí,
J.Pablo Zebraitis: O sea,
lse posgrados: claro.
J.Pablo Zebraitis: en este caso el PVT es más orientado a gerencial. eh un un es totalmente válido para para un entorno técnico.
lse posgrados: Pois. Okay. Y bueno, los criterios de evaluación, bueno, lo que hemos mencionado, la documentación, la presentación y y cómo mostramos, digamos, de la verdad que todavía no no no tengo mucha información para valorarlos, pero yo creo que el baseline de nuevo y lo lo conversamos al principio, quizás no estaban todos, es aquellos que desarrollan código, usen todas las herramientas que tengan. aquellos que no los ayudo a generar y conceptualizar el problema. Yo creo que son muy pocos los que no, casi ninguno, porque alguna parte de código algo se puede desarrollar aunque sea. Eh, digamos, van a contar con mi apoyo para como para desarrollarlo en ese sentido. Quédense tranquilos. Bueno, entonces al final se entrega un documento explicativo de siete secciones, una presentación en PowerPoint obligatoria, estas dos y como opcional, bueno, el el documento en colab, que creo que la herramienta más fácil para usar hoy en día, o un repositorio si es que lo han trabajado en local o han hecho algún alguna otra otro diseño para para aplicarlo.

00:30:10

lse posgrados: Esta presentación está en la carpeta de después se las comparto porque creo usted viste que entran donde están las asistencias hay un link a la carpeta en ese link a la carpeta están las clases y esta parte está detallada ahí también, pero era más o menos lo que lo que hemos conversado. dudas sobre el pipeline de la o requerimientos, porque nada, esto sea adaptativo, lo podemos ir adaptando. Bueno, entonces comencemos con la con la clase uno. En la clase uno, lo que vamos a hacer, básicamente, se lo se lo adelanto, es armar un canvas. ¿Ustedes tuvieron alguna vez acceso a lo que es un canvas para desarrollo, para ideas, para proyectos, para negocios, etcétera?
Gabi Tallarico: Sí,
lse posgrados: Es bastante es bastante explicativo.
Gabi Tallarico: sí.
lse posgrados: Levante la mano al que nunca vio un canvas o reaccionen al que nunca vio un canvas. Hay uno, Shimmon, Fede. Bueno, son son varios, así que lo vamos lo vamos a detallar bastante así. Igual es bastante explicativo. Este, no es un canvas aplicado a Llms, básicamente porque así lo medio que lo lo tñé o lo acomodé para que vayamos hacia ahí.

00:31:55

lse posgrados: Ahí vamos. Entonces, de nuevo, no, como cuando presento no puedo ver el chat, entonces simplemente prendan el micrófono y y hacen la consulta. Okay, acá me gustaría tener un poco de interacción porque hay algunas algunas preguntitas que que y también como para que nos vayamos nivelando sobre todo lo que vieron en la Dipllo. Vamos a hablar un poquito de lo que son de la inteligencia artificial y los LL, los LLMs, los grandes modelos de lenguaje, los tracks y los enfoques que que detecté en la en la encuesta que les que les realicé, ¿sí? Que bueno ya se los adelanté. Básicamente son agentes clasificación y RAC y uno visión por computadora. Eh, vamos a buscar definir bien el problema, ¿sí? para que después eh definido bien el problema, podemos buscar una solución micro que solucione, no quizás no todo el problema, pero parte del problema y ese ya hasta encaminado el proyecto hacia ahí. Vamos a ver el un canvas simplificado para como herramienta para formalizar cada proyecto y al final de la clase vamos a tener una ronda de presentaciones, algunos minutos por alumno para que compartan cómo cómo lo cómo lo han desarrollado. Sí. El entregable del día, de nuevo, no es un entregable obligatorio, más bien para obtener feedback.

00:33:24

lse posgrados: Él ficha el canvas con algún texto explicativo. Bueno, eh ustedes hace cuánto que vienen trabajando o que vienen usando IA me gustaría que no sé recibiera un poquito decir la usan día a día, la usan solamente para desarrollar texto, para procesar datos. ¿Tienen algún pipeline ya ejecutado? ¿Tienen algo automatizado? ¿Alguien que quiera
Shimon Achtung: solamente las plataformas,
lse posgrados: compartir?
Shimon Achtung: las interfaces conocidas, no, no sé si son inteligencias artificiales, CHPT, Gemini o Notebook M o Cloud, no sé, voy probando con cada uno de repente lo que vaya viendo,
lse posgrados: Y y pagas la pagas la suscripción o estás con los modos gratis.
Shimon Achtung: eh, no solamente Chap GPT, sí, Plan Plus lo tengo desde hace un año y medio.
lse posgrados: Claro. Okay. Okay.
Shimon Achtung: medio más o menos o un poco
lse posgrados: Ah, bueno, un año y medio ya. Y cuando aprendiste a usar algún criterio para hacer el promés la
Shimon Achtung: más.
lse posgrados: consulta, como eh o le mandas así cualquier así la
Shimon Achtung: No, no, no. O sea,
lse posgrados: consulta.
Shimon Achtung: a ver, en principio sí hago, trato de hacer GPTs o ahora proyectos donde le establezco un rol, le explico el contexto,

00:34:46

lse posgrados: Ah,
Shimon Achtung: le pido que no me abrume con las respuestas,
lse posgrados: okay.
Shimon Achtung: que sea preciso, que se enfoque en alguna parte de las fuentes que le estoy dando.
lse posgrados: Bueno, bueno, usuario moderado avanzado ya con armar proyectos y y configurar ya se está usando, digamos, alguien que lo use a nivel empresarial hacen alguna automatización.
Marcelo Luna: Sí, yo ahí puedo contar un poco mi experiencia. Nosotros en la empresa usamos hacemos uso de bastantes herramientas eh de variadas, ¿sí? Usamos Cloud, usamos Cursor, usamos Gemini, eh bueno, varias cosas, pero e hay todo un esquema también para crear skills y compartirlos a través de de servidores MCP. Entonces, digo, la idea ahí es buscar automatizar tareas eh repetitivas. Eh, yo para dar un ejemplo, eh, por ejemplo, recorrer un repositorio de código para generar un diagrama de arquitectura, para mostrar las dependencias de los elementos técnicos y ese tipo de cuestiones. Eh,
lse posgrados: Claro,
Marcelo Luna: después lo lo ¿Cómo?
lse posgrados: técnico, el trabajo ese,
J.Pablo Zebraitis: No.
Marcelo Luna: Perdón.
lse posgrados: muy técnico, digamos,
Marcelo Luna: Sí,
lse posgrados: de desarmar
Marcelo Luna: sí. Eh eh eso es muy técnico, pero digo, de ahí para arriba en el nivel de abstracción, obvio, hasta eh elaborar documentación, reportes, este evaluación de riesgos, hay un montón de cuestiones que vamos trabajando eh que un poco sobre la marcha se van desarrollando también, ¿no?

00:36:28

Marcelo Luna: nos dan suit de herramientas y la premisa es bueno,
lse posgrados: Так.
Marcelo Luna: okay, tenés libertad para crear los skill, para usar las herramientas, para definir automatizaciones, para lo que quiera, que después son son puestas a disposición del resto para que las pueda usar.
Santiago Germino: Eh, tengo tengo una pregunta para Marcelo,
lse posgrados: Sí,
Santiago Germino: perdón, por ahí no es este oí eh porque estás hablando de de un
lse posgrados: sí, sí.
Santiago Germino: montón de de generación de un montón de de cuestiones de documentación,
Marcelo Luna: ¿Te
Santiago Germino: ¿cómo cómo es que están seguros o se aseguran de que esa documentación es exactamente es correcta, digamos, técnicamente correcta?
Marcelo Luna: referís a la documentación generada?
Santiago Germino: Claro, los diagramas,
Marcelo Luna: Ah, bueno,
Santiago Germino: el tema arquitectura.
Marcelo Luna: la la premisa es que en cada producto que sale de ese tipo de automatizaciones tiene que ser revisada por alguien con el conocimiento arquitectónico.
lse posgrados: Claro.
J.Pablo Zebraitis: Eh, yo yo estoy en una situación similar a la tuya. Este, básicamente hace una semana, por ejemplo, la gente de la fundación Linux este trabajó el tema este respecto a la responsabilidad
Marcelo Luna: H
J.Pablo Zebraitis: del código este expuesto por un programador y este y bueno, trazó algunos lineamientos de la responsabilidad, digamos, de la persona que que hace eso y la forma en que debería documentarse la coparticipación de de la IA, este, respecto a modificaciones de código en particular, ¿no?

00:38:00

J.Pablo Zebraitis: Nosotros también trabajamos con skills, este,
Marcelo Luna: Mhm.
J.Pablo Zebraitis: trabajamos definiendo políticas en repos globales para que luego en todos los repos hijos, digamos, implementen esas políticas que automáticamente trabajamos mucho con Cloud, este, a pesar de que también tenemos semina y también tenemos este Copilot, este hacemos revisiones cruzadas de de de una contra otra, o sea, por ejemplo, hacemos código con cloud y cosas por estilo, después lo tiramos al repo, el repoaliza este copilot, copilot hace observaciones Lo tom que critique lases de más allá de todo eso hace una persona.
lse posgrados: Creo que el punto común,
Marcelo Luna: Ch
J.Pablo Zebraitis: No.
lse posgrados: el punto común en todos y desde hace dos años en adelante es que esto no ha cambiado la forma de trabajar o quizá la la confirmación es que quizás somos más productivos, o sea, producimos producimos más. No sé si hay alguien que no esté de acuerdo en que produce más hoy en día con
Shimon Achtung: Sí, en mi caso lo que yo noto es que ante la dificultad de producir eh yo lo
lse posgrados: esto.
Shimon Achtung: que le pido al chatt o a cualquier interfaz de chat que haga empiezo a corregirlo y empiezo a hacer a partir de eso.
Marcelo Luna: Sí,
Shimon Achtung: Cambio de rol ahí.

00:39:15

Marcelo Luna: yo yo pongo un ejemplo que para mí es es en mi trabajo en particular eh digo,
lse posgrados: Claro.
Marcelo Luna: lo que me pasaba era ir a un cliente y capturar toda la información para elaborar una vista arquitectónica y lo que me tomaba un montón de tiempo era armar los diagramas, dibujar,
Shimon Achtung: Yeah.
Marcelo Luna: que todo quede estéticamente más o menos razonable. Ahora se lo tiras a un MCP de droga y es le sale más lindo que a mí ocupando una semana de dibujar.
lse posgrados: Claro. Voy a hacer frontend o
Marcelo Luna: No, no, no, no, no construyo código.
lse posgrados: diseño.
Marcelo Luna: Eso yo. Claro, es una mirada arquitectural y y más de arquitectura empresa inclusive,
lse posgrados: Diseño.
Marcelo Luna: pero más
lse posgrados: Claro. Sí, sí, sí.
Marcelo Luna: estratégica.
lse posgrados: Yo creo que la digamos el que diga que no que no no aumentó la productividad, no, eso no es cierto. Si no no nos lleva hacia eso, pero bueno, en definitiva lo que viene esto es a de alguna forma, no sé si a reemplazar, pero porque es como que suena duro y y no creo que no seamos 100% reemplazables, pero sí viene de alguna forma a reemplazar tareas que antes no aportaban tanto valor, digamos.

00:40:28

lse posgrados: Hoy en día la, digamos, nuestro conocimiento por nuestra experiencia aporta más valor que lo que podíamos desarrollar por por el propio código, digamos, ¿no? Incluso eh casi muchas veces el código que desarrollan las plataformas, digamos, está bastante bueno. Obviamente si agarramos un super senor de desarrollo me va a matar, pero pero no ahorra mucho tiempo, digamos. No es lo mismo escribirlo de cero que escribir algo y después empezar a ir, porque a todos debe haber pasado que desarrollamos algo, un texto, lo que sea y después tenemos que ir como ajustándolo a lo que realmente queremos. digamos, no creo que esa es un un punto común, digamos,
J.Pablo Zebraitis: Otro punto, otro punto importante es que si la documentación este del código está cerca del código con con IA, es que muchas veces no solamente resolvés un tema, sino que adjunto también resolvés que la documentación quede correcta y que los casos de test queden correctos todo de una sola vez. Y eso en un equipo de desarrollo a veces es bastante complicado, o sea, eso está bueno porque además eh respeta reglas mucho más que humanos, por ejemplo,
Marcelo Luna: Yeah.
J.Pablo Zebraitis: y eso también está está bueno en el equipo de desarrollo, o sea, que no solamente aumenta la productividad, aumenta, digamos, la eh el dinamismo y la calidad.

00:41:41

lse posgrados: la calidad.
Marcelo Luna: Perfecto.
J.Pablo Zebraitis: Yeah.
lse posgrados: Claro. Exacto. Para Cuba se usa un montón. O sea, nosotros, por ejemplo, en en la empresa donde trabajamos, nosotros desarrollamos procedimiento, no sé, para cuidado del medio ambiente, etcétera. Y antes, ah, escribir procedimiento, ya era un y era medio digamos un tiempo que tenía que uno está escribiendo, ¿no? Entonces hoy, digamos, delegado eso y ajustándolo, la verdad que está ayuda un montón. Pero de nuevo, a lo que voy con esto es que ustedes han notado que que digamos que por cada proyecto, por cada contexto que uno va trabajando, esto se va haciendo más específico y de alguna forma nos va reconociendo, ¿no? O sea, eh hay como hay como como un como que cada uno de nuestros chats, por así decirlo, de nuestra herramienta, ya nos conoce un poco más, digamos, ¿no? Y eso lo hace matemáticamente a través de probabilidades, como seguramente vieron en en la en las clases NLP con los Transformers y todas las todo lo que surgió a partir después de los Transformers. Eh, lo que yo creo y este es un punto de vista personal que en la variabilidad eh también hay algo que enriquece y eso es lo que yo creo que sí se pierde, digamos, ¿no?, en la variabilidad de ideas, etcétera.

00:43:01

lse posgrados: Entonces, por ahí todo el tiempo que ganamos en en, no sé, mi equipo de trabajo, todo el tiempo que ganamos en desarrollar por ahí lo digamos lo ocupamos en discutir nuevas medidas, por ejemplo, y hay cosas que no se delegan, digamos, ¿no? Me parece que eso es como una un insight que que quería que les quería compartir. Bueno, en volviendo, volvemos en este curso lo que vamos a a aplicarlo básicamente es a Raxs, a clasificación todos los proyectos que vi están en procesamiento en lenguaje natural, agentes, etcétera, digamos. Así que vamos a estar casi enfocado en eso. Sí,
Marcelo Luna: Hm.
lse posgrados: como vieron seguramente en la primer materia, todo aparte de de datos, entrenamiento, ¿sí? donde digamos se define un algoritmo, se lo se lo entrena, digamos, y se hace una evaluación y a partir de eso se hace una inferencia, ¿cierto? Eh, lo mismo aplica para lo para para todo lo que es eh generación generación de texto. Sí, hace exactamente lo mismo los Transformers los que van prediciendo la probabilidad de la palabra siguiente según un contexto indicado y según el entrenamiento que tuvo, digamos. Entonces, en definitiva, no no nos hemos ido mucho más lejos de lo que un machine learning típico, digamos, que que es una un aprendizaje por entrenamiento y reconocimiento de patrones, ¿no?

00:44:25

lse posgrados: E los invito, les dejé esto en la presentación, hay una una plataforma que se llama Datacamp. aquellos que ya yo creo que ya quizás esto un poco obsoleto en el sentido de que hoy aprender a codear no es tan necesario, pero cuando yo empecé no hace cco o se años atrás y y no estaba todo estas herramientas para generar código y y era era complejo, digamos, eh entrar a est overflow y empezar a ver cómo se solucionaban ciertos problemas. Ya esto pareciera que fue hace, no sé, 15 años atrás y fue hace 3 años, digamos, cuatro, ¿no? Eh, esta plataforma llama Datacamp para aquellos que están iniciando y los que manejan volúmenes de datos chiquitos, digamos, para hacer gráficos reporte, aprender a usar funciones de Python y cuestiones sencillas, digamos, de baja escala, viene muy muy bien. Sí. Eh, le dejé los enlaces. El datacamp.com es una muy buena plataforma. No recuerdo en cuánto cuánto cuesta anualmente ahora. Creo que $50 anual creo que es o algo por el estilo y hay como un autoaprendizaje ahí. Y la verdad que está a mí me ayudó un montón al principio cuando empecé a meter y a tratar de entender un poco el código.

00:45:45

lse posgrados: Vieron, vi algunas clases de de la materia anterior, pero de la primer materia no vi los videos, honestamente. Pero digamos, aprendieron lo que es un aprendizaje supervisado, no supervisado, problema de regresión, problema de clasificación, etcétera.
Gabi Tallarico: Sí, los explicaron. Eso no quiere decir que lo
Shimon Achtung: Sí.
Gabi Tallarico: sepamos.
lse posgrados: Okay, okay, está bien. Sí. Bueno, en en digamos son digamos en ocho clases ver todo eso y más algo de exploración etcétera, debe ser un desafío grande, pero bueno, lo lo
Shimon Achtung: Quizás más, perdón, no,
lse posgrados: Sí.
Shimon Achtung: en la en el segundo bimestre quizás se vio más en el análisis de datos eh
Gabi Tallarico: Claro.
Shimon Achtung: todo esto del tipo clasificación y regresión logística con data mining. Quizá una de las últimas pueda aclarar un poco lo que vimos.
lse posgrados: Claro. Okay. Sí, sí. Yo yo creo que la clase de la próxima la clase de de EDA voy a tomar algunos minutos. Voy a agregar que me dicen esto, algo de visualización de datos, aquellos que trabajan con números, tabla y cosas. Siempre viene bien tener algunas líneas guías hacia cómo explorar los datos, digamos.

00:47:08

lse posgrados: Sí. Así que en eso en eso eh puedo aportar bastante. Quizá el modelado eh el modelado surge después de de exploración porque a partir de exploración uno puede más o menos orientarse a si va a usar al tal o cual modelo, si hay un problema de clasificación o si un problema de regresión. O sea, que básicamente la el supervisado, el aprendizaje supervisado se si yo voy a predecir categorías, digamos, una variable categórica, una variable continua, una regresión, una variable categórica, clasificación y después el no supervisado, básicamente lo que hace y digamos en palabra sencilla es agrupar por parecido, o sea, agrupar cosas que matemáticamente o algebraicamente son similares, como lo que se hace en los racks cuando se busca por similaridad coseno, como vieron en las clases anteriores. Bueno, eh el aprendizaje no ha supervisado la parte del clustering, hace eso con distintos métodos, distintas formas de medir distancias, cómo están separados uno del otro, etcétera. Eso es importante, pero para su claridad les puse estos enlaces que que está bueno saberlo porque si digamos si yo digamos en algún correo que compartí con con algunos compañeros es si tengo una herramienta que es sencilla, no sé, un modelo muy sencillo de clasificación es árboles de decisión que son reglas lógicas por variables continuas o categóricas, si es mayor, menor o igual a, entonces clasifico así o sea, es un modelo muy sencillo y si funciona eso no no voy aplicar un modelo más complejo, como por ejemplo Xibus, que realmente es complejo, digamos, ¿no?

00:48:46

lse posgrados: Entonces, eh lo mismo aplica para el procesamiento de lenguaje natural. Si yo de repente eh evito usar un LLM y consumir tokens de alguna aplicación o de algún servidor y lo puedo resolver con un transformer de uso gratis que funcione moderadamente bien, ¿para qué voy a hacer algo más complejo? No, entonces también es ese criterio un poco lo que vamos a conversar cuando cuando empecemos cuando empieza a dar vuelta por por la por los grupos. Bueno, esto cambió muy rápido, un poco lo hemos hablado del 2024 en adelante. Eh, realmente en dos años esto cambió y va a seguir va a seguir cambiando, digamos, ¿no? E a mí no deja de sorprenderme, honestamente, digamos, ¿no? Y me imagino los que trabajan en IT con todo el desarrollo, creo que hay impactó bastante bastante más, pero creo que en definitiva y por debajo de todos los algoritmos eh siempre, digamos, hay hay conceptos básicos como el de back propagation, que básicamente es como cómo se actualizan las redes neuronales para que esto aprenda, digamos, ¿no? Y por debajo de eso no deja de ser máquina de Touring, digamos, donde uno le dice si pasa esto, hace tal cosa, aprendiendo a través de otros parámetros.

00:50:06

lse posgrados: Entonces por ahí, digamos, no esta generación o esta acumulación de conocimiento en los LLM que están disponibles para de alguna forma democratizar el conocimiento no está generando nuevas cosas o o por lo menos por ahora no. Si ha descubierto Inside, se ha descubierto, puede ayudarnos, pero de alguna forma todavía están al servicio nuestro, digamos, ¿no? Esa como ese miedo que existe del Skynet, etcétera, creo que está lejos de pasar todavía, pero sí no hay no hay ninguna duda que estamos viviendo una transición en la que de alguna forma hay que tratar de comprenderlo. Por eso están ustedes acá para aplicarlo en nuestros trabajos, nuestro desarrollo, en nuestra vida, digamos, de alguna forma. Bueno, y eso me viene a decir, bueno, ¿cuándo para qué es bueno la IA? Sí, digamos, para que cuando hay cuando hay muchas reglas para programar manualmente, cuando hay patrones que donde hay no hay una regla clara, trabaja con texto porque son cuestiones que no son tan matemáticas, hay que transformarlas, digamos, ¿no? Eso es bastante complejo. Entonces, para ese tipo de cuestiones, sí, pero ¿cuándo no debo usarla? Creo que por ahí es importante que esto se haga en la autoprenda. digamos, si hay una regla, si digamos, si hay algo simple, sí, como un filtro en Excel, para qué uso una ya no no gasto tokens haciendo eso, digamos, ¿no?

00:51:31

lse posgrados: Porque también a nos nos perjudica. A ver, yo lo veo día a día, a veces tengo una cadena de correo electrónico super larga, le pido que me la resuma. Bueno, hay cuestiones que por ahí hay que uno tiene que ir viendo hacia adentro y decir, "Bueno, para esto sí, para esto no, digamos, ¿no? Eh, también cuando esto es importante, cuando la transparencia es obligatoria, eh, muchos modelos no son muy explicativos, no son muy demostrables, digamos. Hay hay un un sinfín de de ejemplo de modelo en los cuales no tienen una explicabilidad. Entonces, ante una auditoría es complejo de demostrar. Bueno, en lo que es procesamiento en lenguaje natural, básicamente el pipeline es este procesar, entender y generar. Nosotros buscamos generar un texto a partir de documentos que se ha presentado, que se han se han procesado en en los RACs. Ah, yo creo que en este en este punto particular hay mucho para mejorar, al menos los proyectos que que algunos proyectos que he visto. De nuevo, no es lo mismo meter un PDF completo que tratar de urgar dentro de ese texto y tratar de de separar componentes de texto que ayuden a que el sistema funcione mejor, digamos.

00:52:48

lse posgrados: Eso lo vamos a ver. un poquito más cuando cuando el grupo.
Gabi Tallarico: No,
lse posgrados: Sí.
Gabi Tallarico: ahí justo estás como tratando una de las preguntas que yo le hacía, creo que en la en la última materia se las hacía e que era justamente, digo, ¿en qué casos convenía hacer lo que estábamos haciendo tratando de armar micolap y todos los los chang y los rage y demás? o agarrar ese PDF y no sé y trabajar con un notebook LM que tenía mejores resultados que lo que estaba haciendo. O digo, "¿Y si esto se lo pongo a un agente ya prehecho en Copilot?" Me daba mejor que todo lo que estaba como armando. Sentía como que las materias iban en un, no sé, por un carril y las herramientas que yo tenía eh o tengo disponibles van por otros. No logré todavía conectar cuándo usar una cosa y cuándo usar otra. Y es más,
lse posgrados: Yo creo que Ah,
Gabi Tallarico: siempre me estoy me tiraba por ahí a usar estas herramientas generalistas
lse posgrados: sí, sí.
Gabi Tallarico: porque me daban mejores resultado que lo que estaba
lse posgrados: Bueno, te doy te voy a dar un ejemplo claro.
Gabi Tallarico: haciendo.

00:53:57

lse posgrados: Eh, cuando vos tenés que procesar 12 PDFs a al notebook LM se lo podes poner, digamos, no en ese caso son cientos o o miles. Tenés que tener una algo que que escale.
Gabi Tallarico: Claro.
lse posgrados: Quiero que que la respuesta es que Notebook LM no va a escalar y que tu y tu y que de alguna forma tu arquitectura la que vos planeaste, que es como naiv, digamos, ingenua o inicial o vainilla, como se le dice, eso que es inicial podría escalar más, digamos. Sí, esa es una posible respuesta. Y ahora esa sensación que tenemos que bueno, p****, estoy aprendiendo esto y ya va a salir el nuevo cloud, que nada, no voy a tener que prender inteligencia artificial para utilizarlo. hago pregunta o me diseña los prompt según mi especialidad y esa sensación la van la vamos a seguir teniendo, la tenemos todo el tiempo y creo que es importante entender qué es lo
Gabi Tallarico: Estoy sola.
lse posgrados: que No,
Gabi Tallarico: No estoy sola haciéndome preguntas.
lse posgrados: no, pero pero por favor no, no, pero yo creo que no hay que perder las bases, digamos, eh, y por ahí va la ahí va el hecho de de tratar de hacer un algo que sea mínimo, chiquito, escalable, pero que funcione, que vos sepas que que vos que tengas cierta explicabilidad, digamos.

00:55:18

lse posgrados: Te doy un ejemplo puntual en en el caso Gabi, en el caso tuyo del del texto, muchas veces cuando yo vi con R colab, etcétera, y me fijé, parte del texto no tenían sentido. Sí, o sea,
Gabi Tallarico: Mucho.
lse posgrados: parte del texto como que cortaba y no tenía mucho sentido, ¿cierto? Bueno, pero podes usar quizás la la misma filosofía antes y decir,
Gabi Tallarico: Sí.
lse posgrados: "Bueno, voy a sacar la parte del texto y hacer un resumen que realmente aporte valor." Y eso el que eso es lo que va a alimentar mi modelo y no un pedazo de texto que
Gabi Tallarico: Aha.
lse posgrados: justo el el chank lo cortó a la mitad de la palabra y y me y me quedó incomprensible, digamos. Entonces, eh obviamente si a una escala chiquitita Notebook LM va a
Gabi Tallarico: No, no, digo esto.
lse posgrados: funcionar.
Gabi Tallarico: Por eso yo digo, este es un ejemplo de 12, pero nada, nosotros tenemos 5600, creo, PDF más o menos la escala, ¿no?
lse posgrados: Bueno,
Gabi Tallarico: A donde habría que apuntar. Obviamente que estamos lejos de eso.
lse posgrados: para para mi trabajo final de de de procedimiento de lenguaje natural tres de la

00:56:26

Gabi Tallarico: Ya te vamos a
lse posgrados: especialidad,
Gabi Tallarico: contratar.
lse posgrados: lo que hicimos fue procesar eh boletines oficiales de la de la provincia de Salta, que ese va a ser un un ejemplo para aquellos que no tengan trabajo, digamos, no tengan trabajo final. Esa es una posibilidad y realmente, por ejemplo, para un abogado que tiene que sentarse y leer el documento, pero vos imagínate que si el abogado tiene que tirar los últimos 10 años del boletín oficial para una auditoría al gobierno,
Marcelo Luna: H
lse posgrados: por ejemplo, no sé, para ver contrataciones o para buscar eh edictos judiciales del último mes. Si ya tenés mucho volumen de información, digamos, todo lo generalista que es notebook LM pierde especificidad y en escabelabilidad, digamos, ¿no? Por entender un poquito esta arquitectura quizás te permita a vos decir, bueno, che, tengo que buscar un desarrollador que me haga esto y vos lo deco, necesito un sistema rag al cual le ingresen los t y vos lo vas a controlar de una mejor forma. Capaz que no lo puedes desarrollar vos. Esa es la realidad. una diplomatura de pocas materias, no no no lo va a poder hacer, digamos, quizás no a una escala micro, sí,

00:57:39

Gabi Tallarico: No, no, no pretendo tanto,
lse posgrados: pero sí,
Gabi Tallarico: eh, no pretendía hacer eso. Los 5000 documentos.
lse posgrados: pero al menos sabes cómo funciona hacia ahí,
Gabi Tallarico: Sí,
lse posgrados: digamos,
Gabi Tallarico: sí.
lse posgrados: ¿no? ¿Alguien más? ¿Alguien más iba a hacer un
Marcelo Luna: No, sí, yo iba a agregar algo porque eh digo,
lse posgrados: comentario?
Marcelo Luna: creo que lo que lo que dice eh va un poco en línea con algo que yo también eh eh percibo percibí durante la cursada. Eh, pero digo, yo estoy en el otro extremo. Yo tengo que procesar muy poco PDF, pero lo tengo que procesar de una manera muy específica. Vos ya viste mi trabajo y me hiciste un comentario y de hecho todo lo que vos me comentaste es más o menos lo que tenía como como previsto para hacer en esta en esta materia. Ahora, la realidad es que sea Notebook LM o sea alguna otra herramienta, eh hay performance notablemente diferente entre una herramienta y otra. Y por ahí, esto lo digo desde mi lado personal, eh por ahí lo que hubiera sido más útil es, además de entender cómo construir todo el mecanismo del RA y hacer la ingesta, entender que por ahí a veces conviene dárselo, por ejemplo, un notebook LM y hacer una conexión MCP y consumir lo que lo que esa

00:59:00

lse posgrados: Claro.
Marcelo Luna: plataforma genera. digo, no digo en todos los casos, pero justamente es bueno, en qué casos sí, en qué casos no. Yo,
lse posgrados: Claro.
Marcelo Luna: por ejemplo, sentí falta de Yeah.
J.Pablo Zebraitis: Sí. Este, sumando a eso, yo ya en el proyecto que que tengo armado, este, tengo una evaluación de modelos corriendo localmente con Oyama contra API de Gemini y una evaluación de costos de cuánto me costaría y los tiempos y todo lo demás. Y y realmente digo, mi conclusión hoy es que por el volumen de de casos que tengo que analizar, el tiempo que me demora y el costo de de implementar una solución in house, este no tenía sentido. O sea, hice la prueba localmente con equipos sin GPUs y bueno, fue fue un desastre, o sea, sucedió y lo hice y está está testeado, está monitoreado, está medido, pero luego con Gemini también lo hice y bueno, y laación de costos no tiene sentido hacerlo con con una cosa local.
lse posgrados: Sí, digamos el ejemplo local, yo tampoco estoy de acuerdo, honestamente, porque por ahí uno saca la API la API key de cualquiera y muchas tienen free tire, o sea, no se pagan para al menos para los ejemplos de digamos de práctica que usamos nosotros. me me parece bien que exploren otras soluciones y que y que esa y esa propia conclusión que sacaste que para qué lo voy a hacer local y si no básicamente el costo es cero o muy poco, eh me consume muy pocos token en mi trabajo,

01:00:42

lse posgrados: también es una propia es la propia conclusión. Ahora yo recibo feedback y está bueno que me lo den para que en las futuras digamos digamos ediciones de la diplo incorporemos esta herramienta. Yo no sé si MCP es algo para digamos como para tratar en en una diplo. Sí, obviamente hay me parece que la diplo está más orientada a entender cómo funcionan los sistemas más que para más que como para diseñarlo y ejecutar algo que sea en producción, digamos, ¿no? más que nada para entender y conceptualizar y armar una prueba de concepto y que ustedes si en sus trabajos tienen que consultar algún experto, al menos hablen un idioma parecido al experto para que puedan ayudarlo, digamos,
J.Pablo Zebraitis: Eh, perdón, Santiago, tú tenías levantada después, Santiago.
lse posgrados: No.
Santiago Germino: Hola.
J.Pablo Zebraitis: A ver,
Santiago Germino: Sí,
J.Pablo Zebraitis: no.
Santiago Germino: sí, acá estoy, acá estoy.
J.Pablo Zebraitis: Gracias.
Santiago Germino: Eh, no, no, yo quería comentarles en cuanto al tema de justamente yo lo que estoy tratando de hacer es hacer uso local de de un modelo del LM y sinceramente después de haber usado mucho e, ¿cómo se llama? Eh, opusionet 4,5 4,6 eh el el en W 3,5 es tan bueno o quizá en algunas cosas mejor.

01:02:06

Santiago Germino: Y el problema que yo tengo es que yo lo estaba corriendo,
lse posgrados: Oh.
Santiago Germino: eh estaba pagando el el copilot y eh lo estaba usando. La verdad que no no bastaba nada, pero porque yo estaba todo el tiempo encima de la yo la estaba corrigiendo todo el tiempo. Si yo la dejo hacer eh y la dejo investigar y la dejo divagar, me consume los tokens a lo loco. Y entonces en este proyecto eh surgió el tema de correr lo local por un tema de que el costo se iba a las nubes. va a ser imposible pagarlo. Calculé más o menos, no sé, 5000. Una cosa absurda dejar correr correr este un modelo generando tokens todo el día. Eh, ¿qué es lo que creo que le está empezando a pasar a las empresas que dicen, "Bueno, dejemos eh no sé, agentes corr?" Claro, dejémoslo correr,
lse posgrados: Volvamos.
Santiago Germino: que hagan algo, déjenlo, dejémoslos eh sin asistencia y a ver qué hacen en cuando lo hagan y le está generando unos gastos que que de repente capaz que hubiese sido mejor este, no digo no usar la guía, pero sí usar a alguien con la experiencia suficiente para poder guiar a la guía y que la guía se vea mucho más barata.

01:03:13

Santiago Germino: Entonces, tenés lo mejor de dos mundos. es la aceleración de la guía con la dirección de alguien que que tiene experti en el área.
lse posgrados: Yo creo que en definitiva eso es lo importante, decir, bueno, cuándo conviene y cuándo no. que la variable económica está ahí, pero si sí creo que por ahí ya el el uso de los modelos locales eh va va a ir en detrimento porque el precio de los modelos que son más específicos y más complejo es eh ya es sumamente bajo, digamos, dependiendo también de la escala del proyecto, ¿no? Pero eh no está mal tampoco aprender a bajarse uno el local y que de alguna forma te ayude, opere. Igual tarea simple, digamos,
Santiago Germino: Claro, el tema también es el hardware. Si uno tiene hardware, se baja cualquier modelo y lo corre y tiene resultados buenísimos. Ahora tenés,
lse posgrados: crack.
Santiago Germino: no sé, $,000 para meter en hardware y mejor pago un pago mensual porque no no lo no lo no lo logro este amortizar.
J.Pablo Zebraitis: Bueno,
Santiago Germino: Ok.
J.Pablo Zebraitis: no solamente eso, sino que vos planteaste un escenario en el cual tenés todo el día corriendo algo, haciendo cosas autónomas. En particular, yo para lo que necesitaba en este caso son llamadas específicas de un datet de que tiene este cosas multimodales, o sea, imágenes más texto más todo, o sea, eso ya me requiere determinado tipo de procesamiento local, determinado tipo de modelo este y además son, yo sé, 10 hits que llevan, no sé, eh, 30 segundos resolver a un Gemini, por ejemplo, este, por día, por lo que en ese caso jamás se podría este amortizar una inversión de de

01:04:55

J.Pablo Zebraitis: un en torno de lo que tú estabas diciendo a nivel de del producto, ¿no? O sea, tener claro qué es lo que tenemos que que diseñar, cuál es realmente el uso de la idea que le vas a dar específicamente para esto, cuánto tiempo tenés que consumir, la cantidad de toques y optimizarlo correctamente. Respecto a la otra pregunta que decías tú, profe, este, de si la si la diplomatura está bien mal o bien orientada malentado fuera, es yo lo que veo acá es una teorogenidad muy grande y y tal vez como que tenía que haber dos tipos de diplomaturas de A. Una es más a lo que vendría ser los fierros, como lo que estuvimos viendo muchas veces este en el curso para atrás, o sea, a nivel matemático, a nivel de cómo funciona y todo demás y otro más orientado a lo que vendría a ser la práctica y el uso eh de modelos existentes o cuándo decir una cosa y la otra y más a la práctica de cómo resolver problemas más reales. es mi punto de vista,
lse posgrados: Gracias. Sí, sí, viene bien el feedback, viene bien y lo lo digamos no solo no solo entiendo que no solo han hablado de esto en esta materia, sino en otras también. Créame que se está trabajando, se está trabajando en eso.

01:06:00

lse posgrados: De nuevo, nosotros o mi propósito es tratar de encontrar un un punto medio entre los que ya son tienen todos los fierros y todo el toda la cuestión de hardware y software ahí el código y aquellos que están empezando se están empezando a animar, hay que encontrar un punto medio, ¿no? Entonces, en eso les pido colaboración, así vamos todos juntos. Bueno, en definitiva, en NP, perdón, déjame que explique un poquito más. Eh, han visto a digamos saben que se pueden resolver problemas de clasificación de texto, reconocimiento de entidades, búsqueda semántica, ¿sí? y generación de texto. Esto esto lo han entendido, quedó comprensible en la materia anterior y obviamente los RACs que como la una s solución
Shimon Achtung: A mí me falta un par de golpe de horno,
lse posgrados: y
Shimon Achtung: pero lo vengo siguiendo. Eh,
lse posgrados: hay alguien hay alguien que no comprenda cuando yo le digo, bueno, que un problema de clasificación con contexto. Bien.
Gabi Tallarico: No,
Shimon Achtung: Eh,
Gabi Tallarico: no.
lse posgrados: Estamos, digamos, no iba a decir algo,
Shimon Achtung: He.
Gabi Tallarico: Sí que por ahí cuando hagamos esto los canvas estaría bueno que los comentemos,

01:07:19

lse posgrados: Gavid.
Gabi Tallarico: que nos demos un ratito para comentar qué está haciendo cada uno, porque está es rico la comparar los proyectos, ver en qué lo están aplicando, que eso no lo hicimos, no esperar las seis clases, sino hacerlo ya la clase que viene o la otra
lse posgrados: Sí, sí, sí. Ahora compartimos, ¿no?
Gabi Tallarico: No.
lse posgrados: Hoy en la últimos 30 minutos vamos a compartirlo porque también de lo que yo revisé las clases anteriores entiendo que esta posibilidad de interacción no ha estado tan presente porque ha habido tiempo de desarrollo, de explicación, código, notebooks, etcétera. Entonces, mi propósito es esto que estamos haciendo ahora, yo escucharlo ir adaptando también un poco el contenido según lo que vaya escuchando, digamos, ¿no? Pero en definitiva, si ustedes han entendido procesamiento de lenguaje natural, podrían ejecutar cualquier o desarrollar una herramienta chiquita, muy chiquita, en colab, reconocer entidades, búsqueda semántica y generación de texto a partir de eso, digamos, ¿no? Obviamente los más avanzados pueden hacer mucho más que eso, pero en definitiva una partecita hace eso, digamos, no es como un engranaje reloj hace una parte de esto. Obviamente si subo mucho engranaje tengo un problema complejo, pero en definitiva es lo que hace el procesamiento de lenguaje natural más menos algunas cosas más, digamos, ¿no?

01:08:54

lse posgrados: Bueno, los modelos ya los conocen. Vi que no estado usando consulta alguien. Cuando yo digo API Key de un modelo, no entiende qué es. Todos saben conectarse, o sea, todos han sacado un AP key de alguna plataforma para para usarla.
Shimon Achtung: A ver, a mí me pasa que cuando no puedo explicar algo me parece que no lo entiendo, pero vi algunas
lse posgrados: O sea, vos, o sea,
Shimon Achtung: cosas.
lse posgrados: entendés que, por ejemplo, en vez de bajarte un modelo local, te bajas una piquí, hacés un par de sentencias en el código, ese código se conecta a través de internet, manda información y te devuelve información y te evita tener que trabajar en un modelo local, digamos.
Shimon Achtung: Claro, una API la considero como una interfaz básicamente y una que
lse posgrados: Claro. Ex.
Shimon Achtung: conecta como conectar el volante con el motor con el árbol de levas,
lse posgrados: Sí,
Shimon Achtung: digamos.
lse posgrados: exacto, exacto. Sí, es útil que sepan esto porque eh no sé,
Shimon Achtung: Ok.
lse posgrados: por ejemplo, la de Gemy tiene un free tire y por ahí es más sencillo usar esa, digamos, o pagar la de GPT, que también sale dos mangos antes que usar.

01:10:11

lse posgrados: o la ama, digamos, ¿no? Eh, eso es importante, digamos, porque por ahí en en digamos los en en en la mayoría de los
Shimon Achtung: H
lse posgrados: casos no va a haber tantísima diferencia. Es un problema sencillo, pero si son problema más complejos, quizás conviene ahí. Ahora le hago otra pregunta que viene un poquito más allá. Eh, cuando cuando se habla del espacio vectorial para llevar los embedings a esas dimensiones, ¿han trabajado con algún servicio o lo han trabajado en local en las notebooks?
Shimon Achtung: En local trabajó poco, pruebas muy chiquitas,
lse posgrados: ¿Algún servicio parecido de base de datos vectorial en la nube,
Shimon Achtung: ¿no?
lse posgrados: digamos?
Shimon Achtung: uso los a través de interfaces de la nube. Sí.
lse posgrados: Okay. Bueno, buenísimo. Bueno, ah, saben lo que es toquenización, saben lo que es embeding, digamos, eso es, digamos, sobre todo lo que es un embeding,
Shimon Achtung: He.
lse posgrados: deberían deberían deberían tenerlo claro, digamos, ¿no? ¿Qué qué es un embeding? ¿Quién me puede definir que es un embeding?

01:11:36

lse posgrados: Anímense, tiren cualquiera. No importa para acá
Shimon Achtung: lo cómo es algo PR clustering que va agrupando
lse posgrados: para
Shimon Achtung: eh ciertos vectores por sentido, digamos.
lse posgrados: Está cerca, está cerca,
Shimon Achtung: Sí.
lse posgrados: está cerca, pero no tan cerca, digamos. Eh eh está adelante,
Marcelo Luna: Eh,
lse posgrados: está en la fase siguiente, tiene sentido lo que decís, pero esto es una fase atrás, digamos. Alguno de de de de los que sabe lo que es un embeding o tiene
Shimon Achtung: Hm.
lse posgrados: confianza para para explicar lo que es un edi
Marcelo Luna: confianza.
Shimon Achtung: Gracias,
Marcelo Luna: No.
Juan Pablo Rueda: Yo no sé cómo definirlo técnicamente,
Marcelo Luna: Ah, dale, dale,
Juan Pablo Rueda: pero me da la sensación de que es subir información,
Manuel Babuglia: Es
Marcelo Luna: dale.
Juan Pablo Rueda: subirle la la información a al LM. M.
lse posgrados: está cerca todavía. Y si agamos una más, si no lo explico.
Marcelo Luna: Ah, de vuelta.
Manuel Babuglia: eh a dale Marcelo,
Marcelo Luna: No, perdón, perdón. Dale, dale.
Manuel Babuglia: dale Marcelo.

01:12:36

Marcelo Luna: No, no. Dale, dale, dale,
Manuel Babuglia: Eh, a ver, mi intento. es un vector de unas cuantas dimensiones,
Marcelo Luna: dale.
Manuel Babuglia: típicamente,
lse posgrados: Okay.
Manuel Babuglia: no sé, 300 para arriba tal vez,
lse posgrados: Ajá.
Manuel Babuglia: donde todo el el las palabras del modelo o las frases del contenido quedan eh en una representación espacial donde si palabras eh eh similares mantienen ciertas relaciones espaciales, como por ejemplo rey con reina, este hombre con mujer, etcétera. aquello de que si cualquier cualquier palabra pudiera tener,
lse posgrados: Okay.
Manuel Babuglia: por ejemplo, de si es una fruta o no es una fruta, es un animal o no es un animal, es un animal de cuatro patas, color, todas esas dimensiones, pero eh no con significado para los humanos, sino para la computadora, digamos, porque en definitiva no son dimensiones que se puedan mapear uno a uno con eso que que sí entendemos los humanos, pero sino que son por relaciones que el modelo sacó y descubrió, digamos.
lse posgrados: Okay, okay, está bien, pero eh necesito que se lo explique Shin porque hablamos de un vector. Es un vector, digamos, hablamos de un espacio. Es super complejo de explicar, lo sé, pero digamos voy a tratar de hacerlo muy sencillo.

01:14:09

lse posgrados: Eh, de alguna forma lo que hace el embeding es a al token lo transforma. Cuando decimos vector, en realidad es una concatenación de números.
Shimon Achtung: número
lse posgrados: Sí. es una lista de números, por decirlo.
Shimon Achtung: H
lse posgrados: Sí, es un vector es pero eso esa cantidad de números que representan ese token, que puede ser una parte de una palabra o la palabra está representado en un espacio. ¿Por qué? Porque si yo junto, digamos, no podría comparar, digamos, un token si tiene lo llevo a una concatenación de 300 de 300 números, si lo quiero comparar con otro token, tengo que tener la misma dimensión, si no no están en el mismo espacio. Uno le va a faltar una dimensión. cada dimensión es un elemento de esa lista de números, digamos, ¿no?
Marcelo Luna: Yeah.
lse posgrados: Es la forma y lo lo explicaron bastante bien, la forma matemática que tenemos, digamos, de llevar las palabras a a un a un modelo espacial que no es comprensible para humano, porque nosotros hasta 3D venimos bien, hasta 4D si le metemos tenemos un espacio en 3D, si le metemos un símbolo en en vez de digamos ese espacio en 3D, imagín un bloque en 3D, si si ponemos puntito y de repente le ponemos una dimensión más que pueda ser, no sé, el tamaño del punto.

01:15:35

lse posgrados: Pero cada vez que le vamos agregando más dimensiones más difícil de comprender, digamos, ¿no? Entonces el Llm funciona así. divide un una sucesión de palabras en tokens, cada uno de esos token en una fracción de una palabra o una palabra que está compuesta por una determinada cantidad de números dependiendo las dimensiones del embeding que estamos trabajando. Eso hace que sea fácil cuando uno hace,
Marcelo Luna: Oh.
lse posgrados: aplica la función de atención de los Transformers, digamos, eh reconocer las relaciones que hay entre palabras, eh, como como dijeron, rey, reino, que viene, qué viene primero yo, que viene después, digamos, dentro de cada palabra. y a la vez hace útil que la generación de la próxima palabra se genere, valga la redundancia, porque está basada en el comportamiento de ese espacio de palabra. Entonces, lo que hace básicamente un LLM es toma una determinada cantidad, una determinada cantidad de palabras, las lleva a un a tokens, los tokens se llevan a un espacio multidimensional. La función de atención de los Transformers detecta las relaciones que hay entre esas palabras. No es una relación, sino son muchas cabezas de atención que se llaman, pu llamar multi attention. las relaciones que existen complejas entre distintas palabras y la sucesión de esas palabras, cómo ocurren para que después la generación cuando yo escribo una palabra o una pregunta tenga una probabilidad de cuál es la palabra que sigue, digamos.

01:17:13

lse posgrados: Sí. Eh, eso es lo todo eso es lo que le explicaron como transformer is como está en el paper, digamos, ¿no? Pero en definitiva es tratar de que la máquina entienda la relación entre las palabras para que después cuando genere genere por por niveles de probabilidad. Eso si uno lo lleva a modelos que han entrenado con un montón de texto, hace que cuando uno escriba o le hace una pregunta a a un LM, la respuesta tenga sentido, digamos, ¿no? No sé si me expliqué porque capaz que lo dice más complejo y ya lo si no para clase que viene le traigo un ejemplo así bien más sencillito de lo que de toda esta parte, ¿no? igual ahí a continuación más o menos lo
Shimon Achtung: No, no vendría, no vendría mal, pero sí lo que entendí es que digamos toma de los tokens alguna forma de
lse posgrados: explico.
Shimon Achtung: digamos de números para poder agrupar de diferentes maneras para poder relacionar banco de plaza con banco de financiero o algo así.
lse posgrados: Exacto, exacto. Sí, pero voy a buscar algún algún vídeo de que est hay un montón, pero voy a buscar alguno que sea bien ABC para que lo para que lo puedan entender, digamos. En la operatividad, digamos, viene bien saber que lo que me va a generar el LLM está basado en algo que aprendió.

01:18:37

lse posgrados: Y si yo le estoy preguntando con algo, algo respecto que no haya aprendido, es probable que tire fruta, como habrán visto y habrán y habrán experimentado que alucinan, ¿no es cierto? que generan generan palabras por probabilidad independientemente de lo que yo le pregunte. Hm. Bueno, lo que le expliqué básicamente esto es un embeding, digamos, es tratar de llevar a una determinada a a una determinada cantidad de dimensiones una palabra en un y si nosotros tenemos dos dimensiones un gráfico X y si tenemos tres dimensiones X y Z. Si tenemos cuatro dimensiones, ya es un campo y ya después empieza a ser mucho más complejo, ¿no? Eh, pero en definitiva lo que busca es por similaridad. Algo importante que sí tienen que saber es lo que se llama ventana de contexto. ¿Entienden lo que es la ventana de contexto? ¿Por qué algunos modelos generan más que otros o algunos le podemos preguntar más que a otros? La ventana de contexto es básicamente una cantidad de tokens que se forman entre la pregunta y la respuesta y que los modelos están digamos toleran toleran eh el input. Actualmente casi que no tiene tanto límite como antes, pero antes cuando uno le preguntaba a GPT 3.5 y se le ponía un texto muy grande, apareció un un mensaje diciendo, "Che, esto no lo puedo procesar." Eh,

01:20:08

lse posgrados: actualmente eh Cloud 3 está cerca de 200,000 token. También creo que es eso uno de los parámetros que tiene Cloud, que seguramente se habrán dado cuenta que uno le hace una pregunta simple y no sé, uno le dice, "No, hacemos un gráfico con esta tabla y te genera un dashboard o no. ¿No has notado eso? Cloud consume mucho más tokens porque tiene esa capacidad y no está limitado a menos que uno se lo pida, ¿no? Sí, alguien levantó la mano.
Santiago Germino: Sí, acá eh me parece que el tema de los tokens eh juega mucho, no cuando uno hace una sola pregunta que que puede ser enorme y entonces ahí se complica, sino cuando uno hace una seguidilla de preguntas que tienen que ver con las preguntas anteriores, como todos los chatbots actualmente y eso en algún momento te agota el el tamaño del contexto y lo que están haciendo, por ejemplo, en cómo se llama, bueno, los chatb lo que hacen es de alguna manera sumarizar que dicen es como, bueno, agarro todo este cacho, este pedazo de contexto, lo de alguna manera lo comprimo, hago que que el significado quede, pero que ocupe menos y sigo, sigo y sigo. Eh,
J.Pablo Zebraitis: Muchas veces dice compactando la la comunicación,

01:21:21

Santiago Germino: bueno,
lse posgrados: Exacto.
J.Pablo Zebraitis: compactando
Santiago Germino: claro, eso sí, sí es eso, porque si no se queda sin sin contexto. Chao, termina ahí. Okay.
lse posgrados: Sí. Bueno, eh algo importante que lo tengan en cuenta para los RACS es que cuanto mayor es la ventana, más documentos le puedo inyectar para que para que haga la consulta, ¿no? Eso eso es importante y por eso eh le voy a ver por los grupos que intenten conectarse a alguna apquí de alguno de los modelos más grandes que puedan que puedan trabajar un poquito más con más específico, digamos. Bueno, eh ya lo que hemos hablado genera, digamos, la los riesgos de las limitaciones, la alucinación escribe la próxima palabra está por probabilidad, no por lo que vos le estás preguntando, digamos, realmente, sino por la probilidad del modelo con lo que fue entrenado. Hay fechas de corte, o sea, hay me acuerdo cuando salió uno de los primeros GPT modo chat, eh, estaba entrenado como modelo del año anterior, entonces uno cuando le preguntaba cosas actuales no tenía capacidad de de revisar páginas web ni responder actualmente. Hoy eso ya quedó en el pasado, todos te responden con con cuestiones actuales, leen páginas y te las resumen.

01:22:37

lse posgrados: Entonces, un poco que eso eso se ha ido se ha ido se ha ido mejorando, ¿no? Como les dije, esto no razona, predice. O sea, la respuesta está basada en probabilidades, no es que piensa, no no nos dejemos engañar, digamos. Bueno, entonces acá en antes de de que abramos la sala y empecemos a ver las cosas, eh todos entienden que es un sistema RAC, porque la mayoría de los proyectos están basados en sistemas RAC. ¿Alguien alguien le quedó alguna duda? Así más o menos lo vemos en en un ratito.
Shimon Achtung: Yo, o sea, por ahora no lo puedo explicar todavía, pero lo que vi en clase, bueno, más o menos entendí. M.
lse posgrados: Mira, lo voy a tomar me voy a tomar un ratito para para acá acá hay un yo sigo a esta persona que es un uno de LinkedIn que la verdad que que es un crack, tiene un montón de cuestiones disponibles. Eh, a ver si puedo aumentar esto.
Gabi Tallarico: en dos minutos más de clase nos manda hacer la primer materia, creo,
lse posgrados: No, no, por favor.
Gabi Tallarico: No.
lse posgrados: Bueno, todo todos entendemos que un sistema RAC, digamos, tiene distintos componentes, ¿no es cierto?

01:24:03

lse posgrados: Sí, eso lo entendemos. Hay una un documento que yo entrego, ¿sí? Y sí, lo que lo que lo que espero de ustedes es que sepan separar las fases del del del RAC. Entonces creo que la mayoría a esta primera fase de la ingesta, o sea, tengo distintos documentos, distintas fuentes en este caso, por ejemplo, esos documentos eh usualmente lo que pude ver, no hablo de todo, pero una determinada cantidad, lo han ingresado así sin ningún preprocesamiento, simplemente ingresan, los chanqueo y entran. Sí, hay acá hay mucho para hacer, digamos. Sí, esos documentos lo que se lo que se hace se los fragmenta, sí, por esta cuestión de las ventanas de contexto para que el modelo lo pueda lo lo pueda convertir a un espacio vectorial o que se llama embedings, modelo de embedings. Por eso ustedes cuando hicieron los racks, hay una parte donde ustedes decen, bueno, ¿cuál va a ser el modelo de embeding que voy a usar? ¿Lo bajaron de Hing Face o usaron alguno de de Olama de algún otro? que hicieron, usaron ese modelo. Eso fue paraar una base de dato vectorial, ¿sí?

01:25:17

lse posgrados: Que lo que hizo fue poner en ese espacio de características, ¿sí?, todos esos documentos, ¿sí? Todo ese contexto. Ahora, ¿cuál es la la más? Hasta acá no hemos hecho nada nada interesante. Lo interesante acá es que cuando un usuario hace una pregunta también tiene que pasar por el mismo modelo de embedings. Se genera un vector y por similaridad me va a traer los n cantidad de documentos relacionados a la pregunta. Eso es importante, digamos, ¿no? O sea, un rack no solo responde con documentos, sino te trae la n cantidad de documentos más similares a la a la pregunta que que el usuario hace. Eh, digamos, para generar la respuesta, el LLM lo que hace es basarse en esa n cantidad de documentos para generar la respuesta. ¿Sí? Entonces, es como el el pipeline seguiría este camino del documento a un modelo de embedings. El modelo embedings a una base de datos vectorial que se almacena en una base de datos. Sí. La pregunta se pasa al modelo embeddings. Una parte lo que hace es buscar por similaridad la n cantidad de documentos y un ll toma esa cantidad de documentos para hacer la respuesta y el usuario recibe una respuesta.

01:26:50

lse posgrados: A a eso lo entienden quieren que les resuelva alguna alguna consulta en particular.
Shimon Achtung: Creo que en el trabajo hice algo en una parte parecido a eso, así
lse posgrados: Bueno, el objetivo de esta materia es casualmente pone todo eso en orden,
Shimon Achtung: Sí.
lse posgrados: digamos. Entonces, si tu trabajo tenía todo eso en un solo bloque de código, lo que vamos a hacer es se para, bueno, preprocesamiento del texto. Bueno, ¿cómo viene el texto? ¿Al texto lo voy a almacenar en pedacitos de texto o lo voy a eh poner en una tabla donde cada fila sea un chank? Eh, o bueno, a eso es lo ahí quiero ir, digamos, ¿no? Como en todo modelo, garbage in, garbage out. Si yo acá le meto mucha más energía, pruszamiento, texto y trabajo, esto que voy a almacenar va a tener mucho más sentido. En consecuencia de lo que yo pregunte va a tener mejor respuestas. En consecuencia de la respuesta generada va a tener una una mejor calidad, digamos. No hay formas de medir la calidad de un rag. ¿Vieron algo de eso en clase? métricas,

01:28:04

Shimon Achtung: Mira, yo lo que lo que pude experimentar a través del trabajo que hice con Fernando,
lse posgrados: básicamente.
Shimon Achtung: que me ayudó, que me corrigió los embedings que yo había puesto de hing face en donde corregía mejor la manera, digamos, de encontrar los embedings y bueno, seguramente eso le da más sentido a la respuesta, digamos, mejor sentido. Esa fue mi experiencia, digamos.
lse posgrados: Está bien. Bueno,
Shimon Achtung: Recortó
lse posgrados: a a este chat se le digamos a a este pipeline se le pueden agregar cosas,
Shimon Achtung: mejor.
lse posgrados: digamos, ¿no? Este es como el más sencillo. Acá uno para antes de generar embeding podemos usar un LLM para generar
Shimon Achtung: Hm.
lse posgrados: metadatos. Por ejemplo, metadatos son, se acuerda que dimos que reconocimiento de entidades dentro del texto, que es una de las, digamos, de las cosas que se puede hacer con procesamiento de lenguaje natural. Entonces, bueno, si yo a esa parte la, por ejemplo, si yo estoy hablando eh de un texto, no sé, agronómico y de repente si yo al al fragmento del chan le saco
Shimon Achtung: Hm.
lse posgrados: metadata que esté relacionada a esa, esa metadata también la puedo llevar y va a mejorar la calidad.

01:29:21

lse posgrados: Sí. Entonces, yo de repente, no sé, fecha de siembre, etcétera, las puedo poner en una tabla, bueno, en una tabla no, pero en un Jason, un documento estructurado que después le pueda consultar, que forme parte de la respuesta. Va a aumentar la calidad. La calidad del rack se va a medir, se mide distintas formas, pero una es, por ejemplo, la cantidad de documentos que realmente aportan a la respuesta. Si si yo, por ejemplo, traigo 10 documentos, si el retribal me saca a mí 10 documentos relevantes y de esos 10 documentos relevantes, ocho no tienen nada que ver con la respuesta y bueno, hay algo ahí que me está trayendo mal, digamos, ¿no? Capaz que hay cosas para mejorar. Eh, bueno, ahí ya.
Shimon Achtung: Oh.
lse posgrados: Y perdón que me fui, yo aprovecho para como para saldar dudas y y tener y tener feedback de ustedes, digamos, ¿no? Bueno, ah, vieron cómo cómo crear los promps para que se genere la respuesta. También hay promps del, digamos, del del chan. Gabi, creo que vos aplicaste una clasificación antes para que esa clasificación forme parte de la respuesta también, lo cual una estrategia también.

01:30:40

lse posgrados: Entonces, vamos a tener distintas formas de mejorar los RACS con con ingeniería prompt.
Gabi Tallarico: Y el y el pron que puse es un desastre porque era recortito, no le puse nada. Después me dije, debería haber construido un prom verdadero.
lse posgrados: Lo vamos lo vamos a ir mejorando.
Gabi Tallarico: porque no supiera hacer PR, porque pensé que no iba en ese punto a hacer algo tan extenso.
lse posgrados: Yo creo que hoy en día la la por ahí lo que es prompto. Por ahí sí, el primera aproximación a un prom lo hacé, pero después se lo tirm y que te haga un prom picante, digamos. No, tratar de que no alucine el prompt, pero está bueno tener ese feedback de decir, bueno, le pido a Geminch,
Shimon Achtung: Ah.
lse posgrados: mira, tengo esta situación, contexto, etcétera, etcétera, diseñame un prom y ahí lo lo iterás y lo probas. Sí. O sea, no, eso seguramente lo han hecho, digamos, uno no se larga con un promp así no más, digamos, también le consulta a los LLM con algún determinado rol para que generale un buen un buen prompting, digamos. Bueno, las aplicaciones hay un montón, digamos, eh salud legal y finanzas para el agro, hay bastante aplicaciones.

01:31:51

lse posgrados: Eh, ¿qué es lo que qué es lo que un RAC lo acabamos lo acabamos de ver, digamos? Básicamente genera documentos, extrae los document las partes del documento que estén relacionado para que un LM los tome y genera una respuesta fundamentada. Es como notebook LM. antes que esté notebook LM se hacía esto, digamos, hoy más fácil tirarle al notebook LM algunas cosas y lo hace, pero lo que está abajo hace exactamente eso, digamos. Bueno, ah, lo que lo que vi es que digamos el aquellos que están con el trabajo en en modo rack, que son creo que la mayoría, salvo algunos casos, eh este sería como la arquitectura básica, lo que expliqué recién, los documentos, el chanking, los embeding, cuál va a ser la estrategia para guardar esos vectores, la pregunta, la generación de la del embeding digamos, de esa pregunta, la recuperación de los cada documento y la respuesta, ¿no? Eso quedó quedó claro. Para base de datos a puedo usar croma db eh modelos hay varios para para los eding también hay varios modelos y frameworks lo podemos programar nosotros o también ya hay como frameworks que alguno me parece que usó el Langchin también está bastante bueno el uso de frameworks. Lo vamos lo vamos a ver seguramente grupo por grupo.

01:33:19

lse posgrados: Hay algunos que si tienen casos de clasificación de texto. Me parece también excelente buscar, como dije en un principio, una solución a mi problema que sea la más simple posible, ¿no? Toda. Obviamente una solución con aplicando un LLM para que clasifique texto es buena, puede ser atribuible, pero quizás si un cero shot funciona, que son modelos que ya están medio preentrenados para eso en Hing Face o en otros lugares, puede andar. Quizá para aquellos que tengan ese track de clasificación de texto, el baseline usar lo más sencillo que es tres cuatro líneas de código con cero shot y ver qué da, digamos, y después con usando un LLM cómo se mejora y ese es su trabajo y me parece bárbaro, digamos, ¿no? que quede documentado, argumentado y solución solución terminada, digamos. Eh, entregables para esta clase. Básicamente va a ser el canvas que voy a ver ahora en en dos slides más. Sí. Eh, me parece que se fue el último. Est, perdón, me adelanté acá. ¿Qué es lo que qué tipo de trabajo el que vamos a hacer nosotros ahora? es algunos van a estar en prueba de concepto y otros van a estar en MVP, digamos, ¿no?

01:34:45

lse posgrados: Algunos chicos ya tienen, como mencionaron al principio, algunos están ya bastante adelantados, no está mal. Eh, lo que espero es que compartan esos desarrollos con con los compañeros y también que que haya feedback para que se aprendamos entre todos. Y algunos están en prueba de concepto, que tampoco está mal, me parece perfecto, digamos. Yo voy a tratar de llevarlos a cada uno la mínima expresión posible de su problema y que esa que ese pipeline quede lo lo más argumentado y detallado posible. Eh, digamos, va es muy fácil hoy en día a usar Cloud y tirar un problema Cloud y que Cloud lo haga endto end. Vamos a tratar de de no ir por ese camino, sino más bien ir pasito a pasito. No está mal el uso de de modelos para generar texto, etcétera, y para ayudarnos a entender un poco más los problemas. Pero vamos a tratar de de no ir a un MVP que lo haga cloud solo, etcétera, sino más bien de ir a una prueba bien de concepto para aquellos que están iniciales y los que ya están en esta en esta fase de de MVP o casi producción también bienvenido, digamos, ¿no? Bueno, ¿qué es lo que es un canvas? Canvas básicamente lo que hace es mapear distintas cuestiones de un problema de negocios, eh, entradas, salidas, actores, stakeholders, como se dice ahora.

01:36:06

lse posgrados: eh cuestiones de costo, etcétera, para tratar de de digamos en esta fase de diseño, hoy en fase de diseño, eh alinearnos entre todos o alinear todos los proyectos, mejor dicho, a lo mínimo posible y que quede bien definido qué es lo que vamos a hacer y qué no vamos a hacer. Parte de esto entiendo que lo entregaron de alguna quizás de alguna otra forma para NLP1, una prueba de concepto donde habían algunas cosas de qué es lo que se hacía, qué no se hacía, etcétera. Pero esta es una forma eh bastante visual de llevar el problema a algo escrito, digamos, ¿no? y también de aquellos quizás plantearon una idea que era muy muy abarcativa o muy ambiciosa, llevarla a un problema más sencillo. Básicamente lo que hace el CAM es preguntarnos qué problema resuelvo. Sí, eh tiene que ser muy sencillo en una oración, no tenemos que mencionar eh la tecnología, sino más bien qué problema. El problema nos tenemos que poner el punto de vista del usuario que va a ser el uso de esta herramienta o de las herramientas que están por diseñar y responder eh digamos en función a eso. ¿Quién para quién? Es importante que sepan, digamos, quién va a ser el equipo que lo va a usar, quién va a ser el usuario final, eh, y y qué es lo que necesita, digamos, nos ayuda a poner del lado del del posible cliente o de nosotros mismos para ver qué es realmente lo que necesito.

01:37:34

lse posgrados: ¿Con qué documentos trabajo, vamos a necesitar Corpus? O sea, básicamente textos o lo que ustedes estén diseñando, de dónde viene el dataset, si un dataset libre, si lo pueden utilizar o no, si no hay restricciones éticas, tecnológicas o de confidencialidad que le permitan usar esos datos. Eh, ¿qué es lo que voy a construir? si un rack, si un rack avanzado agéntico o si simplemente una clasificación de de texto. ¿Y cómo voy a evaluar si funcionan aquí? Si no conocen las métricas, yo se las dejé anotadas, digamos, para que también en la clase que veamos, creo que la clase 4 C, yo les voy a explicar bien qué es lo que mide cada métrica de de un rack. Por el momento, digamos, eh yo diría que se va a usar RAC. Si esto no lo pueden completar hoy, que se tomen un tiempito en la semana, yo igual les puedo mandar material para que para que vean qué es lo que cada métrica de de los sistemas RAC y aquellos que estén usando otras herramientas que planteen exactamente cuál va a ser la métrica, digamos, para ver si esto funciona o no, si mejora o no. Ojo, si no mejora también es un resultado.

01:38:48

lse posgrados: Eh, este es el template, ¿sí? Que tienen que completar el Ahí les paso en en el el enlace para que puedan descargarlo. Sí. Eh, básicamente, ¿de dónde vienen los datos? ¿Cuál es el corpus que voy a tener que usar? ¿Qué modelo? Acá pueden completar, el que usaron para NLP1 o aquel modelo que planearon utilizar. Eh, ¿qué modelo de embeding estoy pensando utilizar y de base de datos, sí? Vectorial, la propuesta de valor, ¿sí? O sea, ¿qué es lo que definitivamente por qué quiero usar esto y no otra cosa, digamos? Y y qué valor aporta eh la integración, cómo voy a hacer que esto esté disponible. Ojo acá, capaz si es un collab. Es un collab si que tienen pensado hacer una interfaz. Bueno, si aquellos que tengan pensado hacer un frontend, una API para servir el modelo, nada, acá vamos a ir caso por caso. Un colab está mal, digamos, puede funcionar un chat puede funcionar también. ¿Quiénes quéos son los state holders o cuáles son las personas que están interesadas o que puedan que estén relacionados a esto?

01:40:00

lse posgrados: Acá hay que mapear todos aquellos que estén relacionados a los dueños de la información, quiénes lo van a usar. Entonces, esto sí es importante. ¿Y cuál va a ser el usuario final, digamos, no? Acá en costo algunos hablaron, si es que tienen algún modelo de costo ya previsto. Eh, el precio por token está en las páginas de los modelos, podrían llegar a estimarlo, digamos, en función de la cantidad de tokens que ya han generado en los proyectos de de NLP1. Si en el caso que no tengan esta información, argumenten por qué no las tiene y yo los ayudo a buscarla o a estimarla. las métricas de digamos de mejora y cómo cómo mejora esto en la productividad o qué valor económico lo puedo estimar. Acá se suele usar también el precio promedio de horas hombre. Pueden, si son profesionales, pueden ver en el consejo de de profesionales cuánto vale su hora profesional. No sé, por ejemplo, acá en Saltan un ingeniero, la hora profesional está cercana a los $30, por así decirlo, más eh algún otro ingreso de posible venta. En esta parte del en estas dos partes de costo de ingreso, no le ponga mucho esfuerzo hoy porque seguramente puede que que vaya cambiando a medida que vayamos desarrollando.

01:41:17

lse posgrados: Si en lo que es el pipeline, digamos, ¿no? O sea, en en esta parte de qué corpus, qué datos, etcétera, digamos, ¿no? Eh, les puse algunos ejemplitos, ¿sí?, que están ya resueltos. Eh, y con ustedes vamos a ver, digamos, en en un uno por uno. Eh, ahora les voy a mostrar quiénes son los grupos que estaban, al menos los que me respondieron. Me gustaría que aquellos que no tengan eh proyecto vemos, yo le tengo una una propuesta para ellos para armar un un rack con el boletín oficial. Eh, y la dinámica de hoy, bueno, ya creo que me extendí un poquitito, pero nada, no pasa nada, nos queda todavía una hora y 20 para para para armar. Es eh terminar el template y una ronda de presentaciones. ¿Sí? Entonces, lo que queda de la de la clase, vamos a descansar ahora 10 minutos. Tomo agua, tómense un café y después vamos a hacer la ronda o digamos vamos a llenar el el voy a conocerlos en detalle las cosas que tienen. Preparen las notebook, lo que ya hayan presentado. Aquellos que no tengan proyecto, eh, avisen para que yo les suministre un un un nada, le voy a dar el enlace, un PDF y que puedan trabajar con con el Boletín Oficial de la Nación.

01:42:36

lse posgrados: Me parece una buena una buena posible herramienta. Eh, y en la presentación nada, no hace falta que elaboren la presentación, simplemente muestran el el template lleno, ¿sí? Eh, y lo explican rápidamente en dos tr minutos cada uno. Sí. Eh, así que bueno, nada, eso. E dudas.
Marcelo Luna: Una sí, una una pregunta. rápida, digo, para entender y situarme, pero la idea es que completemos el canvas hoy.
lse posgrados: Sí, sí. A ver, con lo que puedan, no, no el entregable no es para hoy, digamos, la presentación es para hoy para que tengamos feedback y yo los pueda conocer a casi todos o a todos y todos tengamos conocimiento de lo que están haciendo los grupos, pero hasta antes de la clase que viene debería estar más desarrollado. Esto es más para ustedes que para mí, digamos, ¿no? O sea, aquellas cuestiones del canvas que no puedan completarla hoy, me la entregan durante la semana, hasta antes de las clases que vienen, pero hasta antes de la clase que viene debería estar
Marcelo Luna: No, no, digo, yo había asumido eso como punto de partida porque,
lse posgrados: terminado.
Marcelo Luna: no sé, de vuelta hablo por mi caso, hay algunas cosas que yo todavía necesito investigar para poder determinar.

01:43:55

Marcelo Luna: Entonces, por ahí no voy a tener una respuesta para hoy,
lse posgrados: Sí, pero ahora hay hay tu caso es el de las el del
Marcelo Luna: pero
lse posgrados: reglamento de Sí,
Marcelo Luna: me regatas.
lse posgrados: sí, sí, sí. Bueno, sí, ahí yo te puedo tirar alguna idea, digamos, ¿no? Mi trabajo es ese, digamos. Ahora es armar grupos o bien ahora les voy a presentar qué diagnóstico tuve de las de las respuestas, eh, para que veamos cómo estamos, digamos. Sí. Bueno, a casi todos tienen proyectos, salvo tres personas que respondieron. Sí. Eh, Luis, Juan y Marcelo no tienen un proyecto, están explorando opciones. proyecto individual están casi todo y proyectos abiertos a colaborar son bueno los que están ahí, digamos. Si alguno de los que están sin proyecto se quiere unir a a los proyectos que están abiertos a colaborar de Gabriela, Fabricio, Carlos Lorna y Shimon,
Gabi Tallarico: son bienvenidos.
lse posgrados: son bienvenidos para que haya interacción y se puedan repartir el trabajo y etcétera, digamos. Eh eh me gustaría que me respondan ahora,
Marcelo Luna: Sí,
lse posgrados: así ya lo vamos lo vamos viendo,
Marcelo Luna: sí, perdón.

01:45:17

Marcelo Luna: Eh,
lse posgrados: digamos.
Marcelo Luna: yo ahí vuelvo. Digo, yo justamente soy uno de los que aparece ahí como sin proyecto. En realidad por ahí se digo, no fui claro cuando contesté la encuesta, pero digo, la idea es continuar con ese proyecto en particular. ¿Me entendés? Ahí como sin proyecto. Sí.
lse posgrados: Bueno, te pongo eh no sé si hay alguien que esté,
Marcelo Luna: Ah,
lse posgrados: digamos,
Marcelo Luna: sí.
lse posgrados: ahora sin sin proyecto que hable ahora o a ver.
Lorna Pons: Hola, buenas noches.
lse posgrados: Sí. ¿Quién habla? Lorna.
Lorna Pons: Lorna, Lorna, sí, ¿cómo andas? Yo no completé la encuesta,
lse posgrados: Sí.
Lorna Pons: pero tengo ya el proyecto pensado, ¿sí? Como ampliar lo que hice para PNL.
lse posgrados: Okay. Alguien que no tenga nada, absolutamente ninguna idea de cómo empezar con el trabajo final.
juan ignacio sinopoli: Buenas noches. ¿Cómo va? Yo al igual que el orna también, o sea, terminé definiendo seguir por la misma línea del proyecto para PN.
lse posgrados: Buenísimo. Bueno, entonces estamos todos con proyectos individuales, ¿no?

01:46:24

lse posgrados: Y tienen afinidad entre ustedes para armar grupos. Si no, vamos por individuales, no hay ningún problema. Es complejo armar grupo cuando ya al final de la de la Claro.
Shimon Achtung: Creo que ni nos conocemos.
lse posgrados: Exacto. Sí, sí. Bueno, esta clase, digamos, yo vengo a romper a romper eso, digamos. Yo quiero que interactúen si ya el código lo vieron con los con los chicos. Bueno, la modalidad va a ser la siguiente. Descansamos 10 minutos ahora hasta la 55. Volvemos y cuando volvemos para no armar x cantidad de grupos, digamos, porque son muchos, son 17 grupos. Ah, yo los les pasé en el chat el Yo creo que deben poder ingresar ahí. Sí. Y ahí está en la clase uno. Ah, eso ustedes van a ingresar a al Drive en la clase uno definición. Ahí al final está el canvas. No hace falta que sigan ese template, tomen los títulos y escríbanlo en un Word si le hace falta. O sea, no hace falta que lo completen así como está ahí, sino más bien tomen los títulos, los ponen en un texto, eh, y lo van completando, ¿sí?, con sus temas.

01:47:43

lse posgrados: Yo voy a ir pasando ahora usando, eh, digamos la información que tengo uno por uno, eh, después del descanso y ahí empezamos a interactuar. Para no distraerlos, les sugiero que nada, que que pongan en silencio la compu, así vamos uno por uno y no y no se distraen. La otra opción es armar 17 grupos, con lo cual me parece reineficiente, digamos. Me me parece mejor que voy uno por uno, que quiera escuchar las conversaciones que tenga con un grupo, o sea, con una persona, lo deja aprendido y el que no, simplemente lo pone en en silencio en la compu y trabaja a la vez. Si tiene alguna duda levanta la mano y ahí abrimos el micrófono. Sí, Santi iba a decir algo.
Santiago Germino: Ay, no, perdón, tenía la mano levantada.
lse posgrados: Ah, bueno. Volvemos en 10 entonces.
Shimon Achtung: Okay.
Gabi Tallarico: No, a las 9 en punto 15.
lse posgrados: O sea, en 10 minutos a las 9 men 10 a las 9 a las 8:55.
Gabi Tallarico: No, a las 21. A las 21.
lse posgrados: Estiramos 15 minutos.

01:48:55

lse posgrados: Bueno, listo.
Gabi Tallarico: Sí.
lse posgrados: Tiramos 15 minutos.
Gabi Tallarico: Yeah.
lse posgrados: Vayan, vayan viéndolo, ¿no? Por favor. Bueno, vamos volviendo que ya tomar un cafecito. Bueno, lo voy a hacer así para que no quede tan desordenado la interacción. Voy a armar cuatro salas al azar y de ahí voy a tomar uno, dos y voy a ir recorriendo los grupos. Sí, uno por el grupo primero, después va a volver récord récord en segundo y así digamos no no queda tan tan desordenado. Sí. Así que ahora los asigno a salas y sesiones separadas. Editar cuatro salas.
J.Pablo Zebraitis: Disculpe, profe, este, yo estoy de viaje de trabajo y tengo un equipo esperando, o sea, que o o lo dejo para la próxima o soy el primero, como como tú teorezcas, no hay problema. Este,
lse posgrados: algo para compartir ahora antes de que abra sala lo comenzamos
J.Pablo Zebraitis: si si querés, sí, digo, medio rápido, si no perdón,
lse posgrados: yup
J.Pablo Zebraitis: disculpe que no es lo común, pero me tengo que retirar. Este, le comparto si quieres.

02:03:20

lse posgrados: compartir pantalla y lo v los chicos que quieran seguir trabajando en el canvas sigan
J.Pablo Zebraitis: Sí, porque no no quiero,
lse posgrados: Eh,
J.Pablo Zebraitis: no quiero perjudicar a a al equipo que me
lse posgrados: todo lo que lo hacemos. Si,
J.Pablo Zebraitis: asignes.
lse posgrados: Pablo, no hay ningún problema. compartí, me interesa saber conocer tu proyecto, que me expliques tus datos y sí,
J.Pablo Zebraitis: Bueno, eh, ¿estás viendo bien?
lse posgrados: ahí se ve.
J.Pablo Zebraitis: Eh, básicamente mi proyecto es este eh nosotros trabajamos con una empresa que brinda servicios este de este de juego, digamos, post y sistemas backend y todo lo demás con alcance regulatorio en Uruguay. Y este y básicamente el objetivo del proyecto era optimizar eh el ciclo de vida de los de la entrada de incidentes. Este hoy no está automatizado esto y en su momento quiso utilizarse una herramienta de seguimiento de incidentes como Redmine con ISUS. Este, en la práctica los usuarios no utilizan mucho esto, eh, por lo que mandan mensajes en WhatsApp, ¿sí? mensaje de texto y mensajes de imágenes. Este, y bueno, básicamente lo que lo que intento hacer es eh llevar esto que se registren todos los incidentes este automáticamente.

02:04:42

J.Pablo Zebraitis: Este está fuera de alcance la captación eh inicial porque estoy cuestionándome si usar WhatsApp pago o usar otras tecnologías. Este, eso está escrito por acá en los documentos e eh en la parte de alcance. Sí. Este, y bueno, básicamente lo que intento es que eh ya se definieron algunas imágenes como este entradas. Eh, vamos a ir a por acá un segundo,
lse posgrados: Sí,
J.Pablo Zebraitis: por favor.
lse posgrados: me gustaría saber A ver, ¿cuál es el dataset? Si es texto o es una
J.Pablo Zebraitis: Acá acá tengo justamente esto. Eh,
lse posgrados: imagen.
J.Pablo Zebraitis: yo le solicité a la gente de soporte actual que pusiera 18 casos, ¿sí? Eh, concretos. Básicamente son imágenes de WhatsApp como estas. Sí.
lse posgrados: Yo estoy una consola ahora lo que parece ser una
J.Pablo Zebraitis: En el Perdón,
lse posgrados: consola.
J.Pablo Zebraitis: perdón, perdón, perdón, perdón, perdón. Un segundo, por favor. Un segundo. No sé por qué no puedo compartir toda la pantalla.

02:06:08

J.Pablo Zebraitis: Eh, vamos acá. Así vamos a ir una cosa por vez. ¿Qué están viendo ahora? ¿Están viendo el caso uno? No, no están viendo nada. Un segundo, por favor. Bien, disculpen, ahí está bien. Sí,
lse posgrados: Ahí sí se ve. Sí. O sea, tu dater qué ingresa,
J.Pablo Zebraitis: perdón.
lse posgrados: porque eso es importante que sepamos.
J.Pablo Zebraitis: Eso es lo que ingresa. Lo que ingresa básicamente son cosas como estas. hoy
lse posgrados: Ahora te consulto.
J.Pablo Zebraitis: este
lse posgrados: Yo te consulto. Cada una de esas cuestiones. Eso es un ticket.
J.Pablo Zebraitis: es un bueno,
lse posgrados: Aparentemente
J.Pablo Zebraitis: puede ser un ticket de quñera, puede ser este una pantalla de un sistema, no tengo muy claro,
lse posgrados: no hay un patrón, digamos.
J.Pablo Zebraitis: no hay un patrón definido. Esto también es un ticket,
lse posgrados: Eh,
J.Pablo Zebraitis: por ejemplo, o sea, es es una un usuario sacándole una foto a una imagen de un ticket o un usuario sacándole una foto en una pantalla de de de una computadora.

02:07:08

lse posgrados: déjame que te que entonces tu sistema va a ingresar, van a ingresar x cantidad de imágenes. Esto es importante que que determinés cuántas
J.Pablo Zebraitis: imágenes acompañadas de textos.
lse posgrados: imágenes.
J.Pablo Zebraitis: En general, cada caso tiene una, dos, no mucho más que eso,
lse posgrados: Entonces,
J.Pablo Zebraitis: imágenes.
lse posgrados: tu dataset vos va a tener cada caso va a estar acompañado de un texto y una imagen.
J.Pablo Zebraitis: Exacto.
lse posgrados: A esa
J.Pablo Zebraitis: texto, perdón, texto,
lse posgrados: imagen,
J.Pablo Zebraitis: porque la ingesta en su momento va a ser a través de alguna método de ingresos que está fuera del scope de este de este
lse posgrados: eso está claro. Eso está claro,
J.Pablo Zebraitis: proyecto.
lse posgrados: Pablo. Lo que yo necesito saber es que definamos exactamente qué es lo que ingresa.
J.Pablo Zebraitis: Puede ser imagen o puede no tener imagen.
lse posgrados: ingresa.
J.Pablo Zebraitis: Puede ser, simplemente tengo problemas con tal
lse posgrados: Okay.
J.Pablo Zebraitis: cosa.
lse posgrados: Pero cada caso vos lo tenés en una carpeta. Si tiene una imagen, ingresa la imagen. Si tiene un texto, ingresa el texto.

02:08:01

lse posgrados: Entonces, vos lo que vas a hacer, vas a hacer, digamos, estoy tratando de llevar esto algo que se pueda resolver, digamos, la primer, al menos la primer parte de ingesta.
J.Pablo Zebraitis: Exacto.
lse posgrados: Tu primer parte de ingesta va a ser iterar por una el directorio carpeta por carpeta. Si la carpeta tiene una imagen, se procesa la imagen, se extrae el texto con OCR o alguna herramienta vinculada a la detección de texto. Sí, se genera un dataset o un texto, un txt o un Jason y a la vez se le agrega,
J.Pablo Zebraitis: ¿cierto?
lse posgrados: si es que contiene un texto ese caso, ese texto, ¿cierto?
J.Pablo Zebraitis: Para lo que es el contexto de la materia siempre van a ser imágenes porque los casos que tengo de prueba por ahora son solo son solo imágenes, ¿ya? O sea,
lse posgrados: Okay,
J.Pablo Zebraitis: imágenes que contienen a su vez imágenes adentro o no.
lse posgrados: okay,
J.Pablo Zebraitis: No,
lse posgrados: está claro.
J.Pablo Zebraitis: esto que estamos viendo ahora.
lse posgrados: Buenísimo.
J.Pablo Zebraitis: Sí.
lse posgrados: Eso es lo ingresa.
J.Pablo Zebraitis: Entonces,
lse posgrados: ¿Y vos qué pregunta querés

02:08:57

J.Pablo Zebraitis: bueno, la cuestión no es una pregunta.
lse posgrados: responder?
J.Pablo Zebraitis: El sistema lo que hace es agarrar esta imagen, este, identificar eh qué es lo que está sucediendo del origen que está llegando, porque viste quebqnr, o sea, esto puede venir de diferentes orígenes, o sea, cuáles de mis clientes está reportando el problema que está teniendo. Trata de identificar cuál es el problema identificando cosas dentro de la imagen, ¿sí? la boleta, el sorteo y cosas por el estilo. Procesa esa información, genera una entrada a un mecanismo clasificador, ¿sí?
lse posgrados: Aha.
J.Pablo Zebraitis: Que agarra y en base a reglas que se le definen y contexto de sistemas y y cosas, este, trata de clasificar y taguear cierta información, generar un issue en Redmine que registre la entrada de ese de ese de ese caso. Sí. Eh,
lse posgrados: Claro.
J.Pablo Zebraitis: Redman debería ser como un GitHub o no sé si conoces, o sea, o sea, es un mecanismo de ticketing, sí, es genera la entrada y eso automáticamente también genere un link al chat de Google Chat que utiliza GT de soporte. Sí,
lse posgrados: Okay.
J.Pablo Zebraitis: con tal de que todavía no termina,

02:10:03

lse posgrados: ¿Dónde empieza y dónde termina tu sistema? tu sistema
J.Pablo Zebraitis: todavía no termina.
lse posgrados: de
J.Pablo Zebraitis: El sistema termina cuando, o sea, el usuario realiza la acción, marca como que toma todo.
lse posgrados: no el sistema, tu sistema, el que vos estás proponiendo,
J.Pablo Zebraitis: Es
lse posgrados: porque yo yo te recomendaría para que no abarque todo, digamos, absolutamente todo lo que mencionas,
J.Pablo Zebraitis: todo.
lse posgrados: cortarlo, cortarlo hasta hasta que lea lo que está en la imagen, lo procese y hacer un sistema rag. en donde vos le puedas consultar y te traiga aquellos documentos relevantes y todo lo que es, digamos, el pipeline posterior escalarlo luego, digamos, ¿sí? cosa de que de de acotarlo lo máximo posible y luego si tenés más tiempo lo podés seguir escalando. el hecho de tener una imagen, procesarla, sacarle el texto, armar un documento que contenga el contexto de ese texto y una herramienta que a la que vos le preguntés y te de alguna forma te simplifique cuáles son, digamos, lo, no sé, por ejemplo, los casos con determinada característica por día, por semana, por mes, yo creo que Hasta ahí es, digamos, hasta ahí ya estamos más que bien, digamos.

02:11:16

J.Pablo Zebraitis: Perfecto.
lse posgrados: No sé si te parece.
J.Pablo Zebraitis: Bien, ya lo tengo evolucionado eso con con el resto, pero está bien. O sea, empiezo con esto. Vemos. Después te muestro alguna cosa.
lse posgrados: Claro,
J.Pablo Zebraitis: ya tengo hecha este porque ya tengo cosas más avanzadas, o sea, en todo esto.
lse posgrados: me parece bien, pero con que documentemos esto no solo te sirve a vos, sino también creo que al al equipo, digamos, todos los que estamos trabajando en esto, ya que vos podas desarrollar una herramienta que tome una imagen se que el texto genere genere un texto de resumen y estadísticas respecto a los casos, es sumamente ente útil, no solo para, obviamente vos lo tenés desarrollado, pero ya justificarlo, etcétera, escribirlo en un documento, armar el canasta ahí
J.Pablo Zebraitis: Perfecto. Capaz que te cambio capaz que te cambio el final,
lse posgrados: especificar.
J.Pablo Zebraitis: que tal vez sería un output de Jason con
lse posgrados: Perfecto.
J.Pablo Zebraitis: clasificación
lse posgrados: Ese tu problema sería un problema de clasificación donde ingresa un texto y vuelvo a decir en un caso de xxvels,

02:12:12

J.Pablo Zebraitis: ahí que te tague las cosas y después lo ingeste en otro lado,
lse posgrados: digamos.
J.Pablo Zebraitis: pero eso después fuera de
lse posgrados: Ahora te consulto. ¿Vos tenés algún modelo de clasificación?
J.Pablo Zebraitis: scopo.
lse posgrados: Porque creo que el que vos mostraste era vos lo ponías en un embeding y usabas learn y algún modelo de clasificación típico. ¿Cuál es tu
J.Pablo Zebraitis: Yo básicamente, yo básicamente probé dos cosas.
lse posgrados: benchmark?
J.Pablo Zebraitis: probé conama clasificar esto y ver a ver contra contra los datos reales que yo infiero y y el tiempo de mi máquina y que no tiene GPU y todo lo demás y fue bastante malo. Lo que yo hice fue agarrar de eso. Agarré con Gemini,
lse posgrados: Oh.
J.Pablo Zebraitis: sí, tengo una cuenta, una piquí de la empresa y este y le tiré esto a esos 18 casos y este y me dio eh valores bastante aceptables. Este y bueno, este creo que por la cantidad de casos por día y y lo que mencionaba antes, ¿no? este me iría hacia hacia hacia que el caso, hacia que el uso real sería con una piqui de seminite que resuelve esto en 30 segundos y y funciona perfectamente

02:13:13

lse posgrados: Claro,
J.Pablo Zebraitis: para para luego seguir el pipeline a soporte,
lse posgrados: claro. Cortemos el pipeline hasta donde hasta donde mencionaste y a eso lo lo redondear,
J.Pablo Zebraitis: ¿no?
lse posgrados: lo arm, un documentito, etcétera. Hasta ahí estamos. Digo, si sumas complejidad y por ahí no entramos más un problema de arquitectura y de conexión, etcétera, más que un problema de lenguaje,
J.Pablo Zebraitis: Aha.
lse posgrados: digamos, ¿no? El el problema del lenguaje natural y lo que vos querés resolver ahora es hasta ahí, digamos. Yo creo que hasta ahí estamos más que bien y puede ser útil también para otros chicos que tengan casos similares respecto de si tienen que procesar imágenes o algo por el estilo,
J.Pablo Zebraitis: Bien,
lse posgrados: ¿te parece?
J.Pablo Zebraitis: muchas gracias. Gracias por
lse posgrados: Y bueno, sí, no,
J.Pablo Zebraitis: tolerancia.
lse posgrados: mira, lo importante es que trate de completar el canvas hasta lo que hemos hablado recién, digamos,
J.Pablo Zebraitis: Sí,
lse posgrados: ¿no?
J.Pablo Zebraitis: este, voy a intentar ahí está.
lse posgrados: Y y de una Sí,

02:14:04

J.Pablo Zebraitis: Si es posible después te mando el C más. Sí,
lse posgrados: sí, buenísimo.
J.Pablo Zebraitis: dale.
lse posgrados: Me queda, me queda claro lo que tenés que hacer y cómo lo tenés que hacer y ya quedó definido,
J.Pablo Zebraitis: Gracias.
lse posgrados: digamos. Perfecto.
J.Pablo Zebraitis: Gracias. Yeah.
lse posgrados: Bueno, eh, vamos con a ver lo agarro acá por orden no más. Carlos Salini lo agarro así de una. Sí, creo que le es útil ver lo que los chicos están compartiendo. Sí, no, me parece que por ahí respondo más de una pregunta. ¿Alguien está compartiendo
Gabi Tallarico: Sí, me ver lo que están compartiendo.
lse posgrados: Pablo? Me parece que se alguien sigue compartiendo. Eh, yo estoy viendo una pantalla ahora. Ahí está. Listo. Ahora sí.
Marcelo Luna: Yeah.
lse posgrados: Ahora vamos con Carlos. Carlos, eh, comentanos cómo. Carlos Salí, ¿estás ahí? Listo. Siguiente.

02:15:02

lse posgrados: Fabricio, ¿estás disponible?
Fabrizio De Luca: Sí, ¿cómo andás?
lse posgrados: Te anima a compartir tus datos y cómo qué es lo que tenés pensado
Fabrizio De Luca: No, para compartirnos.
lse posgrados: y del
Fabrizio De Luca: ¿De qué hablas? De la pantalla. De la
lse posgrados: proyecto. ¿Tenés tenés asignado?
Fabrizio De Luca: Sí,
lse posgrados: ¿Tenés un PDF que podamos que puedas mostrar algún documento, tus datas?
Fabrizio De Luca: no, todavía
lse posgrados: O sea,
Fabrizio De Luca: no.
lse posgrados: vos sos de las personas que no tienen un proyecto asignado, digamos, no ten comenzar
Fabrizio De Luca: No, tengo una idea. Bajada. En realidad sí tengo un dataset, pero eh no lo tengo en esta máquina que estoy trabajando.
lse posgrados: Ajá. Y y pero ¿Pero de qué se trata?
Fabrizio De Luca: Eh,
lse posgrados: ¿De qué de qué se trata?
Fabrizio De Luca: es el de cojeras en vacas
lse posgrados: Ah,
Fabrizio De Luca: lecheras.
lse posgrados: okay, okay. Ahora yo te quería ahí en lo lo vi. Vos tenés un vos tenés videos o tenés fotos.

02:16:01

lse posgrados: Videos.
Fabrizio De Luca: videos.
lse posgrados: Okay. Para para los chicos, lo que Fabricio plantea es detectar usando visión por computadora si una vaca tiene o no problemas de cojera a partir de videos, ¿cierto?
Fabrizio De Luca: Sí, simple es eso,
lse posgrados: Sí. Bueno, un problema de visión por computadora. No, no, no, a mí no me parece nada nada.
Fabrizio De Luca: ¿no? Pero el cuento, el cuento es corto.
lse posgrados: Pero vos tenés videos con los cuales podimentar un un modelo de visión por computadora.
Fabrizio De Luca: Sí. Bueno, ahí es un poco la dificultad que estoy teniendo hoy, que no es que solo tengo el video, tengo pocos videos, estoy trabajando con 80 videos, este, necesitaría mucho más, pero aparte están etiquetados por mí, ¿eh? Y vamos,
Gabi Tallarico: Te podemos ayudar a buscar los videos.
Fabrizio De Luca: Gabi, todo inta,
lse posgrados: en vez de videosun
Fabrizio De Luca: todo Inta, Inia metido dentro. Sí, le he mangueado a mucha gente, la verdad, le he mangueado mucha gente videos y he hablado con de Argentina con Enrique Pocher,
lse posgrados: por
Fabrizio De Luca: que es una persona que sabe mucho de patas en pacas, también de acá de Uruguay con Juan Manuel, capaz alguno lo conoce ahí porque viene alguno de de

02:17:19

lse posgrados: ahí lo que me preocupa,
Fabrizio De Luca: agronomía.
lse posgrados: Fabricio, de tu trabajo es que, digamos, en esta clase no tengas claro qué es lo que va a entregar ni qué va a entrar, digamos, ¿no? O sea, eso me preocupa, digamos, que que no o sea, yo esto que vos me digas, mira, entra un video y sale eh un un video etiquetado,
Fabrizio De Luca: No.
lse posgrados: digamos, donde cada vaca va decir va con una label, con una determinada probabilidad si está enferma o no está enferma, digamos. Si vos me explicass eso,
Fabrizio De Luca: Sí, eso sí.
lse posgrados: yo me quedo tranquilo porque sé que lo va a poder lo lo capaz que no lo pero lo tenés claro,
Fabrizio De Luca: Sí. Hoy sí,
lse posgrados: digamos.
Fabrizio De Luca: sí, hoy hoy mi idea no es entregar un producto, que cuando me refiero a producto es entregar una cámara puesta en un establecimiento porque tiene mucha complejidad a nivel de dónde se pone el hardware, internet, etcétera, etcétera, pero sí de de cargar un video, como si fueran una app, cargar un video. Y hoy tengo avanzado hasta las hasta la estimación de poses, que es estoy etiquetando poner los puntos en la vaca para hacerlo a través de poses estimation.

02:18:24

Fabrizio De Luca: O sea,
lse posgrados: Okay.
Fabrizio De Luca: ya con los 80 videos lo que logré entrenar es es que ponga los puntos que voy a tomar como referencia para hacer el círculo de de la
lse posgrados: Perfecto. O sea,
Fabrizio De Luca: cojera.
lse posgrados: vos no vas a entregar directamente la la probabilidad de cojera, sino más bien un video etiquetado con los tags en los puntos que te después te servirían para determinar si tienen coger o no.
Fabrizio De Luca: No, eso es lo que tengo ahora hecho. Eh, mi idea es es Sí, es el escor de cojera. Si no llego a eso, por lo menos decir si es una vaca sana o una vaca renga, porque hay una dificultad ahí en, o sea, es claro cuando una vaca está este sana, pero después el los grados de cojera hay, para explicarlo para todos los grados de cojera hay varios, pero el que estoy tomando yo es del uno al cinco. Uno es una vaca sana. Cinco es una vaca que no camina casi. Es muy fácil darse cuenta un grado cinco para alguien que no sabe como yo. Y es muy fácil darse cuenta que una vaca sana. Pero después para lo que sirve realmente el establecimiento es detectar una vaca dos y tres, que es una vaca que tiene cierta dificultad para caminar, pero no te das tanto cuenta, ¿no?

02:19:41

Fabrizio De Luca: A simple vista tenés que ser como eh tenés que conocer o ser idóneo o o
lse posgrados: Okay.
Fabrizio De Luca: bueno, o estar entrenado en eso, ¿no?
lse posgrados: Pero con tu digamos vos tus 80 videos puedes separar 60 videos para entrenar y 20
Fabrizio De Luca: Entonces,
lse posgrados: videos para ver cómo funciona.
Fabrizio De Luca: sí, lo que pasa que esos videos los tengo etiquetados solamente para ponerles puntos a la vaca, que después los tomo como referencia. Todavía no tengo videos etiquetados para decir este video con estos puntos es una vaca sana o es una vaca enferma. Y eso es lo que necesito hoy. Espero poder conseguir porque si no mi proyecto no llega a su fin.
lse posgrados: Y y ¿por qué no digo por qué no no bajamos un poco la un
Fabrizio De Luca: Bueno, sí puedo entregar el post estimation, pero en realidad ya hay un hay un un coso ahí que estuve investigando y hay uno que ya pone
lse posgrados: Learning pu decir transfer, perdón, chicos, transfer learning es modelos de visión por computadora que ya existen para determinada solución, que se descargan, se usan, se les pasa y de alguna forma ya resuelven el problema, lo cual, Fabricio, a mí me parece que no está mal, digamos, para esta fase.

02:20:53

lse posgrados: De nuevo, yo voy a tratar de bajar a la mínima expresión posible para que puedan ejecutar algo, digamos, ¿no?
Fabrizio De Luca: Sí, por ejemplo, yo uso solo para la detección del del del bounding box de la vaca para que para que detecte que la vaca sea la misma en toda la trayectoria,
lse posgrados: solo.
Fabrizio De Luca: en todos los frames. Este, pero pero bueno, después he encontrado ya hay unos chinos ahí que tienen uno de cojera, pero no tienen el dataset, entonces no me sirve mucho.
lse posgrados: Yo yo diría que que si digamos también yo entiendo que puede pon por ahí quedar algo más desafiante como para que te aporte más valor,
Fabrizio De Luca: No.
lse posgrados: pero los fines de la materia yo creo que con que completemos la justificación del proyecto, el bonding box, la aplicación de de yolo para detectar vacas en los videos y y la siguiente fase de ese posting estimation, etcétera, y ya por más que ya lo tenga desarrollado, me parece que ya ponerlo en un documento es un avance y ponerle toda esta lógica, digamos, que que pedimos en el documento ya es suficiente. Eh, yo creo que con eso con eso estamos hasta ahí.
Fabrizio De Luca: Perdón, perdón que me viene mi hijo,
lse posgrados: Sí, sí, tranqui, tranqui.

02:22:06

Fabrizio De Luca: chicos.
lse posgrados: Yo creo que hasta ahí está está okay, Fabricio. No hace falta, digamos, hacer el modelo de renguera de una sola vez, si no vamos una fase antes y algo que podá explicar,
Fabrizio De Luca: A ver.
lse posgrados: aplicar, ¿entendés? calcularle alguna métrica, etcétera.
Fabrizio De Luca: para que te voy a ver si te puedo mostrar algo. Eh, pasa que estoy justo en la computadora del trabajo y está toda bloqueada, entonces no puedo bajar mi programa, nada. A ver si puedo bajar esto. Bueno, si quiere que sea otro y ahora les muestro un video de lo que
lse posgrados: Compartme a mí en mi correo,
Fabrizio De Luca: hace,
lse posgrados: compartirme y digo para que me mi
Fabrizio De Luca: ¿no? Lo que hace el lo que hace un bounding box. En realidad le cargo el eh un video que sí tengo yo grabado por mí de vacas y lo que hace es
lse posgrados: trabajo
Fabrizio De Luca: poner el score de la vaca. Lo que hace Yolo en realidad que te devuelve un video con el impon de la vaca
lse posgrados: ya eso ya con eso estamos,
Fabrizio De Luca: y

02:23:15

lse posgrados: eh, te digo, si lo queres escalar un poco más, hacerlo, pero me parece que que con
Fabrizio De Luca: ah, pero eso como muy poco en realidad,
lse posgrados: Eso tenés certeza
Fabrizio De Luca: ¿no? Ok.
lse posgrados: de vos tenés certeza de que va a poder aunque esté clasificado mal si está renga o no está renga dale. Si no va solamente identificación. Bueno, vamos al siguiente. Shimon Shimon, perdón, Shimon,
Shimon Achtung: Eh, bueno, más que preparar el ¿Qué tal?
lse posgrados: comentanos.
Shimon Achtung: ¿Cómo andas? Eh, más que preparar este el canvas, estuve tratando de estar interesando bien por lo que decían los compañeros. Eh, yo tengo el proyecto ese que el nombre lo dejé ahí, pero bueno, después es una marca registrada que la tengo que cambiar. Decme qué se siente, que es básicamente tomar la URL de videos de YouTube y empezar a a ver, tomar esos datos para ver eh qué bueno, voy a voy a ver lo que completé de acá, el Corpus, ¿no? tomar la URL,
lse posgrados: O sea, vos vas a transcribir,
Shimon Achtung: eh,
lse posgrados: vos vas a transcribir videos de YouTube.

02:24:16

lse posgrados: Va ser tu corpus tierno.
Shimon Achtung: tomar la URL, este,
lse posgrados: Sí.
Shimon Achtung: la digamos la con Fernando lo que trabajé es un un colab con Python y un este Ah,
lse posgrados: A ver, verlo así rapidito.
Shimon Achtung: no, no lo tengo acá que te mandé por mail, pero es una interfaz de gradio donde le cargo la URL y bueno, ahí empieza a dar comentarios positivos, negativos. o eh raro o imprevisto, digamos,
lse posgrados: No, no,
Shimon Achtung: para para sacarme,
lse posgrados: no me queda no me queda claro comentario de que del chat del video
Shimon Achtung: claro, perdón,
lse posgrados: o Ah,
Shimon Achtung: los comentarios de los videos de YouTube.
lse posgrados: okay. Entonces, tu dataset es vas a entrenar un modelo que tiene una determinada cantidad de URLs. Esas URL te generan un un chat, digamos, un documento de texto que es un chat y vos a cada frase o cada respuesta del chat te va a poner una etiqueta si es buena, mala o media, etcétera.
Shimon Achtung: Claro, por ejemplo, no sé, no, un político, ponés la URL de un video de un político y en los comentarios en en mi dataset, o sea, lo que va a utilizar para para ver si los comentarios son positivos, negativos.

02:25:29

Shimon Achtung: Eh, acá contesto a que me preguntaran es gradio es la interfaz que explicó Fernando en un este.
lse posgrados: como
Shimon Achtung: Exacto. Y ahí me da ay, Gabi, este ver los resultados para que para ver las métricas rápidamente. cualquier persona que sea, no sé, este, que trabaje en marketing, que sea docente, que sea lo que fuere, puede haber métricas rápido que no son muy rigurosas, pero sí que podés ver este rápidamente que qué daga, digamos, ¿no? Eso es lo que entra y lo que sale
lse posgrados: O o sea, para entenderlo, tu vos vas vos vas a sacar el texto de cada URL,
Shimon Achtung: básicamente.
lse posgrados: que es un chat, vas a etiquetar a mano, digamos, eh para entrenar ar el modelo decir, bueno, esto es positivo, esto es negativo. Digamos, estoy pensando en un benchmark sencillo.
Shimon Achtung: Sí.
lse posgrados: A cada texto lo va a pasar un modelo de embeding, usar algún modelo de clasificación supervisada, por ejemplo, digamos, learn, etcétera, y te va a dar un modelo.
Shimon Achtung: Mhm.
lse posgrados: Ese modelo vos lo vas a servir a un usuario que está haciendo, por ejemplo, un streaming. Entonces, ese modelo que va a hacer es se alimenta del chat, o sea, le ingresa una URL del streaming y a medida que van saliendo los comentarios en el chat, te va a dicir, "Este comentario es positivo, este comentario negativo." Lo entiendo

02:26:47

Shimon Achtung: No, a ver, que que vos puedas ver un cuadro con una métrica donde puedas,
lse posgrados: así.
Shimon Achtung: no sé, si vos te interesa de repente ver eh sobre algo que vos estás investigando, poner la URL y decir, "Bueno, los comentarios de este video son positivos, negativos o hay palabras raras que de repente no uno no pueda del tema que vos quieras. vos agarras la URL, la cargas en ese en esa pequeña interfaz de gradio y ahí te empieza a dar los
lse posgrados: métricas.
Shimon Achtung: comentarios y vos tenés que crear los comentarios,
lse posgrados: Sí, te voy a decir claro,
Shimon Achtung: digamos, las métricas de los comentarios.
lse posgrados: pero yo,
Shimon Achtung: Claro,
lse posgrados: perdón, soy usuario y necesito saber cómo voy a usar esto, digamos,
Shimon Achtung: claro.
lse posgrados: yo le pongo la le pongo la URL de un de un documental y me va a entregar las métricas.
Shimon Achtung: Sí,
lse posgrados: 50 comentarios positivos, 20 comentarios negativos. Eh,
Shimon Achtung: exacto.
lse posgrados: okay, perfecto. Es, o sea, sería un modelo de clasificación, básicamente.
Shimon Achtung: Eh,
lse posgrados: Bien. Sí.
Shimon Achtung: sí.

02:27:39

lse posgrados: y y lo y lo lo pensabas aplicar con ese modelo de clasificación usando LLMs, creo que como lo hiciste, o usando un modelo de clasificación basado en, no sé, en en machine learning, por ejemplo.
Shimon Achtung: No sé si tengo tanto.
Gabi Tallarico: Y y por qué de clasificación y no de ponderación,
Shimon Achtung: A ver.
Gabi Tallarico: porque no estaría como tanteando la temperatura del humor del video, va a decir de las sensaciones.
Shimon Achtung: Sí, es
Gabi Tallarico: Habría como un nivel de temperatura social en lo que estás midiendo en vez de clasificarlo.
Shimon Achtung: un depende de la hora de que
lse posgrados: pasa que claro,
Shimon Achtung: ingreses.
lse posgrados: pero vos ponete lo yo necesito entender cuál es el input.
Gabi Tallarico: No.
lse posgrados: El input son chat, los comentarios del video.
Shimon Achtung: lead comentarios de
lse posgrados: El video, ¿sí? Todos los comentarios que vienen en la URL. Ahora,
Shimon Achtung: Exacto.
lse posgrados: digamos, vos podrías al final, digamos, después de clasificar cada comentario, hacer una métrica general del video usando esos comentarios.
Shimon Achtung: Sí,
lse posgrados: Sí.
Shimon Achtung: lo que lo que puedo decir es aplicar un gráfico en el cual la persona automáticamente pueda detectar si tiene buenos o malos comentarios el video.

02:28:52

lse posgrados: Sí,
Shimon Achtung: No, si se
lse posgrados: está claro, está acotado, está bien. Lo que sí yo tengo que te tengo que decir que bueno,
Gabi Tallarico: Oi.
lse posgrados: tu benchmark, digamos, tu modelo más sencillo,
Shimon Achtung: puede
lse posgrados: yo lo lo que haría sería tomar los comentarios, armar un dataset de muchos comentarios, digamos, etiquetarlos vos a mano primero, digamos, decirte, bueno, esto es malo, no delegarle eso a un LM. etiquetarlo vos a una x cantidad, digamos, cuando tengas tu dataset, usa un modelo de psych de clasificación, digamos, cualquier o el, no sé, el el que vos considere algún modelo de clasificación, porque vos ahí en etiqueta va a decir, "Bueno, este comentario es bueno, malo, intermedio, va a tener tres etiquetas." Listo. Una vez que tengas eso hecho, es tu benchmark. Es el modelo más sencillo. ¿Cómo lo va a mejorar? decir, bueno, no voy a usar un modelo de clasificación ahora. Voy a usar algo que que lo puede para mejorarlo. ¿Cómo lo usando LLM? Entonces, en tu segunda versión de tu mejora ya no vas a usar el el el clasificador que puede tener errores,

02:29:53

Shimon Achtung: Mhm.
lse posgrados: sino más bien va a usar un LLM. Y en ese LLM ahí ya le aplicas un modelo de clasificación con algún prom, etcétera, para que clasifique y ahí podés comparar y ahí queda cerrado, digamos. ¿Me entendés?
Shimon Achtung: Ahí.
lse posgrados: Y ahí ya me me cierro un poco más. Ahí va a poder jugar entre eh cómo convertirlos en beding de cuántas dimensiones, etcétera, etcétera. Ahí lo vamos a ir viendo en es importante que que vos vayas pensando en la próxima clase en la exploración del dataset. Entonces, pues ya tendrías que tener una tabla donde estén la URL del video, los comentarios, la clasificación, la dimensión invading y podamos hacer gráficas con eso, ver más o menos con lo que tenés. No te dio un montón, pero sí algo para maquetarlo.
Shimon Achtung: y y comentas que que busque alguno con una cierta cantidad de comentarios hasta un límite
lse posgrados: Sí,
Shimon Achtung: o en la prueba fue muy chica con 50
lse posgrados: yo diría no, pero parece que esto esto es hay que hacer.
Shimon Achtung: comentarios.
lse posgrados: Yo diría que busqué 10 de distintos temáticas, por ser política, ciencia,

02:30:57

Shimon Achtung: Okay,
lse posgrados: tecnología y que esa sea también una etiqueta más que ayude al NM después, digamos, ¿no?
Shimon Achtung: vamos a
lse posgrados: Entonces y pero sí sería interesante que busques la forma de automatizar el
Shimon Achtung: ir
lse posgrados: pipeline, decir, "Yo eres un ministro una Elluve tabla con los comentarios para que vos esa tabla después la puedas etiquetar." Sí, eso ese es como tu desafío para la próxima clase.
Shimon Achtung: ok.
lse posgrados: Eh,
Shimon Achtung: Gracias.
lse posgrados: que veamos. ¿Hay algún voluntario? Así empezamos a Gabi, te veo ahí. ¿Estás muteada,
Gabi Tallarico: Ah,
lse posgrados: Gab?
Gabi Tallarico: tengo muchas cosas abiertas y nada de lo que corresponde. Eh, a ver si les muestro lo que tengo compartido.
lse posgrados: No han tenido otra instancia donde han compartido, ¿cierto? Las cosas que están haciendo. Al menos el anterior no lo vi.
Shimon Achtung: una sola vez en en el bimestre dos que mostramos con data mining esto, análisis de datos. M.
Gabi Tallarico: No encuentro ni lo que mandé. Espérenme, no estaba preparada.

02:32:20

juan ignacio sinopoli: Ok.
Gabi Tallarico: Te preparo. Vaya alguien buscando,
lse posgrados: Bueno,
Gabi Tallarico: presentando si quieren y yo ya me preparo.
lse posgrados: vamos Juan algo
Gabi Tallarico: Después vengo
lse posgrados: para a ver,
Fabrizio De Luca: Le muuestra las vaquitas si quieres.
lse posgrados: a ver,
Fabrizio De Luca: Mira a ver si
lse posgrados: a ver,
Gabi Tallarico: yo.
lse posgrados: Fabricio,
Fabrizio De Luca: tengo. Avisan cuando vean.
lse posgrados: se ve, se ve.
Fabrizio De Luca: No se ve nada. No se ve.
lse posgrados: Sí, se ve. Se ve. Se ve el navegador.
Fabrizio De Luca: Ah.
lse posgrados: Ahí está. Se ve en Windows. Para mí está, para mí hasta ahí ya estamos.
Fabrizio De Luca: Hermoso.
lse posgrados: Eh, sí, sí. Si si tenés un par de videos para decir esta vaca está renga, esta no así,
Fabrizio De Luca: Eso lo hace solo yo. Lo veces como muy
Gabi Tallarico: Es posible.
lse posgrados: pero pero para eso están,
Fabrizio De Luca: poco.
lse posgrados: digamos, igual los LLM hacen gran parte del trabajo, digamos, no no digamos tratarlo y

02:33:30

Fabrizio De Luca: Okay.
lse posgrados: no gasté más tiempo en desarrollo, digamos, porque capaz que no lleg Bueno, eso ya la vara te la pones vos,
Fabrizio De Luca: Bueno, no sé si se recuperó.
lse posgrados: Dav. Marcelo, te veo ahí. Tenés tu PDF de No sé si un PDF, pero tu reglamento de regatas.
Marcelo Luna: Tengo les puedo mostrar el el el prototipo que tengo,
lse posgrados: Ale
Marcelo Luna: la prueba de concepto o algo por el estilo, pero les cuento de qué se trata el eh e digo, lo que lo que conceptualicé es un asistente para analizar incidentes en regata. Eh, no me quiero extender porque además como es un tema que me gusta, puedo hablar toda la noche. Eh, pero cuando hay barcos corriendo regatas, hay situaciones en donde eh se protestan. No digo, me hicieron una infracción. Eh, normalmente en la mayoría de las competencias no se resuelve en el momento, se resuelve posteriormente con la intervención de tres jueces que analizan el relato. Bueno, hay hay un montón de de cuestiones. Eso está todo basado en un en un reglamento que es internacional y y que digo que es disponible. Eh,
Fabrizio De Luca: Le llegó el regata.
Marcelo Luna: sí,
lse posgrados: Oh.

02:34:56

Marcelo Luna: no,
Fabrizio De Luca: segundos.
Marcelo Luna: el bar funciona en las competencias de alto nivel donde lo es en línea, ¿no? Que te marcan con la rayita, con video, con no sé qué. Eh, acá la cosa es un poco más sencilla, pero es okay. Basado en el relato del barco que hace la protesta, eh, identificar cuáles son las reglas que aplican en el incidente y llegar a una eh conclusión, a una determinación si corresponde o no una penalización, a quién le corresponde la penalización y demás. Eh, eso es lo que Sí,
lse posgrados: Está clar.
Marcelo Luna: perdón.
lse posgrados: Yo te digo cómo lo cuando cuando leí tu caso, yo cómo lo conceptualizaría, digamos, haber visto tu documento, ¿no?
Marcelo Luna: Mhm.
lse posgrados: Yo conceptualizaría primero por un lado, por un lado un sistema rack que tenga todo el reglamento, digamos, donde tu input sea el reglamento, me imagino que un PDF,
Marcelo Luna: Sí,
lse posgrados: un documento. Okay, eso va a entrar.
Marcelo Luna: sí,
lse posgrados: A eso le vamos a aplicar procesamiento de texto, porque es importante,
Marcelo Luna: sí.
lse posgrados: no es lo mismo, me imagino, no es lo mismo las reglas que aplican al comportamiento de las personas que reglas que aplican al tamaño de la vela.

02:36:10

lse posgrados: ¿Qué s yo? No sé,
Marcelo Luna: Sí.
lse posgrados: por ejemplo. Bueno, okay, esa es una primera parte. Una segunda parte,
Marcelo Luna: Mm.
lse posgrados: yo lo creo que lo que haría sería a modo de testing si tenés
Marcelo Luna: Sí.
lse posgrados: relatos, relatos que vos puedas poner en en cosas de cosas que hayan pasado, no sé, 10, 15 relatos para poner a prueba esto. Entonces, nosotros al relato también le tendríamos que hacer algún trabajo para sacar lo
Marcelo Luna: Mm.
lse posgrados: conceptual, lo semántico del relato que esté relacionado con las reglas de la
Marcelo Luna: Sí. Eh, digo,
lse posgrados: protesta.
Marcelo Luna: ya pasé con este variaciones, pero pasé por todo ese proceso. Eh, les muestro, hay un caso de que es como casos de referencia que publica la misma ISAF, que es la que establece las reglas. Eh, y yo lo que hice fue sacar el ground trot de ese conjunto de casos en particular.
lse posgrados: Ah,
Marcelo Luna: Eh, hay sí algunas cosas que vos me sugeriste y que yo también después este fui elaborando, que por ejemplo recuperación semántica en lugar de léxica, eh aplicar este expresiones regulares para hacer el eh eh para hacer todo el procesamiento del del reglamento Rag.

02:37:30

Marcelo Luna: Entiendo que todo eso me va a ayudar a mejorar las métricas. Sí. Eh, lo que lo que hice, les puedo mostrar ahora si tienen 2 minutos de paciencia. Esto es el el como el prototipo. Eh, yo lo estoy corriendo con con los modelos que puedo instalar en Oyama local. Eh, usé un modelo de quen que tiene mejor rendimiento que el Yama 3. Acá se pueden elegir los modelos a a ejecutar, pero yo prefiero ese. Y después lo que hice fue diferentes pruebas con el idioma del system prompt en español, en inglés y con la estrategia también, porque en Chain of thought directamente los resultados eran más pobres que usando F shot,
lse posgrados: Claro.
Marcelo Luna: lo cual es bastante razonable, eh, Pero digo, les muestro muy rápido, este es el caso de dos barcos en donde hay establecido un derecho de paso, pero el el barco que tiene derecho de paso intenta forzar al otro a comer la infracción y y es como que lo persigue y lo persigue hasta que comete la infracción. Sí. Eh, digo, en este caso en particular y el barco I es el que tiene el derecho de paso, pero como como orzando es la maniobra que hace que lo acerca cada vez más a B,
Shimon Achtung: Yeah.
Marcelo Luna: B no puede evitar el contacto y entonces se produce un contacto.

02:38:49

Marcelo Luna: Entonces,
Shimon Achtung: Halo
Marcelo Luna: la el resultado del incidente debería ser que el que es penalizado a pesar de tener el derecho de paso es Sí. Sí. Eh,
lse posgrados: Yo ahí yo ahí,
Marcelo Luna: sí,
lse posgrados: perdón, yo no le dejaría esa decisión al a la a la máquina.
Marcelo Luna: Ale.
lse posgrados: Yo traería toda,
Marcelo Luna: Mm.
lse posgrados: yo lo dejaría solamente hasta que traiga las reglas relacionadas y que lo lean las
Marcelo Luna: Okay.
lse posgrados: reglas y listo, digamos, ¿no? O sea,
Marcelo Luna: Okay.
lse posgrados: no le dejaría esa decisión al al LM, digamos, ¿no? ¿Por qué? Porque porque en esa explicación del incidente debería ser
Marcelo Luna: Hm.
lse posgrados: semánticamente tan bien escrita, digamos, que para que el modelo la entienda e interprete con el reglamento y hay como una complejidad que
Marcelo Luna: Aha.
lse posgrados: quizá, digamos, no queremos explorar en esta instancia. Yo en en tu caso sería que de hecho lo tenés hecho, sería tener el reglamento y un sistema RAC que ante una situación te aporte cuáles son las reglas relacionadas a esa situación y que eso le sirva a un jurado o al juez o jueces que en función de las reglas la hagan cumplir y generen un resultado, pero que la resolución sea a partir del humano, no de una máquina, digamos.

02:40:05

Marcelo Luna: Okay.
lse posgrados: y lo cortaría como ahí, digamos,
Marcelo Luna: Eh,
lse posgrados: ¿no? Yo capaz que le estoy acotando un montón los alcances, pero bueno, es para que sea algo escalable,
Marcelo Luna: no, a ver,
lse posgrados: ¿viste?
Marcelo Luna: yo yo lo entiendo. Esta esta es la respuesta del sistema, ¿no? Eh, identifica los hechos, identifica cuáles son las reglas que aplican. Hace un rayonale, ¿sí?
lse posgrados: Perfecto.
Marcelo Luna: Fíjate que inclusive deduce que hay maniobra de I que implica cambio de rumbo que limitan la capacidad de B y decide penalizar ahí como corresponde.
lse posgrados: Claro,
Marcelo Luna: ¿Qué qué qué me pasa si lo si lo corto? Lo digo,
lse posgrados: perfecto.
Marcelo Luna: entiendo el punto, eh, pero empiezo a sentir que deja de aportar valor porque la mayoría de los jueces internacionales hoy en día ya saben cuáles son las reglas que aplican,
lse posgrados: Memoria.
Marcelo Luna: ¿me entendés?
Fabrizio De Luca: Y los que compiten, me imagino que también a este
Marcelo Luna: Sí,
Fabrizio De Luca: nivel
Marcelo Luna: digo, en general vos sabés cuáles son las reglas por la que protestás.
Fabrizio De Luca: como la Fórmula
Marcelo Luna: Sí. Eh, ahora, ¿cuál es cuál es el objetivo de esto?

02:41:14

Marcelo Luna: Pero el objetivo no es que esto sea el juez del caso,
lse posgrados: sistema de apoyo de decisiones.
Marcelo Luna: sino que que sea que sea como la base para que
lse posgrados: Sí.
Marcelo Luna: digo, después la decisión de los tres jueces confluye y no siempre son eh alineadas. Entonces sí, bueno, a ver, para tenemos una orientación de cómo analizar este caso. A partir de eso, si estamos de acuerdo, vamos y tomamos la decisión específicamente.
lse posgrados: Claro.
Marcelo Luna: E lo que agregué, no digo, es como un aspiracional, es meter también la versión del otro barco, porque el barco tiene el protestado tiene derecho a hacer el descargo. Sí, pero ahí también agrega una complejidad mayor que es, bueno, che, pero cuál me dice la verdad, ¿no? Eh, y por eso lo tengo medio por ahora en pausa esa parte, pero
lse posgrados: Yo de nuevo hay que acotarlo, hay que acotarlo. Creo que hasta ahí donde está, digamos,
Marcelo Luna: sí.
lse posgrados: un posible dictamen con las reglas relacionadas, eh, etcétera. Sí, ahí lo que digamos digamos yendo yendo al al canvas que tenés que llenar. La propuesta de valor está clara, ¿sí? Los modelos están claros.

02:42:28

lse posgrados: Por ahí me gustaría conocer un poco más cuando me compartaste, creo que ya lo hiciste, el el sistema de embeding que está usando y todo lo que es preproceso para para armar los chanks, digamos, ¿no? A ver cómo cómo
Marcelo Luna: Sí, ahí digo,
lse posgrados: armaste.
Marcelo Luna: todavía necesito refinar un poco porque fue como muy fui por lo más simple para la prueba de concepto. O sea, el objetivo de mi prueba de concepto era probar el razonamiento del modelo a partir
lse posgrados: Claro.
Marcelo Luna: de un procesamiento muy muy elemental del reglamento. Eh, digo, este es el canvas que armé,
lse posgrados: Sí,
Marcelo Luna: pero está también como muy como muy
lse posgrados: sí, sí, sí. Me parece bien,
Marcelo Luna: superficial.
lse posgrados: te recomiendo para mejorarlo, digamos. A ver,
Marcelo Luna: Mm.
lse posgrados: no lo conozco en detalle,
Marcelo Luna: Eh,
lse posgrados: pero es probable que tengas oportunidades de mejora en el en cómo tratas al
Marcelo Luna: acá.
lse posgrados: Corpus,
Marcelo Luna: Sí, absoluto.
lse posgrados: digamos.
Marcelo Luna: E lo que de hecho lo que vos me sugeriste en el mail es identificar expresiones regulares para entender reglas, modificadores, digo, varias cosas, eh, y sobre todo hacer recuperación semántica, porque para mí todo eso va a contribuir, eh, digo, los números que me dio en las pruebas que hice no me gustaron mucho.

02:43:44

Marcelo Luna: me da el mejor de los casos, un 80% de de aciertos, digo, por decirlo de alguna manera.
lse posgrados: Claro, hay ahí vamos a ver más adelante las métricas. Igual yo por cadena de correo le voy a compartir las métricas de los RACs para que tengan en cuenta, porque hay varias métricas que puedo poder tener en cuenta en un RAC,
Marcelo Luna: Okay.
lse posgrados: pero para eso digamos que tu sistema está pensado en el usuario porque ya como entrega,
Marcelo Luna: Correcto.
lse posgrados: pero no está pensado en el en vos que lo estás desarrollando. Entonces,
Marcelo Luna: Mm.
lse posgrados: de alguna forma, capaz que tu desafío es agregarle antes que tome la decisión algo
Marcelo Luna: Ok,
lse posgrados: visual para que te entreguen los cada para ver y explorar qué documentos te estás recuperando para tomar esa respuesta. ¿Sí? Entonces, vos cuando lo veás va a decir, "Che, pero está tomando la regla 65 y en realidad tiene que aplicar la 63 y la 62.
Marcelo Luna: ok.
lse posgrados: Este texto le está sumando ruido a la respuesta. Entonces, me parece que por por ahí viene,
Marcelo Luna: Okay.
lse posgrados: o sea, por un lado, ¿cómo tratas el corpus y por otro lado las métricas que usas del RAC?

02:44:52

lse posgrados: Para las métricas rack,
Marcelo Luna: Sí,
lse posgrados: sí o sí va a necesitar una ventana o o en tu sistema un lugar donde te vos veás claramente qué documentos te está mostrando.
Marcelo Luna: sí. Okay.
lse posgrados: Buenísimo. Está bueno, che me me Vos sos desarrollador.
Marcelo Luna: ¿Cómo? ¿Cómo?
lse posgrados: ¿Sos desarrollador o
Marcelo Luna: Hace muchos años que no trabajo más como desarrollador,
lse posgrados: lo
Marcelo Luna: pero sí soy ingeniero en sistema, tengo conocimiento.
lse posgrados: meté mano? Claro. Sí, sí, sí. Está claro.
Marcelo Luna: Sí,
lse posgrados: Y lo ten lo tenés localizado
Marcelo Luna: no,
lse posgrados: eso.
Marcelo Luna: no está es muy prototipo, está hecho todo
lse posgrados: Okay.
Marcelo Luna: local.
lse posgrados: Okay. Para que lo que sepan,
Fabrizio De Luca: ¿Puedo hacer un comentario?
lse posgrados: hay un hay
Fabrizio De Luca: ¿Puedo hacer un comentario ahí del sistema?
lse posgrados: ¿Cómo?
Marcelo Luna: Sí.
Fabrizio De Luca: Puede ser que sé poco de regatas, ¿no? Pero yo me imagino si estuviera compitiendo, capaz sería como un una herramienta para challengear mi mi protesta.

02:45:48

Fabrizio De Luca: No sé si me explico. O sea, si voy con la protesta,
Marcelo Luna: Sí,
lse posgrados: Sí, claro.
Fabrizio De Luca: capazciaría mi mejor protesta con la herramienta,
lse posgrados: con todo esto,
Fabrizio De Luca: digamos.
Marcelo Luna: sí,
Fabrizio De Luca: tiro. No, no vayas por ahí. El dictamen fue para el otro. Entonces, cuando el dictamen es como para mí,
Marcelo Luna: sí,
Fabrizio De Luca: ahí voy con
lse posgrados: abogado
Marcelo Luna: sí. Eh,
Fabrizio De Luca: eso.
Marcelo Luna: digo, por eso los competidores son usuarios finales también del sistema en
Fabrizio De Luca: Ah, bueno,
Marcelo Luna: particular,
Fabrizio De Luca: felicitaciones. No sé si no sirve para nada mi opinión.
Marcelo Luna: ¿no? Sí, cómo no. La opinión de todo sirve, ¿cómo no?
Fabrizio De Luca: Ah.
Marcelo Luna: Sí.
lse posgrados: se me ocurrió algo que cuando vos si podés traer la en el texto, sorry, se me me acaba de de aparecer una la fecha, me imagino que la fecha también puede jugar ahí con variables como no sé, me imagino que si es un domingo, capaz que los domingos la gente hace un comentario más positivo y y si no se decide un lunes o un miércoles, mitad de semana, todo, ¿me entendés?

02:46:45

lse posgrados: como que hay hay hacer mining ahí en la fecha y en todo lo que puedas sacar para ver qué
Shimon Achtung: semana.
lse posgrados: más. Capaz que no hay nada, pero al menos exploralo, digamos.
Shimon Achtung: El domingo es un corchazo, pero sí.
lse posgrados: Ah,
Shimon Achtung: Ok.
lse posgrados: bueno, Gabi, eh, Gabi,
Gabi Tallarico: Sí,
lse posgrados: igual tenemos Dale,
Gabi Tallarico: ahí voy,
lse posgrados: conto.
Gabi Tallarico: ahí voy, ahí voy,
lse posgrados: Dime.
Gabi Tallarico: ahí voy. esto llegué, no sé si ves, ahí está mi mi canvas que no no sé si no lo terminé de completar, pero les cuento un poco la idea. Eh, estoy intentando armar un agente inteligente de tipo asesoramiento técnico. la expectativa de la materia anterior, me dijeron que nada, que baje y que con un chatb era suficiente, pero el proyecto quiere no solamente integrar fuente bibliográfica seleccionada y que sea un corpusrado, es decir, que no esté buscando por todas la todo internet, sino que sea los eh realmente un
lse posgrados: documentación
Gabi Tallarico: Exacto.
lse posgrados: validada.
Gabi Tallarico: en función de esa documentación, eh, que responda preguntas de distintos órdenes y características o de enfermedades productivas o de modalidades de producción de cuidado,

02:47:55

lse posgrados: ¿Puedes
Gabi Tallarico: de enfermedad, de plaga y bueno, para eso entonces primero lo que empecé a hacer era el análisis del del corpus que tenía. Eh,
lse posgrados: abrir un PDF?
Gabi Tallarico: sí. Y ahí les iba a mostrar, bueno, los que tenía de todos,
lse posgrados: Hay uno que tiene una tabla, me acuerdo que lo vi, digamos.
Gabi Tallarico: todos tienen tablas, tienen fotos, o sea, que nada, todo ese tratamiento no lo hice. Ese es otro otro problema porque yo lo único que analizaba era los textos del momento. Dije, lo dejo para para el trabajo final. ¿Ven? Estos son los PDF que son totalmente fichas técnicas. Algunos tienen así más texto, otros tienen tabla. Este, por ejemplo.
lse posgrados: Se ve solamente el canvas.
Gabi Tallarico: Ah, bueno, espere, perdón, ahí dejo. Siento de ventana
lse posgrados: Ahí está.
Gabi Tallarico: este, por
lse posgrados: Bueno, ahí ahí me interesa a ver cómo digamos es simplemente una pregunta a ver si alguien se anima a
Gabi Tallarico: ejemplo,
lse posgrados: responder. Para una máquina es fácil leer una tabla.

02:49:13

lse posgrados: La respuesta seguramente es no. ¿Cómo le recomendarían una máquina o cómo ustedes en qué transformarían esa tabla? Pon una tabla, Gabi, porfa.
Gabi Tallarico: A lo mejor tengo que convertir eso un Excel y ya está. Y pasarle un Excel,
lse posgrados: Cerca, está cerca, está cerca. Marcelo tiene la respuesta.
Gabi Tallarico: ¿no?
lse posgrados: Marcelo, ¿no? Bueno, yo lo convertiré en un Jason. ¿Saben lo que es un Jason?
Marcelo Luna: Ah, okay. Puede
lse posgrados: Sí,
Gabi Tallarico: Sí.
lse posgrados: la máquina entienden rápido los Jason,
Marcelo Luna: ser.
lse posgrados: digamos. Entonces, por ahí capaz que tu desafío para esta semana, Gabi, es encontrar una forma usando LM o rejex, procesamiento queamos de patrones, etcétera, de convertir esas tablas en en un en un Jason. Ahora, y la pregunta es,
Gabi Tallarico: Bien.
lse posgrados: en tu caso particular, si solo van a ser 12 documentos, ponete, yo le agregaría valor a esto si no encontrar una forma automática hacerlo a mano, o sea, hacerlo vos a mano, digamos, ¿no?
Gabi Tallarico: Bien.

02:50:21

lse posgrados: Eh, ¿por qué? Porque son solo 12, ¿sí? Y va a aportar más valor. ¿Está bien? Ahora, cuando algo es escalable, digamos, yo le si yo le meto 12 documentos ahora para como para que funcione, después meter 1000 documentos, bueno, sí tenes que buscar una herramienta que lo haga automático, pero sí siempre van a ser 12 como invertir el tiempo para hacerlo,
Gabi Tallarico: No,
lse posgrados: ¿me
Gabi Tallarico: claro. A ver,
lse posgrados: entendés?
Gabi Tallarico: si pienso en este acotado así que es para específicamente para producción de ajo. Sí, digo, van a ser 30 lo suman, digo, no más que eso, porque tampoco hay en el país tanta producción de bibliografía específica e nacional, pero la idea era armar como un prototipo de agente que después se traslade a distintas cadenas o distintos tipo terminamos ajo, empezar con cebolla. Entonces ahí sí el escalamiento de de PDF van a ser enorme. Eh, yo no pretendo tanto, obviamente para la materia, por eso me dijeron nada, trabajar con menos PDF, eh, y manuales, pero bueno,
lse posgrados: De nuevo, llevando esto,

02:51:28

Gabi Tallarico: la chica porfiada.
lse posgrados: un llevando esto un benchmark, vos el benchmark ya lo tenés, digamos, es decir, ya hiciste un rack donde entraron PDF,
Gabi Tallarico: Ah, claro.
lse posgrados: donde el procesamiento de del texto fue, digamos, básico y te dio un resultado. Ahora tu desafío es, bueno, voy a trabajar en el pipeline, en la ingesta para mejorarlo.
Gabi Tallarico: Sí.
lse posgrados: En eso vamos a trabajar para mejorarlo, digamos, y en función de eso volver a probar y ver si las métricas, digamos, de rack mejoran. Sí,
Gabi Tallarico: Bien.
lse posgrados: ese sería hasta ahí llega tu trabajo. Vos documentás cómo funciona así y cómo funciona de otra forma. resuelto, digamos, en el caso de de Shimon, él va a documentar cómo funciona con el cycle learn y una clasificación así y una clasificación usando un LLM y hay una mejora, no hay una mejora, mejora de tanto, etcétera, tiene tanto costo, terminar el trabajo. Sí. Entonces, yo estoy haciendo comentarios generales para que los chicos que no van a poder exponer por el tiempo eh lo lo digamos capten cómo viene cómo viene el trabajo. ¿Algún voluntario para seguir?

02:52:38

lse posgrados: Quedó clarísimo, Gabi.
Gabi Tallarico: Perfecto. No, quería mostrarle que había llegado a hacer un intento ahí como de chat de le preguntaba, qué sé yo, eh, a ver si me deja como Bueno, ahora no puedo. Le preguntaba si iba haciendo preguntas y test y hasta me contaba cuántas preguntas gratuitas me dejaba hacer como lo que hice. Ya quería complicar eso. Ya después lo saqué, pero lo había intentado decir como que después se convertí en pavo. Deja de preguntar
lse posgrados: Claro, claro.
Gabi Tallarico: gratis.
lse posgrados: Igual ahora lo lo que yo voy a hacer esta semana me va a quedar pendiente para mí es enviarle métricas de RAC para que empiecen a conocerlas y la clase que viene les voy a mostrar un rack con con digamos con algunas métricas digamos para que ustedes puedan aplicarlo en su benchmark. Juan, te escuchamos. Gracias,
juan ignacio sinopoli: Buenas, ¿cómo va? Bueno, yo puedo puedo mostrar algo muy muy básico.
lse posgrados: Gabi.
juan ignacio sinopoli: Eh, particularmente tomé la decisión de volver a de seguir el trabajo que presentamos para procesamiento de lenguaje natural. Lo que me doy cuenta es que mi punto de partida es más extractor de entidades, no no es un RAS como tal.

02:54:00

juan ignacio sinopoli: Sin embargo, veo potencial de que lo puedo convertir a eso. ¿Por qué? Porque es la idea que se me ha ocurrido a mí es la la extracción automática de de la información de mensajes que recibe cualquier centro de atención al cliente.
lse posgrados: Claro.
juan ignacio sinopoli: Eh, puntualmente la extracción de ciertas de ciertas entidades propias del mensaje, que ese sería mi corpus. Yo acá ya tengo identificado un sesgo que es, necesito un dataset grande. O sea, yo lo que armé fue con 15 mensajes, algo relativamente acotado y eso puede generar un sesgo,
lse posgrados: Okay.
juan ignacio sinopoli: entonces necesito datos bastante más grandes.
lse posgrados: Wait. Yo entiendo que vos no tenés los textos esos quizás,
juan ignacio sinopoli: Sí.
lse posgrados: pero hacer un hacer un prompt y que te genere 100, o sea, hacer un prom mand a no sé a cualquier Ll y que te genere 100,
juan ignacio sinopoli: Sí,
lse posgrados: 200, ¿sí? cosas, o sea, eso llama datos sintéticos,
juan ignacio sinopoli: sí.
lse posgrados: digamos, ¿no? Eh, generar vos, digamos,
juan ignacio sinopoli: Mm.

02:55:05

Shimon Achtung: Muchas veces eh hay,
lse posgrados: Simón.
Shimon Achtung: por ejemplo, en Facebook, no sé, por ejemplo, tenés línea de colectivo y aparecen los comentarios de del los usuarios. Si encontrás los usuarios de algún tipo de producto para de usuarios o para dar respuesta, puedes tomar esa base de datos y bueno, ahí están más o menos.
lse posgrados: Claro, o sea, buscar la buscar la vuelta por ahí en esa parte. Ahora seguí y creo que te, o sea,
Shimon Achtung: Bueno,
lse posgrados: vos te entran determinada cantidad de mensajes y tú lo que va a hacer tu es entregar una documentación estructurada.
juan ignacio sinopoli: Mhm.
lse posgrados: Eso te entrega, te entrega el mensaje,
juan ignacio sinopoli: Sí.
lse posgrados: pero no sé, escribió una vecina y la vecina te escribió así con muy coloquial y el LM va a interpretar lo que quiso decir y te va a llenar determinadas casilleras en un Jason y a veces va tu
juan ignacio sinopoli: Exactamente, ese es el output,
lse posgrados: salida.
juan ignacio sinopoli: eso es lo que actualmente devuelve y en el en el trabajo el trabajo anterior con a través de la interfaz de gredio. No, eso me me lo volvía formateado ahí, pero sí, el output es un Jason, claramente no es una respuesta, por eso es donde ahí está la la diferencia, ¿eh?

02:56:16

juan ignacio sinopoli: Y justo darme ahora esta tablita bien rápido, como viendo qué cosas tengo que ajustar de la idea original para convertirlo en rag. Eh, puntualmente me dijo lo que estoy iterando, lo iteré ahora un poco con Cloud, ¿no? Para ver cómo podía eh sí transformarlo. Eh, y obviamente me cambié un poco el foco de problema, o sea, que esto no sea una extracción de entidad tan así cruda, sino más una generación de respuesta a partir de un determinado mensaje. Ehm,
lse posgrados: Esa parte si no la tenés clara todavía, yo no la aplicaría del todo a menos que hasta, no sé, hasta la semana que viene la la tenga capaz diseñada. Es decir, yo digamos esto va a ser e-commerce, ¿sí? Eh, creo que está más acotado,
juan ignacio sinopoli: Mhm.
lse posgrados: con lo cual la respuesta debería ser acotada a las reglas de ese e-commerce. No sé eh si la si la pregunta al al o el comentario, etcétera, está orientado a los tiempos, fecha, etcétera, y no se cumplió, será una disculpa. No sé,
juan ignacio sinopoli: Mhm.
lse posgrados: le regalamos tanto cantidad de puntos o lo que sea, digamos, ¿no?

02:57:27

lse posgrados: Digamos, si esa parte de respuesta de la generación de de texto no la tenés del todo definida, yo lo cerraría con porque ponete,
juan ignacio sinopoli: Nada.
lse posgrados: te doy un ejemplo, eh el proyecto de Gabi necesita un reconocedor de entidades y aporta un montón de valor porque si tu proyecto aplicaría tablas como tiene como tiene Gabi, tu parte del proyecto alimenta un sistema RAC y resuelto.
juan ignacio sinopoli: Mhm.
lse posgrados: Juan que presentó al principio, que también lo hemos cortado hasta donde terminó el lugar, hasta este hasta ese reconocimiento que también reconocimiento de entidad y clasificación lo que va a ser Pablo e idem, digamos, ¿no? Entonces yo yo te diría que te centres en el canvas ahora en eso que ya tenés que ya lo tenés claro. Ahora, cuando vos hagas los datos sintéticos, etcétera, y hag,
juan ignacio sinopoli: Okay.
lse posgrados: hagamos la exploración de los datos y ahí se te prende alguna idea para un sistema RAG, está bueno, porque igual RA le puede decir, bueno, eh, ¿cuáles de todos los mensajes están relacionados a incumplimiento de eh facturación, etcétera, no sé? Y van, ¿me entendés?
juan ignacio sinopoli: Bueno, eso en cierto parte lo tengo más o menos definido porque tengo son habíamos definido 13 categorías de problemas que creo que ese puede ser un un condicionante para la evolución de la respuesta del

02:58:49

lse posgrados: Bueno, entonces tu sistema no es solo reconocer reconocer entidades,
juan ignacio sinopoli: RAC.
lse posgrados: sino también un problema de clasificación, porque para reconocer el problema va a tener que aplicar una
juan ignacio sinopoli: Sí.
lse posgrados: clasificación
juan ignacio sinopoli: Sí, correcto. Para lo que quiero armar, sí, para esto en particular, el output era simplemente un Jason y la extracción de los
lse posgrados: Yo creo que digamos el reconocimiento de entidades tiene un un una
juan ignacio sinopoli: datos.
lse posgrados: complejidad y la clasificación usando esas entidades, digamos, y la información de esas entidades, eh tiene otra complejidad. Con esas dos complejidades estamos más que bien, no iría a lo otro. Te doy un ejemplo, no sé si si el mensaje reconoce si es hombre,
juan ignacio sinopoli: Bien.
lse posgrados: varón mujer, si hay más mensaje por parte del sexo femenino o o no definió el sexo en la entidad y bueno, todo ese tipo de información ya aporta valor. Yo creo que lo dejaría hasta ahí, digamos,
juan ignacio sinopoli: Okay, está. Lo mantengo lo más fico posible.
lse posgrados: y de última después escala, digamos, yo creo que hasta ahí podemos cerrar. Bueno,

02:59:57

juan ignacio sinopoli: Perfecto.
lse posgrados: un creo que lo que aplicamos aplica a todos, chicos, ¿no? O sea, los que me quieran compartir por correo, yo me me los mandan a los obviamente todos mándemelos por canvas, no es obligatorio. Mándame los canvas por correo, eh, me sirve un montón conocer, pero a medida que vamos avanzando en los proyectos, eh, yo voy a detectar también aquellos que están más atrás y en las próximas clases me meto más con ellos. Sí. Eh, ¿alguien más? Uno más. Tengo tiempo para uno más. Ahí va.
Lorna Pons: Hola. Yo lo hice en un hice un para explicar así simple. Em, a ver, lo comparto. Está muy simple. ¿Lo ven acá? Sí. Eh,
lse posgrados: Sí,
Lorna Pons: bueno, el mío es una extensión. E lo pensé todavía no no empecé a prepararlo.
lse posgrados: el de matemáticas.
Lorna Pons: Eh, sí, porque yo soy docente de matemáticas de tecnología y en PNL lo que hice fue un asistente de corrección para trabajos de tecnología que tienen más sobre fundamentos, conclusiones personales, tienen más texto. Entonces, lo hice con un LLM y me dio un resultado excelente comparándolo con mis correcciones.

03:01:33

Lorna Pons: Entonces, para hacerlo en matemáticas necesito que sea un rack porque quiero que tome mi resolución del ejercicio, que puede ser de trabajos prácticos o de exámenes. Y eh como deep sic distintas resoluciones. Yo ya lo había probado. pongo, "Bueno, dame tres o cuatro resoluciones distintas de este ejercicio y me las da." Entonces pensaba tomarlas y que corrija a partir de probar cómo corrige a partir de mi resolución y de tres o cuatro más, porque generalmente los ejercicios de matemática tienen cuatro o cinco formas distintas de hacerse e y bueno,
lse posgrados: Claro.
Lorna Pons: y combinar eso.
lse posgrados: Ay, se me ahí me Bueno,
Lorna Pons: Bueno,
lse posgrados: la complejidad digamos de de cognitiva o semántica que tiene la resolución de un de un problema de matemática escapa,
Lorna Pons: Eh,
lse posgrados: digamos, a mi experiencia. Entonces ahí no como que me yo me me yo lo que haría si soy profe de matemáticas hacer preguntas teóricas y irme al texto y semántico, ¿no? Pero si vos te animas a digamos a la generación digamos de de cuatro resoluciones posibles
Lorna Pons: Sí.
lse posgrados: y y que de alguna con una métrica de similaridad, cuán parecida es una resolución respecto de las cuatro posibles que te entrega el modelo y y digamos ahí debería si tenía alguna

03:03:01

Lorna Pons: Sí,
lse posgrados: notebook, etcétera, para compartirme para que revise, ¿viste?
Lorna Pons: sí, todavía no, pero bueno, yo soy de secundaria, profesora, así que son bastante simples las resoluciones y en realidad para texto yo ya probé con lo otro, con lo de PNL y ahora quería ampliarlo y Bueno, ver esto,
lse posgrados: tecnología
Lorna Pons: ¿cómo es la comparación con la nota que pondría yo, porque el asistente devuelve dos cosas, devuelve la nota y devuelve la devolución escrita al docente y alumno.
lse posgrados: lo ten implementado en un colab, ¿cierto?
Lorna Pons: Sí, sí, sí.
lse posgrados: Sí. E digo esto,
Lorna Pons: E
lse posgrados: mira, yo te recomiendo probar esta semana con fórmulas matemáticas,
Lorna Pons: sí.
lse posgrados: con resoluciones matemáticas en en caso que que no que no sea tan coherente, porque de nuevo desconozco qué tan buenos son los modelos para tirar cuatro cuatro resoluciones,
Lorna Pons: No.
lse posgrados: digamos, y que las puedas plantear porque no lo he probado. Si vos ves que va bien, listo, seguimos por ahí. En el caso de que vos ves que está complicado medir, qué sé yo, eh, volvemos un paso atrás y tratamos de mejorar lo lo anterior, si te parece.

03:04:19

lse posgrados: Ah,
Lorna Pons: Dale, dale, dale, dale. Pruebo entonces con,
lse posgrados: bueno,
Lorna Pons: no sé, cinco ejercicios, por ejemplo. Y
lse posgrados: claro, porque aparte tiene la complejidad de que ten me imagino que le ingresa una foto,
Lorna Pons: eh
lse posgrados: le sacó una foto al examen, el examen se tiene que pasar esa foto, la tiene que o de ahí ten ahí tiene una complejidad extra,
Lorna Pons: sí.
lse posgrados: ¿no? que eh digamos si es un examen de matemática, si vos tenés eh que resolverlo la resolución a mano, tenés que pasar la foto a un una determinada cantidad de caracteres, fórmulas, digamos, ¿no? que a la vez tienen que ser entendidas por por la máquina y que es una complejidad extra,
Lorna Pons: Sí.
lse posgrados: pero bueno, no te corto ahí de una, pero sí probar esta semana, si no la semana que viene volantazo y vamos al al
Lorna Pons: Dale, dale, lo pruebo con cinco ejercicios que doy para hacer,
lse posgrados: texto.
Lorna Pons: bueno, o prácticos que yo tengo para corregir, aprovecho y y los uso y No vemos.
lse posgrados: Está está bueno. Bueno,
Lorna Pons: Sí.

03:05:20

lse posgrados: e yo quería para para resumir y para cerrar, yo diría que todos si pueden compártanme por correo eh un PDF con el con el can. No hace falta no hace falta que que esté escrito en el canvas. Si me lo quieren poner un Word, así como mostró Lorna, suficiente. Es para ver que estén alineados y ir siguiendo quién se puede haber quedado atrás para que la clase que viene lo lo alineemos. Y me interesa su feedback ahora así totalmente honesto de cómo ven la dinámica de la clase para ver si la clase que viene ajusto algo o no.
Shimon Achtung: A mí me pareció muy bien, muy lógica, pero bueno, siendo tan
lse posgrados: por ahí los que están en MVP,
Shimon Achtung: disparó
lse posgrados: no sé quién quién está en MVP, así alguien que ya tenga todo medio que Marcelo lo tiene casi atada, la tiene, digamos, eh,
Shimon Achtung: la vuelta, Marcelo.
lse posgrados: pero los que estaban con el tema de de MCP, digamos, de digamos de algo más más avanzado, no como hablaron, pero no les pude ver quién era, no sé quiénes son, digamos.
Juan Pablo Rueda: Sí, está muy buena. A mí me gusta me gustó la clase así, la mejor de todas.
lse posgrados: Bueno,

03:06:37

Juan Pablo Rueda: Yeah.
lse posgrados: ahora la clase que viene va a ser la misma dinámica.
Shimon Achtung: Sí.
lse posgrados: Sí. Eh, entonces para que esto siga funcionando en la clase que viene, como ya los conocemos, traigan datos, quiero ver colaps, quiero ver las tablas, quiero ver los textos, eh, para que podamos ir ir haciendo. Mi recomendación a todos los que están trabajando con texto es que cuando haya una ingesta se genere o una tabla que tenga ingesta, digamos, o un archivo txt con ese con ese chank chank idhan número 1.txt en el propio colab para que se vaya almacenando. ¿Cómo hacerlo? Cloud, digamos, no vamos no vamos a perder tiempo ahí. Cloud, cómo hacer y ahí lo implementan en colab. Eso le da cierta lógica y una escalabilidad mayor. Eh, lo vamos a ver la clase que viene cuando yo les muestre un ejemplo, pero vayan trabajando o una tabla, si es un dataset chiquitito, una tabla que tenga digamos el ID del chan, las cuestiones importantes en chan, el chank, el el no sé si le quieren extraer algo con reje al propio chan, vayan como incrementándole la complejidad, pero deberíamos tener dataset.
Shimon Achtung: Ok.
lse posgrados: Entonces, la clase que viene, como vamos a trabajar con Neda, necesitamos ver dataset para ver de qué se tratan los textos, hacer nube de palabra, cuántos chang en promedio tenemos, cuántos token por chan tenemos, etcétera, etcétera, etcétera, para ir ir viéndolo así.

03:08:07

lse posgrados: Bueno, bueno. Y dudas antes de cerrar, ¿algo que me quieran decir?
Shimon Achtung: Por ahora no te van a llegar mails.
lse posgrados: Bueno, la encuesta y ahí acomodamos todo, no se
Gabi Tallarico: No, que a mí me gustó esa la idea de compartir o de ver los colaps de otros porque veo que hay cosas
lse posgrados: preocupen.
Gabi Tallarico: que por ahí son muy similares para ver cómo las resolvió uno u otro y ver lo que tenemos mal, porque en el propio colap a veces no ni me doy cuenta si tengo las cosa bien o o podría hacerse de otra
lse posgrados: Sí,
Gabi Tallarico: forma.
lse posgrados: mi trabajo es que que digamos entrar a los colab en las clases que viene y empezar a decir, "Che, bueno, mira, leete este paper o mira, te paso este colab con ejemplos y cosas de ahí y aplicalo."
Gabi Tallarico: Claro.
lse posgrados: Ah,
Gabi Tallarico: Excelente.
lse posgrados: bueno,
Shimon Achtung: H
lse posgrados: le quito más tiempo,
Gabi Tallarico: Buenísimo.
lse posgrados: un placer. Espero que nos quedan siete clases más
Gabi Tallarico: Mil gracias.
lse posgrados: todavía.
Gabi Tallarico: Chao. Chao.
Marcelo Luna: Gracias.
juan ignacio sinopoli: Gracias.
lse posgrados: Ciao.
Marcelo Luna: Ciao.

La transcripción finalizó después de 03:45:13

Esta transcripción editable se ha generado por ordenador y puede contener errores. Los usuarios también pueden cambiar el texto después de que se haya generado.

