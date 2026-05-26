import argparse
import asyncio
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CASES_PATH = ROOT_DIR / "dataset" / "evaluacion_mvp.json"


def normalize_for_match(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text.lower())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = normalized.replace("\n", " ")
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return " ".join(normalized.split())


def normalize_source(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", str(value).lower())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    normalized = re.sub(r"[^a-z0-9]+", ".", normalized)
    return normalized.strip(".")


def source_matches(retrieved_source: str, expected_source: str) -> bool:
    retrieved = normalize_source(retrieved_source)
    expected = normalize_source(expected_source)
    if not retrieved or not expected:
        return False
    return retrieved == expected or retrieved.startswith(f"{expected}.") or expected.startswith(f"{retrieved}.")


def keyword_search_with_metadata(question: str, chat_service, limit: int) -> list[dict]:
    normalized_question = chat_service._normalize_search_text(question)
    query_terms = chat_service._extract_query_terms(normalized_question)
    if not query_terms:
        return []

    ranked = []
    for text, metadata in zip(chat_service.knowledge_texts, chat_service.knowledge_metadatas):
        title = metadata.get("title", "")
        haystack = chat_service._normalize_search_text(f"{title} {text}")
        score = 0

        for term in query_terms:
            if term in chat_service._normalize_search_text(title):
                score += 4
            if term in haystack:
                score += 1

        if score > 0:
            ranked.append(
                {
                    "retrieval_mode": "keyword",
                    "score": score,
                    "section": metadata.get("section", ""),
                    "title": title,
                    "source_path": metadata.get("source_path", ""),
                }
            )

    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:limit]


def get_retrieved_documents(question: str, chat_service, top_k: int, retrieval_mode: str) -> list[dict]:
    retrieved = []
    seen_sources = set()

    if retrieval_mode in {"keyword", "hybrid"}:
        keyword_limit = top_k if retrieval_mode == "keyword" else min(2, top_k)
        for item in keyword_search_with_metadata(question, chat_service, limit=keyword_limit):
            key = (item.get("source_path", ""), item.get("title", ""))
            if key in seen_sources:
                continue
            seen_sources.add(key)
            retrieved.append(item)
            if len(retrieved) >= top_k:
                return retrieved[:top_k]

        if retrieval_mode == "keyword":
            return retrieved[:top_k]

    if retrieval_mode not in {"vector", "hybrid"}:
        return retrieved[:top_k]

    try:
        vector_limit = max(top_k, chat_service.retrieval_k)
        for rank, doc in enumerate(chat_service.vectorstore.similarity_search(question, k=vector_limit), start=1):
            metadata = doc.metadata or {}
            item = {
                "retrieval_mode": "vector",
                "score": None,
                "vector_rank": rank,
                "section": metadata.get("section", ""),
                "title": metadata.get("title", ""),
                "source_path": metadata.get("source_path", ""),
            }
            key = (item.get("source_path", ""), item.get("title", ""))
            if key in seen_sources:
                continue
            seen_sources.add(key)
            retrieved.append(item)
            if len(retrieved) >= top_k:
                break
    except Exception as exc:
        retrieved.append(
            {
                "retrieval_mode": "vector_unavailable",
                "score": None,
                "section": "",
                "title": "Vector retrieval unavailable",
                "source_path": "",
                "error": str(exc),
            }
        )

    return retrieved[:top_k]


