from __future__ import annotations

import cv2
import numpy as np
from fastapi.testclient import TestClient
from app.main import app


def test_predict_api_without_model() -> None:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    ok, encoded = cv2.imencode(".jpg", image)
    assert ok
    response = TestClient(app).post(
        "/predict",
        files={"file": ("sample.jpg", encoded.tobytes(), "image/jpeg")},
    )
    assert response.status_code == 200
    assert response.json()["result"]["model_loaded"] is False
