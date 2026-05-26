from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_HTML = Path("docs/presentacion_final_chatbot_coradir.html")
OUTPUT_MD = Path("docs/presentacion_final_chatbot_coradir.md")
CHART_DIR = Path("docs/charts_presentacion")
MODEL_CHART_DIR = Path("docs/charts_modelos")
MODEL_BENCHMARK_DIR = Path("docs/benchmarks_modelos_livianos")


MODEL_SIZES_GB = {
    "granite4:350m": 0.708,
    "lfm2.5-thinking:1.2b": 0.731,
    "qwen3.5:0.8b": 1.0,
    "deepseek-r1:1.5b": 1.1,
    "qwen3.5:latest": 6.6,
    "gemma4:e4b": 9.6,
}

MODEL_COLORS = {
    "granite4:350m": "#22c55e",
    "lfm2.5-thinking:1.2b": "#38bdf8",
    "qwen3.5:0.8b": "#f97316",
    "deepseek-r1:1.5b": "#a78bfa",
    "qwen3.5:latest": "#facc15",
    "gemma4:e4b": "#fb7185",
}


SECTIONS = [
    {
        "id": "inicio",
        "eyebrow": "Trabajo final",
        "title": "Chatbot RAG para CORADIR Movilidad Electrica",
        "lead": "MVP funcional para responder consultas frecuentes sobre vehiculos, precios, carga, garantias, agencias y condiciones comerciales.",
        "bullets": [
            "Base de conocimiento cerrada y curada.",
            "Backend FastAPI con chat web.",
            "RAG con Chroma, embeddings locales y Ollama.",
            "Benchmark reproducible y metricas RAG para auditar la calidad.",
        ],
    },
    {
        "id": "problema",
        "eyebrow": "1. Problema",
        "title": "La informacion existia, pero no estaba lista para responder bien",
        "lead": "El desafio no era solo conectar un LLM: habia que transformar datos administrativos en evidencia recuperable y auditable.",
        "cards": [
            {
                "title": "Datos jerarquicos",
                "text": "El dataset original estaba en JSON, util para administrar informacion, pero poco conveniente para recuperacion semantica directa.",
            },
            {
                "title": "Riesgo de mezcla",
                "text": "Una respuesta generativa libre podia combinar versiones, precios o condiciones comerciales de forma incorrecta.",
            },
            {
                "title": "Necesidad academica",
                "text": "La presentacion necesitaba evidencia medible, no solo una demo aparentemente correcta.",
            },
        ],
    },
    {
        "id": "solucion",
        "eyebrow": "2. Solucion",
        "title": "Un pipeline hibrido: recuperar, verificar y recien despues redactar",
        "lead": "La mejora principal fue estructural: preprocesar la base, recuperar fragmentos mas precisos y usar una capa extractiva para datos factuales.",
        "flow": ["Usuario", "FastAPI", "Clasificacion", "Retrieval", "Capa extractiva", "LLM", "Respuesta"],
        "bullets": [
            "111 documentos indexables generados desde el dataset original.",
            "Chroma como base vectorial local.",
            "Ollama con qwen3.5:0.8b como default liviano y qwen3.5:latest como fallback.",
            "Prompts baseline, sales y strict para comparar comportamiento.",
        ],
    },
    {
        "id": "datos",
        "eyebrow": "3. Datos",
        "title": "Preprocesamiento orientado a RAG",
        "lead": "El sistema no indexa el JSON completo como un bloque: lo transforma en unidades semanticas mas chicas y consultables.",
        "cards": [
            {
                "title": "Fuente",
                "text": "dataset/dataset_movilidad.json con informacion institucional, vehiculos, precios, agencias, carga, FAQs y condiciones comerciales.",
            },
            {
                "title": "Transformacion",
                "text": "scripts/prepare_dataset.py normaliza claves, corrige codificacion y genera dataset/knowledge_base_movilidad.jsonl.",
            },
            {
                "title": "Impacto",
                "text": "Menos ruido en el contexto, respuestas mas concretas y mejor trazabilidad de la evidencia usada.",
            },
        ],
    },
    {
        "id": "evaluacion",
        "eyebrow": "4. Evaluacion",
        "title": "El benchmark inicial valida el MVP, el extendido muestra los limites",
        "lead": "La evaluacion se separo en dos niveles: un benchmark corto para demo/regresion y uno extendido para detectar fallas reales.",
        "chart": "charts_presentacion/accuracy_overview.png",
        "bullets": [
            "Benchmark MVP: 15/15 casos correctos en variantes strict y sales.",
            "Benchmark extendido: 35/64 casos correctos.",
            "El descenso no invalida el proyecto: muestra que el nuevo dataset es mas exigente y sensible.",
            "La lectura tecnica es que falta medir retrieval directamente.",
        ],
    },
    {
        "id": "metricas",
        "eyebrow": "5. Metricas RAG",
        "title": "Mejora: separar recuperacion y redaccion",
        "lead": "A partir de los criterios trabajados durante la cursada, la evaluacion se amplio para distinguir si falla la busqueda de evidencia o la respuesta final.",
        "cards": [
            {
                "title": "Precision@K",
                "text": "De los documentos recuperados en el top K, cuantos eran relevantes. Ayuda a medir ruido en el contexto.",
            },
            {
                "title": "Recall@K",
                "text": "De todos los documentos relevantes esperados, cuantos aparecieron en el top K. Ayuda a detectar omisiones.",
            },
            {
                "title": "MRR",
                "text": "Mide en que posicion aparece el primer documento relevante. Es importante cuando la respuesta debe salir rapido.",
            },
            {
                "title": "Faithfulness",
                "text": "Evalua si cada afirmacion de la respuesta esta respaldada por las fuentes recuperadas.",
            },
        ],
    },
    {
        "id": "resultados",
        "eyebrow": "6. Resultados",
        "title": "Resultados actuales y lectura honesta",
        "lead": "El sistema funciona en el alcance MVP, pero el benchmark extendido muestra donde conviene mejorar antes de afirmar robustez general.",
        "chart": "charts_presentacion/extended_benchmark.png",
        "bullets": [
            "Los fallos aparecen sobre todo en vehiculos especificos, agencias puntuales e informacion institucional.",
            "Puede haber fallos por recuperacion, respuesta parcial, keyword demasiado estricta o dato ausente.",
            "El proximo paso metodologico es guardar fuentes recuperadas por consulta.",
        ],
    },
    {
        "id": "retrieval",
        "eyebrow": "7. Retrieval",
        "title": "Nueva mejora: medir si aparece la fuente correcta",
        "lead": "El benchmark ahora guarda documentos recuperados y calcula Precision@5, Recall@5, MRR y Top-1 source accuracy.",
        "chart": "charts_presentacion/retrieval_metrics.png",
        "bullets": [
            "Corrida retrieval-only sobre 64 casos del dataset extendido.",
            "Recall@5: 89.8%. La fuente esperada aparece en el top 5 en la mayoria de los casos.",
            "Top-1: 65.6%. Todavia hay margen para ordenar mejor el contexto.",
            "MRR: 75.9%. Sirve para distinguir fallas de recuperacion de fallas de redaccion.",
        ],
    },
    {
        "id": "corpus",
        "eyebrow": "8. Corpus",
        "title": "Nueva mejora: EDA de chunks con TTR y MATTR",
        "lead": "Antes de lematizar o cambiar chunking, se midio la calidad del corpus RAG generado.",
        "chart": "charts_presentacion/corpus_eda.png",
        "bullets": [
            "111 documentos analizados desde knowledge_base_movilidad.jsonl.",
            "Promedio de 44.21 tokens por documento.",
            "MATTR promedio: 0.8538, una densidad lexica alta.",
            "Decision: no aplicar lematizacion global por ahora; priorizar metadata y retrieval.",
        ],
    },
    {
        "id": "embeddings",
        "eyebrow": "9. Comparacion",
        "title": "Nueva evidencia: los embeddings locales si cambian el retrieval",
        "lead": "Al medir retrieval vectorial puro, los embeddings nuevos superaron al baseline nomic-embed-text.",
        "chart": "charts_modelos/embedding_vector_metrics.png",
        "bullets": [
            "qwen3-embedding:0.6b obtuvo el mejor Recall@5: 81.2%.",
            "embeddinggemma obtuvo el mejor MRR: 69.5% y Top-1: 60.9%.",
            "nomic-embed-text fue el mas liviano, pero quedo bajo en retrieval vectorial puro.",
            "Recomendacion: probar embeddinggemma como nuevo default y validar accuracy final.",
        ],
    },
    {
        "id": "hardware",
        "eyebrow": "10. Hardware",
        "title": "Nueva mejora: evaluar modelos mas chicos",
        "lead": "Como el sistema ya reduce la carga del LLM con retrieval y respuesta extractiva, se preparo una matriz para probar si modelos livianos alcanzan para preguntas frecuentes.",
        "chart": "charts_modelos/chat_quality_vs_size.png",
        "bullets": [
            "Todos los modelos locales evaluados obtuvieron 15/15 en el benchmark MVP.",
            "Con guardrail previo, los candidatos tambien obtuvieron 6/6 en casos por fuera.",
            "granite4:350m, lfm2.5-thinking:1.2b y qwen3.5:0.8b son candidatos fuertes para rutas factuales.",
            "El resultado muestra que la capa extractiva reduce la necesidad de un modelo grande.",
            "Estrategia recomendada: modelo chico para FAQ factual y qwen3.5:latest como fallback complejo.",
        ],
    },
    {
        "id": "fuera-dominio",
        "eyebrow": "11. Guardrail",
        "title": "Casos por fuera: la mejora no fue cambiar de modelo, sino evitar alucinacion",
        "lead": "La comparacion mostro que los modelos no debian recibir consultas que el sistema podia rechazar por reglas de alcance.",
        "chart": "charts_modelos/chat_no_respondibles_accuracy.png",
        "bullets": [
            "Antes del guardrail, la capa extractiva podia traer contexto irrelevante.",
            "Despues del guardrail, todos los candidatos evaluados lograron 6/6.",
            "La latencia queda en 0.0 s porque no se llama al LLM.",
            "Esto permite usar modelos chicos con menor riesgo operativo.",
        ],
    },
    {
        "id": "demo",
        "eyebrow": "12. Demo",
        "title": "Demo en vivo dentro de la presentacion",
        "lead": "La presentacion puede cargar el chat real si se abre desde la API local. Esto permite probar preguntas sin salir del recorrido.",
        "demo": True,
        "steps": [
            "Preguntar: Cuanta autonomia tiene el TITO S5 y como se carga?",
            "Preguntar: Cual es el precio del TITO S5-300 AA?",
            "Preguntar: Donde hago un reclamo o pido servicio tecnico?",
            "Si el chat no carga, verificar que la API este levantada en http://localhost:8851.",
            "Cerrar mostrando Precision@5, Recall@5, MRR, EDA de corpus, embeddings y modelos livianos.",
        ],
    },
    {
        "id": "cierre",
        "eyebrow": "13. Cierre",
        "title": "El MVP no solo responde: tambien deja evidencia para auditarlo",
        "lead": "El proyecto queda defendible porque combina implementacion, reproducibilidad, medicion y una hoja de ruta alineada con los contenidos de clase.",
        "cards": [
            {
                "title": "Implementado",
                "text": "Chat web, backend, base preprocesada, RAG local, prompts comparables y benchmark automatizado.",
            },
            {
                "title": "Validado",
                "text": "15/15 en benchmark MVP y benchmark extendido preparado para encontrar limites reales.",
            },
            {
                "title": "Siguiente salto",
                "text": "Medir retrieval, revisar faithfulness y separar fallos de recuperacion de fallos de generacion.",
            },
        ],
    },
]


