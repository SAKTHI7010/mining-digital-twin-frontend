import streamlit as st
import pandas as pd
from utils.state import get_selected_plant
from services.api_client import APIClient
from components.kpi_cards import render_kpi_cards
from components.trend_charts import render_trend_chart
from components.alarm_panel import render_alarm_panel
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Executive Overview', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()

plant_id = get_selected_plant()
api = APIClient()

overview_data = api.get_overview(plant_id) or {}
kpis_row1 = {
    "throughput": overview_data.get("throughput"),
    "recovery": overview_data.get("recovery"),
    "concentrate_grade": overview_data.get("concentrate_grade"),
    "tail_grade": overview_data.get("tail_grade")
}
kpis_row2 = {
    "energy_intensity": overview_data.get("energy_intensity"),
    "water_intensity": overview_data.get("water_intensity"),
    "availability": overview_data.get("availability")
}

render_kpi_cards(kpis_row1)
st.markdown("<br>", unsafe_allow_html=True)
render_kpi_cards(kpis_row2)

st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("24h Trend")
    ts_data = api.get_timeseries(plant_id)
    if ts_data and "data" in ts_data:
        df = pd.DataFrame(ts_data["data"])
        render_trend_chart(df, ["throughput", "recovery"], "Throughput & Recovery")

with col2:
    render_alarm_panel([
        {"type": "SAG Mill High Power", "severity": "high", "timestamp": "10 min ago"},
        {"type": "Thickener High Torque", "severity": "medium", "timestamp": "2 hours ago"}
    ])
    
st.markdown("---")
st.subheader("Economic Value Opportunity")
st.metric("Estimated Daily Opportunity", "$45,200", "+$2,100")
