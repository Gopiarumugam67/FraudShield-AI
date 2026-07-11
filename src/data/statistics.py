"""
Dataset statistics module for FraudShield AI.

Provides summary statistics for datasets.
"""

from __future__ import annotations

import pandas as pd

from app.core.logger import logger
from src.data.schema import schema


class DatasetStatistics:
    """
    Generates statistical summaries for a dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def dataset_shape(self) -> dict:
        """Return dataset shape."""

        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
        }

    def missing_values(self) -> int:
        """Return total missing values."""

        return int(self.df.isnull().sum().sum())

    def duplicate_rows(self) -> int:
        """Return duplicate row count."""

        return int(self.df.duplicated().sum())

    def class_distribution(self) -> dict:
        """Return fraud class distribution."""

        distribution = (
            self.df[schema.target_column]
            .value_counts()
            .to_dict()
        )

        return {
            "normal_transactions": distribution.get(
                schema.normal_label,
                0,
            ),
            "fraud_transactions": distribution.get(
                schema.fraud_label,
                0,
            ),
        }

    def memory_usage(self) -> float:
        """Return memory usage in MB."""

        memory = (
            self.df.memory_usage(deep=True).sum()
            / (1024 ** 2)
        )

        return round(memory, 2)

    def generate_report(self) -> dict:
        """
        Generate complete dataset report.
        """

        logger.info(
            "Generating dataset statistics..."
        )

        report = {
            **self.dataset_shape(),
            "missing_values": self.missing_values(),
            "duplicate_rows": self.duplicate_rows(),
            **self.class_distribution(),
            "memory_usage_mb": self.memory_usage(),
        }

        logger.info(
            "Statistics generated successfully."
        )

        return report