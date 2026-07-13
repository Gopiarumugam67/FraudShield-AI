"""
Pydantic schemas for FraudShield AI prediction.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """
    Request schema for fraud prediction.
    """

    Time: float = Field(..., description="Transaction time")

    V1: float = Field(...)
    V2: float = Field(...)
    V3: float = Field(...)
    V4: float = Field(...)
    V5: float = Field(...)
    V6: float = Field(...)
    V7: float = Field(...)
    V8: float = Field(...)
    V9: float = Field(...)
    V10: float = Field(...)
    V11: float = Field(...)
    V12: float = Field(...)
    V13: float = Field(...)
    V14: float = Field(...)
    V15: float = Field(...)
    V16: float = Field(...)
    V17: float = Field(...)
    V18: float = Field(...)
    V19: float = Field(...)
    V20: float = Field(...)
    V21: float = Field(...)
    V22: float = Field(...)
    V23: float = Field(...)
    V24: float = Field(...)
    V25: float = Field(...)
    V26: float = Field(...)
    V27: float = Field(...)
    V28: float = Field(...)

    Amount: float = Field(
        ...,
        description="Transaction amount",
        ge=0,
    )


class PredictionResponse(BaseModel):
    """
    Response schema for fraud prediction.
    """

    prediction: int = Field(
        ...,
        description="0 = Legitimate, 1 = Fraud",
    )

    probability: float = Field(
        ...,
        description="Fraud probability",
        ge=0,
        le=1,
    )

    risk_level: str = Field(
        ...,
        description="Low / Medium / High",
    )

    confidence: float = Field(
        ...,
        description="Model confidence (%)",
        ge=0,
        le=100,
    )