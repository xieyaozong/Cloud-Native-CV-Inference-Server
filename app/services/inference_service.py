from __future__ import annotations

from threading import Lock
import numpy as np
from app.services.model_loader import get_session
from app.services.postprocessing import summarize_outputs
from app.services.preprocessing import to_nchw


_lock = Lock()
_requests = 0
_failures = 0
_latencies: list[float] = []


def predict_image(image: np.ndarray) -> dict:
    session = get_session()
    if session is None:
        return {
            "model_loaded": False,
            "image_shape": list(image.shape),
            "detections": [],
        }

    input_meta = session.get_inputs()[0]
    tensor = to_nchw(image)
    outputs = session.run(None, {input_meta.name: tensor})
    return {
        "model_loaded": True,
        "input_name": input_meta.name,
        "outputs": summarize_outputs(outputs),
    }


def record_latency(latency_ms: float) -> None:
    global _requests
    with _lock:
        _requests += 1
        _latencies.append(latency_ms)


def record_failure() -> None:
    global _failures
    with _lock:
        _failures += 1


def metrics_snapshot() -> dict:
    with _lock:
        average = sum(_latencies) / len(_latencies) if _latencies else 0.0
        return {
            "requests": _requests,
            "failures": _failures,
            "average_latency_ms": round(average, 3),
        }
