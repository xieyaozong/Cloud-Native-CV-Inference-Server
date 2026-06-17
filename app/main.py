from __future__ import annotations

from fastapi import FastAPI
from app.api.routes_health import router as health_router
from app.api.routes_metrics import router as metrics_router
from app.api.routes_predict import router as predict_router
from app.config import settings
from app.services.logging_service import configure_logging


configure_logging()

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(health_router)
app.include_router(predict_router)
app.include_router(metrics_router)
