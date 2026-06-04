from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_BENCHMARK_PATH = ROOT_DIR / "docs" / "benchmark_extendido_strict_post_extraccion_v3.json"
DEFAULT_KNOWLEDGE_PATH = ROOT_DIR / "dataset" / "knowledge_base_movilidad.jsonl"
DEFAULT_OUTPUT_JSON = ROOT_DIR / "docs" / "auditoria_rag_chunks_clase6.json"
DEFAULT_OUTPUT_CSV = ROOT_DIR / "docs" / "auditoria_rag_chunks_clase6.csv"
DEFAULT_OUTPUT_MD = ROOT_DIR / "docs" / "auditoria_rag_chunks_clase6.md"


STOPWORDS = {
    "a",
    "al",
    "como",
    "con",
    "cual",
    "cuales",
    "cuando",
    "cuanta",
    "cuanto",
    "de",
    "del",
    "donde",
    "el",
    "en",
    "es",
    "esta",
    "estas",
    "este",
    "estos",
    "la",
    "las",
    "lo",
    "los",
    "me",
    "no",
    "o",
    "para",
    "por",
    "que",
    "se",
    "si",
    "son",
    "su",
    "sus",
    "te",
    "tiene",
    "tienen",
    "un",
    "una",
    "y",
}


def fix_mojibake(text: Any) -> str:
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


def token_list(text: str) -> list[str]:
    values = []
    for raw_token in normalize_text(text).split():
        token = raw_token.strip(".")
        if len(token) <= 1 or token in STOPWORDS:
            continue
        values.append(token)
    return values


def token_set(text: str) -> set[str]:
    return set(token_list(text))


def overlap_ratio(left: set[str], right: set[str]) -> float:
    if not left:
        return 0.0
    return round(len(left & right) / len(left), 4)


