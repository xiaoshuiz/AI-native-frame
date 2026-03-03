"""Factory for selecting an LLM provider."""

from ai_native_frame.config import Settings
from ai_native_frame.llm.base import LLMClient
from ai_native_frame.llm.mock import MockLLMClient
from ai_native_frame.llm.openai_client import OpenAIClient


def get_llm_client(settings: Settings) -> LLMClient:
    """Instantiate provider based on configuration."""

    provider = settings.llm_provider.strip().lower()
    if provider == "mock":
        return MockLLMClient(model=settings.llm_model)
    if provider == "openai":
        if not settings.openai_api_key:
            raise ValueError("AINF_OPENAI_API_KEY is required when AINF_LLM_PROVIDER=openai.")
        return OpenAIClient(api_key=settings.openai_api_key, model=settings.llm_model)
    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
