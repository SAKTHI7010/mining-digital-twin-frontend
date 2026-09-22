import streamlit as st
from utils.state import get_selected_plant
from utils.constants import UNIT_LABELS
from services.api_client import APIClient
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Unit Operations', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()

plant_id = get_selected_plant()
api = APIClient()

unit_type = st.selectbox("Select Unit Type", list(UNIT_LABELS.values()))
# Map back to code
unit_code = [k for k, v in UNIT_LABELS.items() if v == unit_type][0]
unit_id = f"{unit_code}_01"

st.header(f"{unit_type} Detail ({unit_id})")

unit_data = api.get_unit(plant_id, unit_id)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Current State (Measured)")
    if unit_data and 'current_state' in unit_data:
        for k, v in unit_data['current_state'].items():
            st.metric(k.replace('_', ' ').title(), f"{v:.1f}")

with col2:
    st.subheader("Recommended Actions")
    if unit_data and 'recommended_mvs' in unit_data:
        for k, v in unit_data['recommended_mvs'].items():
            st.metric(f"New {k.replace('_', ' ').title()}", f"{v:.1f}", delta=f"{v - unit_data['current_state'].get(k, 0):.1f}")

st.markdown("---")
st.subheader("Control Variables")
st.table([
    {"Variable": "Feed Rate", "Type": "MV", "Value": "1150", "Unit": "t/h"},
    {"Variable": "Ore Hardness", "Type": "DV", "Value": "14.2", "Unit": "kWh/t"},
    {"Variable": "P80", "Type": "CV", "Value": "150", "Unit": "µm"}
])
