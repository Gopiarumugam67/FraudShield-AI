"""
Model Loader for FraudShield AI.
"""

from __future__ import annotations
from xml.parsers.expat import model

import joblib

from app.core.logger import logger


class ModelLoader:
    """
    Loads trained machine learning models.
    """

    def load(
        self,
        file_path: str,
    ):

        logger.info(
            f"Loading model from {file_path}"
        )

        model = joblib.load(file_path)

        print("\nMODEL FEATURES:")
        print(model.feature_names_in_)

        logger.info("Model loaded successfully.")

        return model