"""
Data loading module for FraudShield AI.

Responsible for reading datasets and validating them before returning
a pandas DataFrame.
"""

from pathlib import Path

import pandas as pd

from app.config.settings import settings
from app.core.exceptions import DatasetNotFoundError
from app.core.logger import logger
from src.data.validator import DataValidator


class DataLoader:
    """
    Handles loading datasets from disk.
    """

    def __init__(self):

        self.data_directory = Path(settings.raw_data_dir)

    def load_dataset(
        self,
        filename: str = "creditcard.csv",
    ) -> pd.DataFrame:
        """
        Load and validate a dataset.

        Parameters
        ----------
        filename : str
            Dataset filename.

        Returns
        -------
        pd.DataFrame
        """

        dataset_path = self.data_directory / filename

        logger.info(
            "Loading dataset from %s",
            dataset_path,
        )

        if not dataset_path.exists():
            raise DatasetNotFoundError(
                f"Dataset not found: {dataset_path}"
            )

        try:

            df = pd.read_csv(dataset_path)

        except FileNotFoundError as e:

            raise DatasetNotFoundError(
                f"Dataset not found: {dataset_path}"
            ) from e

        validator = DataValidator(df)

        validator.validate_dataset()

        logger.info(
            "Dataset loaded successfully."
        )

        return df