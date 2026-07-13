"""
Feature scaler for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import StandardScaler

from app.core.logger import logger
from src.feature_engineering.base_processor import BaseProcessor


class Scaler(BaseProcessor):
    """
    Scale numerical features using StandardScaler.
    """

    def __init__(self):
        self.scaler = StandardScaler()

    def process(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Scaling numerical features...")

        scaled_df = dataframe.copy()

        numeric_columns = scaled_df.select_dtypes(
            include=["number"]
        ).columns

        # Never scale the target column
        if "Class" in numeric_columns:
            numeric_columns = numeric_columns.drop("Class")

        scaled_df[numeric_columns] = self.scaler.fit_transform(
            scaled_df[numeric_columns]
        )

        logger.info("Scaling completed.")

        return scaled_df