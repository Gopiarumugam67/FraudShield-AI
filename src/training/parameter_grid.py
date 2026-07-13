"""
Hyperparameter grids for FraudShield AI.
"""

from __future__ import annotations


RANDOM_FOREST_GRID = {
    "n_estimators": [100],
    "max_depth": [10, None],
}


LOGISTIC_REGRESSION_GRID = {
    "C": [0.01, 0.1, 1, 10],
    "solver": ["lbfgs", "liblinear"],
}


PARAMETER_GRIDS = {
    "random_forest": RANDOM_FOREST_GRID,
    "logistic_regression": LOGISTIC_REGRESSION_GRID,
}