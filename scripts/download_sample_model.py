from __future__ import annotations

from pathlib import Path


def main() -> None:
    target = Path("models/model.onnx")
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Place or download a sample ONNX model at {target}")


if __name__ == "__main__":
    main()
