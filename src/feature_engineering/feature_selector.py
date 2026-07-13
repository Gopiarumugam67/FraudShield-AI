"""
Feature selector for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd
from sklearn.feature_selection import VarianceThreshold

from app.core.logger import logger
from src.feature_engineering.base_processor import BaseProcessor


class FeatureSelector(BaseProcessor):
    """
    Select informative features by removing
    low-variance features.
    """

    def __init__(self, threshold: float = 0.0):
        self.selector = VarianceThreshold(threshold)

    def process(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Selecting important features...")

        df = dataframe.copy()

        # Separate features and target
        X = df.drop(columns=["Class"])
        y = df["Class"]

        # Fit selector
        X_selected = self.selector.fit_transform(X)

        selected_columns = X.columns[
            self.selector.get_support()
        ]

        processed_df = pd.DataFrame(
            X_selected,
            columns=selected_columns,
            index=df.index,
        )

        # Add target back
        processed_df["Class"] = y

        logger.info("Feature selection completed.")

        return processed_df