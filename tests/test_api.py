from __future__ import annotations

import json
import pytest

from app import app


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
    )
    assert resp.status_code in (200, 201)
    data = resp.get_json()
    assert data and data.get("status") == "ok"


def test_post_ideas_rejects_non_json_content_type():
    client = app.test_client()
    resp = client.post(
        "/api/ideas",
        data="title=t&content=c",
        content_type="application/x-www-form-urlencoded",
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
    )
    assert resp.status_code == 400
    payload = resp.get_json()
    assert payload and "Nieprawidłowy JSON" in payload["message"]
