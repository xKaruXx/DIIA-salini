// Demo Day — Chatbot RAG CORADIR (10 min, 11 slides)
// Tema oscuro alineado a los charts PNG existentes (fondo #111827)
const pptxgen = require("pptxgenjs");

const BG = "111827";      // fondo (igual a los charts)
const CARD = "1B2436";    // tarjetas
const TEAL = "14B8A6";    // acento principal
const MINT = "2DD4BF";    // acento claro
const ORANGE = "F97316";  // acento de contraste
const WHITE = "F3F4F6";
const MUTED = "94A3B8";   // gris para footers
const MUT2 = "B6C2D2";    // gris claro para texto secundario (proyector-safe)
const HEAD = "Trebuchet MS";
const BODY = "Calibri";

const DOCS = "C:/Repositorios/DIIA-salini/docs";

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Carlos Salini";
pres.title = "Chatbot RAG CORADIR — Demo Day";

function baseSlide(num, total = 11) {
  const s = pres.addSlide();
  s.background = { color: BG };
  if (num > 1) {
    s.addText(`${num} / ${total}`, {
      x: 9.2, y: 5.28, w: 0.7, h: 0.3, fontSize: 9, color: MUTED,
      fontFace: BODY, align: "right", margin: 0,
    });
    s.addText("Chatbot RAG CORADIR · Demo Day", {
      x: 0.5, y: 5.28, w: 4, h: 0.3, fontSize: 9, color: MUTED,
      fontFace: BODY, margin: 0,
    });
  }
  return s;
}

function slideTitle(s, kicker, title) {
  s.addText(kicker.toUpperCase(), {
    x: 0.5, y: 0.3, w: 9, h: 0.28, fontSize: 11.5, bold: true,
    color: TEAL, fontFace: BODY, charSpacing: 3, margin: 0,
  });
  s.addText(title, {
    x: 0.5, y: 0.7, w: 9.1, h: 0.55, fontSize: 27, bold: true,
    color: WHITE, fontFace: HEAD, margin: 0,
  });
}

function statCard(s, x, y, w, h, value, label, accent = TEAL, labelColor = WHITE) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: CARD } });
  s.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.06, h, fill: { color: accent } });
  s.addText(value, {
    x: x + 0.18, y: y + 0.1, w: w - 0.3, h: h * 0.48, fontSize: 30, bold: true,
    color: accent, fontFace: HEAD, margin: 0, valign: "middle",
  });
  s.addText(label, {
    x: x + 0.18, y: y + h * 0.55, w: w - 0.32, h: h * 0.42, fontSize: 11.5,
    color: labelColor, fontFace: BODY, margin: 0, valign: "top",
  });
}

// =====================================================================
// 1 — Título
// =====================================================================
let s = baseSlide(1);
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: TEAL } });
s.addText("DIPLOMATURA EN INTELIGENCIA ARTIFICIAL · UBA – FIUBA · TALLER DE PROYECTO FINAL", {
  x: 0.7, y: 0.75, w: 8.8, h: 0.3, fontSize: 12, bold: true, color: MINT,
  fontFace: BODY, charSpacing: 2, margin: 0,
});
s.addText("Chatbot RAG para\nMovilidad Eléctrica CORADIR", {
  x: 0.7, y: 1.4, w: 8.8, h: 1.7, fontSize: 44, bold: true, color: WHITE,
  fontFace: HEAD, margin: 0,
});
s.addText("Recuperación híbrida y respuesta extractiva sobre la base de conocimiento\nde vehículos eléctricos — medible, trazable y 100% local.", {
  x: 0.7, y: 3.2, w: 8.6, h: 0.8, fontSize: 16, color: MUT2, fontFace: BODY, margin: 0,
});
s.addShape(pres.shapes.LINE, { x: 0.7, y: 4.35, w: 8.6, h: 0, line: { color: "334155", width: 1 } });
s.addText([
  { text: "Carlos Salini", options: { bold: true, color: WHITE, fontSize: 15 } },
  { text: "   ·   Track A — RAG / Chatbot   ·   Demo Day 17/06/2026", options: { color: MUT2, fontSize: 13 } },
], { x: 0.7, y: 4.55, w: 8.8, h: 0.4, fontFace: BODY, margin: 0 });
s.addText("github.com/xKaruXx/DIIA-salini", {
  x: 0.7, y: 5.0, w: 6, h: 0.3, fontSize: 12, color: TEAL, fontFace: "Consolas", margin: 0,
});

