import httpx
import time
from config.settings import get_settings
from services import endpoints
from services import mock_data

class APIClient:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = self.settings.BACKEND_BASE_URL.rstrip('/')
        self.timeout = 30
        self.retries = 3

    def _should_mock(self):
        return self.settings.MOCK_MODE

    def get(self, path, params=None):
        if self._should_mock():
            return None
        # Add actual HTTP call here if needed
        return None

    def post(self, path, data=None):
        if self._should_mock():
            return None
        return None

    def is_backend_healthy(self) -> bool:
        return self._should_mock()

    def get_plants(self):
        if self._should_mock(): return mock_data.get_mock_plants()
        return None

    def get_overview(self, plant_id):
        if self._should_mock(): return mock_data.get_mock_overview(plant_id)
        return None

    def get_live_state(self, plant_id):
        if self._should_mock(): return mock_data.get_mock_live_state(plant_id)
        return None

    def get_timeseries(self, plant_id, params=None):
        if self._should_mock(): return mock_data.get_mock_timeseries(plant_id, params)
        return None

    def get_unit(self, plant_id, unit_id):
        if self._should_mock(): return mock_data.get_mock_unit(plant_id, unit_id)
        return None

    def simulate(self, payload):
        if self._should_mock(): return mock_data.get_mock_simulation(payload)
        return None

    def optimize(self, payload):
        if self._should_mock(): return mock_data.get_mock_optimization(payload)
        return None

    def get_advisory(self, plant_id):
        if self._should_mock(): return mock_data.get_mock_advisory(plant_id)
        return None

    def get_diagnostics(self, asset_id):
        if self._should_mock(): return mock_data.get_mock_diagnostics(asset_id)
        return None

    def get_data_quality(self, plant_id):
        if self._should_mock(): return mock_data.get_mock_data_quality(plant_id)
        return None

    def get_model_metadata(self, plant_id):
        if self._should_mock(): return mock_data.get_mock_model_metadata(plant_id)
        return None
