import pathlib
from tools.prov_check import check_module


def test_missing_canary(tmp_path: pathlib.Path) -> None:
    p = tmp_path / "m.py"
    p.write_text("x = 1\n")
    err = check_module(p)
    assert err is not None and "_PROV_CANARY" in err


def test_present_canary(tmp_path: pathlib.Path) -> None:
    p = tmp_path / "m.py"
    p.write_text(
        "from typing import Final\n"
        "_PROV_CANARY: Final[tuple[int, ...]] = (97, 98, 49, 50)\n"
    )
    assert check_module(p) is None
