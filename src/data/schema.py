"""
Dataset schema definition for FraudShield AI.

This module defines the expected structure of the credit card fraud dataset.
It acts as a single source of truth for dataset validation.
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DatasetSchema:
    """
    Defines the expected schema of the credit card fraud dataset.
    """

    target_column: str = "Class"

    time_column: str = "Time"

    amount_column: str = "Amount"

    fraud_label: int = 1

    normal_label: int = 0

    @property
    def required_columns(self) -> List[str]:
        """
        Return the required columns for the dataset.
        """

        return (
            [self.time_column]
            + [f"V{i}" for i in range(1, 29)]
            + [self.amount_column]
            + [self.target_column]
        )

    @property
    def expected_column_count(self) -> int:
        """
        Return the expected number of columns.
        """

        return len(self.required_columns)


schema = DatasetSchema()