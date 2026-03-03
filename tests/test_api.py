from fastapi.testclient import TestClient

from ai_native_frame.api import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "app_name" in payload


def test_research_task_endpoint() -> None:
    response = client.post(
        "/v1/tasks/research",
        json={
            "query": "How should we structure AI native repos?",
            "context": ["Need prompt management and evaluation loops"],
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] == "mock"
    assert payload["answer"]