// =====================================================================
// 2 — Problema
// =====================================================================
s = baseSlide(2);
slideTitle(s, "El problema", "Conocimiento valioso, imposible de consultar");
s.addText(
  "CORADIR fabrica vehículos eléctricos (TITO, TITA, CHIKI...) y administra precios, especificaciones, agencias y FAQs en un único JSON interno y jerárquico.",
  { x: 0.5, y: 1.5, w: 5.4, h: 0.95, fontSize: 15, color: WHITE, fontFace: BODY, margin: 0 }
);
s.addText([
  { text: "Sin consulta en lenguaje natural: ", options: { bold: true, color: MINT } },
  { text: "ventas y visitantes web dependen de búsqueda manual.", options: { color: WHITE, breakLine: true } },
  { text: "\nSin trazabilidad: ", options: { bold: true, color: MINT } },
  { text: "imposible auditar qué fuente respalda cada respuesta.", options: { color: WHITE, breakLine: true } },
  { text: "\nDatos exactos: ", options: { bold: true, color: MINT } },
  { text: "un precio o una dirección aproximada es peor que no responder.", options: { color: WHITE } },
], { x: 0.5, y: 2.55, w: 5.4, h: 2.3, fontSize: 14.5, fontFace: BODY, margin: 0 });
statCard(s, 6.3, 1.5, 3.2, 1.05, "1 JSON", "documento administrativo como única fuente", ORANGE);
statCard(s, 6.3, 2.72, 3.2, 1.05, "5 líneas", "de vehículos + agencias en ~10 provincias", TEAL);
statCard(s, 6.3, 3.94, 3.2, 1.05, "0 fuentes", "ninguna respuesta citaba su respaldo", ORANGE);

// =====================================================================
// 3 — Solución
// =====================================================================
s = baseSlide(3);
slideTitle(s, "La solución", "RAG híbrido + respuesta extractiva, 100% local");
s.addText(
  "Chatbot web que convierte el JSON en 111 documentos atómicos trazables, los recupera con búsqueda léxica + vectorial, y extrae el dato literal antes de pedirle nada a un LLM.",
  { x: 0.5, y: 1.45, w: 9, h: 0.75, fontSize: 15, color: WHITE, fontFace: BODY, margin: 0 }
);
const chips = [
  ["JSON → JSONL", "111 docs atómicos con source_path"],
  ["Chroma + léxico", "retrieval híbrido top-5"],
  ["Capa extractiva", "dato literal en 0,01 s"],
  ["LLM local", "qwen3.5 vía Ollama"],
];
chips.forEach(([t, d], i) => {
  const x = 0.5 + i * 2.36;
  s.addShape(pres.shapes.RECTANGLE, { x, y: 2.45, w: 2.2, h: 1.2, fill: { color: CARD } });
  s.addShape(pres.shapes.RECTANGLE, { x, y: 2.45, w: 2.2, h: 0.06, fill: { color: TEAL } });
  s.addText(t, { x: x + 0.15, y: 2.62, w: 1.95, h: 0.32, fontSize: 14, bold: true, color: MINT, fontFace: HEAD, margin: 0 });
  s.addText(d, { x: x + 0.15, y: 3.0, w: 1.95, h: 0.55, fontSize: 10.5, color: WHITE, fontFace: BODY, margin: 0, valign: "top" });
  if (i < 3) s.addText("→", { x: x + 2.16, y: 2.87, w: 0.24, h: 0.4, fontSize: 15, color: MUT2, align: "center", margin: 0 });
});
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.05, w: 9.0, h: 0.9, fill: { color: "0D2E2A" } });
s.addText("DEMO EN VIVO", {
  x: 0.75, y: 4.05, w: 1.7, h: 0.9, fontSize: 14, bold: true, color: TEAL,
  fontFace: HEAD, valign: "middle", margin: 0,
});
s.addText("“¿Cuánta autonomía tiene el TITO S5?”  →  respuesta literal, con fuente, en 0,01 s", {
  x: 2.55, y: 4.05, w: 6.8, h: 0.9, fontSize: 13.5, italic: true, color: WHITE,
  fontFace: BODY, valign: "middle", margin: 0,
});

