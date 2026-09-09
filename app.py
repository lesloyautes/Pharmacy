import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="COSMAX Pharmacy", layout="wide")
st.markdown("<style>.block-container{padding:0} header,footer{display:none}</style>", unsafe_allow_html=True)

with open("index.html", encoding="utf-8") as f:
    components.html(f.read(), height=900, scrolling=False)