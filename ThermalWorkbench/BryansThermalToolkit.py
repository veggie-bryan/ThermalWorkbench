import streamlit as st

st.set_page_config(page_title="Bryan's Thermal Toolkit", page_icon="🌡️", layout="wide")

st.title("🌡️ Bryan's Thermal Toolkit")
st.write("Select Section.")

with st.container():
    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("🔧 Tools")
        st.write("Thermal Calculators")
        st.page_link("pages/Tools.py", "Browse Tools", icon="🔧")

    with c2:
        st.subheader("📚 Database")
        st.write("Thermal Physical/Optical Properties")
        st.page_link("pages/Database.py", "Browse Database", icon="📚")

    with c3:
        st.subheader("🗒️ Notes")
        st.write("Bryan's Thermal Engineering Notes")
        st.page_link("pages/Notes.py", "Browse Notes", icon="🗒️")

st.markdown("---")
st.write("Developed by Bryan Serrano - Contact: bryanaserrano3@gmail.com")