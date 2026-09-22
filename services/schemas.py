from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class PlantInfo(BaseModel):
    plant_id: str
    name: str
    location: Optional[str] = None
    capacity: Optional[float] = None

class KPIOverview(BaseModel):
    throughput: Optional[float] = None
    recovery: Optional[float] = None
    concentrate_grade: Optional[float] = None
    tail_grade: Optional[float] = None
    energy_intensity: Optional[float] = None
    water_intensity: Optional[float] = None
    availability: Optional[float] = None

class ProcessState(BaseModel):
    plant_id: str
    timestamp: str
    units: List[Dict[str, Any]]

class TimeseriesData(BaseModel):
    plant_id: str
    data: List[Dict[str, Any]]

class UnitDetail(BaseModel):
    unit_id: str
    type: str
    current_state: Dict[str, float]
    recommended_mvs: Dict[str, float]
    health_score: Optional[float] = None

class SimulationResult(BaseModel):
    base_kpis: Dict[str, float]
    simulated_kpis: Dict[str, float]
    timeseries: List[Dict[str, Any]]

class OptimizationResult(BaseModel):
    recommendations: List[Dict[str, Any]]
    expected_gain: Optional[float] = None

class AdvisoryResponse(BaseModel):
    plant_id: str
    advisories: List[Dict[str, Any]]

class DiagnosticsData(BaseModel):
    asset_id: str
    health_score: float
    anomalies: List[Dict[str, Any]]
    rul_days: Optional[float] = None

class DataQualityReport(BaseModel):
    plant_id: str
    tag_stats: List[Dict[str, Any]]
    freshness_score: float

class ModelMetadata(BaseModel):
    plant_id: str
    models: List[Dict[str, Any]]
