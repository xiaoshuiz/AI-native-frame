import pytest

from ai_native_frame.api import get_workflow
from ai_native_frame.config import get_settings


@pytest.fixture(autouse=True)
def force_mock_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AINF_LLM_PROVIDER", "mock")
    monkeypatch.setenv("AINF_LLM_MODEL", "mock-test-model")
    get_settings.cache_clear()
    get_workflow.cache_clear()
