import streamlit as st

def render_advisory_panel(advisories):
    st.subheader("Control Advisory Recommendations")
    if not advisories:
        st.info("No active recommendations.")
        return
        
    for idx, adv in enumerate(advisories):
        status_color = "red" if adv.get("status") == "critical" else "orange" if adv.get("status") == "caution" else "green"
        with st.container():
            st.markdown(f"""
            <div style='border: 1px solid {status_color}; padding: 10px; border-radius: 5px; margin-bottom: 10px;'>
                <h4 style='margin-top:0; color:{status_color}'>{adv.get('variable')}</h4>
                <p>Current: <b>{adv.get('current')}</b> | Recommended: <b>{adv.get('recommended')}</b></p>
                <p>Expected Impact: {adv.get('impact')} (Confidence: {adv.get('confidence')}%)</p>
            </div>
            """, unsafe_allow_html=True)
            if adv.get("status") == "critical":
                st.warning("Critical action required. Review limits before applying.")
            if st.button("Apply Recommendation", key=f"apply_{idx}"):
                st.success(f"Applied change to {adv.get('variable')}")
