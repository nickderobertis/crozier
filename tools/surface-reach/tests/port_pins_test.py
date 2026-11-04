"""Real check and repin subprocesses over copies of the pinned Rust source."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "surface-census"))
import port_pins

REPO = Path(__file__).resolve().parents[3]


def stage(root: Path) -> None:
    for directory in ("src", "tools/surface-census", "tools/corpus"):
        shutil.copytree(REPO / directory, root / directory, ignore=shutil.ignore_patterns("__pycache__", "tests"))
    shutil.copy2(REPO / "justfile", root / "justfile")
    subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)


def command(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=120)


def test_tokens_ignore_rustfmt_reflow_whitespace_and_comments(tmp_path: Path) -> None:
    stage(tmp_path)
    pin = next(pin for pin in port_pins.census(tmp_path).PORT_PINS if pin.name == "camel_join")
    path = tmp_path / "src/ir.rs"
    parsed = port_pins._parsed("src/ir.rs", path.read_bytes())
    unit = next(unit for unit in parsed.units if unit.key == "camel_join")
    tokens = parsed.tokens[unit.item : unit.last + 1]
    # Copy this real pinned function alone into a scratch Rust file. Joining
    # every token and splitting every token give rustfmt both forms to reflow.
    body = parsed.source[tokens[0].start : tokens[-1].end].decode("utf-8")
    for layout in (" ".join(body.splitlines()), body.replace(",", ",\n")):
        path.write_text(layout, encoding="utf-8")
        assert port_pins.digest(tmp_path, pin) == pin.digest
        formatted = command(tmp_path, "rustfmt", str(path))
        assert formatted.returncode == 0, formatted.stderr
        assert port_pins.digest(tmp_path, pin) == pin.digest
    text = path.read_text(encoding="utf-8")
    path.write_text(
        text.replace("{", "{ /* a comment { with nested /* braces */ } */\n // another comment\n", 1), encoding="utf-8"
    )
    assert port_pins.digest(tmp_path, pin) == pin.digest
    # A local rename changes a token while the pinned function still resolves.
    path.write_text(text.replace("words", "changed_words"), encoding="utf-8")
    assert port_pins.digest(tmp_path, pin) != pin.digest


def test_three_drifts_require_individual_explicit_confirmation(tmp_path: Path) -> None:
    stage(tmp_path)
    pins = port_pins.census(tmp_path).PORT_PINS
    selected = [pin for pin in pins if pin.name in {"camel_join", "first_tag", "alnum_lower"}]
    assert len(selected) == 3
    path = tmp_path / "src/ir.rs"
    source = path.read_text(encoding="utf-8")
    for pin in selected:
        source = source.replace(f"fn {pin.name}(", f"fn {pin.name}( /* layout alone */", 1)
        parsed = port_pins._parsed("src/ir.rs", source.encode())
        unit = next(unit for unit in parsed.units if unit.key == pin.name)
        opening = next(token.end for token in parsed.tokens[unit.item : unit.last + 1] if token.text == "{")
        source = (source.encode()[:opening] + b" let _port_changed = 1; " + source.encode()[opening:]).decode()
    path.write_text(source, encoding="utf-8")
    table = tmp_path / "tools/surface-census/openapi-surface-census.py"
    original = table.read_bytes()

    def failing(names: list[str]) -> None:
        for args in ((sys.executable, "tools/surface-census/port_pins.py"), ("just", "census-repin")):
            run = command(tmp_path, *args)
            assert run.returncode != 0, run.stdout
            for pin in selected:
                assert (pin.report() in run.stderr) == (pin.name in names), run.stderr

    failing([pin.name for pin in selected])
    assert table.read_bytes() == original
    first, *remaining = selected
    run = command(tmp_path, "just", "census-repin", "--confirm-port", first.name)
    assert run.returncode != 0
    updated = port_pins.census(tmp_path).PORT_PINS
    for before, after in zip(pins, updated, strict=True):
        assert before[:-1] == after[:-1]
        assert (before.digest != after.digest) == (before.name == first.name)
    failing([pin.name for pin in remaining])
    run = command(tmp_path, "just", "census-repin", *[arg for pin in remaining for arg in ("--confirm-port", pin.name)])
    assert run.returncode == 0, run.stderr
    assert command(tmp_path, sys.executable, "tools/surface-census/port_pins.py").returncode == 0
    assert command(tmp_path, "just", "census-repin", "--confirm-port", first.name).returncode == 0
    clean = table.read_bytes()
    run = command(tmp_path, "just", "census-repin", "--confirm-port", "not-a-port")
    assert run.returncode != 0 and "unknown port" in run.stderr
    assert table.read_bytes() == clean


def test_confirmation_preserves_unicode_metadata_and_crlf(tmp_path: Path) -> None:
    """AST columns are byte offsets; a confirmation must preserve all other bytes."""
    import ast

    stage(tmp_path)
    table = tmp_path / "tools/surface-census/openapi-surface-census.py"
    source = table.read_text(encoding="utf-8")
    pin = next(pin for pin in port_pins.census(tmp_path).PORT_PINS if pin.name == "camel_join")
    call = next(
        node
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "PortPin"
        and ast.literal_eval(node.args[0]) == pin.name
    )
    lines = source.splitlines(keepends=True)
    fields = [pin.name, pin.port, pin.rust, pin.confirm + " (café)", pin.digest]
    lines[call.lineno - 1 : call.end_lineno] = ["    PortPin(" + ", ".join(repr(value) for value in fields) + "),\n"]
    original = "".join(lines).replace("\n", "\r\n").encode()
    table.write_bytes(original)
    rust = tmp_path / "src/ir.rs"
    body = rust.read_text(encoding="utf-8")
    signature = "fn camel_join(words: &[String]) -> String {"
    assert signature in body
    rust.write_text(body.replace(signature, signature + " let _changed = 1;", 1), encoding="utf-8")
    actual = port_pins.digest(tmp_path, pin)
    assert actual != pin.digest
    run = command(tmp_path, "just", "census-repin", "--confirm-port", pin.name)
    assert run.returncode == 0, run.stderr
    assert table.read_bytes() == original.replace(pin.digest.encode(), actual.encode(), 1)
