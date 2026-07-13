"""
Prediction Pipeline for FraudShield AI.
"""

from __future__ import annotations

import traceback

import pandas as pd

from app.core.logger import logger
from app.config.settings import settings

from src.inference.model_loader import ModelLoader
from src.inference.predictor import Predictor

from src.explainability.shap_explainer import SHAPExplainer
from src.explainability.explanation import ExplanationGenerator


class PredictionPipeline:
    """
    End-to-end prediction pipeline.
    """

    def __init__(self):

        loader = ModelLoader()

        model = loader.load(
            settings.model_path
        )

        self.predictor = Predictor(model)

        self.explainer = SHAPExplainer(model)

        self.generator = ExplanationGenerator()

    def predict(
        self,
        transaction: pd.DataFrame,
    ) -> dict:

        logger.info(
            "Running prediction pipeline..."
        )

        result = self.predictor.predict(
            transaction
        )

        logger.info(
            "Generating SHAP explanation..."
        )

        try:

            shap_values = self.explainer.explain(
                transaction
            )

            print("\n========== SHAP VALUES ==========")
            print(type(shap_values))
            print(shap_values)
            print("=================================\n")

            explanation = self.generator.generate(
                transaction,
                shap_values,
            )

            result["explanation"] = explanation

            logger.info(
                "Explanation generated successfully."
            )

        except Exception:

            logger.error(
                "Failed to generate explanation."
            )

            traceback.print_exc()

            raise

        return result

    def predict_batch(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        predictions = []

        probabilities = []

        for _, row in dataframe.iterrows():

            result = self.predict(
                pd.DataFrame([row])
            )

            predictions.append(
                result["prediction"]
            )

            probabilities.append(
                result["probability"]
            )

        return pd.DataFrame(
            {
                "Prediction": predictions,
                "Fraud Probability": probabilities,
            }
        )