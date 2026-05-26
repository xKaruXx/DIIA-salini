# Taller de trabajo final (3_8) - d015b25_ 2026_05_13 18_55 GMT-03_00 - Notas de Gemini

- Fuente: `Taller de trabajo final (3_8) - d015b25_ 2026_05_13 18_55 GMT-03_00 - Notas de Gemini.docx`
- Tipo: DOCX
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

📝 Las notas

may 13, 2026

Taller de trabajo final (3/8) - d015b25

Invitado salinastalamilla@gmail.com Taller de trabajo final - DIIAA 1Co2025

Archivos adjuntos Taller de trabajo final (3/8) - d015b25

Registros de la reunión Transcripción Grabación

Resumen

La reunión revisó metodologías de gestión de datos, limpieza técnica y resultados de análisis operativo avanzados.

Metodología y procesamiento técnico
Se estableció priorizar la ingesta cruda antes de la limpieza, separando funciones para mejorar la mantenibilidad y detección de errores. Se recomendó el almacenamiento en formatos estructurados como JSON.

Optimización y segmentación semántica
Se discutió la importancia de la segmentación semántica sobre la división por páginas para mejorar la recuperación RAG. Se validó el uso de datos sintéticos en etapas tempranas.

Análisis y hallazgos operativos
El análisis de datos en Redmine reveló que solo el 30% de las clasificaciones manuales coinciden con la realidad operativa. Se automatizó la clasificación mediante modelos de lenguaje.

Próximos pasos

[J.Pablo Zebraitis] Enviar Archivos: Enviar los archivos MD, Word o Zip, directamente para su revisión.

[J.Pablo Zebraitis] Explicar Solución: Preparar una explicación de la solución de desarrollo de producto (15 a 20 minutos) para la próxima sesión.

[lse posgrados] Revisar Solución: Revisar la solución presentada por J.Pablo Zebraitis. Proporcionar retroalimentación hoy o mañana.

[lse posgrados] Subir Video: Descargar el video y el resumen de la clase anterior. Subir ambos archivos al Drive.

[Juan Pablo Rueda] Enviar Documentos: Enviar un documento PDF y la tabla de datos asociada (Excel) a lse posgrados.

[Juan Pablo Rueda] Encontrar Función: Buscar una función (usando IA) para automatizar la conversión del PDF de entrada a la tabla estructurada deseada.

[lse posgrados] Asistir Búsqueda: Ayudar a Juan Pablo Rueda a encontrar la función necesaria para la conversión de PDF a tabla.

[Juan Pablo Rueda] Crear Estrategias: Definir 10 estrategias sintéticas (ficticias). Incluir estas estrategias en los datos del proyecto.

[Lorna Pons] Enviar Archivo: Enviar el archivo Excel/CSV con los datos limpios a lse posgrados para su revisión.

[Lorna Pons, Gabi Tallarico] Chunking Semántico: Implementar el chunking semántico en la separación de datos. Usar funciones y patrones regex, evitando la separación por página.

[El grupo] Generar Dashboard: Iterar con Cloud o Gemini para obtener un dashboard. Aplicar dashboard al tener gráficas.

[Marcelo Luna] Mostrar Código: Presentar código en la tutoría de mañana.

Detalles

Intercambio de archivos y presentaciones: J.Pablo Zebraitis envió una estructura de proyecto comprimida en un archivo Zip, incluyendo gráficos y dashboards, para su revisión (00:00:00). lse posgrados solicitó que J.Pablo Zebraitis prepare una presentación de 15 a 20 minutos para la próxima sesión con el fin de explicar su enfoque de desarrollo de producto, ya que se encuentra en una etapa avanzada (00:02:28).

Resumen del pipeline del proyecto: lse posgrados informó sobre la metodología de trabajo para esta semana, destacando que se realizarán tutorías en lugar de clases largas (00:03:49). Se repasó el flujo de trabajo: inicio con una pregunta base (utilizando un Canvas para definir alcances), seguido de la exploración de datos (análisis exploratorio de datos) (00:04:53). Se mencionó la metodología Lean de excelencia operacional para la gestión de actores clave o interesados, sugiriendo considerar este aspecto en etapas avanzadas del desarrollo (00:06:15).

Ingesta y limpieza de datos: lse posgrados enfatizó la necesidad de separar las funciones de ingesta de datos y limpieza, ya que ejecutar ambas tareas en una sola función dificulta la identificación de errores (00:07:32). Se utilizó como ejemplo un caso previo donde el texto ingresaba "en espejo" (invertido), lo cual no sería detectable si el proceso no estuviera segmentado (00:08:46). Es fundamental verificar la salida de cada función mediante herramientas como "print" para asegurar que los datos sean interpretables para el modelo (00:10:01).

Formatos de almacenamiento y optimización: Para manejar grandes volúmenes de documentos, lse posgrados recomendó exportar los resultados de la ingesta y limpieza a archivos CSV o archivos JSON en Google Drive, en lugar de procesar los archivos crudos repetidamente en Google Colab (00:12:43). El formato JSON es particularmente útil para manejar estructuras de datos complejas (diccionarios), permitiendo asociar documentos con tablas o metadatos específicos (00:16:52).

Documentación del proceso: lse posgrados insistió en la importancia de documentar un ciclo completo de trabajo, desde la entrada de datos crudos hasta el modelo final, para justificar las mejoras realizadas (00:23:03). Esta documentación debe reflejar cómo el proceso de limpieza y exploración de datos impacta en el rendimiento del modelo final, independientemente de si los resultados son perfectos (00:21:42).

Consulta sobre el orden de los procesos: Marcelo Luna preguntó si es posible realizar la limpieza antes que la ingesta (00:25:44). lse posgrados aclaró que, aunque existen excepciones (como descartar páginas irrelevantes al inicio), la regla general es realizar la ingesta de datos crudos primero (00:27:06). Se reiteró que la separación de tareas en funciones individuales es fundamental para la mantenibilidad del código, evitando mezclar responsabilidades como la eliminación de caracteres especiales con la selección de documentos (00:28:07).

Automatización del caso de productos nutricionales: Juan Pablo Rueda presentó su progreso con el manejo de etiquetas de productos en un archivo de Excel, observando una mejora significativa en las respuestas tras estructurar los datos (00:30:48). lse posgrados sugirió automatizar este proceso mediante la creación de una función (basada en el uso de prompts y expresiones regulares) que procese nuevos archivos PDF y genere la estructura deseada sin intervención manual (00:31:50).

Uso de estrategias sintéticas: Juan Pablo Rueda consultó sobre cómo manejar estrategias de engorde de ganado que aún no tienen una fuente oficial validada por veterinarios (00:32:50). lse posgrados aconsejó utilizar estrategias sintéticas para construir el flujo de trabajo inicial, permitiendo avanzar en el desarrollo y en la configuración del sistema de recuperación (retrieval) antes de contar con los datos finales (00:33:56).

Avances en el proyecto de transporte: Lorna Pons y Gabi Tallarico mostraron avances en la limpieza de documentos sobre carga y transporte, incluyendo la implementación de un glosario para el chatbot (00:37:27). lse posgrados revisó el archivo de Excel resultante, destacando la segmentación de textos (fragmentos) y la importancia de que el sistema de recuperación apunte a fragmentos de texto limpio y relevante, no al contenido sucio (00:41:05) (00:43:53).

Segmentación semántica vs. por página: lse posgrados explicó la diferencia entre separar documentos por página (fácil pero potencialmente impreciso semánticamente) y realizar una segmentación semántica (00:50:53). Se recomendó utilizar expresiones regulares para identificar contenidos específicos (como títulos o secciones) y fragmentar el texto basándose en su significado, lo que mejora la calidad de la respuesta del sistema de recuperación (RAG) (00:47:17) (00:52:21).

Presentación de J.Pablo Zebraitis sobre tickets: J.Pablo Zebraitis compartió su plan de trabajo, que consiste en transicionar desde el análisis de capturas de pantalla de WhatsApp a la ingesta de datos del sistema de gestión de tickets Redmine (00:56:34). El objetivo es identificar variables, realizar un análisis exploratorio y alimentar un sistema de recuperación basado en reglas de decisión validadas con el equipo de soporte operativo (00:57:45).

Proceso de ingesta de datos de Redmine: J.Pablo Zebraitis detalló el proceso de extracción de datos del sistema Redmine correspondientes a los años 25 y 26 a través de la Interfaz de Programación de Aplicaciones. Estos datos fueron descargados como archivos en formato Markdown y posteriormente transformados en un archivo JavaScript Object Notation para normalizar la información, incluyendo imágenes que fueron ajustadas a una estructura consistente (00:58:56).

Exploración de Análisis de Datos (EDA): J.Pablo Zebraitis compartió la realización de una Exploración de Análisis de Datos, tras iterar a través de cuatro versiones para refinar los resultados. La etapa inicial automática no fue efectiva debido a la inclusión de variables irrelevantes, como casos de soporte mezclados con funciones o errores, por lo que se implementaron filtros para aislar los datos pertinentes y excluir actualizaciones que no aportaban valor al objetivo de clasificar casos para una resolución más ágil (01:02:09).

Clasificación mediante modelos de lenguaje: Para abordar la falta de etiquetas en el corpus original, J.Pablo Zebraitis empleó un modelo de lenguaje para realizar una interpretación semántica del texto. Esto permitió categorizar los casos por tema, integrando reglas de dominio específicas para mejorar la precisión y evitar interpretaciones erróneas, estableciendo un sistema progresivo para la identificación de casos (01:03:19).

Análisis del Acuerdo de Nivel de Servicio (SLA): A través de la exploración, J.Pablo Zebraitis identificó una discrepancia significativa entre el Acuerdo de Nivel de Servicio declarado manualmente por los operadores y el tiempo real transcurrido entre la apertura y el cierre de los casos. Se descubrió que solo el 30% de las clasificaciones manuales coincidían con la realidad, y que muchos casos marcados como "no aplica" correspondían a tiempos de resolución superiores a 30 días (01:04:21).

Gestión de datos y calidad de entrada: lse posgrados y J.Pablo Zebraitis discutieron la importancia de que el personal operativo comprenda el valor de los datos que ingresan al sistema, sugiriendo que la visibilidad de estos resultados podría mejorar la calidad de las futuras entradas. J.Pablo Zebraitis enfatizó la relevancia de automatizar estos procesos para asegurar que la trazabilidad refleje la realidad operativa del soporte (01:06:28).

Hallazgos adicionales en la exploración de datos: J.Pablo Zebraitis identificó que los usuarios tienden a clasificar la mayoría de los temas como "normales", sin visualizar urgencias en las categorías. Además, se aplicaron filtros para comparar el origen de los casos, diferenciando si fueron iniciados por el equipo de soporte interno o por los clientes, permitiendo una visión detallada del comportamiento del sistema (01:08:24).

Recomendaciones pedagógicas y logística de tutoría: lse posgrados felicitó a J.Pablo Zebraitis por la aplicación de las herramientas sugeridas y alentó a los demás participantes a experimentar con modelos de inteligencia artificial para la generación de tableros, destacando la importancia previa de organizar bien los datos. Marcelo Luna indicó que enviará materiales por correo electrónico para ser discutidos en la sesión de mañana, la cual se dividirá en una parte expositiva y otra de interacción (01:10:07).

Revisa las notas de Gemini para asegurarte de que sean precisas. Obtén sugerencias y descubre cómo Gemini toma notas

Cómo es la calidad de estas notas específicas? Responde una breve encuesta para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.

📖 Transcripción

13 may 2026

Taller de trabajo final (3/8) - d015b25 - Transcripción

00:00:00

