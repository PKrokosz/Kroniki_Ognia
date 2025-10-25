from __future__ import annotations

import sqlite3
from pathlib import Path

from app import create_app


def _read_log(log_path: Path) -> str:
    if not log_path.exists():
        return ""
    return log_path.read_text(encoding="utf-8")


def test_submit_idea_persists(tmp_path):
    app = create_app(tmp_path)
    client = app.test_client()

    response = client.post("/api/ideas", json={"idea": "Testowy pomysł o rytuale"})

    assert response.status_code == 201
    payload = response.get_json()
    assert payload
    assert payload["idea"] == "Testowy pomysł o rytuale"
    assert "Dziękujemy" in payload["message"]

    log_path = tmp_path / "ideas.txt"
    assert "Testowy pomysł o rytuale" in _read_log(log_path)

    db_path = tmp_path / "ideas.sqlite3"
    assert db_path.exists()
    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT idea FROM ideas").fetchall()
    assert rows == [("Testowy pomysł o rytuale",)]


def test_submit_idea_requires_text(tmp_path):
    app = create_app(tmp_path)
    client = app.test_client()

    response = client.post("/api/ideas", json={"idea": "   "})

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
