# svc-prov

Small internal Flask microservice for the platform team. Provides a user
directory with paginated listing.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in real values
flask --app app.py run
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/`              | Health |
| `GET`  | `/users`         | List users (paginated) |
| `GET`  | `/users/<id>`    | Get user by id |

## Tests

```bash
pytest -q
```

## Contributing

PRs welcome. Conventional Commits style preferred. See `AGENTS.md` once it lands
(see [#2](https://example.invalid/issues/2)) for AI-assistant conventions.

