import plotly.graph_objects as go
import pandas as pd
from utils.constants import COLOR_NORMAL, COLOR_CAUTION, COLOR_ALARM, COLOR_OPTIMIZED

def apply_industrial_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=40, b=40),
        font=dict(color="white")
    )
    return fig

def create_kpi_gauge(name, value, min_v, max_v, target) -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': name},
        delta={'reference': target, 'increasing': {'color': COLOR_NORMAL}},
        gauge={
            'axis': {'range': [min_v, max_v]},
            'bar': {'color': COLOR_NORMAL if value >= target else COLOR_CAUTION},
            'steps': [
                {'range': [min_v, target * 0.9], 'color': "gray"},
                {'range': [target * 0.9, target], 'color': "lightgray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': target
            }
        }
    ))
    return apply_industrial_theme(fig)

def create_trend_chart(df: pd.DataFrame, y_cols: list, title: str) -> go.Figure:
    fig = go.Figure()
    for col in y_cols:
        if col in df.columns and "timestamp" in df.columns:
            fig.add_trace(go.Scatter(x=df["timestamp"], y=df[col], mode='lines', name=col))
    fig.update_layout(title=title)
    return apply_industrial_theme(fig)

def create_comparison_bar(base, current, optimized, labels) -> go.Figure:
    fig = go.Figure(data=[
        go.Bar(name='Base', x=labels, y=base),
        go.Bar(name='Current', x=labels, y=current),
        go.Bar(name='Optimized', x=labels, y=optimized)
    ])
    fig.update_layout(barmode='group')
    return apply_industrial_theme(fig)

def create_pareto_chart(x_values, y_values) -> go.Figure:
    fig = go.Figure([go.Bar(x=x_values, y=y_values)])
    return apply_industrial_theme(fig)

def create_health_heatmap(data) -> go.Figure:
    # Minimal heatmap placeholder
    df = pd.DataFrame(data)
    fig = go.Figure(data=go.Heatmap(z=df.values))
    return apply_industrial_theme(fig)

def create_scatter_recovery_grade(recovery, grade) -> go.Figure:
    fig = go.Figure(data=go.Scatter(x=recovery, y=grade, mode='markers'))
    fig.update_layout(xaxis_title="Recovery (%)", yaxis_title="Grade (%)")
    return apply_industrial_theme(fig)
