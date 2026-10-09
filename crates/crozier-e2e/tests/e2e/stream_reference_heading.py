"""The `stream-reference-return-type` departure's evidence journey.

Usage: stream_reference_heading.py <generated SDK root> contradicts|agrees

Generated from the `streaming-extension-terminator` hand-written fixture, the SDK's
`reference.md` heading for `follow_build_log` is compared with the return the
method declares and with what iterating it yields, two events served by a local
HTTP server over real sockets. Exits 0 when the heading contradicts or agrees
with the method as the second argument expects.
"""

import inspect
import pathlib
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USAGE = "usage: stream_reference_heading.py <generated SDK root> contradicts|agrees"
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


class Events(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b'data: {"step": "lint", "passed": true}\n\ndata: {"step": "test", "passed": false}\n\ndata: [DONE]\n\n'
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 0), Events)
threading.Thread(target=server.serve_forever, daemon=True).start()
client = FernApi(base_url=f"http://127.0.0.1:{server.server_address[1]}")
method = client.follow_build_log
declared = inspect.signature(method).return_annotation
declared = f"typing.Iterator[{declared.__args__[0].__name__}]"
yielded = sorted({type(chunk).__name__ for chunk in method(build_id="b-1")})
heading = documented["follow_build_log"]
print(f"reference.md heads follow_build_log `-> {heading}`; the method declares `-> {declared}`; iterating yields {yielded}")
agrees = heading == declared and yielded == [declared.removeprefix("typing.Iterator[").removesuffix("]")]
if agrees != (sys.argv[2] == "agrees"):
    sys.exit(f"expected the heading to {sys.argv[2].replace('agrees', 'agree with')} the method, and it does not")
