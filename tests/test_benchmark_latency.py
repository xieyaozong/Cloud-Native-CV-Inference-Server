from __future__ import annotations

from pathlib import Path
from scripts.benchmark_latency import p95, validate_image_path
import pytest

def test_p95() -> None:
    assert p95([1, 2, 3, 4, 5]) == 5


def test_validate_image_path_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="Image not found"):
        validate_image_path(tmp_path / "missing.jpg")
