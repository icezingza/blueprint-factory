# ⚙️ Blueprint Factory

[![Docker Build](https://img.shields.io/badge/Docker-Ready-2496ed?logo=docker&logoColor=white)](https://ghcr.io/icezingza/blueprint-factory)
[![CI](https://github.com/icezingza/blueprint-factory/actions/workflows/ci.yml/badge.svg)](https://github.com/icezingza/blueprint-factory/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/icezingza/blueprint-factory?display_name=tag)](https://github.com/icezingza/blueprint-factory/releases)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit Cloud](https://img.shields.io/badge/Streamlit-Cloud-ff4b4b?logo=streamlit&logoColor=white)](https://share.streamlit.io/icezingza/blueprint-factory)

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=icezingza/blueprint-factory)

**TH:** Blueprint Factory คือเว็บแอปที่ช่วยเปลี่ยนไฟล์ PDF/Word/TXT ให้เป็นแพ็กเกจดิจิทัลพร้อมขาย (Starter / Agency / Whitelabel) ด้วยการอัปโหลดครั้งเดียวแล้วดาวน์โหลด ZIP ได้ทันที.

**EN:** Blueprint Factory turns PDF/Word/TXT files into ready-to-sell digital packages (Starter / Agency / Whitelabel) with a single upload and one-click ZIP export.

## Features / ฟีเจอร์
- รองรับหลายไฟล์ PDF, DOCX, TXT พร้อมกัน / Multi-file upload support.
- สร้างโฟลเดอร์แพ็กเกจอัตโนมัติ / Automated package structure.
- ดาวน์โหลด ZIP ครั้งเดียว / One-click ZIP download.
- แยกเก็บผลลัพธ์ใน `output/` / Outputs stored in `output/`.

## Quick Start (Local) / เริ่มใช้งานบนเครื่อง
```bash
git clone https://github.com/icezingza/blueprint-factory.git
cd blueprint-factory
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
เปิด `http://localhost:8501`

## Docker Compose (Local) / รันแบบ Docker
```bash
docker-compose up
```
เปิด `http://localhost:8501`

## GHCR (Container Registry)
```bash
docker run -p 8501:8501 ghcr.io/icezingza/blueprint-factory:latest
```
มีแท็กเสริมชื่อ `ghcr.io/icezingza/namo-hub:latest` เพื่อใช้งานกับชื่อแบรนด์เดิม.

## Streamlit Cloud
Deploy ฟรีผ่าน Streamlit Cloud:
1) ไปที่ `https://share.streamlit.io`
2) เลือก repo `icezingza/blueprint-factory` และไฟล์ `app.py`
3) กด Deploy

## Development / การพัฒนา
```bash
pip install -r requirements.txt -r requirements-dev.txt
black --check .
flake8 .
pytest
```

## Versioned Images / เวอร์ชันของ Image
- `ghcr.io/icezingza/blueprint-factory:latest`
- `ghcr.io/icezingza/blueprint-factory:v1.0.0`
- `ghcr.io/icezingza/namo-hub:latest`
- `ghcr.io/icezingza/namo-hub:v1.0.0`

## GitHub Pages
Landing page: `https://icezingza.github.io/blueprint-factory`

## Project Structure / โครงสร้างโปรเจกต์
```text
blueprint-factory/
├── app.py
├── src/
│   ├── extractor.py
│   ├── packager.py
│   └── templates.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── docs/
└── .github/workflows/
```

Developed by IceZingZa
