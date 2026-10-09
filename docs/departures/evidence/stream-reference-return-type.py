import inspect
import pathlib
import re
import sys

import httpx

USAGE = "usage: stream-reference-return-type.py <generated SDK root> contradicts|agrees"
if len(sys.argv) != 3 or sys.argv[2] not in ("contradicts", "agrees"):
    sys.exit(USAGE)
root = pathlib.Path(sys.argv[1])
if not (root / "src" / "fern" / "__init__.py").is_file() or not (root / "reference.md").is_file():
    sys.exit(f"{root}: no generated `fern` package and reference.md here; pass the SDK root\n{USAGE}")
sys.path.insert(0, str(root / "src"))
from fern import FernApi

HEADING = re.compile(r'^<details><summary><code>client\.<a href="[^"]+">(\w+)</a>\(.*\) -> (.+)</code></summary>$')
documented = {
    match.group(1): match.group(2)
    for match in map(HEADING.match, (root / "reference.md").read_text(encoding="utf-8").splitlines())
    if match
}


def events(request):
    body = 'data: {"step": "lint", "passed": true}\n\ndata: {"step": "test", "passed": false}\n\ndata: [DONE]\n\n'
    return httpx.Response(200, headers={"content-type": "text/event-stream"}, text=body)


client = FernApi(base_url="https://builds.test", httpx_client=httpx.Client(transport=httpx.MockTransport(events)))
method = client.follow_build_log
declared = inspect.signature(method).return_annotation
declared = f"typing.Iterator[{declared.__args__[0].__name__}]"
yielded = sorted({type(chunk).__name__ for chunk in method(build_id="b-1")})
heading = documented["follow_build_log"]
print(f"reference.md heads follow_build_log `-> {heading}`; the method declares `-> {declared}`; iterating yields {yielded}")
agrees = heading == declared and yielded == [declared.removeprefix("typing.Iterator[").removesuffix("]")]
if agrees != (sys.argv[2] == "agrees"):
    sys.exit(f"expected the heading to {sys.argv[2].replace('agrees', 'agree with')} the method, and it does not")
