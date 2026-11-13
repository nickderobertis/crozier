# llmlint: ignore-file[shell_test_tiers_stay_split] It drives curl against a loopback server on 127.0.0.1 only: every lane carries curl, and nothing here reaches a network.
"""`fetch-tool.sh`, the visual-docs capture's download of its pinned tools, run against a loopback
server that answers each request the way a case scripts: a transfer cut off part-way, a reset
connection, an HTTP error, or the archive itself. The release host is the one thing doubled."""

from __future__ import annotations

import os
import socket
import struct
import subprocess
import threading
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from enum import Enum
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "screenshots" / "fetch-tool.sh"
ARCHIVE = b"pinned tool archive\n" * 64

pytestmark = pytest.mark.skipif(os.name == "nt", reason="the capture runs on the Linux lint lane")


class Cut(Enum):
    """A transfer the release host breaks off."""

    PARTIAL = "partial"  # headers and a part of the body, then the connection closes: curl exit 18
    RESET = "reset"  # the connection reset before any answer: curl exit 56


@dataclass(frozen=True)
class Status:
    """An HTTP error answer."""

    code: int


ARCHIVE_ANSWER = "archive"
Answer = Cut | Status | str  # str: ARCHIVE_ANSWER, the whole archive


class Release:
    """A release host whose successive answers are scripted, recording how many it gave."""

    def __init__(self, answers: list[Answer]) -> None:
        self.answers = answers
        self.served = 0
        release = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                answer = release.answers[min(release.served, len(release.answers) - 1)]
                release.served += 1
                match answer:
                    case Cut.PARTIAL:
                        self.send_response(200)
                        self.send_header("Content-Length", str(len(ARCHIVE)))
                        self.end_headers()
                        self.wfile.write(ARCHIVE[:40])
                        self.wfile.flush()
                        self.close_connection = True
                    case Cut.RESET:
                        # SO_LINGER 0: close with a RST, the dropped connection curl reports as exit 56.
                        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0))
                        self.connection.close()
                        self.close_connection = True
                    case Status(code=code):
                        self.send_error(code)
                    case _:
                        self.send_response(200)
                        self.send_header("Content-Length", str(len(ARCHIVE)))
                        self.end_headers()
                        self.wfile.write(ARCHIVE)

            def log_message(self, format: str, *args: object) -> None:
                return

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}/freeze_0.2.2_Linux_x86_64.tar.gz"


@pytest.fixture
def release() -> Iterator[Callable[[list[Answer]], Release]]:
    servers: list[Release] = []

    def start(answers: list[Answer]) -> Release:
        host = Release(answers)
        threading.Thread(target=host.server.serve_forever, daemon=True).start()
        servers.append(host)
        return host

    yield start
    for host in servers:
        host.server.shutdown()
        host.server.server_close()


def fetch(url: str, out: Path, **env: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(SCRIPT), url, str(out)],
        env={**os.environ, "FETCH_TOOL_DELAY": "0", "no_proxy": "127.0.0.1", **env},
        capture_output=True,
        text=True,
        check=False,
    )


def test_one_unretried_attempt_is_what_a_dropped_transfer_used_to_fail(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Cut.PARTIAL, ARCHIVE_ANSWER])
    plain = subprocess.run(
        ["curl", "-fsSL", "-o", str(tmp_path / "plain.tgz"), host.url], capture_output=True, text=True, check=False
    )
    assert plain.returncode == 18, plain.stderr


def test_a_dropped_and_a_reset_transfer_are_retried_into_the_whole_archive(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Cut.PARTIAL, Cut.RESET, ARCHIVE_ANSWER])
    out = tmp_path / "freeze.tgz"
    result = fetch(host.url, out)
    assert result.returncode == 0, result.stderr
    assert out.read_bytes() == ARCHIVE
    assert host.served == 3
    assert "attempt 1/4 failed (curl exit 18" in result.stderr
    assert "attempt 2/4 failed (curl exit 56" in result.stderr
    assert not (tmp_path / "freeze.tgz.part").exists()


def test_a_server_error_is_retried_and_its_recovery_kept(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Status(503), ARCHIVE_ANSWER])
    out = tmp_path / "ruff.tgz"
    result = fetch(host.url, out)
    assert result.returncode == 0, result.stderr
    assert out.read_bytes() == ARCHIVE
    assert "error: 503" in result.stderr


def test_a_failure_that_outlasts_the_retries_names_the_url_and_curls_last_error(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Cut.RESET])
    out = tmp_path / "freeze.tgz"
    result = fetch(host.url, out, FETCH_TOOL_ATTEMPTS="3")
    assert result.returncode == 1
    assert host.served == 3
    assert f"fetch-tool: could not download {host.url} after 3 attempt(s): curl exit 56" in result.stderr
    assert not out.exists(), "a failed download leaves no archive to install"


def test_a_missing_release_fails_at_once(release: Callable[[list[Answer]], Release], tmp_path: Path) -> None:
    host = release([Status(404)])
    result = fetch(host.url, tmp_path / "freeze.tgz")
    assert result.returncode == 1
    assert host.served == 1, "a 404 is no transient failure"
    assert "after 1 attempt(s): curl exit 22" in result.stderr


def test_it_refuses_a_call_it_does_not_take(tmp_path: Path) -> None:
    result = subprocess.run(["bash", str(SCRIPT), "only-a-url"], capture_output=True, text=True, check=False)
    assert result.returncode == 2
    assert "usage: screenshots/fetch-tool.sh URL OUT" in result.stderr
    for name, value in (("FETCH_TOOL_ATTEMPTS", "many"), ("FETCH_TOOL_ATTEMPTS", "0"), ("FETCH_TOOL_DELAY", "61")):
        result = fetch("http://127.0.0.1:9/x", tmp_path / "x", **{name: value})
        assert result.returncode == 2, (name, value)
        assert f"{name} must be a whole number from" in result.stderr


def test_a_leading_zero_is_read_as_decimal(release: Callable[[list[Answer]], Release], tmp_path: Path) -> None:
    host = release([Cut.RESET, ARCHIVE_ANSWER])
    result = fetch(host.url, tmp_path / "freeze.tgz", FETCH_TOOL_DELAY="00", FETCH_TOOL_ATTEMPTS="08")
    assert result.returncode == 0, result.stderr
    assert "attempt 1/8 failed" in result.stderr


def test_an_archive_it_cannot_put_in_place_says_so_and_what_to_do(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([ARCHIVE_ANSWER])
    blocked = tmp_path / "freeze.tgz"
    blocked.mkdir()
    (blocked / "keep").write_text("a directory where the archive belongs\n", encoding="utf-8")
    result = fetch(host.url, blocked)
    assert result.returncode == 2
    assert f"fetch-tool: {blocked} is a directory, so the archive from {host.url} cannot be written" in result.stderr
    assert host.served == 0, "nothing is downloaded that could not be kept"
