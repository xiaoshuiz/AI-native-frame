from ai_native_frame.evals.runner import evaluate_result


def test_evaluate_result_with_expected_keywords() -> None:
    answer = "Summary: production rollout needs canary and risk controls."
    assert evaluate_result(answer, ["canary", "risk"])


def test_evaluate_result_rejects_too_short_answer() -> None:
    assert not evaluate_result("short", [])
