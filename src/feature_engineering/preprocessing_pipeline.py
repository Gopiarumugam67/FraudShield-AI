"""
Preprocessing pipeline for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from app.core.logger import logger

from src.feature_engineering.missing_value_handler import MissingValueHandler
from src.feature_engineering.scaler import Scaler
from src.feature_engineering.feature_selector import FeatureSelector

class PreprocessingPipeline:
    """
    Executes the complete preprocessing workflow.
    """

    def __init__(self):

        self.processors = [

            MissingValueHandler(),

            Scaler(),

            FeatureSelector(),

        ]

    def process(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info(
            "Starting preprocessing pipeline..."
        )

        processed_df = dataframe.copy()

        for processor in self.processors:

            processed_df = processor.process(
                processed_df
            )

        logger.info(
            "Preprocessing pipeline completed."
        )

        return processed_df