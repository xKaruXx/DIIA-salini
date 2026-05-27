from __future__ import annotations

import argparse
import asyncio
import csv
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import aiohttp
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
DEFAULT_CASES_PATH = ROOT_DIR / "dataset" / "evaluacion_manual_modelos.json"
DEFAULT_OUTPUT_JSON = ROOT_DIR / "docs" / "evaluacion_manual_modelos_respuestas.json"
DEFAULT_OUTPUT_CSV = ROOT_DIR / "docs" / "evaluacion_manual_modelos_matriz.csv"
DEFAULT_OUTPUT_MD = ROOT_DIR / "docs" / "evaluacion_manual_modelos_matriz.md"
EMBEDDING_MODEL_PATTERNS = ("embed", "embedding", "nomic")
DEFAULT_MODEL_ORDER = [
    "gemma3:270m",
    "granite4:350m",
    "lfm2.5-thinking:1.2b",
    "qwen3.5:0.8b",
    "deepseek-r1:1.5b",
    "llama3.2:3b",
    "nemotron-3-nano:4b",
    "qwen3.5:4b",
    "qwen3.5:latest",
    "gemma4:e4b",
]
MODEL_SIZE_GB = {
    "gemma3:270m": 0.291,
    "granite4:350m": 0.708,
    "lfm2.5-thinking:1.2b": 0.731,
    "qwen3.5:0.8b": 1.0,
    "deepseek-r1:1.5b": 1.1,
    "llama3.2:3b": 2.0,
    "nemotron-3-nano:4b": 2.8,
    "qwen3.5:4b": 3.4,
    "qwen3.5:latest": 6.6,
    "gemma4:e4b": 9.6,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una matriz de revision manual comparando modelos Ollama sobre una muestra balanceada."
    )
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES_PATH)
    parser.add_argument("--models", nargs="*", help="Modelos a evaluar. Usar 'all' para todos los modelos de chat.")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout por modelo/pregunta en segundos.")
    parser.add_argument("--base-url", default=os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434"))
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--template-only", action="store_true", help="Genera matriz vacia sin llamar a Ollama.")
    parser.add_argument("--num-predict", type=int, default=280, help="Limite de tokens de salida aproximado.")
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--keep-alive", default="10m", help="Tiempo para mantener cargado cada modelo durante su bloque.")
    return parser.parse_args()


def load_cases(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        cases = json.load(file)
    if not isinstance(cases, list) or not cases:
        raise ValueError(f"No hay casos validos en {path}")
    return cases


def list_ollama_models() -> list[str]:
    try:
        completed = subprocess.run(
            ["ollama", "list"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except Exception as exc:
        raise RuntimeError("No se pudo ejecutar 'ollama list'. Verificar que Ollama este instalado.") from exc

    models = []
    for line in completed.stdout.splitlines()[1:]:
        parts = line.split()
        if not parts:
            continue
        name = parts[0].strip()
        if name and not is_embedding_model(name):
            models.append(name)
    return models


def is_embedding_model(model_name: str) -> bool:
    lowered = model_name.lower()
    return any(pattern in lowered for pattern in EMBEDDING_MODEL_PATTERNS)


def select_models(requested: list[str] | None) -> list[str]:
    available = list_ollama_models()
    if requested and requested != ["all"]:
        selected = [model for model in requested if model in available]
        return sorted(selected, key=lambda model: MODEL_SIZE_GB.get(model, 999))
    if requested == ["all"]:
        return sorted(available, key=lambda model: MODEL_SIZE_GB.get(model, 999))

    ordered = [model for model in DEFAULT_MODEL_ORDER if model in available]
    extras = [model for model in available if model not in ordered]
    return ordered + sorted(extras, key=lambda model: MODEL_SIZE_GB.get(model, 999))


def normalize_model_id(model_name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "_", model_name)


def is_thinking_model(model_name: str) -> bool:
    lowered = model_name.lower()
    return "qwen" in lowered or "thinking" in lowered


def contains_thinking_trace(text: str) -> bool:
    return bool(re.search(r"(?is)<think\b|</think>|^\s*(thinking|reasoning|razonamiento)\s*:", str(text or "")))


def sanitize_response_text(text: str) -> str:
    text = str(text or "")
    text = re.sub(r"(?is)<think\b[^>]*>.*?</think>", "", text)
    text = re.sub(r"(?is)^.*?</think>\s*", "", text)
    text = re.sub(r"(?is)<think\b[^>]*>.*$", "", text)
    text = re.sub(r"(?im)^\s*(thinking|reasoning|razonamiento)\s*:\s*", "", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\2", text)
    text = re.sub(r"^\s*[*-]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def get_context(chat_service: Any, question: str) -> str:
    try:
        return chat_service._obtener_contexto_relevante(question)
    except Exception:
        keyword_hits = chat_service._keyword_search(question, limit=4)
        return "\n\n".join(f"{title}\n{text}" if title else text for _, title, text in keyword_hits)


async def call_ollama(
    session: aiohttp.ClientSession,
    base_url: str,
    model: str,
    system_prompt: str,
    question: str,
    timeout_seconds: int,
    temperature: float,
    num_predict: int,
    keep_alive: str,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "stream": False,
        "keep_alive": keep_alive,
        "messages": [
            {
                "role": "system",
                "content": (
                    system_prompt
                    + "\n\nPara esta evaluacion, no muestres cadena de razonamiento ni bloques <think>. "
                    + "Devuelve solo la respuesta final en texto plano."
                ),
            },
            {"role": "user", "content": question},
        ],
        "options": {
            "temperature": temperature,
            "num_predict": num_predict,
        },
    }
    # Ollama respeta `think: false` en varios modelos reasoning; si un modelo lo ignora,
    # la sanitizacion posterior marca thinking_removed/thinking_only.
    payload["think"] = False

    started = time.perf_counter()
    try:
        async with session.post(
            f"{base_url.rstrip('/')}/api/chat",
            json=payload,
            timeout=aiohttp.ClientTimeout(total=timeout_seconds),
        ) as response:
            if response.status != 200:
                text = await response.text()
                raise RuntimeError(f"HTTP {response.status}: {text[:300]}")
            data = await response.json()
            message = data.get("message") or {}
            raw_content = message.get("content", "").strip()
            raw_thinking = message.get("thinking", "")
            thinking_removed = bool(raw_thinking) or contains_thinking_trace(raw_content)
            content = sanitize_response_text(raw_content)
            latency = round(time.perf_counter() - started, 2)
            if not content:
                if thinking_removed:
                    return {
                        "status": "thinking_only",
                        "latency_seconds": latency,
                        "response": "",
                        "error": "El modelo devolvio solo razonamiento thinking y no una respuesta final.",
                        "thinking_removed": True,
                    }
                return {
                    "status": "empty",
                    "latency_seconds": latency,
                    "response": "",
                    "error": "Respuesta vacia del modelo.",
                    "thinking_removed": False,
                }
            return {
                "status": "ok",
                "latency_seconds": latency,
                "response": content,
                "error": "",
                "thinking_removed": thinking_removed,
            }
    except asyncio.TimeoutError:
        return {
            "status": "timeout",
            "latency_seconds": timeout_seconds,
            "response": "",
            "error": f"Timeout de {timeout_seconds}s.",
            "thinking_removed": False,
        }
    except Exception as exc:
        return {
            "status": "error",
            "latency_seconds": round(time.perf_counter() - started, 2),
            "response": "",
            "error": str(exc),
            "thinking_removed": False,
        }


async def unload_ollama_model(session: aiohttp.ClientSession, base_url: str, model: str) -> None:
    payload = {"model": model, "keep_alive": 0}
    try:
        async with session.post(
            f"{base_url.rstrip('/')}/api/generate",
            json=payload,
            timeout=aiohttp.ClientTimeout(total=30),
        ):
            return
    except Exception:
        return


async def run_evaluation(args: argparse.Namespace, cases: list[dict[str, Any]], models: list[str]) -> list[dict[str, Any]]:
    if args.template_only:
        return [
            build_row(
                case=case,
                model=model,
                result={
                    "status": "pending",
                    "latency_seconds": "",
                    "response": "",
                    "error": "",
                    "thinking_removed": "",
                },
            )
            for case in cases
            for model in models
        ]

    load_dotenv(ROOT_DIR / ".env")
    from api.chat_service import ChatService

    chat_service = ChatService()
    rows = []
    async with aiohttp.ClientSession() as session:
        for model_index, model in enumerate(models, start=1):
            print(f"[{model_index}/{len(models)}] Modelo {model}", flush=True)
            for case_index, case in enumerate(cases, start=1):
                question = case["question"]
                context = get_context(chat_service, question)
                system_prompt = chat_service.system_template.format(context=context)
                print(f"  [{case_index}/{len(cases)}] {case['id']}...", flush=True)
                result = await call_ollama(
                    session=session,
                    base_url=args.base_url,
                    model=model,
                    system_prompt=system_prompt,
                    question=question,
                    timeout_seconds=args.timeout,
                    temperature=args.temperature,
                    num_predict=args.num_predict,
                    keep_alive=args.keep_alive,
                )
                rows.append(build_row(case=case, model=model, result=result))
            await unload_ollama_model(session, args.base_url, model)
            print(f"  Modelo descargado de memoria: {model}", flush=True)
    return rows


def build_row(case: dict[str, Any], model: str, result: dict[str, Any]) -> dict[str, Any]:
    assistant_score, assistant_notes = score_response(case, result)
    return {
        "question_id": case["id"],
        "evaluation_group": case.get("evaluation_group", ""),
        "category": case["category"],
        "question": case["question"],
        "expected_criteria": " | ".join(case.get("expected_criteria", [])),
        "common_failures": " | ".join(case.get("common_failures", [])),
        "model": model,
        "status": result.get("status", ""),
        "latency_seconds": result.get("latency_seconds", ""),
        "response": result.get("response", ""),
        "error": result.get("error", ""),
        "thinking_removed": result.get("thinking_removed", ""),
        "assistant_score_1_5": assistant_score,
        "assistant_notes": assistant_notes,
        "manual_correct": "",
        "manual_score_1_5": "",
        "manual_notes": "",
    }


def normalize_for_score(text: str) -> str:
    text = str(text or "").lower()
    replacements = str.maketrans("áéíóúüñ", "aeiouun")
    text = text.translate(replacements)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def score_response(case: dict[str, Any], result: dict[str, Any]) -> tuple[str, str]:
    status = result.get("status", "")
    response = result.get("response", "")
    error = result.get("error", "")
    group = case.get("evaluation_group", "")
    normalized = normalize_for_score(response)
    question = normalize_for_score(case.get("question", ""))

    if status == "pending":
        return "", ""
    if status in {"timeout", "empty", "thinking_only", "error"}:
        return "1", f"No evaluable: {status}. {error}".strip()
    if not normalized:
        return "1", "Respuesta vacia."

    if group == "fuera_dominio":
        reject_terms = ("no tengo informacion", "fuera de dominio", "coradir", "movilidad electrica", "no puedo")
        unsafe_terms = {
            "mundial": ("argentina", "francia", "futbol"),
            "receta": ("harina", "papa", "huevo", "cocinar"),
            "script": ("import os", "python", "codigo"),
            "presidente": ("milei", "gobierno", "opino"),
            "medicamento": ("aspirina", "ibuprofeno", "paracetamol"),
            "dolares": ("plazo fijo", "invertir", "tasa"),
            "tesla": ("model 3", "nissan leaf", "tesla"),
        }
        rejects = any(term in normalized for term in reject_terms)
        leaks = any(trigger in question and any(term in normalized for term in terms) for trigger, terms in unsafe_terms.items())
        if rejects and not leaks:
            return "5", "Rechaza/redirige correctamente fuera de dominio."
        if rejects:
            return "3", "Redirige, pero incluye contenido fuera de dominio."
        return "1", "No rechaza la consulta fuera de dominio."

    expected_text = " ".join(case.get("expected_criteria", []))
    expected_tokens = [
        token
        for token in normalize_for_score(expected_text).split()
        if len(token) > 3 and token not in {"debe", "mencionar", "evitar", "responder", "puede", "corresponde"}
    ]
    expected_tokens = list(dict.fromkeys(expected_tokens))
    matched = [token for token in expected_tokens if token in normalized]
    ratio = len(matched) / len(expected_tokens) if expected_tokens else 0

    hallucination_flags = []
    if "no tengo informacion" in normalized and group != "fuera_dominio":
        hallucination_flags.append("rechazo de una pregunta del dominio")
    if "100 000" in normalized or "100000" in normalized:
        hallucination_flags.append("precio inventado")
    if "tesla" in normalized or "nissan" in normalized:
        hallucination_flags.append("contenido externo")

    if group == "ambigua":
        asks_or_qualifies = any(term in normalized for term in ("necesito saber", "depende", "para recomendar", "edad", "uso", "carga", "personas", "ubicacion", "provincia"))
        if hallucination_flags:
            return "2", "Respuesta ambigua con posible error: " + "; ".join(hallucination_flags)
        if asks_or_qualifies and ratio >= 0.2:
            return "5", "Maneja la ambiguedad con aclaraciones y criterio."
        if asks_or_qualifies:
            return "4", "Pide o incluye aclaracion, pero falta informacion del dominio."
        if ratio >= 0.35:
            return "3", "Responde parcialmente, pero sin manejar bien la ambiguedad."
        return "2", "Respuesta pobre para consulta ambigua."

    if hallucination_flags:
        return "2", "Posible problema: " + "; ".join(hallucination_flags)
    if ratio >= 0.65:
        return "5", "Cubre la mayoria de criterios esperados."
    if ratio >= 0.4:
        return "4", "Respuesta mayormente correcta, con omisiones."
    if ratio >= 0.2:
        return "3", "Respuesta parcialmente correcta."
    return "2", "Respuesta insuficiente frente a criterios esperados."


def write_json(path: Path, rows: list[dict[str, Any]], models: list[str], cases: list[dict[str, Any]]) -> None:
    payload = {
        "summary": {
            "cases": len(cases),
            "models": models,
            "total_rows": len(rows),
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "rows": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def md_escape(value: Any) -> str:
    text = str(value).replace("\n", "<br>").replace("|", "\\|")
    return text


def write_markdown(path: Path, rows: list[dict[str, Any]], models: list[str], cases: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Matriz para revision manual de modelos locales\n\n",
        "Objetivo: separar la primera evaluacion sintetica/automatica de la revision manual del autor sobre una muestra balanceada.\n\n",
        "El script completa respuestas, estados y latencias. La correccion, el score y las notas deben completarse manualmente leyendo cada respuesta.\n\n",
        "Tambien completa `assistant_score_1_5` y `assistant_notes` como preevaluacion sintetica orientativa; esos campos no reemplazan la revision manual.\n\n",
        "Para modelos thinking, la matriz no guarda cadena de razonamiento: remueve bloques `<think>...</think>` y marca `thinking_removed` cuando detecta ese contenido.\n\n",
        "Escala sugerida: 1 = incorrecta, 2 = pobre, 3 = parcialmente correcta, 4 = correcta con detalles menores, 5 = correcta y util.\n\n",
        f"- Casos: {len(cases)}\n",
        "- Distribucion: 7 preguntas factuales claras, 7 preguntas ambiguas y 7 preguntas fuera de dominio/no respondibles.\n",
        f"- Modelos: {', '.join(models)}\n",
        "- Columnas manuales a completar en CSV: `manual_correct`, `manual_score_1_5`, `manual_notes`.\n\n",
    ]

    for case in cases:
        case_rows = [row for row in rows if row["question_id"] == case["id"]]
        lines.append(f"## {case['id']} - {case.get('evaluation_group', '')} - {case['category']}\n\n")
        lines.append(f"Pregunta: {case['question']}\n\n")
        lines.append("Criterios esperados:\n")
        for criterion in case.get("expected_criteria", []):
            lines.append(f"- {criterion}\n")
        lines.append("\n")
        lines.append("| Modelo | Estado | Latencia | Thinking removido | Score asistente | Nota asistente | Respuesta / error | Correcta | Score manual | Notas manuales |\n")
        lines.append("|---|---:|---:|---:|---:|---|---|---|---|---|\n")
        for row in case_rows:
            content = row["response"] if row["response"] else row["error"]
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_escape(row["model"]),
                        md_escape(row["status"]),
                        md_escape(row["latency_seconds"]),
                        md_escape(row["thinking_removed"]),
                        md_escape(row["assistant_score_1_5"]),
                        md_escape(row["assistant_notes"]),
                        md_escape(content),
                        "",
                        "",
                        "",
                    ]
                )
                + " |\n"
            )
        lines.append("\n")

    path.write_text("".join(lines), encoding="utf-8")


async def async_main() -> None:
    args = parse_args()
    cases = load_cases(args.cases)
    models = select_models(args.models)
    if not models:
        raise RuntimeError("No se seleccionaron modelos validos.")

    rows = await run_evaluation(args, cases, models)
    write_json(args.output_json, rows, models, cases)
    write_csv(args.output_csv, rows)
    write_markdown(args.output_md, rows, models, cases)

    print(f"Generado {args.output_json}")
    print(f"Generado {args.output_csv}")
    print(f"Generado {args.output_md}")


if __name__ == "__main__":
    asyncio.run(async_main())
