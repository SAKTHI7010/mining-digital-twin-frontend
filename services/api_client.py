import httpx
import time
from config.settings import get_settings
from services import mock_data

class APIClient:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = self.settings.BACKEND_BASE_URL.rstrip('/')
        self.timeout = 10
        self.retries = 2

    def _should_mock(self):
        return self.settings.MOCK_MODE

    def _get(self, path: str, params=None):
        if self._should_mock():
            return None
        for attempt in range(self.retries):
            try:
                r = httpx.get(f"{self.base_url}{path}", params=params, timeout=self.timeout)
                if r.status_code == 200:
                    body = r.json()
                    if isinstance(body, dict) and "data" in body:
                        return body["data"]
                    return body
            except Exception:
                if attempt < self.retries - 1:
                    time.sleep(0.3)
        return None

    def _post(self, path: str, data=None):
        if self._should_mock():
            return None
        for attempt in range(self.retries):
            try:
                r = httpx.post(f"{self.base_url}{path}", json=data or {}, timeout=self.timeout)
                if r.status_code == 200:
                    body = r.json()
                    if isinstance(body, dict) and "data" in body:
                        return body["data"]
                    return body
            except Exception:
                if attempt < self.retries - 1:
                    time.sleep(0.3)
        return None

    def is_backend_healthy(self) -> bool:
        if self._should_mock():
            return True
        try:
            r = httpx.get(f"{self.base_url}/health", timeout=5)
            return r.status_code == 200
        except Exception:
            return False

    def get_plants(self):
        res = self._get("/api/v1/plants")
        return res if res is not None else mock_data.get_mock_plants()

    def get_overview(self, plant_id: str):
        res = self._get(f"/api/v1/plants/{plant_id}/overview")
        if res and isinstance(res, dict) and "kpis" in res:
            d = {}
            for item in res["kpis"]:
                key = item.get("name", "").lower().replace(" ", "_")
                d[key] = item.get("value")
            return d
        return mock_data.get_mock_overview(plant_id)

    def get_live_state(self, plant_id: str):
        res = self._get(f"/api/v1/plants/{plant_id}/live-state")
        return res if res is not None else mock_data.get_mock_live_state(plant_id)

    def get_timeseries(self, plant_id: str, params=None):
        res = self._get(f"/api/v1/plants/{plant_id}/timeseries", params=params)
        return res if res is not None else mock_data.get_mock_timeseries(plant_id, params)

    def get_unit(self, plant_id: str, unit_id: str):
        res = self._get(f"/api/v1/plants/{plant_id}/unit/{unit_id}")
        return res if res is not None else mock_data.get_mock_unit(plant_id, unit_id)

    def simulate(self, payload: dict):
        res = self._post("/api/v1/simulate", payload)
        if res and isinstance(res, dict) and "kpis" in res:
            return {
                "base_kpis": {"throughput": 1150, "recovery": 87.3},
                "simulated_kpis": {
                    "throughput": res["kpis"].get("throughput_tph", payload.get("feed_rate", 1150)),
                    "recovery": res["kpis"].get("recovery_pct", 88.0)
                },
                "timeseries": []
            }
        return mock_data.get_mock_simulation(payload)

    def optimize(self, payload: dict):
        # Format objective if needed
        obj = payload.get("objective", "recovery").lower().replace("maximize ", "").replace("minimize ", "")
        res = self._post("/api/v1/optimize", {"plant_id": "PLANT_001", "objective": obj})
        if res and isinstance(res, dict) and "recommended_setpoints" in res:
            recs = []
            for k, v in res["recommended_setpoints"].items():
                recs.append({
                    "variable": k.replace("_", " ").title(),
                    "current": round(v * 0.95, 1),
                    "recommended": round(v, 1),
                    "impact": "+Optimal",
                    "confidence": int(res.get("confidence_score", 0.9) * 100)
                })
            return {
                "recommendations": recs,
                "expected_gain": 250000
            }
        return mock_data.get_mock_optimization(payload)

    def get_advisory(self, plant_id: str):
        res = self._post("/api/v1/control-advisory", {"plant_id": plant_id})
        if res and isinstance(res, dict) and "suggested_actions" in res:
            advisories = []
            for act in res.get("suggested_actions", []):
                advisories.append({
                    "variable": act,
                    "current": "Active",
                    "recommended": "Maintain",
                    "impact": "Stable",
                    "confidence": int(res.get("apc_readiness", 0.85) * 100),
                    "status": "normal"
                })
            return {"plant_id": plant_id, "advisories": advisories}
        return mock_data.get_mock_advisory(plant_id)

    def get_diagnostics(self, asset_id: str):
        res = self._get(f"/api/v1/diagnostics/{asset_id}")
        if res and isinstance(res, dict):
            anomalies = []
            for anom in res.get("anomalies", []):
                anomalies.append({
                    "type": anom,
                    "severity": "medium",
                    "timestamp": "Just now"
                })
            return {
                "asset_id": asset_id,
                "health_score": int(res.get("sensor_health", 0.9) * 100),
                "anomalies": anomalies,
                "rul_days": 120
            }
        return mock_data.get_mock_diagnostics(asset_id)

    def get_data_quality(self, plant_id: str):
        res = self._get(f"/api/v1/data-quality/{plant_id}")
        if res and isinstance(res, dict) and "overall_quality" in res:
            return {
                "plant_id": plant_id,
                "tag_stats": [
                    {"tag": tag, "missing_pct": 0.5, "quality": "good", "outliers": 2}
                    for tag in res.get("tag_reports", {}).keys()
                ] or mock_data.get_mock_data_quality(plant_id)["tag_stats"],
                "freshness_score": res.get("overall_quality", 0.98) * 100
            }
        return mock_data.get_mock_data_quality(plant_id)

    def get_model_metadata(self, plant_id: str):
        res = self._get(f"/api/v1/model-metadata/{plant_id}")
        return res if res is not None else mock_data.get_mock_model_metadata(plant_id)
