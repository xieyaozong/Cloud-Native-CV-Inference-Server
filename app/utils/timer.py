from __future__ import annotations

from time import perf_counter


def now_ms() -> float:
    return perf_counter() * 1000