lse posgrados: Buen día. Va. Buenas noches.
Gabi Tallarico: Buenas tardes. Entonces,
lse posgrados: ¿Cómo están?
J.Pablo Zebraitis: Buenas tardes.
Gabi Tallarico: bien.
lse posgrados: Qué bueno.
J.Pablo Zebraitis: llegando.
Gabi Tallarico: Sí,
lse posgrados: Un
Gabi Tallarico: sí. No,
lse posgrados: ratito.
Gabi Tallarico: no son ni las 7 todavía, faltan 2 minutos.
Marcelo Luna: Hola. Hola.
lse posgrados: Hola.
Gabi Tallarico: Marc, ¿cómo va todo?
Marcelo Luna: ¿Cómo andan?
Gabi Tallarico: Muy
lse posgrados: ¿Qué hacemos? Bien,
Marcelo Luna: Bien.
lse posgrados: Pablo, ayer recibí el correíto.
Gabi Tallarico: H
lse posgrados: Eh, ¿será posible que me mande los MD directamente para que los lea? Porque por ahí tengo que descargar el SIP, ¿viste? me es más fácil que me mandes un Word o un zip, perdón, que me mandes un Word o algo así para que lo para que a ver, yo entiendo entiendo la arquitectura y está buenísima,
J.Pablo Zebraitis: No.
lse posgrados: pero por ahí no no creo que me pueda meter a ver exactamente todo el detalle, pero sí por ahí la interpretación del del text.

00:01:19

J.Pablo Zebraitis: No sé si escucho porque el llegando ahora
lse posgrados: Sí, te escucha.
J.Pablo Zebraitis: escuchaste bien el tema el siguiente.
lse posgrados: Sí.
J.Pablo Zebraitis: Sí, si no hay ningún problema. Lo que te mandé fue apelando a la herramienta que tú mostraste, toda una estructura en la herramienta que tú mostraste eh con todos los gráficos.
lse posgrados: Claro.
J.Pablo Zebraitis: fue lo que te mandé todo y querés después como ejemplo lo que fuera,
lse posgrados: Ah, okay. No, no, entonces no,
J.Pablo Zebraitis: pero te mando
lse posgrados: no. Entonces, por ahí.
J.Pablo Zebraitis: el
lse posgrados: Okay, entonces el zip si yo lo descomprimo y lo abro con estudio, ya lo puedo ver bien.
J.Pablo Zebraitis: tenés podés también si corres con Python la
Marcelo Luna: Oi,
lse posgrados: Perfecto.
J.Pablo Zebraitis: aplicación tenés este los dashw que te dicen de varias imágenes de varios gráficos y todo lo
lse posgrados: Debería, debería
J.Pablo Zebraitis: demás mandé por eso, compri por eso. Vale.
lse posgrados: buenísimo. Yo lo voy a lo voy a ver e por ahí, digamos, e para para todos la la solución de de Pablo es bastante más orientada a, digamos, a un desarrollo de producto final, pero en el fondo es lo que estamos haciendo, digamos, ¿no?

00:02:28

lse posgrados: O sea, en lo teórico y en lo conceptual es lo mismo, pero quizás más pensado en una solución ya eh digamos terminada o casi terminada. Eh, y estaría bueno, Pablo, que en alguna de las sesiones, no sé si en la próxima te prepares un ratito, no sé, 15, 20 minutos y la expliqués, ¿viste? Eh, porque por ahí estamos estamos en distintas fases de desarrollo de de distinto. Me refiero a Sebraitis, a Juan Pablo Cebraitis igual Pablo, Juan Pablo Rueda, Dale Gabo también si queré.
Juan Pablo Rueda: M.
lse posgrados: E pero nada, buenísimo, Juan Pablo, ahí preparado. Yo creo que para la clase que viene sería bueno empezar. Yo lo voy a revisar, igual te voy a dar un poquito de feedback de eso en, no sé, hoy o mañana y para la próxima, porque está bueno que mostré también cómo ella la habla cuando uno aplica todo esto como un producto casi final, digamos,
J.Pablo Zebraitis: Eh, sí, inclusive junté ahí varios casos porque hice como tres rondas de investigación, eh, más allá de ampliar el scope para tener mandatos iniciales.
lse posgrados: Mhm.
J.Pablo Zebraitis: Sí, pero dice como tres rondas de investigación sobre los primeros pasos de de cierta exploración que hice y dos tres pasos más para definir mejor el negocio, las métricas, las variables.

00:03:49

J.Pablo Zebraitis: Eh, y bueno, ahí lo digo, lo digo un poco en el que vas a chao. Okay.
lse posgrados: De una, de una. Ah, bueno, la idea de esta semana a raíz también de los comentarios que que recibí eh es eh tener tutorías, ¿no? Ayer hubo una eh con algunos grupos y algunas situaciones, digamos, algunos casos. Eh, la idea de hoy es continuar y mañana hay otra planteada con otro grupo. Entonces, la de hoy va a ser cortita la clase. Sí, me gustaría que si hay gente que tiene dudas la hagamos así a modo como ya ya lo hice ayer. Así seguimos aplicando. Pero antes de eso voy a dar un resumen de lo que de lo que vimos ayer rapidito con con los grupos. Eh, ayer mandé un video en una aplicación que no sé si todos pudieron ingresar, a veces te pide loguear. Más fácil la voy a descargar. y la subo al Drive, así todo puede ingresar, menos lío, digamos. Esa aplicación está buena porque te te graba la clase, o sea, te graba lo que vos hacés, te hace un resumen, etcétera.

00:04:53

lse posgrados: Voy a bajar el resumen y la clase. Son prácticamente dos, casi dos horas que hemos estado interactuando ahí con con los grupos y así les queda también para que la revisen. Seguramente va a dar algún tipo de solución a a alguno algún otro grupo más. Bueno, ahí voy ahora a compartir pantalla y avíseme cuando se vea. Ya se ve. Perfecto. Buenísimo. Eh, un poco el cuál es el el cuál es el pipeline o cuál qué es lo que estamos trabajando nosotros eh desde el inicio. Sí, voy a hacer un breve resumen porque quiero utilizar más el tiempo con con los otros con los otros casos. Eh, lo primero que hemos hecho en la clase uno ha sido definir, plantear la pregunta o o qué, hacia dónde vamos, digamos, ¿no? ¿Cuál es la cuál es la pregunta que queremos responder? Un profe siempre en ingeniería, en la universidad que me decía, bueno, todo empieza con una pregunta, todo empieza con una pregunta. Entonces, nuestro desarrollo siempre va a responder esa pregunta. Sí, esto por digamos traducido a lo que hemos hecho en la clase uno es el canvas, ¿no? Donde básicamente hemos reducido bastante alcances de algunos grupos.

00:06:15

lse posgrados: Eh, hemos alineado más o menos qué es lo que entra, qué es lo que sale, qué es lo que pretendemos, algunas cuestiones relacionada a los costos y a los beneficios y a los actores clave, digamos, ¿no? En esta fase inicial, por ahí, cuando uno va planteando una idea o o cuando va planteando un proyecto, los actores todavía no intervienen tanto hasta que ya pasan a etapas más antes de empezar una usabilidad. Por eso no lo tocamos mucho ahora. ¿Cuál es? Hay forma y hay metodologías especiales para trabajar con stakeholder o con o digamos yo, por ejemplo, trabajo en minería y en minería hay un formulario de basado en la metodología que se llama Lean de excelencia operacional donde cuando vos querés hacer un cambio tenés que seguir una serie de pasos. Una de esas partes de los pasos es censar a los stakeholders o a los digamos a las personas que va a estar relacionada con el cambio que vos estás por implementar para evitar problemas, digamos. Bueno, no viene el caso, pero bueno, eh también deberían deberían pensarlo en una etapa más avanzada. La segunda clase hemos estado más en la cuestión de EDA. Sí. Eh, nosotros hemos pasado directamente de plantear la pregunta a hacer una exploración y mostrar gráfico, etcétera.

00:07:32

lse posgrados: Lo que realmente corresponde y quizás fue un error mío, eh, fue saltearme dos dos pasos que yo lo di por como por entendido, eh, pero que no viene no viene mal repasarlos. El primer paso es la ingesta. La ingesta de los datos es sumamente importante, básicamente meterlos dentro de nuestro sistema. Casi todos están usando Colab o algún otro sistema. Eh, digamos sistema, me refiero a cuál va a ser el motor que van a usar ustedes para hacer la limpieza. Eh, en este caso estamos usando colab, ¿cierto? o la mayoría está usando colab, pero abajo siempre hay un Python, etcétera. Bueno, esta acá la parte ingesta debería haber funciones que lo que hacen es eh toman un dato crudo y devuelven un dato ya ingestado, por así decirlo, ¿no? Esta parte es importante y como les dije la la clase pasada, por ahí todo lo que se haga es, por ejemplo, una función debería ser solamente una tarea. No podemos hacer ingesta y limpieza. en en una en una sola función. Entonces, eso también para que vayan viendo, porque he visto colabo sé que están están iterando los colab traten de separar ingesta de eh limpieza.

00:08:46

lse posgrados: Entonces, cuando sé que todos y yo también lo uso, cuando proménen a la IA, pídanle que separe claramente las funciones de ingesta y de limpieza y que no ponga todo en un solo en una sola función. si no nos estamos perdiendo, ¿qué es lo que pasa en el medio, si estamos ingestando los datos? Bien, por ejemplo, doy doy doy un ejemplo que surgió ayer eh ayer durante la clase e creo que esto está con eh crear una copia, por eso no me deja ah no me deja evitarlo. Eh ayer durante la clase surgieron cosas de, por ejemplo, la ingesta. un un le doy un ejemplo. Si le ingesta eh el texto en vez de en vez de decir eh te acordas, Gabi, que que estaba al revés,
Gabi Tallarico: Sí, que lo escrib vez como un
lse posgrados: digamos, al revés. Bueno, ¿qué problema escribir al revés? Por ejemplo,
Gabi Tallarico: espejo.
lse posgrados: si de repente la ingesta traía eh debería traer eh no sé, la palabra captura, la ingesta quizás está trayendo la palabra al revés. Ah,
Gabi Tallarico: Creo que eran todos los pies de página que estaban invertidos.
lse posgrados: claro,

00:10:01

Gabi Tallarico: Difícil es escribirlo si no ten el espejo.
lse posgrados: listo. Entonces, digamos, si si uno no separa, digamos, lo que debería ingresar sería captura, pero me está me está ingestando esto. Si yo no tengo algo para ver acá, básicamente un print, eh, me está ingresando esto. Yo ya estoy pasando la función de limpieza y aleda sin limpiar. y esto no lo acá no hizo acá esto no es interpretable esto entra al modelo, el modelo puede fallar, no está tomando esto no va a formar parte del contexto del contexto porque nada no tiene sentido.
Gabi Tallarico: M.
lse posgrados: Entonces lo ideal lo ideal es que cada fase, cada función que tengan ustedes en el colab o en el trabajo que están haciendo tenga una algo que te permita ver. Entonces, eh de repente eh eh si yo voy a tener la ingesta, ¿sí? Vamos a hacer una un cuadrito. Si yo hago directamente la ingesta, ¿sí? Yo en en algunos casos lo he visto y y en otros no, sí, pero si yo la entrada, voy a poner un un caso particular. Si la entrada es un PDF, sí, el PDF va a ingresar a la función de ingesta. Sí. Y de la función de ingesta va a salir, ¿qué es lo que sale de la función de ingesta?

00:11:24

