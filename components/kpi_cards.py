import streamlit as st
from utils.formatting import format_value, format_delta
from utils.constants import KPI_TARGETS

def render_traffic_light(status):
    colors = {"good": "#2ECC71", "caution": "#F39C12", "alarm": "#E74C3C", "normal": "#95A5A6"}
    color = colors.get(status, colors["normal"])
    return f"<div style='width: 15px; height: 15px; border-radius: 50%; background-color: {color}; display: inline-block;'></div>"

def render_kpi_cards(kpis: dict):
    cols = st.columns(len(kpis))
    for col, (kpi_name, value) in zip(cols, kpis.items()):
        target = KPI_TARGETS.get(kpi_name, 0)
        delta_val, status = format_delta(value, target)
        light = render_traffic_light(status)
        with col:
            st.markdown(f"""
            <div style='background-color:#1E1E1E; padding:15px; border-radius:5px; border-left: 4px solid {status_color(status)};'>
                <div style='color:#AAA; font-size:12px; text-transform:uppercase;'>{kpi_name.replace('_', ' ')} {light}</div>
                <div style='font-size:24px; font-weight:bold; margin-top:5px;'>{format_value(value, '')}</div>
                <div style='font-size:14px; color:{status_color(status)};'>{delta_val} from target</div>
            </div>
            """, unsafe_allow_html=True)

def status_color(status):
    return {"good": "#2ECC71", "caution": "#F39C12", "alarm": "#E74C3C"}.get(status, "#FFF")
