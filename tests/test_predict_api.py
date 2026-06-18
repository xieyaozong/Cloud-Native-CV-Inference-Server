from __future__ import annotations

from app.main import app
from fastapi.testclient import TestClient
import cv2
import numpy as np


def image_bytes() -> bytes:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    ok, encoded = cv2.imencode(".jpg", image)
    assert ok
    return encoded.tobytes()


def test_predict_api_without_model() -> None:
    response = TestClient(app).post(
        "/predict",
        files={"file": ("sample.jpg", image_bytes(), "image/jpeg")},
    )
    assert response.status_code == 200
    assert response.json()["result"]["model_loaded"] is False


def test_predict_api_rejects_non_image() -> None:
    response = TestClient(app).post(
        "/predict",
        files={"file": ("sample.txt", b"not an image", "text/plain")},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Upload must be a readable image file."


def test_metrics_after_prediction() -> None:
    client = TestClient(app)
    before = client.get("/metrics").json()
    response = client.post(
        "/predict",
        files={"file": ("sample.jpg", image_bytes(), "image/jpeg")},
    )
    after = client.get("/metrics").json()
    assert response.status_code == 200
    assert after["requests"] == before["requests"] + 1
