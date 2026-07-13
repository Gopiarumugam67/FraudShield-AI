"""
Prediction API routes for FraudShield AI.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)

from app.services.prediction_service import (
    PredictionService,
)

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)

service = PredictionService()


@router.post(
    "",
    response_model=PredictionResponse,
    summary="Predict a single credit card transaction",
    description="Returns fraud prediction and probability.",
)
async def predict(
    request: PredictionRequest,
):
    """
    Predict whether a transaction is fraudulent.
    """

    try:

        result = service.predict(request)

        probability = result["probability"]

        confidence = max(
            probability,
            1 - probability,
        ) * 100

        if probability < 0.30:
            risk = "Low"
        elif probability < 0.70:
            risk = "Medium"
        
        else:
            risk = "High"

        return PredictionResponse(
            prediction=result["prediction"],
            probability=probability,
            confidence=confidence,
            risk_level=risk,
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


@router.get(
    "/info",
    summary="Prediction Endpoint Information",
)
async def prediction_info():
    """
    Returns endpoint information.
    """

    return {
        "endpoint": "/predict",
        "method": "POST",
        "description": "Predict fraud for a single transaction.",
    }