import streamlit as st

st.set_page_config(page_title="Bryan's Thermal Toolkit", page_icon="🔥", layout="wide")

st.title("🔥 Bryan's Thermal Toolkit 🛰️")
st.write("")
st.write("Welcome to Bryan's Thermal Toolkit! A suite of tools and resources for thermal engineering enthusiasts and professionals! Enjoy. (^-^)-b")
st.write("")
st.write("")
st.write("")


with st.container():
    c1, c2, c3 = st.columns(3)

    with c1:
        st.page_link("pages/Tools.py", icon="🔧")
        st.write("  Thermal calculators.")

    with c2:
        st.page_link("pages/Database.py", icon="📚")
        st.write("  Thermal physical and optical properties.")

    with c3:
        st.page_link("pages/Notes.py", icon="🗒️")
        st.write("  Thermal engineering notes.")


st.markdown("---")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Developed by Bryan Serrano - Contact: bryanaserrano3@gmail.com")