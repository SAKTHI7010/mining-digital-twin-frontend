import streamlit as st
from utils.state import get_selected_plant
from services.api_client import APIClient
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Asset Health', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()
api = APIClient()

st.title("Asset Health & Diagnostics")

diag = api.get_diagnostics("SAG_01")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Equipment Health Scores")
    st.markdown(f"""
    <div class='metric-card status-amber'>
        <h3>SAG Mill</h3>
        <h1 style="color: #F39C12;">{diag.get('health_score', 0)}%</h1>
        <p>RUL: {diag.get('rul_days', 'N/A')} days</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='metric-card status-green'>
        <h3>Ball Mill</h3>
        <h1 style="color: #2ECC71;">94%</h1>
        <p>RUL: >180 days</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Active Anomalies")
    if diag and 'anomalies' in diag:
        for anom in diag['anomalies']:
            st.error(f"**{anom.get('type')}** detected (Severity: {anom.get('severity')}) at {anom.get('timestamp')}")
            
    st.subheader("Soft Sensor Estimates")
    st.metric("Liner Wear Proxy", "65%", "+2% from last week")
    st.metric("Bearing Temp Trend", "Stable", "")
