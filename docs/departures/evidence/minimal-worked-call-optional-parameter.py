# llmlint: ignore-file[new_code_lands_in_a_project] documentary evidence kept beside the departure it proves.
"""Show the certified call passing an optional argument, and the minimal call binding."""

import ast
import pathlib
import re
import subprocess
import sys
import tempfile
import typing

root = pathlib.Path(__file__).resolve().parents[3]
fixtures = root / "tests/fixtures"
sources = fixtures / "corpus-sources"


class Case(typing.NamedTuple):
    """One document's omitted optional argument: where to read it and what was declared."""

    fixture: str
    group: str
    method: str
    keyword: str
    line: str
    declared: str


CASES = (
    Case(
        "registered-literals-kong-developer-konghq-com-d58ac8e1",
        "dashboards",
        "list",
        "sort",
        'sort="created_at desc",',
        "example: created_at desc",
    ),
    Case(
        "registered-literals-crate-works-ro-crate-api-f2457da3",
        "entities",
        "list_entities",
        "entity_type",
        'entity_type=["http://pcdm.org/models#Collection"],',
        'example: ["http://pcdm.org/models#Collection"]',
    ),
)
crozier = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "target/debug/crozier"


def parameter_default(client: str, method: str, name: str) -> ast.expr:
    """The default the method's signature gives `name`: an optional argument has one."""
    function = next(
        node
        for node in ast.walk(ast.parse(client))
        if isinstance(node, ast.FunctionDef) and node.name == method
    )
    names = [argument.arg for argument in function.args.kwonlyargs]
    default = function.args.kw_defaults[names.index(name)]
    assert default is not None, f"{name} is required"
    return default


for case in CASES:
    fixture, group, method, keyword, line, declared = (
        case.fixture,
        case.group,
        case.method,
        case.keyword,
        case.line,
        case.declared,
    )
    document = next((sources / fixture).glob("openapi.*")).read_text(encoding="utf-8")
    assert declared in document, f"{fixture}: the document does not declare {declared}"
    certified = (fixtures / fixture / f"expected/src/fern/{group}/client.py").read_text(encoding="utf-8")
    assert line in certified, f"{fixture}: the certified docstring does not pass {line}"
    parameter_default(certified, method, keyword)
    with tempfile.TemporaryDirectory() as directory:
        source = next((sources / fixture).glob("openapi.*"))
        subprocess.run(
            [str(crozier), "generate", "--spec", str(source), "--output", directory, "--package-name", "fern", "python"],
            check=True,
            capture_output=True,
        )
        ours = (pathlib.Path(directory) / f"src/fern/{group}/client.py").read_text(encoding="utf-8")
    assert line not in ours, f"{fixture}: crozier still passes {line}"
    parameter_default(ours, method, keyword)
    call = re.search(rf"client\.{group}\.{method}\((.*?)\)\n", ours, re.DOTALL)
    assert call is not None and f"{keyword}=" not in call.group(1), f"{fixture}: no minimal call"
    print(f"{fixture}: certified passes {line} crozier leaves {keyword} out; both calls bind")
