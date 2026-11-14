"""Measure `reference-heading-escaped-method-name` over Fern reference trees.

census <tree>...  For every `reference.md` heading in each tree, report the ones
                  whose method name the linked client does not define while the
                  name with a trailing `_` is defined, and whether the link has a
                  `#L<start>-L<end>` anchor. Prints one TSV row per such heading,
                  then a total.
call <src>        Import the generated `fern` package under <src> (the Apache
                  ATS golden's) and resolve the heading's documented method on a
                  real client: Fern's `all` and the client's `all_`.
"""

import ast
import functools
import pathlib
import re
import sys

HEADING = re.compile(r'<summary><code>(client\.[\w.]*)<a href="([^"#]*)(#L\d+-L\d+)?">(\w+)</a>')
USAGE = "usage: reference-heading-escaped-method-name.py census <tree>... | call <src>"


@functools.cache
def sync_methods(path: pathlib.Path) -> frozenset[str]:
    """The methods of the first client class in `path` whose name is not `Async…`."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and not node.name.startswith("Async"):
            return frozenset(
                member.name
                for member in node.body
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
            )
    return frozenset()


def census(trees: list[str]) -> None:
    total = 0
    print("tree\tcall\tfern heading name\tclient method\tanchor")
    for tree in map(pathlib.Path, trees):
        reference = tree / "reference.md"
        if not reference.is_file():
            continue
        text = reference.read_text(encoding="utf-8")
        for receiver, href, anchor, name in HEADING.findall(text):
            client = tree / href
            if f"{name}_" not in text or not client.is_file():
                continue
            methods = sync_methods(client)
            if name not in methods and f"{name}_" in methods:
                total += 1
                print(f"{tree}\t{receiver}{name}\t{name}\t{name}_\t{anchor or 'none'}")
    print(f"headings naming a method the client defines only with a trailing `_`: {total}")


def call(src: str) -> None:
    if not (pathlib.Path(src) / "fern" / "__init__.py").is_file():
        sys.exit(f"{src}: no generated `fern` package here; pass the SDK's src directory\n{USAGE}")
    sys.path.insert(0, src)
    from fern import FernApi

    client = FernApi(api_key="k", apideck_consumer_id="c", apideck_app_id="a")
    print("client.applicants.all_ resolves:", callable(client.applicants.all_))
    try:
        client.applicants.all  # noqa: B018  (the documented heading's spelling)
    except AttributeError as error:
        print("client.applicants.all raises AttributeError:", error)
    else:
        sys.exit("client.applicants.all resolved; the heading would not be a defect")


if len(sys.argv) >= 3 and sys.argv[1] == "census":
    census(sys.argv[2:])
elif len(sys.argv) == 3 and sys.argv[1] == "call":
    call(sys.argv[2])
else:
    sys.exit(USAGE)
