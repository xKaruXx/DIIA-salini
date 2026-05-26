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
DEFAULT_INPUT = ROOT_DIR / "dataset" / "knowledge_base_movilidad.jsonl"
DEFAULT_OUTPUT_JSON = ROOT_DIR / "docs" / "eda_corpus_rag.json"
DEFAULT_OUTPUT_MD = ROOT_DIR / "docs" / "eda_corpus_rag.md"
DEFAULT_CHART_DIR = ROOT_DIR / "docs" / "charts_corpus"


def normalize_text(value: str) -> str:
    text = unicodedata.normalize("NFKD", str(value).lower())
    text = "".join(char for char in text if not unicodedata.combining(char))
    return text


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", normalize_text(value))


def ttr(tokens: list[str]) -> float:
    return len(set(tokens)) / len(tokens) if tokens else 0


def mattr(tokens: list[str], window: int = 50) -> float:
    if not tokens:
        return 0
    if len(tokens) <= window:
        return ttr(tokens)
    scores = [ttr(tokens[index : index + window]) for index in range(0, len(tokens) - window + 1)]
    return sum(scores) / len(scores)


def load_records(path: Path) -> list[dict]:
    records = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0
    ordered = sorted(values)
    index = (len(ordered) - 1) * p
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def analyze(records: list[dict], mattr_window: int) -> dict:
    documents = []
    section_counts = Counter()
    section_tokens = defaultdict(list)

    for record in records:
        content = record.get("content", "")
        tokens = tokenize(content)
        token_count = len(tokens)
        type_count = len(set(tokens))
        doc = {
            "id": record.get("id", ""),
            "section": record.get("section", ""),
            "title": record.get("title", ""),
            "source_path": record.get("source_path", ""),
            "token_count": token_count,
            "type_count": type_count,
            "ttr": round(ttr(tokens), 4),
            "mattr": round(mattr(tokens, mattr_window), 4),
        }
        if token_count < 30:
            doc["length_flag"] = "too_short"
        elif token_count > 300:
            doc["length_flag"] = "too_long"
        else:
            doc["length_flag"] = "ok"

        if doc["mattr"] < 0.4:
            doc["lexical_flag"] = "low_density"
        elif doc["mattr"] > 0.6:
            doc["lexical_flag"] = "high_density"
        else:
            doc["lexical_flag"] = "medium_density"

        documents.append(doc)
        section_counts[doc["section"]] += 1
        section_tokens[doc["section"]].append(token_count)

    token_counts = [doc["token_count"] for doc in documents]
    ttr_values = [doc["ttr"] for doc in documents]
    mattr_values = [doc["mattr"] for doc in documents]

    summary = {
        "total_documents": len(documents),
        "total_tokens": sum(token_counts),
        "token_count": {
            "min": min(token_counts) if token_counts else 0,
            "max": max(token_counts) if token_counts else 0,
            "mean": round(statistics.mean(token_counts), 2) if token_counts else 0,
            "median": round(statistics.median(token_counts), 2) if token_counts else 0,
            "p90": round(percentile(token_counts, 0.9), 2),
        },
        "ttr": {
            "mean": round(statistics.mean(ttr_values), 4) if ttr_values else 0,
            "median": round(statistics.median(ttr_values), 4) if ttr_values else 0,
        },
        "mattr": {
            "window": mattr_window,
            "mean": round(statistics.mean(mattr_values), 4) if mattr_values else 0,
            "median": round(statistics.median(mattr_values), 4) if mattr_values else 0,
        },
        "length_flags": dict(Counter(doc["length_flag"] for doc in documents)),
        "lexical_flags": dict(Counter(doc["lexical_flag"] for doc in documents)),
        "sections": {
            section: {
                "documents": count,
                "mean_tokens": round(statistics.mean(section_tokens[section]), 2),
            }
            for section, count in sorted(section_counts.items())
        },
    }

    return {
        "summary": summary,
        "documents": documents,
    }


def write_charts(report: dict, chart_dir: Path) -> None:
    chart_dir.mkdir(parents=True, exist_ok=True)
    documents = report["documents"]
    plt.rcParams.update({"font.family": "DejaVu Sans"})

    token_counts = [doc["token_count"] for doc in documents]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(token_counts, bins=18, color="#14b8a6", edgecolor="#0f172a")
    ax.set_title("Distribucion de longitud por documento")
    ax.set_xlabel("Tokens")
    ax.set_ylabel("Documentos")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(chart_dir / "corpus_token_distribution.png", dpi=180)
    plt.close(fig)

    lexical_counts = Counter(doc["lexical_flag"] for doc in documents)
    labels = ["low_density", "medium_density", "high_density"]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(labels, [lexical_counts.get(label, 0) for label in labels], color=["#ea580c", "#2563eb", "#14b8a6"])
    ax.set_title("Densidad lexica por MATTR")
    ax.set_ylabel("Documentos")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(chart_dir / "corpus_mattr_flags.png", dpi=180)
    plt.close(fig)

    section_items = sorted(report["summary"]["sections"].items(), key=lambda item: item[1]["documents"], reverse=True)
    labels = [item[0] for item in section_items]
    values = [item[1]["documents"] for item in section_items]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(labels, values, color="#38bdf8")
    ax.invert_yaxis()
    ax.set_title("Documentos por seccion")
    ax.set_xlabel("Documentos")
    fig.tight_layout()
    fig.savefig(chart_dir / "corpus_documents_by_section.png", dpi=180)
    plt.close(fig)


