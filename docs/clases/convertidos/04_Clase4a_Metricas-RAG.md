# 04_Clase4a_Metricas-RAG

- Fuente: `04_Clase4a_Metricas-RAG.pdf`
- Tipo: PDF
- Fecha de conversion: 2026-05-24

> Conversion automatica para consulta, estudio y armado de presentacion. Puede requerir ajustes manuales si el material original contiene columnas, tablas complejas, imagenes o formulas.

- Paginas extraidas: 12

## Pagina 1

Evaluación Práctica de
Sistemas RAG
El arte de medir la recuperación y la generación sin morir en el intento
AUDITORÍA DINÁMICA · FORMACIÓN TÉCNICA

## Pagina 2

El Enfoque Pedagógico: El Examen a Libro Abierto
Un sistema RAG se comporta como un alumno que se presenta a un examen con acceso a un manual completo. Sin embargo, el suspen so
puede llegar por dos caminos completamente distintos.
Fallo de Retrieval
El alumno leyó la página equivocada. El buscador vectorial
recuperó documentos irrelevantes o incompletos. El LLM nunca
tuvo la oportunidad de responder bien: la materia prima era
defectuosa desde el inicio.
Fallo de Generation
Leyó la página correcta… pero redactó una mentira. El documento
recuperado era el adecuado, pero el modelo generó una respuesta
que contradice o extrapola más allá del contexto. Esto se llama
alucinación y es el riesgo más difícil de detectar.
Comprender esta distinción es el primer paso para auditar un sistema RAG de forma sistemática y eficaz.

## Pagina 3

MÓDULO I
La Puntería del
Buscador
Métricas para auditar la base de datos vectorial y el proceso de
Retrieval

## Pagina 4

Precision@k vs. Recall@k — La Analogía del Pescador
Ambas métricas se calculan sobre los k primeros documentos recuperados y responden preguntas complementarias sobre la calidad del
buscador vectorial.
Precision@k
"De los peces que sacaste en la red, ¿cuántos eran los que
buscabas?"
Mide la proporción de documentos relevantes entre los k
recuperados. Una Precision@k baja significa que el contexto
enviado al LLM está contaminado con ruido, lo que puede
confundir la generación.
Recall@k
"De todos los peces buenos del lago, ¿qué porcentaje lograste
atrapar?"
Mide cuántos documentos relevantes existentes fueron
efectivamente recuperados. Un Recall@k bajo implica que
información crítica fue omitida, dejando al LLM ciego ante datos
clave.
Ejemplo con k=3: Si hay 5 documentos relevantes en el corpus y el sistema recupera 3, de los cuales 2 son relevantes →
Precision@3 = 2/3 ≈ 0,67 y Recall@3 = 2/5 = 0,40. Siempre existe una tensión entre ambas métricas.

## Pagina 5

MRR — El Impacto del Primer Flechazo
Mean Reciprocal Rank (MRR) evalúa una única pregunta: ¿en qué posición aparece el primer documento relevante? No le interesa el conjunto
completo, solo la velocidad del acierto inicial.
La Fórmula
Donde rank_i es la posición del primer documento relevante
para la consulta i. Se promedia sobre todas las consultas
del conjunto de evaluación.
¿Cómo premia y castiga?
•
Posición 1 → Puntuación = 1,00 (máximo)
•
Posición 2 → Puntuación = 0,50
•
Posición 3 → Puntuación = 0,33
•
Posición 5 → Puntuación = 0,20 (severo castigo)
El descenso es no lineal: pasar del puesto 1 al 2 es mucho más costoso que
pasar del 4 al 5.
Ideal para asistentes de respuesta rápida donde el usuario no
quiere revisar múltiples resultados.

## Pagina 6

NDCG — El Valor del Orden
Normalized Discounted Cumulative Gain es la métrica más sofisticada del Retrieval. No solo pregunta si los documentos son relevantes, sino si
están ordenados de mayor a menor importancia.
Nivel 1 — Relevancia Graduada
Los documentos no son simplemente
"buenos" o "malos". Se les asignan notas
(p. ej., 0 = irrelevante, 1 = parcialmente
relevante, 2 = muy relevante). Esto
captura la riqueza real del corpus.
Nivel 2 — Penalización por
Posición
La información más crucial debe
aparecer arriba. NDCG descuenta
logarítmicamente la relevancia de los
documentos según su posición: un
documento muy relevante en la posición
5 vale mucho menos que en la posición 1.
Nivel 3 — Comparación contra
el Orden Perfecto (IDCG)
El resultado se normaliza dividiéndolo
entre el DCG ideal (IDCG), es decir, el
ranking perfecto teórico. El valor final
oscila entre 0 y 1: cuanto más cerca de 1,
más se acerca el sistema al orden óptimo
posible.

## Pagina 7

MÓDULO II
La Mente de la IA
Cómo evaluar si el LLM procesa… o inventa

## Pagina 8

