# Auditoria RAG de Chunks Recuperados

## Resumen ejecutivo

Este reporte recompone la evidencia caso por caso para medir si el sistema esta recuperando los chunks que corresponden. A diferencia del benchmark base, aca se agrega el contenido del chunk, tokens, solapamientos y diagnostico por ranking.

- Casos auditados: 64
- Chunks recuperados auditados: 257
- Casos con alguna fuente esperada en top K: 63/64
- Casos con todas las fuentes esperadas en top K: 61/64
- Casos con fuente esperada en top 1: 56/64
- Precision@K promedio: `0.3188`
- Recall@K promedio: `0.9688`
- Soporte promedio de respuesta en chunks esperados: `0.641`

Archivos generados:

- `docs/auditoria_rag_chunks_clase6.json`: auditoria completa con contenido de chunks y tokens.
- `docs/auditoria_rag_chunks_clase6.csv`: una fila por chunk recuperado.
- `docs/auditoria_rag_chunks_clase6.md`: lectura ejecutiva y casos a revisar.

## Como leer las metricas

| Campo | Lectura |
|---|---|
| `matches_expected_source` | Indica si el `source_path` recuperado coincide con la fuente esperada del caso. |
| `question_token_overlap` | Cuanto de la pregunta aparece en el chunk. Ayuda a ver si el chunk habla del mismo tema. |
| `expected_keyword_overlap` | Cuanto de las keywords esperadas aparece en el chunk. Ayuda a validar si el dato buscado estaba en el contexto. |
| `response_token_support` | Cuanto de la respuesta queda respaldado lexicalmente por el chunk. |
| `keyword_score` | Score de busqueda lexical cuando el documento vino por modo keyword. |
| `vector_rank` | Posicion original en la busqueda vectorial cuando el documento vino por vector. |

## Diagnostico global

| Diagnostico | Casos |
|---|---:|
| `missing_expected_source` | 3 |
| `ok` | 8 |
| `ranking_review` | 7 |
| `review_extra_chunks` | 46 |

## Casos a revisar

