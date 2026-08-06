"""Application configuration.

Values are read from environment variables, with sensible local-dev
defaults. In production, override via a real .env file or your
deployment platform's secret manager.
"""
from __future__ import annotations

import os


class Settings:
    # -- Database ------------------------------------------------------
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "sqlite:///./taskflow.db"
    )

    # -- Auth ------------------------------------------------------------
    JWT_SECRET: str = os.getenv("JWT_SECRET", "dev-secret-change-me")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    # Long-lived token, by design, for the pre-Ticket-13 baseline.
    JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", str(60 * 24 * 30)))

    # -- App ---------------------------------------------------------------
    APP_NAME: str = os.getenv("APP_NAME", "TaskFlow API")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"


settings = Settings()
