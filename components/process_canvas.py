import streamlit as st
import graphviz

def render_process_canvas(plant_id, live_data=None):
    st.subheader("Live Process Canvas (2D Flowsheet)")
    
    # Create a graphviz directed graph
    graph = graphviz.Digraph(engine='dot')
    graph.attr(rankdir='LR', size='10,5', bgcolor='transparent')
    
    # Define node styles
    node_attr = {
        'shape': 'box',
        'style': 'filled,rounded',
        'fontname': 'Helvetica',
        'fontsize': '12',
        'margin': '0.2',
        'color': '#cbd5e1',     # border color
        'fillcolor': '#f8fafc'  # default background
    }
    graph.attr('node', **node_attr)
    
    # Define edge styles
    edge_attr = {
        'color': '#64748b',
        'arrowsize': '0.8',
        'fontname': 'Helvetica',
        'fontsize': '10'
    }
    graph.attr('edge', **edge_attr)
    
    # Helper to determine color based on status if live_data is provided
    def get_color(unit_id):
        default_color = '#f1f5f9'
        if live_data and 'units' in live_data:
            for u in live_data['units']:
                if u.get('unit_id') == unit_id:
                    status = u.get('status', 'normal')
                    if status == 'normal': return '#bbf7d0'    # green
                    if status == 'caution': return '#fef08a'   # yellow
                    if status == 'alarm': return '#fecaca'     # red
        return default_color

    # Add nodes (Equipment)
    graph.node('Feed', 'Ore Feed', shape='cylinder', fillcolor='#e2e8f0')
    graph.node('SAG', 'SAG Mill\\n(SAG_01)', fillcolor=get_color('SAG_01'))
    graph.node('BM', 'Ball Mill\\n(BM_01)', fillcolor=get_color('BM_01'))
    graph.node('CYC', 'Hydrocyclone', fillcolor='#e0f2fe', shape='invtriangle')
    graph.node('FLOT', 'Flotation\\n(FL_RO_01)', fillcolor=get_color('FL_RO_01'))
    graph.node('THK', 'Thickener\\n(THK_01)', fillcolor=get_color('THK_01'), shape='invtrapezium')
    graph.node('Tailings', 'Tailings', shape='cylinder', fillcolor='#e2e8f0')
    graph.node('Concentrate', 'Concentrate', shape='cylinder', fillcolor='#e2e8f0')

    # Add edges (Flows)
    graph.edge('Feed', 'SAG', label=' Fresh Ore')
    graph.edge('SAG', 'BM', label=' Slurry')
    graph.edge('BM', 'CYC', label=' Mill Discharge')
    graph.edge('CYC', 'BM', label=' Underflow\\n(Coarse)', style='dashed')
    graph.edge('CYC', 'FLOT', label=' Overflow\\n(Fine)')
    graph.edge('FLOT', 'THK', label=' Tailings')
    graph.edge('FLOT', 'Concentrate', label=' Froth Product')
    graph.edge('THK', 'Tailings', label=' Underflow')

    # Render the graph in Streamlit
    st.graphviz_chart(graph, use_container_width=True)
    
    # Add a simple legend below the flowsheet
    st.markdown('''
    <div style="display: flex; gap: 15px; margin-top: 10px; font-size: 14px;">
        <div style="display: flex; align-items: center;"><div style="width: 15px; height: 15px; background: #bbf7d0; border: 1px solid #ccc; margin-right: 5px;"></div> Normal</div>
        <div style="display: flex; align-items: center;"><div style="width: 15px; height: 15px; background: #fef08a; border: 1px solid #ccc; margin-right: 5px;"></div> Caution</div>
        <div style="display: flex; align-items: center;"><div style="width: 15px; height: 15px; background: #fecaca; border: 1px solid #ccc; margin-right: 5px;"></div> Alarm</div>
    </div>
    ''', unsafe_allow_html=True)
