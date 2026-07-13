"""
Base processor interface for FraudShield AI.

All preprocessing components inherit from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseProcessor(ABC):
    """
    Abstract base class for all preprocessing processors.
    """

    @abstractmethod
    def process(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Process the dataframe.
        """

        pass