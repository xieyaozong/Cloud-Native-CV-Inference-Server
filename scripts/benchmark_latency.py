from __future__ import annotations

from pathlib import Path
from time import perf_counter
import argparse
import statistics
import httpx


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8000/predict")
    parser.add_argument("--image", type=Path, default=Path("sample_data/demo_images/sample.jpg"))
    parser.add_argument("--runs", type=int, default=10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    latencies = []
    for _ in range(args.runs):
        start = perf_counter()
        with args.image.open("rb") as handle:
            response = httpx.post(args.url, files={"file": (args.image.name, handle, "image/jpeg")}, timeout=30)
        response.raise_for_status()
        latencies.append((perf_counter() - start) * 1000)
    print(f"runs={args.runs} avg_ms={statistics.mean(latencies):.2f} p95_ms={sorted(latencies)[int(args.runs * 0.95) - 1]:.2f}")


if __name__ == "__main__":
    main()
