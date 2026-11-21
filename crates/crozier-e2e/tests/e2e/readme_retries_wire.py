"""Assert a generated SDK retries exactly the status codes its README's Retries section lists.

Usage: readme_retries_wire.py README IMPORT_ROOT PACKAGE CLIENT. README is the
generated README.md; IMPORT_ROOT is put on sys.path so PACKAGE imports, and
CLIENT names its root client class. A local HTTP server answers every request
with one scripted status (and `Retry-After-Ms: 1`, so a retry waits a
millisecond); each status is requested once through the sync and the async
`lamps.get_lamp` with `max_retries=1`, and must be attempted twice exactly when
the README lists it (a `5XX` entry lists every 5xx status). Exit 0 prints one
success line; exit 1 names each status whose attempts disagree with the README;
exit 2 reports invalid CLI arguments or a README with no readable Retries list.
"""

import argparse
import asyncio
import http.server
import importlib
import re
import sys
import threading
from pathlib import Path

LEAD = "A request is deemed retryable when any of the following HTTP status codes is returned:"
ENTRY = re.compile(r"^- \[([0-9]{3}|[1-5]XX)\]\(https://developer\.mozilla\.org/[^)]*\) \(.+\)$")
# Every 4xx and 5xx class a client meets: the listed ones and unlisted neighbours.
STATUSES = (400, 401, 403, 404, 407, 408, 409, 410, 422, 425, 429, 500, 501, 502, 503, 504, 599)


class Unreadable(ValueError):
    """The README has no Retries list this script reads."""


def listed_codes(readme: str) -> list[str]:
    """The status-code entries the README's Retries section lists, in order."""
    section = readme.split("\n### Retries\n", 1)
    if len(section) != 2:
        raise Unreadable("the README has no `### Retries` section")
    body = section[1].split("\n### ", 1)[0].splitlines()
    if LEAD not in body:
        raise Unreadable(f"the Retries section does not say {LEAD!r}")
    codes = []
    for line in body[body.index(LEAD) + 1 :]:
        match = ENTRY.match(line)
        if match is None:
            break
        codes.append(match.group(1))
    if not codes:
        raise Unreadable("the Retries section lists no status code")
    return codes


def is_listed(status: int, codes: list[str]) -> bool:
    return str(status) in codes or f"{status // 100}XX" in codes


def serve(hits: list[int], status: list[int]) -> http.server.HTTPServer:
    class Scripted(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            hits.append(status[0])
            body = b'{"message": "scripted"}'
            self.send_response(status[0])
            self.send_header("Content-Type", "application/json")
            self.send_header("Retry-After-Ms", "1")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Scripted)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path)
    parser.add_argument("import_root", type=Path)
    parser.add_argument("package")
    parser.add_argument("client")
    args = parser.parse_args()
    if not (args.import_root / args.package / "__init__.py").is_file():
        parser.error(f"import_root must contain the generated {args.package} package")
    try:
        codes = listed_codes(args.readme.read_text(encoding="utf-8"))
    except (OSError, Unreadable) as error:
        parser.error(f"{args.readme}: {error}")
    sys.path.insert(0, str(args.import_root.resolve()))
    sdk = importlib.import_module(args.package)
    api_error = importlib.import_module(f"{args.package}.core.api_error").ApiError
    request_options = importlib.import_module(f"{args.package}.core.request_options").RequestOptions
    hits: list[int] = []
    status = [0]
    server = serve(hits, status)
    base_url = f"http://127.0.0.1:{server.server_port}"
    sync_client = getattr(sdk, args.client)(base_url=base_url)
    async_client = getattr(sdk, f"Async{args.client}")(base_url=base_url)
    options = request_options(max_retries=1)

    def sync_call() -> None:
        # llmlint: ignore[async_typed_clients_at_boundaries] The synchronous client is half of the generated SDK's public surface under test, the one the README's Retries example calls; async_call below drives the async half, and the SDK, not this script, owns the HTTP boundary.
        sync_client.lamps.get_lamp("lamp-1", request_options=options)

    def async_call() -> None:
        asyncio.run(async_client.lamps.get_lamp("lamp-1", request_options=options))

    wrong = []
    for name, call in (("sync", sync_call), ("async", async_call)):
        for code in STATUSES:
            status[0] = code
            before = len(hits)
            try:
                call()
            except api_error as error:
                if error.status_code != code:
                    wrong.append(f"{name} {code}: raised for status {error.status_code}")
                    continue
            else:
                wrong.append(f"{name} {code}: did not raise")
                continue
            attempts = len(hits) - before
            expected = 2 if is_listed(code, codes) else 1
            if attempts != expected:
                wrong.append(f"{name} {code}: {attempts} attempt(s), the README implies {expected}")
    server.shutdown()
    if wrong:
        print(f"the README lists {', '.join(codes)}; the client disagrees:", file=sys.stderr)
        print("\n".join(wrong), file=sys.stderr)
        return 1
    retried = sum(is_listed(code, codes) for code in STATUSES)
    print(f"{retried} of {len(STATUSES)} status(es) retried as the README lists, sync and async")
    return 0


if __name__ == "__main__":
    sys.exit(main())
