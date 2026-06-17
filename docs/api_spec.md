# API Spec

## GET /health

Returns service status and whether the ONNX model is loaded.

## POST /predict

Accepts multipart image upload under `file`.

## GET /metrics

Returns request count, failure count, and average latency.
