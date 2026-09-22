import random
from datetime import datetime, timedelta

def get_mock_plants():
    return [{"plant_id": "PLANT_001", "name": "Copper Concentrator Demo", "location": "Demo Site", "capacity": 1200}]

def get_mock_overview(plant_id):
    return {
        "throughput": 1150 + random.uniform(-20, 20),
        "recovery": 87.3 + random.uniform(-1, 1),
        "concentrate_grade": 27.8 + random.uniform(-0.5, 0.5),
        "tail_grade": 0.09 + random.uniform(-0.01, 0.01),
        "energy_intensity": 18.5 + random.uniform(-0.5, 0.5),
        "water_intensity": 0.85 + random.uniform(-0.05, 0.05),
        "availability": 94.2
    }

def get_mock_live_state(plant_id):
    return {
        "plant_id": plant_id,
        "timestamp": datetime.utcnow().isoformat(),
        "units": [
            {"unit_id": "SAG_01", "type": "SAG", "status": "normal", "throughput": 1150, "power": 12.5},
            {"unit_id": "BM_01", "type": "BM", "status": "caution", "power": 14.2},
            {"unit_id": "CYC_01", "type": "CYC", "status": "normal", "pressure": 110, "overflow_p80": 150},
            {"unit_id": "FL_RO_01", "type": "FL_RO", "status": "normal", "recovery": 85},
            {"unit_id": "THK_01", "type": "THK", "status": "alarm", "underflow_density": 55},
        ]
    }

def get_mock_timeseries(plant_id, params=None):
    now = datetime.utcnow()
    data = []
    for i in range(72):
        ts = now - timedelta(hours=71 - i)
        data.append({
            "timestamp": ts.isoformat(),
            "throughput": 1150 + random.gauss(0, 15),
            "recovery": 87.3 + random.gauss(0, 0.5),
            "concentrate_grade": 27.8 + random.gauss(0, 0.2),
            "tail_grade": 0.09 + random.gauss(0, 0.005)
        })
    return {"plant_id": plant_id, "data": data}

def get_mock_unit(plant_id, unit_id):
    return {
        "unit_id": unit_id,
        "type": "SAG",
        "current_state": {"speed": 72.5, "feed_rate": 1150, "power": 12.5},
        "recommended_mvs": {"speed": 73.0, "feed_rate": 1180},
        "health_score": 92.5
    }

def get_mock_simulation(payload):
    return {
        "base_kpis": {"throughput": 1150, "recovery": 87.3},
        "simulated_kpis": {"throughput": payload.get("feed_rate", 1180), "recovery": 88.1},
        "timeseries": []
    }

def get_mock_optimization(payload):
    return {
        "recommendations": [
            {"variable": "SAG Speed", "current": 72.5, "recommended": 73.5, "impact": "+15 t/h", "confidence": 92},
            {"variable": "Collector Dosage", "current": 15.0, "recommended": 16.5, "impact": "+0.5% Rec", "confidence": 85},
            {"variable": "Froth Depth", "current": 300, "recommended": 250, "impact": "+0.2% Grade", "confidence": 78}
        ],
        "expected_gain": 250000
    }

def get_mock_advisory(plant_id):
    return {
        "plant_id": plant_id,
        "advisories": [
            {"variable": "SAG Speed", "current": 72.5, "recommended": 73.5, "impact": "High", "confidence": 92, "status": "critical"},
            {"variable": "Froth Depth", "current": 300, "recommended": 280, "impact": "Medium", "confidence": 80, "status": "caution"}
        ]
    }

def get_mock_diagnostics(asset_id):
    return {
        "asset_id": asset_id,
        "health_score": 85,
        "anomalies": [
            {"type": "Vibration", "severity": "high", "timestamp": datetime.utcnow().isoformat()}
        ],
        "rul_days": 120
    }

def get_mock_data_quality(plant_id):
    return {
        "plant_id": plant_id,
        "tag_stats": [
            {"tag": "FI-101", "missing_pct": 0.5, "quality": "good", "outliers": 2},
            {"tag": "AI-205", "missing_pct": 5.2, "quality": "poor", "outliers": 15}
        ],
        "freshness_score": 98.5
    }

def get_mock_model_metadata(plant_id):
    return {
        "plant_id": plant_id,
        "models": [
            {"name": "Recovery Prediction", "version": "v1.2", "accuracy": 94.5}
        ]
    }