def calculate_retrieval_metrics(expected_sources: list[str], retrieved_documents: list[dict], top_k: int) -> dict:
    retrieved_sources = [item.get("source_path", "") for item in retrieved_documents]
    relevant_positions = []

    for index, retrieved_source in enumerate(retrieved_sources, start=1):
        if any(source_matches(retrieved_source, expected_source) for expected_source in expected_sources):
            relevant_positions.append(index)

    matched_expected = [
        expected_source
        for expected_source in expected_sources
        if any(source_matches(retrieved_source, expected_source) for retrieved_source in retrieved_sources)
    ]

    relevant_count = len(relevant_positions)
    precision_at_k = relevant_count / top_k if top_k else 0
    recall_at_k = len(matched_expected) / len(expected_sources) if expected_sources else None
    reciprocal_rank = 1 / relevant_positions[0] if relevant_positions else 0

    return {
        "top_k": top_k,
        "expected_sources": expected_sources,
        "retrieved_sources": retrieved_sources,
        "matched_expected_sources": matched_expected,
        "relevant_positions": relevant_positions,
        "precision_at_k": round(precision_at_k, 4),
        "recall_at_k": round(recall_at_k, 4) if recall_at_k is not None else None,
        "reciprocal_rank": round(reciprocal_rank, 4),
        "first_relevant_rank": relevant_positions[0] if relevant_positions else None,
    }


async def run_cases(
    cases: list[dict],
    chat_service,
    retrieval_top_k: int,
    skip_response: bool,
    retrieval_mode: str,
) -> dict:
    results = []

    for index, case in enumerate(cases, start=1):
        start_time = time.perf_counter()
        if skip_response:
            response = ""
            latency = 0
            missing_keywords = None
            passed = None
        else:
            response = await chat_service.process_message(
                case["question"],
                user_id=f"benchmark_{case['id']}",
                user_ip="127.0.0.1",
            )
            latency = time.perf_counter() - start_time

            normalized_response = normalize_for_match(response)
            missing_keywords = [
                keyword
                for keyword in case["expected_keywords"]
                if normalize_for_match(keyword) not in normalized_response
            ]
            passed = not missing_keywords

        retrieved_documents = get_retrieved_documents(case["question"], chat_service, retrieval_top_k, retrieval_mode)
        expected_sources = case.get("expected_sources", [])
        retrieval_metrics = (
            calculate_retrieval_metrics(expected_sources, retrieved_documents, retrieval_top_k)
            if expected_sources
            else None
        )

        results.append(
            {
                "index": index,
                "id": case["id"],
                "category": case["category"],
                "question": case["question"],
                "expected_keywords": case["expected_keywords"],
                "missing_keywords": missing_keywords,
                "passed": passed,
                "latency_seconds": round(latency, 2),
                "response": response,
                "retrieved_documents": retrieved_documents,
                "retrieval": retrieval_metrics,
            }
        )

    evaluated_response_results = [result for result in results if result["passed"] is not None]
    passed = sum(1 for result in evaluated_response_results if result["passed"])
    total = len(results)
    response_total = len(evaluated_response_results)
    average_latency = (
        round(sum(result["latency_seconds"] for result in evaluated_response_results) / response_total, 2)
        if response_total
        else 0
    )

    retrieval_results = [result["retrieval"] for result in results if result.get("retrieval")]
    retrieval_summary = {}
    if retrieval_results:
        retrieval_summary = {
            "top_k": retrieval_top_k,
            "evaluated_cases": len(retrieval_results),
            "mean_precision_at_k": round(
                sum(item["precision_at_k"] for item in retrieval_results) / len(retrieval_results),
                4,
            ),
            "mean_recall_at_k": round(
                sum(item["recall_at_k"] for item in retrieval_results if item["recall_at_k"] is not None)
                / len([item for item in retrieval_results if item["recall_at_k"] is not None]),
                4,
            ),
            "mrr": round(
                sum(item["reciprocal_rank"] for item in retrieval_results) / len(retrieval_results),
                4,
            ),
            "top_1_source_accuracy": round(
                sum(1 for item in retrieval_results if item["first_relevant_rank"] == 1)
                / len(retrieval_results),
                4,
            ),
        }

    return {
        "summary": {
            "total_cases": total,
            "passed_cases": passed,
            "response_evaluated_cases": response_total,
            "accuracy": round(passed / response_total, 4) if response_total else None,
            "average_latency_seconds": average_latency,
            "prompt_variant": os.getenv("PROMPT_VARIANT", "sales"),
            "llm_provider": os.getenv("LLM_PROVIDER", "ollama"),
            "chat_model_name": os.getenv("CHAT_MODEL_NAME", ""),
            "embedding_provider": os.getenv("EMBEDDING_PROVIDER", os.getenv("LLM_PROVIDER", "ollama")),
            "embedding_model_name": os.getenv("EMBEDDING_MODEL_NAME", ""),
            "retrieval": retrieval_summary,
            "retrieval_mode": retrieval_mode,
        },
        "results": results,
    }


