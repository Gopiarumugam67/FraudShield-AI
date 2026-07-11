"""
Data validation module for FraudShield AI.

This module validates datasets before they enter the ML pipeline.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from app.core.exceptions import (
    DatasetValidationError,
    MissingTargetColumnError,
)
from app.core.logger import logger
from src.data.schema import schema


class DataValidator:
    """
    Validates a dataset against the expected schema.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    # -------------------------------------------------
    # Main Validation Method
    # -------------------------------------------------

    def validate_dataset(self) -> bool:
        """
        Run all validation checks.

        Returns
        -------
        bool
            True if validation succeeds.

        Raises
        ------
        DatasetValidationError
        """

        logger.info("Starting dataset validation...")

        self.validate_dataset_not_empty()
        self.validate_columns()
        self.validate_missing_values()
        self.validate_duplicates()
        self.validate_target_column()
        self.validate_class_distribution()

        logger.info("Dataset validation completed successfully.")

        return True

    # -------------------------------------------------
    # Individual Validations
    # -------------------------------------------------

    def validate_dataset_not_empty(self) -> None:
        """Ensure dataset is not empty."""

        if self.df.empty:
            raise DatasetValidationError(
                "Dataset is empty."
            )

    def validate_columns(self) -> None:
        """Validate required columns."""

        missing_columns = [
            column
            for column in schema.required_columns
            if column not in self.df.columns
        ]

        if missing_columns:
            raise DatasetValidationError(
                f"Missing columns: {missing_columns}"
            )

    def validate_missing_values(self) -> None:
        """Validate missing values."""

        missing = self.df.isnull().sum().sum()

        if missing > 0:
            raise DatasetValidationError(
                f"Dataset contains {missing} missing values."
            )

    def validate_duplicates(self) -> None:
        """Validate duplicate rows."""

        duplicates = self.df.duplicated().sum()

        if duplicates > 0:
            logger.warning(
                "Dataset contains %d duplicate rows.",
                duplicates,
            )

    def validate_target_column(self) -> None:
        """Validate target column."""

        if schema.target_column not in self.df.columns:
            raise MissingTargetColumnError(
                f"Target column '{schema.target_column}' not found."
            )

        unique_values = set(self.df[schema.target_column].unique())

        valid_values = {
            schema.normal_label,
            schema.fraud_label,
        }

        if not unique_values.issubset(valid_values):
            raise DatasetValidationError(
                "Target column contains invalid values."
            )

    def validate_class_distribution(self) -> None:
        """Check fraud class distribution."""

        counts = self.df[schema.target_column].value_counts()

        logger.info(
            "Class Distribution:\n%s",
            counts,
        )

        if len(counts) < 2:
            raise DatasetValidationError(
                "Dataset contains only one class."
            )