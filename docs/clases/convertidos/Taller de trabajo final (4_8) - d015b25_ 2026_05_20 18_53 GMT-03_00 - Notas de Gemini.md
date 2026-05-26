# Taller de trabajo final (4_8) - d015b25_ 2026_05_20 18_53 GMT-03_00 - Notas de Gemini

- Fuente: `Taller de trabajo final (4_8) - d015b25_ 2026_05_20 18_53 GMT-03_00 - Notas de Gemini.docx`
- Tipo: DOCX
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

📝 Las notas

may 20, 2026

Taller de trabajo final (4/8) - d015b25

Invitado salinastalamilla@gmail.com Taller de trabajo final - DIIAA 1Co2025

Archivos adjuntos Taller de trabajo final (4/8) - d015b25

Registros de la reunión Transcripción Grabación

Resumen

La sesión integró avances de análisis exploratorio de datos con métricas técnicas para optimizar sistemas RAG.

Avances en EDA y proyectos
Los estudiantes presentaron sus cuadernos de análisis exploratorio de datos, validando métodos de limpieza y estrategias de visualización de resultados. Se determinó que los proyectos cuentan con hallazgos suficientes para iniciar la etapa de documentación final.

Optimización y riqueza léxica
La discusión se centró en la importancia de la lematización y la economía de tokens para mejorar la precisión de los sistemas. Se acordó que estas técnicas son fundamentales para reducir la redundancia y optimizar el rendimiento del modelo.

Métricas de evaluación RAG
Se definió la implementación de métricas de precisión para evaluar los sistemas de recuperación y generación. Se decidió priorizar el análisis de precisión sobre indicadores complejos para medir efectivamente el desempeño del proyecto.

Califica este resumen: Útil o Poco útil

Próximos pasos

[lse posgrados] Responder correos: Responder los correos pendientes de los alumnos al finalizar la sesión.

[El grupo] Enviar documentos: Enviar los trabajos de análisis exploratorio de datos para revisión antes de la clase 7.

[Shimon Ben] Corregir trabajo: Revisar el correo enviado y corregir las observaciones realizadas por el docente.

[El grupo] Documentar mejoras: Redactar los cambios técnicos implementados en el proyecto siguiendo la estructura de resumen, justificación y metodología.

[Shimon Ben] Revisar datos problemáticos: Analizar los casos problemáticos donde se capturaron 206 filas en lugar de 200 para corregir el error en el dataset.

[Shimon Ben] Generar datos sintéticos: Generar datos de forma sintética para la clase minoritaria de comentarios neutros y equilibrar el balance de las clases.

[Shimon Ben] Ajustar gráficos: Rotar los gráficos de barras y los diagramas de caja intercambiando los ejes para mejorar la legibilidad y la presentación en el informe.

[Shimon Ben] Documentar proyecto: Finalizar la documentación del proyecto y pasar todo el trabajo en limpio para su presentación.

[El grupo] Investigar economía tokens: Investigar el repositorio y el artículo sobre el estilo de habla tipo cavernícola para aplicar técnicas de ahorro de tokens.

[El grupo] Coordinar tutoría: Solicitar mediante correo electrónico un espacio de trabajo si requieren apoyo o están atrasados.

[El grupo] Calcular precisión: Realizar 50 preguntas y evaluar la relevancia de los 5 documentos recuperados para obtener esta métrica.

[El grupo] Documentar mejoras: Comparar los resultados actuales con el estado inicial del proyecto para evidenciar el progreso.

[lse posgrados] Responder alumnos: Enviar retroalimentación a los estudiantes sobre los avances en su análisis exploratorio.

Detalles

Introducción y carga de trabajo: Marcelo Luna y Gabi Tallarico comentan brevemente sus compromisos académicos actuales, incluyendo cursos sobre visión por computadora y aprendizaje profundo, mientras coordinan los horarios de cursada (00:00:00).

Revisión de avances del EDA: lse posgrados inicia la sesión confirmando que, en general, los estudiantes han aplicado correctamente los conceptos de Análisis Exploratorio de Datos (EDA) para fundamentar el diseño de sus soluciones, cumpliendo con el objetivo de la etapa (00:00:54).

Logística y contexto de la clase: lse posgrados señala que hay 11 asistentes presentes e insta a los estudiantes a continuar trabajando en la exploración de variables numéricas, palabras y tokens antes de llegar a la clase 7, además de mencionar que responderá los correos electrónicos pendientes al finalizar la sesión (00:03:53).

Comentarios individuales y presentaciones: Shimon Ben indica que debe revisar las correcciones enviadas por correo, mientras lse posgrados invita a Shimon Ben y Marcelo Luna a compartir sus cuadernos (Colab) con la clase para ilustrar el proceso de descubrimiento y los resultados obtenidos (00:05:19).

Visualización de datos y arte: Shimon Ben reflexiona sobre cómo adaptar la visualización de datos para aplicaciones artísticas o instalaciones, utilizando como ejemplo el análisis de obras de autores como Borges. lse posgrados sugiere investigar el trabajo de Cedric, un referente en la comunicación de datos que utiliza gráficos efectivos (00:06:25).

Comunicación de datos y herramientas: lse posgrados destaca que el uso de librerías como Ggplot en R permite crear gráficos de alta calidad y que la capacidad de "curar" y comunicar datos es una habilidad valiosa en el mercado laboral, más allá de la complejidad del código (00:07:53).

Teoría de la riqueza léxica: lse posgrados explica la métrica de riqueza léxica, diferenciando entre *tokens* (todas las apariciones de palabras) y *types* (formas únicas). Se detalla que la relación entre ambos, conocida como *Type-Token Ratio* (TTR), permite medir la diversidad del vocabulario (00:12:10).

Limitaciones del TTR: lse posgrados advierte que el TTR tradicional presenta un sesgo según la longitud del texto: en textos más largos, es más probable que las palabras se repitan, lo que reduce artificialmente la métrica. Por ello, se recomienda estandarizar el texto o utilizar métodos alternativos (00:15:26).

Aplicación práctica de la métrica: Shimon Ben y lse posgrados discuten cómo esta métrica ayuda a identificar redundancia, comparando hipotéticamente la diversidad de vocabulario de una obra literaria frente a letras de canciones, lo cual influye en las decisiones de diseño para sistemas de recuperación de información (00:17:08).

Cálculo mediante media móvil: lse posgrados explica que, para hacer comparables textos de distintas dimensiones, se utiliza una media móvil que calcula el TTR sobre ventanas de tamaño fijo (ej. 50 tokens) que se desplazan a lo largo del documento (00:19:39).

Lematización y RAG: lse posgrados define la lematización como una estrategia de limpieza que reduce las palabras a su forma base (ej. "decretará" y "decretó" a "decreto"). Esto ayuda a estandarizar el texto y mejora el rendimiento de los sistemas de Recuperación Aumentada por Generación (RAG) (00:22:24).

Impacto en el espacio vectorial: lse posgrados advierte que la redundancia léxica sin lematizar puede generar vectores similares para conceptos equivalentes, confundiendo al sistema de RAG y reduciendo la precisión de la recuperación, por lo que ajustar este preprocesamiento es una decisión técnica clave (00:25:40).

Reglas de decisión léxica: lse posgrados sugiere que un TTR inferior a 0.4 indica una redundancia alta donde la lematización podría ser beneficiosa, y anima a los estudiantes a probar este análisis utilizando las librerías y el código de ejemplo proporcionado en la notebook (00:27:29).

Comparativa de métodos y trade-offs: lse posgrados demuestra, mediante gráficos en la notebook, que la media móvil ofrece una medición más estable que el TTR simple, aunque reconoce que la lematización implica una pérdida de información específica a cambio de uniformidad semántica (00:30:53).

Experiencia de Marcelo Luna: Marcelo Luna comenta que, aunque no aplicó lematización formal, realizó análisis de frecuencia de palabras para detectar términos relevantes del dominio, lo cual lse posgrados valida como un paso válido dependiendo del tipo de texto (00:35:25).

Importancia en dominios específicos: lse posgrados destaca que, si bien la limpieza básica (minúsculas, acentos) es estándar, la lematización resulta particularmente valiosa en textos legales u oficiales, donde abundan las variaciones gramaticales de términos clave (00:38:20).

Documentación de mejoras: lse posgrados enfatiza que el objetivo central de la materia es que los estudiantes documenten las mejoras y cambios realizados en sus soluciones durante el proceso iterativo, lo cual será fundamental para las etapas finales del proyecto (00:39:55).

Formato de documentación: Gabi Tallarico consulta sobre estándares de formato, y lse posgrados sugiere mantener un estilo libre pero estructurado, similar a un artículo científico (Introducción, metodología, resultados), evitando plantillas rígidas (00:42:59).

Presentación del proyecto de Shimon Ben: Shimon Ben muestra su cuaderno, destacando el uso de Markdown para estructurar el contenido y explicando la evolución de su proyecto: pasar de un flujo de entrada dinámico de URLs a un conjunto de datos fijo y definido (00:45:33).

Alcance y metodología del proyecto: Shimon Ben detalla que su dataset consiste en 10 URLs de YouTube con 20 comentarios cada una, sumando 150 evaluaciones manuales (positivos, negativos, neutros) para validar el modelo "Robertito" (00:49:34).

Procesamiento y limpieza de datos: Shimon Ben describe la fase de construcción del dataset, que incluyó la limpieza de texto, normalización de minúsculas/mayúsculas y corrección de espacios para asegurar una entrada uniforme al modelo (00:50:57).

Desafíos de balanceo de clases: lse posgrados señala un desbalance en las etiquetas de los comentarios de Shimon Ben (especialmente en los neutros) y aconseja probar estrategias de sobremuestreo sintético o submuestreo de las clases mayoritarias para mejorar el entrenamiento (00:52:21).

Evaluación del modelo: Shimon Ben informa que el modelo "Robertito" alcanzó una precisión cercana a 0.5, superando la eficacia de los enfoques heurísticos probados anteriormente (00:54:59).

Estructura del dataset: Shimon Ben explica que su dataset final contiene 200 filas y 18 columnas, donde la mayor parte de las columnas son variables sintéticas generadas durante la exploración de datos (00:56:25).

Detección de duplicados: Shimon Ben y lse posgrados analizan la presencia de comentarios duplicados en el dataset, confirmando que la detección y eliminación de spam es una parte necesaria de la etapa de limpieza (00:57:35).

Análisis de distribución y balance de clases: Shimon Ben compartió los hallazgos de su análisis de comentarios, señalando dificultades para encontrar polaridad en videos infantiles y notando un desequilibrio de clases con una mayoría de comentarios positivos. lse posgrados indicó que este desequilibrio, especialmente la escasez de la clase minoritaria (neutros), podría sesgar el modelo, sugiriendo considerar si es necesario normalizar los datos para mejorar la precisión (00:59:00). Shimon Ben discutió si conviene reducir el porcentaje de comentarios neutros, los cuales a menudo contienen ironía o sarcasmo, concluyendo que desde una perspectiva de negocio es difícil definirlos, pero estadísticamente es un punto a evaluar (01:01:34).

Estrategias de visualización de datos: Shimon Ben mostró mapas de calor y gráficos de barras para categorizar temáticas. lse posgrados elogió la utilidad de los mapas de calor para identificar rápidamente la separación entre clases (01:02:41). Ante la dificultad de visualizar etiquetas largas, lse posgrados sugirió rotar los ejes de los gráficos (cambiando las barras verticales por horizontales) en lugar de abreviar los nombres de las etiquetas, lo cual fue aceptado para mejorar la presentación en el informe final (01:03:58).

Análisis de longitud de comentarios: Shimon Ben presentó un análisis indicando que los comentarios negativos tienden a ser más largos y dispersos, mientras que los neutros son más cortos y presentan una desviación estándar menor. lse posgrados confirmó que el "boxplot" permite visualizar claramente esta dispersión y recomendó rotar los gráficos para una mejor legibilidad, coincidiendo en que la visualización es adecuada (01:05:14).

Frecuencia de palabras y economía de tokens: Shimon Ben destacó el uso de gráficos para mostrar la frecuencia de palabras, notando que términos comunes como artículos ocupan gran parte de los recursos. lse posgrados y Shimon Ben discutieron la importancia de la "economía de tokens" para reducir costos, mencionando que en el futuro la gestión eficiente de los datos será clave para evitar gastos innecesarios, especialmente considerando que herramientas como Robertuito ya ofrecen métricas de rendimiento (01:06:26).

Análisis de confianza del modelo: Shimon Ben mostró la confianza del modelo por temática, utilizando el modelo Robertuito de Hugging Face. lse posgrados sugirió que el promedio de confianza no siempre es informativo, proponiendo analizar qué porcentaje de comentarios supera un umbral de confianza de 0.6. Esta aproximación resultó más útil para distinguir diferencias entre temáticas, permitiendo identificar mejor el desempeño real del modelo (01:09:00).

Cierre del proyecto de Shimon Ben: Shimon Ben mencionó problemas menores con la captura de datos, pero lse posgrados valoró positivamente el avance logrado, incluyendo la heurística aplicada y el análisis por categorías. Se acordó que el proyecto tiene suficientes hallazgos para pasar a la etapa de documentación y cierre, sirviendo como un ejemplo para otros estudiantes del curso (01:11:34).

Proyecto de Marcelo Luna (Ingesta y procesamiento de PDF): Marcelo Luna presentó su trabajo sobre un manual de reglas, enfocado en el procesamiento de PDFs no estructurados. Explicó que, tras las sugerencias recibidas, implementó mejoras en el preprocesamiento para optimizar la ingesta. Se identificó la necesidad de analizar la distribución de información en documentos disímiles, distinguiendo entre reglas puras y compendios de casos (01:31:58).

Riesgos de redundancia en sistemas RAG: lse posgrados y Marcelo Luna discutieron los peligros de la redundancia en documentos de jurisprudencia dentro de los sistemas de Recuperación Aumentada por Generación (RAG). Se advirtió que si el sistema recupera documentos similares con decisiones contradictorias, el modelo podría generar respuestas erróneas, por lo que se enfatizó la importancia de gestionar cuidadosamente el contenido legal (01:37:25).

Análisis de stopwords y tokenización: Marcelo Luna presentó métricas sobre la longitud de los documentos y el impacto de las "stopwords" (palabras de relleno), encontrando que aproximadamente el 50% del contenido de sus documentos consiste en conectores gramaticales sin valor semántico para el dominio. Se discutió la importancia de contabilizar los tokens necesarios para cada documento, considerando que esto impactará directamente en los costos de implementación futura (01:38:28).

Estrategias de optimización de tokens: Santiago Germino introdujo el concepto de hablar como "cavernícola" (usar frases simplificadas) para reducir el consumo de tokens sin perder comprensión del modelo. Shimon Ben y lse posgrados discutieron la realidad de los costos crecientes de los tokens, validando que eliminar conectores y gramática innecesaria es una estrategia viable de optimización que deben considerar (01:42:47).

Estrategias de fragmentación (Chunking): Marcelo Luna y lse posgrados analizaron la necesidad de fragmentar los documentos de manera diferenciada. lse posgrados advirtió que el "chunking" uniforme no es adecuado para este proyecto, ya que los libros de reglas requieren una separación distinta a los libros de casos. Se debatió si incluir el libro de casos en el RAG podría sesgar las respuestas, un tema que Marcelo Luna sigue explorando (01:47:57).

Implementación de recuperación híbrida: Marcelo Luna describió su enfoque para implementar un sistema de recuperación híbrida, combinando técnicas léxicas (para reglas rígidas) y semánticas (para interpretar la intención del usuario). Utilizó un "semáforo" para visualizar la frecuencia de términos relevantes en los documentos y verificar que la limpieza de datos no elimine información crucial para el dominio del problema (01:52:10).

Cierre de tutorías y próximos pasos: lse posgrados cerró la sesión invitando a aquellos estudiantes que aún no han avanzado con su Análisis Exploratorio de Datos (EDA) a contactarles por correo electrónico para coordinar sesiones de tutoría personalizadas, enfatizando que estas interacciones han sido muy efectivas para resolver problemas técnicos. Se dio paso a la explicación sobre las métricas de RAG (01:55:35).

Introducción a las métricas de RAG: lse posgrados explica que las métricas de Generación Aumentada por Recuperación (RAG, por sus siglas en inglés) se dividen en dos categorías principales: el proceso de recuperación (retrieval) y el proceso de generación por parte del modelo de lenguaje (LLM). Se define al sistema de recuperación como un examen a libro abierto, donde los fallos pueden ocurrir al no encontrar la página correcta o al interpretar incorrectamente la información del libro, destacando que es crucial evaluar cómo se preprocesan los documentos antes de que el LLM genere una respuesta (01:58:28).

Métricas de precisión y recall: La precisión mide la proporción de documentos relevantes entre los K documentos recuperados, siendo una métrica recomendada para aplicar esta semana mediante revisiones manuales (02:01:44). Por otro lado, el recall es descrito como una métrica más compleja que evalúa cuántos documentos relevantes existentes fueron efectivamente recuperados, lo cual requiere conocer el volumen total de información relevante disponible (02:03:12).

Rango recíproco medio (MRR): Se presenta el Rango Recíproco Medio (MRR, por sus siglas en inglés) como una métrica que evalúa en qué posición aparece el primer documento relevante para una pregunta específica. Si el primer documento aparece en la primera posición se otorga un valor de uno, pero se aplican penalizaciones severas si aparece en posiciones posteriores; lse posgrados sugiere que los estudiantes no se enfoquen en esta métrica por ahora a menos que tengan disponibilidad, debido a la carga de trabajo manual que conlleva (02:04:36).