lse posgrados: Un texto. Sí, o sea, entra un PDF y sale un texto. Ahora, ese texto, ¿cómo administran ese texto? Ese texto puede ser un texto por página, un texto por párrafo, un texto por chonk, un texto por título del documento, un texto por lo que ustedes consideren, digamos. Entonces, digamos que acá en esta fase eh es importante que ustedes conozcan el negocio. Sí. O sea, ¿qué es lo que están haciendo? ¿Qué es lo que estamos haciendo? Estamos si el PDF tiene también lo hemos visto ayer en un caso, si tiene si el PDF introducción eh intro eh típico metodología, sí, eh resultado, conclusiones, quizás yo quisiera tener un texto por intro, un texto por metodología, un texto por resultado y un texto por conclusiones y las tablas por aparte, por ejemplo. Eso es en un caso o cada uno tiene su caso, digamos, ¿no? Entonces, dependiendo de cómo entra este PDF, es la cantidad de textos que yo voy a sacar. Ahora, al texto, dentro del texto, estamos hablando de la ingesta. Dentro del texto también lo puedo decir. No, yo no quiero tener archivos punto txt porque voy a tener, supongamos que sera, este, sería el archivo txt txt.

00:12:43

lse posgrados: Listo. Se guarda así dentro del sistema de archivo de colabo del que estoy manejando en local. Y así si yo tengo cinco, voy a seguir sumando la x cantidad de txt y bueno, después voy a tener que crear una función que vaya iterando y y abriendo cada uno de estos. Esa es una forma me parece esto, a m me parece super prorijo a mí. Eh, ahora yo le doy la libertad a ustedes también de que lo puedan hacer con un formato de tabla. Sí. Entonces, en una tabla eh seguro pod insertar alguna tabla. En una tabla podremos tener la ingesta donde tendremos que tener el ID del documento de ID del documento. Sí. Entonces acá será eh, no sé, intro.pdf, ¿sí? El identificador del documento. Eh, y acá quizás ya directamente el texto. Sí. Okay. Acá el el texto ya debería ir. Sí. Acá ya directamente vendría el el texto. Sí. Y acá todas las cantidad de información que ustedes quieran ingresarle al texto que puedair llegar a servir para ustedes, pero también le quiero dar esa opción, o sea, pueden hacerlo así y después una función que vaya tomando todo lo txt o pueden tener esto que es exactamente

00:14:00

Gabi Tallarico: Ah.
lse posgrados: lo mismo, nada más que eh por ahí es más eh es más e no sé, más práctico a la hora de usar un colab. ¿Por qué? Porque colap a esto lo vas a a esta ingesta la vamos a tener como eh a esta ingesta la vamos a tener como
Gabi Tallarico: No.
lse posgrados: un archivo de tipo eh generalmente punto CSB, ¿sí? O sea, lo exportamos como un CSB. Y acá truco para para muchos que si que seguramente lo están haciendo así, esto será un punto CSB. Cuando ustedes hagan la celda, lo que conviene es que todo este proceso que está acá de ingesta, separación, etcétera, no lo corran cada vez que cada vez que terminó la ingesta. Entonces, en CSB, esto sean los TXT o el CSB, mi recomendación es que lo manden directo al Drive, ¿sí? a un sistema ya al Google Drive o algún sistema local que se puedan conectar para que después la cuando tengan que correr el colab, si es que están trabajando con mucho archivo, etcétera, eh directamente el colab va se le va a pegar al drive y ahí va a seguir y ya no va a ser esta. Entonces pueden hacer esta una sola vez y una vez que tienen todo esto respaldado en drive del del drive, digamos, de esa celda en adelante, ya corre normal la conexión al drive, trae los archivos y comentan las celdas de arriba.

00:15:35

lse posgrados: ¿Para qué? Para que cuando corran todo de nuevo, estén más adelante en el desarrollo no tengan que volver a pasar por esto. ¿Eso quedó claro?
Gabi Tallarico: Sí,
lse posgrados: Sí.
Gabi Tallarico: a mí me quedaba ahí una pregunta ahí justo con la ingesta, por ejemplo,
lse posgrados: Bueno,
Gabi Tallarico: si tenemos como fuentes PDF por un lado y no sé, archivos X LS, qué s yo tablas de Excel, muchas ahí tienen que ser siempre dos funciones por separado.
lse posgrados: yo creo que sí, digamos, los textos lo va a procesar así. Yo, en tu caso particular, lo que tiene Gabi es un PDF, tiene pedazo de texto que tiene muchísima información interesante o que se puede usar para responder preguntas y de repente bloques de imágenes que las sacas, pero te quedas con las tablas que también son difícil de procesar. Entonces, eh, digamos,
Gabi Tallarico: Es otra función hacer otra
lse posgrados: yo creo que sí, exacto. Y separa las tablas, digamos,
Gabi Tallarico: que ya las tenemos separadas,
lse posgrados: vos va a tener
Gabi Tallarico: ¿no? Porque después aparte ahí charlando también digo,
lse posgrados: Claro.
Gabi Tallarico: en algún momento vamos a tener que hacer también una ingesta de imágenes que no van a ser las que están en ese PDF, pero si no vamos a construirla, ¿no?

00:16:52

Gabi Tallarico: Para este trabajo, no te asustes.
lse posgrados: ¿Cómo hace
Gabi Tallarico: No sé cómo lo vamos a hacer, pero está bueno pensar qué es lo que tenemos que hacer en algún momento del día, del
lse posgrados: otra? Claro, otra otra posibilidad de armar un Jason.
Gabi Tallarico: año.
lse posgrados: Ya, el Jason lo que vendría a ser en vez de tener el CSB, digamos, o en vez de tener todo esto que está acá, entonces voy directamente eh un paso previo sería y acá ya vamos
Gabi Tallarico: Sí.
lse posgrados: entrar un poquito más más en el caso, dependerá de cada uno, ¿no? Y acá podemos meter un Jason y el Jason son básicamente llaves diccionarios que van ingresando información.
Gabi Tallarico: Mhm.
lse posgrados: Entonces, un posible Jason que pueden trab. Entonces, una una un campo será ID eh ID del documento, ¿sí? ID del documento y acá obviamente el clave valor y del documento intro. PDF. Sí.
Gabi Tallarico: Sería como la tabla construida ese
lse posgrados: Y, claro, exacto.
Gabi Tallarico: Jason.
lse posgrados: Pero lo bueno que tenés vos tenés ese ID del documento, eh, y acá le mandas directamente cuál es el contenido del texto.

00:18:08

lse posgrados: Estoy haciendo un Jason simplificadísimo,
Gabi Tallarico: Sí,
lse posgrados: ¿no?
Gabi Tallarico: sí.
lse posgrados: Florem Y. Sí. Y acá si vos tenés acá le acá ya podés linkear las tablas. Sí. Y como esto es una mamuska de, digamos, de cosas que le podes meter y está bueno porque los sistemas lo leen sencillamente al Jason, eh, entonces se ve. Acá ya podes de nuevo meter más, digamos, ¿no? Entonces acá a podes meter varias tablas. Acá pueden ingresar todas tus tablas en este diccionario acá.
Gabi Tallarico: Bien.
lse posgrados: Sí. Entonces si si los trabajas así y del flujo en adelante le este Jason de nuevo, no corras todo de nuevo, respalda el Jason en el drive. Entonces esta es una función intermedia que lo que hace es une todo esto, ¿sí? Esto y lo convierte en un Jason y ya lo tenés en el drive y después lo que va a hacer es vos va a tener que Colab se va a conectar al drive y va a seguir con la fase de limpieza. ¿Sí? O o quizá ahora pensándolo bien, eh, bueno,
Gabi Tallarico: Sí,
lse posgrados: no,

00:19:15

Gabi Tallarico: ya está limpio el el Jason.
lse posgrados: yo yo no puedas todo acá y este texto esté sucio
Gabi Tallarico: A lo mejor.
lse posgrados: todavía y voy acá extraer cosas y después digamos eh en
Gabi Tallarico: Ah,
lse posgrados: realidad te doy otro. Mira, entonces vos directamente le ponés otra función acá y por ahí vos decís, "Bueno, pero no puedo seguir encadenando funciones." Créeme que así es como se trabaja. O sea, no sé por qué,
Gabi Tallarico: yo te recreo,
lse posgrados: pero así se trae trae mucho orden esto.
Gabi Tallarico: eh, todo lo que digas.
lse posgrados: Entonces acá directamente el txt acá el tt ra, digamos este el texto que como venía el crudo y después va a tener el txt, el texto va directamente limpio. Entonces, está bueno esto.
Gabi Tallarico: Ah,
lse posgrados: ¿Por qué? Y acá ya vendrá eh ajo.com, qué sente tu caso. Ahora, eh, ¿por qué está bueno esto? Porque vos al hacerlo así como parcializado, o sea, función por función, vos vas viendo que es lo vas estás teniendo control de las funciones que están haciendo. Entonces, esto me parece fantástico hacerlo así.

00:20:21

lse posgrados: Cak ya va a tener el texto sucio, el texto limpio. En un solo Jason, abriendo el Jason va a poner el texto sucio,
Gabi Tallarico: Tenemos todo.
lse posgrados: el texto limpio,
Gabi Tallarico: No.
lse posgrados: si realmente la función está aplicando lo que vos buscas y de acá ya que sigan adelante. Y obviamente cuando vos tengas que seleccionar estos datos, le pegas, le apuntas directamente le apuntas a al texto limpio porque el texto suyo no te interesa, digamos. Sí, le apuntada a esta llave y a esta no la tomas, digamos. ¿Me entendés?
Gabi Tallarico: Perfecto.
lse posgrados: Pero lo tenés ahí. Bueno, eh, y acá seguíamos. Bueno, una vez que va la fase de limpieza, ya después eleda. Eh, acá creo que habían habían cosas, la mayoría de los grupos estaban haciendo cosas, me llegaron, revisé, están están buena. Alguno le diré alguna alguna notebook para que para usarla, pero en síntesis y la conclusión de lo que hemos hablado ayer es que eh al final del EDA debería haber una pregunta. si hace falta algún modelo eh para digamos para responder la pregunta inicial, quizá con una regla de decisión o quizás después del EDA no encontramos relaciones entre las variables que puede que permitan aplicar un modelo para responder la pregunta.

00:21:42

lse posgrados: Sí, bienvenidos y sí, pero si si no encontramos si tenemos que hacer un problema de regresión y de repente no encontramos eh relaciones o correlaciones entre variables, difícilmente lo podemos hacer. podemos intentarlo, pero capaz que no performa bien. Y después de esta pregunta, hay que decir, bueno, a ver, eh ese modelo puede ser un modelo eurístico basado simplemente en reglas de decisión, aplicando funciones, eh, digamos decir si es mayor, menor, sin aplicar modelos más estadísticos. Bueno, esta me gustaría que la apliquen igual si es que aplican en sus casos al menos si en EDA descubren que pueden separar o clasificar texto sin tener que aplicar eh un modelo tipo Llm para que clasifique o algún modelo tipo psych learning para que de machine learning para que lo haga. Bueno, buenísimo. Pero todo esto es aprendizaje, digamos. Acá ya viene la acá ya viene eh digamos lo que nosotros dónde aportamos valor nosotros digamos y dónde se aporta más donde se aporta muchísimo valor en esta fase en limpieza y en edad. La mayoría de los proyectos pasan de plantar la pregunta a meterlo en un modelo y ya directamente decir, "Bueno, performó, ¿peró no performó?" Digamos. Ahora, si esta fase eh digamos aporta valor, la el performance del modelo debería ser mejor, digamos, o al menos más prolijo también.

00:23:03

