import streamlit as st
from pathlib import Path

# Укажите путь к вашему HTML-файлу
html_file_path = "index (1).html"

# Прочитайте содержимое HTML-файла
html_content = Path(html_file_path).read_text(encoding="utf-8")

# Настройте страницу Streamlit
st.set_page_config(
    page_title="Портфолио Графического Дизайнера",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Отобразите HTML-контент
st.components.v1.html(html_content, width=None, height=2000, scrolling=True)