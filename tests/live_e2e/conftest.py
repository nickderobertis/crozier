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

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

# The `client.<sub>.<method>` call that names the endpoint a reference snippet
# exercises (the client-construction line `client = FernApi(` never matches). The
# captured `sub.method` is the endpoint key: real specs reuse a method name across
# sub-clients, so the sub-client is part of the identity.
_CALL_RE = re.compile(r"^client\.(\w+\.\w+)", re.MULTILINE)

_ROOT = Path(__file__).resolve().parents[2]
_FIXTURES = _ROOT / "tests" / "fixtures"
_DRIVER = Path(__file__).parent / "_driver.py"
_RELAX = Path(__file__).parent / "_relax.py"

# Pinned so the mock server is reproducible across the matrix. This is the single
# source of truth for the Prism version: the CI workflow greps the value out of the
# assignment below to `npm install -g` the same pin (see .github/workflows/ci.yml),
# and locally we fall back to `npx` with it. Keep the assignment start-of-line and
# double-quoted so the anchored grep keeps matching it.
PRISM_PKG = "@stoplight/prism-cli@5.14.2"


@dataclass(frozen=True)
class Fixture:
    """A corpus to drive live, plus the naming flags `crozier` is generated with —
    the runtime-behavior analog of the byte-diff `Corpus` in `tests/e2e.rs`. The
    generated package must be importable as `fern` for the `reference.md` snippets
    to run, so `package_name` is `fern`.

    `registered_source` selects the committed publisher-source registry; locally
    authored specifications live beside their goldens."""

    name: str
    package_name: str = "fern"
    project_name: str = "default_package_name"
    audiences: tuple[str, ...] = ()
    audience_strict: bool = False
    client_class_name: str | None = None
    extra_fields: str | None = None
    registered_source: bool = False
    # Whether crozier's client *grouping* matches Fern's, so its generated
    # `reference.md` endpoint keys (`sub_client.method`) equal the committed golden's.
    # True for a byte-matched corpus: each Fern-documented
    # endpoint is cross-checked one-per-test and coverage is asserted key-for-key.
    # False for a partially-matched corpus (bunq groups sub-clients differently —
    # see docs/matching.md): the runtime sweep instead proves crozier's *own*
    # documented endpoints round-trip, and structural parity is left to the byte-diff
    # gate rather than re-asserted here against a grouping crozier does not yet match.
    strict_coverage: bool = True

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


# Registered publisher APIs driven live: Qakka exercises binary requests,
# Apideck CRM provides a smaller resource API, and bunq stresses the pipeline
# at scale. The committed references supply endpoint counts.
FIXTURES: list[Fixture] = [
    Fixture(
        name="apache.org-qakka",
        registered_source=True,
    ),
    Fixture(
        name="apideck.com-crm",
        registered_source=True,
    ),
    Fixture(
        name="bunq.com",
        registered_source=True,
        # crozier does not yet reproduce bunq's tag-based sub-client grouping, so its
        # generated reference keys diverge from the golden's. The runtime sweep still
        # drives crozier's own reference and asserts every documented endpoint
        # round-trips (see test_live_e2e.py); the structural gap is the byte-diff
        # test's concern (docs/matching.md), not this suite's.
        strict_coverage=False,
    ),
]


def committed_reference(fixture: Fixture) -> Path:
    return _FIXTURES / fixture.name / "expected" / "reference.md"


def reference_methods(fixture: Fixture) -> list[str]:
    """Ordered, de-duplicated `sub.method` endpoint keys from a fixture's committed
    `reference.md` — the endpoint catalog, resolved at collection time so each
    endpoint is its own reported test case."""
    text = committed_reference(fixture).read_text(encoding="utf-8")
    return list(dict.fromkeys(_CALL_RE.findall(text)))


def pytest_generate_tests(metafunc):
    """Parametrize any test that asks for an `endpoint`: one case per fixture ×
    reference method, id'd as `<fixture>:<method>`."""
    if "endpoint" not in metafunc.fixturenames:
        return
    cases, ids = [], []
    # Only strict-coverage fixtures get one-test-per-endpoint keyed off the committed
    # golden: a partial corpus's generated reference keys don't line up with it (its
    # sub-client grouping differs), so it is asserted in aggregate over its own sweep.
    for fixture in FIXTURES:
        if not fixture.strict_coverage:
            continue
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


def _spec_path(fixture: Fixture, work: Path) -> Path:
    """Read the committed source; corpus URLs are rebuild provenance only."""
    if not fixture.registered_source:
        return _FIXTURES / fixture.name / "openapi.yml"
    result = subprocess.run(
        [sys.executable, str(_FIXTURES.parent.parent / "scripts/corpus_sources.py"),
         "prepare", "--fixture", fixture.name, "--output", str(work / "source")],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return Path(result.stdout.strip())


def _generate_sdk(crozier: str, fixture: Fixture, spec: Path, out: Path):
    result = subprocess.run(
        [crozier, *fixture.generate_args(spec, out)],
        capture_output=True,
        text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"crozier generate failed for {fixture.name}:\n{result.stdout}{result.stderr}"
        )


def _relax_spec(python: str, fixture: Fixture, spec: Path, dest: Path):
    result = subprocess.run(
        [python, str(_RELAX), str(spec), str(dest)], capture_output=True, text=True, encoding="utf-8"
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
        text=True, encoding="utf-8",
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
            spec = _spec_path(fixture, work)
            sdk = work / "sdk"
            _generate_sdk(crozier, fixture, spec, sdk)
            relaxed = work / "relaxed.openapi.yml"
            _relax_spec(python, fixture, spec, relaxed)

            port = _free_port()
            # `-d --seed` (dynamic, seeded): generate each response from its schema
            # rather than echoing the spec's committed `example`. Real specs carry
            # examples that violate their own declared types (e.g. a `format: date`
            # field whose example is a full datetime), which the SDK correctly
            # rejects; schema-generated data respects the declared types, and the
            # fixed seed keeps it reproducible across the matrix.
            proc = subprocess.Popen(
                [
                    *prism_cmd,
                    "mock",
                    "-p",
                    str(port),
                    "-h",
                    "127.0.0.1",
                    "-d",
                    "--seed",
                    "1",
                    str(relaxed),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True, encoding="utf-8",
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
