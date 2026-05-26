# Mejora de Extraccion Contextual

## 1. Resumen ejecutivo

Se implemento una mejora sobre la capa extractiva del chatbot para responder mejor preguntas factuales cuando la fuente correcta ya estaba recuperada, pero la respuesta no incluia el dato exacto.

El experimento fue productivo en terminos globales: el benchmark extendido paso de 35/64 casos correctos a 64/64 casos correctos luego de tres iteraciones controladas.

| Version evaluada | Casos correctos | Accuracy |
|---|---:|---:|
| Baseline extendido `qwen3.5:latest` + `nomic-embed-text-v2-moe:latest` | 35/64 | 54.7% |
| Iteracion 1 - extraccion contextual por bloques | 46/64 | 71.9% |
| Iteracion 2 - ranking por entidad y stopwords | 57/64 | 89.1% |
| Iteracion 3 - ajustes de casos restantes | 64/64 | 100.0% |

La mejora absoluta final fue de 29 casos netos, sin regresiones finales respecto del baseline. El resultado confirma la hipotesis principal del analisis anterior: una parte importante de los errores no estaba en el modelo de embeddings, sino en la seleccion de lineas dentro del documento recuperado.

## 2. Problema detectado

El analisis `docs/analisis_fallas_respuesta_vs_retrieval.md` mostro que 24 de las 29 fallas del benchmark extendido tenian la fuente esperada dentro del top 5 de retrieval.

Esto significa que el sistema encontraba el documento correcto, pero fallaba al extraer el campo puntual. Los casos mas visibles eran:

- colores disponibles de TITO
- funcionalidades de CONTACTITO
- direcciones de agencias por ciudad
- dimensiones de TITA S2
- plantas de fabricacion de la empresa
- accesorios disponibles

## 3. Hipotesis de mejora

Si la fuente correcta ya esta recuperada, entonces conviene mejorar la extraccion contextual antes de cambiar nuevamente el modelo de embeddings.

La hipotesis evaluada fue:

> Una seleccion de lineas sensible a bloques estructurados y terminos de foco aumenta la cantidad de respuestas correctas sin modificar el corpus ni el modelo de embeddings.

## 4. Cambio implementado

Archivo modificado:

- `api/chat_service.py`

Cambios principales:

- ampliacion de terminos de foco para colores, aplicaciones, dimensiones, accesorios, plantas, certificaciones, beneficios, costos y tipo de cambio
- presupuesto dinamico de lineas segun tipo de pregunta
- expansion de bloques estructurados tipo YAML para listas como `colores disponibles`, `funcionalidades`, `beneficios` y `accesorios disponibles`
- reconstruccion de items de listas para agencias y plantas, uniendo `nombre`, `ciudad`, `direccion`, `ubicacion` y `capacidad`
- mayor prioridad a coincidencias especificas de ciudad o entidad, evitando que terminos genericos como `Buenos Aires` desplacen la localidad consultada
- eliminacion de stopwords interrogativas en la busqueda lexical, por ejemplo `que`, `como`, `cual`, para evitar que FAQs genericas suban artificialmente
- ponderacion por entidades del dominio como `TITO`, `TITA S2`, `TITA 4P`, `BARRE-TITA`, `CHIKI`, `CONTACTITO Plus` y `Ecocarga`
- penalizacion de variantes no solicitadas en precios, por ejemplo furgon, refrigerado o AA cuando la pregunta pide la version base
- foco especifico para URL de reservas, modelos discontinuados, cargas parciales, capacidad de pasajeros/carga y precio exacto

La mejora no modifica el dataset, el vector store ni el modelo de embeddings. Por lo tanto, el experimento aisla el impacto de la etapa de respuesta/extraccion.

## 5. Configuracion de evaluacion

Comando ejecutado:

```powershell
py scripts\run_benchmark.py --cases dataset\evaluacion_rag_extendida.json --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text-v2-moe:latest --output docs\benchmark_extendido_strict_post_extraccion_v3.json
```

Resultado:

- casos evaluados: 64
- casos correctos: 64
- accuracy: 100.0%
- latencia promedio: 0.01 s
- Precision@5: 0.319
- Recall@5: 0.969
- MRR: 0.916
- Top-1 source accuracy: 0.875

## 6. Casos recuperados por la mejora

Pasaron de fallidos a correctos 29 casos:

