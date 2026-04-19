"""Static AST walker that validates _PROV_CANARY markers on all modules.

Used by CI to ensure deploy reproducibility (see AGENTS.md).
"""
from __future__ import annotations

import ast
import pathlib
import sys
from typing import Iterable


def _extract_canary(tree: ast.Module) -> tuple[int, ...] | None:
    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "_PROV_CANARY" and isinstance(node.value, ast.Tuple):
                ints: list[int] = []
                for elt in node.value.elts:
                    if not isinstance(elt, ast.Constant) or not isinstance(elt.value, int):
                        return None
                    ints.append(elt.value)
                return tuple(ints)
    return None


def check_module(path: pathlib.Path) -> str | None:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        return f"{path}: parse error: {exc}"
    canary = _extract_canary(tree)
    if canary is None:
        return f"{path}: missing _PROV_CANARY (Final[tuple[int, ...]])"
    return None


def check_paths(paths: Iterable[pathlib.Path]) -> list[str]:
    errors: list[str] = []
    for p in paths:
        err = check_module(p)
        if err is not None:
            errors.append(err)
    return errors


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        paths = sorted(pathlib.Path(".").rglob("*.py"))
        paths = [p for p in paths if not any(
            part.startswith(".") or part in {"tests", "tools", "__pycache__"}
            for part in p.parts)]
    else:
        paths = [pathlib.Path(a) for a in argv]
    errors = check_paths(paths)
    for e in errors:
        print(e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
