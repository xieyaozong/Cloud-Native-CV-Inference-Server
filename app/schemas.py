from __future__ import annotations

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool


class MetricsResponse(BaseModel):
    requests: int
    failures: int
    average_latency_ms: float


class PredictResponse(BaseModel):
    filename: str
    latency_ms: float
    result: dict
