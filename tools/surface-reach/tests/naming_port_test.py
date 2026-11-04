"""Compare naming ports with the real Rust source compiled as a small executable."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "surface-census"))
import port_pins

REPO = Path(__file__).resolve().parents[3]


def test_naming_ports_against_compiled_rust(tmp_path: Path) -> None:
    port = port_pins.census(REPO)
    source = (REPO / "src/naming.rs").read_text(encoding="utf-8")
    driver = tmp_path / "naming.rs"
    driver.write_text(
        source
        + r"""
fn main() {
    use std::io::BufRead;
    for line in std::io::stdin().lock().lines() {
        let line = line.unwrap();
        let (function, value) = line.split_once('\t').unwrap();
        let output = match function {
            "enum_identifier" => enum_identifier(value),
            "deburred" => (deburr(value) != value).to_string(),
            "is_uuid" => is_uuid(value).to_string(),
            "collapse_digit_boundaries" => collapse_digit_boundaries(value),
            "sanitize_identifier" => sanitize_identifier(value),
            "to_snake_case" => to_snake_case(value),
            "split_words" => split_words(value).join("\t"),
            "class_name" => class_name(value),
            "is_reserved_method" => is_reserved_method(value).to_string(),
            _ => panic!("unknown naming port"),
        };
        println!("{}", output.bytes().map(|b| format!("{b:02x}")).collect::<String>());
    }
}
""",
        encoding="utf-8",
    )
    binary = tmp_path / "naming"
    built = subprocess.run(
        ["rustc", "--edition=2024", str(driver), "-o", str(binary)], capture_output=True, text=True, timeout=120
    )
    assert built.returncode == 0, built.stderr
    # Real naming inputs, arithmetic boundaries, symbol mappings, UUIDs and the
    # whole Latin deburr range. Include values for which identifier recovery fires.
    values = sorted(
        {
            "",
            "list",
            "set",
            "class",
            "123abc",
            "!!!",
            "a.b_c-d",
            "HTTPServer",
            "x1A_b2",
            "000",
            "01_00_AM",
            "n/a",
            "<=",
            "A B C",
            "1a2b",
            "9abc-def0-1234-5678-123456789abc",
            *[f"{digit}abc1234-abcd-1234-abcd-123456789abc" for digit in range(10)],
            "1abc1234-abcd-1234-abcd-123456789abc",
            "12ab1234-abcd-1234-abcd-123456789abc",
            *[str(n) for n in (0, 1, 9, 10, 19, 20, 99, 100, 101, 999, 1000, 1001, 9999, 10000)],
            *[chr(n) for n in range(0xC0, 0x180)],
            *re.findall(r"\('([^']+)',", source.split("const DEBURRED_LATIN:", 1)[1].split("];", 1)[0]),
            *[value for value in re.findall(r'"([^"\n\\]*)"', source) if "\t" not in value],
        }
    )
    functions = (
        "enum_identifier",
        "sanitize_identifier",
        "to_snake_case",
        "split_words",
        "class_name",
        "is_reserved_method",
        "deburred",
        "is_uuid",
        "collapse_digit_boundaries",
    )
    cases = [(name, value) for name in functions for value in values]
    run = subprocess.run(
        [str(binary)],
        input="".join(f"{name}\t{value}\n" for name, value in cases),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert run.returncode == 0, run.stderr
    answers = run.stdout.splitlines()
    assert len(answers) == len(cases)
    for (name, value), answer in zip(cases, answers, strict=True):
        expected = bytes.fromhex(answer).decode("utf-8")
        if name == "deburred":
            trace: set[str] = set()
            port.enum_identifier(value, trace)
            actual = str("deburred" in trace).lower()
        elif name == "is_uuid":
            actual = str("schema.enum:uuid-member" in port.enum_member_predicates({"enum": [value]})).lower()
        elif name == "collapse_digit_boundaries":
            actual = port._collapse_enum_digit_boundaries(value)
        else:
            actual = getattr(port, name)(value)
        if name == "split_words":
            actual = "\t".join(actual)
        elif name == "is_reserved_method":
            actual = str(actual).lower()
        assert actual == expected, (name, value, actual, expected)