| Caso | Categoria | Diagnostico | Ranks relevantes | Recall@K | Precision@K | Top chunks |
|---|---|---|---|---:|---:|---|
| `tito_s5_aa_precio` | precios | `review_extra_chunks` | [1, 2, 3] | 1.0 | 0.6 | #1 OK keyword `Precios_Vehiculos_Actualizados.TITO S5.TITO S5-300` kw=0.5<br>#2 OK keyword `Precios_Vehiculos_Actualizados.TITO S5.TITO S5-300 AA` kw=1.0<br>#3 OK vector `Precios_Vehiculos_Actualizados.TITO S5` kw=1.0 |
| `tita_s2_capacidad` | vehiculos | `review_extra_chunks` | [1, 2] | 1.0 | 0.4 | #1 OK keyword `vehiculos_detalles.TITA S2 300` kw=1.0<br>#2 OK keyword `vehiculos_detalles.TITA S2 300.versiones_disponibles.TITA S2-300` kw=0.0<br>#3 NO vector `todos_los_vehiculos_disponibles.TITA S2` kw=0.0 |
| `tita_furgon_refrigerado_precio` | precios | `review_extra_chunks` | [1, 3, 4] | 1.0 | 0.6 | #1 OK keyword `Precios_Vehiculos_Actualizados.TITA S2.TITA S2 300 AA con Furgón Refrigerado` kw=1.0<br>#2 NO keyword `vehiculos_detalles.TITA S2 300.versiones_disponibles.TITA S2-300 con Furgón Refrigerado` kw=0.0<br>#3 OK vector `Precios_Vehiculos_Actualizados.TITA S2` kw=1.0 |
| `chiki_autonomia_velocidad` | vehiculos | `ranking_review` | [2] | 1.0 | 0.2 | #1 NO keyword `Precios_Vehiculos_Actualizados.CHIKI.CHIKI-L (110KM) LITIO` kw=0.0<br>#2 OK keyword `vehiculos_detalles.CHIKI` kw=1.0<br>#3 NO vector `todos_los_vehiculos_disponibles.CHIKI` kw=0.3333 |
| `barre_tita_capacidad` | vehiculos | `review_extra_chunks` | [1] | 1.0 | 0.2 | #1 OK keyword `vehiculos_detalles.BARRE-TITA` kw=1.0<br>#2 NO keyword `todos_los_vehiculos_disponibles.BARRE-TITA` kw=0.0<br>#3 NO vector `Precios_Vehiculos_Actualizados.TITA 4P Cuadrilla` kw=0.0 |
| `garantia` | posventa | `review_extra_chunks` | [1, 3] | 1.0 | 0.4 | #1 OK keyword `preguntas_frecuentes.mantenimiento[2]` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.general[1]` kw=0.0<br>#3 OK vector `preguntas_frecuentes.mantenimiento[0]` kw=0.0 |
| `reclamos_servicio` | posventa | `review_extra_chunks` | [1, 3] | 1.0 | 0.4 | #1 OK keyword `preguntas_frecuentes.mantenimiento[1]` kw=1.0<br>#2 NO keyword `condiciones_compra_entrega.servicio_entrega` kw=0.0<br>#3 OK vector `contactos.telefono_movilidad_posventa` kw=1.0 |
| `carga_rapida` | carga | `review_extra_chunks` | [1, 2] | 1.0 | 0.4 | #1 OK keyword `preguntas_frecuentes.carga[2]` kw=1.0<br>#2 OK keyword `infraestructura_carga.ecocarga` kw=1.0<br>#3 NO vector `preguntas_frecuentes.adquisicion[1]` kw=0.0 |
| `instalacion_carga` | carga | `review_extra_chunks` | [1, 3, 4] | 1.0 | 0.6 | #1 OK keyword `preguntas_frecuentes.carga[0]` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.vehiculos[1]` kw=0.0<br>#3 OK vector `preguntas_frecuentes.carga[1]` kw=0.0 |
| `reserva_entrega` | compra | `review_extra_chunks` | [1, 3] | 1.0 | 0.4 | #1 OK keyword `condiciones_compra_entrega.entrega_inmediata` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.adquisicion[1]` kw=0.0<br>#3 OK vector `condiciones_compra_entrega.reserva_pago_inicial` kw=0.5 |
| `telefono_ventas` | contacto | `review_extra_chunks` | [1] | 1.0 | 0.2 | #1 OK keyword `contactos.telefono_movilidad_ventas` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.general[0]` kw=0.0<br>#3 NO vector `site_navigation.current_site` kw=0.0 |
| `empresa_que_es_coradir_movilidad` | empresa | `missing_expected_source` | [1] | 0.5 | 0.2 | #1 OK keyword `preguntas_frecuentes.general[0]` kw=1.0<br>#2 NO keyword `sitios_web.movilidad_electrica` kw=0.0<br>#3 NO vector `sitios_web.energias_renovables` kw=0.0 |
| `empresa_donde_se_fabrican` | empresa | `missing_expected_source` | [1] | 0.5 | 0.2 | #1 OK keyword `preguntas_frecuentes.general[1]` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.vehiculos[0]` kw=0.1667<br>#3 NO vector `preguntas_frecuentes.adquisicion[0]` kw=0.0 |
| `empresa_plantas_fabricacion` | empresa | `review_extra_chunks` | [1] | 1.0 | 0.2 | #1 OK keyword `empresa.plantas_fabricacion` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.general[0]` kw=0.0<br>#3 NO vector `empresa.nombre` kw=0.0 |
| `empresa_certificaciones_iso` | empresa | `ranking_review` | [2] | 1.0 | 0.2 | #1 NO keyword `aplicaciones_coradir.contactito_plus` kw=0.0<br>#2 OK keyword `empresa.historia` kw=1.0<br>#3 NO vector `empresa.nombre` kw=0.0 |
| `empresa_valores` | empresa | `missing_expected_source` | [] | 0.0 | 0.0 | #1 NO keyword `preguntas_frecuentes.general[1]` kw=0.0<br>#2 NO keyword `preguntas_frecuentes.vehiculos[0]` kw=0.0<br>#3 NO vector `site_navigation.main_menu` kw=0.0 |
| `movilidad_beneficios_generales` | movilidad | `review_extra_chunks` | [1] | 1.0 | 0.2 | #1 OK keyword `movilidad_electrica.beneficios_generales` kw=1.0<br>#2 NO keyword `preguntas_frecuentes.general[0]` kw=0.0<br>#3 NO vector `sitios_web.energias_renovables` kw=0.0 |
| `movilidad_relacion_gastos` | movilidad | `ranking_review` | [2] | 1.0 | 0.2 | #1 NO keyword `preguntas_frecuentes.general[0]` kw=0.5<br>#2 OK keyword `movilidad_electrica.beneficios_generales` kw=1.0<br>#3 NO vector `sitios_web.movilidad_electrica` kw=0.0 |

