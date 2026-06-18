from __future__ import annotations

from math import ceil
from pathlib import Path
from time import perf_counter
import argparse
import statistics
import httpx


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8000/predict")
    parser.add_argument("--image", type=Path, default=Path("sample_data/demo_images/dog_on_log_cc0.jpg"))
    parser.add_argument("--runs", type=int, default=10)
    args = parser.parse_args()
    if args.runs < 1:
        parser.error("--runs must be at least 1")
    return args


def validate_image_path(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(
            f"Image not found: {path}. See sample_data/ASSET_SOURCES.md for the bundled demo image."
        )


def p95(latencies: list[float]) -> float:
    index = max(0, ceil(len(latencies) * 0.95) - 1)
    return sorted(latencies)[index]


def main() -> None:
    args = parse_args()
    validate_image_path(args.image)
    latencies = []
    for _ in range(args.runs):
        start = perf_counter()
        with args.image.open("rb") as handle:
            response = httpx.post(args.url, files={"file": (args.image.name, handle, "image/jpeg")}, timeout=30)
        response.raise_for_status()
        latencies.append((perf_counter() - start) * 1000)
    print(f"runs={args.runs} avg_ms={statistics.mean(latencies):.2f} p95_ms={p95(latencies):.2f}")


if __name__ == "__main__":
    main()
