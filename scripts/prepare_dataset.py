import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = ROOT_DIR / "dataset" / "dataset_movilidad.json"
DEFAULT_OUTPUT_PATH = ROOT_DIR / "dataset" / "knowledge_base_movilidad.jsonl"


def normalize_text(value: Any) -> str:
    text = str(value)
    if any(token in text for token in ("Ã", "Â", "ðŸ")):
        try:
            repaired = text.encode("latin1").decode("utf-8")
            if repaired:
                text = repaired
        except UnicodeError:
            pass

    text = text.replace("\r", " ").replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


def slugify(value: str) -> str:
    cleaned = normalize_text(value).lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned)
    return cleaned.strip("-") or "document"


def humanize_key(key: Any) -> str:
    return normalize_text(str(key).replace("_", " "))


def serialize_node(node: Any, indent: int = 0) -> list[str]:
    prefix = "  " * indent

    if isinstance(node, dict):
        lines = []
        for key, value in node.items():
            label = humanize_key(key)
            if isinstance(value, (dict, list)):
                nested = serialize_node(value, indent + 1)
                if nested:
                    lines.append(f"{prefix}{label}:")
                    lines.extend(nested)
            else:
                scalar = normalize_text(value)
                if scalar:
                    lines.append(f"{prefix}{label}: {scalar}")
        return lines

    if isinstance(node, list):
        lines = []
        for item in node:
            if isinstance(item, (dict, list)):
                nested = serialize_node(item, indent + 1)
                if nested:
                    lines.append(f"{prefix}-")
                    lines.extend(nested)
            else:
                scalar = normalize_text(item)
                if scalar:
                    lines.append(f"{prefix}- {scalar}")
        return lines

    scalar = normalize_text(node)
    return [f"{prefix}{scalar}"] if scalar else []


def make_document(section: str, title: str, content: str, source_path: str) -> dict[str, str]:
    return {
        "id": f"{slugify(section)}::{slugify(title)}",
        "section": section,
        "title": title,
        "content": content.strip(),
        "source_path": source_path,
    }


def extend_generic_section(
    documents: list[dict[str, str]],
    section_name: str,
    payload: Any,
    source_path: str,
) -> None:
    if isinstance(payload, dict):
        for key, value in payload.items():
            content = "\n".join(serialize_node(value))
            if content:
                documents.append(
                    make_document(
                        section=section_name,
                        title=f"{humanize_key(section_name)} - {humanize_key(key)}",
                        content=content,
                        source_path=f"{source_path}.{key}",
                    )
                )
        return

    content = "\n".join(serialize_node(payload))
    if content:
        documents.append(
            make_document(
                section=section_name,
                title=humanize_key(section_name),
                content=content,
                source_path=source_path,
            )
        )


def build_documents(data: dict[str, Any]) -> list[dict[str, str]]:
    documents: list[dict[str, str]] = []

    for faq_group, questions in data.get("preguntas_frecuentes", {}).items():
        for index, item in enumerate(questions, start=1):
            documents.append(
                make_document(
                    section="preguntas_frecuentes",
                    title=f"FAQ {humanize_key(faq_group)} - {item['pregunta']}",
                    content=f"Pregunta: {item['pregunta']}\nRespuesta: {item['respuesta']}",
                    source_path=f"preguntas_frecuentes.{faq_group}[{index - 1}]",
                )
            )

    for vehicle_name, payload in data.get("todos_los_vehiculos_disponibles", {}).items():
        content = "\n".join(serialize_node(payload))
        if content:
            documents.append(
                make_document(
                    section="disponibilidad_vehiculos",
                    title=f"Disponibilidad {vehicle_name}",
                    content=content,
                    source_path=f"todos_los_vehiculos_disponibles.{vehicle_name}",
                )
            )

    for vehicle_name, payload in data.get("vehiculos_detalles", {}).items():
        content = "\n".join(serialize_node(payload))
        if content:
            documents.append(
                make_document(
                    section="vehiculos_detalles",
                    title=f"Ficha tecnica {vehicle_name}",
                    content=content,
                    source_path=f"vehiculos_detalles.{vehicle_name}",
                )
            )

        for index, model_payload in enumerate(payload.get("modelos_disponibles", [])):
            model_name = model_payload.get("nombre", f"{vehicle_name} modelo {index + 1}")
            model_content = "\n".join(serialize_node(model_payload))
            if model_content:
                documents.append(
                    make_document(
                        section="vehiculos_detalles",
                        title=f"Modelo {model_name}",
                        content=model_content,
                        source_path=f"vehiculos_detalles.{vehicle_name}.modelos_disponibles[{index}]",
                    )
                )

        for version_name, version_payload in payload.get("versiones_disponibles", {}).items():
            version_content = "\n".join(serialize_node(version_payload))
            if version_content:
                documents.append(
                    make_document(
                        section="vehiculos_detalles",
                        title=f"Version {version_name}",
                        content=version_content,
                        source_path=f"vehiculos_detalles.{vehicle_name}.versiones_disponibles.{version_name}",
                    )
                )

    for vehicle_name, payload in data.get("Precios_Vehiculos_Actualizados", {}).items():
        content = "\n".join(serialize_node(payload))
        if content:
            documents.append(
                make_document(
                    section="precios",
                    title=f"Precios {vehicle_name}",
                    content=content,
                    source_path=f"Precios_Vehiculos_Actualizados.{vehicle_name}",
                )
            )

        if isinstance(payload, dict):
            for version_name, version_payload in payload.items():
                if not isinstance(version_payload, dict):
                    continue
                version_content = "\n".join(serialize_node(version_payload))
                if version_content:
                    documents.append(
                        make_document(
                            section="precios",
                            title=f"Precio {version_name}",
                            content=version_content,
                            source_path=f"Precios_Vehiculos_Actualizados.{vehicle_name}.{version_name}",
                        )
                    )

    provinces = data.get("distribucion", {}).get("agencias_oficiales_por_provincia", {})
    for province, agencies in provinces.items():
        content = "\n".join(serialize_node(agencies))
        if content:
            documents.append(
                make_document(
                    section="agencias",
                    title=f"Agencias en {province}",
                    content=content,
                    source_path=f"distribucion.agencias_oficiales_por_provincia.{province}",
                )
            )

    sections_with_generic_projection = (
        "empresa",
        "movilidad_electrica",
        "aplicaciones_coradir",
        "site_navigation",
        "leasing_estado_actual",
        "beneficios_discapacidad",
        "condiciones_compra_entrega",
        "infraestructura_carga",
        "contactos",
        "sitios_web",
    )

    for section_name in sections_with_generic_projection:
        payload = data.get(section_name)
        if payload:
            extend_generic_section(documents, section_name, payload, section_name)

    unique_documents = []
    seen_keys = set()
    for document in documents:
        dedupe_key = (document["title"], document["content"])
        if dedupe_key in seen_keys:
            continue
        seen_keys.add(dedupe_key)
        unique_documents.append(document)

    return unique_documents


def write_jsonl(documents: Iterable[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        for document in documents:
            output_file.write(json.dumps(document, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepara la base de conocimiento para el chatbot de movilidad.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH, help="Ruta al dataset JSON original.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH, help="Ruta del JSONL de salida.")
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8") as input_file:
        dataset = json.load(input_file)

    documents = build_documents(dataset)
    write_jsonl(documents, args.output)
    print(f"Documentos generados: {len(documents)}")
    print(f"Archivo de salida: {args.output}")


if __name__ == "__main__":
    main()
