from __future__ import annotations

from app.services.preprocessing import decode_image, to_nchw
import cv2
import numpy as np
import pytest


def test_decode_image() -> None:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    ok, encoded = cv2.imencode(".jpg", image)
    assert ok
    decoded = decode_image(encoded.tobytes())
    assert decoded.shape[:2] == (8, 8)


def test_decode_image_rejects_empty_upload() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        decode_image(b"")


def test_to_nchw() -> None:
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    tensor = to_nchw(image)
    assert tensor.shape == (1, 3, 8, 8)
    assert tensor.dtype == np.float32
