import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(layout="wide")
st.title("📚 Database")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "database.xlsx"

try:
    df = pd.read_excel(DATA_PATH, skiprows=3)

    query = st.text_input("Search for a material:")
    if query:
        mask = df.astype(str).apply(lambda col: col.str.contains(query, case=False, na=False))
        filtered_df = df[mask.any(axis=1)]
    else:
        filtered_df = df
    
    st.dataframe(filtered_df.iloc[:,:6], use_container_width=True, height=800)

except FileNotFoundError:
    st.error("Database file not found. Please ensure 'database.xlsx' is in the 'data' folder.")