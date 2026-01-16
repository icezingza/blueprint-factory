import pathlib

import docx
import fitz


def extract_contents(input_dir: pathlib.Path):
    """ดึงข้อความ+โค้ดจากทุกไฟล์ pdf/docx/txt"""
    data = {"text": "", "codes": []}
    for path in input_dir.iterdir():
        if path.suffix == ".pdf":
            data["text"] += "\n".join(page.get_text() for page in fitz.open(path))
        elif path.suffix == ".docx":
            data["text"] += "\n".join(
                paragraph.text for paragraph in docx.Document(path).paragraphs
            )
        elif path.suffix == ".txt":
            data["text"] += path.read_text(encoding="utf-8")
        data["codes"].extend(
            [
                line.strip()
                for line in data["text"].splitlines()
                if line.startswith("```") and len(line) > 3
            ]
        )
    return data
