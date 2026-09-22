import streamlit as st
import pandas as pd
from utils.state import init_session_state, get_selected_plant
from services.api_client import APIClient
from components.header import render_header
from components.sidebar import render_sidebar

st.set_page_config(page_title='Data Quality', layout='wide')
with open("assets/css/custom.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

init_session_state()

render_header()
render_sidebar()

plant_id = get_selected_plant()
api = APIClient()

st.title("Data Quality & Sensor Validation")

dq = api.get_data_quality(plant_id)

st.metric("Overall Freshness Score", f"{dq.get('freshness_score', 0):.1f}%")

st.subheader("Tag Availability")
if dq and 'tag_stats' in dq:
    df = pd.DataFrame(dq['tag_stats'])
    st.dataframe(df, use_container_width=True)

st.subheader("Model Confidence & Adaptation")
metadata = api.get_model_metadata(plant_id)
if metadata and 'models' in metadata:
    for model in metadata['models']:
        st.markdown(f"""
        <div class='metric-card'>
            <h4>{model.get('name')}</h4>
            <p>Version: {model.get('version')} | Accuracy: {model.get('accuracy')}%</p>
        </div>
        """, unsafe_allow_html=True)
