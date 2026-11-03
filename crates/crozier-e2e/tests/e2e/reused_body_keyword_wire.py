"""Compile and run a generated README's synchronous `file_question` worked call.

Usage: reused_body_keyword_wire.py TREE. TREE is a generated SDK holding
README.md and src/fern. The README's one synchronous
`client.questions.file_question(` call is compiled; a call that does not
compile (a repeated keyword) prints its SyntaxError on stderr and exits 1.
One that compiles is executed, unmodified, against the generated `fern`
package; only httpx's network transport is replaced, so each request the
SDK's own client sends is answered locally and printed as `METHOD URL BODY`;
exit 0. Exit 2 reports invalid CLI arguments or a tree without one such call.
"""

import argparse
import re
import sys
from pathlib import Path

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
sent: list[httpx.Request] = []


def handle(_transport: httpx.HTTPTransport, request: httpx.Request) -> httpx.Response:
    request.read()
    sent.append(request)
    return httpx.Response(200, json={"ticket_id": "t-1"})


# llmlint: ignore[e2e_not_mocked, tests_mirror_real_usage] The README's call is run verbatim, so its `FernApi()` builds the SDK's client through the public constructor against the declared `https://desk.greenhouse.test`; pointing it at a local server would edit the call under test, so only the socket boundary is replaced, standing in for that external server's response.
httpx.HTTPTransport.handle_request = handle  # type: ignore[method-assign]
# Running the generated README's own worked call is what this journey proves.
exec(code, {"__name__": "worked_call"})  # noqa: S102
for request in sent:
    print(request.method, str(request.url), request.content.decode())
