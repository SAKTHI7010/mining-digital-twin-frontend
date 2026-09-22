import streamlit as st
import datetime
from utils.state import init_session_state, get_selected_plant
from services.api_client import APIClient
from components.process_canvas import render_process_canvas
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Live Process Twin', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

init_session_state()

render_header()
render_sidebar()

plant_id = get_selected_plant()
api = APIClient()

live_state = api.get_live_state(plant_id)

st.title("Live Process Flowsheet")
st.markdown(f"Last updated: **{datetime.datetime.now().strftime('%H:%M:%S')}**")

col1, col2 = st.columns([3, 1])

with col1:
    render_process_canvas(plant_id, live_state)

with col2:
    st.subheader("Unit Details")
    st.info("Click a unit on the flowsheet to view details.")
    # Placeholder for selected unit details
    st.markdown("""
    **Selected:** SAG Mill (SAG_01)
    - Status: Normal
    - Feed Rate: 1150 t/h
    - Speed: 72.5 %
    - Power: 12.5 MW
    """)
