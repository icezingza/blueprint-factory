import pathlib, shutil, datetime
from jinja2 import Environment, FileSystemLoader

def create_packs(content: dict) -> dict:
    """สร้าง 3 แพ็กเกจ zip พร้อมขาย"""
    out = pathlib.Path("output") / datetime.datetime.now().strftime("%Y%m%d_%H%M")
    packs = {"starter": out / "starter-pack",
             "agency": out / "agency-pack",
             "whitelabel": out / "whitelabel-pack"}
    # สร้างโฟลเดอร์เปล่า
    for p in packs.values():
        p.mkdir(parents=True, exist_ok=True)
    # ใส่ของแต่ละแพ็ก
    for key, root in packs.items():
        (root / "src").mkdir(exist_ok=True)
        if content["codes"]:
            (root / "src" / "main.py").write_text("\n".join(content["codes"][:2]), encoding="utf-8")
        (root / "README.md").write_text(_readme(key), encoding="utf-8")
        if key != "starter":
            (root / "docker-compose.yml").write_text(_docker(), encoding="utf-8")
            (root / "slides.pptx").touch()  # placeholder
        if key == "whitelabel":
            (root / "LICENSE").write_text("MIT License (White-label)", encoding="utf-8")
    return {k: str(v) for k, v in packs.items()}

def _readme(tier: str) -> str:
    return f"""# NaMo Blueprint ({tier})
สรุปเนื้อหาจากไฟล์ที่อัปโหลด  
รันได้ทันทีด้วย `docker-compose up` (ยกเว้น starter)
"""

def _docker() -> str:
    return """version: \"3.8\"
services:
  app:
    build: .
    ports:
      - \"8000:8000\"
"""
