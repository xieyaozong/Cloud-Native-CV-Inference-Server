# Cloud Native CV Inference Server

FastAPI service skeleton for deploying computer-vision ONNX inference with Docker, AWS, and Kubernetes.

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

## Docker

```powershell
docker compose up --build
```

## Model

Place an ONNX model at `models/model.onnx`, or set:

```powershell
$env:MODEL_PATH = "models\your_model.onnx"
```

If no model is present, `/predict` still validates upload, decodes the image, and returns demo metadata.

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
