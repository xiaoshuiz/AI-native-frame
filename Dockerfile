FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd -m appuser

COPY pyproject.toml README.md ./
COPY src ./src
COPY prompts ./prompts
COPY evals ./evals
COPY configs ./configs

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

USER appuser

EXPOSE 8000

CMD ["uvicorn", "ai_native_frame.api:app", "--host", "0.0.0.0", "--port", "8000"]
