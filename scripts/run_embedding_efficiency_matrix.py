from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT_DIR / "dataset" / "evaluacion_rag_extendida.json"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "docs" / "benchmarks_embeddings"
DEFAULT_EMBEDDINGS = [
    "nomic-embed-text:latest",
    "embeddinggemma:latest",
    "qwen3-embedding:0.6b",
    "nomic-embed-text-v2-moe:latest",
]


def safe_name(value: str) -> str:
    return "".join(character if character.isalnum() else "_" for character in value).strip("_")


def run_benchmark(embedding_model: str, args: argparse.Namespace) -> int:
    output = args.output_dir / f"benchmark_embedding_{safe_name(embedding_model)}.json"
    command = [
        sys.executable,
        str(ROOT_DIR / "scripts" / "run_benchmark.py"),
        "--cases",
        str(args.cases),
        "--output",
        str(output),
        "--prompt-variant",
        args.prompt_variant,
        "--llm-provider",
        "ollama",
        "--chat-model",
        args.chat_model,
        "--embedding-provider",
        "ollama",
        "--embedding-model",
        embedding_model,
        "--retrieval-top-k",
        str(args.retrieval_top_k),
        "--retrieval-mode",
        args.retrieval_mode,
        "--skip-response",
    ]
    print(f"\n==> Evaluando embedding {embedding_model}")
    print(" ".join(command))
    completed = subprocess.run(command, cwd=ROOT_DIR)
    return completed.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta una matriz de retrieval con embeddings locales de Ollama.")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--embeddings", nargs="+", default=DEFAULT_EMBEDDINGS)
    parser.add_argument("--chat-model", default="qwen3.5:latest")
    parser.add_argument("--prompt-variant", default="strict")
    parser.add_argument("--retrieval-top-k", type=int, default=5)
    parser.add_argument("--retrieval-mode", choices=["hybrid", "keyword", "vector"], default="vector")
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    failures = []
    for embedding_model in args.embeddings:
        code = run_benchmark(embedding_model, args)
        if code != 0:
            failures.append(embedding_model)
            if not args.continue_on_error:
                break

    if failures:
        print("\nEmbeddings con error:")
        for embedding_model in failures:
            print(f"- {embedding_model}")
        sys.exit(1)

    print("\nMatriz de embeddings completada sin errores.")


if __name__ == "__main__":
    main()
