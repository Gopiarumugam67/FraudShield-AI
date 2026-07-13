"""
Application configuration.

Loads configuration from environment variables using Pydantic Settings.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # =====================================
    # Application
    # =====================================

    app_name: str = "FraudShield AI"
    app_version: str = "1.0.0"

    environment: str = "development"
    debug: bool = True

    # =====================================
    # API
    # =====================================

    api_host: str = "127.0.0.1"
    api_port: int = 8000

    # =====================================
    # Paths
    # =====================================

    raw_data_dir: str = "data/raw"
    processed_data_dir: str = "data/processed"
    sample_data_dir: str = "data/sample"

    model_dir: str = "models"
    model_path: str = "models/artifacts/random_forest.pkl"

    log_dir: str = "logs"

    # =====================================
    # Model
    # =====================================

    model_version: str = "v1.0.0"

    random_state: int = 42

    # =====================================
    # Database
    # =====================================

    database_url: str = "sqlite:///fraudshield.db"

    # =====================================
    # Logging
    # =====================================

    log_level: str = "INFO"

    # =====================================
    # MLflow
    # =====================================

    mlflow_tracking_uri: str = "mlruns"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,

        # Allow additional variables in .env
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()


settings = get_settings()