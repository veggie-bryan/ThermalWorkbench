import streamlit as st
from pathlib import Path


st.set_page_config(layout="wide")
st.title("🗒️ Notes")

NOTES_PATH = Path(__file__).resolve().parent.parent / "data" / "notes.txt"
NOTES_PATH.parent.mkdir(parents=True, exist_ok=True)

text = NOTES_PATH.read_text(encoding="utf-8") if NOTES_PATH.exists() else ""

new_text = st.text_area("Enter Notes:", value=text, height=600)

if new_text != text:
    NOTES_PATH.write_text(new_text, encoding="utf-8")
    st.success("Notes saved!")
