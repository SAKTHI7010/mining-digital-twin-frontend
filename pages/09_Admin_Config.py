import streamlit as st
from config.settings import get_settings
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Admin Config', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_header()
render_sidebar()

st.title("Admin & Configuration")

settings = get_settings()

col1, col2 = st.columns(2)

with col1:
    st.subheader("System Settings")
    st.text_input("Backend URL", value=settings.BACKEND_BASE_URL)
    st.checkbox("Force Mock Mode", value=settings.MOCK_MODE, disabled=True, help="Set via .env file")
    st.text_input("App Environment", value=settings.APP_ENV, disabled=True)
    if st.button("Test Connection"):
        st.success("Connection to backend successful (mocked)")

with col2:
    st.subheader("Alert Thresholds")
    st.slider("Throughput Tolerance (%)", 1, 20, 5)
    st.slider("Recovery Tolerance (%)", 0.1, 5.0, 1.0)
    st.slider("Grade Tolerance (%)", 0.1, 5.0, 0.5)
    
    st.button("Save Configuration", type="primary")

st.markdown("---")
st.write("App Version: 1.0.0")