Ganancia acumulada descontada normalizada (NDCG): lse posgrados menciona la métrica NDCG, la cual evalúa la relevancia graduada de los documentos, penaliza la posición y compara el resultado contra un orden ideal. Se especifica que es una métrica sofisticada y que los estudiantes no deben enfocarse en ella por el momento, recomendando priorizar la precisión (02:06:04).

Métrica de fidelidad y presentación del caso de estudio: La métrica de fidelidad (faithfulness) evalúa si cada afirmación en la respuesta generada puede ser verificada directamente en los documentos recuperados. Para ilustrar esto, lse posgrados introduce un caso de estudio basado en el Boletín Oficial, donde se utilizan fragmentos filtrados en lugar de la ingesta total de PDFs, facilitando la evaluación del sistema (02:07:28).

Comparación entre RAG ingenuo y optimizado: Se contrastan dos arquitecturas: un "RAG ingenuo" que utiliza fragmentación fija sin metadatos, y un enfoque optimizado que aplica preprocesamiento, extracción de entidades, metadatos y fragmentación recursiva (02:09:09). lse posgrados explica que el enfoque optimizado permite que la búsqueda no se limite solo al contenido del fragmento, sino que utilice metadatos como números de resolución y categorías, lo que resulta en respuestas más precisas (02:10:45).

Consideraciones de ejecución y costos: lse posgrados advierte sobre el costo de utilizar APIs de terceros, mencionando una experiencia personal donde un cargo de 5 dólares fue inesperado. Para evitar estos costos y problemas de consumo, el pipeline fue ejecutado localmente utilizando Ollama; se demostró que, aunque en ejemplos sencillos las diferencias de respuesta pueden ser mínimas, el método optimizado mejora la extracción de entidades específicas como números de DNI (02:13:52).

Asignación de tareas para la semana: Para esta semana, se solicita que las y los estudiantes apliquen estas métricas a sus proyectos para comparar el rendimiento actual con la arquitectura inicial utilizada al comienzo del curso. Aquellas personas trabajando en RAG deben intentar configurar el sistema para recuperar cinco documentos y calcular la precisión, mientras que quienes trabajan en clasificación deben utilizar matrices de confusión u otras métricas de mejora (02:18:32).

Contexto industrial y retroalimentación: Gabi Tallarico comenta que la práctica realizada ayuda a entender cómo aplicar las métricas discutidas en videos previos. lse posgrados señala que el uso de estas tecnologías ya es una solución industrial aplicada en sistemas de gestión y certificaciones ISO, donde los chatbots utilizan motores de recuperación para gestionar grandes volúmenes de procedimientos (02:21:34).

Planificación futura y sesiones de coaching: El objetivo principal es documentar la mejora de los proyectos, ya sea que esta exista o no, permitiendo transitar de un esquema de prueba de concepto a uno más operativo (02:24:32). lse posgrados ofrece disponibilidad durante el fin de semana para realizar sesiones de coaching con los grupos que lo soliciten vía correo electrónico, y adelanta que la próxima clase tratará métricas más complejas y el diseño del documento final (02:26:10).

Revisa las notas de Gemini para asegurarte de que sean precisas. Obtén sugerencias y descubre cómo Gemini toma notas

Cómo es la calidad de estas notas específicas? Responde una breve encuesta para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.

📖 Transcripción

20 may 2026

Taller de trabajo final (4/8) - d015b25 - Transcripción

00:00:00

Marcelo Luna: Pero, pero estás peleando un rato largo con eso, ¿no?
Gabi Tallarico: Claro.
Marcelo Luna: Hola, Cristian,
lse posgrados: Buen día.
Gabi Tallarico: ¿Cómo te va?
lse posgrados: Buen día, gente. ¿Cómo están?
Gabi Tallarico: Muy
Marcelo Luna: ¿cómo anda?
lse posgrados: Qué bueno.
Gabi Tallarico: bien.
Marcelo Luna: Eh, pero bueno, ahí está la experiencia.
lse posgrados: C
Marcelo Luna: Está buena la otra,
Gabi Tallarico: Y esa que haces cursal los lunes todos los martes de 3 horas
Marcelo Luna: ¿no? Los martes van cambiando las materias,
Gabi Tallarico: también. Claro,
Marcelo Luna: pero el primer bimestre cursé el lunes,
Gabi Tallarico: las profes.
Marcelo Luna: el segundo cursé el martes.
Gabi Tallarico: Ah, viste que no estaba tan mal con la gente.
Marcelo Luna: No,
Gabi Tallarico: ¿Qué habías dicho un
Marcelo Luna: no, sí, sí,
Gabi Tallarico: día?
Marcelo Luna: no está bastante bien. podía ser peor,
Gabi Tallarico: Claro,
Marcelo Luna: pero bueno, eh,
Gabi Tallarico: él está haciendo otra otra diplomatura también. Entonces, le estaba preguntando, ¿qué onda?
Marcelo Luna: estoy haciendo la división por computadora, ¿viste Cristian? Y le decía a Gabi recién,

00:00:54

Gabi Tallarico: Ok.
lse posgrados: Buen
Marcelo Luna: estoy cursando ahora aprendizaje profundo con Gerardo, eh, pero me tiró un ejercicio el TP que hay que entregar mañana. Ya lo tengo medio terminado. Hola, Shimón. Eh, tiene toda una parte de preparación de datos muy intensa que nosotros no vimos con esa profundidad en esta diplomatura y en la otra no tenés la materia. Entonces, a mí me agarró medio en el aire, así que estuve ahí peleando un poco con todo la parte de Leda para poder después hacer el ejercicio, ¿no?
Juan Pablo Rueda: Hola gente, ¿cómo
Shimon Ben: Hola,
Gabi Tallarico: ¿Qué tal?
lse posgrados: Claro.
Shimon Ben: ¿qué
Gabi Tallarico: ¿Qué Juan
Marcelo Luna: Hola, ¿cómo andan?
Shimon Ben: tal?
Gabi Tallarico: Pablo?
Diego Methol: Bien.
Marcelo Luna: Hola,
lse posgrados: Buenas.
Marcelo Luna: Ah.
lse posgrados: Bueno, eh estuve revisando los correos e algunos enviaron avances con otros los había visto la semana pasada.
Shimon Ben: No.
lse posgrados: Eh, los que los que tengan pendiente o que tengan ganas de que le revise un poco el edad, eh, mándenlo. tengo pendiente responder uno o dos correos, pero en general me me sorprendió porque para bien, digamos, eh porque en general se aplicó lo que vimos en clase todo de de encontrar descubrimientos a partir de Ledas que puedan ser usados en el diseño de la modelación o de alguna respuesta, el alguna solución, digamos, ¿no?

00:02:47

lse posgrados: En definitiva es lo que lo que buscábamos. Así que nada, objetivo cumplido, chicos.
Gabi Tallarico: Vamos muy bien.
lse posgrados: Buenísimo.
Gabi Tallarico: ¿Viste que fuimos mejorando?
lse posgrados: Y sí, sí, sí,
Marcelo Luna: Bueno,
lse posgrados: sí. O sea, el objetivo es ese. Igual tengo pendiente responder un par de correos, e, pero sí, sí, sí me gustó, me gustó mucho lo que vi. E yo yo digamos como siempre les digo, mi objetivo por ahí es hacerlo más pragmático, o sea, es buscar para qué hago esto, para qué hago aquello. E la clase de hoy hay dos cosas que vamos a ver. una que quedó pendiente la clase pasada,
Gabi Tallarico: Espera 2 minutos que muy
lse posgrados: que yo la la Ah,
Gabi Tallarico: temprano.
lse posgrados: perdón, yo yo le entré a yo entré con la clase.
Gabi Tallarico: Si vos venís con mucha energía al lado de nuestro,
lse posgrados: Ah, sí, sí.
Gabi Tallarico: pero somos poquitos, me parece todavía.
lse posgrados: De una, ¿cuántos somos?
Gabi Tallarico: Ah, no, mira, ocho.
lse posgrados: Ah,

00:03:53

Shimon Ben: Once
lse posgrados: no,
Gabi Tallarico: Ya pensé que era o menos.
lse posgrados: somos poquitos. Y y bueno, los que no hayan enviado, no hay problema. O sea, como les dije, me importa más el la entrega al final, pero sí me gustaría que antes de que lleguemos a la clase 7 me manden un un documento como para ir alineándolos.
Marcelo Luna: Sí.
lse posgrados: De nuevo, tengo pendiente algunas respuestas, eh, lo más probable que lo haga hoy, ahora cuando termine la clase, pero por lo general bien, digamos, o sea, tampoco hay mucho para hacer contexto, o sea, es lo que lo que hemos visto en la clase de visualización, contexto hay que darse maña con dónde encontrar la las variables numéricas, en la cantidad de palabras, en en los posibles token que o que podamos hacer, en la información que pueda a tener las palabras, etcétera, digamos,
Marcelo Luna: Hm.
lse posgrados: pero no hay mucho, muchísimo más, digamos. Entonces, hay que ponerse un poquito creativo cuando pero no hay que no hay que dejar de hacerlo. Sí. Eh, voy a aprovechar esta que está acá. ¿Alguno tiene alguna duda que queramos que quieran conversar antes que comience con una partecita teórica?

00:05:19

Shimon Ben: Tengo que revisar el mail que me mandaste y, o sea, lo leí muy para arriba, tengo que corregir cosas, pero bueno, iremos así por mail.
lse posgrados: Sí, sí, sí.
Marcelo Luna: Hm.
lse posgrados: E después cuando termine un poco lo
Shimon Ben: Ok.
lse posgrados: lo teórico capaz que conviene que eh tu caso si te animas porque está bueno los descubrimientos y el caso de Marce que
Marcelo Luna: Listo.
lse posgrados: también lo hablamos en la sesión anterior, eh, si lo pueden mostrar ratit los chicos y alguien hay alguien más que lo quiera mostrar porque sobre todo apuntando a al proceso de descubrimiento y al descubrimiento. Sí, no, de nuevo,
Shimon Ben: con lo que
lse posgrados: no el código, no,
Shimon Ben: quede.
lse posgrados: etcétera. Hasta ahí un poquito. Si no,
Shimon Ben: Sí,
lse posgrados: yo tengo el el colado.
Shimon Ben: sí, sí, sí. No,
Gabi Tallarico: Secretary No.
Shimon Ben: no, está bien, pero ya hoy hoy fue un día movido. Se me fue, pero sí puedo dar una idea de lo que lo que está
lse posgrados: Sí,
Shimon Ben: pasando en realidad.
lse posgrados: es abrir el colabar o menos lo lo que se hizo, digamos,

00:06:25

Shimon Ben: A ver, lo que más me me digamos lo que más me me generó es
lse posgrados: Ok.
Shimon Ben: que cómo este formato de repente se me lo puedo ir adaptando, no con esto, sino que tomar como, o sea, mi tarea sería acá, crear datasets que pueden ser, ¿no?, de YouTube y empezar a a ver otro tipo de de de representaciones gráficas.
Marcelo Luna: Ok.
lse posgrados: Claro.
Shimon Ben: Eh, yo como durante mucho tiempo estuve vinculado a las artes por la carrera que estudié, el tema de instalaciones y video de arte a través de digamos de poder montar números en una en una instalación, lo que fuere y ir modificándolo a partir de bueno, diferentes representaciones, ¿no? O sea, si vos de repente queréis poner la obra de Borges todo adentro y decir, "Mira, acá Borges habla muchas veces de esto o así o lo que sea y de
lse posgrados: Hm.
Shimon Ben: repente este representarlo en imagen y y espacio como instalación. Pero bueno, después hay que empezar a ver del análisis de datos qué produce imágenes interesantes y que da a una simple vista al usuario de la instalación. Eh, algo interesante que si, "Ah, entendí, está pasando esto. Mirad todas las veces que us esta palabra y todo lo que qué
lse posgrados: Hay hay toda una rama dentro del digamos, de la parte de análisis de datos, que es comunicar con datos, digamos,

00:07:53

Shimon Ben: Mhm.
lse posgrados: la la el database y y si vos tenés herramientas artísticas tuyas,
Shimon Ben: Mhm.
lse posgrados: ya digamos de tu formación, eh podés ir por ahí. Hay gente que se dedica solo a eso,
Shimon Ben: Claro.
lse posgrados: eh a crear gráficos picantes, ¿viste? Hacer a a digamos entre comillas curarlos, ¿no? Hacer una curación de qué es lo que querés comunicar,
Shimon Ben: Hm.
lse posgrados: cómo las paletas y y todo lo que hay atrás. digamos, eh, hay buenos buscar uno si les comparto eh se llama Creo que si no se los paso después hace él hace de cuestiones climáticas y la verdad que está bastante
Marcelo Luna: Hm.
lse posgrados: bueno,
Shimon Ben: H
lse posgrados: creo que se llamaba yo lo tengo en el Lo tengo en LinkedIn. Lo voy a buscar en el break. Así, así se los paso bien. Cedric acá está. Es lo paso en el chat, pero él usa él usa R porque por ahí R tiene una una librería que se llama G Plot que
Marcelo Luna: Hm.
lse posgrados: es bastante más amigable desde mi punto de vista que que las de Python. Ahí se lo paso.

00:09:18

lse posgrados: Cedric. él hace gráficos eh con cuestiones climáticas y es como un un buen referente de de esa parte. A ver, voy a compartir pantalla y de paso ya quedó. Ahí
Shimon Ben: Ok.
lse posgrados: estoy ahí está con un poquito de problema de conexión.
Marcelo Luna: Hopa !
lse posgrados: Aviso por si se corta, pero bueno. Este pibe que se llama Cedric, Cedric es da cursos a veces, ¿eh? y tiene tiene un para hacer los gráficos que a mí la verdad me encanta. Muchas cosas yo para la se las robo en mi trabajo y y nada, este estilo de cosas se las robo y después la trato de las trato de replicar. Eh, él tiene él todo esto lo hace en R. Eh,
Shimon Ben: Hm.
lse posgrados: la verdad comunica muy bien esto. Esto parece ser una pirámide de edad. esas pirámides, no me acuerdo cómo llamaban, pero donde uno pone las edades y y las cantidades. Y como ven, él el pibe la tiene clarísima con comunicar con datos. Eh, son gráficos de barra típicos. Estos serían dos gráficos de barra. Una barra sería hasta acá y la otra barra sería hasta acá, pero él quiere mostrar la diferencia.

00:10:49

lse posgrados: Entonces, no pone dos barras, pone la diferencia. Eso ya más avanzado, ¿viste? Pero en todo lo que es comunicación con datos, esto está buenísimo. Y digamos acá hay acá hay un mercado laboral también, ¿no? Revistas, qué s yo, páginas, etcétera. Y no no es tan complejo. Yo creo que lo más complejo en código acá es eh la cuestión artística, digamos, decir, de encontrar qué es lo que cómo, cómo lo va a comunicar, qué queres comunicar. Después el código se va cocinando más cona, digamos, pero eh ahí los invito a que vean el laburo de
Marcelo Luna: Hm.
lse posgrados: de Cedric. Los gráficos que hemos hecho nosotros son iniciales, pero por ahí para comunicar hay toda una toda una rama de eh ocultar. Bueno, son 10. Ya empecemos. Había hoy vamos a ver dos cosas. Por un lado, un primer pantallazo de las métricas que se pueden utilizar en un rack. Eh,
Marcelo Luna: H
lse posgrados: y en segunda instancia, algo que quedó pendiente de la clase anterior, de la de la riqueza léxica, que algunos sí avanzaron y otros quedó como quedó pendiente.

00:12:10

lse posgrados: Y en en el colap que les pasé había una parte teórica, pero que durante la exposición había generado confusión. Eh, por eso preparé como un colab y un una pequeña presentación de eso. Eh, ¿alguien tiene básicamente yo lo comienzo y ustedes me me frenan si si aplica o no aplica o cómo lo usaron, si no lo usaron? Me parece que Marcelo lo usó un poco. Eh, la riqueza léxica. Nosotros desde el punto de vista del de de esta métrica llamada TTR o MATR, que es una media móvil, eh digamos es una forma de medir o de relacionar la cantidad de tokens por las cantidades, digamos, de formas únicas que hay en ese token. Sí. eh un digamos cada palabra digamos tal como aparece escrita en el texto de las repeticiones eh digamos token cuando vos lo dividís hace eso, ¿no? corta, inicia en un lugar, corta en un lugar y toma todas las palabras y, incluso las repeticiones, aunque aunque esas repeticiones sean ambigüedades o por el estilo textual eh o o semántico con el cual se haya escrito y en los par los términos legales aparece un montón, eh no importa si se repitió n cantidad de veces esa palabra y no aporta, por decirlo de alguna forma las palabras repetidas por ahí aportar más información.

00:13:47

