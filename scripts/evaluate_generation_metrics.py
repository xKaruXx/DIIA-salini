from __future__ import annotations

import argparse
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_BENCHMARK_PATH = ROOT_DIR / "docs" / "benchmark_extendido_strict_post_extraccion_v3.json"
DEFAULT_KNOWLEDGE_PATH = ROOT_DIR / "dataset" / "knowledge_base_movilidad.jsonl"
DEFAULT_OUTPUT_JSON = ROOT_DIR / "docs" / "evaluacion_metricas_generacion_clase6.json"
DEFAULT_OUTPUT_MD = ROOT_DIR / "docs" / "evaluacion_metricas_generacion_clase6.md"
DEFAULT_CHART_PATH = ROOT_DIR / "docs" / "charts_presentacion" / "generation_metrics_class6.png"


STOPWORDS = {
    "de",
    "del",
    "la",
    "las",
    "el",
    "los",
    "un",
    "una",
    "y",
    "o",
    "a",
    "en",
    "por",
    "con",
    "para",
    "que",
    "como",
    "cual",
    "cuales",
    "cuanto",
    "cuanta",
    "tiene",
    "tienen",
    "es",
    "son",
    "se",
    "si",
    "no",
    "al",
    "lo",
    "su",
    "sus",
    "este",
    "esta",
    "estos",
    "estas",
    "respuesta",
    "pregunta",
    "nombre",
    "precio",
}