def normalize_source(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", str(value).lower())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = re.sub(r"[^a-z0-9]+", ".", normalized)
    return normalized.strip(".")


def source_matches(candidate_source: str, expected_source: str) -> bool:
    candidate = normalize_source(candidate_source)
    expected = normalize_source(expected_source)
    if not candidate or not expected:
        return False
    return candidate == expected or candidate.startswith(f"{expected}.") or expected.startswith(f"{candidate}.")


def load_corpus(path: Path) -> list[dict[str, Any]]:
    documents = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        item["title"] = fix_mojibake(item.get("title", ""))
        item["content"] = fix_mojibake(item.get("content", ""))
        documents.append(item)
    return documents


def find_corpus_documents(source_path: str, corpus: list[dict[str, Any]], max_children: int = 8) -> list[dict[str, Any]]:
    exact = [doc for doc in corpus if normalize_source(doc.get("source_path", "")) == normalize_source(source_path)]
    if exact:
        return exact

    matches = [doc for doc in corpus if source_matches(doc.get("source_path", ""), source_path)]
    matches.sort(key=lambda doc: len(str(doc.get("source_path", ""))))
    return matches[:max_children]


def compact(text: str, limit: int = 260) -> str:
    cleaned = " ".join(fix_mojibake(text).split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3].rstrip() + "..."


def diagnose_case(case: dict[str, Any]) -> str:
    retrieval = case.get("retrieval") or {}
    recall = retrieval.get("recall_at_k")
    first_rank = retrieval.get("first_relevant_rank")
    if recall is not None and recall < 1:
        return "missing_expected_source"
    if first_rank is None:
        return "no_relevant_chunk"
    if first_rank > 1:
        return "ranking_review"
    if case.get("low_supporting_chunk_count", 0):
        return "review_extra_chunks"
    return "ok"


def build_audit(benchmark: dict[str, Any], corpus: list[dict[str, Any]]) -> dict[str, Any]:
    audited_cases = []
    chunk_rows = []

    for result in benchmark.get("results", []):
        question = fix_mojibake(result.get("question", ""))
        response = fix_mojibake(result.get("response", ""))
        expected_keywords = [fix_mojibake(item) for item in result.get("expected_keywords", [])]
        expected_sources = (result.get("retrieval") or {}).get("expected_sources", [])

        question_tokens = token_set(question)
        response_tokens = token_set(response)
        expected_keyword_tokens = token_set(" ".join(expected_keywords))

        audited_chunks = []
        for rank, retrieved in enumerate(result.get("retrieved_documents", []), start=1):
            retrieved_source = retrieved.get("source_path", "")
            corpus_docs = find_corpus_documents(retrieved_source, corpus)
            content = "\n\n".join(doc.get("content", "") for doc in corpus_docs)
            content_tokens = token_set(content)
            matches_expected = any(source_matches(retrieved_source, expected_source) for expected_source in expected_sources)
            matched_expected_sources = [
                expected_source
                for expected_source in expected_sources
                if source_matches(retrieved_source, expected_source)
            ]
            keyword_hits = sorted(content_tokens & expected_keyword_tokens)
            question_hits = sorted(content_tokens & question_tokens)
            response_hits = sorted(content_tokens & response_tokens)

            chunk_audit = {
                "rank": rank,
                "retrieval_mode": retrieved.get("retrieval_mode"),
                "keyword_score": retrieved.get("score"),
                "vector_rank": retrieved.get("vector_rank"),
                "section": retrieved.get("section", ""),
                "title": fix_mojibake(retrieved.get("title", "")),
                "source_path": retrieved_source,
                "matches_expected_source": matches_expected,
                "matched_expected_sources": matched_expected_sources,
                "corpus_documents_matched": [
                    {
                        "id": doc.get("id", ""),
                        "section": doc.get("section", ""),
                        "title": doc.get("title", ""),
                        "source_path": doc.get("source_path", ""),
                        "token_count": len(token_list(doc.get("content", ""))),
                        "content": doc.get("content", ""),
                    }
                    for doc in corpus_docs
                ],
                "content_token_count": len(token_list(content)),
                "question_token_overlap": overlap_ratio(question_tokens, content_tokens),
                "expected_keyword_overlap": overlap_ratio(expected_keyword_tokens, content_tokens),
                "response_token_support": overlap_ratio(response_tokens, content_tokens),
                "question_token_hits": question_hits,
                "expected_keyword_hits": keyword_hits,
                "response_token_hits": response_hits,
                "content_excerpt": compact(content),
            }
            audited_chunks.append(chunk_audit)

            chunk_rows.append(
                {
                    "case_id": result.get("id"),
                    "category": result.get("category"),
                    "question": question,
                    "rank": rank,
                    "retrieval_mode": retrieved.get("retrieval_mode"),
                    "keyword_score": retrieved.get("score"),
                    "vector_rank": retrieved.get("vector_rank"),
                    "matches_expected_source": matches_expected,
                    "expected_sources": " | ".join(expected_sources),
                    "source_path": retrieved_source,
                    "title": fix_mojibake(retrieved.get("title", "")),
                    "section": retrieved.get("section", ""),
                    "content_token_count": chunk_audit["content_token_count"],
                    "question_token_overlap": chunk_audit["question_token_overlap"],
                    "expected_keyword_overlap": chunk_audit["expected_keyword_overlap"],
                    "response_token_support": chunk_audit["response_token_support"],
                    "expected_keyword_hits": " | ".join(keyword_hits),
                    "content_excerpt": chunk_audit["content_excerpt"],
                }
            )

        low_supporting_chunk_count = sum(
            1
            for chunk in audited_chunks
            if not chunk["matches_expected_source"] and chunk["expected_keyword_overlap"] == 0
        )

        case_audit = {
            "index": result.get("index"),
            "id": result.get("id"),
            "category": result.get("category"),
            "question": question,
            "question_tokens": sorted(question_tokens),
            "expected_keywords": expected_keywords,
            "expected_keyword_tokens": sorted(expected_keyword_tokens),
            "expected_sources": expected_sources,
            "response": response,
            "response_tokens": sorted(response_tokens),
            "passed_keyword_check": result.get("passed"),
            "missing_keywords": result.get("missing_keywords"),
            "retrieval": result.get("retrieval"),
            "retrieved_chunk_count": len(audited_chunks),
            "relevant_chunk_ranks": [
                chunk["rank"] for chunk in audited_chunks if chunk["matches_expected_source"]
            ],
            "low_supporting_chunk_count": low_supporting_chunk_count,
            "diagnosis": "",
            "chunks": audited_chunks,
        }
        case_audit["diagnosis"] = diagnose_case(case_audit)
        audited_cases.append(case_audit)

    retrieval_items = [case.get("retrieval") for case in audited_cases if case.get("retrieval")]
    diagnosis_counts = Counter(case["diagnosis"] for case in audited_cases)
    category_counts = defaultdict(Counter)
    for case in audited_cases:
        category_counts[case["category"]][case["diagnosis"]] += 1

    first_ranks = [
        item.get("first_relevant_rank")
        for item in retrieval_items
        if item.get("first_relevant_rank") is not None
    ]
    precision_values = [item.get("precision_at_k", 0) for item in retrieval_items]
    recall_values = [
        item.get("recall_at_k")
        for item in retrieval_items
        if item.get("recall_at_k") is not None
    ]
    support_values = [
        chunk["response_token_support"]
        for case in audited_cases
        for chunk in case["chunks"]
        if chunk["matches_expected_source"]
    ]

    summary = {
        "benchmark_source": str(DEFAULT_BENCHMARK_PATH.relative_to(ROOT_DIR)),
        "total_cases": len(audited_cases),
        "total_retrieved_chunks": sum(case["retrieved_chunk_count"] for case in audited_cases),
        "cases_with_any_expected_source_in_top_k": sum(
            1 for case in audited_cases if case["relevant_chunk_ranks"]
        ),
        "cases_with_all_expected_sources_in_top_k": sum(
            1
            for case in audited_cases
            if (case.get("retrieval") or {}).get("recall_at_k") == 1.0
        ),
        "cases_with_expected_source_at_top_1": sum(
            1 for case in audited_cases if case["relevant_chunk_ranks"] and case["relevant_chunk_ranks"][0] == 1
        ),
        "mean_precision_at_k": round(statistics.mean(precision_values), 4) if precision_values else 0,
        "mean_recall_at_k": round(statistics.mean(recall_values), 4) if recall_values else 0,
        "mean_first_relevant_rank": round(statistics.mean(first_ranks), 2) if first_ranks else None,
        "mean_response_support_on_expected_chunks": round(statistics.mean(support_values), 4)
        if support_values
        else 0,
        "diagnosis_counts": dict(diagnosis_counts),
        "diagnosis_by_category": {
            category: dict(counts) for category, counts in sorted(category_counts.items())
        },
    }

    return {
        "summary": summary,
        "methodology": {
            "purpose": "Auditar si el benchmark recupera los chunks esperados y si esos chunks contienen tokens de pregunta, keywords esperadas y respuesta.",
            "source_match_rule": "Un chunk se considera relevante si su source_path coincide exactamente, es hijo, o es padre de una fuente esperada.",
            "question_token_overlap": "tokens(pregunta) presentes en el contenido del chunk / tokens(pregunta)",
            "expected_keyword_overlap": "tokens(keywords esperadas) presentes en el contenido del chunk / tokens(keywords esperadas)",
            "response_token_support": "tokens(respuesta) presentes en el contenido del chunk / tokens(respuesta)",
            "note": "El JSON guarda contenido completo por chunk. El Markdown y CSV usan extractos para lectura.",
        },
        "cases": audited_cases,
        "chunk_rows": chunk_rows,
    }


def write_csv(report: dict[str, Any], path: Path) -> None:
    rows = report["chunk_rows"]
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(report: dict[str, Any], path: Path) -> None:
    summary = report["summary"]
    cases = report["cases"]
    review_cases = [
        case
        for case in cases
        if case["diagnosis"] != "ok" or not case["relevant_chunk_ranks"]
    ]
    review_cases = review_cases[:18]

    lines = [
        "# Auditoria RAG de Chunks Recuperados\n\n",
        "## Resumen ejecutivo\n\n",
        "Este reporte recompone la evidencia caso por caso para medir si el sistema esta recuperando los chunks que corresponden. A diferencia del benchmark base, aca se agrega el contenido del chunk, tokens, solapamientos y diagnostico por ranking.\n\n",
        f"- Casos auditados: {summary['total_cases']}\n",
        f"- Chunks recuperados auditados: {summary['total_retrieved_chunks']}\n",
        f"- Casos con alguna fuente esperada en top K: {summary['cases_with_any_expected_source_in_top_k']}/{summary['total_cases']}\n",
        f"- Casos con todas las fuentes esperadas en top K: {summary['cases_with_all_expected_sources_in_top_k']}/{summary['total_cases']}\n",
        f"- Casos con fuente esperada en top 1: {summary['cases_with_expected_source_at_top_1']}/{summary['total_cases']}\n",
        f"- Precision@K promedio: `{summary['mean_precision_at_k']}`\n",
        f"- Recall@K promedio: `{summary['mean_recall_at_k']}`\n",
        f"- Soporte promedio de respuesta en chunks esperados: `{summary['mean_response_support_on_expected_chunks']}`\n\n",
        "Archivos generados:\n\n",
        "- `docs/auditoria_rag_chunks_clase6.json`: auditoria completa con contenido de chunks y tokens.\n",
        "- `docs/auditoria_rag_chunks_clase6.csv`: una fila por chunk recuperado.\n",
        "- `docs/auditoria_rag_chunks_clase6.md`: lectura ejecutiva y casos a revisar.\n\n",
        "## Como leer las metricas\n\n",
        "| Campo | Lectura |\n",
        "|---|---|\n",
        "| `matches_expected_source` | Indica si el `source_path` recuperado coincide con la fuente esperada del caso. |\n",
        "| `question_token_overlap` | Cuanto de la pregunta aparece en el chunk. Ayuda a ver si el chunk habla del mismo tema. |\n",
        "| `expected_keyword_overlap` | Cuanto de las keywords esperadas aparece en el chunk. Ayuda a validar si el dato buscado estaba en el contexto. |\n",
        "| `response_token_support` | Cuanto de la respuesta queda respaldado lexicalmente por el chunk. |\n",
        "| `keyword_score` | Score de busqueda lexical cuando el documento vino por modo keyword. |\n",
        "| `vector_rank` | Posicion original en la busqueda vectorial cuando el documento vino por vector. |\n\n",
        "## Diagnostico global\n\n",
        "| Diagnostico | Casos |\n",
        "|---|---:|\n",
    ]

    for diagnosis, count in sorted(summary["diagnosis_counts"].items()):
        lines.append(f"| `{diagnosis}` | {count} |\n")

    lines.extend(
        [
            "\n## Casos a revisar\n\n",
            "| Caso | Categoria | Diagnostico | Ranks relevantes | Recall@K | Precision@K | Top chunks |\n",
            "|---|---|---|---|---:|---:|---|\n",
        ]
    )

    for case in review_cases:
        retrieval = case.get("retrieval") or {}
        top_chunks = []
        for chunk in case["chunks"][:3]:
            marker = "OK" if chunk["matches_expected_source"] else "NO"
            top_chunks.append(
                f"#{chunk['rank']} {marker} {chunk['retrieval_mode']} `{chunk['source_path']}` kw={chunk['expected_keyword_overlap']}"
            )
        lines.append(
            f"| `{case['id']}` | {case['category']} | `{case['diagnosis']}` | {case['relevant_chunk_ranks']} | {retrieval.get('recall_at_k', '')} | {retrieval.get('precision_at_k', '')} | {'<br>'.join(top_chunks)} |\n"
        )

    lines.extend(
        [
            "\n## Muestra detallada de casos\n\n",
        ]
    )

    for case in cases[:10]:
        retrieval = case.get("retrieval") or {}
        lines.extend(
            [
                f"### {case['index']}. `{case['id']}` - {case['category']}\n\n",
                f"Pregunta: {case['question']}\n\n",
                f"Fuentes esperadas: `{'; '.join(case['expected_sources'])}`\n\n",
                f"Recall@K: `{retrieval.get('recall_at_k')}` | Precision@K: `{retrieval.get('precision_at_k')}` | First relevant rank: `{retrieval.get('first_relevant_rank')}`\n\n",
                "| Rank | OK fuente | Modo | Score | Source path | KW overlap | Resp support | Extracto |\n",
                "|---:|---|---|---:|---|---:|---:|---|\n",
            ]
        )
        for chunk in case["chunks"]:
            score = chunk["keyword_score"] if chunk["keyword_score"] is not None else chunk["vector_rank"]
            lines.append(
                f"| {chunk['rank']} | {'si' if chunk['matches_expected_source'] else 'no'} | {chunk['retrieval_mode']} | {score} | `{chunk['source_path']}` | {chunk['expected_keyword_overlap']} | {chunk['response_token_support']} | {compact(chunk['content_excerpt'], 120)} |\n"
            )
        lines.append("\n")

    lines.extend(
        [
            "## Proximo uso recomendado\n\n",
            "Usar el CSV para filtrar rapidamente casos donde `matches_expected_source=false` en los primeros puestos o donde `expected_keyword_overlap=0`. Usar el JSON cuando haga falta auditar el contenido completo del chunk y los tokens exactos que justifican cada metrica.\n",
        ]
    )

    path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera auditoria completa de chunks recuperados por benchmark.")
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK_PATH)
    parser.add_argument("--knowledge-base", type=Path, default=DEFAULT_KNOWLEDGE_PATH)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    benchmark = json.loads(args.benchmark.read_text(encoding="utf-8"))
    corpus = load_corpus(args.knowledge_base)
    report = build_audit(benchmark, corpus)

    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(report, args.output_csv)
    write_markdown(report, args.output_md)

    summary = report["summary"]
    print(f"Generado {args.output_json}")
    print(f"Generado {args.output_csv}")
    print(f"Generado {args.output_md}")
    print(
        "Resumen: "
        f"{summary['cases_with_all_expected_sources_in_top_k']}/{summary['total_cases']} con todas las fuentes esperadas en top K | "
        f"{summary['cases_with_any_expected_source_in_top_k']}/{summary['total_cases']} con alguna fuente esperada en top K | "
        f"{summary['cases_with_expected_source_at_top_1']}/{summary['total_cases']} en top 1"
    )


if __name__ == "__main__":
    main()
