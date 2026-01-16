import streamlit as st
import zipfile, io, pathlib, shutil, datetime, tempfile
from src.extractor import extract_contents
from src.packager import create_packs

st.set_page_config(page_title="Blueprint Factory", page_icon="⚙️", layout="centered")
st.title("⚙️ Blueprint Factory Web App")
st.markdown("วางไฟล์ PDF/Word/TXT → สร้างแพ็กเกจพร้อมขายทันที")

uploaded = st.file_uploader("เลือกไฟล์ (หลายไฟล์พร้อมกันได้)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

def generate_blueprint_package(uploaded_files):
    """Core logic to process files and generate a ZIP package."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_in = pathlib.Path(temp_dir)
        for file in uploaded_files:
            (temp_in / file.name).write_bytes(file.getbuffer())
            
        contents = extract_contents(temp_in)
        packs = create_packs(contents)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            for key, pack_path in packs.items():
                for file in pathlib.Path(pack_path).rglob("*"):
                    zf.write(file, arcname=f"{key}/{file.relative_to(pack_path)}")
        zip_buffer.seek(0)
        return zip_buffer

if st.button("สร้าง Blueprint", type="primary") and uploaded:
    with st.spinner("กำลังสร้าง..."):
        zip_buffer = generate_blueprint_package(uploaded)

    st.success("✅ สร้างเสร็จ!")
    st.download_button("📦 ดาวน์โหลด Blueprint ทั้งหมด", zip_buffer,
                       file_name=f"blueprint-{datetime.datetime.now():%Y%m%d-%H%M}.zip",
                       mime="application/zip")
