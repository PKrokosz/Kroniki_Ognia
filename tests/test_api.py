from __future__ import annotations

import json
from typing import Any

from flask.testing import FlaskClient

from app import app


def _build_client() -> FlaskClient:
    return app.test_client()


def test_post_ideas_smoke() -> None:
    client = _build_client()
    resp = client.post(
        "/api/ideas",
        data=json.dumps({"title": "t", "content": "c"}),
        content_type="application/json",
    )
    assert resp.status_code in (200, 201)
    data = resp.get_json()
    assert data and data.get("status") == "ok"


def test_health_ok() -> None:
    client = _build_client()
    resp = client.get("/api/health")
    assert resp.status_code == 200
    payload_raw = resp.get_json()
    assert isinstance(payload_raw, dict)
    payload: dict[str, Any] = payload_raw

    expected_storage_raw = payload.get("storage", {})
    assert isinstance(expected_storage_raw, dict)
    expected_storage: dict[str, Any] = expected_storage_raw

    assert payload.get("status") == "ok"
    assert expected_storage.get("database_exists") is True
    assert expected_storage.get("log_exists") is True
    assert isinstance(expected_storage.get("data_dir"), str) and expected_storage["data_dir"]
