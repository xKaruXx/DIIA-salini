from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT_DIR / "dataset" / "evaluacion_mvp.json"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "docs" / "benchmarks_modelos_livianos"
DEFAULT_MODELS = [
    "qwen3.5:latest",
    "qwen3.5:0.8b",
    "deepseek-r1:1.5b",
    "lfm2.5-thinking:1.2b",
    "granite4:350m",
    "gemma4:e4b",
]


def safe_name(value: str) -> str:
    return "".join(character if character.isalnum() else "_" for character in value).strip("_")


def run_benchmark(model: str, args: argparse.Namespace) -> int:
    output = args.output_dir / f"benchmark_model_{safe_name(model)}_{args.prompt_variant}.json"
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
        model,
        "--embedding-provider",
        args.embedding_provider,
        "--embedding-model",
        args.embedding_model,
        "--retrieval-top-k",
        str(args.retrieval_top_k),
    ]
    if args.skip_response:
        command.append("--skip-response")

    print(f"\n==> Evaluando {model}")
    print(" ".join(command))
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT_DIR,
            timeout=args.subprocess_timeout_seconds if args.subprocess_timeout_seconds else None,
        )
        return completed.returncode
    except subprocess.TimeoutExpired:
        print(f"Timeout evaluando {model} luego de {args.subprocess_timeout_seconds} segundos")
        return 124


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta una matriz de benchmarks con modelos livianos de Ollama.")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS)
    parser.add_argument("--prompt-variant", default="strict")
    parser.add_argument("--embedding-provider", default="ollama")
    parser.add_argument("--embedding-model", default="nomic-embed-text:latest")
    parser.add_argument("--retrieval-top-k", type=int, default=5)
    parser.add_argument("--skip-response", action="store_true")
    parser.add_argument("--continue-on-error", action="store_true")
    parser.add_argument("--subprocess-timeout-seconds", type=int, default=0)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    failures = []
    for model in args.models:
        code = run_benchmark(model, args)
        if code != 0:
            failures.append(model)
            if not args.continue_on_error:
                break

    if failures:
        print("\nModelos con error:")
        for model in failures:
            print(f"- {model}")
        sys.exit(1)

    print("\nMatriz completada sin errores.")


if __name__ == "__main__":
    main()
