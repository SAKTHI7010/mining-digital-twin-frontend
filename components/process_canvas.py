import streamlit as st
import streamlit.components.v1 as components
import json

def render_process_canvas(plant_id, live_data=None):
    st.subheader("Live Process Canvas")
    
    # Check if html file exists, otherwise fallback
    try:
        with open("assets/html/process_scene.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            # Inject live data as a JSON string to be picked up by JS
            data_str = json.dumps(live_data or {})
            html_content = html_content.replace('// INJECT_DATA_HERE', f'window.plantData = {data_str};')
            components.html(html_content, height=600)
    except FileNotFoundError:
        st.warning("3D Process Canvas not found. Showing 2D fallback.")
        st.markdown("""
        <div style="border:1px solid #555; height: 400px; display:flex; align-items:center; justify-content:center; background:#222;">
            <p style="color:#aaa;">[SVG Flowsheet Fallback] - Plant ID: {}</p>
        </div>
        """.format(plant_id), unsafe_allow_html=True)
