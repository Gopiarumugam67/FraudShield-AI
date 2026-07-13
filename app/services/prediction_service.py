"""
Prediction Service for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from app.core.logger import logger
from app.schemas.prediction import PredictionRequest

from src.inference.prediction_pipeline import PredictionPipeline


class PredictionService:
    """
    Service layer for fraud prediction.
    Responsible for converting API requests into
    model predictions.
    """

    def __init__(self):

        logger.info(
            "Initializing Prediction Service..."
        )

        self.pipeline = PredictionPipeline()

    def predict(
        self,
        request: PredictionRequest,
    ) -> dict:
        """
        Predict a single transaction.
        """

        logger.info(
            "Received prediction request."
        )

        try:

            transaction = pd.DataFrame(
                [request.model_dump()]
            )

            result = self.pipeline.predict(
                transaction
            )

            logger.info(
                "Prediction completed successfully."
            )

            return result

        except Exception as error:

            logger.exception(
                f"Prediction failed: {error}"
            )

            raise