lse posgrados: Sí. En cambio, el type, digamos, que es otra forma de de analizarlo, eh, toma cada forma única de la palabra, ¿sí? Independientemente cuántas veces se repita. Hay como dos caminos, usando tokens o usando types. Por ejemplo, si tenemos esta esta frase o esta oración, el decreto aprueba el presupuesto, acá vamos a tener cinco tokens, pero en la palabra L va a aparecer dos veces. Sí. Ahora si no vamos por por el otro camino, eh, vamos a tener solo cuatro porque él, la palabra él se repite. Bueno, eh esta distensión es, digamos, una forma de medir la riqueza léxica en función de cuántos types únicos tengamos respecto al total de tokens. Sí, a digamos eh a mayor es mayor la cuanto más cercano a uno va a ser mayor la riqueza la riqueza léxica que tengamos, o sea, va a haber menos palabras que se repitan. ¿Sí? Es decir, si tenemos eh los types divididos, la cantidad de tokens, una relación de uno va a ser que ninguna palabra se repita. Si no tenemos la máxima riqueza. Uno cercano a 05 va a ser equilibrado. Y cuando está menor a 05 el usando esta métrica eh hay mucha repetición de texto.

00:15:26

lse posgrados: Sí. Y esto esto se puede usar para para análisis, digamos. Ahora, eh hay un sesgo en la longitud, porque veamos eh usando esta métrica, aquellos textos que sean más largos tienen más probabilidad de repetir palabra. Si tienen más probabilidad de repetir palabra, la métrica va a ir cayendo, ¿cierto? Entonces, para evitar eso es que existe la otra métrica que es en la media móvil. Eh, de alguna manera podríamos decir que es injusto, digamos, eh comparar dos textos de distintas cantidades de palabras con esa métrica. O sea, esa métrica no es e digamos no no es justa para o deberíamos estandarizar el texto para que pueda ser comparable, digamos, ¿no? Porque si no textos más largos tendrían es casi siempre eh esta métrica muy muy abajo. Entonces, en función de eso es que se creó la otra métrica que tomo una media móvil para que de alguna manera se neutralice ese efecto. ¿Quedó, quedó claro esta relación, chicos?
Shimon Ben: la relación más o menos. Sí encuentro la diferencia en cómo identificar, cómo reducir con times respecto a tokens. Eso entendí,
lse posgrados: Ah, claro.
Shimon Ben: pero claro,
lse posgrados: O sea, matizar, digamos, eso lo

00:17:08

Shimon Ben: no entiendo que cuando hiciste la pregunta que hay si entendemos la relación
lse posgrados: puso,
Shimon Ben: ahí me quedé pensando,
lse posgrados: digamos que cuando una por volv nombrarte a Borges,
Shimon Ben: ¿no?
lse posgrados: si digamos, si comparamos dos autores,
Shimon Ben: Sí.
lse posgrados: no sé, los Guachiturros versus Borges, seguramente Borges tenga una variedad léxica mayor y los guachurros cuando agarras digamos
Shimon Ben: Sí, sí.
lse posgrados: agarrar la las primeras 100 palabras de una poesía de Borges y las primeras 100 palabras de una canción de los guachiturros. Seguramente las primeras 100 palabras de una poesía de Borges tengan más variedad léxica porque no va a repetir palabras,
Shimon Ben: Está claro.
lse posgrados: pero los guachiturro va a ser tírate un qué,
Shimon Ben: Sí.
lse posgrados: tírate un paso, digamos, ¿no? Y lo va a repetir un montón de veces. Entonces, eh la variedad, hay una repetición masiva. Esa variedad e digamos en un texto de igual dimensiones los guachiturros van a tener una métrica más baja. Entonces, si vos tenés que hacer un diseño para extraer eh para extraer o recuperar texto usando el retrival, eh quizás no necesitaba una ventana muy grande de del Chank para extraer información de los respecto de la de Borge, por ejemplo.

00:18:38

lse posgrados: ¿Me
Shimon Ben: Sí, eso perfecto.
lse posgrados: entendés?
Shimon Ben: Lo que no entiendo es esa línea divisoria que como que si estuviese dividiendo types sobre tokens ahí por ahí no no me queda claro porque yo yo entendí que podías analizar de dos maneras. Mira, o sacas ciertas palabras que se repiten y o toquenizás y tomas cada palabra por su como un carácter o lo que sea la palabra que
lse posgrados: Claro,
Shimon Ben: como Ah,
lse posgrados: vos haces las dos cosas y las dividís y de esa
Shimon Ben: okay.
lse posgrados: métrica relacionas, ¿entendés?
Shimon Ben: Ah,
lse posgrados: Entonces, vos contás los types y contas tokens y los dividís. Entonces,
Shimon Ben: pues hace la diferencia.
lse posgrados: claro, entonces vos lo dividí al hacer la relación, digamos, el ratio te va a dar que si es un es porque no se repitió ninguna
Shimon Ben: H
lse posgrados: palabra. No, no,
Shimon Ben: okay.
lse posgrados: no hay palabra repetidas, digamos. En este caso, eh, creo que
Shimon Ben: O sea,
lse posgrados: estaba
Shimon Ben: el TTR lo que mide es la diferencia entre está Sí, ahí se ya está.

00:19:39

lse posgrados: claro,
Shimon Ben: Ok.
lse posgrados: es el ratio. Sí. Por ejemplo, acá está el si tenemos la la frase el decreto aprueba el
Shimon Ben: Ok.
lse posgrados: presupuesto. Sí. Eh, usando types teníamos cuatro y usando y contando tokens teníamos cinco. Tenemos cuatro types por cada cinco tokens.
Shimon Ben: Okay.
lse posgrados: O sea,
Shimon Ben: Mm.
lse posgrados: da 08.
Shimon Ben: Está
lse posgrados: Si fuesen cinco palabras distintas, acá se repite él.
Shimon Ben: perfecto.
lse posgrados: Si fuesen cinco, sería 5 sobre 5. Si fuesen todas las palabras distintas, si fuese 5 sobre 5 daría uno y así sucesivamente.
Shimon Ben: Okay.
lse posgrados: Básicamente es la relación entre palabras. Ahora, de nuevo, para hacer esto debería, digamos, para usar esta métrica debería tener textos de la misma dimensión porque si no un tweet tiene, por ejemplo, 50 palabras.
Shimon Ben: Hm.
lse posgrados: Un artículo científico ponente que tenga 500 palabras, pero un libro, una ley, etcétera, va a tener 50,000 palabras. Entonces, cuanto más largo se hace el texto, vos vas a tener, digamos, del lado del acá va a seguir incrementando esta

00:20:52

Shimon Ben: más ratio, más diferencia.
lse posgrados: parte de abajo del de la de la fórmula. Esto se va a ir aumentando y esta se va se va a ir manteniendo, digamos, por la cantidad de palabras totales que tengas únicas, ¿no? Las formas únicas. Entonces eso lo que va a hacer es ir haciendo que esta métrica baje. Entonces algo digamos una regla que tienen que tener para usar esta métrica. Ojo, estamos viendo una métrica para analizar los textos que tenemos dentro del documento como algo de exploración, ¿no? Va a haber la riqueza del vocabulario de los textos que estamos teniendo en en la exploración. E entonces de alguna forma deberían tener la misma dimensión, si no no va a poder ser comparable, pero para resolver esto es que se se generó el el la media móvil de esta métrica que cómo funciona. En lugar de calcular el TTR sobre todo el documento una vez, utiliza ventanas de tamaño fijo, por ejemplo, 50 tokens. Esa ventana se va desplazando palabra por palabra en el texto, ¿sí? Y va calculando el promedio. Entonces, lo primero que hace se define una un tamaño de ventana, por ejemplo, 50 tox. Calcula el TTR para esa ventana.

00:22:24

lse posgrados: Una vez que calcula el TTR para esa ventana, se mueve ventana siguiente desplazando una palabra. calcular, digamos, eh, vuelve a calcular y así al final va promediando. Lo que va haciendo es calculando una media móvil. Entonces, de esta forma es más comparable para texto de distintos tamaños, digamos, independientemente de la extensión. Ahora, ¿cómo cómo conectamos esto? Con algo que yo puse en el notebook, que es lematizar. Sí. Eh, como dijimos, digamos, eh un MT este media móvil bajo, digamos, la media móvil del DTR, eh no siempre indica pobreza real del del documento, en muchos casos refleja eh que hay formas flexionadas del mismo tema y pasa un montón en en en las sobre todo en los temas legales, eh donde por ejemplo tenés verbos conjugados Pero básicamente estás diciendo lo mismo, pero con distintas palabras que están muy relacionadas. Por ejemplo, en en la parte legal, decretó, decretará, decretaron, decretos y decreto. Hablan prácticamente de lo mismo, pero tenés más más riqueza léxica acá, ten mayor cantidad de palabras distintas, pero están diciendo lo mismo. Entonces, una forma de que de que el texto de estandarizar el texto para poder hacerlo es e lematizarlo.

00:24:05

lse posgrados: para lematizarlo hay librerías, digamos, ¿no? O sea, uno no no lo hace a mano. Hay como librería en español, en inglés, etcétera, y de alguna manera lo hacen y también forma parte de de una estrategia de limpieza para ver si laización ayuda a mejorar o no un una recuperación de de fragmento para que sea más más rápida eh o más certera. Y en cambio, si uno estas formas serían una sola palabra, decreto. ¿Sí? Entonces lo que hace laatización es encontrar todas las formas diferentes de la misma palabra o de lo que uno de lo que querría decir y transformarla en una sola palabra. De esa forma, eh el la media móvil de esta métrica que llama TTR, eh va a reflejar mejor la diversidad conceptual, digamos, ¿no? Y eh ahora, ¿cómo impacta esto en en en los racks, digamos, o en cualquier procedimiento de texto que estemos haciendo, digamos, no? Eh, obviamente tenemos que pensar que nuestros chans se van a convertir en vectores, ¿no? O en o en matrices. Entonces, lo que lo que buscamos nosotros es que esas matrices no tengan redundancia de datos si no perdemos información en el medio, digamos, ¿no?

00:25:40

lse posgrados: O sea, es decir, en la similitud coseno la la dispersión vectorial va a reducir la precisión de retriival, pero semánticamente van a ser documentos equivalentes. O sea, si tenemos uno que habla en futuro y otro que habla medio medio en pasado, quizás estamos hablando más o menos lo mismo, pero esta confusión si nosotros no la arreglamos podría traer eh generar en embedings o o matrices distintas en el espacio vectorial que cuando yo las busque las busque sean distintas. Sí. y pero quizás estén juntas o viceversa, hablen de lo mismo, pero las marque como distintas, ¿no? Y el otro caso es tener eh fragmentos que que no digamos que se que hablen de lo mismo. Entonces, si yo tengo en el espacio vectorial en los dos fragmentos llevados a matrices que eh hablan más o menos mismo, cuando yo apunte con el rag, al rack le va a costar distinguir entre uno y el otro, pero como yo le digo al rack, tráeme los k documentos para armar el el la respuesta, puede traer documento uno y documento dos o documento uno hay tres, pero el uno y el dos prácticamente hablan de lo mismo y me estoy perdiendo un un texto que me pueda aportar algo a la mejor a la respuesta. ¿Sí? Entonces, es ahí donde esta cuestión de la lematización forma parte de la, digamos, al menos de explorar la cuestión de la de la riqueza léxica para después posiblemente tomar una decisión si la matizamos o no.

00:27:29

lse posgrados: Quizás en algunos casos, en nuestros casos no, pero nuevo es un una manera más de las que hemos visto, digamos, de limpieza o eh de exploración de datos para ver si eso me permite a mí tomar una decisión respecto al diseño que estoy planteando, digamos. Eh, hay algunas reglas de decisión, sí. digamos matr, no sé cómo nombrarlo. El TTR, la media móvil del TTR mayor a 06 van a indicar un vocabulario más rico y diverso entre 04 y 06. Eh, tiene una variabilidad moderada y menor a 04. Bueno, ahí seguramente hay mucha redundancia. Eso sobre todo en en quizá más eh eh en en textos legales, esto puede esto puede aparecer más en textos legales. Y acá cuando cuando pasa esto sí eh lematizar podría llegar a ayudar un poco al RAC. No necesariamente no estoy diciendo que en sus trabajos lo hagan. Lo que sí eh exploren porque están las fórmulas en el colar que les pasé. exploren suic textos en función de esto para ver si tienen o no un alguna decisión de diseño que que tomar. Eh, bueno, el proceso de de lematizar es básicamente lo que explicamos es llevar es uniformizar distintas formas de o en en un contexto de mejor dicho distintas palabras.

00:29:20

lse posgrados: uniformizarlas en una en función de su contenido o su contexto eh eh léxico, digamos, ¿no? Es decir, todo lo que está en futuro, por ejemplo, lo pasamos a implementar. Eh, lo que está en pasado todo lo llevamos hasta ahí. Por suerte en librería que hacen eso no lo tenemos que hacer nosotros. Yo preparé una una notebook muy sencilla para que lo puedan ver en código. Eh, pero bueno, básicamente eso. Y por último le puse tres librerías que pueden probar, un poquito de código, eh, para ver cómo cómo lo cómo se hace, digamos, ¿no? La que más se usa es esta, que es spicy. Eh, bueno, cada uno tendrá sus ventajas, sus desventajas. Obviamente usan un modelo, ¿sí? Por abajo usan un modelo, eh, y creo que la la que está puesta en la notebook es esta. y utilicen eso es simplemente como para explorar un poco la la posible solución o el el esta exploración respecto de la riqueza léxica en en los fragmentos de texto. dudas. Creo que en la primera cuando di la clase de visualización no lo había explicado tan tan detallado, ¿verdad?

00:30:53

Gabi Tallarico: No,
lse posgrados: Ahora, ahora les quedó más
Gabi Tallarico: poner Ev.
lse posgrados: claro. Sí, digamos, es básicamente una forma más para una herramientita más como para probar y para visualizar a ver cómo cómo están los fragmentos, cuánto cuánto mejor dicho, sí, cuanto nuestros fragmentos de texto sean más certeros, el retrival va le va a apuntar mejor a los fragmentos y va a generar una mejor respuesta.
Gabi Tallarico: Sí, sí, es así.
lse posgrados: Entonces, eh básicamente es para eso, no no es para mucho más. O sea, quizás en la exploración te dice, "No, mira, a m no lo no tiene sentido que lo haga. No, no se hace." Eh, y acá está la notebook. Bueno, la notebook puse algunos textos. Sí, tiene dos secciones, una de para ver la la fórmula y el otro para ver cómo puede impactar la alematización en un fragmento de texto. Hay dos funciones, una para calcular el TTR y otra la media móvil. El que tiene la media móvil obviamente va a tener una ventana para ver qué ventana se trabaja. Sí. Y va calculando sobre sobre esa ventana. Y a acá hay una un gráfico de digamos usando este este fragmento que está acá, lo comparamos con un fragmento 15 veces más grande, obviamente repetido.

00:32:34

lse posgrados: Y lo que lo que se ve es que a medida que va aumentando, digamos, la media móvil va a quedar en un lugar porque obviamente va usando, pero eh si vamos aumentando la cantidad de de tokens añadidos y calculados en la en el ratio, esto va a ir cayendo. Es decir, cuando más grande el texto, la la TTR, lo que decíamos va a caer. Sí, lógicamente, porque las palabras se van y digamos nuestro bucular no es infinito, entonces las palabras se van a empezar a repetir. Como se van a empezar a repetir relacionado con la cantidad de de las que no se repinten, los types, digamos, esa ese índice va a empezar a caer. Como va a empezar a caer, nada, en algún momento va a llegar una asíntota, digamos, ¿no? Pero en cambio la media móvil, ¿no? Por eso lo que la idea de este gráfico es mostrarles que eh que este indicador de la media móvil usando ventana de texto, capaz que hay que fijar acá dependiendo de cada caso cuál va a ser la ventana a usar. Eh, siempre va a ser mejor utilizarlo. Ahora, ¿cuándo uso uno y cuándo uso el otro? Si yo tengo fragmentos que son comparables en tamaño como los chanks, podría usar este.

00:33:53

lse posgrados: Yo tengo fragmentos que tienen distintas cantidad de palabras y esa y esa, digamos separación es más grande, se decir tengo 50 versus 100 o 40 versus 70, eh esa comparación, digamos no es no es justa. Entonces ahí conviene ir a la de las medias móvil. Bueno, y acá le puse eh bueno, cómo matizar usando la librería. Sí, texto original, texto en Lemas creando un data frame, ¿sí? Y después comparando. Sí. Eh, usando la cómo baja si lo matizo. Obviamente las dos métricas van a bajar, una va a bajar más que la otra quizás, pero eh solamente para que entiendan que voy a perder, digamos, eh van a perder palabras, digamos, o sea, ahí digamos no van a perder palabras, sino van a uniformizar lo que quieren decir en las palabras. Sí. Eh, y acá también le puse un gráfico, eh, sí, como para que entiendan que eh cuando uno lo visualiza en en un espacio vectorial, las palabras parecidas están muy cercanas, ¿no? Entonces, yo quiero decir que cuando uno le matiza decretarán, decretó y decretamos, están todas más o menos en el mismo espacio.

00:35:25

lse posgrados: Entonces, lo que hacemos es le aplicamos una palabra problematizada, digamos, ¿no? Acá perdemos, perdemos. Hay algo que se pierde, ¿sí? Como en todo uniformización, hay algo que se pierde, pero a favor de otras cosas. Bueno, también eso es una una variable, ajustar y y tomar decisiones si sí o si no. Eh, bueno, obviamente si cuando uno lo loematiza van a disminuir, digamos, las cantidades de de dimensiones o de palabras únicas, ¿no? El objetivo, digamos, ¿no? Eh, así. Bueno, esta esta también está subida al sitio, digamos en la carpeta para que la exploren y vean si si hace falta que la apliquen o no en su en su caso. Mar, ¿vos lo habías aplicado, cierto?
Marcelo Luna: Yo no hice lematización en sí mismo. Lo que sí fue, lo que sí hice fue explorar un poco, por ejemplo, no si te acordabas, pero había hecho los gráficos de las palabras que más aparecen eh en todo el texto. Digo, va un poco por ese lado, pero no es exactamente la técnica para entender la relevancia semántica del documento que quería meter en el rack, ¿no?

