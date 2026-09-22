import streamlit as st
from utils.state import init_session_state

st.set_page_config(page_title='Mining Digital Twin', layout='wide', page_icon='⛏️')

with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

init_session_state()

from components.header import render_header
from components.sidebar import render_sidebar
from components.api_status import render_api_status

render_header()
render_sidebar()

st.title("Welcome to Mining Digital Twin")
st.markdown("""
This application provides a comprehensive digital twin for mining and metallurgical operations. 
Navigate through the pages on the left to monitor live operations, run simulations, get optimization recommendations, and analyze asset health.
""")

st.info("Select a page from the sidebar to begin.")
