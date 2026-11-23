"""A header and a body property sharing one wire name keep their own values.

`docs/fern-measurements/bodies-responses/header-body-collision/` declares two
operations whose header and body property share a wire name. Both generated
SDKs rename the body argument (`run_action_request_kiln_token`); this records
each SDK through `_recorder.COLLISION_JOURNEYS`, whose journeys fail unless the
header argument travels as the header and the body argument in the JSON body,
and asserts the two recordings are the same. The Rust harness
(`sdk_env_crozier_matches_fern_runtime_behavior`) sets
`FERN_COLLISION_SDK_SRC` to the certified pair's committed tree and
`CROZIER_COLLISION_SDK_SRC` to crozier's SDK for the same document.
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
    src = os.environ.get(src_env)
    if not src:
        pytest.fail(f"{src_env} is not set")
    proc = subprocess.run(
        [sys.executable, RECORDER],
        env={**os.environ, "WIRE_SDK_SRC": src, "WIRE_JOURNEYS": "header-body-collision"},
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"recorder failed for {src}:\n{proc.stdout}{proc.stderr}"
    return json.loads(proc.stdout)


@pytest.fixture(scope="session")
def fern_collision():
    return _record("FERN_COLLISION_SDK_SRC")


@pytest.fixture(scope="session")
def crozier_collision():
    return _record("CROZIER_COLLISION_SDK_SRC")


def test_both_sdks_record_every_collision_journey(fern_collision, crozier_collision):
    assert set(fern_collision) == set(_recorder.COLLISION_JOURNEY_NAMES)
    assert set(crozier_collision) == set(_recorder.COLLISION_JOURNEY_NAMES)


@pytest.mark.parametrize("journey", _recorder.COLLISION_JOURNEY_NAMES)
def test_crozier_sends_each_value_where_fern_does(journey, fern_collision, crozier_collision):
    assert crozier_collision[journey] == fern_collision[journey]