00:36:56

Marcelo Luna: Entonces, digo, en el caso mío, lo que tenía era una lista de palabra distribuida por por veces que se repetían. Sí. Eh, pero para entender su relevancia y particularmente aparecían todas palabras del dominio, ¿no? bote, marca, virada, todas esas palabras eran las que las que se veían más repetidas, pero no hice directamente un análisis de este
lse posgrados: Okay.
Marcelo Luna: tipo.
lse posgrados: En los casos, entre comillas, legales, porque el tuyo es no no sé si es legal, pero tiene como cuestiones técnicas de de legislación,
Marcelo Luna: Exacto.
lse posgrados: digamos. Eh, ahí vos va vos quizás veas que a mí me pasa cuando yo procé el boletín oficial o
Marcelo Luna: Claro.
lse posgrados: los boletines oficiales que sí me me aparecían oportunidades de matizar por esto de regular, regularan,
Marcelo Luna: Claro,
lse posgrados: reguló, decretar, decretó. Entonces, eh por por ahí y también por una cuestión de que todo lo
Marcelo Luna: sí.
lse posgrados: que de de que cada cambio que uno haga para te ahorrar token después para para el proceso, ¿no? Y y también un ahorro económico quizás.
Marcelo Luna: Sí, en en el No,
lse posgrados: Entonces,
Marcelo Luna: perdón, te no te quería interrumpir.

00:38:20

lse posgrados: no digamos una variable a a y un y un aspecto a a tener en cuenta en el preproceso de del texto, porque usualmente el preproceso del texto es planchar todo el texto a minúsculas,
Marcelo Luna: H
lse posgrados: ¿sí? sacar acentos, eh espacios, tildes, etcétera, y tratar de llevar más todo un texto más plano. Pero hay cuestiones de la semántica o lo que quiere decir la palabra que quizás con las limpiezas tradicionales no no le apliquen tanto cambio.
Marcelo Luna: Hm.
lse posgrados: definitivamente la lematización o el análisis de la diversidad o riqueza
Marcelo Luna: H.
lse posgrados: léxica podría traer repercusiones en una solución, digamos, ¿no? Así es
Marcelo Luna: Yo lo que encontré en el trabajo mío es particularmente que el conjunto de reglas
lse posgrados: importante.
Marcelo Luna: justamente está redactado, pero no está redactado con esa estructura que decir, bueno, todas las reglas que tienen algún tipo de similitud están escritas de la misma manera. Eso para mí fue un hallazgo. Yo esperaba algo más normalizado, eh, digo, más cercano a lo que sería el formato de un texto legal, eh, pero particularmente lo que encontré es que que no porque no debe estar escrito por gente que sabe de leyes, sino gente que sabe de barcos, pero no necesariamente de leyes.

00:39:55

lse posgrados: Sí, sí. E yo yo creo que ahora es antes de pasar a la a la métrica, digamos, en nosotros en la a ver si tengo acá mano eh acá en esta en la organización habíamos visto clase por clase, ¿cierto?
Marcelo Luna: Hm.
lse posgrados: Había un Sí. Bueno, nosotros nos habíamos quedado medio en la clase dos. La clase tres fue tutoría, diseño de la solución. Eh, lo que me importa, digamos, en en en estas clases que estamos viendo es básicamente documentar mejora, o sea, que que en esto que que estamos diseñando para procesar texto sea, digamos la la solución que sea de clasificación en el caso de Shimon o en el o los RACs como la mayoría de los casos, eh, o o otras posibles soluciones. es la mejora, digamos, ¿no? Nosotros deberíamos llegar a la a la siguiente clase ya con eh y ya con mejoras probadas, digamos, ¿no? Entonces, por ahí ese ese es el objetivo, digamos, ¿no? en en hemos hablado bastante de la arquitectura en la clase anterior o en las sesiones grupales que hemos
Marcelo Luna: H
lse posgrados: tenido respecto de cómo diseño la ingesta, cómo voy guardando los datos, lo voy metiendo un dataset, etcétera.

00:41:31

lse posgrados: Eh, quizás lo que lo que quede pendiente para la clase que viene sea unir un poco de la construcción del modelo, el pipeline, que hemos visto el pipeline también. Pero lo que me interesa en esto antes de llegar ya digamos a la cuesta abajo de la materia es que documenten la mejora, digamos, ¿no? Es decir, que que estos cambios que se hicieron respecto de lo que tenían queden documentados en
Gabi Tallarico: Ah.
lse posgrados: un texto, ¿ok? en en si son si hicieron dos o tres cambios, que esos dos o tres cambios queden eh como resultado de digamos que de de de mejoras implementadas. Sí, eso eso es lo que me me lo el propósito de de alguna forma la materia es documentar la mejora, que en definitiva es después lo que lo que cualquier cliente no no no va a pedir, digamos, ¿no? Ahora vamos a a ver
Gabi Tallarico: Y para eso hay, digo,
lse posgrados: un
Gabi Tallarico: hay como algún formato estandarizado para para esa documentación o no sé,
lse posgrados: Mira,
Gabi Tallarico: qué sé yo,
lse posgrados: yo por ahí como soy del más del palo e yo soy más del nada técnico, digamos, para mí todo el reporte tiene que tener un resumen, justificación de problema, arquitectura, solución.

00:42:59

lse posgrados: O sea, es como que todo tiene que ir a introducción, eh metodología, resultados, digamos, ¿sí?
Gabi Tallarico: Bien.
lse posgrados: Eh, que es digamos eh más o menos lo que espero, digamos, ¿no? Cuando cuando ustedes hagan esto, o sea, cualquier documento científico tiene siempre esto, ¿viste?
Gabi Tallarico: Sí, sí,
lse posgrados: por la
Gabi Tallarico: está bien. No pensé que a lo mejor si yo ya tenía como una fórmula estandarizada de que siempre son en Excel,
lse posgrados: introducción.
Gabi Tallarico: siempre son en Word, siempre son de tal modo o paso a paso, qué sé yo.
lse posgrados: Ah,
Gabi Tallarico: el formato de de
lse posgrados: por ahí hay sistemas de gestión para digamos para documentar mejoras.
Gabi Tallarico: esto.
lse posgrados: Lo usamos ponerle en en Lean. Hay metodologías como Lean y otras que seguramente lo tienen. No, no me parece. Yo creo que hay que dejarlo un poquito más libre.
Gabi Tallarico: No, por ahí son un poco más difíciles,
lse posgrados: Claro,
Gabi Tallarico: como que llevan más tiempo.
lse posgrados: por eso hay que hay que dejarlo libre. Sí, sí, sí.

00:43:55

lse posgrados: Para mí hay que dejarlo libre.
Gabi Tallarico: Bien.
lse posgrados: Nosotros eh digamos en el documento de texto que ya tienen usted que perdón en el documento de texto que ya deberían empezar a escribir eh tenemos que poner un resumen. La justificación del problema, cómo plantean la solución, el edad, los descubrimientos del EDA, ¿sí? Eh, acá el desarrollo técnico sería más bien también un poco los resultados. Entonces, acá en el punto cinco sí podríamos ir documentando ya esto, ¿sí? Eh, y al final una evaluación final de resultado y conclusiones del de la de la del diseño final, digamos, ¿no? Pero tampoco nos no me gustaría que nos perdamos en esta interacción. a muchos a muchos eh casos particulares lo hemos hablado de que eh no no una vez que eramos encontramos una mejora, la documentamos, bueno, no nos enrosquemos más y vamos hacia ahí, digamos, pero sí el documento debería tener esto, digamos, hoy en día, se llamo digamos con total honestidad, escribir un documento no representa una dificultad porque no se lo pasa a un LM, más o menos un contexto, resultado y eh el LM va a ser el trabajo por nosotros, digamos, pero eh por ahí lo que lo que yo estoy buscando es que sean más sus propias palabras, decir, "Bueno, probé, se hicieron esta fase de iteración, ¿sí? En el desarrollo técnico,

00:45:33

lse posgrados: si teóo cuatro veces con esta, esta y esta estrategia, la definitiva es esta. Listo. Y a esa evalúo. Hm. Y ahí quedó documentada la mejora.
Gabi Tallarico: Okay, perfecto.
lse posgrados: Bien. E antes de que vaya a las métricas del rack, me gustaría porque ya para cerrar la fase de edas y y todo esto que que nos llevó un tiempito, pero a mí me parece que aporta mucho valor. Si Marce o o Shimón, querés compartir tu colab, tu colab está clarísimo, ¿eh? Tiene tiene los tiene los subtítulos, ¿viste? Itar los gráficos y lo y lo iteramos un ratito ahí. Mar segundo. Ahí lo prepar.
Manuel Babuglia: Está muteado.
Shimon Ben: Okay, ahí va. Perdón, un poco más grande se ve o ahí está.
lse posgrados: Se ve bien, amigo.
Shimon Ben: Perfecto. And un poco.
lse posgrados: M.
Shimon Ben: Bueno, acá están todas las importaciones. Básicamente fue adaptarme un poco a lo que proponés en el colab que me que me fuiste ordenando bastante.

00:47:07

Shimon Ben: Eh, no sé si querés que muestre más la fase tres que son
lse posgrados: A la izquierda, ahí tiene los puntitos,
Shimon Ben: Sí.
lse posgrados: a la otra izquierda. Ahí, ahí donde tiene como el menú hamburguesa que se llama toda a la izquierda del del
Shimon Ben: Este,
lse posgrados: colaboner drive
Shimon Ben: a la izquierda. Ah, perdón, perdón.
lse posgrados: para listo.
Shimon Ben: Sí, ahí va. Perfecto.
lse posgrados: Ahí ahí está como está bueno.
Shimon Ben: Y sí.
lse posgrados: Vieron que que se lo puede ir separando así como usando eso. Llama lenguaje markdown. una forma de ir estructurando el texto dentro del colabo. Está bueno para para como para ordenar un poquito el texto.
Shimon Ben: Okay. E, ¿te interesa que hable de la fase desde la fase uno
lse posgrados: Sí, danos un poquito de contexto mínimo y vamos al EDA,
Shimon Ben: o Bueno,
lse posgrados: digamos, a la fase tres.
Shimon Ben: básicamente el el proyecto consiste en capturar
lse posgrados: Yes.
Shimon Ben: eh comentarios de URLs de YouTube. Bueno, acá un segundito la pantalla directamente acá, así no.

00:48:23

Shimon Ben: Acáas empiezo acá es el modo demo. Ro que se ve. Bueno, acá empiezo a cargar la que empieza lo que es la ingesta.
lse posgrados: Ahí,
Shimon Ben: E cómo
lse posgrados: ahí anteriormente, ahí te corto. Anteriormente,
Shimon Ben: sí.
lse posgrados: Shimon lo que había hecho era desarrollado como un pipeline en donde uno podía una URL y una interfaz gradio hacía un como
Shimon Ben: H
lse posgrados: que era URL URL el resultado y entonces no teníamos dataset, digamos, ¿no? Entonces, la primer mejora fue decir, bueno, no fijo mi dataset en este en x cantidad de URL que tienen x cantidad de comentario. Entonces, ya podemos empezar a trabajar porque ya tenemos un dataset fijo. Entonces, eh a otras personas que están trabajando también un poco que los guía decir, "Bueno, armemos un dataset y trabajemos." Ese fue como el primer el primer insight, digamos, ¿no? Si bueno, fijo un dataset.
Shimon Ben: Claro,
lse posgrados: Ahora sí.
Shimon Ben: entiendo que es para una especie de entrenamiento de algo que no tenía un vocabulario previo, que era lineal y que vos le ponías una cosa, salíamos algo sin ningún tipo de entretenamiento.

00:49:34

lse posgrados: Claro.
Shimon Ben: Bueno, e bueno, podemos lo que hice es ponerle 10 este URLs. extraje acá extraje 20 comentarios de cada de cada URL, pero en definitiva lo que hice es hacer evaluaciones manuales de 150, o sea, de 15 comentarios de cada uno de los videos haciendo 150 comentarios en total que son las evaluaciones eh manuales, son las que verifiqué si el modelo que en este caso puse, que se llama Robertito, que se utilizaba previamente para tweets, eh si está funcionando bien o no. Y lo que vamos a clasificar es si los comentarios son positivos, negativos o neutros. Neutros como una especie de enigma, digamos, de si de si no no da claridad.
lse posgrados: Claro.
Shimon Ben: E bueno, acá se ejecutan. Bueno, acá eh digamos pusiste en modo de prueba demo.
lse posgrados: Todo esto sería la ingesta.
Shimon Ben: Eh,
lse posgrados: Sí está,
Shimon Ben: exacto.
lse posgrados: digamos, la ingesta está ya separada, fragmentada y tiene un resultado.
Shimon Ben: Cap.
lse posgrados: Eso iría dentro de lo que esperamos en el documento como arquitectura. La primer parte, ¿no? Ingestamos, ¿sí?

00:50:57

lse posgrados: creamos un creamos algo físico entre comillas a los cual después le pegamos y hacemos análisis, digamos, ¿no? O modelos o o
Shimon Ben: Bueno,
lse posgrados: entrenamos.
Shimon Ben: gracias por moderar este mi desorden. Eh, okay. Y bueno, acá viene la fase dos, la construcción de dataset, básicamente dondeemos algunas funciones para para ir clasificándolo. y empezamos a ver, digamos, cada cada cómo vamos a asignar cada columna, este, donde empiece empieza se empieza a hacer una especie de limpieza donde vemos que se repite, qué espacios están mal, qué tipo de ruido, qué tipo eh si hay una información que es poco clara, la va limpiando, espacios que hay demás, eh a veces hay palabras mal escritas, eh normaliza, por ejemplo, eh de repente tenés una oración en la cual hay palabras en minúscula y otras mayúscula y las va normalizando de manera que estén más ordenadas para que para cuando se entrene el modelo se entienda este de una manera más uniforme. E,
Marcelo Luna: He.
Shimon Ben: ¿qué más sigue acá? Bueno, acá eh el modelo está viendo un poco la evaluación manual que yo que yo estuve haciendo, este y empieza ahí un poco la comparación si es eficiente o no.

00:52:21

lse posgrados: O sea,
Shimon Ben: Eh,
lse posgrados: vos usaste un modelo de Face o de algú alg un servidor para evaluarlo y después vos le hiciste una etiqueta manual comprendiendo vos si
Shimon Ben: sí,
lse posgrados: era positivo, negativo, neutro, digamos.
Shimon Ben: cada comentario. Exacto.
lse posgrados: Exacto. ¿Cuántas fila de 150?
Shimon Ben: La tarea el 150 de cada URL, ¿no?
lse posgrados: Okay.
Shimon Ben: De cada video.
lse posgrados: Ahí hay algo importante porque y y cuando
Shimon Ben: Sí.
lse posgrados: cuando apareció tu caso,
Marcelo Luna: Ja.
lse posgrados: eh uno capaz que lo vieron ustedes como el balance de clases en en las primeras en las primeras clases, digamos, ¿no? Cuando uno cuando uno tiene un modelo de clasificación va a buscar, entre comillas tener que todas las clases tengan la misma cantidad de ocurrencias para que el modelo aprenda cuando entrene,
Shimon Ben: H
lse posgrados: aprenda de forma igualitaria, porque si de repente tenés 1000 observaciones de una clase y tenés dos observaciones de otra, bueno, obviamente el modelo va a estar un poco sesgado hacia la clase que tiene más observaciones. En este caso, eh tus neutros tienen casi la mitad de de, digamos, del que menos tiene de las otras clases que están más balanceadas, ¿no?

00:53:48

lse posgrados: O sea, la clase la clase negativa o o estoy estoy leyendo mal, creo que estoy leyendo mal, pero los neutros tienen menos precisión, pero no estoy seguro si los neutros tienen la misma proporción.
Shimon Ben: un poquito menos que los negativos.
lse posgrados: A eso me refiero.
Shimon Ben: un poquito menos, pero
lse posgrados: Eso también una forma de mejora es generar más neutro
Shimon Ben: Hm
lse posgrados: sintéticamente. Ponete se hace, se suele hacer o sub o en las muestras submuestrear aquellas clases
Shimon Ben: hm.
lse posgrados: mayoritarias, o sea, una es sintético hacia lo de la clase más minoritaria, esa es una estrategia. Y la otra estrategia es eh tener eliminar casos de las clases mayoritarias.
Shimon Ben: esos
lse posgrados: Son las dos. Ninguna ninguna, digamos la ganadora. A veces se prueba las dos en la que da mejor resultado, en la que va, digamos, ¿no? Pero seguí seguí. Te te quiero comentario como para
Shimon Ben: dices que no, vos dices que me conviene eh digamos equiparar y que quede más o menos eh mismo
lse posgrados: que capaz que te conviene probar probarla a ver como si ahí te da mejor,
Shimon Ben: porcentaje.

00:54:59

