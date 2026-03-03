"""OpenAI provider via HTTP API."""

from typing import Any

import httpx


class OpenAIClient:
    """Minimal OpenAI Chat Completions client."""

    def __init__(self, api_key: str, model: str, timeout: float = 45.0) -> None:
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    async def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload: dict[str, object] = {
            "model": self.model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()

        data: Any = response.json()
        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ValueError("OpenAI response schema is unexpected.") from exc
        if not isinstance(content, str):
            raise ValueError("OpenAI response content is not a string.")
        return content.strip()
