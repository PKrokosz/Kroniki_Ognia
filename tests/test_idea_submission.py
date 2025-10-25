from __future__ import annotations

import sqlite3
from pathlib import Path

from app import API_KEY, create_app


def _read_log(log_path: Path) -> str:
    if not log_path.exists():
        return ""
    return log_path.read_text(encoding="utf-8")


def test_submit_idea_persists(tmp_path):
    app = create_app(tmp_path)
    client = app.test_client()

    response = client.post(
        "/api/ideas",
        json={
            "title": "Testowy tytuł",
            "content": "Testowy pomysł o rytuale",
            "tags": ["rytuał", "ognisko"],
        },
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "X-API-Key": API_KEY,
        },
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload
    assert payload["status"] == "ok"
    assert payload["id"]
    assert payload["record_id"]

    log_path = tmp_path / "ideas.txt"
    log_contents = _read_log(log_path)
    assert "Testowy tytuł" in log_contents
    assert "rytuał, ognisko" in log_contents

    db_path = tmp_path / "ideas.sqlite3"
    assert db_path.exists()
    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT title, content, tags FROM ideas").fetchall()
    assert rows == [("Testowy tytuł", "Testowy pomysł o rytuale", '["rytuał", "ognisko"]')]


def test_submit_idea_requires_text(tmp_path):
    app = create_app(tmp_path)
    client = app.test_client()

    response = client.post(
        "/api/ideas",
        json={"title": "Bez treści", "content": "   "},
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "X-API-Key": API_KEY,
        },
    )

    assert response.status_code == 400
    payload = response.get_json()
    assert payload
    assert "Podaj treść pomysłu" in payload["message"]

    log_path = tmp_path / "ideas.txt"
    assert _read_log(log_path) == ""

    db_path = tmp_path / "ideas.sqlite3"
    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT COUNT(*) FROM ideas").fetchone()
    assert rows == (0,)
