# Cloud-Native-CV-Inference-Server

FastAPI service for packaging a computer-vision ONNX model as a deployable inference API.

The first milestone is a small service that can run locally or in Docker, accept image uploads, return prediction metadata, and expose basic runtime metrics. When no ONNX model is present, the API still validates the image path and returns a deterministic demo response, which keeps the deployment and API flow testable before model selection is final.

## Flow

```text
Client
  -> FastAPI /predict
  -> Preprocessing
  -> ONNX Runtime Inference
  -> Postprocessing
  -> JSON Response + Metrics
```

## MVP

- `/health`
- `/predict`
- `/metrics`
- Docker and Docker Compose
- Local sample-image inference path
- Latency benchmark script

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## Benchmark

Start the API, then run:

```powershell
python scripts/benchmark_latency.py --runs 10
```

The default input is `sample_data/demo_images/dog_on_log_cc0.jpg`. Source and license details are recorded in `sample_data/ASSET_SOURCES.md`.

## Docker

```powershell
docker compose up --build
```

## Model

Place an ONNX model at `models/model.onnx`, or set:

```powershell
$env:MODEL_PATH = "models\your_model.onnx"
```

If no model is present, `/predict` still validates the upload, decodes the image, and returns demo metadata. Invalid or unreadable model files are treated as not loaded so the health endpoint and local API flow stay available during setup.

## Layout

```text
cloud-native-cv-inference-server/
  app/        FastAPI app, routes, services, utilities
  models/     local ONNX model files
  scripts/    model, benchmark, and deployment helpers
  infra/      AWS and Kubernetes examples
  docs/       architecture and deployment notes
  tests/      API and preprocessing checks
```

## Deploy Notes

- Push Docker image to ECR: see `scripts/push_to_ecr.sh`.
- Deploy to ECS: see `scripts/deploy_ecs.md` and `infra/aws/`.
- Deploy to Kubernetes: see `infra/k8s/` and `docs/deployment_kubernetes.md`.
