"""Shared agent data models."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class AgentInput:
    """Input payload for a single agent run."""

    query: str
    context: list[str] = field(default_factory=list)


@dataclass(slots=True)
class AgentOutput:
    """Output payload from an agent."""

    answer: str
    model: str