lse posgrados: digamos, probar.
Shimon Ben: Okay.
lse posgrados: Hm.
Shimon Ben: Eh, bien. Y también tomé esta recomendación que vos me decías de hacer eh una prueba urística viendo patrones por fuera del modelo para ver si de repente, digamos, era necesario el modelo o no. Y lo que me mostró que sí modelo, porque los resultados creo que daban un 0,30 de eficacia y mientras el modelo Robertito me daba cerca del 05 este de eficacia que sin ser demasiado eficiente, bueno, es más eficiente, digamos, bastante más eficiente que que el que digamos Sí,
lse posgrados: Cuando decí eficacia, precisión, ¿cierto? Es así.
Shimon Ben: sí, sí, precisión, Bien. A ver,
lse posgrados: Okay.
Shimon Ben: para que bueno, esto más informe, más informe. Bueno, hicimos acá ya no sé si me estoy olvidando algo o ya hablé de
lse posgrados: Ese el dataset. Muéstr un ratito porque ahí queda como claro que cómo viene tu dataset, digamos,
Shimon Ben: Ah, bueno, sí. Eh, hay algunos eh,
lse posgrados: ¿no?
Shimon Ben: digamos acá de 200 filas, tiene 200 filas y 18 columnas.

00:56:25

Shimon Ben: Eh, bueno, no me acuerdo. 18, digamos, este,
lse posgrados: Sí, de las cosas queando,
Shimon Ben: pero sí las 200 se
lse posgrados: o sea, cada comentario tiene, o sea, vos digamos tu dataset sería sería hasta la hasta la columna cuatro,
Shimon Ben: miden
lse posgrados: que es comentario limpio, por ejemplo. Después la demás es de la exploración, o sea, de la columna cinco en adelante son columnas sintéticas generadas para
Shimon Ben: hasta la 17.
lse posgrados: explorar, digamos,
Shimon Ben: Claro, está la 17. La 18 es la la evaluación manual que yo hago el check de todo este. Y bueno,
lse posgrados: No,
Shimon Ben: después el tipo de valores que da, digamos, porque da algunos valores que son enteros eh digamos por sí o por no flotantes y después este también hay un buleano. Sí. y y algunos que este no object, pero este nada más. Eh, bueno, esto no sé si me me quedo pendiendo algo que preguntaste recién
lse posgrados: No,
Shimon Ben: o no.
lse posgrados: no, nos vamos a la fase tres donde están los descubrimientos.
Shimon Ben: Bueno, después empez empezamos a ver algunos gráficos.

00:57:35

Shimon Ben: No sé si algo. Okay. Eh,
lse posgrados: Acá empieza lo rico.
Shimon Ben: sí. E ver si puedo ver un gráfico, se muestra un poco más. Eh, acá empieza a ver cuando empieza a anotar, por ejemplo, en la evaluación manual empieza a anotar algunas algunos datos repetidos. ver cómo lo
lse posgrados: D, o sea, O sea, lo que hiciste fue testear duplic o sea,
Shimon Ben: duplicado. Exactamente.
lse posgrados: puede pasar, por ejemplo,
Shimon Ben: Y
lse posgrados: puede pasar que un comentario se repita. A eso nos referimos con duplicado.
Shimon Ben: sí.
lse posgrados: Es decir, vino un usuario determinado, copió y pegó, copió y pegó, copió y pegó y spameó en en un video de YouTube. Eso puede pasar. Entonces es al menos así lo entendí yo. Eliminar duplicado o detectar esos duplicados tiene importancia en este caso,
Shimon Ben: Sí,
lse posgrados: digamos.
Shimon Ben: exacto. Bueno, este gráfico muestra un poco eso. Eh,
lse posgrados: No hay básicamente duplicado.
Shimon Ben: este en esta no hay muy poquito.

00:59:00

Shimon Ben: Eh, después este distribución matemática. Bueno, sí, todos tienen 20 comentarios. Yo solamente evaluo 15 de cada de cada video. Si este no tiene mucho
lse posgrados: Claro, ahí lo que hizo fue crear ahí,
Shimon Ben: ya,
lse posgrados: déjame que explique un poquito como como que se crearon
Shimon Ben: sí.
lse posgrados: eh categorías, digamos, se se categorizó cada comentario, si era eh o cada video si era tipo documental, conspiraciones y eh anda la tabla de arriba, por
Shimon Ben: Sí,
lse posgrados: favor.
Shimon Ben: me pasó que cuando vos hiciste la sugerencia de buscar videos infantiles, ninguno tiene comentarios eh para para buscar,
lse posgrados: Ah,
Shimon Ben: ¿viste?,
lse posgrados: mira.
Shimon Ben: alguna polaridad y no la pude encontrar, sinceramente. Eh, bueno, eh, la distribución acá lo que da, bueno, lo vo mostrar un gráfico, acá me lo muestra en una tabla. que que en promedio, bueno, tienen la cantidad, por ejemplo, de de 150 95 son positivos, 68 negativos y 37 neutros. A ver si tengo algún gráfico para mostrarlo. Cachito. Bueno, ahí se ve más fácil,

01:00:21

lse posgrados: O sea,
Shimon Ben: ¿no?
lse posgrados: ese sería el balance de clases, digamos.
Shimon Ben: Exactamente.
lse posgrados: Okay. En cualquier problema de clasificación, el balance de clases es el primer análisis que hay que hacer porque es
Shimon Ben: Mhm.
lse posgrados: es cómo vos estás pesando los distintos problemas que querés separar, digamos. Si vos tenés obviamente más comentarios positivos, muchísimos más respecto de la clase mentoritaria, que es en este caso el neutro, obviamente tu modelo, tu análisis va a estar más sesgado hacia ahí, digamos. Entonces,
Shimon Ben: Sí.
lse posgrados: esto de eh uniformizarlo es como
Shimon Ben: Ok.
lse posgrados: algo eh que podría llegar a mejorar, digamos, ¿no? Eh, sobre todo aquella en la clase minoritaria, digamos, ¿no? Si vos tenés problema en detectar la clase minoritaria, que en este caso es neutro, es porque está de alguna forma haciendo eh overfeitting hacia lo positivo, digamos, porque tiene mucho caso. Entonces ahí hay que plantearse, ¿no? Para allá, pero al menos plantearse esa pregunta. Dec, bueno, la métrica respecto a los neutro es justa al respecto de los positivos.

01:01:34

lse posgrados: Eso
Shimon Ben: Está bien. A mí me parecía que, por ejemplo,
lse posgrados: es.
Shimon Ben: los neutros son todos aquellos que no los entendían. Entonces, por ahí que crezca ese porcentaje. En realidad, yo como digo, bueno, por ahí la tendencia es que se trate de chicar ese porcentaje porque si no lo puedes interpretar,
lse posgrados: Claro.
Shimon Ben: difícilmente puedas dar una respuesta a la gente, decir, mira, neutro, no sé qué hay acá. Pero no sé si me conviene porque yo por lo
lse posgrados: Es verdad. Sí, sí, sí. Claro, entend es un tema de negocio,
Shimon Ben: que
lse posgrados: digamos, es de lo que vos del propósito del proyecto. Yo por ahí te hablo desde lo estadístico, capaz que no
Shimon Ben: Okay.
lse posgrados: aplica.
Shimon Ben: Eh, ahí es como justo el color dio un gris básicamente porque no puedo decir que hay adentro digamos porque hay ironía,
lse posgrados: Sí.
Shimon Ben: hay sarcasmo, hay humor, hay de todo, pero digamos no se puede definir ni por positivo ni negativo. Así que este por eso siempre no sé si me conviene quizás hacer una tendera a a que se vaya deduciendo ese porcentaje, si sumándole, por ejemplo, más comentarios si lo hiciese.

01:02:41

lse posgrados: Sí, sí, está claro.
Shimon Ben: Okay. Eh, em, a ver, ¿qué es? Entiendo por temática. Ah, bueno, está. Eh, cada temática también tiene, independientemente más allá de los 150 comentarios, cada temática tiene su su valoración. Acá, por ejemplo, eh, en conspiraciones muestra document, bueno, h negativo nu, neutro 3, positivo 8. Bueno, para ver, quiero ver si tengo un gráfico que le pueda mostrar mejor, sea en un mapa de calor.
lse posgrados: Está buení.
Shimon Ben: Claro. O en este de barras que también se ve más bastante claro de A ver si puedo ver un poquito más grande.
lse posgrados: Sí, a mí me parece el acá el hit map me parece fantástico, digamos, ¿no? El hit map, el mapa de calor ese que está a la izquierda, ¿no?
Shimon Ben: Sí.
lse posgrados: Claramente los lo eh la categoría famosos públicos, famoso fútbol de publicidad, eh son todos comentarios positivos. O sea, de nuevo,
Shimon Ben: Sí.
lse posgrados: lo que buscamos es en una simple mirada ver cómo se separan las cosas, digamos, cómo se paran las aguas. Entonces, cuando cuando vi esto dije, "Buenísimo, ya está." O sea,

01:03:58

lse posgrados: esto ya de por sí comunica y sacas insight de estos. Ahora, y como te puse en el comentario por ahí,
Shimon Ben: Hm.
lse posgrados: la única la el único digamos observación es que si en en por ejemplo vos tenés las palab digamos cada etiqueta en horizontal ahí. Sí. Entonces, eh quizás te con toda estrategia o en el gráfico de la derecha o reducís el el nombre por confiración documental a CD, compilación documental o lo que sea para digamos hacer alguna forma de reducirla
Shimon Ben: Mhm.
lse posgrados: o lo rotas, digamos, si no lo quieres reducir rotalo, o sea, pon lo que está en X, ponlo en I y lo que está en Y, ponlo en X.
Shimon Ben: Ah, okay,
lse posgrados: las barra en vez de ser verticales van a ser horizontales y en vez de ponerlo al lado,
Shimon Ben: okay,
lse posgrados: como lo tenía acá, ponerlo abajo. Entonces ahí ya entendé,
Shimon Ben: Okay.
lse posgrados: ya yo creo que la más que eh hacer abreviación de la de la etiqueta, ahora se me ocurre, rotalo. Si lo rotá,
Shimon Ben: Camb está bien cambi que
lse posgrados: lo rotáis, ya va a quedar digamos para el informe.

01:05:14

Shimon Ben: cambi los ejes. Bueno, eh esta es la apreciación de cada de cada temática, digamos, en cada URL. Eh, bueno, acá el análisis de longitud de comentarios lo que explica y voy a ver si encuentro el gráfico, es que los vamos a ver si puedo chequear un poco más esto, que los que tienen comentarios más negativos, voy a ver si lo puedo achegar porque si no no se aprecia, suelen suelen dejar más mayor cantidad de caracteres, comentarios más largos, un poco más chicos y los que, bueno, los que tienen una apreciación positiva. Este, las respuestas son bastante más cortas, ¿eh?
lse posgrados: CL ahí se ve. Claro.
Shimon Ben: Medio chiquito.
lse posgrados: Acuérdate que el boxplot lo que te habla dos cosas
Shimon Ben: ¿En dónde están?
lse posgrados: de Claro. Y dónde está concentrado,
Shimon Ben: Sí.
lse posgrados: ¿no? Fíjate que los negativos son más dispersos, o sea, tiene una caja más grande. Los neutros definitivamente tienen la caja más chiquita, tienen la desviación estándar más chiquita y los positivos están ahí entre
Shimon Ben: Mm.
lse posgrados: entre uno y otro, digamos, ¿no? Entre los negos, o sea, vos tenés dos partes.

01:06:26

lse posgrados: Los negativos, por un lado,
Shimon Ben: Sí.
lse posgrados: dispersión grande más cantidad de palabra, el otro extremo, los neutros, poca cantidad de palabra y dispersión chica. Y en el medio te los positivos,
Shimon Ben: Sí. Sí. Más de 20 palabras.
lse posgrados: digamos.
Shimon Ben: Otro menos de 10 y el otro entre sería entre 10 y 20, 15 por ahí. Okay.
lse posgrados: Buenísimo.
Shimon Ben: No sé si se llega a ver bien este. Bueno, tengo que retomar un poco el el
lse posgrados: Para mí quedó bien de nuevo el boxplot,
Shimon Ben: tamaño.
lse posgrados: el que tiene los nombres de las categorías. Rotalo. Lo mismo lo rotas.
Shimon Ben: Claro.
lse posgrados: Y listo. En vez de tener las cajitas hacia arriba, tener hacia el costado.
Shimon Ben: Bien. Eh,
lse posgrados: Perfecto.
Shimon Ben: esto y ah bueno, este grafico también está muy bueno porque te muestra con qué frecuencia se utilizan las palabras y las que más llaman la atención y eso también visualmente es muy muy impresionante eh por el caso este que decíamos recién con losos y Este,

01:07:40

lse posgrados: Gracias.
Shimon Ben: así que también, por ejemplo,
lse posgrados: Carga.
Shimon Ben: en el caso que la palabra más repetida fuese un artículo, quizás todo esto empieza a cobrar sentido de eso de ir reduciéndolo.
lse posgrados: Mm.
Shimon Ben: Y el artículo el se utiliza es la palabra más grande, podría reducir mucho el coste de los tokens o lo que fue.
lse posgrados: Claro.
Shimon Ben: este o bueno,
lse posgrados: China.
Shimon Ben: destacarlo en el caso de cómo y
lse posgrados: ¿Por qué China? ¿Sabes por qué aparece China entrarás?
Shimon Ben: mira, yo puse un video de bueno, hay geopolítica, eh hay ya está Trump en otro. Eh, traté de buscarlo más controversial para ver que los comentarios sean eh,
lse posgrados: Okay.
Shimon Ben: viste, lo más polarizados posibles. Eh, bueno, este es bastante claro. Todo por sentimiento. Okay. Ah, bueno, eh, acá detalla este el con respecto al otro gráfico, ¿cuál eh cuánto usó cada palabra en el caso de los positivos, negativos y neutros? Y está bueno ver, por ejemplo, que no sé, gracias más de 60 veces. Eso que es una palabra que perfectamente se podría tratar de buscar de de reducir a uno en vez de que aparezca más de 40 veces en el caso

01:09:00

lse posgrados: Claro, claro.
Shimon Ben: de que reducir tokens, ¿no? En la economía de los tokens, que es lo que entiendo que es lo que se viene. E an confianza de modelo. Bueno,
lse posgrados: Mhm.
Shimon Ben: acá es donde de repente eh eh a ver hablamos dijiste de eficacia, ¿no? Eh, otra palabra utilizaste de
lse posgrados: Precisión. Precisión.
Shimon Ben: precisión. Exacto. Y bueno,
lse posgrados: Acresí
Shimon Ben: acá el modelo Robertuito, que es el que utilicé de Hing Face, bueno, eh, tiene, bueno, en cada caso para cada video te lo muestra detallado. Yo lo que te decía anteriormente era en la síntesis entre todos que bueno, tenía una respuesta de de 05 C respecto al la heurística que me había bastante más bajo.
lse posgrados: Claro.
Shimon Ben: E y creo que a ver si ya termino esto, a ver si o tengo un acá estáengo de repente un gráfico que pueda mostrar mejor. Eh, acá te puestra la confianza de modelo por temática, que eso está bueno. Este, mira, bueno, en música fue más claro por lo pronto,
lse posgrados: Hay algunas que sea que o andan todas más o menos iguales,

01:10:21

Shimon Ben: no estamos iguales, pero bueno, qué sé yo. Es verdad que que música quizás tenga menos, a menos que ponga algún tipo de de video que que sea controversial, en general las personas que hacen esa búsqueda van a estar como de acuerdo, a menos que sea una noticia,
lse posgrados: Claro,
Shimon Ben: que ahí sí empieza la controversia de repente. Bueno, el porcentaje puede confesar por
lse posgrados: donde creo que sí se despegan las clases en esa de porcentaje de comentarios con
Shimon Ben: temática.
lse posgrados: confianza mayor a 06 porque ahí me parece que porque en confianza promedio vos los ponés todos la misma bolsa,
Shimon Ben: Sí,
lse posgrados: lo promedias,
Shimon Ben: sí.
lse posgrados: pero digamos en me pareció interesante ese cuántos de todos esos comentarios o filas por categoría eh tienen una una mejor confianza porque digamos vos querés evaluar tu modelo y el promedio no te no te puede decir, no te está diciendo,
Shimon Ben: Mhm.
lse posgrados: hay una distinta de la otra, o sea, no me está clasificando. eh mejor música respecto de economía. Sí. Ahora, eso en el promedio. Ahora, si te vas a aquellos porcentajes con mayor a 06, como está en el gráfico de la de la derecha, ahí me parece que sí hay un despegue,

01:11:34

Shimon Ben: Sí.
lse posgrados: ¿no? Donde a música, donde música tenés pocos, o sea, tenés pocos comentarios o poco porcentaje de comentarios con una confianza mayor al 06, digamos. Eso también es un descubrimiento. digo, intentamos ir por la confianza por medio, no nos comunicó nada, hurgaste un poquito más y ahí podés ver un poco más cómo se distinguen las clases.
Shimon Ben: Claro, claro. Con respecto al modelo. Está bien. E casos problemáticos.
lse posgrados: Hai
Shimon Ben: Bueno, acá creo que es donde más despolijo estuve porque creo que me apareció algún dato, pero ya te quería mandar el mail porque me tenía que ir. Eh, creo que apareció algún dato de más porque creo que me me capturó 206 datos en vez de 200 y ahí bueno, como que no termine de evaluar bien en este caso. Es total 206 no sé qué es lo que hizo acá que tengo que revisar. Eh, a ver, acá hay algo que no me termino de cerrar y que pero que quería mandarte el mail para para ir viendo.
lse posgrados: Bien, pero ya ya tenés insight, digamos, ¿no?
Shimon Ben: Hm.
lse posgrados: Esto de haber uno el el haber probado la heurística, ¿listo?