## Muestra detallada de casos

### 1. `tito_s5_autonomia_carga` - vehiculos

Pregunta: ¿Cuánta autonomía tiene el TITO S5 y cómo se carga?

Fuentes esperadas: `vehiculos_detalles.TITO`

Recall@K: `1.0` | Precision@K: `0.2` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 12 | `vehiculos_detalles.TITO.modelos_disponibles[1]` | 1.0 | 1.0 | nombre: TITO S5-300 descripcion: Evolución del TITO S2 con avanzada tecnología y características innovadoras, demostr... |
| 2 | no | keyword | 10 | `todos_los_vehiculos_disponibles.TITO S5` | 0.25 | 0.1765 | modelos disponibles: - TITO S5-300 - TITO S5-300 AA disponibilidad: Inmediata - Unidades limitadas |
| 3 | no | vector | 1 | `Precios_Vehiculos_Actualizados.TITO S5` | 0.25 | 0.1765 | TITO S5-300: precio: USD 16.981,25 disponibilidad: Inmediata - Unidades limitadas TITO S5-300 AA: precio: USD 17.731,... |

### 2. `tito_s5_aa_precio` - precios

Pregunta: ¿Cuál es el precio del TITO S5-300 AA?

Fuentes esperadas: `Precios_Vehiculos_Actualizados.TITO S5.TITO S5-300 AA`

Recall@K: `1.0` | Precision@K: `0.6` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 20 | `Precios_Vehiculos_Actualizados.TITO S5.TITO S5-300` | 0.5 | 0.75 | precio: USD 16.981,25 disponibilidad: Inmediata - Unidades limitadas |
| 2 | si | keyword | 20 | `Precios_Vehiculos_Actualizados.TITO S5.TITO S5-300 AA` | 1.0 | 0.75 | precio: USD 17.731,25 disponibilidad: Inmediata - Unidades limitadas |
| 3 | si | vector | 1 | `Precios_Vehiculos_Actualizados.TITO S5` | 1.0 | 1.0 | TITO S5-300: precio: USD 16.981,25 disponibilidad: Inmediata - Unidades limitadas TITO S5-300 AA: precio: USD 17.731,... |
| 4 | no | vector | 3 | `todos_los_vehiculos_disponibles.TITO S5` | 0.0 | 0.0 | modelos disponibles: - TITO S5-300 - TITO S5-300 AA disponibilidad: Inmediata - Unidades limitadas |
| 5 | no | vector | 5 | `Precios_Vehiculos_Actualizados.TITO S2` | 0.5 | 0.5 | TITO S2-300: precio: USD 15.972,50 disponibilidad: Inmediata - Unidades limitadas TITO S2-300 AA: precio: USD 16.722,... |

### 3. `tita_s2_capacidad` - vehiculos

Pregunta: ¿Qué capacidad de carga y de pasajeros tiene la TITA S2-300?

Fuentes esperadas: `vehiculos_detalles.TITA S2 300`

Recall@K: `1.0` | Precision@K: `0.4` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 17 | `vehiculos_detalles.TITA S2 300` | 1.0 | 1.0 | nombre: TITA S2-300 (también conocida como TITA 300) descripcion: Furgoneta eléctrica diseñada para satisfacer las ne... |
| 2 | si | keyword | 15 | `vehiculos_detalles.TITA S2 300.versiones_disponibles.TITA S2-300` | 0.0 | 0.0 | autonomía: 300 Km aire acondicionado: No |
| 3 | no | vector | 1 | `todos_los_vehiculos_disponibles.TITA S2` | 0.0 | 0.0 | modelos disponibles: - TITA S2-300 - TITA S2-300 AA disponibilidad: ENTREGA INMEDIATA |
| 4 | no | vector | 5 | `Precios_Vehiculos_Actualizados.TITO S2` | 0.0 | 0.0 | TITO S2-300: precio: USD 15.972,50 disponibilidad: Inmediata - Unidades limitadas TITO S2-300 AA: precio: USD 16.722,... |

### 4. `tita_furgon_refrigerado_precio` - precios

Pregunta: ¿Cuánto cuesta la TITA S2 300 AA con furgón refrigerado?

Fuentes esperadas: `Precios_Vehiculos_Actualizados.TITA S2.TITA S2 300 AA con Furgón Refrigerado`

