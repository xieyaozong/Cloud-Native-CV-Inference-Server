from __future__ import annotations

from fastapi import APIRouter
from app.schemas import MetricsResponse
from app.services.inference_service import metrics_snapshot


router = APIRouter(tags=["metrics"])


@router.get("/metrics", response_model=MetricsResponse)
def metrics() -> MetricsResponse:
    return MetricsResponse(**metrics_snapshot())
