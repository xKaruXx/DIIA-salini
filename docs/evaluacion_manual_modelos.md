# Revision manual de respuestas por modelo local

## Motivo

La comparacion en vivo dentro de la presentacion sirve para mostrar diferencias rapidas entre modelos, pero no alcanza para elegir un modelo productivo. En la primera revision sintetica/automatica se midieron coincidencias de keywords, latencias y resultados de benchmarks reproducibles. Esa revision fue util como filtro inicial, pero no reemplaza la lectura humana de la calidad de respuesta.

En pruebas manuales aparecieron respuestas insatisfactorias: rechazos incorrectos de preguntas dentro del dominio, respuestas demasiado comerciales, respuestas vacias o latencias muy altas en algunos modelos.

Por eso se agrega una matriz para la revision manual del autor sobre 21 preguntas fijas y balanceadas. Esta segunda etapa queda separada de la evaluacion sintetica generada por scripts. La pregunta practica es: que modelo local entrega respuestas mas correctas, utiles y estables para el chatbot de CORADIR Movilidad Electrica segun criterio humano.

## Modelos locales detectados

Ultima revision con `ollama list`:

- `gemma3:270m`
- `granite4:350m`
- `qwen3.5:0.8b`
- `deepseek-r1:1.5b`
- `lfm2.5-thinking:1.2b`
- `llama3.2:3b`
- `nemotron-3-nano:4b`
- `qwen3.5:4b`
- `qwen3.5:latest`
- `gemma4:e4b`

Los modelos de embeddings no se incluyen como modelos de respuesta: `nomic-embed-text`, `nomic-embed-text-v2-moe`, `embeddinggemma` y `qwen3-embedding`.

## Dataset para revision manual

Archivo de casos:

- `dataset/evaluacion_manual_modelos.json`

Incluye 21 preguntas representativas, distribuidas de forma homogenea:

- 7 preguntas factuales claras
- 7 preguntas ambiguas
- 7 preguntas fuera de dominio o no respondibles

La separacion evita que la evaluacion favorezca modelos que solo responden bien preguntas factuales y permite medir tres capacidades distintas: precision factual, manejo de ambiguedad y rechazo correcto.

Cada caso tiene criterios esperados y fallas comunes. La matriz no decide automaticamente si una respuesta es buena: deja columnas para la revision manual del autor.

## Modelos thinking

Algunos modelos, especialmente variantes Qwen y modelos con `thinking` en el nombre, pueden devolver una cadena de razonamiento antes de la respuesta final, muchas veces dentro de bloques `<think>...</think>`. Esa cadena no debe mostrarse ni usarse como respuesta del chatbot.

Para evitar que eso rompa la comparacion:

- el script agrega una instruccion para no mostrar razonamiento
- la llamada a Ollama usa `think: false`, que fue el ajuste efectivo para Qwen y otros modelos reasoning
- si igual aparece un bloque `<think>...</think>`, se remueve antes de guardar la respuesta
- la columna `thinking_removed` indica si se detecto y removio razonamiento
- si el modelo devuelve solo razonamiento y no respuesta final, el estado queda como `thinking_only`

Esto diferencia claramente una respuesta final evaluable de una traza interna de razonamiento.

## Ejecucion

Generar solo una plantilla vacia:

```powershell
py scripts\run_manual_model_evaluation.py --template-only
```

Ejecutar modelos seleccionados:

```powershell
py scripts\run_manual_model_evaluation.py --models gemma3:270m granite4:350m qwen3.5:0.8b lfm2.5-thinking:1.2b llama3.2:3b nemotron-3-nano:4b qwen3.5:4b --timeout 120
```

Ejecutar todos los modelos de chat disponibles en Ollama:

```powershell
py scripts\run_manual_model_evaluation.py --models all --timeout 120
```

## Salidas

El script genera:

- `docs/evaluacion_manual_modelos_respuestas.json`
- `docs/evaluacion_manual_modelos_matriz.csv`
- `docs/evaluacion_manual_modelos_matriz.md`
- `docs/evaluacion_manual_modelos_resumen.md`

El CSV es el archivo principal para revisar manualmente. Las columnas automaticas provienen del script, incluyendo `assistant_score_1_5` y `assistant_notes` como preevaluacion sintetica orientativa. Las siguientes columnas quedan reservadas para la revision manual del autor:

- `manual_correct`: si la respuesta se considera correcta
- `manual_score_1_5`: puntaje manual de 1 a 5
- `manual_notes`: comentario breve sobre errores, omisiones o calidad

La columna `thinking_removed` la completa el script y no requiere revision manual.

La columna `assistant_score_1_5` no reemplaza el criterio manual: es un score preliminar calculado con reglas sobre estado, criterios esperados, rechazo de fuera de dominio y señales de posible alucinacion.

Escala sugerida:

- 1: incorrecta
- 2: pobre
- 3: parcialmente correcta
- 4: correcta con detalles menores
- 5: correcta y util

## Diferencia entre revision sintetica y revision manual

- Revision sintetica/automatica: la realizan los scripts con keywords esperadas, estados `ok/error/timeout`, latencia y salidas reproducibles.
- Revision manual del autor: la completa una persona leyendo cada respuesta y asignando correccion, score y notas.

La matriz debe conservar esa separacion para no presentar como juicio humano lo que fue una medicion automatica.

## Interpretacion

Una respuesta no debe evaluarse solo por si menciona una palabra clave. Tambien importa:

- si responde realmente la pregunta
- si no inventa informacion
- si usa datos concretos cuando corresponden
- si maneja bien preguntas ambiguas
- si rechaza correctamente preguntas fuera de dominio
- si responde en un tiempo aceptable

Los resultados de esta matriz deben usarse para decidir el modelo por defecto o una estrategia mixta: modelo chico para preguntas factuales simples y modelo mas robusto o fallback para preguntas ambiguas o comerciales.
