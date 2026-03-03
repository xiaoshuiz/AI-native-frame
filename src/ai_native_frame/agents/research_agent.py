"""A minimal research-style agent."""

from ai_native_frame.agents.base import AgentInput, AgentOutput
from ai_native_frame.llm.base import LLMClient


class ResearchAgent:
    """Single-step agent that prepares context and prompts an LLM."""

    def __init__(
        self,
        llm: LLMClient,
        model_name: str,
        system_prompt: str,
        task_prompt_template: str,
    ) -> None:
        self.llm = llm
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.task_prompt_template = task_prompt_template

    async def run(self, agent_input: AgentInput) -> AgentOutput:
        context_text = "\n".join(f"- {item}" for item in agent_input.context)
        if not context_text:
            context_text = "- (no extra context provided)"
        user_prompt = self.task_prompt_template.format(
            query=agent_input.query,
            context=context_text,
        )
        answer = await self.llm.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
        )
        return AgentOutput(answer=answer, model=self.model_name)
