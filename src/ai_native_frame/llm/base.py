"""LLM client protocol."""

from typing import Protocol


class LLMClient(Protocol):
    """Common interface for all LLM providers."""

    async def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Generate a response from the model."""
