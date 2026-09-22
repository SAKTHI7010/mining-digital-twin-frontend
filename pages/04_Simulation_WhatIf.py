import streamlit as st
import pandas as pd
from services.api_client import APIClient
from utils.state import get_selected_plant
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Simulation & What-If', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()
api = APIClient()

st.title("Simulation & What-If Analysis")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Simulation Inputs")
    with st.expander("Feed Conditions", expanded=True):
        feed_rate = st.slider("Feed Rate (t/h)", 800, 1500, 1150)
        feed_grade = st.slider("Cu Feed Grade (%)", 0.5, 2.5, 1.2)
        hardness = st.slider("Ore Hardness (Wi)", 10.0, 20.0, 14.5)
        
    with st.expander("Grinding Parameters"):
        sag_speed = st.slider("SAG Speed (%)", 60.0, 80.0, 72.5)
        ball_charge = st.slider("Ball Charge (%)", 20.0, 35.0, 28.0)
        
    with st.expander("Flotation Parameters"):
        air_flow = st.slider("Air Flow (m3/min)", 50, 150, 100)
        froth_depth = st.slider("Froth Depth (mm)", 100, 500, 300)

    run_sim = st.button("Run Simulation", type="primary", use_container_width=True)

with col2:
    st.subheader("Simulation Results")
    if run_sim:
        payload = {"feed_rate": feed_rate, "sag_speed": sag_speed}
        result = api.simulate(payload)
        
        st.success("Simulation Complete")
        
        c1, c2, c3 = st.columns(3)
        base = result['base_kpis']
        sim = result['simulated_kpis']
        
        c1.metric("Throughput (t/h)", f"{sim.get('throughput',0):.1f}", f"{sim.get('throughput',0) - base.get('throughput',0):.1f}")
        c2.metric("Recovery (%)", f"{sim.get('recovery',0):.1f}", f"{sim.get('recovery',0) - base.get('recovery',0):.1f}")
        c3.metric("Profit Impact", "$+12,500/day")
        
        st.markdown("### Projected Impact")
        # Placeholder for chart
        st.line_chart(pd.DataFrame({
            "Base": [85, 86, 85.5, 87, 87.3],
            "Simulated": [85, 86, 86.5, 87.8, 88.1]
        }))
    else:
        st.info("Adjust parameters and click Run Simulation.")