01:12:59

lse posgrados: Y segundo, haber probado por clase, por categoría, ya es una exploración, digamos. Así que yo creo que ya es momento de más o menos cerrarlo y empezar a documentarlo, digamos, ¿no? Eh, sí, sí, sí.
Shimon Ben: Okay.
lse posgrados: Pasarlo en limpio, pasarlo en limpio y ya queda medio medio cerrado. E la verdad estuvo bueno el avance, Simón.
Shimon Ben: Sí, te agradezco mucho por toda la ayuda porque me ordenó bastante a pesar de que ahora para no se puede transmitir con claridad a los compañeros, pero bueno,
lse posgrados: Y por ahí yo creo que lo que hacía falta más o menos que es eh una guía,
Shimon Ben: este
lse posgrados: digamos, lleva por ahí y ya se acomoda, digamos, a la mayoría, ¿no? E así que no, buenísimo,
Shimon Ben: muy agradecido. Bueno,
lse posgrados: estamos rebién.
Shimon Ben: gracias por toda la
lse posgrados: No, no, no estamos ya estamos, o sea, lo lo quería que lo mostrés en clase para que porque sirve para para aquellos eh
Shimon Ben: ayuda.
lse posgrados: compañeros que están avanzando, que que están empezando. Eh, o nada, a mí me pareció fantástico, digamos, tu ejemplo.

01:14:10

lse posgrados: ¿Quieren que hagamos un un recrédito y después seguimos? Así tomo agua también. que un poco con con tema.
Shimon Ben: Muchas gracias.
lse posgrados: Sí. Bueno,
Gabi Tallarico: Ok.
lse posgrados: volvemos a la no tomemos 15 redondeemos hasta las y
Shimon Ben: Okay,
lse posgrados: media, así ya quedan un par de minutos más. Volvemos media.
Shimon Ben: okay.
lse posgrados: Okay.
Shimon Ben: Bueno, ya resiste el mensaje, Gabi. Entonces,
lse posgrados: Sí,
Gabi Tallarico: Hoy no hablé todavía. Vengo super concentrada.
lse posgrados: pero te la
Shimon Ben: tener mail docente, así que hay mucha
Gabi Tallarico: No, no, no. Hoy no dije nada.
lse posgrados: mente.
Gabi Tallarico: Estoy en silencio.
Shimon Ben: presión.
Gabi Tallarico: Sí, sí. Es más, digo, está buenísimo. Mi Simón lo que decía,
Shimon Ben: Bueno,
Gabi Tallarico: preste atención.
Shimon Ben: nos vamos entonces.
lse posgrados: Bueno, ahí volvemos al media. Yeah.
Juan Pablo Rueda: profe.
lse posgrados: Gracias,

01:31:58

Shimon Ben: No.
lse posgrados: Juan Marce, tenés tus minutos de fama. Eh, me parece hay dos casos est usa estos dos casos testigos
Marcelo Luna: O
lse posgrados: porque uno es de clasificación, puede aportar bastante. Tiene cuestiones que el dataset eh puede llegar a cambiar, ¿sí? Porque le metemos otras URL, tener otros comentarios. Entonces, y por otro lado, algo más fijo que es el el trabajo de Marcelo, que busca eh digo, eh el el manual de reglas de veleros no va a cambiar o no va a cambiar mucho, entonces la solución que vos hagas no va a iterar tantísimo,
Marcelo Luna: Claro.
lse posgrados: si no se puede ir mejorando, pero los dataset no van a ir cambiando. Son como dos casos diferentes que me que me que quería que quería que comentemos.
Marcelo Luna: Sí. Ahí. Dale, dale,
lse posgrados: compart y y vamos viendo los
Marcelo Luna: dale. Eh,
lse posgrados: hallazgos.
Marcelo Luna: les comparto, eh, ahí estamos. Esp un segundo. Ah, ver si todavía no. Esto deberían ver. Ahí está. No,
lse posgrados: Se ve.
Marcelo Luna: bueno, para que cerramos acá. Yo lo que hice fue e en realidad mi trabajo no está todo en una notebook, sino más bien tienen formato de aplicación.

01:33:35

Marcelo Luna: Eh, pero lo que sí hice fueron notebooks para ir probando cosas y para trabajar un poco sobre todo sobre la ingesta, porque originalmente en mi caso lo que había hecho era bueno, no más ahí están todos los PDF. Eh, trabajaba con los PDF medio crudo, eh, probablemente por ignorancia de muchos conceptos. Sí. Eh, y si bien los resultados no digo fueron bastante bastante mejor de lo que de lo que entiendo ahora que podrían haber sido, eh, sí tomé un poco alguno de los comentarios que me fuiste haciendo y y traté un poco de mejorar, así que digo, lo que hice fue sacar algunas métricas que son las que te compartía vos, Cristian, la semana pasada, pero también trabajar trabajar sobre el preprocesamiento del del de los documentos para obtener lo que después les muestro pretendería ser lo que finalmente hay que ingestar para tener un mejor una solución un poco mejor. Eh, pero bueno, fui haciendo, hice varias cosas, el código no importa mucho, pero una de las primeras cosas que hice medio obvia, pero fue bueno, tratar de entender un poco la la eh la longitud de de de cada documento y dónde se concentran eh los se concentra la información. Son documentos que por ahí tienen muchas páginas, no sé si muchas, pero tienen algunas páginas que están en blanco eh o o páginamente un texto aclaratorio o ese tipo de cuestiones.

01:35:33

Marcelo Luna: Eh, y entonces ahí fui tratando de entender un poco cómo estaba distribuida la información. eh son documentos muy disímiles en general eh y están escritos de manera muy diferente. Eso también este me me llevó a tratar de entender un poquito más que qué era lo que había. E nada, hay algunos gráficos de barra, pero eh por ejemplo eh eh esto parece muy básico, pero para que se entienda, este del medio es el conjunto de reglas, eh, y este medio naranjita es como un como un documento adicional que complementa las reglas para un tipo de competencia específicamente, que es el que el que voy a enfocar. Eh, este, que es el que tiene más páginas, es el e es es como un compendio de casos en donde se muestra un caso específico y cómo aplican las reglas. Él es de lo que sería como una especie de ground de de ground truth para mí. Yo tomé casos de ahí como casos de referencia para después probar cómo cómo
lse posgrados: Es la jurisprudencia,
Marcelo Luna: funcionan exactamente algo así.
lse posgrados: digamos.
Marcelo Luna: Sí. Eh, sigue habiendo una gran parte del ejercicio de entender qué reglas aplican en un escenario que que queda medio sujeta a una interpretación. Bueno, eh eh hay mucho por explorar ahí todavía, pero eh pero bueno, por eso por eso están por eso tan voluminoso este, ¿no?

01:37:25

lse posgrados: Claro,
Marcelo Luna: Porque las reglas están acá.
lse posgrados: no hay ahí hay en ese lo que quizás eh esto que hemos hablado del de
Marcelo Luna: Acá sí.
lse posgrados: lo de lo léxico y semántico, etcétera, que no existan redundancias, pues ten dos casos muy parecidos,
Marcelo Luna: Ah,
lse posgrados: con dos decisiones muy opuestas.
Marcelo Luna: correcto.
lse posgrados: El retrae cuando apunte Claro.
Marcelo Luna: No vas a saber qué traer.
lse posgrados: Exacto. Te puede traer el documento uno con una decisión, el documento dos con otra decisión y el y bueno,
Marcelo Luna: Correcto.
lse posgrados: y el LLM se va a alimentar de esos dos documentos para generar una respuesta y puede generar una
Marcelo Luna: Correcto.
lse posgrados: contradicción, ¿no? Entonces ahí en lo que sigue la clase voy a voy a comentar sobre las métricas LM,
Marcelo Luna: Sí, sí.
lse posgrados: perdón,
Marcelo Luna: M del
lse posgrados: las métricas del rag y ahí lo vamos a discutir un poquito.
Marcelo Luna: R. Bueno, eh, bueno, después hice algunas métricas también que son medio medio básicas. Y qué cantidad de caracteres había e en en lugar de por página,
lse posgrados: H
Marcelo Luna: porque era se me iba a ser enorme el gráfico.

01:38:28

Marcelo Luna: Lo que hice fue agrupar en grupos de a 10 páginas. No sé si me aportó demasiado eh el el la gráfica esta en particular, eh, pero la intención era entender qué cantidad de caracteres había antes de pasar por la limpieza y después de pasar por la limpieza del de lo básico del del PDF. No, no, la verdad que no cambió mucho, no hay cambio muy sensible. Hasta acá no, a mí no no me no en particular no.
lse posgrados: Nada.
Marcelo Luna: Eh, pero por ahí las cosas las cosas más sustanciosas las fui
lse posgrados: Eso de ser por lo que está en inglés,
Marcelo Luna: encontrando como
lse posgrados: porque quizás las en inglés tener menos pérdida,
Marcelo Luna: como
lse posgrados: digamos,
Marcelo Luna: Sí, pu puede ser. La verdad es que habría que estudiarlo ahí un poco,
lse posgrados: No.
Marcelo Luna: pero a donde empecé a encontrar algunas cosas, es decir, cuando cuando me puse con el el tema de las stops, por ejemplo, que vos las habías mencionado. Y acá sí encontré un hallazgo interesante, no, no sé si es un hallazgo, pero encontré que cada documento tiene casi un 50% de stopws, o sea,
lse posgrados: Claro.
Marcelo Luna: que que hay un montón de palabras que que no aportan al dominio del problema específicamente,

01:39:45

lse posgrados: Mhm.
Marcelo Luna: sino que son conectores, eh es gramática, digo, básicamente. E y tomé una lista de de stops en inglés que está por acá definida. digo, cada bueno, son todo, digo, no hay no hay ninguna eh no hay ninguna palabra propia del dominio, sino que son todas palabras de del
lse posgrados: O capaz que capaz que la conclusión es que el dominio tenga pocas palabras también
Marcelo Luna: del Puede
lse posgrados: tenga variedad de palabras,
Marcelo Luna: ser,
lse posgrados: digamos,
Marcelo Luna: puede ser. ahí. Bueno, después tengo otra otra otro análisis medio parecido, pero esto sí me resultó interesante porque digo, "Che, casi la mitad del documento, eh, no, digo, casi la mitad de las palabras no aportan sustancialmente, más o menos es relativo eso también, ¿no? Pero e pero bueno, nada, ahí si encontré después hice también un análisis de qué porcentaje del documento cabe en 512 tokens. Era la idea original. Sí. Eh,
lse posgrados: Ah.
Marcelo Luna: lo que lo que terminé, digo, a lo que le terminé sacando más valor fue en realidad entender qué cantidad de tokens necesitaba para procesar cada documento. Eh,
lse posgrados: Claro.
Marcelo Luna: ahí lo que dice, yo yo elegí un modelo con el que trabajar, eh, busqué un tokenizador de ese modelo, que lo que hace es tomar los documentos y y y tokeniza como toqueniza el modelo, básicamente.

01:41:33

Marcelo Luna: Y entonces lo que hace básicamente es contar en el documento, decir, "Che, este documento te va a implicar 58000 token, este 32000, este 107000." Sí,
lse posgrados: Claro, eso cuando lo mandó en espacio vectorial va a tener un
Marcelo Luna: sí, correcto. Eh, lo hice más que nada pensando también en que es un elemento fundamental para
lse posgrados: Toda
Marcelo Luna: poder presentar un análisis de costos, ¿no?, "Che, ¿y si alguien quiere construir esto? ¿Cuánto? ¿Cuánto le cuesta? Sí, el mismo ejercicio podes hacer después con cada consulta, con cada análisis de cada escenario, pero este es como fundamental. Si poner esto en marcha te va a costar esta cantidad de token.
lse posgrados: Sí, hay un comentario, algo que dijo Shimón, hoy todo es gratis,
Marcelo Luna: Eh,
lse posgrados: hoy le metemos y y yemin te da y y Cloud está un poco más limitado porque tiene una ventana en contexto más grande y más desarrollo, pero yo creo que en y de hecho hacia eso vamos, en los próximos años las herramientas van a tener un cambio en en el pago,
Marcelo Luna: sí.
lse posgrados: ¿no? Entonces, la economía tokens es es una disciplina que se va a venir, digamos, ¿no? Cómo cómo hacer el preproceso y tratar de ahorrar a

01:42:47

Marcelo Luna: Mhm.
lse posgrados: digamos la cantidad de token a procesar en las preguntas, en las respuestas, en los espacios vectoriales acá y allá. Me parece que eso es algo que todavía no está todavía, porque obviamente cuando todo abunda, digamos, cuando nada escasea, cuando el recurso no es escaso, no hay nadie diseñando nada hacia eso, pero cuando empieza a escasear capaz que está bueno tenerlo ya listo, ¿no? Entonces, como tenerlo ahí como una banderita y me tengo que poner investigar
Marcelo Luna: Sí, sí. Vamos a terminar como como se programaba en los inicios del de la
lse posgrados: esto.
Marcelo Luna: computación, ¿no? tenía 8 meg de memoria y tenía que andar viendo a ver qué poner en memoria y qué no, porque si no no te no te daban ahí tiene la mano.
lse posgrados: Sí, Santi, Santi, te escuchamos.
Santiago Germino: Hola, ahí está. No podía activar el micrófono. Eh, no, yo les quería comentar, no sé si sabían o si lo habrán nombrado por acá, pero hay un un repo en algún lado e que habla sobre hablar como cavernícola, que eso después este en realidad no es un original, sino que fue de alguien que hizo, publicó un paper hace un rato, años también comentando que si uno hablaba tipo como cavernícola, los toques majaban y el modelo te entendía igual.

01:44:07

Santiago Germino: Entonces, eh digamos,
lse posgrados: Ah.
Santiago Germino: hay maneras de de de economizar, digamos, tokens que ya están, digamos, siendo probadas, eh, y y en cuanto a lo que comentaba aquel compañero de que están subiendo los precios,
Marcelo Luna: Ok.
Santiago Germino: van a subir en los próximos años, están subiendo ahora, están subiendo significativamente ahora, eh, y se están llevando las empresas que que incorporaron en sus procesos una sorpresa enorme, porque las facturas que le están llegando son increíbles. Tak.
lse posgrados: Genial. Ahí encontré el repo es lo primero que encontré, así que puede que tenga algún error, pero después busco más. Está bueno eso, porque si hablar como cavernícola ayuda, todo lo que hemos visto de Leda tiene mucha más relevancia,
Marcelo Luna: Sí,
lse posgrados: ¿no? Sí, simón.
Shimon Ben: No, sí,
Marcelo Luna: sí.
Shimon Ben: la apuesta es a pérdida básicamente. Lo que pasa que bueno, por ahora no necesitan para recaudar datos. Y en general se empieza a hacer caro cuando eh vos eh a ver está mucho uno si va viendo, digamos, la información actual las noticias de inteligencia artificial, te proponen hacer ya agentes y automatizaciones, etcétera, que eso sí necesita mucho recurso y sí por ahí tenés que pagarte un un plan de algún o para hacer imagen, video, todo eso sí, para eso sí tienes que por ahí probablemente pagar un plan, pero mientras sea vos usar palabras para que la

01:45:40

Shimon Ben: IAT sepa más de vos, por ahora van a hacer ese despilfarro, van a invertir en nosotros, nos van a regalar un poco de tokens que necesitan es saber nuestros consumes y costumbres. Este,
Marcelo Luna: H
Shimon Ben: pero sí es verdad que que hay unos momentos estuve viendo que que e este de de Shemin aumentó como tres veces más el la cantidad el valor del token. Eso fue en estos días.
Santiago Germino: Sí, sí,
lse posgrados: Sí,
Santiago Germino: También estado.
lse posgrados: hay que economizar, digamos, ¿no? O correr modelos locales
Marcelo Luna: Sí,
lse posgrados: también.
Marcelo Luna: yo ahí tengo dos comentarios. Eh, digo, lo que decía Santiago, sí, es correcto. Eh, no hay que perder de vista que en realidad un token no necesariamente es una palabra, ¿no? Eh, digo, depende de los modelos y entonces también la de economizar lenguaje no es necesariamente equivalente a economizar token, pero obviamente cuanto más acotadas más este
lse posgrados: Claro, yo creo que apunta más el proceso.
Marcelo Luna: más ventaja.
lse posgrados: Saca stop. Capaz que si saca tod el L entiende igual.
Marcelo Luna: Exacto.
lse posgrados: ¿Ustedes no les pasa?
Marcelo Luna: Y ahí saca medio medio documento casi en mi

01:46:53

