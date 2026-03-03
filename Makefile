PYTHON ?= python3
VENV ?= .venv

.PHONY: setup run lint format typecheck test eval ci

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -e ".[dev]"

run:
	$(VENV)/bin/uvicorn ai_native_frame.api:app --reload --host 0.0.0.0 --port 8000

lint:
	$(VENV)/bin/ruff check src tests
	$(VENV)/bin/ruff format --check src tests

format:
	$(VENV)/bin/ruff check --fix src tests
	$(VENV)/bin/ruff format src tests

typecheck:
	$(VENV)/bin/mypy src

test:
	$(VENV)/bin/pytest

eval:
	$(VENV)/bin/python -m ai_native_frame.evals.runner --dataset evals/datasets/sample_tasks.jsonl

ci: lint typecheck test eval