Recall@K: `1.0` | Precision@K: `0.6` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 26 | `Precios_Vehiculos_Actualizados.TITA S2.TITA S2 300 AA con Furgón Refrigerado` | 1.0 | 0.6667 | precio: USD 23.632,00 aclaración: El precio 23.632,00 se obtiene de sumar a 17.731,25 USD (precio de TITA S2 300 AA)... |
| 2 | no | keyword | 25 | `vehiculos_detalles.TITA S2 300.versiones_disponibles.TITA S2-300 con Furgón Refrigerado` | 0.0 | 0.5 | autonomía: 300 Km aire acondicionado: Opcional accesorio: Furgón refrigerado descripcion accesorio: Accesorio que con... |
| 3 | si | vector | 1 | `Precios_Vehiculos_Actualizados.TITA S2` | 1.0 | 0.7083 | TITA S2-300: precio: USD 16.981,25 disponibilidad: ENTREGA INMEDIATA TITA S2-300 AA: precio: USD 17.731,25 disponibil... |
| 4 | si | vector | 5 | `Precios_Vehiculos_Actualizados.TITA S2.TITA S2 300 AA con Furgón` | 0.5 | 0.5833 | precio: USD 20.632,00 descripcion: TITA S2 300 AA + accesorio furgón aclaración: El precio 20.632,00 se obtiene de su... |

### 5. `chiki_autonomia_velocidad` - vehiculos

Pregunta: ¿Qué autonomía y velocidad máxima tiene el CHIKI de litio?

Fuentes esperadas: `vehiculos_detalles.CHIKI`

Recall@K: `1.0` | Precision@K: `0.2` | First relevant rank: `2`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | no | keyword | 10 | `Precios_Vehiculos_Actualizados.CHIKI.CHIKI-L (110KM) LITIO` | 0.0 | 0.0 | precio: USD 9.900,00 disponibilidad: ENTREGA A 60 DÍAS |
| 2 | si | keyword | 9 | `vehiculos_detalles.CHIKI` | 1.0 | 1.0 | modelo disponible: nombre: CHIKI-L (110KM) LITIO descripcion: Versión con batería de litio del CHIKI, ofreciendo mayo... |
| 3 | no | vector | 1 | `todos_los_vehiculos_disponibles.CHIKI` | 0.3333 | 0.1304 | modelos disponibles: - CHIKI-L (110KM) LITIO disponibilidad: ENTREGA A 60 DÍAS |
| 4 | no | vector | 5 | `vehiculos_detalles.ACLARACION_IMPORTANTE` | 0.3333 | 0.2174 | nota discrepancia web: IMPORTANTE: La información de este chatbot está más actualizada que la página web. Si encontrá... |

### 6. `barre_tita_capacidad` - vehiculos

Pregunta: ¿Cuál es la capacidad de trabajo y el tanque de agua de la BARRE-TITA?

Fuentes esperadas: `vehiculos_detalles.BARRE-TITA`

Recall@K: `1.0` | Precision@K: `0.2` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 14 | `vehiculos_detalles.BARRE-TITA` | 1.0 | 1.0 | descripcion: Producto revolucionario que se destaca por su rendimiento excepcional en la limpieza de superficies, equ... |
| 2 | no | keyword | 10 | `todos_los_vehiculos_disponibles.BARRE-TITA` | 0.0 | 0.0 | modelos disponibles: - BARRE-TITA disponibilidad: ENTREGA INMEDIATA |
| 3 | no | vector | 3 | `Precios_Vehiculos_Actualizados.TITA 4P Cuadrilla` | 0.0 | 0.0 | TITA 4P-300: precio: USD 17.981,25 disponibilidad: ENTREGA INMEDIATA TITA 4P-300 AA: precio: USD 18.731,25 disponibil... |
| 4 | no | vector | 5 | `Precios_Vehiculos_Actualizados.TITO S5` | 0.0 | 0.0 | TITO S5-300: precio: USD 16.981,25 disponibilidad: Inmediata - Unidades limitadas TITO S5-300 AA: precio: USD 17.731,... |

### 7. `garantia` - posventa

Pregunta: ¿Qué garantía tienen los vehículos?

Fuentes esperadas: `preguntas_frecuentes.mantenimiento`

