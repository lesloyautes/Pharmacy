import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="COSMAX Pharmacy", layout="wide")

st.markdown("""<style>
header, footer {display:none !important;}
.block-container {padding:0 !important; max-width:100% !important;}
div[data-testid="stAppViewContainer"] {overflow:hidden;}
iframe {height:100vh !important; width:100% !important; display:block;}
</style>""", unsafe_allow_html=True)

with open("index.html", encoding="utf-8") as f:
    components.html(f.read(), height=800, scrolling=False)