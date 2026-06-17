# Architecture

The service exposes FastAPI routes for health, prediction, and metrics. Uploaded images are decoded with OpenCV, converted to an NCHW float tensor, sent to ONNX Runtime when a model is present, and returned as JSON.
