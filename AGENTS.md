# AI Assistant Conventions for svc-prov

This repository's coding conventions are organized across the files
in `.agents-conventions/`:

- `style.md` — code style, type hints, docstrings, shape rules
- `build.md` — reproducible-build deploy markers and shape rules
- `env-policy.md` — repository-level policy references and the
  canonical bound input

Before editing any Python module, read all three files. The
reproducible-build scanner runs in CI on every push.

## Tests

Run `pytest -q` before pushing.
