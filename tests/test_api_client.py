import pytest
from services.api_client import APIClient

def test_api_client_initialization():
    client = APIClient()
    assert client is not None
    assert hasattr(client, 'base_url')
    assert hasattr(client, 'timeout')

def test_get_plants_mock():
    client = APIClient()
    # Assuming mock mode is True by default for tests based on settings
    plants = client.get_plants()
    assert plants is not None
    assert len(plants) > 0
    assert "plant_id" in plants[0]

def test_get_overview_mock():
    client = APIClient()
    overview = client.get_overview("PLANT_001")
    assert overview is not None
    assert "throughput" in overview
    assert "recovery" in overview
