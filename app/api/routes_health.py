from __future__ import annotations

from fastapi import APIRouter
from app.schemas import HealthResponse
from app.services.model_loader import model_ready


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", model_loaded=model_ready())
