"""Research workflow implementation."""

from dataclasses import dataclass, field

from ai_native_frame.agents import AgentInput, ResearchAgent
from ai_native_frame.config import Settings
from ai_native_frame.llm import get_llm_client
from ai_native_frame.prompts import load_prompt


@dataclass(slots=True)
class ResearchTask:
    """Workflow input."""

    query: str
    context: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ResearchResult:
    """Workflow output."""

    answer: str
    model: str
    provider: str


class ResearchWorkflow:
    """Coordinates prompt loading, agent invocation and result shaping."""

    def __init__(self, agent: ResearchAgent, provider: str) -> None:
        self.agent = agent
        self.provider = provider

    @classmethod
    def from_settings(cls, settings: Settings) -> "ResearchWorkflow":
        system_prompt = load_prompt("system/research.md")
        task_prompt = load_prompt("tasks/research_task.md")
        llm = get_llm_client(settings)
        agent = ResearchAgent(
            llm=llm,
            model_name=settings.llm_model,
            system_prompt=system_prompt,
            task_prompt_template=task_prompt,
        )
        return cls(agent=agent, provider=settings.llm_provider)

    async def run(self, task: ResearchTask) -> ResearchResult:
        output = await self.agent.run(AgentInput(query=task.query, context=task.context))
        return ResearchResult(
            answer=output.answer,
            model=output.model,
            provider=self.provider,
        )
