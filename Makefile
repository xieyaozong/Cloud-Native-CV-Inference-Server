.PHONY: install test run docker benchmark

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest -q

run:
	uvicorn app.main:app --reload

docker:
	docker compose up --build

benchmark:
	python scripts/benchmark_latency.py
