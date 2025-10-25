from __future__ import annotations

import json
import os
import sqlite3
import threading
import time
import uuid
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, TypedDict, cast

from flask import Flask, Response, current_app, jsonify, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import BadRequest

import requests


# Aktualizacja: definiujemy TypedDict dla payloadu, aby doprecyzować kontrakt API.
class IdeaPayload(TypedDict, total=False):
    title: str
    content: str
    tags: Sequence[str] | str | None
    idea: str | None


N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")
N8N_TOKEN = os.getenv("N8N_TOKEN", "")
API_KEY = os.getenv("API_KEY", "dev-key")


def _forward_to_n8n_async(payload: dict[str, Any]) -> None:
    def _job() -> None:
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {N8N_TOKEN}",
            }
            requests.post(
                N8N_WEBHOOK_URL,
                json=payload,
                headers=headers,
                timeout=5,
            )
        except Exception:
            # Fire-and-forget: nie przerywamy UX przy problemach po stronie n8n.
            pass

    threading.Thread(target=_job, daemon=True).start()


def _resolve_data_dir(app: Flask) -> Path:
    data_dir = app.config.get("IDEAS_DATA_DIR")
    if data_dir is None:
        env_dir = os.environ.get("IDEAS_DATA_DIR", "data")
        data_dir = Path(env_dir)
        app.config["IDEAS_DATA_DIR"] = data_dir
    if isinstance(data_dir, str):
        data_dir = Path(data_dir)
        app.config["IDEAS_DATA_DIR"] = data_dir
    return data_dir


def _ensure_schema(connection: sqlite3.Connection) -> None:
    expected_columns = {
        "title": "ALTER TABLE ideas ADD COLUMN title TEXT",
        "content": "ALTER TABLE ideas ADD COLUMN content TEXT",
        "tags": "ALTER TABLE ideas ADD COLUMN tags TEXT DEFAULT '[]'",
        "idea": "ALTER TABLE ideas ADD COLUMN idea TEXT",
    }
    existing_columns = {column[1] for column in connection.execute("PRAGMA table_info(ideas)")}
    for column_name, statement in expected_columns.items():
        if column_name not in existing_columns:
            connection.execute(statement)


def init_storage(app: Flask | None = None) -> None:
    target_app = app or current_app
    data_dir = _resolve_data_dir(target_app)
    data_dir.mkdir(parents=True, exist_ok=True)

    db_path = data_dir / "ideas.sqlite3"
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                tags TEXT,
                created_at TEXT NOT NULL,
                idea TEXT
            )
            """
        )
        _ensure_schema(connection)
        connection.commit()

    text_log = data_dir / "ideas.txt"
    text_log.touch(exist_ok=True)


def create_app(data_dir: Path | str | None = None) -> Flask:
    flask_app = Flask(__name__, static_folder=".", static_url_path="")
    if data_dir is not None:
        flask_app.config["IDEAS_DATA_DIR"] = Path(data_dir)
    else:
        _resolve_data_dir(flask_app)

    init_storage(flask_app)

    CORS(
        flask_app,
        resources={
            r"/api/*": {
                "origins": [
                    "https://pkrokosz.github.io",
                    "https://pkrokosz.github.io/Kroniki_Ognia",
                    "https://*.trycloudflare.com",
                ],
                "methods": ["GET", "POST", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
    )

    limiter = Limiter(
        get_remote_address,
        app=flask_app,
        default_limits=[],
        storage_uri="memory://",
    )

    @flask_app.route("/")
    def root() -> Response:
        return flask_app.send_static_file("index.html")

    @flask_app.get("/api/health")
    def health() -> tuple[Response, int]:
        data_dir_path = _resolve_data_dir(flask_app)
        db_path = data_dir_path / "ideas.sqlite3"
        text_log = data_dir_path / "ideas.txt"

        return (
            jsonify(
                {
                    "status": "ok",
                    "storage": {
                        "data_dir": str(data_dir_path),
                        "database_exists": db_path.exists(),
                        "log_exists": text_log.exists(),
                    },
                }
            ),
            200,
        )

    @flask_app.post("/api/ideas")
    @limiter.limit("10 per minute")
    def submit_idea() -> tuple[Response, int] | Response:
        if request.headers.get("X-API-Key") != API_KEY:
            return jsonify({"status": "error", "error": "unauthorized"}), 401

        if request.mimetype != "application/json":
            return (
                jsonify({"message": "Wymagany nagłówek Content-Type: application/json."}),
                415,
            )

        content_length = request.content_length
        if content_length is not None and content_length > 5 * 1024:
            return (
                jsonify({"message": "Payload przekracza limit 5 KB."}),
                413,
            )

        try:
            raw_payload: Any = request.get_json(force=False, silent=False)
        except BadRequest:
            return jsonify({"message": "Nieprawidłowy JSON w żądaniu."}), 400

        if not isinstance(raw_payload, Mapping):
            return jsonify({"message": "Payload musi być obiektem JSON."}), 400

        payload: IdeaPayload = cast(IdeaPayload, raw_payload)

        legacy_idea = str(payload.get("idea") or "").strip()
        title = str(payload.get("title") or "").strip()
        content = str(payload.get("content") or legacy_idea).strip()

        if not title and legacy_idea:
            title = legacy_idea[:80]

        if not title:
            return jsonify({"message": "Podaj tytuł pomysłu."}), 400

        if not content:
            return jsonify({"message": "Podaj treść pomysłu."}), 400

        tags_value = payload.get("tags")
        tags: list[str]
        if tags_value is None:
            tags = []
        elif isinstance(tags_value, str):
            tags = [segment.strip() for segment in tags_value.split(",") if segment.strip()]
        elif isinstance(tags_value, Sequence):
            tags = [str(segment).strip() for segment in tags_value if str(segment).strip()]
        else:
            return jsonify({"message": "Pole tags musi być listą lub tekstem."}), 400

        now = datetime.now(UTC)
        timestamp = now.isoformat(timespec="seconds")
        event_id = f"{int(time.time())}-{uuid.uuid4().hex[:8]}"
        data_dir_path = _resolve_data_dir(flask_app)
        db_path = data_dir_path / "ideas.sqlite3"
        with sqlite3.connect(db_path) as connection:
            cursor = connection.execute(
                "INSERT INTO ideas (title, content, tags, created_at, idea) VALUES (?, ?, ?, ?, ?)",
                (title, content, json.dumps(tags, ensure_ascii=False), timestamp, content),
            )
            connection.commit()
            idea_id = cursor.lastrowid or uuid.uuid4().hex

        text_log = data_dir_path / "ideas.txt"
        with text_log.open("a", encoding="utf-8") as handle:
            tags_fragment = f" | tags: {', '.join(tags)}" if tags else ""
            handle.write(f"{timestamp} | {title} | {content}{tags_fragment} | event: {event_id}\n")

        response_json = {"id": event_id, "status": "ok", "record_id": str(idea_id)}

        if N8N_WEBHOOK_URL:
            client_ip = request.headers.get("CF-Connecting-IP") or request.remote_addr
            n8n_payload = {
                "event_id": event_id,
                "received_at": now.isoformat(),
                "source": "kroniki-ognia-form",
                "idea": {
                    "title": title,
                    "content": content,
                    "tags": tags,
                },
                "client": {
                    "ip": client_ip,
                    "ua": request.headers.get("User-Agent"),
                },
            }
            _forward_to_n8n_async(n8n_payload)

        return jsonify(response_json), 201

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
