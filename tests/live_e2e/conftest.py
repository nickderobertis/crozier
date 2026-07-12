"""Harness for the spec-driven live e2e: stand up a real OpenAPI mock server per
fixture and record the generated SDK driving every endpoint against it.

For each configured fixture this: runs the compiled `crozier` binary to generate
the SDK into a temp dir, writes a request-relaxed copy of the spec (see
`_relax.py`), boots a Prism mock server on it, then runs `_driver.py` in a
subprocess to exercise every endpoint and capture the recording. `test_live_e2e.py`
asserts over that recording, one test per endpoint.

Posture matches the runtime wire tests (`tests/runtime/`): missing tooling
(the `crozier` binary, Node/Prism, or the Python deps) is a **skip** locally and a
hard **failure** under `CI`, so the mock e2e can never silently no-op in the gate.
"""

from __future__ import annotations

import contextlib
import os
import re
import shutil
import socket
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

# The `client.<sub>.<method>` call that names the endpoint a reference snippet
# exercises (the client-construction line `client = FernApi(` never matches).
_CALL_RE = re.compile(r"^client\.\w+\.(\w+)", re.MULTILINE)

_ROOT = Path(__file__).resolve().parents[2]
_FIXTURES = _ROOT / "tests" / "fixtures"
_DRIVER = Path(__file__).parent / "_driver.py"
_RELAX = Path(__file__).parent / "_relax.py"

# Pinned so the mock server is reproducible across the matrix; CI installs this
# exact version and puts `prism` on PATH, locally we fall back to `npx`.
PRISM_PKG = "@stoplight/prism-cli@5.14.2"


@dataclass(frozen=True)
class Fixture:
    """A vendored corpus to drive live, plus the naming flags `crozier` is
    generated with — the runtime-behavior analog of the byte-diff `Corpus` in
    `tests/e2e.rs`. The generated package must be importable as `fern` for the
    `reference.md` snippets to run, so `package_name` is `fern`."""

    name: str
    package_name: str = "fern"
    project_name: str = "default_package_name"
    audiences: tuple[str, ...] = ()
    audience_strict: bool = False
    client_class_name: str | None = None
    extra_fields: str | None = None

    def generate_args(self, spec: Path, out: Path) -> list[str]:
        args = [
            "generate",
            "--spec",
            str(spec),
            "--output",
            str(out),
            "--package-name",
            self.package_name,
            "--project-name",
            self.project_name,
        ]
        for audience in self.audiences:
            args += ["--audience", audience]
        if self.audience_strict:
            args += ["--audience-strict"]
        if self.client_class_name:
            args += ["--client-class-name", self.client_class_name]
        if self.extra_fields:
            args += ["--extra-fields", self.extra_fields]
        return args


# The corpora driven live. Spec-driven, so this grows by one line as more fixtures
# gain a runnable SDK; `exhaustive` is the deliberately complicated seed (55 typed
# endpoints across 15 sub-clients). See tests/live_e2e/AGENTS.md.
FIXTURES: list[Fixture] = [
    Fixture(name="exhaustive"),
]


def committed_reference(fixture: Fixture) -> Path:
    return _FIXTURES / fixture.name / "expected" / "reference.md"


def reference_methods(fixture: Fixture) -> list[str]:
    """Ordered, de-duplicated endpoint method names from a fixture's committed
    `reference.md` — the endpoint catalog, resolved at collection time so each
    endpoint is its own reported test case."""
    text = committed_reference(fixture).read_text()
    return list(dict.fromkeys(_CALL_RE.findall(text)))


def pytest_generate_tests(metafunc):
    """Parametrize any test that asks for an `endpoint`: one case per fixture ×
    reference method, id'd as `<fixture>:<method>`."""
    if "endpoint" not in metafunc.fixturenames:
        return
    cases, ids = [], []
    for fixture in FIXTURES:
        for method in reference_methods(fixture):
            cases.append((fixture.name, method))
            ids.append(f"{fixture.name}:{method}")
    metafunc.parametrize("endpoint", cases, ids=ids)


