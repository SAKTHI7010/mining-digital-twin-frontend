import pytest
import sys
import os

# Add root directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import_app():
    # Very basic smoke test to ensure no syntax errors on import
    # Streamlit scripts are hard to test directly via import due to execution model,
    # but we can test helper modules
    from utils.formatting import format_value
    assert format_value(10.123, "t/h", 1) == "10.1 t/h"

def test_mock_data_structure():
    from services.mock_data import get_mock_overview
    data = get_mock_overview("PLANT_01")
    assert isinstance(data, dict)
    assert "throughput" in data
