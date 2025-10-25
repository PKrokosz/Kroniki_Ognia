import json

from app import app


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
