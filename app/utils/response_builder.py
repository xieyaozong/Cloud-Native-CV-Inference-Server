from __future__ import annotations

from app.schemas import PredictResponse


def prediction_response(filename: str, latency_ms: float, result: dict) -> PredictResponse:
    return PredictResponse(filename=filename, latency_ms=round(latency_ms, 3), result=result)