lse posgrados: Eh, ahora, ¿qué es lo que nos interesa a nosotros para la materia? Para la materia, a mí me interesa que planteen la pregunta, que hagan la ingesta claramente, que el proceso quede documentado de limpieza, que le da aporte conclusiones relevantes respecto a la pregunta. Sí. Eh, no no buscamos conclusiones que sean eh complejas, buscamos que algún gráfico aporte el entendimiento de la pregunta que estamos haciendo, ¿sí?, de esa exploración. Luego en las clases más adelante ya vamos a llegar a la parte modelado. Esta parte de urística va a depender si la eleda nos permitiría o no hacer algo de heurística. Quizás sí, quizás no, no lo sabemos. Y el primer modelo, sí, este que creo que este ya la versión cero ya la tienen hecha y lo que hicieron las materias anteriores. Ahora todo esto va a ser nuevo y este modelo ya va a pasar a un modelo más limpio. No debería, quizás no performa, pero aún así es el aún así es aporte, aunque es una conclusión. Eh, y ahí cerramos, digamos. Ese sería como el el la historia del cuento con el documento y documentada eh la mejora. Y ahí viene un punto importante que suele pasar que cuando uno va escribiendo, haciendo, el proyecto, parte del modelo va se va perdiendo las primeras fases.

00:24:28

lse posgrados: ¿Por qué? Porque yo ya hice eleda, ya cambié el código y y y no me daba bien la limpieza. Me interesa que al menos un ciclo de esto quede documentado.
J.Pablo Zebraitis: Yeah.
lse posgrados: Si al principio entró el texto así y el modelo daba mal o daba bien o esta métrica. Eh, y después de la limpieza esto está funcionando de esta manera. Es esa documentación me interesa. Y hasta ahí llegamos, digamos, ¿no? Eh, bueno, eso fue básicamente lo que lo que hemos hablado ayer con con los grupos. Eh, ahora lo que queda, eh, me gustaría que si tienen dudas o si alguien quiere plantear su situación y y la vamos viendo ahí con entre todos y y aprovechamos. La clase de hoy va a ser corta, chicos, porque también obviamente estamos estoy interviniendo en otras horas. Mañana también tenemos eh tutoría, entonces la idea de lo que queda, digamos, la quizás los 40 minutos que queden es usarlo para eso. Sí. ¿Quién quién se anima,
Marcelo Luna: Yo tengo una pregunta,
lse posgrados: Marcelo?
Marcelo Luna: Cristian, ahí, eh, digo, con respecto a lo que mirabas recién, a lo que mostrabas recién, eh, vos mostrabas recién primero la ingesta y después la limpieza.

00:25:44

Marcelo Luna: Sí. Y y me pregunto si no en algún caso no cabe al
lse posgrados: Exacto.
Marcelo Luna: revés, no puedo hacer primero el proceso de limpieza y después la ingesta.
lse posgrados: No, o sea, digamos, dependiendo depende del caso.
Marcelo Luna: Claro.
lse posgrados: El texto siempre va a entrar como un texto crudo. Sí.
Marcelo Luna: Sí,
lse posgrados: Sin
Marcelo Luna: pero hay, perdón,
lse posgrados: limpieza.
Marcelo Luna: que te interrumpa, pero justamente lo que estaba pensando, por ejemplo, en mi caso, yo yo no tengo una gran cantidad de documentos que ingestar, tengo pocos documentos, pero los tengo que pero tengo que hacer la ingesta con cierto criterio y cierta estructura. Y para poder definir en y entender esa estructura, necesito separar cosas. Por ejemplo, el prefacio de las reglas de navegación a vela no me interesa, ¿entendés? Entonces, previo a la ingesta, yo tengo la posibilidad de decir,
lse posgrados: Ah.
Marcelo Luna: "Che, okay, tomá todo lo que no sea esto y tomalo con esta estructura y ahí no estoy haciendo un poco de limpieza previo a la ingesta.
lse posgrados: Sí, lo que yo haría sería meter todo el texto y después sacar lo que no me sirve porque ahora no te sirve. Sí,

00:27:06

Marcelo Luna: Sí.
lse posgrados: sí, porque ahora no te sirve. y y y si después te sirve o si después lo va lo va a tener que volver atrás y cambiar el
Marcelo Luna: Okay.
lse posgrados: flujo. Pero de nuevo, esto depende de cada caso. Ahora, si vos me decís, "Bueno, yo, por ejemplo, si yo quiero cuando hago la limpieza, me salteo la página uno a cinco porque no tiene información, digamos." Sí,
Marcelo Luna: H.
lse posgrados: obvio. Ahí sería una una ingesta limpia, por así decir,
Marcelo Luna: Ok.
lse posgrados: entre comillas. Eh, está bien, digamos, ¿no? Pero la la ingesta lo que busca es que entren los datos de forma cruda.
Marcelo Luna: Ok.
lse posgrados: Entrando los datos de forma cruda, a vos te va a permitir tener toda la información y después seleccionar qué información es relevante y qué no para este caso. Sí. Y además eh creo quizás tengas más control visual respecto de lo que ingresa y de lo que lo que estás limpiando, digamos,
Gabi Tallarico: Eh, si estás trabajando conductos estructurados también sería primero ingesta y después
lse posgrados: ¿no?
Gabi Tallarico: limpieza.
lse posgrados: Sí, sí,

00:28:07

Gabi Tallarico: Poner
lse posgrados: siempre es casi es casi regla eso. Hay excepciones, hay excepciones.
Gabi Tallarico: Ah.
lse posgrados: Como por ejemplo lo que digo, yo no voy a meter en cuando leo un PDF, quizás la portada y dos páginas más adelante no me sirven de nada. Entonces, ¿para qué la voy a meter? Okay, sí, e es una engesta más limpia, digamos, ¿no? Pero después el paso de limpieza va a venir igual porque va a tener que sacar minúscula.
Gabi Tallarico: No.
lse posgrados: Lo que está tratando de de ordenar es que no no meter más de más de una o dos tareas en una función. Sí. eh para que tengan para que sea un proceso más limpio cuando cuando trabajen o si tienen la posibilidad de trabajar por ejemplo
Marcelo Luna: H
lse posgrados: en haciendo pipeline en airflow, se van a dar cuenta o es airflow en un sistema donde uno va haciendo pasito a pasito, digamos, ¿no? Cuando uno mete dos tareas dentro de una sola función, cuando voy y termino todo el pipeline y después quiero cambiar algo, es bastante difícil de entender, ir hacia atrás, digamos, ¿no? Cuando uno que después quiere empezar a corregir es complejo, hay excepciones, tampoco es una regla de oro, decir una tarea, una función, pero traten de minimizar las tareas en la función, básicamente.

00:29:22

lse posgrados: O sea, para responderte, Marcelo, sí puede hacer una ingesta limpia,
Marcelo Luna: Ok.
lse posgrados: pero el la fase después de limpieza la va a tener que ser igual. Separala, separala.
Marcelo Luna: Oh,
lse posgrados: Esa ingesta limpia puede ser eliminar página,
Marcelo Luna: no.
lse posgrados: eliminar algún contenido que no te sirva, que vos tengas claro que no te va a servir. Lo que no puede tener es ingestar y sacar acento, sacar minúscula, eh acomodar un poco el texto, eh etcétera. Eso todo eso junto, no no no, porque le va a perder, le va a perder visualización a lo que va haciendo,
Marcelo Luna: Okay.
lse posgrados: Juan Pablo. Sí.
Juan Pablo Rueda: Sí, profe, yo en el caso mío e bueno, justamente hice un Excel y ahí empecé a cargar las los datos de los de los productos. Sí, o sea, porque todos los productos tienen una serie de íem que son los mismos para todos, nada más que cambian algunos valores. Por ejemplo,
lse posgrados: A ver,
Juan Pablo Rueda: humedad máxima,
lse posgrados: mostra pantalla y podes mostrar pantalla y lo vemos.
Juan Pablo Rueda: energía.
lse posgrados: Así lo lo entendemos un poquito mejor.
Juan Pablo Rueda: Y se ve algo.

00:30:48

Marcelo Luna: Sí.
lse posgrados: Ahí está. Buenísimo.
Juan Pablo Rueda: Bueno,
lse posgrados: Ah,
Juan Pablo Rueda: eh eh es esas son las etiquetas.
lse posgrados: el caso de lo
Juan Pablo Rueda: Esa,
lse posgrados: de
Juan Pablo Rueda: a, esas son las etiquetas como como las manda el nutricionista de la de la de la firma. Sí, yo una de las primeras pruebas que hice en el en el colab es cargando tres o cuatro
lse posgrados: Sí.
Juan Pablo Rueda: PDFs así y la verdad que después hice otra prueba cargándolo así se ve y mejoró muchísimo, o sea,
lse posgrados: Okay.
Juan Pablo Rueda: la la respuesta
lse posgrados: Ahora, mira, si lo que te podría decir así,
Juan Pablo Rueda: está.
lse posgrados: eso vos lo hiciste manual, ¿no es cierto? Así como le ordenaste.
Juan Pablo Rueda: Sí,
lse posgrados: Perfecto. Ahora, lo que quizás te conviene intentar y digamos es eh tratar de encontrar
Juan Pablo Rueda: sí.
lse posgrados: algún prompt, ¿sí? Promptear una función porque ya tenés vos clara tu entrada y cómo lo querés de salida, que es esto que tenía acá. Eso ya sería casi limpio. Ahora lo que faltaría sería che,

00:31:50

Juan Pablo Rueda: Sí.
lse posgrados: si me ingresan 20 documentos más, no tengo ganas de hacer de nuevo esto.
Juan Pablo Rueda: Claro. Sí. Es que en realidad son muchos productos
lse posgrados: Bueno,
Juan Pablo Rueda: más
lse posgrados: pero lo que vos ya tenés claro lo cómo lo querés y cómo entran, lo que te tenés que promptar y encontrar una función en que x cantidad de pasos
Juan Pablo Rueda: bien.
lse posgrados: ingrese un PDF y te devuelva esto que tenés acá. Sí. Eh, hacer una cosa, mandame un PDF y esa tabla. Yo te voy a ayudar a encontrar esa función, pero buscala vos también, digamos, ¿no? O sea,
Juan Pablo Rueda: Bien.
lse posgrados: yo lo que voy a hacer es voy a abrar cloud, voy a buscar un decir, mira, tengo este ingreso y que lo quiero así y alguna que otra más cosa más que decía, separarme la energía eh metabolizante, usar funciones ta ta ta ta, y alguna cosita más y y me empecé a iterar a decir, no lo voy a escribir, digamos,
Juan Pablo Rueda: Bien,
lse posgrados: pero sí lo sí lo queía encontrar sería una función entre entre lo que vos ya querés,
Juan Pablo Rueda: bien,
lse posgrados: porque ya tenés claro cómo lo queres ingestar y eso, cómo te viene, digamos, ¿sí?

00:32:50

lse posgrados: Eh, y cuando la encontrés después la teste con algunos PDF extra y si es así,
Juan Pablo Rueda: Bien,
lse posgrados: bueno, golazo, ya la tenés, digamos, ¿me
Juan Pablo Rueda: bien, bien.
lse posgrados: entendés?
Juan Pablo Rueda: Y en el caso que yo quiera combinar, porque esta sería como una parte la parte más estructural del del producto en sí, pero después yo lo que quiero agregar es es eh, ¿cómo serían? las las estrategias, por ejemplo, de engorde, que eso en realidad es es un proceso que lo tengo que ver primero con los veterinarios de la marca, de la firma.
lse posgrados: Claro.
Juan Pablo Rueda: Ellos me tienen que eh dar cuáles son las estrategias que ellos le comunican a los productores que que actualmente se las comunican de forma verbal yendo al campo. Eh, ¿me explicó?
lse posgrados: y pero y busca busca,
Juan Pablo Rueda: O sea,
lse posgrados: no sé, 10 estrategias eh sintéticas
Juan Pablo Rueda: técnicas.
lse posgrados: sintéticas.
Juan Pablo Rueda: Ah, bien inventadas.
lse posgrados: Claro, claro. O sea, esto es,
Juan Pablo Rueda: Sí, sí,
lse posgrados: digamos,
Juan Pablo Rueda: sí. Okay,
lse posgrados: ¿no?
Juan Pablo Rueda: okay,

