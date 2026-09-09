import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="COSMAX Pharmacy", layout="wide")

# 접속 즉시 약국덱(정적 HTML)으로 자동 이동
components.html(
    "<script>window.parent.location.replace('/app/static/index.html');</script>",
    height=0,
)

# 자동 이동이 안 될 때를 위한 예비 링크
st.markdown("""
<div style="text-align:center; margin-top:30vh; font-family:sans-serif; color:#8C7F7B">
  약국으로 이동 중이에요…<br><br>
  <a href="/app/static/index.html" target="_self"
     style="color:#D6336C; font-weight:700">자동으로 넘어가지 않으면 여기를 눌러주세요</a>
</div>
""", unsafe_allow_html=True)
