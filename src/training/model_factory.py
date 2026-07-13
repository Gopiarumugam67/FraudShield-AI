"""
Model Factory for FraudShield AI.
"""

from __future__ import annotations

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from app.core.logger import logger


class ModelFactory:
    """
    Factory class for creating ML models.
    """

    MODELS = {

        "random_forest": RandomForestClassifier,

        "logistic_regression": LogisticRegression,

        "decision_tree": DecisionTreeClassifier,

    }

    def get_model(
        self,
        model_name: str,
        **kwargs,
    ):

        logger.info(
            f"Loading model: {model_name}"
        )

        if model_name not in self.MODELS:

            raise ValueError(
                f"Unsupported model: {model_name}"
            )

        return self.MODELS[model_name](**kwargs)