"""Centralized runtime configuration."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="AINF_",
        extra="ignore",
    )

    app_name: str = Field(default="AI Native Frame Demo")
    environment: str = Field(default="dev")
    log_level: str = Field(default="INFO")
    llm_provider: str = Field(default="mock")
    llm_model: str = Field(default="gpt-4.1-mini")
    openai_api_key: str | None = Field(default=None)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Use memoization to avoid repeatedly parsing env vars."""

    return Settings()
