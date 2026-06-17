from __future__ import annotations

import cv2
import numpy as np
from app.services.preprocessing import decode_image


def test_decode_image() -> None:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    ok, encoded = cv2.imencode(".jpg", image)
    assert ok
    decoded = decode_image(encoded.tobytes())
    assert decoded.shape[:2] == (8, 8)
