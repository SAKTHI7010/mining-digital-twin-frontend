import streamlit as st
import datetime
from utils.state import get_selected_plant, set_selected_plant
from components.api_status import render_api_status

def render_header():
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("<h2 style='margin:0;'>⛏️ Mining Digital Twin</h2>", unsafe_allow_html=True)
        plant = st.selectbox("Select Plant", ["PLANT_001"], index=0, label_visibility="collapsed")
        set_selected_plant(plant)
    with col2:
        mode = "Mock" if st.session_state.mock_mode else "Live"
        st.markdown(f"<div style='text-align:center; padding:10px; background-color:#333; color:white; border-radius:5px;'>Mode: <b>{mode}</b></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align:right; margin-bottom: 5px;'>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)
        render_api_status()
    st.markdown("---")
