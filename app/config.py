from __future__ import annotations

from dataclasses import dataclass
from os import getenv
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    app_name: str = "Cloud Native CV Inference Server"
    version: str = "0.1.0"
    app_env: str = getenv("APP_ENV", "local")
    model_path: Path = Path(getenv("MODEL_PATH", "models/model.onnx"))
    onnx_provider: str = getenv("ONNX_PROVIDER", "CPUExecutionProvider")
    max_image_size: int = int(getenv("MAX_IMAGE_SIZE", "1280"))
    log_level: str = getenv("LOG_LEVEL", "INFO")


settings = Settings()
