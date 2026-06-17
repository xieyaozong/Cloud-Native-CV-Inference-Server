from __future__ import annotations

from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas import PredictResponse
from app.services.inference_service import predict_image, record_failure, record_latency
from app.services.preprocessing import decode_image
from app.utils.response_builder import prediction_response
from app.utils.timer import now_ms


router = APIRouter(tags=["predict"])


@router.post("/predict", response_model=PredictResponse)
async def predict(file: UploadFile = File(...)) -> PredictResponse:
    start = now_ms()
    data = await file.read()
    try:
        image = decode_image(data)
        result = predict_image(image)
    except ValueError as exc:
        record_failure()
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    latency_ms = now_ms() - start
    record_latency(latency_ms)
    return prediction_response(file.filename or "upload", latency_ms, result)
