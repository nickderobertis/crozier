"""A header and a body property sharing one wire name keep their own values.

`docs/fern-measurements/bodies-responses/header-body-collision/` declares two
operations whose header and body property share a wire name. Both generated
SDKs rename the body argument (`run_action_request_kiln_token`); this records
each SDK through `_recorder.COLLISION_JOURNEYS`. Where the body is inlined, both
send the header argument as the header and the body argument in the JSON body,
and the recordings are the same. Where the body is a shared component, the
certified pair sends the header's value under the body key, the catalogued
`body-query-parameter-value` departure, and crozier sends the body argument. The Rust harness
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


SHARED = "shared_body_header_collision"


@pytest.mark.parametrize("journey", [name for name in _recorder.COLLISION_JOURNEY_NAMES if name != SHARED])
def test_crozier_sends_each_value_where_fern_does(journey, fern_collision, crozier_collision):
    assert crozier_collision[journey] == fern_collision[journey]


def _sent(record):
    return record["headers"].get("idempotency-key"), record["body"].get("idempotency_key")


@pytest.mark.parametrize("client", ["sync", "async"])
def test_crozier_sends_a_shared_bodys_value_beside_the_header(client, crozier_collision):
    """crozier's SDK sends the header argument as the header and the renamed body
    argument in the JSON body."""
    record = crozier_collision[SHARED][client]
    assert _sent(record) == (_recorder.HEADER_VALUE, _recorder.BODY_VALUE)


@pytest.mark.parametrize("client", ["sync", "async"])
def test_the_certified_pair_sends_the_header_value_as_the_body(client, fern_collision, crozier_collision):
    """The `body-query-parameter-value` departure's executed evidence: the
    certified pair's SDK drops the body argument and sends the header's value
    under the body key, while every other part of the request is crozier's."""
    fern = fern_collision[SHARED][client]
    assert _sent(fern) == (_recorder.HEADER_VALUE, _recorder.HEADER_VALUE)
    crozier = crozier_collision[SHARED][client]

    def rest(record):
        """The request beside its body, whose length alone differs."""
        headers = {name: value for name, value in record["headers"].items() if name != "content-length"}
        return {**record, "body": None, "headers": headers}

    assert rest(fern) == rest(crozier)
    assert {**fern["body"], "idempotency_key": None} == {**crozier["body"], "idempotency_key": None}