lse posgrados: Claro, a mí me pasa que cuando yo escribo,
Marcelo Luna: caso.
lse posgrados: ponete, escribo o estoy prompteando, ya ni me preocupo si escribo bien la palabra, honestamente,
Marcelo Luna: Sí, claro,
lse posgrados: porque sé que la interpreta.
Marcelo Luna: porque te entiendo igual.
lse posgrados: Hm.
Marcelo Luna: Sí,
lse posgrados: Entonces,
Marcelo Luna: sí,
lse posgrados: hay algo para testear. Gracias, Santi, porque capaz que si usas abreviaciones,
Marcelo Luna: sí.
lse posgrados: digamos, eh, no sé,
Shimon Ben: Es
lse posgrados: pone la palabra conspiración puede ser dividida en cuatro tokens o dos o tres tokens, pero si usa con ya estás listo en un token y así puede empezar a meter un montón,
Marcelo Luna: Sí,
lse posgrados: ¿me entendés?
Marcelo Luna: sí,
lse posgrados: Sigamos,
Santiago Germino: quitas los conect todas esas cosas
Marcelo Luna: sí.
lse posgrados: Marc.
Santiago Germino: ahí sacas sacas cosas,
Shimon Ben: What?
Santiago Germino: sacas este conectores, sacas este eh un montón de cuestiones que por ahí no hacen el entendimiento del del texto, sino a la como la gramática y eso parece funcionar.
Shimon Ben: Yo como ejercicio lo que hago es pedirle a la IA que siempre me devuelva cuántos tokens utilicé yo para preguntar y cuántos la IA para contestarme,

01:47:57

lse posgrados: Ah, buena.
Shimon Ben: para estar todo el tiempo viendo ese dato y ir intentándolo para cuando empiecen a hacer el ajuste.
Marcelo Luna: Hm.
lse posgrados: Está buena esa. La tomo. Esa no la hacía. Gracias. Está buena.
Marcelo Luna: Sí.
lse posgrados: Bueno, sigamos, Mar. Así ya me voy.
Marcelo Luna: Bueno, dale. Eh, bueno, nada, después digo, tengo algunas algunas cosas más, no sé si son tan este tan relevantes.
Shimon Ben: No.
Marcelo Luna: Eh, déjenme que los encuentre. tengo un montón de código, pero eh nada, la cantidad de chans por documento, digo, esto es un poco más técnico, ¿no? para tratar después de de implementar toda la ingesta y e inclusive el el
lse posgrados: Clar,
Marcelo Luna: la
lse posgrados: ahí importante que veas, fíjate la cantidad de tokens por chunks, cómo cae en los en este en el libro de caso,
Marcelo Luna: Sí,
lse posgrados: o sea, libro de caso es como conversado. El otro son reglas,
Marcelo Luna: sí,
lse posgrados: artículo uno, no sé qué, bla bla bla.
Marcelo Luna: exacto.
lse posgrados: Ahora, libro de reglas, ocupar repocos token por chan, es decir, que la separación cuando la hace decir, bueno, situación, regla asociada, resolución, chao, listo.

01:49:08

Marcelo Luna: Sí,
lse posgrados: Entonces cae cae drásticamente la cantidad de tokens por chance,
Marcelo Luna: correcto.
lse posgrados: con lo cual tu fragmentación no debería ser uniforme, digamos, tu tu chanqueo acá definitivamente no puede hacer un chanqueo uniforme por
Marcelo Luna: Exacto.
lse posgrados: PDF. Porque tu retrival va a mezclar. Lo que no puede hacer tu retrival es mezclar casos del libro de casos.
Marcelo Luna: Claro. Sí.
lse posgrados: no lo puede hacer porque si no va a traer errores.
Marcelo Luna: Eh, sí. Es que de hecho el libro de casos estoy bueno ahora después les muestro dónde estoy porque estoy dudando si incluirlo como parte del radio porque primero mucho volumen y segundo
lse posgrados: Ah.
Marcelo Luna: es en realidad eso es el ejemplo de lo que yo quiero obtener y si le enseño al modelo a responder en función de esos casos en particular no sé hasta dónde lo estoy seggando, pero estoy ahí elaborando la idea.
lse posgrados: Gracias, gracias.
Marcelo Luna: Todavía no lo tengo muy claro. Pero bueno, acá hay también traté de identificar dos, digo, dos de los de los delimitadores que que son bien claros, ¿no? Acá la cantidad de reglas que identifica en cada uno de los eh de los documentos. Pero, ¿qué pasa? E la interpretación es importante acá porque acá las reglas son esto es una lista de reglas.

01:50:40

lse posgrados: Claro.
Marcelo Luna: Sí. Este en particular es una lista de casos. Estos no tienen casos. Sí, porque estos son reglas puras. Este es una lista de casos, pero cada caso por ahí menciona varias reglas. Entonces, ese procesamiento, tratar de entender las con las expresiones regulares. ¿Cómo menciona reglas? Este documento no me sirve de mucho. Sí me sirve para estos dos. Sí.
lse posgrados: Clar, claro.
Marcelo Luna: Digo, ahora les muestro un poco más también. Bueno, después algunas cosas más de eh ruido, de páginas casi vacías, digo, nada, era gratis hacer gráfico y entonces hice
lse posgrados: Está bueno de todo eso seguramente sacaste tu top cinco y tenés ya del lo uso esto.
Marcelo Luna: eh Exacto. Sí. Eh, pero por ejemplo, a mí en este caso el número no es muy alto, pero sí pero sí me pareció eh interesante entender la longitud de las líneas en los documentos, porque si vos tenés un documento muy extenso, pero con un porcentaje muy grande de líneas cortas, de renglones cortos,
lse posgrados: Claro.
Marcelo Luna: eh también te da una idea del del contenido. de la densidad del contenido. Eh, nada, bueno, hay hay varias cosas acá y después lo que hice acá fue algo más relacionado con esto.

01:52:10

Marcelo Luna: Te lo contabas vos el otro día, Cristian, que tiene que ver más por el tipo de de solución que estoy implementando. tengo que buscar un o estoy tratando de buscar una recuperación híbrida léxica por un lado para las cosas más duras como las reglas por ejemplo y semántica para la interpretación de lo que el que está escribiendo, interactuando, quiere eh para tratar de definir la intención de lo que está eh
lse posgrados: Claro.
Marcelo Luna: mostrando. Sí. Y entonces encontré más que este lo que son los términos léxicos por Chank, este es el que a mí me resultó más útil. O sea, ¿cómo cómo se interpreta este esta especie de semáforo? Si eh digo esto busca términos léxicos relevantes en el documento y su frecuencia. Entonces, idealmente esto tendría que ser lo más pequeño posible. Sí, porque estos son los que son de aparición única. Sí.
lse posgrados: Claro,
Marcelo Luna: Y estos verdes deberían ser los que más aparecen. Sí,
lse posgrados: pero tenía está como parecido,
Marcelo Luna: los que están está muy
lse posgrados: ¿no? O no.
Marcelo Luna: balanceado.
lse posgrados: Claro,
Marcelo Luna: Estoy estoy estudiando todavía qué impacto puede tener eso en
lse posgrados: claro, claro.
Marcelo Luna: en los resultados.

01:53:47

Marcelo Luna: Sí, pero digo, en principio una señal de preocupación es que este rojo fuera más grande. Sí, porque esto representa un tercio del del vocabulario global, o sea, no está tan mal, pero estaría bueno que fuera menor. Sí. E y después, bueno, a mí este que este me resultó también más o menos útil, que fue tratar de identificar. Acá hay solamente 18, pero digo, hace toda la cuenta. Sí, pero es esto es ya sin los stops, ¿cuáles son los términos que más se repiten en cada documento? Acá este es medio una anomalía porque esto es gramática también, ¿no? Tiempos verbales, pero eh pero finalmente eh bueno, en el de reglas, regla es justamente el que más se repite, vote, race, comit son todos eh términos asociados con justamente el el dominio del documento. Sí. Eh, a mí por lo menos me sirvió para entender que cuando hago la limpieza no me estoy dejando de fuera eh términos que son relevantes, ¿no? Son más o menos parecidos los tres. Eh, bueno, acá aparece case también, pero bueno, esos fueron un poco las métricas que saqué. Sí, lo único que les quería mostrar es que digo,
lse posgrados: Bien,
Marcelo Luna: después de todo esto, finalmente lo que logré fue hacer un procesamiento para traer esto del PDF, que esto te lo mostré a vos,

01:55:35

lse posgrados: lo que importa
Marcelo Luna: Cristian, el otro día también. Claro, que es efectivamente lo que importa, o sea, de un PDF, que es un texto completamente desestructurado,
lse posgrados: No.
Marcelo Luna: entre comillas, ¿sí? E lo que lo que obtengo finalmente es una tabla de reglas y entonces lo que necesito ahora es identificar para qué caso aplica cada uno de estos renglones o qué renglones aplican para el caso que estoy tratando de de analizar.
lse posgrados: Genial. me da justo el el pie para explicar lo siguiente.
Marcelo Luna: Ni que lo hubiéramos ensayado. Entonces ahí va.
lse posgrados: ¿La viste?
Marcelo Luna: Bueno.
lse posgrados: Gracias, Marc. Buenísimo el avance. Fed, digo, eh, Marce,
Marcelo Luna: Eso.
lse posgrados: Shimón y el los chicos que se sientan atrasados, que no hayan avanzado con el EDA, etcétera, siéntanse libres de escribirme un correo y coordinamos una reunión entre los que necesiten y nos juntamos una horita. Creo que la mejor interacción que hemos tenido ha sido en las tutorías, porque ahí como que vamos al hueso y de nuevo,
Shimon Ben: Ah.
lse posgrados: eh, los que no han no han interaccionado, siéntanse libre de mandarme un correíto y coordinamos.

01:56:49

lse posgrados: Yo por suerte tengo disponibilidad ahora vamos viendo el horario, etcétera. Hacemos una o dos máximo y ahí metemos los que faltan. Okay. Bueno, eh, a ver lo que ensayamos con el acá. Bueno, ahora vamos a hablar de las métricas del RAC, ¿sí? O sea, vamos a ver cómo se recupera, cómo recuperamos. Ahora, de nuevo, a mí siempre me gusta preguntarles si entienden lo que hacen un rack,
Shimon Ben: Ok.
lse posgrados: ya se lo pregunté un montón. Entonces, busqué esta imagen que me parece bastante bastante digamos práctica. Eh, hasta ahora hemos venido hablando de esta de esta sección para que poner presentación. Ahora sí, eh hasta ahora venimos hablando solamente de esta parte y quizá de la base de datos, ¿sí? Don tenemos los archivos que son la fuente, todo lo que es el eda, la extracción, la ingesta, etcétera, etcétera, etcétera. Chanqueado. Seguiría el chanqueado. El vector de embedings, base de datos. Sí. Eh, ahora la parte del retrival es esta que está acá, donde a una pregunta se la vectoriza, se la contrasta con el espacio de, digamos, el espacio de características, la ese mapa con múltiples variables para extraer aquellos documentos relevantes.

01:58:28

lse posgrados: Acá de nuevo y siempre repito, cuando se extrae un documento relevante, no se extrae uno, se extrae un la cantidad K de documento relevante, que es lo que forma después la respuesta y mediante un LLM se genera la respuesta. Entonces acá lo que tenemos que preguntar es dónde puedo meter métricas. Sí, la primer sección, ¿dónde meter una métrica? ¿Dónde puedo evaluar esto? ¿Cómo está funcionando? Es aquí en cómo extraigo los documentos relevantes. Sí, este es el el primero eh transparente porque de nuevo lo hemos hablado un montón en las clases, uy, perdón, lo hemos hablado un montón en en las clases anteriores. Si yo no hago un buen chanqueado, si no no el texto, etcétera, el documento con lo cual se va alimentar el LLM, eh va a generar respuestas malas hacia el usuario, ¿no? Porque después el LM lo que hace es tomar esto y en función de lo de lo de los documentos relevantes generar una respuesta. Y la segunda sección donde podemos meter métricas, donde podemos medir o mejorar esto es acá en cómo está funcionando el LM. Entonces, las métricas de RAC se van a dividir en dos. Por un lado, las que sean propias del retriival, de cómo extraigo la documentación y la segunda por cómo genero, cómo el cómo el LM genera la respuesta porque estas cuestiones escritas que estos bichos pueden pueden alucinar, ¿no?

02:00:17

lse posgrados: Bueno, entonces básicamente un retriival es como un examen al libro abierto,
Shimon Ben: Sí.
lse posgrados: o sea, estoy en la universidad, me dan un examen de un libro y yo puedo eh por un lado fallar en encontrar la página del libro donde tenía que armar la respuesta o yo puedo interpretar mal lo que me entregó el libro para escribir la respuesta. De este lado estamos del retrival y de este lado estamos de la generación, lo que expliqué recién. Eso quedó claro. ¿Hay alguna duda? Porque digamos es como el el punto de partida.
Gabi Tallarico: Bien,
Shimon Ben: H
lse posgrados: Hoy no me voy a meter tanto en esta, voy a solamente mostrarla o quizás mencionarla porque estamos todavía extrayendo documentos, digamos, ¿no? Para armar las respuestas al todavía no lo estamos poniendo a prueba, sino estamos poniendo a prueba o mejorando nuestra forma de preprocesar documentos que nos permitan extraeros documentos para que el Llle. Básicamente, digamos, si todo sale bien, no debería fallar. Bueno, de nuevo, en esta sección el fallo de retraival es esta lógica del arquero. Bueno, a ver, yo estoy apuntando hacia hacia un espacio vectorial donde hay documentos. ¿Cuáles documentos traigo?

02:01:44

lse posgrados: Sí. Entonces acá hay dos métricas, la precision del digamos en función de los documentos y el recal digamos, ¿no? La precisión mide la proporción de esos documentos relevantes entre los K recuperados. O sea, si yo pongo un K de CCO y hay un documento relevante, voy a tener uno en cinco. Sí. Ahora vos decís, "Bueno, ¿cómo automatizo si es relevante o no?" No, ahí no es difícil automatizar, o sea, casi casi que no podemos automatizar si ahí dependemos nosotros, digamos, ¿no? ¿Cómo detecto si es relevante o no? Bueno, podría ser algo con similaridad y tener algunas respuestas estandarizadas y después medir la similaridad entre mi respuesta entre mi entre mi respuesta estandarizada hecha por experto respecto de la respuesta que me que me arrojó el el o el fragmento que me arrojó el retrival. por ahí lo lo mejor es que lo haga una persona. Entonces, eh en los rack, en esta en esta tecnología es es digamos es una buena práctica que lo haga uno, digamos, ¿no? O sea, básicamente tengo mi ground, digamos, le hago una pregunta, me fijo que respondo, me fijo cuántos documentos relevantes, verdaderos hay en la respuesta y eso, ¿qué me va a medir?

02:03:12

lse posgrados: ¿Cómo yo hice los chanqueos? Si si hay overlap entre distintas temáticas. eh, etcétera, digamos, ¿no? ¿Para qué esto es? para evitar que enviar estos fragmentos al LLM para que después responda mal, digamos, ¿no? Ese por un lado, la precisión es la más fácil y es la que yo digamos les pido que aquellos que estén trabajando con RAC lo apliquen ahora, digamos, esta semana, o sea, ya porque esa es muy sencilla. extra los documentos y no sé, le hacés, no sé, 50 preguntas y te fijas dentro de esos cinco documentos, anotas, te fijas cuáles son las relevantes, digamos, las que realmente aportaron y de bueno, la analogía sería de todos los peces que sacaste en la red, ¿cuántos eran los que vos buscabas? Sí. Ahora, el recall es un poco más complejo porque el recall, digamos, mide cuántos documentos relevantes existentes fueron efectivamente recuperados. Entonces, ya tenés que saber eh que existen una determinada cantidad de documentos existentes que quizás en el volumen de información que uno tiene no los conocer a todos, digamos, todos los casos. Sí. Eh, eso es para qué, para eso es como para medir que no se me escape ningún documento relevante.

02:04:36

lse posgrados: Si de repente acá me apareció un uno, pero yo tenía más, entonces digamos eh esto me va a decir, bueno, uno entre entre todos los documentos, un documento relevante entre cinco documentos, por ejemplo, y el recole no, pero yo en realidad todo mi retriival tiene 25 documentos. Bueno, ¿cuánto de esos 25 extrajo la respuesta? Pero para acá hay que trabajar más en en el ground, digamos. Sí. Bueno, ahora esta es otra crítica un poco más más compleja, ¿sí? El min reciprocal rank, digamos, evalúa una pregunta, eh, una única pregunta, ¿en qué posición aparece el primer documento relevante? Es decir, no le interesa el conjunto de todos los demás. Si el primer documento relevante aparece eh primero, que es lo que yo espero siempre en un rack, eh listo, tiene uno. Si si aparece en la segunda posición ya le castigo, le quito peso de nuevo, ¿cómo se esto? trabajo manual, digamos, no lo lo vas puntuando al final, si apareció en la quinta posición, eh, ya le aplica un severo, un castigo severo. Yo diría que por el momento en esta no se metan, a menos que quieran porque requiere más trabajo.

02:06:04

lse posgrados: Entonces, a mí me parece que la mejor para empezar es la precisión que es la más fácil, digamos, ¿no? Eh, no no quieramos ir todavía más allá. Eh, me parece que por ahí puede venirme de la mejor en la práctica, digamos, ¿no? Ahora hay otra hay otra hay otras métricas también, digamos, cada vez más sofisticada y cada vez también requiere más entendimiento de esto, digamos. En este caso eh de la NDSGC de normales discounted como gain no solo pregunta si los documentos son relevantes, si no estando ordenado de mayor a menor relevancia, o sea, nivel uno, relevancia graduado de buenos a malos y el nivel el nivel dos penalizado por posición y el nivel tres comparado contra un orden perfecto. Yo diría que acá no se metan todavía. Solamente se los puse para que sepan que existe. De nuevo, comencemos con la precisión que creo que es el el el es el primero que hay que que hay que usar. Sí. Por otro lado, bueno, eso sería como el paquete de del retrial de extraer documentos, precisión, recal, el mrr. Y este que viene de GC, ¿no? A este nunca lo utilicé yo honestamente.

