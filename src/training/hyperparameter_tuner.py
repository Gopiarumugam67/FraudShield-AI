"""
Hyperparameter tuning module for FraudShield AI.
"""

from __future__ import annotations

import pandas as pd

from sklearn.model_selection import GridSearchCV

from app.core.logger import logger


class HyperparameterTuner:
    """
    Performs hyperparameter optimization using GridSearchCV.
    """

    def __init__(
        self,
        model,
        parameter_grid: dict,
        cv: int = 3,
        scoring: str = "recall",
    ):
        self.model = model
        self.parameter_grid = parameter_grid
        self.cv = cv
        self.scoring = scoring

    def optimize(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
    ) -> dict:

        logger.info("Starting hyperparameter optimization...")

        search = GridSearchCV(
            estimator=self.model,
            param_grid=self.parameter_grid,
            cv=self.cv,
            scoring=self.scoring,
            n_jobs=-1,
            verbose=1,
        )

        search.fit(
            X_train,
            y_train,
        )

        logger.info("Hyperparameter optimization completed.")
        logger.info(f"Best Score      : {search.best_score_:.4f}")
        logger.info(f"Best Parameters : {search.best_params_}")

        return {
            "best_model": search.best_estimator_,
            "best_parameters": search.best_params_,
            "best_score": search.best_score_,
            "cv_results": search.cv_results_,
        }