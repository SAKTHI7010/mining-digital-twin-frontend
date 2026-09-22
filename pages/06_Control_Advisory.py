import streamlit as st
import pandas as pd
from utils.state import get_selected_plant
from services.api_client import APIClient
from components.header import render_header
from components.sidebar import render_sidebar
from components.advisory_panel import render_advisory_panel

st.set_page_config(page_title='Control Advisory', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()

plant_id = get_selected_plant()
api = APIClient()

st.title("Advanced Process Control (APC) Advisory")

col1, col2 = st.columns([2, 1])

with col1:
    advisory_data = api.get_advisory(plant_id)
    if advisory_data and 'advisories' in advisory_data:
        render_advisory_panel(advisory_data['advisories'])
    else:
        st.info("No active advisories.")
        
    st.subheader("MV/CV/DV Matrix (Grinding Circuit)")
    st.table(pd.DataFrame([
        {"Variable": "Feed Rate (MV)", "SAG Weight": "+0.8", "P80": "+0.5"},
        {"Variable": "SAG Speed (MV)", "SAG Weight": "-0.6", "P80": "-0.4"},
        {"Variable": "Water Addition (MV)", "SAG Weight": "-0.2", "P80": "-0.7"},
        {"Variable": "Ore Hardness (DV)", "SAG Weight": "+0.9", "P80": "+0.6"}
    ]))

with col2:
    st.subheader("APC Status")
    st.metric("Readiness Score", "92%", "Good")
    st.info("Optimizer connection: Active (Closed-loop candidate)")
    
    st.subheader("Active Constraints")
    st.markdown("""
    - **High**: SAG Mill Power (Max 14 MW)
    - **Medium**: Cyclone Feed Density (Max 65%)
    """)
