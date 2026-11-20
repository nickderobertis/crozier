# llmlint: ignore-file[new_code_lands_in_a_project] documentary evidence kept beside the departure note it supports, like the other docs/departures/evidence scripts: the sdk-env tier's journey runs it against the committed certified tree and a freshly generated crozier SDK.
"""Execute every worked-example construction of a model whose required field Fern omits.

usage: required-null-union-field-example.py SDK_ROOT {invalid,valid}

SDK_ROOT is a generated SDK (its `src/` holds the `fern` package, and its
`reference.md` sits beside it). The script finds every model whose field is
required (no default) and typed by a union alias opening with
`typing.Optional[`, then every constructor of such a model in a client
docstring or a `reference.md` example, and evaluates each against the
generated package. `invalid` expects each construction to raise pydantic's
`ValidationError` for a missing field (Fern's examples); `valid` expects each to
construct (crozier's). Each construction is printed with its outcome; the exit
status is 0 only when every construction behaves as expected and at least one
was found. Needs pydantic and httpx importable.
"""

from __future__ import annotations

import builtins
import importlib
import pathlib
import re
import sys

UNION = re.compile(r"^(\w+) = typing\.Union\[\n?\s*typing\.Optional\[", re.M)
CLASS = re.compile(r"^class (\w+)\(", re.M)


def required_null_union_fields(package: pathlib.Path) -> dict[str, set[str]]:
    """Each model class's required fields typed by a union opening with an optional member."""
    sources = [path.read_text(encoding="utf-8") for path in package.rglob("*.py")]
    unions = {match.group(1) for text in sources for match in UNION.finditer(text)}
    fields: dict[str, set[str]] = {}
    for text in sources:
        for match in CLASS.finditer(text):
            body = text[match.end() :].split("\nclass ", 1)[0]
            for line in body.splitlines():
                name, _, annotation = line.removeprefix("    ").partition(": ")
                if line.startswith("    ") and not line.startswith("     ") and annotation in unions:
                    fields.setdefault(match.group(1), set()).add(name)
    return fields


def constructions(root: pathlib.Path, classes: set[str]) -> list[tuple[str, str]]:
    """Every `Class(...)` expression of a worked example, with where it was found."""
    found = []
    texts = [(path, path.read_text(encoding="utf-8")) for path in sorted((root / "src").rglob("client.py"))]
    texts.append((root / "reference.md", (root / "reference.md").read_text(encoding="utf-8")))
    for path, text in texts:
        lines = text.splitlines()
        for index, line in enumerate(lines):
            opened = re.fullmatch(r"(\s*)(\w+)\(", line)
            if not opened or opened.group(2) not in classes:
                continue
            indent = opened.group(1)
            end = next(at for at in range(index + 1, len(lines)) if lines[at] == f"{indent})")
            expression = "\n".join(item.strip() for item in lines[index : end + 1])
            found.append((f"{path.relative_to(root)}:{index + 1}", expression))
    return found


class Package(dict):
    """Names an example uses, each looked up on the generated package."""

    def __init__(self, module) -> None:
        super().__init__()
        self.module = module

    def __missing__(self, name: str):
        return getattr(self.module, name)


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in ("invalid", "valid"):
        print(__doc__.split("\n\n", 2)[1], file=sys.stderr)
        return 2
    root, expect = pathlib.Path(argv[0]), argv[1]
    package = root / "src" / "fern"
    if not (package / "__init__.py").is_file():
        print(f"{root}: holds no src/fern package; pass a generated SDK's root", file=sys.stderr)
        return 2
    sys.path.insert(0, str(root / "src"))
    import pydantic

    fern = importlib.import_module("fern")
    fields = required_null_union_fields(package)
    found = constructions(root, set(fields))
    if not found:
        print(f"{root}: no worked example constructs a model with such a field", file=sys.stderr)
        return 1
    failures = 0
    for where, expression in found:
        try:
            eval(expression, {"__builtins__": builtins}, Package(fern))
        except pydantic.ValidationError as error:
            missing = sorted(
                str(problem["loc"][-1]) for problem in error.errors() if problem["type"] == "missing"
            )
            outcome = f"ValidationError: missing {', '.join(missing)}"
            failures += expect == "valid" or not missing
        else:
            outcome = "constructs"
            failures += expect == "invalid"
        print(f"{where}: {outcome}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
