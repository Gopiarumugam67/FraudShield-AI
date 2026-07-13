"""
Model Evaluation Module for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from app.core.logger import logger


class ModelEvaluator:
    """
    Evaluates trained machine learning models.
    """

    def __init__(self, model):
        """
        Initialize the evaluator with a trained model.
        """
        self.model = model

    def evaluate(
        self,
        X_test: pd.DataFrame,
        y_test: pd.Series,
    ) -> dict:
        """
        Evaluate the trained model on the test dataset.
        """

        logger.info("Starting model evaluation...")

        # Generate predictions
        predictions = self.model.predict(X_test)

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        # Generate confusion matrix
        matrix = confusion_matrix(y_test, predictions)

        # Generate classification report
        report = classification_report(y_test, predictions)

        logger.info("Model evaluation completed.")

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "confusion_matrix": matrix,
            "classification_report": report,
        }