def create_charts() -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_CHART_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    plt.style.use("dark_background")

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
    labels = ["P@5", "R@5", "MRR", "Top-1"]
    values = [31.9, 89.8, 75.9, 65.6]
    bars = ax.bar(labels, values, color=["#38bdf8", "#14b8a6", "#a78bfa", "#f97316"])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Puntaje (%)")
    ax.set_title("Metricas nuevas de retrieval")
    ax.grid(axis="y", alpha=0.18, color="#94a3b8")
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%", ha="center", fontweight="bold")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "retrieval_metrics.png", dpi=180)
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
        html.append(f'<figure class="chart"><img src="{section["chart"]}" alt="{section["title"]}"></figure>')
    if section.get("demo"):
        html.append(
            """
            <div class="demo-panel">
              <div class="demo-toolbar">
                <button type="button" id="loadChatDemo">Cargar chat</button>
                <a href="/chat_assets/chat.html" target="_blank" rel="noopener">Abrir fallback</a>
              </div>
              <div id="chatDemoStatus" class="demo-status">Abrir esta presentacion desde http://localhost:8851/docs/presentacion_final_chatbot_coradir.html y presionar "Cargar chat".</div>
              <iframe id="chatDemoFrame" title="Chatbot CORADIR embebido"></iframe>
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
    .demo-status {{
      min-height: 38px;
      margin-bottom: 10px;
      color: var(--muted);
      font-size: 14px;
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
        <p class="lead">MVP funcional, reproducible localmente y evaluado con evidencia. La evaluacion separa recuperacion, respuesta final, calidad del corpus y costo de hardware.</p>
      </div>
      <aside class="hero-panel">
        <div class="metric"><strong>111</strong><span>documentos indexables generados desde la base original.</span></div>
        <div class="metric"><strong>15/15</strong><span>casos correctos en el benchmark MVP.</span></div>
        <div class="metric"><strong>64</strong><span>casos en el benchmark extendido para detectar limites.</span></div>
        <div class="metric"><strong>89.8%</strong><span>Recall@5 en la primera evaluacion retrieval-only.</span></div>
        <div class="metric"><strong>0.85</strong><span>MATTR promedio del corpus RAG.</span></div>
      </aside>
    </section>
    {sections}
  </main>
  <footer class="footer">
    Fuentes internas: <code>docs/reporte_final_implementacion.md</code>, <code>docs/evaluacion_retrieval.md</code>, <code>docs/eda_corpus_rag.md</code>, <code>docs/evaluacion_no_respondibles.md</code> y <code>docs/optimizacion_hardware_modelos.md</code>.
  </footer>
  <script>
    async function loadChatDemo() {{
      const status = document.getElementById('chatDemoStatus');
      const frame = document.getElementById('chatDemoFrame');
      if (!status || !frame) return;
      status.textContent = 'Solicitando token local...';
      try {{
        const response = await fetch('/generate-token', {{ credentials: 'include' }});
        if (!response.ok) {{
          throw new Error('HTTP ' + response.status);
        }}
        const data = await response.json();
        frame.src = '/chat?token=' + encodeURIComponent(data.token);
        status.textContent = 'Chat cargado. Probar una pregunta del recorrido sugerido.';
      }} catch (error) {{
        status.textContent = 'No se pudo cargar el chat embebido. Abrir la presentacion desde http://localhost:8851/docs/presentacion_final_chatbot_coradir.html con la API levantada. Detalle: ' + error.message;
      }}
    }}
    document.addEventListener('DOMContentLoaded', () => {{
      const button = document.getElementById('loadChatDemo');
      if (button) button.addEventListener('click', loadChatDemo);
    }});
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
