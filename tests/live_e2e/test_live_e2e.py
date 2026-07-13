"""Spec-driven live e2e: every generated endpoint, driven against a real OpenAPI
mock server, returns a value of its declared type.

Byte-matching Fern proves the generated *source* is right and the wire tests
(`tests/runtime/`) prove the client's request/response *shaping* matches Fern; this
proves the compiled client actually round-trips over HTTP against a spec-shaped
server — request sent, response received, deserialized into the method's promised
return type — for **every** endpoint the SDK documents, not a hand-picked few. The
endpoint list and the example arguments come from the SDK's own generated
`reference.md`, so the coverage tracks the spec and this suite extends to more
fixtures by adding one line to `conftest.FIXTURES`.

The heavy lifting (generate, relax the spec, boot Prism, drive the endpoints) is
the session-scoped `recordings` fixture in `conftest.py`; these tests assert over
its recording, one reported case per endpoint.
"""

from conftest import FIXTURES, reference_methods


def test_endpoint_returns_typed_response(recordings, endpoint):
    """The generated example call for this endpoint completes against the live mock
    and yields a value matching the SDK method's declared return type."""
    fixture_name, method = endpoint
    recording = recordings[fixture_name]
    assert method in recording, (
        f"{method} was not exercised — crozier's generated reference.md omits an "
        f"endpoint the committed fixture documents"
    )
    observation = recording[method]
    assert observation["ok"], (
        f"{fixture_name}:{method} did not round-trip: {observation.get('error')}"
    )


def test_covers_every_reference_endpoint(recordings):
    """The live sweep hit exactly the endpoints the committed reference documents —
    no silently dropped or renamed method between crozier's output and the fixture."""
    for fixture in FIXTURES:
        expected = set(reference_methods(fixture))
        exercised = set(recordings[fixture.name])
        assert exercised == expected, (
            f"{fixture.name}: live sweep covered {sorted(exercised)} but the reference "
            f"documents {sorted(expected)} (missing={sorted(expected - exercised)}, "
            f"extra={sorted(exercised - expected)})"
        )


def test_response_models_are_deserialized(recordings):
    """Guard against a trivially-passing sweep: a complicated corpus must return real
    pydantic response models, not merely primitives — proof deserialization ran."""
    for fixture in FIXTURES:
        models = sorted(
            m for m, obs in recordings[fixture.name].items() if obs.get("model")
        )
        assert models, (
            f"{fixture.name}: no endpoint returned a pydantic model; response "
            f"deserialization may have degraded to raw JSON"
        )
