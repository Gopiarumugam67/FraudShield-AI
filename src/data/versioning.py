"""
Dataset versioning module for FraudShield AI.

Generates dataset metadata and a unique dataset version.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

import pandas as pd

from app.core.logger import logger


class DatasetVersioning:
    """
    Generates version information for datasets.
    """

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe

    def calculate_hash(self) -> str:
        """
        Generate SHA256 hash of dataset.
        """

        dataset_bytes = self.df.to_csv(index=False).encode()

        return hashlib.sha256(dataset_bytes).hexdigest()

    def dataset_metadata(self) -> dict:

        return {

            "rows": self.df.shape[0],

            "columns": self.df.shape[1],

            "generated_at": datetime.now().isoformat(),

        }

    def save_metadata(
        self,
        metadata: dict,
        output_dir: str = "models/artifacts",
    ) -> None:

        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = (
            Path(output_dir)
            / "dataset_version.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        logger.info(
            "Dataset metadata saved."
        )

    def generate_version(self) -> dict:

        logger.info(
            "Generating dataset version..."
        )

        metadata = self.dataset_metadata()

        metadata["dataset_hash"] = (
            self.calculate_hash()
        )

        self.save_metadata(metadata)

        logger.info(
            "Dataset version generated."
        )

        return metadata