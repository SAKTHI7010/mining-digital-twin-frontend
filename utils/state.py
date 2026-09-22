import streamlit as st

def init_session_state():
    if "selected_plant" not in st.session_state:
        st.session_state.selected_plant = "PLANT_001"
    if "mock_mode" not in st.session_state:
        from config.settings import get_settings
        st.session_state.mock_mode = get_settings().MOCK_MODE
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    if "time_window" not in st.session_state:
        st.session_state.time_window = 1440
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = []

def get_selected_plant() -> str:
    return st.session_state.get("selected_plant", "PLANT_001")

def set_selected_plant(plant_id: str):
    st.session_state.selected_plant = plant_id

def get_mock_mode() -> bool:
    return st.session_state.get("mock_mode", True)

def get_time_window() -> int:
    return st.session_state.get("time_window", 1440)

def save_scenario(name: str, inputs: dict, results: dict):
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = []
    st.session_state.scenarios.append({
        "name": name,
        "inputs": inputs,
        "results": results
    })

def get_scenarios() -> list:
    return st.session_state.get("scenarios", [])
