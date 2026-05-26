from __future__ import annotations

import argparse
import re
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree

import fitz
import nbformat


DOCX_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def slugify(value: str) -> str:
    value = value.strip().replace("\\", "/")
    value = re.sub(r"[/]+", "__", value)
    value = re.sub(r"[^\w.\-() ]+", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", " ", value)
    return value


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    compact: list[str] = []
    blank = False
    for line in lines:
        if not line:
            if not blank:
                compact.append("")
            blank = True
            continue
        compact.append(line)
        blank = False
    return "\n".join(compact).strip()


def target_path(source: Path, source_root: Path, output_root: Path) -> Path:
    rel = source.relative_to(source_root).with_suffix(".md")
    return output_root / rel


def frontmatter(source: Path, kind: str) -> str:
    return (
        f"# {source.stem}\n\n"
        f"- Fuente: `{source.name}`\n"
        f"- Tipo: {kind}\n"
        f"- Fecha de conversion: {date.today().isoformat()}\n\n"
        "> Conversion automatica para consulta, estudio y armado de presentacion. "
        "Puede requerir ajustes manuales si el material original contiene columnas, "
        "tablas complejas, imagenes o formulas.\n\n"
    )


def convert_pdf(source: Path, source_root: Path, output_root: Path) -> Path:
    doc = fitz.open(source)
    blocks = [frontmatter(source, "PDF")]
    blocks.append(f"- Paginas extraidas: {doc.page_count}\n\n")
    for index, page in enumerate(doc, start=1):
        text = clean_text(page.get_text())
        if text:
            blocks.append(f"## Pagina {index}\n\n{text}\n\n")
    output = target_path(source, source_root, output_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(blocks), encoding="utf-8")
    return output


def paragraph_text(paragraph: ElementTree.Element) -> str:
    pieces: list[str] = []
    for node in paragraph.iter():
        if node.tag == f"{{{DOCX_NS['w']}}}t" and node.text:
            pieces.append(node.text)
        elif node.tag == f"{{{DOCX_NS['w']}}}tab":
            pieces.append("\t")
        elif node.tag == f"{{{DOCX_NS['w']}}}br":
            pieces.append("\n")
    return clean_text("".join(pieces))


def convert_docx(source: Path, source_root: Path, output_root: Path) -> Path:
    blocks = [frontmatter(source, "DOCX")]
    with zipfile.ZipFile(source) as archive:
        xml = archive.read("word/document.xml")
    root = ElementTree.fromstring(xml)

    for element in root.iter():
        if element.tag == f"{{{DOCX_NS['w']}}}p":
            text = paragraph_text(element)
            if text:
                blocks.append(f"{text}\n\n")
        elif element.tag == f"{{{DOCX_NS['w']}}}tbl":
            rows: list[list[str]] = []
            for row in element.findall(".//w:tr", DOCX_NS):
                cells = []
                for cell in row.findall("./w:tc", DOCX_NS):
                    cell_text = " ".join(
                        paragraph_text(p)
                        for p in cell.findall(".//w:p", DOCX_NS)
                        if paragraph_text(p)
                    )
                    cells.append(cell_text)
                if cells:
                    rows.append(cells)
            if rows:
                blocks.append(format_markdown_table(rows))

    output = target_path(source, source_root, output_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(blocks), encoding="utf-8")
    return output


def format_markdown_table(rows: list[list[str]]) -> str:
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    header = padded[0]
    lines = [
        "| " + " | ".join(cell or " " for cell in header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in padded[1:]:
        lines.append("| " + " | ".join(cell or " " for cell in row) + " |")
    return "\n".join(lines) + "\n\n"


def convert_ipynb(source: Path, source_root: Path, output_root: Path) -> Path:
    notebook = nbformat.read(source, as_version=4)
    blocks = [frontmatter(source, "Jupyter Notebook")]
    for index, cell in enumerate(notebook.cells, start=1):
        cell_type = cell.get("cell_type", "cell")
        source_text = clean_text(cell.get("source", ""))
        if not source_text:
            continue
        if cell_type == "markdown":
            blocks.append(f"## Celda {index} - Markdown\n\n{source_text}\n\n")
        elif cell_type == "code":
            blocks.append(f"## Celda {index} - Codigo\n\n```python\n{source_text}\n```\n\n")
        else:
            blocks.append(f"## Celda {index} - {cell_type}\n\n{source_text}\n\n")

    output = target_path(source, source_root, output_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(blocks), encoding="utf-8")
    return output


def convert_all(source_root: Path, output_root: Path) -> list[Path]:
    converters = {
        ".pdf": convert_pdf,
        ".docx": convert_docx,
        ".ipynb": convert_ipynb,
    }
    converted: list[Path] = []
    for source in sorted(source_root.rglob("*")):
        if not source.is_file():
            continue
        if output_root in source.parents:
            continue
        converter = converters.get(source.suffix.lower())
        if converter is None:
            continue
        converted.append(converter(source, source_root, output_root))
    return converted


def write_index(output_root: Path, converted: list[Path]) -> None:
    lines = [
        "# Materiales de Clase Convertidos\n\n",
        "Carpeta generada automaticamente a partir de PDFs, notebooks y notas DOCX en `docs/clases`.\n\n",
        "## Archivos\n\n",
    ]
    for path in sorted(converted):
        rel = path.relative_to(output_root).as_posix()
        lines.append(f"- [{rel}]({rel})\n")
    (output_root / "README.md").write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convierte materiales de clase a Markdown.")
    parser.add_argument("--source", type=Path, default=Path("docs/clases"))
    parser.add_argument("--output", type=Path, default=Path("docs/clases/convertidos"))
    args = parser.parse_args()

    converted = convert_all(args.source, args.output)
    args.output.mkdir(parents=True, exist_ok=True)
    write_index(args.output, converted)
    print(f"Convertidos {len(converted)} archivos en {args.output}")


if __name__ == "__main__":
    main()