def fix_mojibake(text: str) -> str:
    if not isinstance(text, str):
        return ""
    if not any(marker in text for marker in ("Ã", "Â", "â")):
        return text
    try:
        fixed = text.encode("latin1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        fixed = text
    replacements = {
        "â€“": "-",
        "â€”": "-",
        "â€œ": '"',
        "â€": '"',
        "â€™": "'",
        "â€˜": "'",
        "â€¦": "...",
    }
    for bad, good in replacements.items():
        fixed = fixed.replace(bad, good)
    return fixed


def normalize_text(text: str) -> str:
    fixed = fix_mojibake(text).lower()
    normalized = unicodedata.normalize("NFKD", fixed)
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = normalized.replace("km/h", "kmh")
    normalized = normalized.replace("km / h", "kmh")
    normalized = re.sub(r"(?<=\d),(?=\d)", ".", normalized)
    normalized = re.sub(r"[^a-z0-9.]+", " ", normalized)
    return " ".join(normalized.split())


def tokens(text: str) -> set[str]:
    result = set()
    for raw_token in normalize_text(text).split():
        token = raw_token.strip(".")
        if len(token) <= 1 or token in STOPWORDS:
            continue
        result.add(token)
    return result


def token_overlap(response: str, expected_keywords: list[str]) -> float:
    expected = tokens(" ".join(expected_keywords))
    generated = tokens(response)
    if not expected:
        return 0.0
    return round(len(generated & expected) / len(expected), 4)


def context_faithfulness(response: str, context: str) -> float:
    generated = tokens(response)
    context_tokens = tokens(context)
    if not generated:
        return 0.0
    return round(len(generated & context_tokens) / len(generated), 4)


def normalize_source(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", str(value).lower())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = re.sub(r"[^a-z0-9]+", ".", normalized)
    return normalized.strip(".")


def source_matches(retrieved_source: str, corpus_source: str) -> bool:
    retrieved = normalize_source(retrieved_source)
    corpus = normalize_source(corpus_source)
    if not retrieved or not corpus:
        return False
    return retrieved == corpus or retrieved.startswith(f"{corpus}.") or corpus.startswith(f"{retrieved}.")


def load_corpus(path: Path) -> list[dict]:
    documents = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        documents.append(item)
    return documents


def context_for_sources(retrieved_documents: list[dict], corpus: list[dict]) -> tuple[str, list[str]]:
    context_parts = []
    matched_sources = []
    seen = set()
    for retrieved in retrieved_documents:
        source = retrieved.get("source_path", "")
        if not source:
            continue
        for doc in corpus:
            corpus_source = doc.get("source_path", "")
            if corpus_source in seen:
                continue
            if source_matches(source, corpus_source):
                seen.add(corpus_source)
                matched_sources.append(corpus_source)
                context_parts.append(
                    "\n".join(
                        [
                            str(doc.get("title", "")),
                            str(doc.get("section", "")),
                            str(doc.get("content", "")),
                        ]
                    )
                )
    return "\n\n".join(context_parts), matched_sources


def classify_case(token_score: float, faithfulness_score: float) -> str:
    token_ok = token_score >= 0.85
    faithful = faithfulness_score >= 0.80
    if token_ok and faithful:
        return "sistema_ok"
    if not token_ok and faithful:
        return "respuesta_incompleta_o_retrieval_incorrecto"
    if token_ok and not faithful:
        return "posible_alucinacion_o_contexto_no_trazado"
    return "fallo_total"


def evaluate(benchmark: dict, corpus: list[dict]) -> dict:
    rows = []
    for result in benchmark.get("results", []):
        response = result.get("response", "")
        expected_keywords = result.get("expected_keywords", [])
        context, matched_context_sources = context_for_sources(result.get("retrieved_documents", []), corpus)
        token_score = token_overlap(response, expected_keywords)
        faithfulness_score = context_faithfulness(response, context)
        response_tokens = tokens(response)
        context_tokens = tokens(context)
        unsupported_tokens = sorted(response_tokens - context_tokens)

        rows.append(
            {
                "id": result.get("id"),
                "category": result.get("category"),
                "question": fix_mojibake(result.get("question", "")),
                "passed_keyword_check": result.get("passed"),
                "token_overlap": token_score,
                "context_faithfulness": faithfulness_score,
                "diagnosis": classify_case(token_score, faithfulness_score),
                "response": fix_mojibake(response),
                "expected_keywords": [fix_mojibake(item) for item in expected_keywords],
                "retrieved_sources": [
                    item.get("source_path", "") for item in result.get("retrieved_documents", [])
                ],
                "matched_context_sources": matched_context_sources,
                "unsupported_response_tokens": unsupported_tokens[:20],
            }
        )

    token_scores = [row["token_overlap"] for row in rows]
    faithfulness_scores = [row["context_faithfulness"] for row in rows]
    diagnosis_counts = Counter(row["diagnosis"] for row in rows)
    by_category = defaultdict(list)
    for row in rows:
        by_category[row["category"]].append(row)

    summary = {
        "total_cases": len(rows),
        "mean_token_overlap": round(statistics.mean(token_scores), 4) if token_scores else 0,
        "mean_context_faithfulness": round(statistics.mean(faithfulness_scores), 4) if faithfulness_scores else 0,
        "min_context_faithfulness": round(min(faithfulness_scores), 4) if faithfulness_scores else 0,
        "high_token_overlap_cases": sum(1 for score in token_scores if score >= 0.85),
        "high_faithfulness_cases": sum(1 for score in faithfulness_scores if score >= 0.80),
        "diagnosis_counts": dict(diagnosis_counts),
        "by_category": {
            category: {
                "cases": len(items),
                "mean_token_overlap": round(statistics.mean(item["token_overlap"] for item in items), 4),
                "mean_context_faithfulness": round(
                    statistics.mean(item["context_faithfulness"] for item in items), 4
                ),
            }
            for category, items in sorted(by_category.items())
        },
    }

    return {
        "summary": summary,
        "methodology": {
            "source": "Clase 6 - Metricas de Generacion en RAG",
            "token_overlap": "tokens(respuesta) & tokens(keywords esperadas) / tokens(keywords esperadas)",
            "context_faithfulness": "tokens(respuesta) & tokens(contexto recuperado) / tokens(respuesta)",
            "thresholds": {
                "token_overlap_high": 0.85,
                "context_faithfulness_high": 0.80,
            },
            "important_note": "Estas metricas son proxies automaticos; no reemplazan revision humana de utilidad ni faithfulness semantico.",
        },
        "rows": rows,
    }


def write_chart(report: dict, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows = report["rows"]
    labels = [f"Q{index + 1}" for index in range(len(rows))]
    token_values = [row["token_overlap"] for row in rows]
    faithfulness_values = [row["context_faithfulness"] for row in rows]

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2), facecolor="#0f172a")
    for ax in axes:
        ax.set_facecolor("#111827")
        ax.grid(axis="y", alpha=0.18, color="#94a3b8")
        ax.set_ylim(0, 1.08)
        ax.tick_params(colors="#e5eefb")
        ax.yaxis.label.set_color("#e5eefb")
        ax.title.set_color("#e5eefb")

    axes[0].bar(labels, token_values, color="#14b8a6")
    axes[0].axhline(0.85, color="#facc15", linestyle="--", linewidth=1.2)
    axes[0].set_title("Token Overlap por caso")
    axes[0].set_ylabel("Score 0-1")
    axes[0].set_xticks(range(0, len(labels), 4))
    axes[0].set_xticklabels(labels[::4], rotation=45, ha="right")

    axes[1].bar(labels, faithfulness_values, color="#38bdf8")
    axes[1].axhline(0.80, color="#facc15", linestyle="--", linewidth=1.2)
    axes[1].set_title("Context Faithfulness por caso")
    axes[1].set_ylabel("Score 0-1")
    axes[1].set_xticks(range(0, len(labels), 4))
    axes[1].set_xticklabels(labels[::4], rotation=45, ha="right")

    fig.suptitle(
        "Metricas de generacion - Clase 6\nToken Overlap + Context Faithfulness",
        color="#e5eefb",
        fontweight="bold",
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def write_markdown(report: dict, output_path: Path, benchmark_path: Path, chart_path: Path) -> None:
    summary = report["summary"]
    diagnosis_labels = {
        "sistema_ok": "Sistema OK",
        "respuesta_incompleta_o_retrieval_incorrecto": "Respuesta incompleta o retrieval incorrecto",
        "posible_alucinacion_o_contexto_no_trazado": "Posible alucinacion o contexto no trazado",
        "fallo_total": "Fallo total",
    }
    diagnosis_counts = summary["diagnosis_counts"]
    weakest = sorted(report["rows"], key=lambda row: row["context_faithfulness"])[:8]

    lines = [
        "# Evaluacion de Metricas de Generacion - Clase 6\n\n",
        "## Resumen ejecutivo\n\n",
        "Se incorporo una evaluacion automatica inspirada en la clase 6 para medir la etapa de generacion del RAG, usando el benchmark extendido ya ejecutado. La mejora no vuelve a llamar al LLM: toma las respuestas guardadas, las keywords esperadas y el contexto recuperado para calcular dos proxies reproducibles.\n\n",
        f"- Benchmark evaluado: `{benchmark_path.relative_to(ROOT_DIR)}`\n",
        f"- Casos evaluados: {summary['total_cases']}\n",
        f"- Token Overlap promedio: `{summary['mean_token_overlap']}`\n",
        f"- Context Faithfulness promedio: `{summary['mean_context_faithfulness']}`\n",
        f"- Casos con Token Overlap alto >= 0.85: {summary['high_token_overlap_cases']}/{summary['total_cases']}\n",
        f"- Casos con Context Faithfulness alto >= 0.80: {summary['high_faithfulness_cases']}/{summary['total_cases']}\n\n",
        f"![Metricas de generacion]({chart_path.relative_to(output_path.parent).as_posix()})\n\n",
        "## Metodologia\n\n",
        "### Token Overlap\n\n",
        "Mide si la respuesta contiene los terminos esperados del caso de evaluacion. En este proyecto se calcula contra `expected_keywords`, por lo tanto funciona como proxy de correccion factual automatica.\n\n",
        "Formula: `tokens(respuesta) & tokens(keywords esperadas) / tokens(keywords esperadas)`.\n\n",
        "### Context Faithfulness\n\n",
        "Mide que proporcion de los tokens significativos de la respuesta aparece en el contexto recuperado. Sirve como proxy de alucinacion o de falta de trazabilidad: si una respuesta contiene muchos terminos que no estaban en los chunks recuperados, debe revisarse.\n\n",
        "Formula: `tokens(respuesta) & tokens(contexto recuperado) / tokens(respuesta)`.\n\n",
        "Nota metodologica: estas metricas son automaticas y lexicales. No reemplazan una revision humana de faithfulness semantico, pero agregan una evidencia objetiva y reproducible alineada con la clase 6.\n\n",
        "## Diagnostico por cuadrantes\n\n",
        "| Diagnostico | Casos | Lectura |\n",
        "|---|---:|---|\n",
    ]

    explanations = {
        "sistema_ok": "La respuesta contiene los terminos esperados y esta mayormente respaldada por el contexto recuperado.",
        "respuesta_incompleta_o_retrieval_incorrecto": "El contexto puede ser fiel, pero la respuesta no contiene suficientes terminos esperados.",
        "posible_alucinacion_o_contexto_no_trazado": "La respuesta parece correcta por keywords, pero parte del texto no aparece en el contexto reconstruido.",
        "fallo_total": "La respuesta falla en keywords y ademas no queda respaldada por el contexto.",
    }
    for key in [
        "sistema_ok",
        "respuesta_incompleta_o_retrieval_incorrecto",
        "posible_alucinacion_o_contexto_no_trazado",
        "fallo_total",
    ]:
        lines.append(f"| {diagnosis_labels[key]} | {diagnosis_counts.get(key, 0)} | {explanations[key]} |\n")

    lines.extend(
        [
            "\n## Resultado por categoria\n\n",
            "| Categoria | Casos | Token Overlap prom. | Context Faithfulness prom. |\n",
            "|---|---:|---:|---:|\n",
        ]
    )
    for category, values in summary["by_category"].items():
        lines.append(
            f"| {category} | {values['cases']} | {values['mean_token_overlap']} | {values['mean_context_faithfulness']} |\n"
        )

    lines.extend(
        [
            "\n## Casos a revisar por menor faithfulness\n\n",
            "| Caso | Categoria | Token Overlap | Context Faithfulness | Diagnostico | Tokens no trazados principales |\n",
            "|---|---|---:|---:|---|---|\n",
        ]
    )
    for row in weakest:
        unsupported = ", ".join(row["unsupported_response_tokens"][:8])
        lines.append(
            f"| `{row['id']}` | {row['category']} | {row['token_overlap']} | {row['context_faithfulness']} | {diagnosis_labels[row['diagnosis']]} | {unsupported} |\n"
        )

    lines.extend(
        [
            "\n## Lectura tecnica\n\n",
            "El benchmark final mantiene la evidencia de exactitud por keywords, pero esta mejora suma una segunda lectura: que tan trazable es la respuesta respecto del contexto recuperado. Esto es importante porque un `64/64` por keywords puede ocultar respuestas con informacion adicional innecesaria, duplicaciones o terminos que no aparecen en los chunks reconstruidos.\n\n",
            "La accion recomendada no es cambiar inmediatamente de modelo. La mejora prioritaria es usar esta tabla como control de calidad para revisar respuestas con bajo `Context Faithfulness`, ajustar la capa extractiva cuando agregue datos de mas y, si hace falta, enriquecer el reporte de benchmark para guardar el contexto textual exacto usado al responder.\n\n",
        ]
    )

    output_path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evalua metricas de generacion inspiradas en clase 6.")
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK_PATH)
    parser.add_argument("--knowledge-base", type=Path, default=DEFAULT_KNOWLEDGE_PATH)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--chart", type=Path, default=DEFAULT_CHART_PATH)
    args = parser.parse_args()

    benchmark = json.loads(args.benchmark.read_text(encoding="utf-8"))
    corpus = load_corpus(args.knowledge_base)
    report = evaluate(benchmark, corpus)

    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_chart(report, args.chart)
    write_markdown(report, args.output_md, args.benchmark, args.chart)

    summary = report["summary"]
    print(f"Generado {args.output_json}")
    print(f"Generado {args.output_md}")
    print(f"Generado {args.chart}")
    print(
        "Resumen: "
        f"Token Overlap={summary['mean_token_overlap']} | "
        f"Context Faithfulness={summary['mean_context_faithfulness']}"
    )


if __name__ == "__main__":
    main()
