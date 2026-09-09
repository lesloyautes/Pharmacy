import streamlit as st

st.set_page_config(page_title="COSMAX Pharmacy", layout="centered")
st.markdown("""
<div style="text-align:center; margin-top:28vh; font-family:sans-serif">
  <h2>COSMAX 약국덱 · 전략마케팅 5조</h2>
  <a href="/app/static/index.html" target="_self"
     style="display:inline-block; margin-top:16px; padding:14px 32px; border-radius:99px;
            background:#D6336C; color:#fff; font-weight:700; text-decoration:none">
    약국으로 입장하기 →
  </a>
</div>
""", unsafe_allow_html=True)
