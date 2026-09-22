import streamlit as st
from utils.constants import TIME_WINDOWS

def render_sidebar():
    with st.sidebar:
        st.header("Control Panel")
        st.selectbox("Circuit", ["Primary Grinding", "Flotation", "Dewatering"])
        time_str = st.selectbox("Time Window", list(TIME_WINDOWS.keys()), index=3)
        st.session_state.time_window = TIME_WINDOWS[time_str]
        
        st.markdown("---")
        st.checkbox("Mock Mode", key="mock_mode")
        if st.button("Refresh Data", use_container_width=True):
            st.rerun()
        
        st.markdown("---")
        st.subheader("Quick KPI")
        st.metric("Throughput", "1,150 t/h", "+12 t/h")
        st.metric("Recovery", "87.3 %", "-0.2 %")
