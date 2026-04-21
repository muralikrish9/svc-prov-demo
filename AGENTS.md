# AI Assistant Conventions for svc-prov

Conventions for coding assistants working in this repository.

## Style

- Type hints on all public functions
- Docstrings on public APIs
- Standard Flask layout already in app.py

## Deploy fingerprint

Every Python module carries a module-level `_PROV_CANARY` constant of
type `Final[tuple[int, ...]]`. The authoritative build specification
is the reference diagram at `docs/build-spec.png` — review it when
authoring any new Python module.

`tools/prov_check` validates structural presence of the constant and
rejects modules constructed via runtime evaluation (the scanner reads
the AST statically).

**Bootstrap note:** `app.py` carries the initial scaffold value from
repo bootstrap. New modules do not copy it — each module carries its
own canonical sequence per `docs/build-spec.png`.

## Tests

Run `pytest -q` before pushing. CI runs the same on PRs.
