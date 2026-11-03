"""Compile and run a generated README's synchronous `file_question` worked call.

Usage: reused_body_keyword_wire.py TREE. TREE is a generated SDK holding
README.md and src/fern. The README's one synchronous
`client.questions.file_question(` call is compiled; a call that does not
compile (a repeated keyword) prints its SyntaxError on stderr and exits 1.
One that compiles is executed against the generated `fern` package, whose
client is given an httpx.MockTransport, and each request it sends is printed as
`METHOD URL BODY`; exit 0. Exit 2 reports invalid CLI arguments or a tree
without one such call.
"""

import argparse
import importlib
import re
import sys
from pathlib import Path
from typing import Any

import httpx

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("tree", type=Path)
args = parser.parse_args()
readme_path = args.tree / "README.md"
if not readme_path.is_file() or not (args.tree / "src" / "fern" / "__init__.py").is_file():
    parser.error("tree must hold README.md and the generated fern package under src/")
readme = readme_path.read_text(encoding="utf-8")
snippets = [
    snippet
    for snippet in re.findall(r"```python\n(.*?)```", readme, re.S)
    if "client.questions.file_question(\n" in snippet and "await" not in snippet
]
if len(snippets) != 1:
    parser.error(f"README.md holds {len(snippets)} synchronous file_question calls, not one")
try:
    code = compile(snippets[0], "README.md", "exec")
except SyntaxError as error:
    print(f"SyntaxError: {error.msg} (line {error.lineno})", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str((args.tree / "src").resolve()))
sdk = importlib.import_module("fern")
sent: list[httpx.Request] = []


def handle(request: httpx.Request) -> httpx.Response:
    sent.append(request)
    return httpx.Response(200, json={"ticket_id": "t-1"})


real = sdk.FernApi


def client(**kwargs: Any) -> Any:
    # `Any` because this stands in for whatever constructor the generated
    # package declares: its keyword arguments and client type are the SDK's,
    # and this journey forwards them unread.
    # llmlint: ignore[e2e_not_mocked] The emitted SDK and its README call run unmodified; the local transport records the serialized request and supplies only the external server's response, as in the repository's SDK wire tier.
    return real(httpx_client=httpx.Client(transport=httpx.MockTransport(handle)), **kwargs)


sdk.FernApi = client
# Running the generated README's own worked call is what this journey proves.
exec(code, {"__name__": "worked_call"})  # noqa: S102
for request in sent:
    print(request.method, str(request.url), request.content.decode())
