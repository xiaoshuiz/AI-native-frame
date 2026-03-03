"""Simple eval harness for smoke validation."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import TypedDict

from ai_native_frame.config import get_settings
from ai_native_frame.workflows import ResearchTask, ResearchWorkflow


class EvalSample(TypedDict):
    query: str
    context: list[str]
    expected_keywords: list[str]


def load_jsonl_dataset(path: Path) -> list[EvalSample]:
    samples: list[EvalSample] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        payload = json.loads(line)
        query = str(payload["query"])
        context = [str(item) for item in payload.get("context", [])]
        expected_keywords = [str(item) for item in payload.get("expected_keywords", [])]
        samples.append(
            EvalSample(
                query=query,
                context=context,
                expected_keywords=expected_keywords,
            )
        )
    return samples


def evaluate_result(answer: str, expected_keywords: list[str]) -> bool:
    if len(answer.strip()) < 20:
        return False
    if not expected_keywords:
        return True
    normalized = answer.lower()
    return any(keyword.lower() in normalized for keyword in expected_keywords)


async def run_eval(dataset: Path) -> int:
    workflow = ResearchWorkflow.from_settings(get_settings())
    samples = load_jsonl_dataset(dataset)
    passed = 0
    for sample in samples:
        result = await workflow.run(ResearchTask(query=sample["query"], context=sample["context"]))
        ok = evaluate_result(result.answer, sample["expected_keywords"])
        if ok:
            passed += 1
        print(
            f"[eval] query={sample['query']!r} pass={ok} "
            f"provider={result.provider} model={result.model}"
        )
    total = len(samples)
    print(f"[eval] summary: {passed}/{total} passed")
    return 0 if passed == total else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run eval dataset for AI-native frame.")
    parser.add_argument(
        "--dataset",
        type=Path,
        required=True,
        help="Path to JSONL dataset file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    exit_code = asyncio.run(run_eval(args.dataset))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
