"""Mock LLM provider for local development and tests."""


class MockLLMClient:
    """Deterministic mock provider with no external dependencies."""

    def __init__(self, model: str) -> None:
        self.model = model

    async def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        compact = " ".join(user_prompt.split())
        preview = compact[:220]
        return f"[MOCK/{self.model}] system={len(system_prompt)} chars; answer={preview}"
