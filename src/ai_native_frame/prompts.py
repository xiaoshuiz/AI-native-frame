"""Prompt loading utilities."""

from pathlib import Path


def _candidate_prompt_roots() -> list[Path]:
    # 1) repo root when running locally, 2) fallback for editable installs.
    return [Path.cwd() / "prompts", Path(__file__).resolve().parents[2] / "prompts"]


def load_prompt(relative_path: str) -> str:
    """Load a markdown prompt from known prompt roots."""

    searched: list[str] = []
    for root in _candidate_prompt_roots():
        prompt_path = root / relative_path
        searched.append(str(prompt_path))
        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8")
    raise FileNotFoundError("Prompt file not found. Tried: " + ", ".join(searched))