Recall@K: `1.0` | Precision@K: `0.4` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 10 | `preguntas_frecuentes.mantenimiento[2]` | 1.0 | 0.614 | Pregunta: ¿Qué garantía tienen los vehículos? Respuesta: Todos nuestros vehículos cuentan con una garantía de fábrica... |
| 2 | no | keyword | 5 | `preguntas_frecuentes.general[1]` | 0.0 | 0.2807 | Pregunta: ¿Dónde se fabrican los vehículos eléctricos de Coradir? Respuesta: Nuestros vehículos se fabrican en Argent... |
| 3 | si | vector | 3 | `preguntas_frecuentes.mantenimiento[0]` | 0.0 | 0.0702 | Pregunta: ¿Qué mantenimiento requieren los vehículos eléctricos de Coradir? Respuesta: Nuestros vehículos requieren m... |
| 4 | no | vector | 5 | `preguntas_frecuentes.general[2]` | 0.0 | 0.193 | Pregunta: ¿Se puede circular por autopistas o rutas con estos vehículos? Respuesta: Estos vehiculos están diseñados s... |

### 8. `reclamos_servicio` - posventa

Pregunta: ¿Dónde hago un reclamo o pido servicio técnico?

Fuentes esperadas: `contactos.telefono_movilidad_posventa; preguntas_frecuentes.mantenimiento`

Recall@K: `1.0` | Precision@K: `0.4` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 15 | `preguntas_frecuentes.mantenimiento[1]` | 1.0 | 0.6897 | Pregunta: ¿Dónde puedo realizar el servicio técnico de mi vehículo o efectuar un reclamo? Respuesta: Contamos con una... |
| 2 | no | keyword | 5 | `condiciones_compra_entrega.servicio_entrega` | 0.0 | 0.1379 | disponible: Servicio de entrega a domicilio disponible costo: Costo de flete no incluido en precio final |
| 3 | si | vector | 3 | `contactos.telefono_movilidad_posventa` | 1.0 | 0.3448 | (0266) 5264805 (Se usa para llamar al área posventa y también se usa para servicio técnico y reclamos) |
| 4 | no | vector | 5 | `contactos.telefono_movilidad_ventas` | 0.5 | 0.1379 | (0266) 4305996 (Se usa para llamar al área de ventas de movilidad eléctrica) |

### 9. `leasing_suspendido` - comercial

Pregunta: ¿Tienen leasing o alquiler con opción a compra?

Fuentes esperadas: `leasing_estado_actual`

Recall@K: `1.0` | Precision@K: `0.6` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 8 | `leasing_estado_actual.descripcion` | 1.0 | 0.1842 | La modalidad de leasing (alquiler con opción a compra) de CORADIR está suspendida. |
| 2 | si | keyword | 7 | `leasing_estado_actual.detalle` | 0.5 | 0.3684 | Si un cliente consulta por leasing, aclarar que esta modalidad quedó pausada y sugerir alternativas como compra al co... |
| 3 | si | vector | 5 | `leasing_estado_actual.mensaje_principal` | 0.25 | 0.1842 | Actualmente no ofrecemos planes de leasing activos para ningún modelo. |

### 10. `beneficio_discapacidad` - beneficios

Pregunta: ¿Cómo es el trámite por beneficio de discapacidad?

Fuentes esperadas: `beneficios_discapacidad.tramite_franquicia`

Recall@K: `1.0` | Precision@K: `0.2` | First relevant rank: `1`

| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |
|---:|---|---|---:|---|---:|---:|---|
| 1 | si | keyword | 15 | `beneficios_discapacidad.tramite_franquicia` | 1.0 | 0.8421 | ley aplicable: Según lo que indica la ley 19279, debe realizar el trámite para verificar si se puede acceder a la fra... |
| 2 | no | keyword | 10 | `beneficios_discapacidad.factura_proforma` | 0.4 | 0.0526 | En el caso de aplicar el beneficio por discapacidad, CORADIR confecciona la factura proforma de acuerdo a los requeri... |
| 3 | no | vector | 3 | `beneficios_discapacidad.resolucion_final` | 0.6 | 0.1316 | El Servicio Nacional de Rehabilitación finalmente emitirá el acto administrativo concediendo o denegando el beneficio... |

## Proximo uso recomendado

Usar el CSV para filtrar rapidamente casos donde `matches_expected_source=false` en los primeros puestos o donde `expected_keyword_overlap=0`. Usar el JSON cuando haga falta auditar el contenido completo del chunk y los tokens exactos que justifican cada metrica.
