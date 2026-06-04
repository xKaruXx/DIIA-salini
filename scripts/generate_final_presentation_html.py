from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_HTML = Path("docs/presentacion_final_chatbot_coradir.html")
OUTPUT_MD = Path("docs/presentacion_final_chatbot_coradir.md")
CHART_DIR = Path("docs/charts_presentacion")
MODEL_CHART_DIR = Path("docs/charts_modelos")
MODEL_BENCHMARK_DIR = Path("docs/benchmarks_modelos_livianos")
MANUAL_MODEL_EVAL_PATH = Path("docs/evaluacion_manual_modelos_respuestas.json")


MODEL_SIZES_GB = {
    "gemma3:270m": 0.291,
    "granite4:350m": 0.708,
    "lfm2.5-thinking:1.2b": 0.731,
    "qwen3.5:0.8b": 1.0,
    "deepseek-r1:1.5b": 1.1,
    "llama3.2:3b": 2.0,
    "granite4.1:3b": 2.1,
    "nemotron-3-nano:4b": 2.8,
    "qwen3.5:4b": 3.4,
    "qwen3.5:latest": 6.6,
    "gemma4:e4b": 9.6,
}

MODEL_COLORS = {
    "gemma3:270m": "#64748b",
    "granite4:350m": "#22c55e",
    "lfm2.5-thinking:1.2b": "#38bdf8",
    "qwen3.5:0.8b": "#f97316",
    "deepseek-r1:1.5b": "#a78bfa",
    "llama3.2:3b": "#2dd4bf",
    "granite4.1:3b": "#34d399",
    "nemotron-3-nano:4b": "#60a5fa",
    "qwen3.5:4b": "#fb923c",
    "qwen3.5:latest": "#facc15",
    "gemma4:e4b": "#fb7185",
}


