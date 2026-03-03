"""FastAPI entrypoint for the AI-native frame demo."""

from functools import lru_cache

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ai_native_frame.config import Settings, get_settings
from ai_native_frame.workflows import ResearchTask, ResearchWorkflow


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


class ResearchRequest(BaseModel):
    query: str = Field(min_length=3, description="Research query")
    context: list[str] = Field(default_factory=list, description="Optional context snippets")


class ResearchResponse(BaseModel):
    answer: str
    model: str
    provider: str


@lru_cache(maxsize=1)
def get_workflow() -> ResearchWorkflow:
    settings = get_settings()
    return ResearchWorkflow.from_settings(settings)


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="AI-native frame demo API",
    )

    @app.get("/health", response_model=HealthResponse)
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            app_name=settings.app_name,
            environment=settings.environment,
        )

    @app.post("/v1/tasks/research", response_model=ResearchResponse)
    async def run_research(payload: ResearchRequest) -> ResearchResponse:
        try:
            result = await get_workflow().run(
                ResearchTask(query=payload.query, context=payload.context)
            )
        except ValueError as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        return ResearchResponse(
            answer=result.answer,
            model=result.model,
            provider=result.provider,
        )

    return app


app = create_app(get_settings())


def run() -> None:
    """CLI helper used by project script entrypoint."""

    uvicorn.run("ai_native_frame.api:app", host="0.0.0.0", port=8000, reload=False)