// =====================================================================
// 4 — Corpus y EDA
// =====================================================================
s = baseSlide(4);
slideTitle(s, "Los datos", "Un corpus corto y asimétrico decidió el diseño");
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.5, w: 5.0, h: 3.0, fill: { color: "FFFFFF" } });
s.addImage({
  path: `${DOCS}/charts_corpus/corpus_token_distribution.png`,
  x: 0.6, y: 1.6, w: 4.8, h: 2.8, sizing: { type: "contain", w: 4.8, h: 2.8 },
});
const hall = [
  ["Mediana 24 tokens · 67 docs < 30", "No fragmentar: documento atómico = unidad de indexado"],
  ["JSON jerárquico con rutas naturales", "source_path como metadato → evaluación contra fuentes esperadas"],
  ["MATTR 0,854 · sin baja densidad", "Sin lematización global: preservar “USD 17.731,25” literal"],
];
hall.forEach(([h, d], i) => {
  const y = 1.5 + i * 1.07;
  s.addShape(pres.shapes.RECTANGLE, { x: 5.75, y, w: 3.78, h: 0.88, fill: { color: CARD } });
  s.addShape(pres.shapes.RECTANGLE, { x: 5.75, y, w: 0.06, h: 0.88, fill: { color: MINT } });
  s.addText(h, { x: 5.92, y: y + 0.07, w: 3.5, h: 0.32, fontSize: 11.5, bold: true, color: MINT, fontFace: BODY, margin: 0 });
  s.addText(d, { x: 5.92, y: y + 0.4, w: 3.5, h: 0.45, fontSize: 10.5, color: WHITE, fontFace: BODY, margin: 0 });
});
s.addText("Regla de la cátedra: cada hallazgo del EDA termina en una decisión.", {
  x: 0.5, y: 4.72, w: 9, h: 0.32, fontSize: 12, italic: true, color: MUT2, fontFace: BODY, margin: 0,
});

// =====================================================================
// 5 — Arquitectura
// =====================================================================
s = baseSlide(5);
slideTitle(s, "Arquitectura", "Pipeline offline + online con artefactos trazables");
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.48, w: 9.0, h: 3.18, fill: { color: "FFFFFF" } });
s.addImage({
  path: `${DOCS}/informe_tecnico/arquitectura_pipeline_slide.png`,
  x: 0.62, y: 1.56, w: 8.76, h: 3.02, sizing: { type: "contain", w: 8.76, h: 3.02 },
});
s.addText("Si la ruta extractiva no alcanza: retrieval híbrido top-5 + LLM con prompt estricto. Historial en SQLite; índice en Chroma.", {
  x: 0.5, y: 4.82, w: 9, h: 0.3, fontSize: 11.5, color: MUT2, fontFace: BODY, margin: 0,
});

