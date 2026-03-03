import pytest

from ai_native_frame.config import get_settings
from ai_native_frame.workflows import ResearchTask, ResearchWorkflow


@pytest.mark.asyncio
async def test_research_workflow_smoke() -> None:
    workflow = ResearchWorkflow.from_settings(get_settings())
    result = await workflow.run(
        ResearchTask(
            query="Give a short deployment checklist for AI agent services.",
            context=["Use canary release and offline eval gate"],
        )
    )
    assert result.provider == "mock"
    assert result.model == "mock-test-model"
    assert len(result.answer) > 20