def write_markdown(report: dict, output_path: Path, chart_dir: Path) -> None:
    summary = report["summary"]
    docs = report["documents"]
    too_short = [doc for doc in docs if doc["length_flag"] == "too_short"]
    too_long = [doc for doc in docs if doc["length_flag"] == "too_long"]
    low_density = [doc for doc in docs if doc["lexical_flag"] == "low_density"]

    lines = [
        "# EDA del Corpus RAG\n\n",
        "## Resumen ejecutivo\n\n",
        "Este reporte aplica el criterio del material de clase 4 sobre riqueza lexica y calidad de chunks al corpus usado por el chatbot. ",
        "El objetivo es decidir con evidencia si conviene cambiar chunking, metadata o normalizacion antes de indexar.\n\n",
        "## Metricas generales\n\n",
        f"- Documentos analizados: {summary['total_documents']}\n",
        f"- Tokens totales: {summary['total_tokens']}\n",
        f"- Tokens por documento: media {summary['token_count']['mean']}, mediana {summary['token_count']['median']}, p90 {summary['token_count']['p90']}, maximo {summary['token_count']['max']}\n",
        f"- TTR promedio: {summary['ttr']['mean']}\n",
        f"- MATTR promedio: {summary['mattr']['mean']} con ventana {summary['mattr']['window']}\n",
        f"- Documentos demasiado cortos: {len(too_short)}\n",
        f"- Documentos demasiado largos: {len(too_long)}\n",
        f"- Documentos con baja densidad lexica: {len(low_density)}\n\n",
        "## Graficos\n\n",
        f"![Distribucion de tokens]({chart_dir.name}/corpus_token_distribution.png)\n\n",
        f"![Densidad MATTR]({chart_dir.name}/corpus_mattr_flags.png)\n\n",
        f"![Documentos por seccion]({chart_dir.name}/corpus_documents_by_section.png)\n\n",
        "## Lectura tecnica\n\n",
    ]

    if too_long:
        lines.append(
            "Hay documentos largos que pueden enviar demasiado contexto junto. Conviene revisar si deben subdividirse o enriquecerse con metadata mas especifica.\n\n"
        )
    else:
        lines.append("No aparecen documentos excesivamente largos bajo el umbral definido de 300 tokens.\n\n")

    if too_short:
        lines.append(
            "Hay documentos muy cortos. No necesariamente son malos: pueden ser utiles si contienen datos puntuales como telefonos, precios o condiciones. Deben revisarse por seccion antes de fusionarlos.\n\n"
        )

    if low_density:
        lines.append(
            "Los documentos con baja MATTR deben revisarse antes de aplicar lematizacion. En este dominio hay nombres de modelos, versiones y valores comerciales; una normalizacion agresiva podria dañar la precision.\n\n"
        )
    else:
        lines.append(
            "La MATTR no sugiere una necesidad inmediata de lematizacion agresiva. La mejora mas prudente es medir retrieval y enriquecer metadata antes de transformar lexicalmente el corpus.\n\n"
        )

    lines.extend(
        [
            "## Top documentos a revisar\n\n",
            "| Motivo | Seccion | Titulo | Tokens | MATTR | Fuente |\n",
            "|---|---|---|---:|---:|---|\n",
        ]
    )
    review_candidates = (
        [(doc, "muy largo") for doc in sorted(too_long, key=lambda item: item["token_count"], reverse=True)[:8]]
        + [(doc, "muy corto") for doc in sorted(too_short, key=lambda item: item["token_count"])[:8]]
        + [(doc, "baja MATTR") for doc in sorted(low_density, key=lambda item: item["mattr"])[:8]]
    )
    for doc, reason in review_candidates[:20]:
        lines.append(
            f"| {reason} | {doc['section']} | {doc['title']} | {doc['token_count']} | {doc['mattr']} | `{doc['source_path']}` |\n"
        )

    lines.extend(
        [
            "\n## Decision recomendada\n\n",
            "1. No aplicar lematizacion global todavia.\n",
            "2. Priorizar metricas de retrieval con fuentes esperadas.\n",
            "3. Enriquecer metadata de dominio para mejorar filtros y diagnostico.\n",
            "4. Revisar manualmente documentos extremos antes de cambiar el chunking.\n",
        ]
    )

    output_path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analiza longitud y riqueza lexica del corpus RAG.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--chart-dir", type=Path, default=DEFAULT_CHART_DIR)
    parser.add_argument("--mattr-window", type=int, default=50)
    args = parser.parse_args()

    records = load_records(args.input)
    report = analyze(records, args.mattr_window)
    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    write_charts(report, args.chart_dir)
    write_markdown(report, args.output_md, args.chart_dir)

    summary = report["summary"]
    print(f"Documentos: {summary['total_documents']}")
    print(f"Tokens promedio: {summary['token_count']['mean']}")
    print(f"MATTR promedio: {summary['mattr']['mean']}")
    print(f"Reporte: {args.output_md}")


if __name__ == "__main__":
    main()
