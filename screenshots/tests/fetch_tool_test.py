# llmlint: ignore-file[shell_test_tiers_stay_split] It drives curl against a loopback server on 127.0.0.1 only: every lane carries curl, and nothing here reaches a network.
"""`fetch-tool.sh`, the visual-docs capture's download of its pinned tools, run against a loopback
server that answers each request the way a case scripts: a transfer cut off part-way, a reset
connection, an HTTP error, or the archive itself. The release host is the one thing doubled."""

from __future__ import annotations

import os
import shutil
import socket
import struct
import subprocess
import threading
import time
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


class Body(Enum):
    """What the release host sends for the archive."""

    WHOLE = "whole"
    PARTIAL = "partial"  # headers and a part of the body, then the connection closes: curl exit 18
    RESET = "reset"  # the connection reset before any answer: curl exit 56


@dataclass(frozen=True)
class Status:
    """An HTTP error answer."""

    code: int


Answer = Body | Status


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
                    case Body.PARTIAL:
                        self.send_response(200)
                        self.send_header("Content-Length", str(len(ARCHIVE)))
                        self.end_headers()
                        self.wfile.write(ARCHIVE[:40])
                        self.wfile.flush()
                        self.close_connection = True
                    case Body.RESET:
                        # SO_LINGER 0: close with a RST, the dropped connection curl reports as exit 56.
                        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0))
                        self.connection.close()
                        self.close_connection = True
                    case Status(code=code):
                        self.send_error(code)
                    case Body.WHOLE:
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
    host = release([Body.PARTIAL, Body.WHOLE])
    plain = subprocess.run(
        ["curl", "-fsSL", "-o", str(tmp_path / "plain.tgz"), host.url], capture_output=True, text=True, check=False
    )
    assert plain.returncode == 18, plain.stderr


def test_a_dropped_and_a_reset_transfer_are_retried_into_the_whole_archive(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Body.PARTIAL, Body.RESET, Body.WHOLE])
    out = tmp_path / "freeze.tgz"
    result = fetch(host.url, out)
    assert result.returncode == 0, result.stderr
    assert out.read_bytes() == ARCHIVE
    assert host.served == 3
    assert result.stderr.count("\n") == 1, "one line for a recovered download"
    assert (
        "downloaded on attempt 3 after transient failures (attempt 1/4: curl exit 18, then 0s; attempt 2/4: curl exit 56, then 0s)"
        in result.stderr
    )
    assert not (tmp_path / "freeze.tgz.part").exists()


def test_a_server_error_is_retried_and_its_recovery_kept(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Status(503), Body.WHOLE])
    out = tmp_path / "ruff.tgz"
    result = fetch(host.url, out)
    assert result.returncode == 0, result.stderr
    assert out.read_bytes() == ARCHIVE
    assert "downloaded on attempt 2 after transient failures (attempt 1/4: curl exit 22, then 0s)" in result.stderr


def test_a_failure_that_outlasts_the_retries_names_the_url_and_curls_last_error(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Body.RESET])
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
    result = fetch("--config=/etc/passwd", tmp_path / "x")
    assert result.returncode == 2
    assert "'--config=/etc/passwd' is not an http(s) URL" in result.stderr
    for name, value in (("FETCH_TOOL_ATTEMPTS", "many"), ("FETCH_TOOL_ATTEMPTS", "0"), ("FETCH_TOOL_DELAY", "61")):
        result = fetch("http://127.0.0.1:9/x", tmp_path / "x", **{name: value})
        assert result.returncode == 2, (name, value)
        assert f"{name} must be a whole number from" in result.stderr
        assert "set it within that range, or unset it for the default" in result.stderr


def test_a_leading_zero_is_read_as_decimal(release: Callable[[list[Answer]], Release], tmp_path: Path) -> None:
    host = release([Body.RESET, Body.WHOLE])
    result = fetch(host.url, tmp_path / "freeze.tgz", FETCH_TOOL_DELAY="00", FETCH_TOOL_ATTEMPTS="08")
    assert result.returncode == 0, result.stderr
    assert "attempt 1/8: curl exit 56" in result.stderr


def test_an_archive_it_cannot_put_in_place_says_so_and_what_to_do(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Body.WHOLE])
    blocked = tmp_path / "freeze.tgz"
    blocked.mkdir()
    (blocked / "keep").write_text("a directory where the archive belongs\n", encoding="utf-8")
    result = fetch(host.url, blocked)
    assert result.returncode == 2
    assert f"fetch-tool: {blocked} is a directory, so the archive from {host.url} cannot be written" in result.stderr
    assert host.served == 0, "nothing is downloaded that could not be kept"


@pytest.mark.parametrize("code", [408, 429, 500, 502])
def test_an_answer_that_asks_for_a_retry_is_retried(
    release: Callable[[list[Answer]], Release], tmp_path: Path, code: int
) -> None:
    host = release([Status(code), Body.WHOLE])
    out = tmp_path / "freeze.tgz"
    result = fetch(host.url, out)
    assert result.returncode == 0, result.stderr
    assert out.read_bytes() == ARCHIVE
    assert "downloaded on attempt 2 after transient failures (attempt 1/4: curl exit 22" in result.stderr


def test_a_refused_connection_is_retried(tmp_path: Path) -> None:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    result = fetch(f"http://127.0.0.1:{port}/freeze.tgz", tmp_path / "freeze.tgz", FETCH_TOOL_ATTEMPTS="2")
    assert result.returncode == 1
    assert "(earlier: attempt 1/2: curl exit 7, then 0s)" in result.stderr
    assert "after 2 attempt(s): curl exit 7" in result.stderr


def test_each_retry_waits_longer_than_the_last(release: Callable[[list[Answer]], Release], tmp_path: Path) -> None:
    host = release([Body.RESET, Body.RESET, Body.WHOLE])
    started = time.monotonic()
    result = fetch(host.url, tmp_path / "freeze.tgz", FETCH_TOOL_DELAY="1")
    assert result.returncode == 0, result.stderr
    assert "(attempt 1/4: curl exit 56, then 1s; attempt 2/4: curl exit 56, then 2s)" in result.stderr
    assert time.monotonic() - started >= 3, "the waits were 1 s and then 2 s"


def failing(tmp_path: Path, name: str) -> dict[str, str]:
    """A PATH whose `name` fails as a full or read-only filesystem fails it; every other tool is the real one."""
    bin_dir = tmp_path / f"failing-{name}"
    bin_dir.mkdir()
    stand_in = bin_dir / name
    stand_in.write_text(f"#!/bin/sh\necho '{name}: Read-only file system' >&2\nexit 1\n", encoding="utf-8")
    stand_in.chmod(0o755)
    assert shutil.which("curl")
    return {"PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}


def test_an_archive_it_cannot_move_into_place_says_so_and_what_to_do(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Body.WHOLE])
    out = tmp_path / "freeze.tgz"
    result = fetch(host.url, out, **failing(tmp_path, "mv"))
    assert result.returncode == 1
    assert f"fetch-tool: downloaded {host.url} but could not move it to {out}" in result.stderr
    assert not out.exists()


def test_a_partial_download_it_cannot_remove_says_so_and_keeps_the_transfer_error(
    release: Callable[[list[Answer]], Release], tmp_path: Path
) -> None:
    host = release([Body.PARTIAL])
    result = fetch(host.url, tmp_path / "freeze.tgz", **failing(tmp_path, "rm"))
    assert result.returncode == 1
    assert f"could not remove the partial download {tmp_path / 'freeze.tgz.part'} (curl exit 18" in result.stderr
