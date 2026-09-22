import streamlit as st

def render_alarm_panel(alarms):
    st.subheader("Active Alarms")
    if not alarms:
        st.success("No active alarms.")
        return
        
    for alarm in alarms:
        color = "#E74C3C" if alarm.get("severity") == "high" else "#F39C12" if alarm.get("severity") == "medium" else "#F1C40F"
        st.markdown(f"""
        <div style='background-color:#1E1E1E; border-left: 4px solid {color}; padding: 10px; margin-bottom: 5px; display: flex; justify-content: space-between;'>
            <div>
                <strong>{alarm.get('type')}</strong> - {alarm.get('timestamp')}
            </div>
            <button style='background:#333; color:white; border:none; padding:2px 10px;'>Ack</button>
        </div>
        """, unsafe_allow_html=True)
