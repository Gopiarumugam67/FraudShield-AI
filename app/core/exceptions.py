"""
Custom exceptions for FraudShield AI.

These exceptions provide meaningful error messages that are specific
to the FraudShield AI application instead of relying only on Python's
built-in exceptions.
"""


class FraudShieldError(Exception):
    """
    Base exception for the entire FraudShield AI application.

    All custom exceptions should inherit from this class.
    """

    pass


# ======================================================
# Dataset Exceptions
# ======================================================

class DatasetError(FraudShieldError):
    """Base class for dataset-related exceptions."""

    pass


class DatasetNotFoundError(DatasetError):
    """Raised when the dataset file cannot be found."""

    pass


class DatasetValidationError(DatasetError):
    """Raised when dataset validation fails."""

    pass


class MissingTargetColumnError(DatasetValidationError):
    """Raised when the target column is missing."""

    pass


# ======================================================
# Model Exceptions
# ======================================================

class ModelError(FraudShieldError):
    """Base class for model-related exceptions."""

    pass


class ModelNotFoundError(ModelError):
    """Raised when a trained model cannot be found."""

    pass


class ModelTrainingError(ModelError):
    """Raised when model training fails."""

    pass


# ======================================================
# Prediction Exceptions
# ======================================================

class PredictionError(FraudShieldError):
    """Raised when prediction fails."""

    pass