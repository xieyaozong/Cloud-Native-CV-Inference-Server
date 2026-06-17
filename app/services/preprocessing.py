from __future__ import annotations

import cv2
import numpy as np
from app.config import settings


def decode_image(data: bytes) -> np.ndarray:
    array = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(array, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Upload must be a readable image file.")
    return image


def to_nchw(image: np.ndarray) -> np.ndarray:
    size = min(settings.max_image_size, max(image.shape[:2]))
    resized = cv2.resize(image, (size, size), interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    tensor = rgb.transpose(2, 0, 1).astype(np.float32) / 255.0
    return np.expand_dims(tensor, axis=0)
