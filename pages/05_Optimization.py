import streamlit as st
from services.api_client import APIClient
from components.header import render_header
from components.sidebar import render_sidebar
from components.advisory_panel import render_advisory_panel
from utils.state import init_session_state

st.set_page_config(page_title='Optimization', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

init_session_state()

render_header()
render_sidebar()
api = APIClient()

st.title("Process Optimization")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Objective")
    objective = st.radio("Select Optimization Objective", [
        "Maximize Profit",
        "Maximize Throughput",
        "Maximize Recovery",
        "Minimize Energy",
        "Minimize Water"
    ])
    
    st.subheader("Constraints")
    st.checkbox("Equipment Limits", value=True)
    st.checkbox("Product Grade Constraints", value=True)
    st.checkbox("Water Balance", value=True)
    
    run_opt = st.button("Run Optimizer", type="primary", use_container_width=True)

with col2:
    if run_opt:
        with st.spinner("Solving optimization problem..."):
            result = api.optimize({"objective": objective})
            
        st.success(f"Optimization Complete. Expected Gain: ${result.get('expected_gain', 0):,}/year")
        
        st.subheader("Recommended Setpoints")
        for rec in result.get('recommendations', []):
            st.markdown(f"""
            <div class='metric-card status-green'>
                <h4>{rec['variable']}</h4>
                <p>Change from {rec['current']} to <b>{rec['recommended']}</b></p>
                <p style="color: #2ECC71;">Impact: {rec['impact']} (Confidence: {rec['confidence']}%)</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Select objective and run optimizer to view recommendations.")
