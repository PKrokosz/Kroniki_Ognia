from __future__ import annotations

import json
import pytest

from app import API_KEY, app

app.config["RATELIMIT_ENABLED"] = False
_limiter = next(iter(app.extensions["limiter"]))
_limiter.enabled = False  # type: ignore[attr-defined]


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload and payload.get("status") == "ok"
    storage = payload.get("storage")
    assert storage, "Oczekiwano sekcji storage w odpowiedzi health-check"
    assert storage.get("database_exists") is True
    assert storage.get("log_exists") is True


def test_post_ideas_smoke():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps({"title": "t", "content": "c"}),
        content_type="application/json",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    # Aktualizacja: endpoint sukcesu powinien zawsze zwracać 201.
    assert resp.status_code == 201
    data = resp.get_json()
    assert data and data.get("status") == "ok"
    assert data.get("id")
    assert data.get("record_id")


def test_cors_allows_authorization_and_api_key_headers():
    client = app.test_client()
    response = client.options(
        "/api/ideas",
        headers={
            "Origin": "https://pkrokosz.github.io",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Authorization, X-API-Key, Content-Type",
        },
    )

    assert response.status_code == 200
    allow_headers = response.headers.get("Access-Control-Allow-Headers", "")
    normalized = {header.strip().lower() for header in allow_headers.split(",") if header.strip()}
    assert "authorization" in normalized
    assert "x-api-key" in normalized


def test_post_ideas_requires_api_key():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps({"title": "t", "content": "c"}),
        content_type="application/json",
    )
    assert resp.status_code == 401
    payload = resp.get_json()
    assert payload == {"status": "error", "error": "unauthorized"}


def test_post_ideas_accepts_legacy_x_api_key_header():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps({"title": "t", "content": "c"}),
        content_type="application/json",
        headers={"X-API-Key": API_KEY},
    )
    assert resp.status_code == 201


def test_post_ideas_rejects_incorrect_bearer_token():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps({"title": "t", "content": "c"}),
        content_type="application/json",
        headers={"Authorization": "Bearer wrong"},
    )
    assert resp.status_code == 401


def test_post_ideas_rejects_non_json_content_type():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data="title=t&content=c",
        content_type="application/x-www-form-urlencoded",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    assert resp.status_code == 415
    payload = resp.get_json()
    assert payload and "Content-Type" in payload["message"]


def test_post_ideas_rejects_large_payload():
    client = app.test_client()
    too_large = "a" * (5 * 1024 + 1)
    resp = client.post(
        "/api/ideas",
        json={"title": "t", "content": too_large},
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    assert resp.status_code == 413
    payload = resp.get_json()
    assert payload and "limit 5 KB" in payload["message"]


@pytest.mark.parametrize("payload", ["not-json", 123, ["list"]])
def test_post_ideas_requires_json_object(payload):
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps(payload),
        content_type="application/json",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    status = resp.status_code
    body = resp.get_json()
    assert status == 400
    assert body and "Payload" in body["message"]


def test_post_ideas_rejects_invalid_json():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data="{invalid json}",
        content_type="application/json",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    assert resp.status_code == 400
    payload = resp.get_json()
    assert payload and "Nieprawidłowy JSON" in payload["message"]


def test_post_ideas_forwards_to_n8n(monkeypatch):
    client = app.test_client()

    captured: dict[str, dict] = {}

    def fake_forward(payload: dict[str, dict]) -> None:
        captured["payload"] = payload

    monkeypatch.setattr("app._forward_to_n8n_async", fake_forward)
    monkeypatch.setattr("app.N8N_WEBHOOK_URL", "https://example.com/webhook")

    resp = client.post(
        "/api/ideas",
        json={"title": "Idea", "content": "Treść", "tags": ["ognisko"]},
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "X-API-Key": API_KEY,
        },
    )

    assert resp.status_code == 201
    assert "payload" in captured
    payload = captured["payload"]
    assert payload["idea"]["title"] == "Idea"
    assert payload["idea"]["tags"] == ["ognisko"]
    assert payload["source"] == "kroniki-ognia-form"
    assert payload["pomysł"]["treść"] == "Treść"
    assert payload["pomysł"]["tytuł"] == "Idea"