00:33:56

lse posgrados: Y cuando vos tengas un documento que sería estrategias jason,
Juan Pablo Rueda: okay.
lse posgrados: por ejemplo, o tu tabla de estrategias e son inventadas, sí, son sintéticas,
Juan Pablo Rueda: Bien, bien. Claro,
lse posgrados: pero en el momento Claro.
Juan Pablo Rueda: por ahí me estoy bien.
lse posgrados: En el momento en el que vos
Juan Pablo Rueda: Estoy li mucho al al producto final,
lse posgrados: Pues
Juan Pablo Rueda: a la respuesta final, porque en realidados,
lse posgrados: no, claro.
Juan Pablo Rueda: por ejemplo, al tener una una, a ver, el bobino engorde al 10% no es el mismo el bovino engorde que tiene otra marca,
lse posgrados: Oh.
Juan Pablo Rueda: entonces a lo mejor ellos tienen una cierta cantidad de relaciones diarias, semanales, mensuales, para que genere un efecto y bueno, pero sí, sí me estoy me Estoy limitando en la respuesta real final. Lo podría hacer con un ejemplo.
lse posgrados: Sí. O sea, de nuevo, digamos, en tu estrategia, esto es estratégico.
Juan Pablo Rueda: Fictísimo.
lse posgrados: ¿Por qué? Porque vos, por ejemplo, eh vos detectas que eso aporta mucho valor. Si la estrategia aporta valor en mi respuesta, en lo que yo busco responder.

00:34:59

lse posgrados: Sí. Ah, pero no, hasta que no tenga la verdadera no puedo terminar p no avanzar. Si es estrategia.
Juan Pablo Rueda: Bien.
lse posgrados: Después lo que voy a hacer va a cambiar la estrategia, va a agarrar el texto real de estrategia. Sí. Entonces, en esa en esa en ese documento nuevo de estrategias que va a poner, trata que e su contenido sea distinto,
Juan Pablo Rueda: Bien.
lse posgrados: o sea, que no sean que no sean cosas muy similares cuando lo hagas sintético, que sean muy contrastantes unas de otra para que cuando vos hagas el retrival te traiga una o la otra y no haga posibilidad de que haya dos que sean parecidas, ¿me entendés?
Juan Pablo Rueda: Ok.
lse posgrados: Ahora, esa es la primer versión. Después la vida real va a decir, "Bueno, de no sé si es eh una estrategia para una vaca, estoy tirando verdura, pero qué sé yo, para una vaca angus o para una vaca, no sé, lo que sea, para un guayu, qué sé yo." Y bueno, capaz que son similares, pero después lo probaba al retrival. Decí, bueno, voy a poner dos estrategias similares,
Juan Pablo Rueda: Bien.
lse posgrados: como en tu pipeline ya va a estar y simplemente agregar una fila más o una llave más en el Jason de la nueva estrategia parecida.

00:36:07

lse posgrados: Y bueno, entre estrategia parecida, realmente el retrabal trae la de la posta, ¿no? Entonces quizás tenés que poner alguna etiqueta o algún metadato que te sirva para que alimentar el retrival y y te seamos operativo, pero no busquemos todavía la excelencia en eso. Sí. Eh, sí que contenga estrategias sintéticas, digamos.
Juan Pablo Rueda: Okay, perfecto.
lse posgrados: ¿Alguien alguien más tiene algo para compartir, chicos? No tanto todo. ¿Cuántos somos, che? A ver, no me fijé.
Marcelo Luna: Vale.
lse posgrados: Bueno, bueno, a ver, eh, aprovechemos la Gabi, no sé si vos pudiste avanzar o vos, Shimon, entre ayer y hoy poco no creo que hayan podido
Shimon Ben: muy poquito.
Gabi Tallarico: Lorna trabajó en este equipo porque yo solo me dedico los sábados y domingos,
lse posgrados: avanzar.
Gabi Tallarico: los días de semana hago poco y nada. Lorna sí creo que estuvo haciendo,
lse posgrados: Bien,
Gabi Tallarico: me mandó ahí estoy viendo los emailes. ¿Estás lorna? Ah, muda,
Marcelo Luna: Mute.
Gabi Tallarico: ¿estás?
lse posgrados: está

00:37:27

Lorna Pons: Sí.
lse posgrados: muteada.
Lorna Pons: Hola, ¿qué tal? Buenas noches.
Shimon Ben: Yes.
Lorna Pons: Eh, sí, avancé con lo que hablamos ayer de hacer e una limpieza que yo la había salteado. La habíamos salteado, dice, la teníamos como para el fin de semana. Eh, hice una limpieza con algunos criterios y y lo hice por sección, que es lo que hablamos ayer, que yo lo he hecho por página.
lse posgrados: Claro.
Lorna Pons: Bueno, y lo hice así y quedó impecable.
lse posgrados: Y a ver, mostr veamos un poquitito. Dale,
Lorna Pons: Esperá que la busque que no tenía
lse posgrados: porfa.
Gabi Tallarico: No, el el Excel sí lo alcancé a mirar y está super
Lorna Pons: preparado. Ah, es ese. Dale,
Gabi Tallarico: claro, pero lo que me faltó que no llegué antes de la clase es ver la función que usaste para lograr eso.
Lorna Pons: Gabi.
Gabi Tallarico: El Excel está super bien ahora, mucho mejor de lo que teníamos,
Lorna Pons: Sí,
Gabi Tallarico: pero porque esa no
Lorna Pons: no, la función está por ahí.
Gabi Tallarico: la encontré. Claro,

00:38:29

Lorna Pons: No,
Gabi Tallarico: me volvé locaentré que yo entiendo
Lorna Pons: no te la mandé. No,
Gabi Tallarico: poco.
Lorna Pons: te mandé el Excel para que lo mires que había quedado lindo nada más.
Gabi Tallarico: No, no,
Lorna Pons: No i para no trabajar nada hoy era solo
Gabi Tallarico: no, no. Eso sí, sí alcancé,
Lorna Pons: eso.
Gabi Tallarico: alcancé.
Lorna Pons: Así que si la tenéis ahí a mano, o sea, digo que quedó linda comparada con la otra, ¿no? Que tenía como
Gabi Tallarico: Ahí
Lorna Pons: eh lo hice con
Gabi Tallarico: voy.
Lorna Pons: un glosario porque yo trabajo con el charge, estoy trabajando con el chat pt y me lo sugirió como me pareció una buena idea. Si alguien pregunta, ¿qué es tal cosa, Gabi, del ajo, por ejemplo,
Gabi Tallarico: Bien.
Lorna Pons: pero si preguntan algo específico es por eso que hay un glosario para que pueda
lse posgrados: A
Gabi Tallarico: Bueno, no sé si se alcanza a
Lorna Pons: contestar,
Gabi Tallarico: leer,
Lorna Pons: ¿no?
lse posgrados: ver,
Lorna Pons: Lo que se ve es lo de ayer que vimos el No,
Gabi Tallarico: pero esto es lo que me pasaste hoy.

00:39:19

Lorna Pons: T
Gabi Tallarico: Estos textos están mucho mejor, todos estos chan.
lse posgrados: se se ve el Excel de seguimiento de ajuste,
Shimon Ben: Sí.
lse posgrados: Gabi. Capaz que no es la misma, no la misma
Gabi Tallarico: Ah,
lse posgrados: pantalla.
Gabi Tallarico: bueno, sí, esperen. Es otro entonces. Sí, sí, otro. Eh, dejo de compartir porque si no lo descargo. No, no le no le gusta. Yo sola veía.
lse posgrados: Por ahí lo que les conviene es es si ya tienen algo moderadamente limpio, etcétera, ya sigan sigan el pasito que viene, porque por ahí uno, ¿viste?
Gabi Tallarico: Sí, todo por suelto. No sé si vale la pena.
lse posgrados: y y lo que había armado vos el orden de envío a la vez, así que puedes mostrar algo de eso. Me parecía superinesante la
Lorna Pons: Ay, a ver.
lse posgrados: igual creo que la mejor forma es eh después llevarlo a colab, digamos, por ahí más útil para compartir todo, para es más útil hasta para mí entrar y revisar un colab y voy corriendo y viendo y que eh que por ahí un archivo en visual hoy en Ya tenemos

00:41:05

Lorna Pons: Sí. ¿Querés, David, que comparta yo la tabla?
Gabi Tallarico: Sí, sí,
lse posgrados: colab
Lorna Pons: La busco,
Gabi Tallarico: porque no y lo de
Lorna Pons: la busco así rapidito y bueno, tengo
Gabi Tallarico: lo de visual hoy avancé un poquito, pero no me no terminé para como mostrarlo yo.
Lorna Pons: eh a ver, voy a compartir eh creo que es esta porque tengo tengo un par Esta esta es la que te mandé, Gabi. No tenía ahí
Gabi Tallarico: Sí,
lse posgrados: Ah,
Gabi Tallarico: esa,
lse posgrados: perfecto. O sea,
Lorna Pons: un
Gabi Tallarico: es esa sí.
lse posgrados: en la entra el PDF y sale esto, digamos. Sí, buenísimo. Mirá, ponete de la de la fila uno.
Lorna Pons: Pero ya
lse posgrados: Es es más, esto no es el texto,
Lorna Pons: Sí,
lse posgrados: también es el texto con el chank, después del chanqueado, digamos,
Lorna Pons: claro. Y esto es porque era una sugerencia,
lse posgrados: ¿no?
Lorna Pons: digamos,
Gabi Tallarico: Sí.
Lorna Pons: y me de lo del glosario me pareció interesante esto, que cuando alguien pregunte qué es tal cosa sea como específico y no le traiga un montón de textos sino solo la definición que está ahí.

00:42:14

lse posgrados: O sea,
Gabi Tallarico: Y en esta ya están los títulos de los archivos,
Lorna Pons: Pero esto,
lse posgrados: vos creaste creaste un
Gabi Tallarico: que era lo que ayer faltaba también.
Lorna Pons: Claro. Ah,
lse posgrados: A,
Lorna Pons: ves que ayer faltaba esto acá.
lse posgrados: pero para para Loren me interesaría es abramos el documento
Lorna Pons: Sí.
lse posgrados: contenido punto PDF. La primera, lo que está ahí en verde, lo que está en verde está separado ya en chansamos. Sí,
Lorna Pons: Esto de acá, contenido.
lse posgrados: exacto.
Lorna Pons: Sí,
lse posgrados: Bueno,
Lorna Pons: sí,
lse posgrados: pero escucha, escucha,
Lorna Pons: sí son.
lse posgrados: abrir el abrir el PDF de contenido.
Lorna Pons: A ver,
lse posgrados: Okay.
Lorna Pons: espera
lse posgrados: Lo que quiero lo que quiero mostrar es con tu ejemplo cómo ingresa y cómo sale después de las funciones,
Lorna Pons: que
lse posgrados: etcétera.
Lorna Pons: bueno.
lse posgrados: Sí,
Lorna Pons: Eh, si no hablo, abro otro, el de carga de transporte, por ejemplo,
lse posgrados: bueno, sí, claro. Sí, cualquiera.

00:42:57

