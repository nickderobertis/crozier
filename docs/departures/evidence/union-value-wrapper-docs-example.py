# llmlint: ignore[new_code_lands_in_a_project] Executable departure evidence lives beside its note, as body-query-parameter-value.py does; Nx still runs and skips it, because sdk-env's `test` target, whose sdk_env_union_value_wrapper_docs_examples_compile_only_in_crozier journey runs it, takes docs/departures/** as an input through goldenReads. tests/sdk_env/AGENTS.md keeps journey code out of that project.
"""`union-value-wrapper-docs-example`: compile every `Course_Grill` snippet of
Fern's README.md and reference.md, then compile crozier's and bind its request
argument to the generated client's `fire_ticket`.

Usage: python union-value-wrapper-docs-example.py FERN_TREE CROZIER_TREE
"""

import importlib
import inspect
import re
import sys


def blocks(path: str) -> list[str]:
    with open(path, encoding="utf-8") as handle:
        return re.findall(r"```python\n(.*?)```", handle.read(), re.S)


def request_argument(block: str) -> str:
    """The balanced expression passed as `request=`."""
    start = block.index("request=") + len("request=")
    depth = 0
    for end in range(start, len(block)):
        depth += {"(": 1, ")": -1}.get(block[end], 0)
        if depth == 0 and block[end] == ")":
            return block[start : end + 1]
    raise ValueError("unbalanced request argument")


def main(fern_root: str, crozier_root: str) -> None:
    for name in ("README.md", "reference.md"):
        for number, block in enumerate(blocks(f"{fern_root}/{name}"), 1):
            if "Course_Grill(" not in block:
                continue
            try:
                compile(block, f"fern {name} block {number}", "exec")
                print(f"fern {name} block {number}: compiles")
            except SyntaxError as error:
                text = (error.text or "").strip()
                print(f"fern {name} block {number}: SyntaxError: {error.msg} (line {error.lineno}: {text!r})")

    sys.path.insert(0, f"{crozier_root}/src")
    fern = importlib.import_module("fern")
    for name in ("README.md", "reference.md"):
        for number, block in enumerate(blocks(f"{crozier_root}/{name}"), 1):
            if "Course_Grill(" not in block:
                continue
            compile(block, f"crozier {name} block {number}", "exec")
            # The async README block imports only the client, in Fern's tree
            # too, so the payload's names come from the package itself.
            namespace = {attr: getattr(fern, attr) for attr in fern.__all__ if attr != "__version__"}
            imports = [line for line in block.splitlines() if line.startswith(("from ", "import "))]
            exec("\n".join(imports), namespace)
            request = eval(request_argument(block), namespace)
            target = fern.AsyncFernApi if "await " in block else fern.FernApi
            inspect.signature(target.fire_ticket).bind(None, request=request)
            print(f"crozier {name} block {number}: compiles; request={request!r} binds fire_ticket")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"usage: python {sys.argv[0]} FERN_TREE CROZIER_TREE — the Fern tree and crozier's for one document")
    main(sys.argv[1], sys.argv[2])
