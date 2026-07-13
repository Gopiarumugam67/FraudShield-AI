"""
Model Persistence Module for FraudShield AI.
"""

from __future__ import annotations

import os
import joblib

from app.core.logger import logger


class ModelSaver:
    """
    Saves trained machine learning models.
    """

    def save(
        self,
        model,
        file_path: str,
    ) -> str:

        logger.info("Saving trained model...")

        # Create folder if it doesn't exist
        os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True,
    )
        joblib.dump(
        model,
        file_path,
    )
        # Save model

        logger.info(
            f"Model saved successfully: {file_path}"
        )

        return file_path