lse posgrados: decir tener
Lorna Pons: porque el de contenido es el A ver,
Gabi Tallarico: El más lío es ese,
Lorna Pons: claro, déjame buscarlo porque lo tengo en el Drive,
lse posgrados: car.
Lorna Pons: no lo tengo acá.
Gabi Tallarico: porque habíamos metido un archivo que también era como un índice general. Entonces después también nos dimos cuenta que que por ahí
Lorna Pons: Claro, encontró que había cosas muy repetidas,
Gabi Tallarico: es
Lorna Pons: por eso tiene muchos menos chans eh a ver que lo voy a buscar donde lo tengo contenido. No me lo
Gabi Tallarico: Yo te lo paso.
Lorna Pons: acuerdo.
lse posgrados: Entonces, el Chan ID significa que es la ficha 40, página 01. Eso es lo que interpretó.
Lorna Pons: Sí.
lse posgrados: Okay. O sea, tenemos la ficha número 40, la página 01. En este caso, esa página en toda esa página entró en un solo chank, porque si no hubiese abrido ficha 40, página 01 A, página B,
Lorna Pons: Sí,
lse posgrados: eso es así, ¿cierto?
Lorna Pons: sí.
lse posgrados: ¿Cuál es el documento fuente?
Lorna Pons: Eh,
lse posgrados: ¿Qué es ese?

00:43:53

Lorna Pons: carga de transporte.
lse posgrados: Perfecto. Acá eh ficha número. Okay. Está dentro de nombre, me parece bien. Después ficha título. Eso lo extrajiste con Rex.
Lorna Pons: Eh, no, ahí decía sin regex. Yo traje, lo limpié con algunos criterios que le di al chat, o sea, yo lo hago así con el chat y como le dije,
lse posgrados: Claro, pero y por eso por eso me interesa que mándame ese Excel y yo voy mostrando y voy
Lorna Pons: sí.
lse posgrados: explicando lo que me interesa.
Gabi Tallarico: Ah.
lse posgrados: Acá tengo el drive con el A ver,
Gabi Tallarico: Acá pasé en el chat puse el PDF,
lse posgrados: listo.
Gabi Tallarico: el de carga y transporte,
lse posgrados: Pasame ese Excel que estás mostrando y ya lo muestro.
Gabi Tallarico: pero eh no y también lo de las ¿Cuál es la función que estaría bueno?
Lorna Pons: Bueno,
Gabi Tallarico: A ver qué hace todo eso.
lse posgrados: F 40 con transporte. Tiki, a me parece claro porque lo por ahí yo porque lo vi al documento, pero por ahí la gente que no tuvo contacto con el documento Lorna, abrí el el PDF que mandó en el chat la la Gabi y ahí lo lo vamos a ir

00:45:01

Lorna Pons: Sí,
lse posgrados: viendo. Sí, porque yo lo que estoy viendo que lo esto es separado por página, ¿cierto?
Lorna Pons: sí.
lse posgrados: Claro, son cuatro páginas, o sea, debería tener cuatro chanks.
Lorna Pons: Y ahora te compartir,
lse posgrados: Vale.
Lorna Pons: Eh,
Gabi Tallarico: No estamos
Lorna Pons: claro, no,
Gabi Tallarico: preparadas.
Lorna Pons: no estaba preparada. Se me está haciendo acá. Acá está.
Gabi Tallarico: Sí,
lse posgrados: Okay.
Gabi Tallarico: sí,
Lorna Pons: No sé si lo pueden ver.
Gabi Tallarico: sí.
lse posgrados: Ahora mira,
Gabi Tallarico: Muy bien.
lse posgrados: fíjate que la primer página baje prácticamente contenido,
Gabi Tallarico: No tiene nada.
lse posgrados: ¿no? La segunda si ya vos trajiste con rejex,
Gabi Tallarico: No,
lse posgrados: que esa la ficha 40, ¿cierto?
Lorna Pons: A ver qué ficha es.
Gabi Tallarico: sí, es la 40 esa.
Lorna Pons: Aparenta.
lse posgrados: Claro. O sea,
Lorna Pons: Sí,
lse posgrados: dentro del del documento que se llama carga y transporte, ¿sí?
Lorna Pons: sí.

00:46:16

lse posgrados: Estásamos lo que les quiero explicar es que una cosa es que vos le metá el texto crudo y que vaya el texto crudo y otra cosa es que vos agarré y digas, "No, bueno, voy a interpretar mi PDF y voy a usar funciones rex para usar reconocimiento de entidades y voy a decir, bueno, cuando sea ficha 40, extraéeme la ficha 40 porque me interesa saber de qué habla la ficha 40 para cuando vos le preguntés a tu retriival, decime qué es lo que menciona la ficha 40 del documento concilización y transporte y te
Lorna Pons: Sí.
lse posgrados: debería traer ese tex esto que estás ahí mostrando en pantalla. Sí,
Lorna Pons: Sí. No, no está.
lse posgrados: nosotros,
Lorna Pons: Con eso no está hecho. Con
lse posgrados: bueno,
Lorna Pons: eso.
lse posgrados: ya sé, ya ya lo sé, pero a eso es lo que apuntamos, digamos, a a eso, es lo que buscamos con esto.
Lorna Pons: Sí.
lse posgrados: O sea, el reconocimiento de entidades usando regex te va a aportar valor para cuando tu retraival tome la fuente, la tome de una forma, digamos, más inteligente. Sí. Y ahí es es bastante más eh digamos más que un notebook LM, digamos, ¿no?

00:47:17

lse posgrados: El notebook LM también te lo va a reconocer porque está Google atrás obviamente, pero eh en esto que vos vas a hacer, digamos, en tu casa con tu computadora, debería funcionar bastante bien si vos le aportas con esos reconocimientos de entidades. Ahora, lo importante acá es ver usando tu caso de ejemplo, es repasar el PDF y ver cómo lo puedo dividir,
Gabi Tallarico: Vale.
lse posgrados: si la estrategia de división de documento es por página, ¿sí? O por contenido que tenga. Por ejemplo, esto es ficha 40, consolidación de carga de transporte. Ahora, dentro de ese PDF hay otra ficha, la 41.
Gabi Tallarico: Sí, en la segunda página,
lse posgrados: Okay.
Gabi Tallarico: en la tercer página.
Lorna Pons: Sí.
lse posgrados: Okay. En la en la ficha 41, ahí está dentro de ese PDF que ya estamos dentro de consolidación y transporte, la ficha 41 es transporte frigorífico. Sí. Y bueno, vos lo fuiste usando funciones regex, capturando y separando los textos así, ¿cierto?
Lorna Pons: Eh, no, yo creo que no usé funciones rex, pero no sé, no, yo lo voy haciendo como dije,
Gabi Tallarico: Sí.
Lorna Pons: bueno, quiero hacer chans de de este de esta estructura, me lo separó.

00:48:37

lse posgrados: Claro.
Lorna Pons: Bueno, y así lo hice guiando medio de lo que estaba en el colap,
lse posgrados: Bueno, ahora te te digamos para Claro.
Lorna Pons: ¿no? Para usar la misma estructura que para que podamos
Gabi Tallarico: Perfecto.
lse posgrados: De nuevo, si nosotros usamos una función para cada cosa y vos corrés
Lorna Pons: trabajar.
lse posgrados: una función para cada cosa y le hacés un print a lo que hace cada cosa, vos sabrías exactamente qué es lo que hace. Entonces también es un, digamos, es un caso particular porque yo también lo hago. Yo le pido al chat, che, necesito no sé qué, no sé cuánto. Y me tira todo. El chat no va a ser. Ahora, si vos en el prom le decís se farame cada función por una tarea y además eh tener en cuenta que necesito justificar o probar los patrones reges que está usando, listo. Eh, te lo va a ir separando. Comentame el código para y vos va cuando vos vas corriendo el colab o tu o tu notebook en Júpiter en en el visual, va ir viendo paso a paso. Sí. Entonces, está bueno el ejemplo. Ahora, yo creo que el Excel es un avance.

00:49:40

lse posgrados: Mándamelo. Lo lo lo voy a revisar. Pero el Excel debería ser esto que te estoy mencionando, o sea, el Excel, el resultado debería ser ficha 41 en una columna, un número de ficha, qué sé yo, eh título o lo que sea de esta parte, contenido del texto y así. Ahora,
Lorna Pons: Sí.
lse posgrados: cuando vos, digamos, el chanking vos lo vas a poder hacer por página como como hemos hablado ayer o lo va a poder hacer por contenido eh semántico que tenga el el coso. Entonces, ahí voy a compartir pantalla porque sirve el ejemplo para otros casos.
Lorna Pons: habíamos quedado que contenido lo íbamos a
lse posgrados: Sí,
Lorna Pons: hacer.
lse posgrados: por eso por eso te estoy diciendo que por eso hacerlo por contrario va a ser más fácil probar. De hecho, yo creo que ya están encaminados en eso. Me parece s super eh potable que lo hagan. Había Ayer habíamos hablado de de esto en alguna parte, eh, pero a ver, para que quede claro, porque puede ser que sea un que sea un caso para para los demás chicos,
Gabi Tallarico: Ok.
lse posgrados: cuando uno tiene un documento TXT, ¿sí?, O sea, ya entra, ya entra el texto.

00:50:53

lse posgrados: Sí, ya entra el texto. Y el texto eh puede estar separado por, no sé, vamos a poner acá. Esta es la página uno del documento. Sí, la página uno. Sí, la página uno puede tener el texto introducción directamente. Puedo poner introducción, intro y acá todo el todo el texto. Sí. Y en la misma página uno puede tener directamente ya eh, no sé, como dijimos recién, la metodología, métodos, ¿sí? Y de nuevo el texto que a mí me que a mí me sirve el tema cuando yo hago los chank y esto lo paso a a un chank, eh, si yo a esto lo tengo lo chanqueo por página, es probable que eh un chank me quede, por ejemplo, intro, que como el chunk no va separando por por por contenido semántico, sino por cantidad de tokens o por cantidad de caracteres me quede directamente un chank mezclando dos cosas, digamos, cuando son problemas chicos, quizás convenga eh separarlo, ¿no? Y acá puede que me quede me met. Sí, ese puede ser un chank. Y el siguiente chunk, sí, este sería un chunk. Y el otro chank podría quedar con lo que sigue de la página.

00:52:21

lse posgrados: ¿Qué qué es lo que sigue? Quizá quede todos o perdón o sí y abajo lo que estaba puesto ya directamente. Entonces como esto va a alimentar tu retrival, el documento va a traer o esto o esto o estos dos documentos, pero como está partido así, no tiene no tiene sentido semántico. Sí. Entonces lo que conviene es primero en vez de hacer una separación por página separación hacer separación semántica. O sea, decir, bueno, eh, voy a decir esto va a ser un TXT que después voy a chanar y esto va a ser un TXT que después voy a chanar. Sí, de esa forma no te va, digamos, vas a tener overlap, etcétera, etcétera, etcétera, pero lo que no vas a tener eh va a ser e redundancia, no vas a tener esas cuestiones mezcladas cuando te cuando el retra lo que va a hacer cuando te traiga los documentos eh los documentos relacionados, esos documentos relacionados van a tener muchísimo más sentido. Sí, en esta parte, ¿se acuerdan? Ayer hemos visto la lo que hace el rag, el el el rack se va a alimentar de de documentos, ¿sí? Todo el contexto que vamos a tener chanqueado, etcétera, y de una pregunta y por una búsqueda vectorial lo que va a traer es n cantidad de documentos relacionado a lo que yo pregunté.

00:53:45

