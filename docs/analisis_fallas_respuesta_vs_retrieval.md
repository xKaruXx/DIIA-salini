# Analisis de Fallas: Respuesta vs Retrieval

## Resumen ejecutivo

Se cruzaron los resultados del benchmark extendido de respuesta con el benchmark de retrieval hibrido usando `nomic-embed-text-v2-moe:latest`.

Resultado principal:

- 35 casos pasaron la validacion por keywords.
- 29 casos fallaron la validacion por keywords.
- De esos 29 fallos, 24 tenian la fuente esperada recuperada dentro del top 5.
- Solo 5 fallos no tenian la fuente esperada en top 5.

Esto indica que la principal oportunidad de mejora no esta solo en el retrieval. En la mayoria de los fallos, el sistema ya recupera la fuente correcta, pero la respuesta final no incluye las keywords esperadas o no extrae el dato exacto.

## Insumos usados

| Archivo | Uso |
|---|---|
| `docs/benchmark_extendido_strict_qwen35_nomic_v2_moe.json` | Resultado de respuestas sobre 64 casos |
| `docs/benchmark_retrieval_extendido_hybrid_v2_moe_fresh.json` | Resultado de retrieval hibrido sobre 64 casos |
| `dataset/evaluacion_rag_extendida.json` | Casos con keywords y fuentes esperadas |

## Clasificacion de resultados

| Clasificacion | Casos | Interpretacion |
|---|---:|---|
| Respuesta correcta | 35 | La respuesta contiene las keywords esperadas |
| Falla de respuesta con fuente recuperada | 24 | El contexto correcto estaba disponible, pero la respuesta no incluyo el dato esperado |
| Falla de retrieval o fuente fuera de top 5 | 5 | El sistema no puso la fuente esperada dentro del top 5 |

## Fallas por categoria

| Categoria | Respuesta correcta | Falla con fuente recuperada | Falla de retrieval |
|---|---:|---:|---:|
| agencias | 1 | 5 | 0 |
| app | 0 | 2 | 0 |
| beneficios | 1 | 0 | 0 |
| carga | 3 | 1 | 0 |
| comercial | 1 | 0 | 0 |
| compra | 3 | 2 | 0 |
| contacto | 1 | 0 | 0 |
| empresa | 2 | 0 | 3 |
| movilidad | 0 | 1 | 1 |
| posventa | 2 | 0 | 0 |
| precios | 11 | 1 | 0 |
| sitios_web | 1 | 0 | 0 |
| vehiculos | 9 | 12 | 1 |

## Fallas con fuente recuperada

Estos casos son prioritarios para mejorar extraccion, ranking interno de lineas o generacion:

| Caso | Categoria | Rank primera fuente | Keywords faltantes |
|---|---|---:|---|
| `movilidad_beneficios_generales` | movilidad | 2 | `220v`, `silencioso`, `sin emisiones` |
| `app_contactito_funciones` | app | 1 | `batería`, `10%`, `100%` |
| `app_contactito_plus` | app | 1 | `historial`, `ubicación` |
| `modelos_discontinuados` | vehiculos | 3 | `100km`, `discontinuados`, `CHIKI-G` |
| `tito_velocidad_potencia` | vehiculos | 2 | `4.5 KW` |
| `tito_colores` | vehiculos | 1 | `Rosa`, `Verde`, `Bicolor` |
| `tita_s2_300_precio` | precios | 1 | `16.981,25` |
| `tita_s2_dimensiones` | vehiculos | 1 | `3750x1370x1720`, `2000x1310x350` |
| `tita_s2_velocidad_potencia` | vehiculos | 1 | `4 KW` |
| `tita_s2_accesorios` | vehiculos | 1 | `Furgón Refrigerado` |
| `tita_s2_color` | vehiculos | 1 | `Blanco` |
| `tita_4p_capacidades` | vehiculos | 1 | `4 personas` |
| `tita_4p_velocidad_potencia` | vehiculos | 1 | `4Kw` |
| `barre_tita_autonomia_bateria` | vehiculos | 1 | `Litio 7,2 Kwh` |
| `chiki_bateria_ciclos` | vehiculos | 3 | `Litio NCM 4,5 KWh`, `2000 ciclos` |
| `chiki_tiempo_carga` | vehiculos | 5 | `7hs` |
| `costos_no_incluidos` | compra | 4 | `patentamiento`, `flete`, `NO están incluidos` |
| `tipo_cambio_bna` | compra | 3 | `BNA`, `tipo vendedor`, `efectivo pago` |
| `ecocarga_negocios` | carga | 3 | `Atrae nuevos clientes`, `Instalación gratuita`, `Ingresos adicionales` |
| `agencia_buenos_aires_moreno` | agencias | 1 | `CHIAMO MOTORS`, `Acceso Oeste Sur 12.802` |
| `agencia_rosario_volts` | agencias | 1 | `VOLTS` |
| `agencia_cordoba_signature` | agencias | 2 | `SIGNATURE`, `Av. Colon 4875` |
| `agencia_mendoza_valentino` | agencias | 1 | `Valentino Motos` |
| `agencia_neuquen_sur_car` | agencias | 1 | `Sur Car` |

## Fallas de retrieval

Estos casos requieren mejorar recuperacion, segmentacion o expected sources:

| Caso | Categoria | Keywords faltantes |
|---|---|---|
| `empresa_plantas_fabricacion` | empresa | `Planta San Luis`, `Planta Buenos Aires`, `Uspallata 2853` |
| `empresa_certificaciones_iso` | empresa | `ISO 9001`, `ISO 14001` |
| `empresa_valores` | empresa | `precio competitivo`, `atención especializada` |
| `movilidad_relacion_gastos` | movilidad | `10 a 1` |
| `tito_capacidad_autonomia` | vehiculos | `4 personas` |

## Interpretacion academica

La prueba fue productiva aunque expuso fallas. De hecho, el hallazgo mas importante es que la mayoria de los errores no son errores de recuperacion: en 24 de 29 fallos, el sistema tenia la fuente correcta dentro del top 5.

Esto cambia la prioridad de mejora:

1. Mejorar extraccion de lineas y seleccion de datos dentro de fuentes recuperadas.
2. Revisar si algunas keywords esperadas son demasiado estrictas o no coinciden con la forma real de respuesta.
3. Mantener el retrieval hibrido con `nomic-embed-text-v2-moe:latest`, porque ofrece buen Recall@5.
4. Solo despues optimizar la segmentacion o el vector store para los 5 casos donde la fuente no aparece.

## Proximo experimento recomendado

Implementar una mejora en la capa extractiva para consultas que piden:

- listas de colores
- direcciones de agencias
- campos tecnicos exactos
- beneficios listados
- costos no incluidos

Luego repetir:

```powershell
py scripts\run_benchmark.py --cases dataset\evaluacion_rag_extendida.json --prompt-variant strict --llm-provider ollama --chat-model qwen3.5:latest --embedding-provider ollama --embedding-model nomic-embed-text-v2-moe:latest --output docs\benchmark_extendido_strict_post_extraccion.json
```

La mejora se consideraria productiva si reduce los 24 casos de "falla con fuente recuperada".
