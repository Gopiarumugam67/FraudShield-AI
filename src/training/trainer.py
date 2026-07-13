"""
Model trainer for FraudShield AI.
"""

from __future__ import annotations

import time
import pandas as pd

from app.core.logger import logger


class ModelTrainer:
    """
    Trains machine learning models.
    """

    def __init__(self, model):
        self.model = model

    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
    ):

        logger.info(
            f"Training {self.model.__class__.__name__}..."
        )

        start_time = time.time()

        self.model.fit(
            X_train,
            y_train,
        )

        training_time = round(
            time.time() - start_time,
            2,
        )

        logger.info(
            f"Training completed in {training_time} seconds."
        )

        return {
            "model": self.model,
            "training_time": training_time,
        }