# Informe Técnico — proyecto Overleaf

Carpeta autocontenida del informe final (Track A — RAG/Chatbot).

## Cómo compilar

1. Comprimir esta carpeta (`informe_tecnico.tex` + `figs/`) en un ZIP.
2. En [Overleaf](https://www.overleaf.com): **New Project → Upload Project** y subir el ZIP.
3. Compilador: **pdfLaTeX** (default). Compilar dos veces para que el índice y las referencias cruzadas queden resueltos (Overleaf lo hace solo).

No requiere paquetes fuera de TeX Live estándar.

## Contenido

- `informe_tecnico.tex` — documento completo (6 secciones + referencias + anexos).
- `figs/arquitectura_pipeline.png` — diagrama propio del pipeline (fuente Mermaid en `arquitectura_pipeline.mmd`; regenerar con `npx @mermaid-js/mermaid-cli -i arquitectura_pipeline.mmd -o figs/arquitectura_pipeline.png -b white -s 2`).
- `figs/corpus_*.png` — gráficos del EDA (generados por los scripts del repo).
- `figs/manual_model_tradeoff.png` — trade-off de selección de LLM.

## Trazabilidad de cifras

Toda cifra del informe sale de un JSON versionado en `docs/`:

| Cifra | Fuente |
|---|---|
| 35/64 → 46 → 57 → 64/64 | `benchmark_extendido_strict_qwen35_nomic_text.json`, `benchmark_extendido_strict_post_extraccion{,_v2,_v3}.json` |
| Recall@5 0.969 · P@5 0.319 · MRR 0.916 · Top-1 0.875 · rank medio 1.22 | `auditoria_rag_chunks_clase6.json` |
| Token Overlap 1.0 · Faithfulness 0.895 · 51/64 | `evaluacion_metricas_generacion_clase6.json` |
| Matriz embeddings (4 modelos) | `evaluacion_embeddings_locales.md` |
| Matriz LLMs (11 modelos, 21 preguntas) | `evaluacion_manual_modelos_resumen.md` / `_matriz.csv` |
| EDA corpus (111 docs, 4907 tokens, MATTR 0.854) | `eda_corpus_rag.json` / `.md` |
