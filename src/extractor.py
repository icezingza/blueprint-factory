import fitz, docx, pathlib

def extract_contents(input_dir: pathlib.Path):
    """ดึงข้อความ+โค้ดจากทุกไฟล์ pdf/docx/txt"""
    data = {"text": "", "codes": []}
    for f in input_dir.iterdir():
        if f.suffix == ".pdf":
            data["text"] += "\n".join(page.get_text() for page in fitz.open(f))
        elif f.suffix == ".docx":
            data["text"] += "\n".join(p.text for p in docx.Document(f).paragraphs)
        elif f.suffix == ".txt":
            data["text"] += f.read_text(encoding="utf-8")
        # สกัดโค้ดในบล็อก ```...```
        data["codes"] += [line.strip() for line in data["text"].splitlines()
                          if line.startswith("```") and len(line) > 3]
    return data