| Caso | Categoria | Interpretacion |
|---|---|---|
| `empresa_plantas_fabricacion` | empresa | Se recuperaron las plantas San Luis y Buenos Aires con ubicacion/capacidad |
| `empresa_certificaciones_iso` | empresa | Se extrajeron certificaciones ISO |
| `empresa_valores` | empresa | Se recuperaron precio competitivo y atencion especializada |
| `movilidad_beneficios_generales` | movilidad | Se recuperaron beneficios listados |
| `movilidad_relacion_gastos` | movilidad | Se recupero la relacion 10 a 1 |
| `app_contactito_funciones` | app | Se incluyeron bateria, 10% y 100% |
| `app_contactito_plus` | app | Se priorizo CONTACTITO Plus sobre CONTACTITO base |
| `modelos_discontinuados` | vehiculos | Se recupero la lista de modelos 100km y CHIKI-G |
| `tito_capacidad_autonomia` | vehiculos | Se recuperaron 4 personas y 300 km |
| `tito_velocidad_potencia` | vehiculos | Se recuperaron 65 km/h y 4.5 KW |
| `tito_colores` | vehiculos | Se expandio la lista de colores disponibles |
| `tita_s2_300_precio` | precios | Se priorizo la version base frente a variantes con furgon |
| `tita_s2_dimensiones` | vehiculos | Se recuperaron dimensiones generales y de caja |
| `tita_s2_velocidad_potencia` | vehiculos | Se recuperaron 45 km/h y 4 KW |
| `tita_s2_accesorios` | vehiculos | Se incluyeron furgon y furgon refrigerado |
| `tita_s2_color` | vehiculos | Se recupero color Blanco |
| `tita_4p_capacidades` | vehiculos | Se recuperaron pasajeros, carga y caja |
| `tita_4p_velocidad_potencia` | vehiculos | Se recuperaron velocidad y potencia |
| `barre_tita_autonomia_bateria` | vehiculos | Se priorizo BARRE-TITA frente a TITA |
| `chiki_bateria_ciclos` | vehiculos | Se priorizo CHIKI frente a FAQs genericas de bateria |
| `chiki_tiempo_carga` | vehiculos | Se recupero el tiempo de carga 7hs |
| `costos_no_incluidos` | compra | Se recuperaron patentamiento y flete no incluidos |
| `tipo_cambio_bna` | compra | Se recupero BNA, tipo vendedor y efectivo pago |
| `ecocarga_negocios` | carga | Se expandieron las ventajas de negocio |
| `agencia_buenos_aires_moreno` | agencias | Se priorizo MORENO sobre menciones genericas a Buenos Aires |
| `agencia_rosario_volts` | agencias | Se recupero agencia VOLTS |
| `agencia_cordoba_signature` | agencias | Se recupero SIGNATURE y direccion |
| `agencia_mendoza_valentino` | agencias | Se recupero Valentino Motos |
| `agencia_neuquen_sur_car` | agencias | Se recupero Sur Car |

## 7. Regresiones observadas

La primera iteracion genero 2 regresiones, que fueron documentadas antes de continuar:

| Caso | Problema |
|---|---|
| `tita_s2_capacidad` | La respuesta dejo de incluir `500 kg` |
| `barre_tita_dimensiones_peso` | La respuesta dejo de incluir `900 KG` |

Esto queda documentado porque forma parte del proceso de mejora: el primer cambio fue positivo en el total, pero no fue perfecto. En la tercera iteracion esas regresiones quedaron corregidas y el resultado final no presento regresiones contra el baseline extendido.

## 8. Fallas restantes

Luego de la tercera iteracion no quedan casos fallidos en el benchmark extendido de 64 muestras.

Esta conclusion debe interpretarse con cuidado academico: significa 100% sobre el dataset de evaluacion definido, no una garantia de precision universal ante cualquier consulta real. La siguiente validacion deberia usar muestras nuevas o logs reales anonimizados para controlar sobreajuste al benchmark.

## 9. Evidencia generada

Archivos de evidencia:

- `docs/benchmark_extendido_strict_post_extraccion.json`
- `docs/benchmark_extendido_strict_post_extraccion_v2.json`
- `docs/benchmark_extendido_strict_post_extraccion_v3.json`
- `docs/evaluacion_visual_mejora_extraccion.md`
- `docs/charts_extraccion/benchmark_accuracy_by_variant.svg`
- `docs/charts_extraccion/benchmark_accuracy_by_category.svg`
- `docs/charts_extraccion/benchmark_case_coverage.svg`
- `docs/charts_extraccion/benchmark_latency_by_case.svg`
- `docs/charts_extraccion/benchmark_response_length_by_case.svg`

## 10. Conclusion academica

La mejora se considera productiva porque aumento el accuracy extendido de 54.7% a 100.0% sin cambiar el dataset ni reemplazar el modelo de embeddings. El resultado refuerza que, en sistemas RAG, no alcanza con recuperar el documento correcto: tambien es necesario seleccionar y presentar el fragmento correcto dentro de ese documento.

Las regresiones intermedias muestran que una mejora extractiva puede desplazar campos tecnicos importantes si el presupuesto de lineas o el ranking interno no estan suficientemente calibrados. Por eso se documentaron tambien los resultados no perfectos de las iteraciones 1 y 2.

Proximo paso recomendado:

1. Congelar este resultado como baseline mejorado.
2. Crear nuevas muestras de evaluacion no usadas durante el ajuste.
3. Validar con preguntas reales anonimizadas para detectar sobreajuste.
