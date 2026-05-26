import argparse
import json
import math
import re
from collections import Counter, defaultdict
from html import escape
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_REPORTS = [
    ROOT_DIR / "docs" / "benchmark_real_strict_qwen35_latest.json",
    ROOT_DIR / "docs" / "benchmark_real_sales_qwen35_latest.json",
]
DEFAULT_OUTPUT_DIR = ROOT_DIR / "docs" / "charts"
DEFAULT_MD_PATH = ROOT_DIR / "docs" / "evaluacion_visual_benchmark.md"


def fix_mojibake(text: str) -> str:
    if not any(marker in text for marker in ("\u00c3", "\u00c2", "\u00e2")):
        return text
    try:
        fixed = text.encode("latin1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        fixed = text
    replacements = {
        "â€“": "-",
        "â€”": "-",
        "â€œ": '"',
        "â€\u009d": '"',
        "â€™": "'",
        "â€˜": "'",
        "â€¦": "...",
    }
    for bad, good in replacements.items():
        fixed = fixed.replace(bad, good)
    return fixed


def normalize_strings(value: Any) -> Any:
    if isinstance(value, str):
        return fix_mojibake(value)
    if isinstance(value, list):
        return [normalize_strings(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_strings(item) for key, item in value.items()}
    return value


def load_report(path: Path, rewrite_normalized: bool) -> dict[str, Any]:
    report = json.loads(path.read_text(encoding="utf-8"))
    report = normalize_strings(report)
    if rewrite_normalized:
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def variant(report: dict[str, Any]) -> str:
    return report["summary"]["prompt_variant"]


def report_label(report: dict[str, Any], include_embedding: bool = False) -> str:
    if report.get("_chart_label"):
        return str(report["_chart_label"])

    summary = report["summary"]
    label = summary["prompt_variant"]
    if include_embedding:
        embedding = summary.get("embedding_model_name", "")
        embedding = embedding.replace(":latest", "")
        embedding = embedding.replace("nomic-embed-", "")
        label = f"{label} / {embedding}"
    return label


def safe_id(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def svg_header(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#1f2933}",
        ".title{font-size:20px;font-weight:700}",
        ".subtitle{font-size:12px;fill:#52616b}",
        ".axis{stroke:#9aa5b1;stroke-width:1}",
        ".grid{stroke:#e4e7eb;stroke-width:1}",
        ".label{font-size:11px}",
        ".tick{font-size:10px;fill:#52616b}",
        ".value{font-size:11px;font-weight:700}",
        ".legend{font-size:12px}",
        "</style>",
    ]


def write_svg(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def bar_chart(
    path: Path,
    title: str,
    labels: list[str],
    series: dict[str, list[float]],
    y_label: str,
    y_max: float | None = None,
    value_suffix: str = "",
    decimals: int = 0,
) -> None:
    width = 980
    height = 520
    margin = {"left": 70, "right": 30, "top": 72, "bottom": 92}
    chart_w = width - margin["left"] - margin["right"]
    chart_h = height - margin["top"] - margin["bottom"]
    colors = ["#2f80ed", "#27ae60", "#f2994a", "#9b51e0"]
    all_values = [value for values in series.values() for value in values]
    y_top = y_max if y_max is not None else max(all_values + [1])
    if y_top <= 0:
        y_top = 1
    y_top = y_top * 1.12

    lines = svg_header(width, height)
    lines.append(f'<text x="{margin["left"]}" y="32" class="title">{escape(title)}</text>')
    lines.append(f'<text x="{margin["left"]}" y="52" class="subtitle">{escape(y_label)}</text>')

    for i in range(6):
        value = y_top * i / 5
        y = margin["top"] + chart_h - (value / y_top) * chart_h
        lines.append(f'<line x1="{margin["left"]}" y1="{y:.1f}" x2="{width - margin["right"]}" y2="{y:.1f}" class="grid"/>')
        lines.append(f'<text x="{margin["left"] - 10}" y="{y + 4:.1f}" text-anchor="end" class="tick">{value:.{decimals}f}{escape(value_suffix)}</text>')

    lines.append(f'<line x1="{margin["left"]}" y1="{margin["top"] + chart_h}" x2="{width - margin["right"]}" y2="{margin["top"] + chart_h}" class="axis"/>')
    lines.append(f'<line x1="{margin["left"]}" y1="{margin["top"]}" x2="{margin["left"]}" y2="{margin["top"] + chart_h}" class="axis"/>')

    group_count = len(labels)
    series_names = list(series.keys())
    group_w = chart_w / max(group_count, 1)
    bar_gap = 6
    bar_w = min(34, (group_w - 18) / max(len(series_names), 1) - bar_gap)
    bar_w = max(bar_w, 8)

    for gi, label in enumerate(labels):
        group_x = margin["left"] + gi * group_w
        total_bars_w = len(series_names) * bar_w + (len(series_names) - 1) * bar_gap
        start_x = group_x + (group_w - total_bars_w) / 2
        for si, name in enumerate(series_names):
            value = series[name][gi]
            bar_h = (value / y_top) * chart_h
            x = start_x + si * (bar_w + bar_gap)
            y = margin["top"] + chart_h - bar_h
            lines.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="2" fill="{colors[si % len(colors)]}"/>')
            shown = f"{value:.{decimals}f}{value_suffix}"
            lines.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" class="value">{escape(shown)}</text>')
        lines.append(f'<text x="{group_x + group_w / 2:.1f}" y="{height - 46}" text-anchor="middle" class="label">{escape(label)}</text>')

    legend_x = margin["left"]
    legend_y = height - 18
    for si, name in enumerate(series_names):
        x = legend_x + si * 150
        lines.append(f'<rect x="{x}" y="{legend_y - 10}" width="12" height="12" fill="{colors[si % len(colors)]}"/>')
        lines.append(f'<text x="{x + 18}" y="{legend_y}" class="legend">{escape(name)}</text>')

    write_svg(path, lines)


def heatmap_chart(path: Path, reports: list[dict[str, Any]]) -> None:
    width = 980
    row_h = 30
    header_h = 88
    height = header_h + row_h * len(reports[0]["results"]) + 48
    left = 260
    cell_w = 130
    lines = svg_header(width, height)
    lines.append('<text x="40" y="32" class="title">Cobertura por caso y variante</text>')
    lines.append('<text x="40" y="52" class="subtitle">OK = todas las palabras clave esperadas presentes en la respuesta</text>')
    labels = [report_label(report, include_embedding=True) for report in reports]
    for vi, report in enumerate(reports):
        x = left + vi * cell_w
        lines.append(f'<text x="{x + cell_w / 2}" y="78" text-anchor="middle" class="legend">{escape(labels[vi])}</text>')
    for ri, result in enumerate(reports[0]["results"]):
        y = header_h + ri * row_h
        label = f'Q{result["index"]} - {result["category"]}'
        lines.append(f'<text x="40" y="{y + 20}" class="label">{escape(label)}</text>')
        for vi, report in enumerate(reports):
            item = report["results"][ri]
            ok = item["passed"]
            color = "#27ae60" if ok else "#eb5757"
            text = "OK" if ok else "Falla"
            x = left + vi * cell_w
            lines.append(f'<rect x="{x}" y="{y + 4}" width="{cell_w - 14}" height="22" rx="4" fill="{color}"/>')
            lines.append(f'<text x="{x + (cell_w - 14) / 2}" y="{y + 20}" text-anchor="middle" class="value" fill="#ffffff">{text}</text>')
    write_svg(path, lines)


def category_chart(path: Path, reports: list[dict[str, Any]]) -> None:
    categories = sorted({result["category"] for report in reports for result in report["results"]})
    series: dict[str, list[float]] = {}
    for report in reports:
        by_cat: dict[str, list[bool]] = defaultdict(list)
        for result in report["results"]:
            by_cat[result["category"]].append(bool(result["passed"]))
        series[report_label(report, include_embedding=True)] = [
            (sum(by_cat[cat]) / len(by_cat[cat]) * 100) if by_cat[cat] else 0
            for cat in categories
        ]
    bar_chart(
        path,
        "Accuracy por categoria",
        categories,
        series,
        "Porcentaje de casos aprobados por categoria",
        y_max=100,
        value_suffix="%",
        decimals=0,
    )


def generate_markdown(path: Path, reports: list[dict[str, Any]], chart_paths: dict[str, Path]) -> None:
    strict = reports[0]
    cases = strict["results"]
    category_counts = Counter(result["category"] for result in cases)
    total_cases = len(cases)
    all_full_pass = all(report["summary"]["passed_cases"] == report["summary"]["total_cases"] for report in reports)
    pass_sentence = (
        f"Todas las variantes evaluadas aprobaron los {total_cases} casos del conjunto de prueba."
        if all_full_pass
        else f"El conjunto evaluado contiene {total_cases} casos y permite comparar cobertura, fallas y longitud de respuesta."
    )
    rows = []
    for report in reports:
        summary = report["summary"]
        rows.append(
            f'| `{report_label(report, include_embedding=True)}` | {summary["passed_cases"]}/{summary["total_cases"]} | '
            f'{summary["accuracy"] * 100:.1f}% | {summary["average_latency_seconds"]:.2f} s | '
            f'`{summary["chat_model_name"]}` | `{summary["embedding_model_name"]}` |'
        )

    rel = {name: chart.relative_to(path.parent).as_posix() for name, chart in chart_paths.items()}
    lines = [
        "# Evaluacion Visual del Benchmark",
        "",
        "## Resumen ejecutivo",
        "",
        f"Se generaron visualizaciones a partir de los reportes reales ejecutados localmente con Ollama. {pass_sentence}",
        "",
        "| Variante | Casos aprobados | Accuracy | Latencia promedio | Modelo chat | Modelo embeddings |",
        "|---|---:|---:|---:|---|---|",
        *rows,
        "",
        "## Graficos",
        "",
        "### Accuracy por variante",
        "",
        f'![Accuracy por variante]({rel["accuracy"]})',
        "",
        "### Latencia por caso",
        "",
        f'![Latencia por caso]({rel["latency"]})',
        "",
        "### Longitud de respuesta por caso",
        "",
        f'![Longitud de respuesta por caso]({rel["response_length"]})',
        "",
        "### Accuracy por categoria",
        "",
        f'![Accuracy por categoria]({rel["category"]})',
        "",
        "### Cobertura por caso y variante",
        "",
        f'![Cobertura por caso y variante]({rel["heatmap"]})',
        "",
        "## Lectura rapida",
        "",
        "- El accuracy permite comparar rapidamente la cobertura de palabras clave esperadas.",
        "- La latencia promedio registrada por el script ayuda a controlar regresiones de performance.",
        "- La longitud de respuesta ayuda a revisar concision: casos con respuestas mas largas deberian revisarse en la matriz factual.",
        "- La cobertura por categoria muestra donde se concentran los aciertos y las fallas.",
        "",
        "## Distribucion de casos",
        "",
        "| Categoria | Casos |",
        "|---|---:|",
    ]
    for category, count in sorted(category_counts.items()):
        lines.append(f"| {category} | {count} |")
    lines.extend(
        [
            "",
            "## Limitacion",
            "",
            "Estos graficos visualizan el benchmark actual, que valida palabras clave en la respuesta final. Todavia falta incorporar metricas especificas de retrieval como Precision@K, Recall@K y MRR.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera charts SVG desde reportes de benchmark.")
    parser.add_argument("--reports", nargs="+", type=Path, default=DEFAULT_REPORTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MD_PATH)
    parser.add_argument("--no-rewrite", action="store_true", help="No normaliza los JSON de entrada.")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report_items = [
        (path, load_report(path, rewrite_normalized=not args.no_rewrite))
        for path in args.reports
    ]
    report_items = sorted(
        report_items,
        key=lambda item: (variant(item[1]), item[1]["summary"].get("embedding_model_name", "")),
    )
    reports = [report for _, report in report_items]

    include_embedding = len({variant(report) for report in reports}) != len(reports)
    labels = [report_label(report, include_embedding=include_embedding) for report in reports]
    if len(set(labels)) != len(labels):
        for path, report in report_items:
            report["_chart_label"] = path.stem.replace("benchmark_extendido_strict_", "").replace("_", " ")
        labels = [report_label(report, include_embedding=include_embedding) for report in reports]
    accuracy_values = [report["summary"]["accuracy"] * 100 for report in reports]
    chart_paths = {
        "accuracy": args.output_dir / "benchmark_accuracy_by_variant.svg",
        "latency": args.output_dir / "benchmark_latency_by_case.svg",
        "response_length": args.output_dir / "benchmark_response_length_by_case.svg",
        "category": args.output_dir / "benchmark_accuracy_by_category.svg",
        "heatmap": args.output_dir / "benchmark_case_coverage.svg",
    }

    bar_chart(
        chart_paths["accuracy"],
        "Accuracy por variante",
        labels,
        {"Accuracy": accuracy_values},
        "Porcentaje de casos aprobados",
        y_max=100,
        value_suffix="%",
        decimals=0,
    )

    case_labels = [f'Q{result["index"]}' for result in reports[0]["results"]]
    latency_series = {
        report_label(report, include_embedding=include_embedding): [result["latency_seconds"] for result in report["results"]]
        for report in reports
    }
    max_latency = max(value for values in latency_series.values() for value in values)
    bar_chart(
        chart_paths["latency"],
        "Latencia por caso",
        case_labels,
        latency_series,
        "Segundos por consulta",
        y_max=max(0.05, math.ceil(max_latency * 100) / 100),
        value_suffix="s",
        decimals=2,
    )

    length_series = {
        report_label(report, include_embedding=include_embedding): [len(result["response"]) for result in report["results"]]
        for report in reports
    }
    bar_chart(
        chart_paths["response_length"],
        "Longitud de respuesta por caso",
        case_labels,
        length_series,
        "Caracteres por respuesta",
        y_max=None,
        value_suffix="",
        decimals=0,
    )

    category_chart(chart_paths["category"], reports)
    heatmap_chart(chart_paths["heatmap"], reports)
    generate_markdown(args.markdown, reports, chart_paths)

    print("Charts generados:")
    for chart in chart_paths.values():
        print(f"- {chart}")
    print(f"Markdown generado: {args.markdown}")


if __name__ == "__main__":
    main()
