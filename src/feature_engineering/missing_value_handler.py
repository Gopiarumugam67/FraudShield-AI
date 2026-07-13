"""
Missing value handler for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from app.core.logger import logger
from src.feature_engineering.base_processor import BaseProcessor


class MissingValueHandler(BaseProcessor):
    """
    Handles missing values in the dataset.
    """

    def __init__(self, strategy: str = "drop"):
        self.strategy = strategy

    def process(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Handling missing values...")

        if self.strategy == "drop":
            dataframe = dataframe.dropna()

        elif self.strategy == "mean":

            numeric_columns = dataframe.select_dtypes(
                include=["number"]
            ).columns

            dataframe[numeric_columns] = dataframe[
                numeric_columns
            ].fillna(
                dataframe[numeric_columns].mean()
            )

        elif self.strategy == "median":

            numeric_columns = dataframe.select_dtypes(
                include=["number"]
            ).columns

            dataframe[numeric_columns] = dataframe[
                numeric_columns
            ].fillna(
                dataframe[numeric_columns].median()
            )

        logger.info("Missing value handling completed.")

        return dataframe