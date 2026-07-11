"""
Application configuration.

Loads configuration from environment variables using Pydantic Settings.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "FraudShield AI"
    app_version: str = "1.0.0"

    environment: str = "development"
    debug: bool = True

    api_host: str = "127.0.0.1"
    api_port: int = 8000

    raw_data_dir: str = "data/raw"
    processed_data_dir: str = "data/processed"
    sample_data_dir: str = "data/sample"
    model_dir: str = "models"
    log_dir: str = "logs"

    database_url: str = "sqlite:///fraudshield.db"

    log_level: str = "INFO"

    mlflow_tracking_uri: str = "mlruns"

    random_state: int = 42

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()


settings = get_settings()