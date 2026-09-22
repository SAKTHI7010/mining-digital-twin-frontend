import streamlit as st
from utils.plotting import create_trend_chart, create_comparison_bar

def render_trend_chart(df, tags, title):
    fig = create_trend_chart(df, tags, title)
    st.plotly_chart(fig, use_container_width=True)

def render_overlay_chart(base, current, optimized):
    # Simplified placeholder for overlay
    st.write("Overlay Chart (Base vs Current vs Optimized)")

def render_sparkline(values):
    st.line_chart(values, height=100)