lse posgrados: Esto me va a separar. Ahora sí, esto esto es lo que va a alimentar el LLM para que el LLM genere respuesta a la parte de la generación del texto. Y acá nosotros las separamos solo por página, por un trabajo para hacerlo rápido o porque nada, simplemente lo no no le ponemos digamos eh limpieza o criterio en esta parte. Todas las partecitas que me devuelva el texto quizás tengan cuestiones mezcladas y el retrival se va a alimentar de eso para armar la respuesta. Entonces, no pierdan de vista esto. El retrabal genera una respuesta argumentada o fundamentada en una n cantidad de documentos que selecciona por similitud semántica a partir de una búsqueda vectorial. Eso es lo que hace el RAC. Entonces, cuanto mejor hagan el chanqueado y le pongan metadato, etcétera, mejor va a ser la respuesta de digamos. Sí. Y eso entra dentro de la parte de lo que hemos hablado eh de hacer las eh las mejoras, ¿no? Limpiar y mejorar esa documentación, esa documentar esas mejoras también está bueno. Entonces sí ahí Gabi Lorno, nada, les sugiero que vayan por ese camino, digamos que eh como son pocos PDF y es un caso bastante, digamos, entre comillas sencillo, digamos, o interpretable, los lo hagan de esa forma.

00:55:15

lse posgrados: Entonces, traten de no separar por página, separar por contenido, que las funciones, usar funciones regex para eso, patrones y ir probando cómo la va lo va separando antes de generar el Excel. Cuando vos te aseguras que ya las partecitas te las está capturando bien los patrones Rejex, recién pasas al al siguiente. Rege te va a decir, si yo voy a decir, "Mira, después de que que me reconozca donde aparezca ficha, etcétera, la primera vez y te lo te lo te lo vaya etiquetando." Eso reg esos patrones lo vas a encontrar. Así que bueno, eh la clase que viene ya va a ser más onda a clase. La idea de esta era más alineamiento de de los grupos. Eh, de todas maneras, eh, de la clase que viene lo que voy a hacer va a ser eh separar y dejar eh al menos una hora para ir, digamos, tener interacción con con ustedes. Ahora los que sí les pido, los que tengan cuestiones avanzadas, es que tengan para cuando lleguen a clase tengan el código listo para ir probando, para ir viendo o al menos los documentos cómo entran, cómo salen para ir para ir mostrándolo. Si hay alguno que ya tiene algo de Leda hecho, me gustaría que se anime a mostrarlo.

00:56:34

lse posgrados: E ahí, Juan Pablo, vos va, vos ya va a mostrar la clase que viene, ¿cierto?
J.Pablo Zebraitis: Bueno, como vos quieras, o sea, no tengo ningún problema. Si querés te muestro ahora si queres que viene,
lse posgrados: Me a ver si si lo tenés me sirve
J.Pablo Zebraitis: recuerdo tus tiempos y planificación.
lse posgrados: mostrarlo
J.Pablo Zebraitis: Dale.
lse posgrados: ahora.
J.Pablo Zebraitis: Bueno, voy a compartir entonces. Este no estaba preparado tampoco, ¿no? O sea, pero bueno, vamos arriba.
lse posgrados: Importa.
J.Pablo Zebraitis: A ver, voy a dar un poquito contexto. La vez pasada que yo hablé hablaba de que teníamos este imágenes este de WhatsApp, ¿no? Que íbamos identificar como imágenes,
lse posgrados: Ahí
J.Pablo Zebraitis: está este grand digamos eh realamos los casos, ¿se acuerdan que que teníamos esto? las imágenes como capturas de de cosas de WhatsApp, de tickets y cosas por el estilo, está pero claro, yo tenía en realidad 18 casos que son las bases que que había definido, que había pedido a la gente de soporte que me sacaran y esto no me daba en principio para para armar un análisis de datos que que fuera relevante o bueno, decidir por otro lado un poquito qué pasa.

00:57:45

J.Pablo Zebraitis: Nosotros tenemos a nivel de soporte operativo esto que es un digamos un sistema de ticketing, ¿si? Que por cada cliente digamos generan issues de situaciones a ser resueltas, está que es lo que vemos en el WhatsApp, ¿no? O sea, el reflejo del WhatsApp se transforma acá como dij paso siguiente
lse posgrados: el paso siguiente, digamos.
J.Pablo Zebraitis: o que dejaron de hacer porque es más cómodo WhatsApp y todos los problemas que tengo, ¿no? Bueno, dicho esto, ¿qué qué decidí hacer? recuerdo lo que tú planteaste la vez pasada la semana pasada.
lse posgrados: Dale.
J.Pablo Zebraitis: Bueno, eh voy a tratar de tener la ingesta de este de esto de Redmine, ¿sí?, de los últimos dos años de estos ISUS para eh procesarlo eh y poder identificar algunas variables y poder hacer un EDA de eso que de última es lo que vamos a generar, ¿no? O sea, después de de WhatsApp ponerle podemos transformar una cosa intermedia en Jason o lo que fuera. Y lo que nosotros queremos es después generar estos ISUS para hacer analítica y cosas por el estilo, ¿no?
lse posgrados: Vale.
J.Pablo Zebraitis: Y después alimentar ciertas reglas autodefinidas o con la gente de soporte y después que haya un retrival de bueno, identificación y miles de cosas más.

00:58:56

J.Pablo Zebraitis: Entonces, este, dado que nos planteaste esta hermosa herramienta la vez pasada también en trabajo con con Cloud, este, lo que hice fue hacer la ingesta de, vamos a poner un poquito de contexto a esto, un segundito. Eh, acá tengo el corpus de No, estos son los hallazgos. O sea, lo que hice fue agarrar de Redmine de los años 25, 26, ¿no? Este, con traer los datos. estos datos que estuve trayendo eh para más o menos verlo los eh los fui trayendo a disco, o sea, de del sistema a través de la API estuve dando ingesta, perdón,
lse posgrados: Sí, sí, lo bajaste, le pegaste Lo
J.Pablo Zebraitis: lo bajé y cada uno de cada uno de estos carpetitas son un nichu de esos,
lse posgrados: desc.
J.Pablo Zebraitis: o sea, un elemento de de soporte eh que básicamente este lo bajé como un archivo de de MD con con digamos los datos del contenido de de de del sistema más este las actualizaciones y cosas que que hubieron en ese tema. O sea, eso en principio, se bajé, digamos, de ingesta fue opa, ese tema. Después lo que hice fue agarrar y transformar esa esa data eh como si fuera un documento, ¿no?

01:00:17

lse posgrados: Claro.
J.Pablo Zebraitis: Un MD o como si fuera un PDF o lo que fuera. la transformé en un archivo Jason, que lo que tú estabas hablando hoy, o sea, acá tenes los marcadores,
lse posgrados: Claro,
J.Pablo Zebraitis: tagueados, está este,
lse posgrados: perfecto.
J.Pablo Zebraitis: entonces en función de digamos preprocesar, claro, esta data está normalizada,
lse posgrados: Claro,
J.Pablo Zebraitis: ¿sí?
lse posgrados: pues el red lo trata así,
J.Pablo Zebraitis: trata, sí,
lse posgrados: digamos.
J.Pablo Zebraitis: esta data está normalizada, pero después lo que voy a hacer básicamente es unir la data no normalizada, o sea, mi ingesta de WhatsApp o del R o de lo que fuera en algo parecido a esto para tener una ingesta homogénea al
lse posgrados: Sí,
J.Pablo Zebraitis: sistema,
lse posgrados: está bueno,
J.Pablo Zebraitis: ¿no?
lse posgrados: es un ejemplo de cómo lo queré estructurar, digamos, ¿no? O sea, acá ten acá ten la maqueta y ahora tu sistema se va a basar en esto.
J.Pablo Zebraitis: Es exacto. Acá, por ejemplo, y ¿qué cosa me puede pasar?

01:01:00

J.Pablo Zebraitis: También tengo en esta el retrival de esas issues, tengo también imágenes metidas en el medio del issue de Redmine y ahí lo que hice, como ven ahí normalizada es porque normalicé las imágenes a un formato de tamaño y estructura similar para poder hacer el proceso de del procesamiento más fácil y poder que eso sea más más estructurado, ¿no? Entonces está algún dato. Eh, los proyectos, estos son cada uno de mis clientes, digamos. Este, estos eran los cantidad de de temas tratados por cada uno de estos elementos, ¿no? Eh,
lse posgrados: Claro, acá ya estamos hablando de EDA tu exploración te di resultado.
J.Pablo Zebraitis: o sea, me dio este resultado, o sea, me dio 700 y pico separados, está eh 1360 adjuntos a estas cosas que son de todo tipo, por eso no norma ni sé. Este, acá hay scripts para para bueno, para todo esto, ¿no? Para para para la ingesta de de la información en particular. Acá es como está estructurado. Acá están los filtros aplicados. Sí. Y la decisión de la presentación de datos. Digo, esto está muy escrito acá, pero está mejor en las imágenes.

01:02:09

J.Pablo Zebraitis: Ahora lo vamos a ver. Este y después, digamos, estamos hablando de las conclusiones de del análisis de cada una de las cosas, ¿no? Bueno, dicho esto, vamos a EDA usando el programita que nos que nos dijiste acá. Eh, le di, ¿Viste que dice B2? En realidad hubo como cuatro versiones de esto porque empecé le dice, le dije a Cloud que, que bueno que armara un EDA inicial con las variables que consideraba directamente de los que extraído de de los issus y no me servía para nada.
lse posgrados: Yeah.
J.Pablo Zebraitis: O sea, me di cuenta de que lo que lo que lo que sacó así automáticamente realmente no se para nada porque los datos en sí, por ejemplo, estaban cosas que eran casos de soporte como futures o bugs o o cosas que me ensuciaban mucho. Eh, el objetivo real de acá, que es clasificar los casos para para procesar y buscar ser más ágil en en en en identificar el problema y corregirlo, derivarlo a desarrollo o cosas por el estilo, ¿no? Ese es mi objetivo del sistema en sí.
lse posgrados: Vale.
J.Pablo Zebraitis: Este, entonces, eh, acá esto fui empezando a generar filtros, por ejemplo, solo los filtros de soporte o no.

01:03:19

J.Pablo Zebraitis: Eh, si si quiero excluir eh identifiqué que había muchos de este tipo, actualizaciones de post, de seguimiento que me ensuciaban lo que lo que a mí me interesaba más, está y que seguramente no va a estar en el futuro. Este, después e está eh después cosas que me parecieron interesantes también en la primera versión de Leda, porque tuve, como te dije, varias versiones, es este esta variable categórica no la tenía tema marco, o sea, que en realidad lo que yo quiero categorizar por tema para poder después derivar.
lse posgrados: Bueno, ¿cómo laiste? ¿Y cómo la la obtuviste?
J.Pablo Zebraitis: Está bueno.
lse posgrados: Si no la tenías en el corpus, ¿cómo la sacaste?
J.Pablo Zebraitis: Después, bueno, a través de ella le dije, "Bueno, está identifiquemos qué casos" y después iterando en eso, identifiqué los ciertos casos que que que estaban que
lse posgrados: Claro. O sea,
J.Pablo Zebraitis: están
lse posgrados: lo que vos hiciste fue tenías un tenías un corpus que no tenía esa etiqueta y usando un
J.Pablo Zebraitis: mm
lse posgrados: LM interpretación semántica el texto le dijiste, "Clasificámelo en esta etiqueta."
J.Pablo Zebraitis: es eso más dominio, eso más darle reglas de dominio.

01:04:21

