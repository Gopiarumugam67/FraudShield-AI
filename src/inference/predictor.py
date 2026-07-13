"""
Prediction module for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from app.core.logger import logger


class Predictor:
    """
    Performs fraud prediction using a trained model.
    """

    def __init__(
        self,
        model,
    ):
        self.model = model

    def predict(
        self,
        transaction: pd.DataFrame,
    ) -> dict:

        logger.info(
            "Predicting transaction..."
        )

        # Ensure feature order matches the trained model
        if hasattr(self.model, "feature_names_in_"):
            transaction = transaction.reindex(
                columns=self.model.feature_names_in_
            )

        prediction = self.model.predict(
            transaction
        )[0]

        probability = self.model.predict_proba(
            transaction
        )[0][1]

        logger.info(
            "Prediction completed."
        )

        return {
            "prediction": int(prediction),
            "probability": float(probability),
        }
    
    def predict_batch(
    self,
    transactions: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info(
        "Predicting batch..."
        )

        if hasattr(self.model, "feature_names_in_"):

            transactions = transactions.reindex(
            columns=self.model.feature_names_in_
        )

        predictions = self.model.predict(
        transactions
        )

        probabilities = self.model.predict_proba(
        transactions
        )[:, 1]

        logger.info(
        "Batch prediction completed."
        )

        return pd.DataFrame({

        "Prediction": predictions,

        "Fraud Probability": probabilities,

        })