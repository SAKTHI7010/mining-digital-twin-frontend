import streamlit as st
from config.settings import get_settings

def render_api_status():
    settings = get_settings()
    if settings.MOCK_MODE:
        color = "orange"
        status = "Mock Mode"
    else:
        # Assuming healthy if not mock for UI simplicity in this component
        color = "green"
        status = "Connected"
        
    st.markdown(f"""
    <div style='text-align: right; display:flex; justify-content: flex-end; align-items:center; gap: 5px;'>
        <div style='width: 10px; height: 10px; border-radius: 50%; background-color: {color};'></div>
        <span style='font-size: 12px; color: #CCC;'>API: {status}</span>
    </div>
    """, unsafe_allow_html=True)