def print_summary(report: dict) -> None:
    summary = report["summary"]
    if summary["accuracy"] is None:
        print(f"Accuracy de respuesta: no evaluada ({summary['total_cases']} casos en modo retrieval-only)")
    else:
        print(
            f"Accuracy: {summary['passed_cases']}/{summary['response_evaluated_cases']} "
            f"({summary['accuracy'] * 100:.1f}%)"
        )
        print(f"Latencia promedio: {summary['average_latency_seconds']} s")
    print(
        "Configuracion: "
        f"{summary['llm_provider']}/{summary['chat_model_name']} | "
        f"{summary['embedding_provider']}/{summary['embedding_model_name']} | "
        f"prompt={summary['prompt_variant']}"
    )

    failed_cases = [result for result in report["results"] if result["passed"] is False]
    if failed_cases:
        print("\nCasos fallidos:")
        for result in failed_cases:
            print(f"- {result['id']}: faltaron {', '.join(result['missing_keywords'])}")

    retrieval_summary = summary.get("retrieval") or {}
    if retrieval_summary:
        print(
            "\nRetrieval: "
            f"P@{retrieval_summary['top_k']}={retrieval_summary['mean_precision_at_k']:.3f} | "
            f"R@{retrieval_summary['top_k']}={retrieval_summary['mean_recall_at_k']:.3f} | "
            f"MRR={retrieval_summary['mrr']:.3f} | "
            f"Top-1={retrieval_summary['top_1_source_accuracy']:.3f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta un benchmark simple del chatbot de movilidad.")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES_PATH, help="Ruta al JSON con casos de prueba.")
    parser.add_argument("--output", type=Path, help="Ruta para guardar el reporte JSON.")
    parser.add_argument("--prompt-variant", default=os.getenv("PROMPT_VARIANT", "strict"))
    parser.add_argument("--llm-provider", default=os.getenv("LLM_PROVIDER", "ollama"))
    parser.add_argument("--chat-model", default=os.getenv("CHAT_MODEL_NAME", "qwen3.5:latest"))
    parser.add_argument("--embedding-provider", default=os.getenv("EMBEDDING_PROVIDER", "ollama"))
    parser.add_argument("--embedding-model", default=os.getenv("EMBEDDING_MODEL_NAME", "nomic-embed-text:latest"))
    parser.add_argument("--retrieval-top-k", type=int, default=5)
    parser.add_argument("--retrieval-mode", choices=["hybrid", "keyword", "vector"], default="hybrid")
    parser.add_argument("--skip-response", action="store_true", help="Solo evalua retrieval; no llama al LLM.")
    args = parser.parse_args()

    os.environ["PROMPT_VARIANT"] = args.prompt_variant
    os.environ["LLM_PROVIDER"] = args.llm_provider
    os.environ["CHAT_MODEL_NAME"] = args.chat_model
    os.environ["EMBEDDING_PROVIDER"] = args.embedding_provider
    os.environ["EMBEDDING_MODEL_NAME"] = args.embedding_model

    if str(ROOT_DIR) not in sys.path:
        sys.path.insert(0, str(ROOT_DIR))

    from api.chat_service import ChatService

    with args.cases.open("r", encoding="utf-8") as cases_file:
        cases = json.load(cases_file)

    chat_service = ChatService()
    report = asyncio.run(
        run_cases(cases, chat_service, args.retrieval_top_k, args.skip_response, args.retrieval_mode)
    )

    default_output = ROOT_DIR / "docs" / f"benchmark_{args.prompt_variant}.json"
    output_path = args.output or default_output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print_summary(report)
    print(f"Reporte guardado en: {output_path}")


if __name__ == "__main__":
    main()
