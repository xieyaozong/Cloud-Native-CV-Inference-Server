from __future__ import annotations

from functools import lru_cache
from typing import Any
import onnxruntime as ort
from app.config import settings


@lru_cache(maxsize=1)
def get_session() -> Any | None:
    if not settings.model_path.exists():
        return None
    return ort.InferenceSession(str(settings.model_path), providers=[settings.onnx_provider])


def model_ready() -> bool:
    return get_session() is not None
