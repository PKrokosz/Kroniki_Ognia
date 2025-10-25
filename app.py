from __future__ import annotations

import os
import sqlite3
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Mapping

from flask import Flask, Response, current_app, jsonify, request


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
                idea TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
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

    @flask_app.route("/")
    def root() -> Response:
        return flask_app.send_static_file("index.html")

    @flask_app.post("/api/ideas")
    def submit_idea() -> tuple[Response, int] | Response:
        payload: Mapping[str, Any] | None = request.get_json(silent=True)
        if not payload:
            payload = request.form
        idea_text = (payload or {}).get("idea")

        if idea_text is None or not str(idea_text).strip():
            return jsonify({"message": "Podaj treść pomysłu."}), 400

        cleaned_idea = str(idea_text).strip()
        timestamp = datetime.now(UTC).isoformat(timespec="seconds")

        data_dir_path = _resolve_data_dir(flask_app)
        db_path = data_dir_path / "ideas.sqlite3"
        with sqlite3.connect(db_path) as connection:
            connection.execute(
                "INSERT INTO ideas (idea, created_at) VALUES (?, ?)",
                (cleaned_idea, timestamp),
            )
            connection.commit()

        text_log = data_dir_path / "ideas.txt"
        with text_log.open("a", encoding="utf-8") as handle:
            handle.write(f"{timestamp} | {cleaned_idea}\n")

        return jsonify({"message": "Dziękujemy! Pomysł został zapisany.", "idea": cleaned_idea}), 201

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