02:07:28

lse posgrados: A este un par de veces sí en trabajos que hice en la especialización y al este es que primero uno ve este precisión me parece más más fácil de entender incluso. Y por otro lado es ver si el LM responde o no, cómo responde el LM, la otra la otra fase, digamos, ¿no? Eh, y ahí está la metría que se llama fightfulness o la fidelidad. Evalúa si cada afirmación presente, la respuesta generada puede ser verificada directamente los documentos recuperados. O sea, yo ya tengo mi lista de documentos recuperados, pero me fijo en la respuesta, entonces tengo que tener ya una respuesta generada. Entonces, ahí vos tenés que ir manualmente decir el texto que generó en realidad se basa en el documento. Sí. Y bueno, eso es lo que mide el esta esta métrica. Eh, no me quiero meter mucho más en las métricas de del LNM porque todavía no lo estamos usando, pero hay más. Les quiero mostrar antes de esto eh un notebook que les preparé. Eh, donde me parece que ya es es esta donde ya hay digamos un algunas y otras métricas, pero bueno, como saben, yo tengo el caso este testigo del eh boletín oficial. Sí. Eh, entonces lo que hice fue separar fragmentos para no trabajar con todo el boletín o con la ingesta el PDF, fragmentos del PDF y hay dos como dos secciones, digamos, ¿no?

02:09:09

lse posgrados: la sección uno, lo que yo llamo un un rack na, digamos, ingenuo, donde lo que hace es toma todo el texto, lo divide, eh vectoriza y recupera los eh con un chanqueo fijo, sin interpretación, sin metadatos, sin nada de lo que hemos hecho. Entonces, esto va haciendo todo lo que ya conocen, TFDF, eh, etcétera, etcétera. De acá viene, ya le los testeé con cinco preguntas que van que son medio específicas de de de los documentos que están hacia arriba y tengo la respuesta. Entonces, eh digamos lo que va a aportar esto va a ser el valor de similaridad coseno en en este caso, como la la OP, que era ese ese número de digamos de de resolución, etcétera, que tenía el texto legal, no va a aparecer, no hice preproceso y y después me va a devolver el el chan ganador, digamos, no podría traer Este trae el top uno, podría traer el top K, en este caso está trayendo uno, digamos, no podría traer cinco, seis, pero la idea es que ustedes vayan en sus en sus trabajos usando esta, digamos, esta arquitectura, porque al principio de cuando iniciamos el curso, en algunos documentos que yo había había visto, no todos traían eh los K documentos, sino traían como el ganador.

02:10:45

lse posgrados: Entonces ahora hay que empezar a mirar los c documentos, digamos, ¿no? Obviamente cuando cuando empezamos a pesar lo las métricas del del del naiv, digamos, del ingenuo, vemos que obviamente a medida que nos vamos hacia los documentos más lejanos, la similitud coseno va a ir va ir bajando, digamos, ¿no? O sea, los fragmentos que me va a ir trayendo van a ya no van a ser tan parecido a la a la pregunta que yo estoy haciendo. Y del otro lado, para comparar está hecho con eh usando un ya preproceso, extrayendo el extrayendo el el ministerio, el expediente, el correje, que todo esto es lo que hemos visto en en la clase de preproceso y y exploración. Entonces acá ya no es tan ingenuo. Hay, digamos, los chan están separados por eh, por resolución, básicamente este número de resolución y tiene un poco de metadatos. Hay cantidad de palabras. No hice exploración, esto porque ya lo habíamos hecho anteriormente, pero sí aplicado un chank recursivo, o sea, un chank a un chanqueo específico para cada para cada resolución, porque en es lo que yo necesito en mi caso, en el caso de los veleros, quizás también aplique algo parecido.

02:12:14

lse posgrados: En el caso de el ajo, quizá también debería aplicar algo parecido, ¿o no? Eso lo están estudiando las chicas de del equipo. Eh, pero en definitiva, cuando aplicas el RAC acá de nuevo, eh, digamos el el documento eh digamos la búsqueda ya no va a ser eh no va a ser solamente por lo que contenga el Chan, sino también lo que contengan los metadatos, digamos, ¿no? Entonces, ya cuando hay un índice que ya tiene el tipo de decreto, el número y su categoría, cuando uno eh tiene esta parte, estos flag, cuando el chan aporte los documentos, por ejemplo, este documento se separó por su tamaño en dos chanks, pero y son de la ley, etcétera. Entonces, como que los chans ya están en el propio chan ya está implícito que se trata solamente de un documento. O sea, si acá tengo estos tres chas que están acá tiene asociado qué documento es. Entonces, la respuesta debería debería ser debería ser mejor, digamos, ¿no? Entonces, bueno, en definitiva, eh cuando uno ya lo cuando uno ya directamente le hace la pregunta, en la misma respuesta traigo el score, el OP, el decreto, eh el el chunk, digamos, completo con lo que con lo que ya con lo que ya trajo, digamos, ¿no?

02:13:52

lse posgrados: Y después ahí está hecho con estas dos métricas. Esta seguramente qué tan arriba aparece el primer chan y eh la precisión, digamos, de todos los chan que me trajo cuáles son relevantes, digamos, ¿no? Acá hay algunas test un test de preguntas, ¿sí? Y acá las métricas. Acá está el cálculo de la métrica, funciones para que puedan reutilizar. Y acá en este caso particular no me dio tanta diferencia porque son documentos chiquititos, pero sí eh quería creo que creo que no subí el el el final donde están las donde está la generación de respuesta. Ah, la sección cuatro. Bueno, acá están están puestas las eh las métricas para que puedan para que puedan ejecutarlo y hay un tercer una tercer sección donde aplico las respuestas, digamos, ¿no? Para eso decir evaluar que qué tan precisa es la generación. Para eso, para hacerlo más fácil eh va lo corrí con con Olama. Sí, para demorar un rato. Ustedes saben cómo funciona esto que cuando uno lo corre en local es medio j*****. Si lo pueden lo que originalmente lo podía poner como APIK, pero bueno, con estos cambios yo no estoy tan seguro de que eh las APIQ de Open sean libres.

02:15:25

lse posgrados: De hecho, procesé boletines en una de las clases y después me fijé, me llegó un consumo de, no sé, 5 o $ y dije, antes era gratis, ahora me cobraron $ por esto. Entonces como que ya de baja la piqu dije, bueno, no me voy a meter en esa, no voy a hacer gastar porque todo, como dijimos, está todo cambiando, digamos, ¿no? Eh, y acá está el pipeline completo. Entonces, en un pipeline completo debería ser así. Eh, esta es la pregunta. ¿Quién fue registrado? ¿Quién fue designado como titular? Este es el fragmento, eh, perdón, esta es la respuesta usando los fragmentos de Undaib, digamos. Fíjense que el LM acá escribe el el titular del registro de notarial número uno fue el escribano tanto. Ahora con el mejorado va mal grano. El escribano t taat DNI números tanto fue designado como titular. En este caso de juguete la diferencia no es tan grande, digamos. Pero en otros casos puede llegar a puede llegar a tener más una mejora o en otros como este son respuestas prácticamente muy parecidas, digamos, ¿no? ¿Cuáles son las sanciones de la ley?

02:16:45

lse posgrados: Ta ta ta. Las sanciones son para curso carrera en materia de salud y básicamente responden lo mismo. Eh, en este caso de juguete no hay tantas diferencias, salvo que cuando pregunto sobre alguna persona como el DNI fue extraído por usando reconocimiento de entidades, la respuesta va a ser más más específica, digamos, ¿no? Y también está acá la las consultas y la mejor respuesta para uno y para el otro, digamos, ¿no? E yo creo que deberían explorar este eh esto para ver qué todo esto aplica para su para su trabajo, digamos, ¿no? En definitiva, acá hice un cosito, hice una comparación donde, bueno, no hay muchas diferencias, digamos, usando la no prácticamente no hay diferencia en este caso particular, digamos, ¿no? En el retrival, eh, pero en sus casos quizás sí, digamos, ¿no? Y y de nuevo, originalmente lo había hecho en en el cine graphic, había hecho este, pero cine gráfico, pero eh el pipeline es este. En mi caso particular de los de los boletines, entra un PDF, usamos PDF Blamber, hacemos la segmentación, paramos los datos, o sea, parciales, ir extrayendo, digamos, iterando, sacando lo la reconocimiento de entidades, aplicar ese chan recursivo, extraer, digamos el eh en prefijos todo esa ese contexto y pasarlo por TFIDF también.

02:18:32

lse posgrados: Una vez hecho eso, vectorizarlo y ya lo que conocemos del del RAC. Sí. Eh, nada, acá hay algunas cositas más. Yo creo que lo lo que deberían ustedes ahora hacer es eh usen esto porque acá ya están las métricas, la fórmula o pueden integrarlo con Llm y hacer que sus rack entreguen eh cinco documentos, ¿no? Entonces, si nos vamos acá y vamos, digamos, lo que espera usted esta semana es que a a yo por ahí hablo y y hablo por el tema de los rag, pero los que tienen problema de clasificación, bueno, usen la precisión, digamos, ¿no? eh o usen una matriz de confusión y empiecen a comparar respecto de cómo estaba el original, o sea, cuando comenzante comenzar la materia, que es más o menos lo que todos entregaron en trabajo final en acá del lado de y la y usando la precisión eh en esa original y cómo es ahora con alguna eh alguno de esos descubrimientos que encontraron en el en eleda, ¿sí? ¿Cómo les cambió o no en en esta métrica, digamos? Sí, eso sería como lo que lo que quedaría para esta semana. Entonces, la semana que viene eh vamos a ver más complejidad respecto de las métricas, un caso más casos más particulares, pero me gustaría ya tener casos de ustedes como decir, bueno, eh, ¿mejoró o no mejoró?

02:20:14

lse posgrados: Voy a tratar de traer casos más eh eh contrastantes para que vean que la métrica sí funciona, pero hay una realidad, hay un digamos en sus trabajos hay que hacer un trabajo, se hay que hacerles preguntas ya al RAC, el RAC va a entregar respuestas y y ustedes tendrán que valorarlas de esas cinco respuestas. Yo no creo que no lo sugieron que haga más de cinco porque si no va a ser muy largo, que entregue cinco documentos y de esos cinco documentos, ¿cuáles son relevante para responder la pregunta? Le hacen, no sé, 10, 20, 30 preguntas y en función de eso calculan la la precisión. Una vez hecho eso, ya lo deberían comparar con respecto a la a la arquitectura original que tenían, eh, y ahí ya tenemos documentada la mejora o no. Y ya nos acercamos un poco más. Una vez documentada la mejora, ya no podemos empezar empezar a trabajar como estructura el informe, los insightes, etcétera. Un poco lo que preguntó Gabi. Gab al principio, capaz que puedo dar un template un poco más más detallado, pero eso sería lo que lo que esperan ustedes esta semana, digamos, ¿no? Sí.
Gabi Tallarico: No, lo que está bueno Sí.

02:21:34

lse posgrados: Pregunta.
Gabi Tallarico: No, no, no más que pregunta es que entendí o que hice el match del video que pasaste de las métricas de RAC con la práctica de hoy, porque después que había visto el video de las métricas los otros días no entendía cómo aplicarlo, cómo hacerlo. Ahora hice como esa unión de las dos cosas, video y práctica.
lse posgrados: Buenísimo. Y en las métricas RGAB hay muchas y obviamente como esto ya es una solución industrial, hay industrias que están aplicando ya esto por ejemplo para sistema de gestión. No sé si alguno ha trabajado alguna vez con sistema de gestión, pero son infinita cantidad de documentos y hay hay empresas que entran a o las mismas empresas que te certifican ISO también te dicen, "Bueno, mira, te armo un retriival." Ellos no llaman retrial, es un chatbot, pero atrás hay un retrial. Entonces, vos le preguntaste, bueno, ¿cuáles son los documentos relacionados a salud higiere para ingreso a plantas eh procesadora de minerales y listo, te manda todos los procedimientos, o sea, se está usando. Entonces, eh como se está usando, se está desarrollando mucho y se está queriendo mejorar tanto del lado del retrible como del lado de la generación. Entonces, para mí la precisión es lo más sencillo.

02:22:55

lse posgrados: Si el primer documento eh es debería nuestro documento, digamos, nuestro retrival después de todo el preproceso, gráfico, análisis que le hemos hecho, el primero, el uno debería responder a pregunta, ¿sí? Y todos los demás deberían ser parecidos. Ahora, en un contexto eh donde ese campo vectorial no está del todo separado, o sea, esa esas matrices que están en el campo vectorial no están del todo separadas porque hay eh digamos el EDA no hemos hecho el EDA o el EDA no nos permitió separar. Bueno, ahí puede que sean ambiguas, digamos, ¿no? La respuesta, pero no debería pasar por cómo por cómo lo hemos trabajado de la clase uno hasta ahora. el reconocimiento de entidad, de metadato, etcétera, eh debería debería habernos aportado una pequeña mejora, digamos. Eh, no sé si tienen dudas aquellos que no están trabajando con Rag por ahí como para porque aquellos que no están trabajando con Rag, si están trabajando con clasificación, la métrica también la precisión problemas más relacionados como el como el de Shimon eh eh más o menos lo mismo, digamos, ¿no? Nada más que ahí la cuál es la precisión del el acurra, así básicamente como como ya lo conocen. Hay otros casos eh que no tampoco son rack eh ahora no los tengo tan tan en claro, pero deberíamos encontrar una métrica de mejora para esos casos.

02:24:32

lse posgrados: ¿Alguien está fuera de estos dos casos de clasificación y RAC? Como para que lo discutamos. Bueno, a mí me queda pendiente responder un par de correos de de de alumnos que me han enviado la eleda y algunos avances, eh, así que nada, voy a voy a avanzar con eso para darle feedback. Creo que de la clase uno a la cuatro han habido progresos grandísimos. Eh, hay obviamente habían alumnos que estaban ya bastante avanzados con con más conocimiento de IT, pero creo que ya de alguna forma no hemos equilibrado esa esa brecha, ya está más equilibrada y era uno de de de mis propósitos. Sí. Ahora, digamos, vamos a dejar eso de lado y lo que vamos a tratar es de eh documentar la mejora. Ese nuestro propósito, documentar la mejora, es decir, aquello que estaba en la clase cero, por así decirlo, era un un esquema, era una prueba de concepto. Ahora nos acercamos a algo un poco más operativo, por así decirlo, y ahí debe haber alguna mejora. En el caso que no haya mejora, no pasa nada, no hay mejora. digamos, ¿no? Pero se documenta de todas formas, así que capaz que eran casos más simples y no por más que hemos hecho esto y aquello no no mejoró.

02:26:10

lse posgrados: Eh, pero no pero sí es necesario hacer este recorrido. La clase que viene voy a traer casos más concretos de métricas de de RAC. Sí. Eh, y eh ya vamos a hablar sobre digamos, o sea, métrica rack de los dos lados, del lado del retrival y del lado de eh la generación. Y ya nos vamos a empezar a a acercar a el el diseño, digamos, acercarnos caso por caso al diseño ya del documento final y qué es lo que quieren comentar, cómo quieran documentar y y hacia dónde se cerraría ese circuito de la como la de esta mejora documentada. Eh, aquellos que quieran seguir trabajando en Eleda, adelante, avancen, les va a servir, pero eh ya vayan apuntándole más a la a las conclusiones. ¿Sí? Y por último, antes de cerrar la clase, eh, de nuevo, tengo disponibilidad, así que mañana no, mañana mañana no, pero durante el fin tengo disponibilidad para acomodarme, eh, si algún uno o dos grupos quieren, tengo un par de horas ahí para para hacer coaching. los que los que ya hicieron y quieren repetir y quieren que nos organicemos, está disponible también me mandan un correo y ahí coordinamos el horario. El los primeros que coordine, esos van a ser los horarios que que queden, digamos, más fácil así y los que se puedan sumar en ese horario mandame un correo con la invitación y bueno, y los que no entiendo que ya están más avanzados quizás, etcétera. De todas formas estoy abierto a que me escriban y y avancemos. Así que bueno, eso es lo que había preparado para hoy. No sé si tienen dudas. Bueno, entonces los libero y
Gabi Tallarico: Muchas gracias.
Marcelo Luna: Gracias,
Gabi Tallarico: No,
Shimon Ben: Gracias.
Gabi Tallarico: Gabi entendió Gabi entendió el video con la realidad,
Marcelo Luna: Cristian.
lse posgrados: dale
Gabi Tallarico: así que es una maravilla.
lse posgrados: Bueno, chao chicos, nos vemos.
Gabi Tallarico: Hasta luego.
Marcelo Luna: Gracias.
Shimon Ben: Ah,
Gabi Tallarico: Chao.
Marcelo Luna: Nos vemos.
Juan Pablo Rueda: Gracias.
lse posgrados: Ciao.
juan ignacio sinopoli: Luo.

La transcripción finalizó después de 02:52:16

Esta transcripción editable se ha generado por ordenador y puede contener errores. Los usuarios también pueden cambiar el texto después de que se haya generado.