// =====================================================================
// 6 — Hallazgo clave (extracción vs retrieval)
// =====================================================================
s = baseSlide(6);
slideTitle(s, "El hallazgo que cambió el proyecto", "Los fallos eran de extracción, no de retrieval");
statCard(s, 0.5, 1.6, 2.9, 1.5, "29", "casos fallidos en el baseline extendido (de 64)", ORANGE);
statCard(s, 3.55, 1.6, 2.9, 1.5, "24 / 29", "ya tenían la fuente correcta en el top-5", TEAL);
statCard(s, 6.6, 1.6, 2.9, 1.5, "5 / 29", "eran fallos reales de retrieval", "64748B", MUT2);
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.4, w: 9.0, h: 1.45, fill: { color: CARD } });
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.4, w: 0.06, h: 1.45, fill: { color: TEAL } });
s.addText([
  { text: "Decisión: ", options: { bold: true, color: TEAL } },
  { text: "mejorar la selección de líneas dentro del documento recuperado (términos de foco, ranking por entidad, presupuesto dinámico) ", options: { color: WHITE } },
  { text: "antes que cambiar embeddings o agregar reranking.", options: { bold: true, color: WHITE, breakLine: true } },
  { text: "\nMedir respuesta y retrieval por separado (expected_sources por caso) fue lo que hizo visible esta distinción.", options: { color: MUT2, fontSize: 12.5 } },
], { x: 0.75, y: 3.52, w: 8.55, h: 1.25, fontSize: 14, fontFace: BODY, margin: 0 });

// =====================================================================
// 7 — Selección de modelo
// =====================================================================
s = baseSlide(7);
slideTitle(s, "Decisión de modelo", "11 LLMs locales medidos con los mismos 21 casos");
s.addImage({ path: `${DOCS}/charts_modelos/manual_model_accuracy.png`, x: 0.5, y: 1.5, w: 5.55, h: 3.34 });
s.addText([
  { text: "qwen3.5:4b", options: { bold: true, color: TEAL, fontSize: 18, breakLine: true } },
  { text: "elegido para la demo", options: { color: MUT2, fontSize: 12, breakLine: true } },
  { text: "\nScore 4,19/5 vs 4,29 del 32B,", options: { color: WHITE, breakLine: true } },
  { text: "con −26% de latencia (3,8 s)", options: { color: WHITE, breakLine: true } },
  { text: "y la mitad de memoria (3,4 GB).", options: { color: WHITE, breakLine: true } },
  { text: "\nDescartados con evidencia:", options: { bold: true, color: MINT, breakLine: true } },
  { text: "gemma3:270m (respuestas vacías),", options: { color: MUT2, fontSize: 12, breakLine: true } },
  { text: "lfm2.5-thinking (sin respuesta final).", options: { color: MUT2, fontSize: 12 } },
], { x: 6.3, y: 1.55, w: 3.2, h: 3.2, fontSize: 13.5, fontFace: BODY, margin: 0 });

// =====================================================================
// 8 — Evidencia: retrieval
// =====================================================================
s = baseSlide(8);
slideTitle(s, "Evidencia · retrieval", "La fuente correcta llega, y llega primera");
statCard(s, 0.5, 1.55, 2.16, 1.35, "0,97", "Recall@5 — la fuente esperada está en el top-5", TEAL);
statCard(s, 2.81, 1.55, 2.16, 1.35, "0,92", "MRR — primer relevante en posición media 1,22", TEAL);
statCard(s, 5.12, 1.55, 2.16, 1.35, "0,88", "Top-1 — la fuente esperada queda primera", TEAL);
statCard(s, 7.43, 1.55, 2.16, 1.35, "0,32", "Precision@5 — el costo del corpus atómico", ORANGE);
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.3, w: 9.0, h: 1.5, fill: { color: CARD } });
s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.3, w: 0.06, h: 1.5, fill: { color: ORANGE } });
s.addText([
  { text: "Lectura honesta: ", options: { bold: true, color: ORANGE } },
  { text: "la Precision@5 baja no es un bug, es el trade-off elegido: 111 documentos muy cortos meten vecinos “extra” en el top-5. Hoy lo absorbe la capa extractiva.", options: { color: WHITE, breakLine: true } },
  { text: "\nAuditoría completa: 257 chunks revisados contra fuentes esperadas; 63/64 casos con la fuente en el top-5.", options: { color: MUT2, fontSize: 12 } },
], { x: 0.75, y: 3.42, w: 8.55, h: 1.3, fontSize: 13.5, fontFace: BODY, margin: 0 });

