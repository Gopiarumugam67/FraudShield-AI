"""
Dataset splitting module for FraudShield AI.

Performs stratified train, validation, and test splits.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd
from sklearn.model_selection import train_test_split

from app.core.logger import logger
from src.data.schema import schema


class DatasetSplitter:
    """
    Split datasets into train, validation, and test sets.
    """

    def __init__(
        self,
        dataframe: pd.DataFrame,
        train_size: float = 0.70,
        validation_size: float = 0.15,
        test_size: float = 0.15,
        random_state: int = 42,
    ):

        self.df = dataframe
        self.train_size = train_size
        self.validation_size = validation_size
        self.test_size = test_size
        self.random_state = random_state

    def split_dataset(self) -> Dict[str, pd.DataFrame]:

        logger.info("Starting dataset split...")

        X = self.df.drop(columns=[schema.target_column])

        y = self.df[schema.target_column]

        X_train, X_temp, y_train, y_temp = train_test_split(
            X,
            y,
            test_size=(
                self.validation_size + self.test_size
            ),
            stratify=y,
            random_state=self.random_state,
        )

        validation_ratio = (
            self.validation_size /
            (
                self.validation_size +
                self.test_size
            )
        )

        X_validation, X_test, y_validation, y_test = train_test_split(
            X_temp,
            y_temp,
            test_size=1 - validation_ratio,
            stratify=y_temp,
            random_state=self.random_state,
        )

        logger.info("Dataset splitting completed.")

        return {

            "X_train": X_train,

            "X_validation": X_validation,

            "X_test": X_test,

            "y_train": y_train,

            "y_validation": y_validation,

            "y_test": y_test,

        }