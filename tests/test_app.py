"""Smoke tests for svc-prov."""

from app import app


def test_index_ok():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json() == {"service": "svc-prov", "status": "ok"}


def test_list_users_empty():
    client = app.test_client()
    r = client.get("/users")
    assert r.status_code == 200
    body = r.get_json()
    assert body["items"] == []
    assert body["meta"]["total"] == 0


def test_get_user_404():
    client = app.test_client()
    r = client.get("/users/999")
    assert r.status_code == 404