// =====================================================================
// 9 — Evidencia: end to end
// =====================================================================
s = baseSlide(9);
slideTitle(s, "Evidencia · end-to-end", "De 54,7% a 100% sin tocar índice ni embeddings");
s.addChart(pres.charts.BAR, [{
  name: "Accuracy (%)",
  labels: ["Baseline\n(RAG naive)", "It. 1\nbloques", "It. 2\nentidades", "Final (It. 3)\nextractiva"],
  values: [54.7, 71.9, 89.1, 100.0],
}], {
  x: 0.5, y: 1.5, w: 5.3, h: 3.3, barDir: "col",
  chartColors: ["14B8A6"],
  chartArea: { fill: { color: "111827" } },
  plotArea: { fill: { color: "111827" } },
  catAxisLabelColor: "94A3B8", valAxisLabelColor: "94A3B8",
  catAxisLabelFontSize: 10, valAxisLabelFontSize: 10,
  valAxisMaxVal: 100, valAxisMinVal: 0,
  valGridLine: { color: "1F2937", size: 0.5 }, catGridLine: { style: "none" },
  showValue: true, dataLabelPosition: "inEnd", dataLabelColor: "0B1220",
  dataLabelFontSize: 11, dataLabelFormatCode: "0.0",
  showLegend: false, showTitle: false,
});
s.addText([
  { text: "64/64 casos correctos", options: { bold: true, color: TEAL, fontSize: 17, breakLine: true } },
  { text: "benchmark extendido, keywords estrictas", options: { color: MUT2, fontSize: 11.5, breakLine: true } },
  { text: "\nFaithfulness media 0,895 · Token overlap 1,0", options: { color: WHITE, breakLine: true } },
  { text: "Latencia extractiva 0,01 s · costo $0/consulta", options: { color: WHITE, breakLine: true } },
  { text: "\nEl asterisco honesto:", options: { bold: true, color: ORANGE, breakLine: true } },
  { text: "el set de 64 casos se usó para iterar la mejora → 100% mide cobertura del benchmark, no generalización. Validar con consultas nuevas es el próximo paso.", options: { color: WHITE, fontSize: 12.5 } },
], { x: 6.1, y: 1.5, w: 3.45, h: 3.4, fontSize: 13.5, fontFace: BODY, margin: 0 });