SECTIONS = [
    {
        "id": "inicio",
        "eyebrow": "Trabajo final",
        "title": "Chatbot RAG para CORADIR Movilidad Electrica",
        "lead": "El proyecto no se centro solo en hacer responder a un LLM: transformo una base administrativa en un corpus RAG medible, recuperable y auditable.",
        "bullets": [
            "Base de conocimiento cerrada, curada y reprocesada.",
            "Corpus JSONL con documentos mas chicos, trazables y orientados a retrieval.",
            "Benchmark reproducible con metricas de respuesta y metricas de recuperacion.",
            "La mejora de respuesta aparece como consecuencia del trabajo sobre datos, retrieval y guardrails.",
        ],
    },
    {
        "id": "problema",
        "eyebrow": "1. Problema",
        "title": "La informacion existia, pero no era evidencia recuperable",
        "lead": "El punto critico era de datos: el contenido estaba disponible, pero no estaba preparado para que un RAG encontrara la fuente correcta y respondiera sin mezclar informacion.",
        "cards": [
            {
                "title": "Formato administrativo",
                "text": "El JSON original servia para almacenar catalogo, precios, agencias y FAQs, pero no para recuperar fragmentos semanticos precisos.",
            },
            {
                "title": "Riesgo factual",
                "text": "Modelos, precios, autonomias y condiciones comerciales podian mezclarse si el contexto llegaba con ruido o demasiado amplio.",
            },
            {
                "title": "Necesidad de evidencia",
                "text": "La defensa no podia depender de una demo aislada: hacia falta medir corpus, retrieval, respuesta final y limites.",
            },
        ],
    },
    {
        "id": "datos",
        "eyebrow": "2. Datos",
        "title": "Del JSON jerarquico a un corpus RAG auditable",
        "lead": "La primera mejora fue convertir datos administrativos en documentos indexables: unidades mas chicas, con sentido propio y con fuente trazable.",
        "cards": [
            {
                "title": "Antes",
                "text": "dataset/dataset_movilidad.json concentraba FAQs, fichas tecnicas, precios, agencias, contactos y condiciones comerciales en una estructura jerarquica.",
            },
            {
                "title": "Proceso",
                "text": "scripts/prepare_dataset.py normaliza claves, corrige codificacion, separa subsecciones y genera documentos textuales coherentes.",
            },
            {
                "title": "Despues",
                "text": "dataset/knowledge_base_movilidad.jsonl deja 111 documentos indexables, cada uno orientado a una consulta o dato del dominio.",
            },
            {
                "title": "Impacto",
                "text": "El retrieval recibe menos ruido, las respuestas quedan mas trazables y los errores pueden diagnosticarse por fuente.",
            },
        ],
    },
    {
        "id": "decisiones-datos",
        "eyebrow": "3. Documentacion",
        "title": "Decisiones tomadas sobre la documentacion",
        "lead": "El trabajo principal fue convertir informacion comercial y tecnica en evidencia recuperable, sin perder trazabilidad hacia la fuente original.",
        "cards": [
            {
                "title": "Granularidad",
                "text": "No indexamos el JSON completo: separamos FAQs, precios, fichas tecnicas, agencias, contactos y condiciones en documentos mas chicos.",
            },
            {
                "title": "Trazabilidad",
                "text": "Cada chunk conserva `section`, `title` y `source_path`; eso permite saber exactamente que fuente recupero cada pregunta.",
            },
            {
                "title": "Normalizacion prudente",
                "text": "Corregimos codificacion y espacios, pero no aplicamos lematizacion global porque el EDA no justificaba perder terminos comerciales exactos.",
            },
            {
                "title": "Evaluacion con fuentes",
                "text": "El dataset extendido agrega `expected_sources`; asi medimos si el retrieval trae el chunk correcto, no solo si la respuesta suena bien.",
            },
        ],
    },
    {
        "id": "corpus",
        "eyebrow": "4. EDA",
        "title": "Medimos el corpus antes de cambiar chunking o normalizacion",
        "lead": "El EDA permitio decidir con evidencia: no aplicar lematizacion global todavia y priorizar metadata, retrieval y revision de documentos extremos.",
        "chart": "charts_presentacion/corpus_eda.png",
        "bullets": [
            "111 documentos analizados desde knowledge_base_movilidad.jsonl.",
            "Promedio de 44.21 tokens por documento; mediana de 24 y p90 de 105.",
            "MATTR promedio: 0.8538, sin senales de baja densidad lexica general.",
            "Hallazgo: revisar documentos muy largos o muy cortos por seccion antes de fusionar o partir mas chunks.",
        ],
    },
    {
        "id": "solucion",
        "eyebrow": "5. Arquitectura",
        "title": "El pipeline queda gobernado por datos, no por prompt",
        "lead": "La solucion final recupera evidencia, aplica reglas de alcance y usa generacion solo cuando el contexto ya esta acotado.",
        "flow": ["Usuario", "FastAPI", "Clasificacion", "Keyword + vector", "Capa extractiva", "LLM", "Respuesta"],
        "bullets": [
            "Chroma conserva el indice vectorial local sobre el corpus curado.",
            "La busqueda lexical ayuda con nombres propios, modelos, precios, telefonos y agencias.",
            "La capa extractiva resuelve datos factuales antes de delegar al LLM.",
            "Ollama permite reproducibilidad local sin depender de servicios pagos para la demo.",
        ],
    },
    {
        "id": "evaluacion",
        "eyebrow": "6. Evaluacion",
        "title": "El benchmark mostro que responder bien no alcanza",
        "lead": "La primera medicion validaba el MVP, pero el dataset extendido obligo a separar errores de datos, retrieval, extraccion y redaccion.",
        "chart": "charts_presentacion/accuracy_overview.png",
        "bullets": [
            "Benchmark MVP: 15/15 casos correctos en variantes strict y sales.",
            "Benchmark extendido inicial: 35/64 casos correctos.",
            "El descenso fue util: revelo consultas mas exigentes sobre vehiculos, agencias e informacion institucional.",
            "Decision metodologica: medir recuperacion de fuentes, no solo keywords en la respuesta.",
        ],
    },
    {
        "id": "metricas",
        "eyebrow": "7. Metricas RAG",
        "title": "Medimos retrieval antes de confiar en la respuesta",
        "lead": "La decision no se tomo por intuicion: cada pregunta tiene fuentes esperadas y se mide si los chunks recuperados contienen esa evidencia.",
        "cards": [
            {
                "title": "Precision@5",
                "text": "Cuantos de los cinco chunks recuperados son fuentes esperadas. Si baja, hay ruido en contexto.",
            },
            {
                "title": "Recall@5",
                "text": "Si la fuente esperada aparece en el top 5. Si baja, falta evidencia y hay que corregir retrieval o datos.",
            },
            {
                "title": "MRR / Top-1",
                "text": "Que tan temprano aparece el chunk correcto. Si baja, el problema es ranking, no necesariamente generacion.",
            },
            {
                "title": "Overlap y soporte",
                "text": "Se cruza chunk contra pregunta, keywords y respuesta para justificar si el dato usado estaba realmente en contexto.",
            },
        ],
    },
    {
        "id": "generacion-clase6",
        "eyebrow": "8. Generacion",
        "title": "Clase 6: medimos si la respuesta es correcta y trazable",
        "lead": "Sumamos metricas de generacion sobre el benchmark final: Token Overlap confirma la cobertura factual y Context Faithfulness detecta respuestas que conviene revisar por trazabilidad.",
        "chart": "charts_presentacion/generation_metrics_class6.png",
        "bullets": [
            "Token Overlap promedio: 1.0 sobre 64 casos, consistente con el 64/64 por keywords.",
            "Context Faithfulness promedio: 0.8949 contra el contexto recuperado.",
            "51/64 casos quedaron en el cuadrante sistema OK: respuesta correcta y respaldada por contexto.",
            "13/64 casos mantienen keywords correctas pero requieren revision por contexto no trazado o informacion adicional.",
        ],
    },
    {
        "id": "retrieval",
        "eyebrow": "9. Retrieval",
        "title": "Auditoria de chunks: que esta recuperando el sistema",
        "lead": "Para cada pregunta guardamos top chunks, score/rank, contenido, tokens y si el source_path coincide con la fuente esperada.",
        "chart": "charts_presentacion/retrieval_metrics.png",
        "bullets": [
            "61/64 casos tienen todas las fuentes esperadas dentro del top 5.",
            "63/64 casos tienen al menos una fuente esperada dentro del top 5.",
            "56/64 casos tienen una fuente esperada en el primer chunk recuperado.",
            "Precision@5 promedio: 31.9%; Recall@5 promedio: 96.9%; MRR: 91.6%.",
            "El CSV permite filtrar chunks con expected_keyword_overlap=0 o matches_expected_source=false.",
        ],
    },
    {
        "id": "ajustes-retrieval",
        "eyebrow": "10. Decisiones",
        "title": "Como decidimos ajustes a partir de los chunks",
        "lead": "La lectura de metricas separa tres problemas distintos: falta de evidencia, ruido en contexto y respuesta con informacion no trazada.",
        "chart": "charts_presentacion/chunk_audit_metrics.png",
        "bullets": [
            "Recall alto + Precision baja: el sistema encuentra el dato, pero trae ruido; conviene mejorar ranking y filtros, no cambiar primero el LLM.",
            "Top-1 de 56/64: la mayoria queda bien ordenada; los casos restantes se marcan como ranking_review.",
            "Casos missing_expected_source: revisar expected_sources, metadata del corpus o cobertura del dataset.",
            "Context Faithfulness bajo: revisar capa extractiva para evitar datos adicionales o contexto no trazado.",
        ],
    },
    {
        "id": "embeddings",
        "eyebrow": "11. Embeddings",
        "title": "Los embeddings se evaluaron por retrieval, no por intuicion",
        "lead": "La comparacion local mostro que cambiar embeddings puede mejorar la recuperacion, pero la decision debe validarse contra accuracy final.",
        "chart": "charts_modelos/embedding_vector_metrics.png",
        "bullets": [
            "qwen3-embedding:0.6b obtuvo el mejor Recall@5: 81.2%.",
            "embeddinggemma obtuvo el mejor MRR: 69.5% y Top-1: 60.9%.",
            "nomic-embed-text fue el mas liviano, pero quedo bajo en retrieval vectorial puro.",
            "Lectura: el embedding no se elige por marca o tamano, sino por fuentes recuperadas.",
        ],
    },
    {
        "id": "resultados",
        "eyebrow": "12. Respuesta",
        "title": "La respuesta mejora porque el contexto llega mejor preparado",
        "lead": "El foco no fue maquillar el texto final: se corrigio el camino que lleva evidencia al modelo y se agrego extraccion para datos factuales.",
        "chart": "charts_presentacion/extended_benchmark.png",
        "bullets": [
            "El benchmark extendido paso de exponer fallas a guiar mejoras concretas del pipeline.",
            "La mejora de extraccion contextual final llego a 64/64 casos correctos en la corrida documentada.",
            "La causa tecnica no fue solo prompt: fue corpus granular, fuentes recuperadas y reglas para datos factuales.",
            "El resultado queda defendible porque se puede rastrear desde pregunta hasta fuente y respuesta.",
        ],
    },
    {
        "id": "fuera-dominio",
        "eyebrow": "13. Guardrail",
        "title": "Tambien mejoramos cuando decidimos no responder",
        "lead": "Los casos por fuera del corpus se resolvieron antes del LLM: si la pregunta no pertenece al dominio o no hay dato disponible, se rechaza de forma controlada.",
        "chart": "charts_modelos/chat_no_respondibles_accuracy.png",
        "bullets": [
            "Antes del guardrail, la capa extractiva podia traer contexto irrelevante.",
            "Despues del guardrail, todos los candidatos evaluados lograron 6/6.",
            "La latencia queda en 0.0 s porque no se llama al LLM.",
            "Esto reduce alucinaciones y muestra que parte de la calidad viene del diseno del dato y del flujo.",
        ],
    },
    {
        "id": "demo",
        "eyebrow": "14. Demo",
        "title": "Demo: mostrar pregunta, fuente y respuesta",
        "lead": "La demo debe reforzar la historia: no probar solo que el bot responde, sino que la respuesta sale de una base curada y de un retrieval medido.",
        "demo": True,
        "steps": [
            "Preguntar: Cuanta autonomia tiene el TITO S5 y como se carga?",
            "Preguntar: Cual es el precio del TITO S5-300 AA?",
            "Preguntar: Donde hago un reclamo o pido servicio tecnico?",
            "Para preparar la demo completa en Windows, ejecutar scripts/start_presentation_demo.ps1.",
            "Si el chat no carga, verificar API en http://localhost:8851/health y Ollama en http://127.0.0.1:11434.",
            "Cerrar mostrando EDA del corpus, Recall@5, MRR y como eso sostiene la respuesta final.",
        ],
    },
    {
        "id": "cierre",
        "eyebrow": "15. Conclusiones",
        "title": "La mejora de respuesta fue consecuencia del trabajo sobre datos",
        "lead": "El resultado defendible no es solo un chatbot funcionando: es un pipeline con datos curados, medicion de corpus, retrieval auditable, guardrails y evaluacion reproducible.",
        "cards": [
            {
                "title": "Dato trabajado",
                "text": "El JSON original se transformo en 111 documentos RAG con mejor granularidad y trazabilidad.",
            },
            {
                "title": "Retrieval medido",
                "text": "Se calcularon Precision@5, Recall@5, MRR y Top-1 para saber si aparece la fuente correcta.",
            },
            {
                "title": "Respuesta controlada",
                "text": "La capa extractiva y los guardrails reducen alucinacion y hacen que el LLM dependa menos de improvisar.",
            },
        ],
    },
]