J.Pablo Zebraitis: para que entendiera de qué estamos hablando, ¿no? O sea, porque confundía cosas que no tenían sentido.
lse posgrados: Claro,
J.Pablo Zebraitis: Y esa es la idea de este sistema, ¿no? O sea, ir generando un sistema que para ir generando progresivamente reglas de dominio que sean mejores para la identificación y clasificación de de todos los
lse posgrados: y Eleda,
J.Pablo Zebraitis: casos.
lse posgrados: ¿qué descubrimiento te aportó?
J.Pablo Zebraitis: Bueno,
lse posgrados: un descubrimiento que vos
J.Pablo Zebraitis: muchos, muchos, muchos, muchos. Este, primero por ejemplo,
lse posgrados: hecho.
J.Pablo Zebraitis: voy a decir uno uno sencillo. Este este indicador está el SLA inferido versus el declarado, ¿está? ¿Qué significa eso? O sea, una de las importantes cosas para para la ISO, para las indicadores de gestión es en cuánto tiempo cumplo con mis objetivos
lse posgrados: Sí,
J.Pablo Zebraitis: de de calidad de de respuesta y de resolución de temas,
lse posgrados: claro.
J.Pablo Zebraitis: ¿no? Entonces, básicamente una de las cosas que yo hice acá a nivel de exploración de datos, porque fue fácil, solamente porque fue fácil, no es porque lo buscara, es darme cuenta de que los issues tenían una métrica que llamaba que que decía eh tagueada, está clasificada manualmente por el operador que decía en cuánto tiempo se resuelven las

01:05:32

lse posgrados: Ô
J.Pablo Zebraitis: cosas, pero después dije, "Bob, esto se me está yendo mucho a no aplica o cosas por estilo, como como que el usuario seleccionaba, lo aplica, ¿viste? Para no decirlo. Este,
lse posgrados: Claro.
J.Pablo Zebraitis: y bueno, y lo que hice yo, en vez de hacer eso, comparé eh el ese valor que categórico que ya estaba venía definido en el corpus, digamos, contra el tiempo que que que el hio estuvo
lse posgrados: Que ingresó,
J.Pablo Zebraitis: abierto y se cerró.
lse posgrados: entre que ingresó la digamos la diferencia entre que solución ingreso.
J.Pablo Zebraitis: Está. Eso también me
lse posgrados: Claro.
Lorna Pons: Vale.
lse posgrados: Y ahí estás viendo que no aplica tener 98 casos, digamos.
J.Pablo Zebraitis: cuestiona.
lse posgrados: O sea, que mucha gente que mucha gente que tenía mucho que la gente que tenía más de, no sé, 30 días le ponía directamente no
J.Pablo Zebraitis: Ahí tenés el un el hallazgo.
lse posgrados: aplica.
J.Pablo Zebraitis: Está solo el 30% de las calificaciones del operador coinciden con inferido en función de esta
lse posgrados: Claro, eso buena decisión porque lo agarró el operador,

01:06:28

J.Pablo Zebraitis: varia.
lse posgrados: "Che, clasific, si no, para qué cargo esto." Pero Pablo,
J.Pablo Zebraitis: Está.
lse posgrados: ahí hay algo importante.
J.Pablo Zebraitis: Y hay otro tema más,
lse posgrados: Hay algo importante.
J.Pablo Zebraitis: eh, respecto al tema si quieres, después te digo, dale.
lse posgrados: Hay algo que te que que por ahí eh desde la gestión, ¿no? hablando de los datos, pero desde la gestión es importante quizá el operador que carga sepa que vos estás usando el dato. Sí, para porque si no que como che es como la encuesta que a veces te mandan, vos le mandas cualquier cosa, pero si realmente el operador ve que lo que él carga aporta valor para el sistema, aporta valor para el trabajo, capaz que te lo empieza a cargar bien y la falla quizás no es que el operador lo cargó mal, sino es que nadie usaba nunca ese dato, ¿me entendés?
J.Pablo Zebraitis: Correcto. Ahora sí es fácil por ya por este sistema y todo lo demás. Ahora sí va a ser fácil. Digo, lo primero que hice fue agarrar al jefe de de esto y mostrarle, ¿no?
lse posgrados: Vale.
J.Pablo Zebraitis: Perdón.

01:07:19

J.Pablo Zebraitis: Pero más allá de esto, eh también me hace visualizar y por eso la importancia de este proyecto que igual esto también es falso, está o sea porque esta conclusión podría ser sacada a primera vista, ¿no? Pero, ¿por qué? en función de cuando se abrió a cuando se cerró el ticket, puede tener un una que se cerró varios días después o lo que fuera, que en realidad es porque no lo cerraron, no porque terminaba ahí el tema, ¿me explico?
lse posgrados: Ah, claro, claro,
J.Pablo Zebraitis: Está,
lse posgrados: claro,
J.Pablo Zebraitis: yo puedo estar teniendo esa cuestión y es verdad y por eso la importancia de automatizar todo esto y que esos procesos queden
lse posgrados: claro.
J.Pablo Zebraitis: lo más eh traqueables y parecidos a la realidad, ¿no? O sea, que esté que sea realmente o que refleje la realidad.
lse posgrados: Es lo que ahora ya ya que hiciste por ahí lo que suele pasar cuando vos haces una primera exploración, probas todo contra todo y empezas a sacar a insight y digamos la conclusión es digamos
J.Pablo Zebraitis: Exacto.
lse posgrados: y lo poner lo que te puede aportar valores, okay, de todo lo que exploré, ¿cuál es mi top 10 de métricas o de cosas que yo voy a poner la lupa de ahora en adelante la gestión?

01:08:24

J.Pablo Zebraitis: Claro,
lse posgrados: Y quizás ahí,
J.Pablo Zebraitis: para definir los KPI.
lse posgrados: claro. Y de ahí capaz que tenés, no sé, otros gráficos, métricas que usaste que son 80 más, que usaste un montón de tiempo para para buscarla, pero que no te aportan, pero ya descubriste la que te aportan, digamos, lo cual está bueno.
J.Pablo Zebraitis: Exacto. No,
lse posgrados: Te
J.Pablo Zebraitis: y para y para y una cosa también otra otro descubrimiento,
lse posgrados: felicito.
J.Pablo Zebraitis: ¿cuál de los categorías están tratadas por los usuarios como más rápid graves, urgentes o no? O sea, porque esta categorización la hace el usuario, está, o sea,
lse posgrados: Claro,
J.Pablo Zebraitis: el usuario que postea la cuestión y después además Exacto.
lse posgrados: son todas normales,
J.Pablo Zebraitis: Sin todas normales,
lse posgrados: no hay
J.Pablo Zebraitis: vos todo normal cualquier tema no hay ningún tema que sea se se visualiza
lse posgrados: urgencia.
J.Pablo Zebraitis: muchísimas cosas por acá, otra de las cosas, ¿quién es el iniciador del caso, puede ser el equipo nuestro o puede ser el cliente?

01:09:11

lse posgrados: Yeah.
J.Pablo Zebraitis: Y ahí yo que hice ponerle filtros para poder ver cómo cómo funcionaba e en en este caso, o sea, las cosas que iniciamos nosotros, el equipo de soporte o las cosas que inician los clientes y cómo varía eso. Y digamos la realmente la herramienta está fantástica, me encantó lo que nos propusiste porque fácilmente permite definir todas estas cosas en base a un corpus de x datos, ¿no? digo, creo que fue un éxito eso de cambiar el approach y no tener solamente los los n casos de estudio así, sino darle un poco más de de cosa para poder lograr esto. Bueno,
lse posgrados: Felicito.
J.Pablo Zebraitis: s si querés que explique algo más.
lse posgrados: La verdad que quedó muy bueno. Quedó muy bueno. Me me alegra que hayas aportado,
J.Pablo Zebraitis: Ah.
lse posgrados: que hayas usado lo de la clase anterior, que ah, yo me quedé preocupado la clase anterior porque terminé de hablar, mostré gráfico, etcétera, y como que quedaron quedaron todos así como ah mucha información y y que lo hayas tomado y que lo hayas aplicado me parece fantástico, che,
J.Pablo Zebraitis: Bueno,
lse posgrados: la verdad que estuvo estuvo bueno.

01:10:07

J.Pablo Zebraitis: eso es lo que Sip.
lse posgrados: Ahora al al a ver, Juan Pablo tiene tiene más experiencia, se nota que trabajan en dominio de los IT, entonces digamos no nos pongamos la vara tan alta todos los demás, digamos, eh, pero anímense a cuando tengan su texto más o menos limpio ya y vayan a fase deda a iterar con Cloud o con Gemini para obtener un dashboard. ya cuando tenga sus gráficas apliquen un dashboard, los hace la verdad que es bastante bastante piola lo que genera hoy en día la IA. Entonces, anímense a a eso. Pero primero, digamos, lo bueno que tenía la lo que mostró Juan Pablo es que ya tenía los datos que venían de un sistema que ya más o menos lo tenía relativamente organizado. Entonces, hay una una fase ahí de organización de datos que muchos de ustedes no la tienen, pero háganla como hemos visto recién con Loren y con Gabi, de Okay. Ficha, eh, el título de la ficha, de qué se trata, etcétera, ¿no? Eh, así que buenísimo. Me alegra. Eh, bueno, chicos, yo creo que ya mañana hay algunos anotados, me parece que Marcelo y hay un hay alguien más anotado, pero y lo veo mañana a la hora que está ahí en la en la Traten de ir ya con algo para mostrar el código.

01:11:29

lse posgrados: Igual yo igual durante la tutoría voy ahí escarvando un poquito y vamos eh charlando sobre
Marcelo Luna: Yo te mandé algo por mail,
lse posgrados: eso.
Marcelo Luna: eh, que un poco la intención era conversarlo mañana, eh, podemos trabajar un poco con eso y y bueno, a ver, un poco de orientación ahí con un par de cosas,
lse posgrados: De una,
Marcelo Luna: pero
lse posgrados: de una y la clase que viene ya va a ser modo más clase, mitad de clase y después interacción mitad de clase.
Marcelo Luna: Bueno,
lse posgrados: Dale. Bueno, chicos, los libero. Muchas gracias.
Gabi Tallarico: No, super fantástico.
Lorna Pons: Buenas noches,
Marcelo Luna: gracias.
Lorna Pons: Ev.
Marcelo Luna: Nos vemos.
Gabi Tallarico: Mil mil gracias.
Manuel Babuglia: Gracias.
lse posgrados: Al al al resto de los grupos anímenense.
J.Pablo Zebraitis: Gracias.
Marcelo Luna: Oh.
lse posgrados: La clase que viene a mostrar más,
Gabi Tallarico: Eh,
lse posgrados: interactuar más les va a servir
Gabi Tallarico: podemos vos podés mandar el enlace de mañana,
lse posgrados: bastante.
Gabi Tallarico: aunque no sea mi grupo, pero escuchar.
lse posgrados: Está está en el mail de todos,
Gabi Tallarico: Ah,
lse posgrados: está en la tabla.
Gabi Tallarico: bien.
lse posgrados: Sí, sí, métanse.
Gabi Tallarico: Después miro porque están buena,
lse posgrados: Es para todos, digamos. Igual la grabación.
Shimon Ben: Ah, yo veo la grabación. Eso te decir.
Gabi Tallarico: está buenísimo escuchar los otros grupos,
lse posgrados: Sí, sí, sí,
Gabi Tallarico: eh,
lse posgrados: sí.
Shimon Ben: Sí.
lse posgrados: Se se aprende un montón.
Gabi Tallarico: se reaprende.
lse posgrados: Gracias Juan Pablo.
Gabi Tallarico: Bien.
lse posgrados: Muy bueno lo tuyo también. Chao,
Shimon Ben: Bueno,
lse posgrados: chicos.
Shimon Ben: a
Marcelo Luna: Gracias. No.

La transcripción finalizó después de 01:29:31

Esta transcripción editable se ha generado por ordenador y puede contener errores. Los usuarios también pueden cambiar el texto después de que se haya generado.

