"""Differential runtime ("wire") tests for a crozier-generated Python SDK.

Byte-matching Fern proves the generated *source* is right and `compileall` proves
it compiles; neither proves the compiled client issues the right HTTP request or
parses the response. Rather than hand-author the expected behavior, this derives
it from Fern: `_recorder.record` drives an SDK through an injected
`httpx.MockTransport` and records what each journey does, and this suite runs it
against **both** the committed Fern fixture SDK and the crozier-generated SDK and
asserts — per journey — that the recordings are identical. The only allowed
difference is the deliberate SDK-identity branding (`X-Crozier-*` vs `X-Fern-*`),
which `_recorder` folds to a common prefix on both sides — the runtime analog of
the byte-diff's `tests/e2e.rs::normalize_sdk_headers`.

The two SDKs are both named `fern` and cannot coexist in one process, so each
recording is produced in its own subprocess (`_recorder` as `__main__`). The Rust
e2e harness (`tests/e2e.rs::crozier_matches_fern_runtime_behavior`) generates the
crozier SDK, prepares the venv, and runs this suite with `CROZIER_SDK_SRC` /
`FERN_SDK_SRC` pointing at the two SDKs' `src/` directories.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))

import _recorder  # noqa: E402  (local helper; on sys.path above)

RECORDER = str(_HERE / "_recorder.py")


def _record(src_env):
    """Record a generated SDK's behavior in a subprocess. `src_env` names the
    environment variable holding its `src/` path (set by the Rust harness)."""
    src = os.environ.get(src_env)
    if not src:
        pytest.skip(f"{src_env} is not set")
    proc = subprocess.run(
        [sys.executable, RECORDER],
        env={**os.environ, "WIRE_SDK_SRC": src},
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"recorder failed for {src}:\n{proc.stdout}{proc.stderr}"
    return json.loads(proc.stdout)


@pytest.fixture(scope="session")
def fern_recording():
    return _record("FERN_SDK_SRC")


@pytest.fixture(scope="session")
def crozier_recording():
    return _record("CROZIER_SDK_SRC")


def test_both_sdks_record_every_journey(fern_recording, crozier_recording):
    """Guard against a trivially-empty match: both recordings must cover exactly
    the declared journeys."""
    assert set(fern_recording) == set(_recorder.JOURNEY_NAMES)
    assert set(crozier_recording) == set(_recorder.JOURNEY_NAMES)


@pytest.mark.parametrize("journey", _recorder.JOURNEY_NAMES)
def test_crozier_matches_fern(journey, fern_recording, crozier_recording):
    """crozier's client behaves identically to Fern's for this journey (request
    construction and response/error handling), beyond the normalized SDK-identity
    headers."""
    assert crozier_recording[journey] == fern_recording[journey]