def load_manual_model_metrics() -> list[dict]:
    if not MANUAL_MODEL_EVAL_PATH.exists():
        return []

    payload = json.loads(MANUAL_MODEL_EVAL_PATH.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    by_model: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_model[row.get("model", "")].append(row)

    metrics = []
    for model, model_rows in by_model.items():
        scores = []
        latencies = []
        group_scores: dict[str, list[int]] = defaultdict(list)
        status_counts: dict[str, int] = defaultdict(int)
        for row in model_rows:
            score_value = row.get("assistant_score_1_5")
            try:
                score = int(score_value)
            except (TypeError, ValueError):
                continue
            scores.append(score)
            group_scores[row.get("evaluation_group", "")].append(score)
            status_counts[row.get("status", "unknown")] += 1
            try:
                latencies.append(float(row.get("latency_seconds", 0.0)))
            except (TypeError, ValueError):
                latencies.append(0.0)

        if not scores:
            continue

        acceptable = sum(1 for score in scores if score >= 4)
        total = len(model_rows) or len(scores)
        metrics.append(
            {
                "model": model,
                "avg_score": sum(scores) / len(scores),
                "acceptable": acceptable,
                "acceptable_pct": acceptable / total * 100,
                "total": total,
                "avg_latency": sum(latencies) / len(latencies) if latencies else 0.0,
                "size_gb": MODEL_SIZES_GB.get(model, 0.0),
                "status_counts": dict(status_counts),
                "groups": {
                    group: sum(values) / len(values)
                    for group, values in group_scores.items()
                    if values
                },
            }
        )

    return sorted(metrics, key=lambda item: (item["acceptable_pct"], item["avg_score"]), reverse=True)


def create_manual_model_charts() -> None:
    metrics = load_manual_model_metrics()
    if not metrics:
        return

    ranked = metrics
    labels = [item["model"] for item in ranked]
    acceptable = [item["acceptable_pct"] for item in ranked]
    avg_scores = [item["avg_score"] for item in ranked]
    latencies = [item["avg_latency"] for item in ranked]
    colors = [MODEL_COLORS.get(item["model"], "#38bdf8") for item in ranked]

    fig, ax = plt.subplots(figsize=(9.2, 5.6), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    y_positions = list(range(len(labels)))
    bars = ax.barh(y_positions, acceptable, color=colors)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Respuestas aceptables (%)")
    ax.set_title("Ranking preliminar por respuestas correctas")
    ax.grid(axis="x", alpha=0.18, color="#94a3b8")
    for bar, pct, item in zip(bars, acceptable, ranked):
        ax.text(
            pct + 1.2,
            bar.get_y() + bar.get_height() / 2,
            f"{item['acceptable']}/{item['total']} | score {item['avg_score']:.2f}",
            va="center",
            fontsize=9,
            fontweight="bold",
        )
    fig.tight_layout()
    fig.savefig(MODEL_CHART_DIR / "manual_model_accuracy.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    top_metrics = ranked[:6]
    group_order = [
        ("factual_clara", "Factuales"),
        ("ambigua", "Ambiguas"),
        ("fuera_dominio", "Fuera dominio"),
    ]
    x_positions = list(range(len(top_metrics)))
    width = 0.24

    fig, ax = plt.subplots(figsize=(9.2, 5.6), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    for index, (group_key, group_label) in enumerate(group_order):
        values = [item["groups"].get(group_key, 0.0) for item in top_metrics]
        offset = (index - 1) * width
        bars = ax.bar(
            [position + offset for position in x_positions],
            values,
            width=width,
            label=group_label,
            color=["#38bdf8", "#14b8a6", "#f97316"][index],
        )
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + 0.06,
                f"{value:.1f}",
                ha="center",
                fontsize=8,
                fontweight="bold",
            )

    ax.set_xticks(x_positions)
    ax.set_xticklabels([item["model"] for item in top_metrics], rotation=18, ha="right")
    ax.set_ylim(0, 5.4)
    ax.set_ylabel("Score promedio 1-5")
    ax.set_title("Medicion por criterio de respuesta")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    ax.legend(frameon=False, labelcolor="#e5eefb")
    for index, (score, latency) in enumerate(zip(avg_scores[:6], latencies[:6])):
        ax.text(index, 5.12, f"prom {score:.2f}\n{latency:.1f}s", ha="center", fontsize=8, color="#cbd5e1")
    fig.tight_layout()
    fig.savefig(MODEL_CHART_DIR / "manual_model_criteria.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.2, 5.6), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    for item in ranked:
        size_gb = item["size_gb"] or 0.5
        marker_size = 130 + size_gb * 70
        ax.scatter(
            item["avg_latency"],
            item["acceptable_pct"],
            s=marker_size,
            color=MODEL_COLORS.get(item["model"], "#38bdf8"),
            edgecolor="#e5eefb",
            linewidth=1.1,
            alpha=0.9,
            zorder=3,
        )
        ax.text(
            item["avg_latency"] + 0.08,
            item["acceptable_pct"] + 0.7,
            f"{item['model']}\n{item['size_gb']:.1f} GB",
            fontsize=8,
            color="#e5eefb",
        )

    ax.set_xlim(0, max(item["avg_latency"] for item in ranked) + 1.2)
    ax.set_ylim(0, 86)
    ax.set_xlabel("Latencia promedio por respuesta (s)")
    ax.set_ylabel("Respuestas aceptables (%)")
    ax.set_title("Decision operativa: acierto vs latencia vs peso")
    ax.grid(axis="both", alpha=0.18, color="#94a3b8")
    ax.text(
        0.02,
        0.03,
        "Burbuja mas grande = modelo mas pesado en disco/memoria local",
        transform=ax.transAxes,
        fontsize=9,
        color="#cbd5e1",
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "#0f172a", "edgecolor": "#334155"},
    )
    fig.tight_layout()
    fig.savefig(MODEL_CHART_DIR / "manual_model_tradeoff.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def create_charts() -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_CHART_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    plt.style.use("dark_background")
    create_manual_model_charts()

    fig, ax = plt.subplots(figsize=(7.4, 4.2), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    bars = ax.bar(["MVP\n15 casos", "Extendido\n64 casos"], [100, 54.7], color=["#0f766e", "#ea580c"])
    ax.set_ylim(0, 110)
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Evaluacion automatizada")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, [100, 54.7]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%", ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "accuracy_overview.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.2), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    bars = ax.bar(["Aprobados", "Fallidos"], [35, 29], color=["#0f766e", "#f97316"])
    ax.set_ylim(0, 64)
    ax.set_ylabel("Casos")
    ax.set_title("Benchmark extendido: 35/64")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, [35, 29]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 1, str(value), ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "extended_benchmark.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.2), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    bars = ax.bar(["nomic-embed-text", "v2-moe"], [54.7, 54.7], color=["#2563eb", "#14b8a6"])
    ax.set_ylim(0, 110)
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Comparacion de embeddings")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, [54.7, 54.7]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%", ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "embedding_comparison.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.2), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    labels = ["Precision@5", "Recall@5", "MRR", "Top-1"]
    values = [31.9, 96.9, 91.6, 87.5]
    bars = ax.bar(labels, values, color=["#38bdf8", "#14b8a6", "#a78bfa", "#f97316"])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Puntaje (%)")
    ax.set_title("Retrieval final sobre benchmark extendido")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%", ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "retrieval_metrics.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.2, 4.8), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    labels = [
        "Todas fuentes\nen top 5",
        "Alguna fuente\nen top 5",
        "Fuente esperada\nen top 1",
        "Casos a revisar\npor ranking",
        "Fuentes faltantes",
    ]
    values = [61, 63, 56, 7, 3]
    colors = ["#14b8a6", "#22c55e", "#38bdf8", "#f97316", "#ef4444"]
    bars = ax.bar(labels, values, color=colors)
    ax.set_ylim(0, 68)
    ax.set_ylabel("Casos sobre 64")
    ax.set_title("Auditoria de chunks recuperados")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 1,
            f"{value}/64",
            ha="center",
            fontweight="bold",
        )
    fig.tight_layout()
    fig.savefig(CHART_DIR / "chunk_audit_metrics.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.2), facecolor="#0f172a")
    ax.set_facecolor("#111827")
    labels = ["Docs", "Tokens prom.", "MATTR prom."]
    values = [111, 44.21, 85.38]
    bars = ax.bar(labels, values, color=["#14b8a6", "#38bdf8", "#a78bfa"])
    ax.set_title("EDA del corpus RAG")
    ax.set_ylabel("Valor")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value, label in zip(bars, values, ["111", "44.21", "0.8538"]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 3, label, ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "corpus_eda.png", dpi=180)
    plt.close(fig)

    model_points = []
    for path in sorted(MODEL_BENCHMARK_DIR.glob("benchmark_model_*_strict.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        summary = payload.get("summary", {})
        model_name = summary.get("chat_model_name")
        if model_name not in MODEL_SIZES_GB:
            continue
        model_points.append(
            {
                "model": model_name,
                "size_gb": MODEL_SIZES_GB[model_name],
                "accuracy": float(summary.get("accuracy", 0.0)) * 100,
            }
        )

    model_points.sort(key=lambda item: item["size_gb"])
    if model_points:
        fig, ax = plt.subplots(figsize=(8.4, 5.2), facecolor="#0f172a")
        ax.set_facecolor("#111827")
        for point in model_points:
            ax.scatter(
                point["size_gb"],
                point["accuracy"],
                s=150,
                color=MODEL_COLORS.get(point["model"], "#38bdf8"),
                edgecolor="#e5eefb",
                linewidth=1.2,
                label=point["model"],
                zorder=3,
            )
        ax.set_xscale("log")
        ax.set_xlim(0.55, 12)
        ax.set_ylim(92, 102)
        ax.set_xlabel("Tamano local del modelo (GB, escala log)")
        ax.set_ylabel("Accuracy benchmark MVP (%)")
        ax.set_title("Calidad vs tamano de modelos locales")
        ax.grid(axis="both", alpha=0.18, color="#94a3b8")
        ax.set_xticks([0.7, 1.0, 1.1, 6.6, 9.6])
        ax.set_xticklabels(["0.7", "1.0", "1.1", "6.6", "9.6"])
        ax.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, -0.18),
            ncol=2,
            frameon=False,
            fontsize=9,
            labelcolor="#e5eefb",
        )
        fig.subplots_adjust(bottom=0.32)
        fig.savefig(MODEL_CHART_DIR / "chat_quality_vs_size.png", dpi=180, bbox_inches="tight")
        plt.close(fig)


def render_cards(cards: list[dict[str, str]]) -> str:
    return "\n".join(
        f"""
        <article class="card">
          <h3>{card["title"]}</h3>
          <p>{card["text"]}</p>
        </article>
        """
        for card in cards
    )


def versioned_asset_path(relative_path: str) -> str:
    path = Path("docs") / relative_path
    if not path.exists():
        return relative_path
    return f"{relative_path}?v={int(path.stat().st_mtime)}"


def render_section(section: dict) -> str:
    html = [
        f'<section class="section" id="{section["id"]}">',
        '<div class="section-copy">',
        f'<span class="eyebrow">{section["eyebrow"]}</span>',
        f'<h2>{section["title"]}</h2>',
        f'<p class="lead">{section["lead"]}</p>',
    ]
    if "flow" in section:
        html.append('<div class="flow">' + "".join(f"<span>{item}</span>" for item in section["flow"]) + "</div>")
    if "bullets" in section:
        html.append("<ul>" + "".join(f"<li>{item}</li>" for item in section["bullets"]) + "</ul>")
    if "steps" in section:
        html.append("<ol>" + "".join(f"<li>{item}</li>" for item in section["steps"]) + "</ol>")
    html.append("</div>")
    if "cards" in section:
        html.append(f'<div class="grid cards-{min(len(section["cards"]), 4)}">{render_cards(section["cards"])}</div>')
    if "chart" in section:
        html.append(
            f'<figure class="chart"><img src="{versioned_asset_path(section["chart"])}" alt="{section["title"]}"></figure>'
        )
    if section.get("demo"):
        html.append(
            """
            <div class="demo-panel">
              <div class="demo-toolbar">
                <button type="button" id="loadChatDemo">Cargar chat</button>
                <button type="button" id="loadModelDemo">Cargar modelos</button>
                <a href="/chat_assets/chat.html" target="_blank" rel="noopener">Abrir fallback</a>
              </div>
              <div id="chatDemoStatus" class="demo-status">Para preparar todo: ejecutar scripts/start_presentation_demo.ps1. Luego presionar "Cargar chat".</div>
              <div id="chatProgress" class="demo-progress" hidden><span></span></div>
              <iframe id="chatDemoFrame" title="Chatbot CORADIR embebido"></iframe>
              <div class="model-demo">
                <div class="model-demo-header">
                  <h3>Comparacion local de modelos</h3>
                  <span id="modelDemoStatus">Requiere Ollama activo y modelos descargados.</span>
                </div>
                <div id="modelProgress" class="demo-progress" hidden><span></span></div>
                <div id="modelChoices" class="model-choices"></div>
                <label class="question-label" for="modelQuestion">Pregunta de evaluacion</label>
                <textarea id="modelQuestion" rows="3">Cual es el precio del TITO S5-300 AA y como se carga?</textarea>
                <button type="button" id="compareModelsDemo">Comparar respuestas</button>
                <div id="modelResults" class="model-results"></div>
              </div>
            </div>
            """
        )
    html.append("</section>")
    return "\n".join(html)


def build_html() -> None:
    nav = "\n".join(f'<a href="#{section["id"]}">{section["eyebrow"]}</a>' for section in SECTIONS)
    sections = "\n".join(render_section(section) for section in SECTIONS)
    html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Presentacion Final - Chatbot RAG CORADIR</title>
  <style>
    :root {{
      --bg: #020617;
      --paper: #0f172a;
      --paper-2: #111827;
      --ink: #e5eefb;
      --muted: #94a3b8;
      --line: #233044;
      --accent: #14b8a6;
      --accent-soft: #123c3d;
      --orange: #ea580c;
      --blue: #38bdf8;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: Inter, Segoe UI, Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.55;
    }}
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 10;
      display: flex;
      gap: 18px;
      align-items: center;
      justify-content: space-between;
      padding: 12px 28px;
      border-bottom: 1px solid var(--line);
      background: rgba(2, 6, 23, 0.94);
      backdrop-filter: blur(10px);
    }}
    .brand {{ font-weight: 800; letter-spacing: 0; }}
    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: flex-end;
    }}
    nav a {{
      color: var(--muted);
      text-decoration: none;
      font-size: 13px;
      padding: 6px 9px;
      border-radius: 6px;
    }}
    nav a:hover {{ background: var(--accent-soft); color: #5eead4; }}
    .hero {{
      min-height: 86vh;
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.9fr);
      gap: 36px;
      align-items: center;
      padding: 72px 7vw 48px;
      border-bottom: 1px solid var(--line);
      background: var(--bg);
    }}
    .eyebrow {{
      display: inline-flex;
      margin-bottom: 14px;
      color: var(--accent);
      font-size: 13px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    h1, h2, h3 {{ margin: 0; line-height: 1.1; letter-spacing: 0; }}
    h1 {{ font-size: clamp(42px, 6vw, 74px); max-width: 980px; }}
    h2 {{ font-size: clamp(30px, 4vw, 50px); max-width: 980px; }}
    h3 {{ font-size: 20px; margin-bottom: 10px; }}
    .lead {{
      color: var(--muted);
      font-size: clamp(18px, 2vw, 23px);
      max-width: 860px;
      margin: 22px 0 0;
    }}
    .hero-panel {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 24px;
      box-shadow: 0 20px 70px rgba(0, 0, 0, 0.38);
    }}
    .metric {{
      display: grid;
      grid-template-columns: 92px 1fr;
      gap: 16px;
      align-items: center;
      padding: 16px 0;
      border-bottom: 1px solid var(--line);
    }}
    .metric:last-child {{ border-bottom: 0; }}
    .metric strong {{ font-size: 34px; color: var(--accent); }}
    .metric span {{ color: var(--muted); }}
    .section {{
      min-height: 92vh;
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(320px, 0.85fr);
      gap: 44px;
      align-items: center;
      padding: 72px 7vw;
      border-bottom: 1px solid var(--line);
    }}
    .section-copy ul, .section-copy ol {{
      margin: 28px 0 0;
      padding-left: 22px;
      font-size: 19px;
    }}
    .section-copy li {{ margin: 12px 0; }}
    .grid {{
      display: grid;
      gap: 16px;
    }}
    .cards-3, .cards-4 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .card {{
      min-height: 160px;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.3);
    }}
    .card p {{ margin: 0; color: var(--muted); }}
    .flow {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 28px 0 0;
    }}
    .flow span {{
      position: relative;
      padding: 10px 12px;
      border-radius: 6px;
      background: var(--accent-soft);
      color: #99f6e4;
      font-weight: 800;
      font-size: 14px;
    }}
    .chart {{
      margin: 0;
      padding: 18px;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.3);
    }}
    .chart img {{ display: block; width: 100%; height: auto; }}
    .demo-panel {{
      min-height: 620px;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.3);
    }}
    .demo-toolbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 10px;
    }}
    .demo-toolbar button, .demo-toolbar a {{
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--accent);
      color: #042f2e;
      font-weight: 800;
      text-decoration: none;
      padding: 9px 12px;
      cursor: pointer;
      font-size: 14px;
    }}
    .demo-toolbar a {{
      background: #1e293b;
      color: var(--ink);
    }}
    .demo-toolbar button:disabled, #compareModelsDemo:disabled {{
      cursor: wait;
      opacity: 0.62;
    }}
    #modelQuestion:disabled, .model-choices input:disabled {{
      cursor: wait;
      opacity: 0.7;
    }}
    .model-demo {{
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
    }}
    .model-demo-header {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 10px;
    }}
    .model-demo-header h3 {{
      font-size: 18px;
    }}
    .model-demo-header span, .question-label {{
      color: var(--muted);
      font-size: 13px;
    }}
    .model-choices {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .model-choices label {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      max-width: 100%;
      padding: 7px 9px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #111827;
      color: var(--ink);
      font-size: 13px;
      overflow-wrap: anywhere;
    }}
    .question-label {{
      display: block;
      margin-bottom: 6px;
      font-weight: 800;
    }}
    #modelQuestion {{
      width: 100%;
      min-height: 78px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #020617;
      color: var(--ink);
      padding: 10px;
      font: inherit;
      font-size: 14px;
    }}
    #compareModelsDemo {{
      margin-top: 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--blue);
      color: #082f49;
      font-weight: 800;
      padding: 9px 12px;
      cursor: pointer;
    }}
    .model-results {{
      display: grid;
      gap: 10px;
      margin-top: 12px;
    }}
    .model-result {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #0b1220;
      padding: 12px;
    }}
    .model-result strong {{
      color: #5eead4;
    }}
    .model-result small {{
      color: var(--muted);
      margin-left: 8px;
    }}
    .model-result p {{
      margin: 8px 0 0;
      color: var(--ink);
      white-space: pre-wrap;
    }}
    .demo-status {{
      min-height: 38px;
      margin-bottom: 10px;
      color: var(--muted);
      font-size: 14px;
    }}
    .demo-progress {{
      height: 8px;
      margin: 0 0 10px;
      overflow: hidden;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: #020617;
    }}
    .demo-progress[hidden] {{
      display: none;
    }}
    .demo-progress span {{
      display: block;
      width: 0;
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, var(--accent), var(--blue));
      transition: width 0.35s ease;
    }}
    #chatDemoFrame {{
      display: block;
      width: 100%;
      height: 520px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #020617;
    }}
    .footer {{
      padding: 34px 7vw;
      color: var(--muted);
      font-size: 14px;
    }}
    code {{
      background: #1e293b;
      color: #e2e8f0;
      padding: 2px 5px;
      border-radius: 4px;
    }}
    @media (max-width: 900px) {{
      .hero, .section {{
        grid-template-columns: 1fr;
        min-height: auto;
        padding: 48px 22px;
      }}
      .topbar {{ align-items: flex-start; flex-direction: column; padding: 12px 18px; }}
      nav {{ justify-content: flex-start; }}
      .cards-3, .cards-4 {{ grid-template-columns: 1fr; }}
    }}
    @media print {{
      .topbar {{ display: none; }}
      .hero, .section {{ min-height: 100vh; break-after: page; }}
      body {{ background: var(--bg); }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="brand">Chatbot RAG CORADIR</div>
    <nav>{nav}</nav>
  </header>
  <main>
    <section class="hero" id="portada">
      <div>
        <span class="eyebrow">Presentacion final</span>
        <h1>Chatbot RAG para CORADIR Movilidad Electrica</h1>
        <p class="lead">MVP funcional y reproducible donde la mejora principal fue convertir datos administrativos en un corpus RAG medible. La respuesta mejora porque antes mejoraron los datos, el retrieval y los guardrails.</p>
      </div>
      <aside class="hero-panel">
        <div class="metric"><strong>111</strong><span>documentos RAG generados desde el JSON original.</span></div>
        <div class="metric"><strong>15/15</strong><span>casos correctos en el benchmark MVP.</span></div>
        <div class="metric"><strong>64</strong><span>casos extendidos con fuentes esperadas.</span></div>
        <div class="metric"><strong>61/64</strong><span>casos con todas las fuentes esperadas dentro del top 5.</span></div>
        <div class="metric"><strong>0.895</strong><span>Context Faithfulness promedio agregado desde clase 6.</span></div>
      </aside>
    </section>
    {sections}
  </main>
  <footer class="footer">
    Fuentes internas: <code>docs/reporte_final_implementacion.md</code>, <code>docs/eda_corpus_rag.md</code>, <code>docs/evaluacion_retrieval_extendida.md</code>, <code>docs/auditoria_rag_chunks_clase6.md</code>, <code>docs/evaluacion_metricas_generacion_clase6.md</code>, <code>docs/mejora_extraccion_contextual.md</code> y <code>docs/evaluacion_no_respondibles.md</code>.
  </footer>
  <script>
    const progressTimers = {{}};

    function startProgress(progressId, statusElement, label) {{
      const progress = document.getElementById(progressId);
      const bar = progress ? progress.querySelector('span') : null;
      if (!progress || !bar) return () => {{}};

      if (progressTimers[progressId]) {{
        clearInterval(progressTimers[progressId]);
      }}

      let value = 4;
      progress.hidden = false;
      bar.style.width = value + '%';
      if (statusElement) statusElement.textContent = label + ' ' + value + '%';

      progressTimers[progressId] = setInterval(() => {{
        const increment = Math.max(1, Math.round((94 - value) * 0.12));
        value = Math.min(92, value + increment);
        bar.style.width = value + '%';
        if (statusElement) statusElement.textContent = label + ' ' + value + '%';
      }}, 700);

      return (finalText) => {{
        clearInterval(progressTimers[progressId]);
        delete progressTimers[progressId];
        bar.style.width = '100%';
        if (statusElement) statusElement.textContent = finalText || label + ' 100%';
        setTimeout(() => {{
          progress.hidden = true;
          bar.style.width = '0%';
        }}, 900);
      }};
    }}

    function setProgress(progressId, value) {{
      const progress = document.getElementById(progressId);
      const bar = progress ? progress.querySelector('span') : null;
      if (!progress || !bar) return;
      progress.hidden = false;
      bar.style.width = Math.max(0, Math.min(100, value)) + '%';
    }}

    function hideProgress(progressId) {{
      const progress = document.getElementById(progressId);
      const bar = progress ? progress.querySelector('span') : null;
      if (!progress || !bar) return;
      setTimeout(() => {{
        progress.hidden = true;
        bar.style.width = '0%';
      }}, 900);
    }}

    function setDemoControlsDisabled(disabled) {{
      ['loadChatDemo', 'loadModelDemo', 'compareModelsDemo'].forEach((id) => {{
        const button = document.getElementById(id);
        if (button) button.disabled = disabled;
      }});
      document.querySelectorAll('#modelChoices input').forEach((input) => {{
        input.disabled = disabled;
      }});
      const question = document.getElementById('modelQuestion');
      if (question) question.disabled = disabled;
    }}

    async function fetchWithTimeout(url, options = {{}}, timeoutMs = 120000) {{
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), timeoutMs);
      try {{
        return await fetch(url, {{ ...options, signal: controller.signal }});
      }} finally {{
        clearTimeout(timeout);
      }}
    }}

    async function loadChatDemo() {{
      const status = document.getElementById('chatDemoStatus');
      const frame = document.getElementById('chatDemoFrame');
      if (!status || !frame) return;
      setDemoControlsDisabled(true);
      const finishProgress = startProgress('chatProgress', status, 'Solicitando token local...');
      try {{
        const response = await fetch('/generate-token', {{ credentials: 'include' }});
        if (!response.ok) {{
          throw new Error('HTTP ' + response.status);
        }}
        const data = await response.json();
        frame.src = '/chat?token=' + encodeURIComponent(data.token);
        finishProgress('Chat cargado. Probar una pregunta del recorrido sugerido.');
      }} catch (error) {{
        finishProgress('No se pudo cargar el chat embebido. Abrir la presentacion desde http://localhost:8851/docs/presentacion_final_chatbot_coradir.html con la API levantada. Detalle: ' + error.message);
      }} finally {{
        setDemoControlsDisabled(false);
      }}
    }}
    document.addEventListener('DOMContentLoaded', () => {{
      const button = document.getElementById('loadChatDemo');
      if (button) button.addEventListener('click', loadChatDemo);
      const modelButton = document.getElementById('loadModelDemo');
      if (modelButton) modelButton.addEventListener('click', loadModelChoices);
      const compareButton = document.getElementById('compareModelsDemo');
      if (compareButton) compareButton.addEventListener('click', compareModels);
    }});

    function escapeHtml(value) {{
      return String(value).replace(/[&<>"']/g, (char) => ({{
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
      }}[char]));
    }}

    async function loadModelChoices() {{
      const status = document.getElementById('modelDemoStatus');
      const container = document.getElementById('modelChoices');
      if (!status || !container) return;
      status.textContent = 'Consultando Ollama...';
      container.innerHTML = '';
      try {{
        const response = await fetch('/demo/ollama-models');
        const data = await response.json();
        status.textContent = data.message || 'Modelos cargados.';
        const models = data.models || [];
        if (!models.length) {{
          container.textContent = 'No hay modelos de chat disponibles.';
          return;
        }}
        container.innerHTML = models.map((model, index) => `
          <label>
            <input type="checkbox" value="${{escapeHtml(model)}}" ${{index < 3 ? 'checked' : ''}}>
            <span>${{escapeHtml(model)}}</span>
          </label>
        `).join('');
      }} catch (error) {{
        status.textContent = 'No se pudieron cargar modelos. Abrir desde la API local y verificar Ollama. Detalle: ' + error.message;
      }}
    }}

    async function compareModels() {{
      const status = document.getElementById('modelDemoStatus');
      const results = document.getElementById('modelResults');
      const question = document.getElementById('modelQuestion')?.value.trim();
      const checked = Array.from(document.querySelectorAll('#modelChoices input:checked')).map((item) => item.value);
      if (!status || !results) return;
      if (!question) {{
        status.textContent = 'Escribir una pregunta para comparar.';
        return;
      }}
      if (!checked.length) {{
        status.textContent = 'Seleccionar al menos un modelo.';
        return;
      }}
      const models = checked.slice(0, 4);
      setDemoControlsDisabled(true);
      status.textContent = `Comparando respuestas: 0/${{models.length}} modelos completados.`;
      results.innerHTML = '';
      setProgress('modelProgress', 0);
      try {{
        for (let index = 0; index < models.length; index += 1) {{
          const model = models[index];
          const startedAt = Date.now();
          const placeholder = document.createElement('article');
          placeholder.className = 'model-result';
          placeholder.innerHTML = `
            <div><strong>${{escapeHtml(model)}}</strong><small>procesando...</small></div>
            <p>Esperando respuesta del modelo local.</p>
          `;
          results.appendChild(placeholder);

          const timer = setInterval(() => {{
            const seconds = Math.round((Date.now() - startedAt) / 1000);
            const currentPercent = Math.round((index / models.length) * 100);
            setProgress('modelProgress', currentPercent);
            status.textContent = `Procesando modelo ${{index + 1}}/${{models.length}}: ${{model}}. ${{seconds}} s transcurridos.`;
            const small = placeholder.querySelector('small');
            if (small) small.textContent = `${{seconds}} s transcurridos`;
          }}, 1000);

          try {{
            const response = await fetchWithTimeout('/demo/compare-models', {{
              method: 'POST',
              headers: {{ 'Content-Type': 'application/json' }},
              body: JSON.stringify({{ question, models: [model] }})
            }}, 120000);
            if (!response.ok) {{
              throw new Error('HTTP ' + response.status);
            }}
            const data = await response.json();
            const item = (data.results || [])[0] || {{
              model,
              ok: false,
              latency_seconds: Math.round((Date.now() - startedAt) / 1000),
              error: 'Sin respuesta del backend.'
            }};
            placeholder.innerHTML = `
              <div><strong>${{escapeHtml(item.model)}}</strong><small>${{item.latency_seconds ?? '-'}} s</small></div>
              <p>${{escapeHtml(item.ok ? item.response : item.error)}}</p>
            `;
          }} catch (error) {{
            const message = error.name === 'AbortError' ? 'Timeout de 120s sin respuesta.' : error.message;
            placeholder.innerHTML = `
              <div><strong>${{escapeHtml(model)}}</strong><small>error</small></div>
              <p>${{escapeHtml(message)}}</p>
            `;
          }} finally {{
            clearInterval(timer);
            const completedPercent = Math.round(((index + 1) / models.length) * 100);
            setProgress('modelProgress', completedPercent);
            status.textContent = `Comparando respuestas: ${{index + 1}}/${{models.length}} modelos completados.`;
          }}
        }}
        status.textContent = 'Comparacion finalizada.';
        hideProgress('modelProgress');
      }} catch (error) {{
        status.textContent = 'No se pudo comparar. Detalle: ' + error.message;
      }} finally {{
        setDemoControlsDisabled(false);
      }}
    }}
  </script>
</body>
</html>
"""
    OUTPUT_HTML.write_text(html, encoding="utf-8")


def build_markdown() -> None:
    lines = ["# Presentacion Final - Chatbot RAG CORADIR\n\n"]
    for section in SECTIONS:
        lines.append(f"## {section['eyebrow']} - {section['title']}\n\n")
        lines.append(f"{section['lead']}\n\n")
        for key in ("bullets", "steps"):
            if key in section:
                for item in section[key]:
                    lines.append(f"- {item}\n")
                lines.append("\n")
        if "cards" in section:
            for card in section["cards"]:
                lines.append(f"### {card['title']}\n\n{card['text']}\n\n")
        if "flow" in section:
            lines.append("Flujo: " + " -> ".join(section["flow"]) + "\n\n")
    OUTPUT_MD.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    create_charts()
    build_html()
    build_markdown()
    print(f"Generado {OUTPUT_HTML}")
    print(f"Generado {OUTPUT_MD}")


if __name__ == "__main__":
    main()
