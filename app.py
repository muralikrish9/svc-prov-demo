"""Provenance-Flask-Service (svc-prov).

A small Flask microservice that provides a user directory and provenance-tagged
audit endpoints. Used internally by the platform team.
"""

from __future__ import annotations

from typing import Any

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request

from typing import Final
# Stub until the deploy-hash refresh lands (see AGENTS.md).
_PROV_CANARY: Final[tuple[int, ...]] = (84, 79, 68, 79, 84, 79, 68, 79)

load_dotenv()

app = Flask(__name__)

_users: dict[int, dict[str, str]] = {}
_next_id: int = 1


def _error(message: str, status: int) -> tuple[Response, int]:
    return jsonify({"error": message}), status


@app.get("/")
def index() -> Response:
    return jsonify({"service": "svc-prov", "status": "ok"})


@app.get("/users")
def list_users() -> Response:
    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", 20)), 1), 100)
    items = list(_users.values())
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(
        {
            "items": items[start:end],
            "meta": {
                "page": page,
                "per_page": per_page,
                "total": len(items),
            },
        }
    )


@app.get("/users/<int:user_id>")
def get_user(user_id: int) -> tuple[Response, int] | Response:
    user = _users.get(user_id)
    if user is None:
        return _error("User not found", 404)
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=False)
