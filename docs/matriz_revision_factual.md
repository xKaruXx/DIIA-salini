# Matriz de Revision Factual

## Objetivo

Esta matriz sirve para revisar manualmente la fidelidad factual de las respuestas del chatbot. Complementa el benchmark automatico, que actualmente valida palabras clave, con una revision humana orientada a detectar alucinaciones, datos mezclados o informacion adicional innecesaria.

La pregunta central para cada caso es:

> ¿Cada afirmacion de la respuesta esta respaldada por la fuente recuperada?

## Criterio de evaluacion

| Valor | Significado |
|---|---|
| OK | La respuesta esta respaldada por la fuente y responde la consulta |
| Parcial | La respuesta contiene datos correctos, pero agrega informacion innecesaria o incompleta |
| Riesgo | La respuesta mezcla fuentes, extrapola o puede inducir a error |
| Falla | La respuesta no esta respaldada por la fuente o contradice la base |

## Casos recomendados para revision

| # | ID | Categoria | Pregunta | Fuente esperada | Respuesta revisada | Evaluacion | Observacion |
|---:|---|---|---|---|---|---|---|
| 1 | `tito_s5_autonomia_carga` | vehiculos | ¿Cuanta autonomia tiene el TITO S5 y como se carga? | `vehiculos_detalles.TITO` | Pendiente | Pendiente | Verificar autonomia, enchufe y tiempo de carga |
| 2 | `tito_s5_aa_precio` | precios | ¿Cual es el precio del TITO S5-300 AA? | `Precios_Vehiculos_Actualizados.TITO` | Pendiente | Pendiente | Verificar que no mezcle precio sin AA con precio AA |
| 3 | `tita_furgon_refrigerado_precio` | precios | ¿Cuanto cuesta la TITA S2 300 AA con furgon refrigerado? | `Precios_Vehiculos_Actualizados.TITA S2 300` | Pendiente | Pendiente | Verificar calculo de accesorio y precio total |
| 4 | `chiki_autonomia_velocidad` | vehiculos | ¿Que autonomia y velocidad maxima tiene el CHIKI de litio? | `vehiculos_detalles.CHIKI` | Pendiente | Pendiente | Revisar si agrega garantia sin que se haya pedido |
| 5 | `garantia` | posventa | ¿Que garantia tienen los vehiculos? | `preguntas_frecuentes` o seccion de garantia | Pendiente | Pendiente | Verificar si trae mantenimiento adicional innecesario |
| 6 | `reclamos_servicio` | posventa | ¿Donde hago un reclamo o pido servicio tecnico? | seccion de contacto/posventa | Pendiente | Pendiente | Confirmar telefono y derivacion |
| 7 | `leasing_suspendido` | comercial | ¿Tienen leasing o alquiler con opcion a compra? | condiciones comerciales | Pendiente | Pendiente | Confirmar que no prometa modalidad pausada |
| 8 | `beneficio_discapacidad` | beneficios | ¿Como es el tramite por beneficio de discapacidad? | beneficios por discapacidad | Pendiente | Pendiente | Confirmar Ley 19279 y organismo citado |
| 9 | `agencia_san_luis` | agencias | ¿Tienen agencia oficial en San Luis? | agencias oficiales | Pendiente | Pendiente | Confirmar direccion |
| 10 | `reserva_entrega` | compra | ¿Como funciona la reserva y la entrega inmediata? | condiciones de compra | Pendiente | Pendiente | Confirmar monto de reserva y plazo |

## Procedimiento recomendado

1. Ejecutar el benchmark con la variante `strict`.
2. Copiar la respuesta de cada caso critico en la columna "Respuesta revisada".
3. Buscar la fuente esperada en `dataset/knowledge_base_movilidad.jsonl`.
4. Verificar si cada dato de la respuesta aparece en la fuente.
5. Asignar una evaluacion: OK, Parcial, Riesgo o Falla.
6. Registrar la observacion concreta.

## Uso esperado en el informe final

Esta matriz permite afirmar no solo que el sistema "acerto palabras clave", sino que las respuestas estan respaldadas por documentos concretos. Es especialmente importante para consultas de precios, garantias, beneficios, agencias y condiciones comerciales.
