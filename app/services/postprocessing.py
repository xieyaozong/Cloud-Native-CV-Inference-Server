from __future__ import annotations

from typing import Any
import numpy as np


def summarize_outputs(outputs: list[Any]) -> list[dict]:
    summary = []
    for index, output in enumerate(outputs):
        array = np.asarray(output)
        summary.append(
            {
                "index": index,
                "shape": list(array.shape),
                "dtype": str(array.dtype),
            }
        )
    return summary