def _crozier_bin() -> str | None:
    """The compiled binary under test. `CROZIER_BIN` (set by the justfile recipe)
    wins; otherwise fall back to a release/debug build in the workspace."""
    explicit = os.environ.get("CROZIER_BIN")
    if explicit and Path(explicit).exists():
        return explicit
    for profile in ("release", "debug"):
        candidate = _ROOT / "target" / profile / "crozier"
        if candidate.exists():
            return str(candidate)
    return shutil.which("crozier")


def _prism_command() -> list[str] | None:
    """`prism` if CI installed it globally, else `npx` to fetch the pinned package."""
    if shutil.which("prism"):
        return ["prism"]
    if shutil.which("npx"):
        return ["npx", "-y", PRISM_PKG]
    return None


def _require(tool: str, value):
    """Skip locally / fail under CI when a required tool is absent — the wire-test
    posture, so the suite never silently no-ops in the gate."""
    if value:
        return value
    message = f"live e2e needs {tool}, which is unavailable"
    if os.environ.get("CI"):
        pytest.fail(message)
    pytest.skip(message)


def _free_port() -> int:
    with contextlib.closing(socket.socket()) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _wait_until_listening(port: int, proc: subprocess.Popen, timeout: float = 60.0):
    """Block until Prism accepts connections, or fail with its log if it dies."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(
                f"prism exited early ({proc.returncode}):\n{proc.communicate()[1]}"
            )
        with contextlib.closing(socket.socket()) as sock:
            sock.settimeout(1.0)
            if sock.connect_ex(("127.0.0.1", port)) == 0:
                return
        time.sleep(0.5)
    raise RuntimeError(f"prism did not start listening on {port} within {timeout}s")


def _generate_sdk(crozier: str, fixture: Fixture, out: Path):
    spec = _FIXTURES / fixture.name / "openapi.yml"
    result = subprocess.run(
        [crozier, *fixture.generate_args(spec, out)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"crozier generate failed for {fixture.name}:\n{result.stdout}{result.stderr}"
        )


def _relax_spec(python: str, fixture: Fixture, dest: Path):
    spec = _FIXTURES / fixture.name / "openapi.yml"
    result = subprocess.run(
        [python, str(_RELAX), str(spec), str(dest)], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"relaxing {fixture.name} spec failed:\n{result.stdout}{result.stderr}"
        )


def _drive(python: str, sdk_src: Path, reference: Path, base_url: str) -> dict:
    import json

    result = subprocess.run(
        [python, str(_DRIVER)],
        env={
            **os.environ,
            "LIVE_SDK_SRC": str(sdk_src),
            "LIVE_REFERENCE": str(reference),
            "LIVE_BASE_URL": base_url,
        },
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"live driver failed for {reference}:\n{result.stdout}{result.stderr}"
        )
    return json.loads(result.stdout)


@pytest.fixture(scope="session")
def recordings(tmp_path_factory) -> dict[str, dict]:
    """Build every fixture's live recording once: generate the SDK, relax the spec,
    boot Prism, and drive all endpoints. Returns `{fixture_name: {method: obs}}`."""
    crozier = _require(
        "the crozier binary (set CROZIER_BIN or build it)", _crozier_bin()
    )
    prism_cmd = _require("Node/Prism", _prism_command())
    python = sys.executable

    servers: list[subprocess.Popen] = []
    out: dict[str, dict] = {}
    try:
        for fixture in FIXTURES:
            work = tmp_path_factory.mktemp(fixture.name)
            sdk = work / "sdk"
            _generate_sdk(crozier, fixture, sdk)
            relaxed = work / "relaxed.openapi.yml"
            _relax_spec(python, fixture, relaxed)

            port = _free_port()
            proc = subprocess.Popen(
                [*prism_cmd, "mock", "-p", str(port), "-h", "127.0.0.1", str(relaxed)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            servers.append(proc)
            _wait_until_listening(port, proc)

            # Drive crozier's own generated reference.md (its documented endpoints);
            # the committed expected/reference.md drives collection, and the coverage
            # test cross-checks the two so any drift is caught.
            out[fixture.name] = _drive(
                python, sdk / "src", sdk / "reference.md", f"http://127.0.0.1:{port}"
            )
        yield out
    finally:
        for proc in servers:
            proc.terminate()
            with contextlib.suppress(subprocess.TimeoutExpired):
                proc.wait(timeout=10)
