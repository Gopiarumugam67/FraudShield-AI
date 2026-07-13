"""
Main entry point for FraudShield AI API.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.config.settings import settings
from app.routers.prediction import router as prediction_router

app = FastAPI(
    title=settings.app_name,
    description="Enterprise Credit Card Fraud Detection API",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Register Routers
app.include_router(
    prediction_router,
    tags=["Prediction"],
)


@app.get(
    "/",
    tags=["Root"],
)
async def root():
    """
    Root endpoint.
    """

    return JSONResponse(
        content={
            "application": settings.app_name,
            "version": settings.app_version,
            "status": "Running",
            "docs": "/docs",
        }
    )


@app.get(
    "/health",
    tags=["Health"],
)
async def health_check():
    """
    Health check endpoint.
    """

    return JSONResponse(
        content={
            "status": "healthy",
            "service": settings.app_name,
        }
    )


@app.get(
    "/model",
    tags=["Model"],
)
async def model_information():
    """
    Model information.
    """

    return JSONResponse(
        content={
            "model": "Random Forest",
            "version": settings.model_version,
            "path": settings.model_path,
        }
    )