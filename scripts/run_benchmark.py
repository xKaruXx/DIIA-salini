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


async def run_cases(cases: list[dict], chat_service) -> dict:
    results = []

    for index, case in enumerate(cases, start=1):
        start_time = time.perf_counter()
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

        results.append(
            {
                "index": index,
                "id": case["id"],
                "category": case["category"],
                "question": case["question"],
                "expected_keywords": case["expected_keywords"],
                "missing_keywords": missing_keywords,
                "passed": not missing_keywords,
                "latency_seconds": round(latency, 2),
                "response": response,
            }
        )

    passed = sum(1 for result in results if result["passed"])
    total = len(results)
    average_latency = round(sum(result["latency_seconds"] for result in results) / total, 2) if total else 0

    return {
        "summary": {
            "total_cases": total,
            "passed_cases": passed,
            "accuracy": round(passed / total, 4) if total else 0,
            "average_latency_seconds": average_latency,
            "prompt_variant": os.getenv("PROMPT_VARIANT", "sales"),
            "llm_provider": os.getenv("LLM_PROVIDER", "ollama"),
            "chat_model_name": os.getenv("CHAT_MODEL_NAME", ""),
            "embedding_provider": os.getenv("EMBEDDING_PROVIDER", os.getenv("LLM_PROVIDER", "ollama")),
            "embedding_model_name": os.getenv("EMBEDDING_MODEL_NAME", ""),
        },
        "results": results,
    }


def print_summary(report: dict) -> None:
    summary = report["summary"]
    print(
        f"Accuracy: {summary['passed_cases']}/{summary['total_cases']} "
        f"({summary['accuracy'] * 100:.1f}%)"
    )
    print(f"Latencia promedio: {summary['average_latency_seconds']} s")
    print(
        "Configuracion: "
        f"{summary['llm_provider']}/{summary['chat_model_name']} | "
        f"{summary['embedding_provider']}/{summary['embedding_model_name']} | "
        f"prompt={summary['prompt_variant']}"
    )

    failed_cases = [result for result in report["results"] if not result["passed"]]
    if failed_cases:
        print("\nCasos fallidos:")
        for result in failed_cases:
            print(f"- {result['id']}: faltaron {', '.join(result['missing_keywords'])}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta un benchmark simple del chatbot de movilidad.")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES_PATH, help="Ruta al JSON con casos de prueba.")
    parser.add_argument("--output", type=Path, help="Ruta para guardar el reporte JSON.")
    parser.add_argument("--prompt-variant", default=os.getenv("PROMPT_VARIANT", "strict"))
    parser.add_argument("--llm-provider", default=os.getenv("LLM_PROVIDER", "ollama"))
    parser.add_argument("--chat-model", default=os.getenv("CHAT_MODEL_NAME", "gemma3:1b"))
    parser.add_argument("--embedding-provider", default=os.getenv("EMBEDDING_PROVIDER", "ollama"))
    parser.add_argument("--embedding-model", default=os.getenv("EMBEDDING_MODEL_NAME", "nomic-embed-text"))
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
    report = asyncio.run(run_cases(cases, chat_service))

    default_output = ROOT_DIR / "docs" / f"benchmark_{args.prompt_variant}.json"
    output_path = args.output or default_output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print_summary(report)
    print(f"Reporte guardado en: {output_path}")


if __name__ == "__main__":
    main()