El Dilema de la Factualidad — El Polígrafo del RAG
El LLM puede sonar brillante… y estar mintiendo.
¿Qué mide Faithfulness?
Faithfulness (Fidelidad) evalúa si cada afirmación presente en la respuesta
generada puede ser verificada directamente en los documentos recuperados. Es el
polígrafo del sistema RAG.
El riesgo oculto
Un LLM puede construir respuestas elocuentes, bien estructuradas y con tono
profesional mientras introduce datos falsos, fechas incorrectas o cifras inventadas.
La fluidez lingüística no garantiza la veracidad factual.
En entornos legales, médicos o financieros, una sola alucinación no
detectada puede tener consecuencias graves. Faithfulness debe ser
métrica prioritaria.

## Pagina 9

Dimensiones de la Respuesta — Relevancia y
Concisión
Más allá de la factualidad, una respuesta de calidad debe ser pertinente (contestar lo que se preguntó) y eficiente (sin redundancias que
encarezcan el sistema). Dos patologías frecuentes lo rompen:
El que se va por las ramas
Baja Relevancia de Respuesta
El sistema genera una respuesta extensa y bien redactada, pero
que no responde la duda concreta del usuario. El contexto
recuperado puede ser correcto, pero el LLM divaga hacia
información adyacente. Se mide comparando la pregunta original
con el contenido real de la respuesta.
El redundante
Baja Concisión
La respuesta repite la misma idea con distintas palabras,
consumiendo tokens innecesariamente. En sistemas con alto
volumen de consultas, la baja concisión se traduce directamente
en mayor coste operativo. La concisión se evalúa detectando
proposiciones duplicadas dentro de la respuesta.
Una respuesta ideal puntúa alto en ambas dimensiones: va al grano (alta relevancia) y no se repite (alta concisión). Optimizar solo
una puede degradar la otra.

## Pagina 10

La Batalla Semántica: BLEU/ROUGE vs. BERTScore
El mismo contenido puede recibir puntuaciones radicalmente distintas según la métrica elegida. El siguiente contraejemplo lo ilustra con
claridad:
Referencia humana
"El comité aprobó el presupuesto municipal."
Respuesta del sistema
"La junta autorizó el dinero del ayuntamiento."
BLEU / ROUGE — Conteo de Palabras
Miden la coincidencia literal de n-gramas entre referencia y
respuesta generada. Al no compartir casi ninguna palabra exacta,
asignan una puntuación muy baja… aunque el significado sea
idéntico. Son rápidas y deterministas, pero ciegas al significado.
BERTScore — Embeddings Semánticos
Convierte cada token en un vector de significado y calcula la
similitud coseno entre ambas frases. Detecta que "aprobó" ≈
"autorizó" y "presupuesto" ≈ "dinero", otorgando una puntuación
alta y correcta. Es la opción robusta para lenguaje natural diverso.

## Pagina 11

La Clave del Éxito: El Golden Dataset
Ninguna métrica funciona si no existe primero un patrón de medida fiable. El Golden Dataset es ese patrón: un conjunto de prueba curado
completamente a mano que actúa como el metro de platino del sistema RAG.
Preguntas Reales
Formuladas por usuarios reales o expertos
del dominio. No preguntas artificiales ni
demasiado simples. Deben cubrir casos
límite, ambigüedades y variedad de
formulaciones.
Documentos Verdaderos
Los fragmentos del corpus que realmente
contienen la respuesta correcta. Etiquetados
manualmente por expertos, no por el propio
sistema. Son el suelo de referencia (ground
truth) del Retrieval.
Respuestas de Referencia
Respuestas ideales redactadas por personas,
no por la IA. Son el estándar contra el que se
compara la generación. Sin ellas, métricas
como Faithfulness o BERTScore no tienen
ancla de comparación.
Invertir tiempo en construir un Golden Dataset de calidad multiplica el valor de todas las métricas posteriores. Sin él, se mide con una
regla torcida.

## Pagina 12

¿Cómo Elegir tu Métrica Clave?
No todas las métricas son igual de relevantes para todos los sistemas. Tu elección debe depender del objetivo prioritario de tu aplicación RAG.
Priorizo la velocidad de
respuesta
Métrica estrella: MRR
Si el usuario necesita la respuesta correcta
en el primer intento (chatbots, asistentes de
soporte), MRR es tu indicador de cabecera.
Un MRR cercano a 1 garantiza que el primer
documento recuperado ya es el relevante.
Priorizo la precisión legal o
médica
Métricas estrella: Faithfulness + NDCG
En entornos de alto riesgo, necesitas saber
que el sistema no alucina (Faithfulness) y
que los documentos más relevantes
aparecen primero (NDCG). La combinación
de ambas cubre integridad factual y calidad
de ranking.
Priorizo el ahorro de costes en
tokens
Métricas estrella: Concisión + Precision@k
Reducir tokens redundantes en la respuesta
(Concisión) y evitar documentos irrelevantes
en el contexto (Precision@k) disminuye
directamente el coste por consulta en APIs
de LLMs como GPT-4 o Claude.
Resumen ejecutivo del módulo
•
Retrieval: Precision@k, Recall@k, MRR, NDCG
•
Generation: Faithfulness, Relevancia, Concisión, BERTScore
•
Fundamento: Golden Dataset bien curado
Espacio para Q&A
¿Qué métrica resulta más difícil de implementar en vuestro contexto?
¿Habéis encontrado tensiones entre Precision y Recall en vuestros
sistemas? ¿Cómo gestionáis la construcción del Golden Dataset en
producción?

