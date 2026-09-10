import streamlit as st

st.set_page_config(
    page_title="Streamlit Use Cases Demo",
    page_icon="⚡",
    layout="wide",
)

page_one = st.Page(
    "views/render.py",
    title="Client Render",
    url_path="client_render",
)

page_two = st.Page(
    "admin/render.py",
    title="Admin Render",
    url_path="admin_render",
)

pg = st.navigation([page_one, page_two])
pg.run()
