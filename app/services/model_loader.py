from __future__ import annotations

from functools import lru_cache
from logging import getLogger
from typing import Any
from app.config import settings
import onnxruntime as ort


logger = getLogger(__name__)


@lru_cache(maxsize=1)
def get_session() -> Any | None:
    if not settings.model_path.exists():
        return None
    try:
        return ort.InferenceSession(str(settings.model_path), providers=[settings.onnx_provider])
    except Exception as exc:
        logger.warning("Could not load ONNX model at %s: %s", settings.model_path, exc)
        return None


def model_ready() -> bool:
    return get_session() is not None