// =====================================================================
// 10 — Errores documentados
// =====================================================================
s = baseSlide(10);
slideTitle(s, "Errores documentados", "Las fallas que más enseñaron — y sus correcciones");
const errs = [
  ["“¿Qué agencia hay en Moreno?”",
   "Respondía “Buenos Aires” genérico, sin CHIAMO MOTORS ni su dirección.",
   "Causa: el doc de agencias BA (388 tokens) + stopwords interrogativas subían FAQs.",
   "Fix: prioridad a localidad específica + reconstrucción de ítems de lista."],
  ["“¿Precio de la TITA S2 300?”",
   "Devolvía variantes con furgón/AA y omitía la versión base (USD 16.981,25).",
   "Causa: el ranking de líneas favorecía coincidencias más largas.",
   "Fix: penalización de variantes no solicitadas cuando piden la base."],
];
errs.forEach(([q, out, causa, fix], i) => {
  const x = 0.5 + i * 4.6;
  s.addShape(pres.shapes.RECTANGLE, { x, y: 1.5, w: 4.4, h: 2.7, fill: { color: CARD } });
  s.addShape(pres.shapes.RECTANGLE, { x, y: 1.5, w: 4.4, h: 0.06, fill: { color: ORANGE } });
  s.addText(q, { x: x + 0.18, y: 1.64, w: 4.05, h: 0.35, fontSize: 13.5, bold: true, color: WHITE, fontFace: HEAD, margin: 0 });
  s.addText(out, { x: x + 0.18, y: 2.08, w: 4.05, h: 0.62, fontSize: 11.5, color: "FCA5A5", fontFace: BODY, margin: 0 });
  s.addText(causa, { x: x + 0.18, y: 2.74, w: 4.05, h: 0.62, fontSize: 11.5, color: MUT2, fontFace: BODY, margin: 0 });
  s.addText(fix, { x: x + 0.18, y: 3.4, w: 4.05, h: 0.62, fontSize: 11.5, color: MINT, fontFace: BODY, margin: 0 });
});
s.addText([
  { text: "Bonus: ", options: { bold: true, color: ORANGE } },
  { text: "la propia mejora introdujo 2 regresiones (se perdió “500 kg” de capacidad). Se documentaron y corrigieron verificando contra el baseline completo antes de congelar.", options: { color: WHITE } },
], { x: 0.5, y: 4.42, w: 9, h: 0.6, fontSize: 12.5, fontFace: BODY, margin: 0 });

// =====================================================================
// 11 — Cierre
// =====================================================================
s = baseSlide(11);
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: TEAL } });
s.addText("CONCLUSIONES", {
  x: 0.7, y: 0.42, w: 9, h: 0.28, fontSize: 11.5, bold: true, color: TEAL, fontFace: BODY, charSpacing: 3, margin: 0,
});
s.addText("Medir por partes fue lo que permitió mejorar", {
  x: 0.7, y: 0.82, w: 9, h: 0.55, fontSize: 27, bold: true, color: WHITE, fontFace: HEAD, margin: 0,
});
const concl = [
  ["Qué demostramos", "Una KB administrativa puede volverse consultable y auditable con stack 100% local: 64/64 con trazabilidad por fuente.", TEAL],
  ["Qué limita al sistema", "Riesgo de sobreajuste al benchmark · Precision@5 0,32 · reglas extractivas atadas al dominio · precios con vencimiento.", ORANGE],
  ["Qué sigue", "Set de validación held-out con consultas reales · reevaluar EmbeddingGemma · faithfulness por consulta en producción.", MINT],
];
concl.forEach(([t, d, c], i) => {
  const y = 1.7 + i * 1.0;
  s.addShape(pres.shapes.RECTANGLE, { x: 0.7, y, w: 8.8, h: 0.88, fill: { color: CARD } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.7, y, w: 0.06, h: 0.88, fill: { color: c } });
  s.addText(t, { x: 0.9, y, w: 2.3, h: 0.88, fontSize: 13.5, bold: true, color: c, fontFace: HEAD, margin: 0, valign: "middle" });
  s.addText(d, { x: 3.3, y, w: 6.0, h: 0.88, fontSize: 12, color: WHITE, fontFace: BODY, margin: 0, valign: "middle" });
});
s.addText([
  { text: "Gracias.  ", options: { bold: true, color: WHITE, fontSize: 16 } },
  { text: "Informe técnico + benchmarks reproducibles en  ", options: { color: MUT2, fontSize: 12.5 } },
  { text: "github.com/xKaruXx/DIIA-salini", options: { color: TEAL, fontSize: 12.5, fontFace: "Consolas" } },
], { x: 0.7, y: 4.95, w: 8.8, h: 0.4, fontFace: BODY, margin: 0 });

pres.writeFile({ fileName: "C:/Repositorios/DIIA-salini/docs/presentacion/presentacion_demo_day.pptx" })
  .then(() => console.log("OK presentacion_demo_day.pptx"));
