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

import pytest

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
    if observation.get("skipped"):
        # A provable mock-infrastructure failure (Prism 5xx, or a response that drops
        # its own schema-required field) — the SDK is not under test here. See
        # `_driver._mock_side_reason`. Skipped, not passed, so the count stays honest.
        pytest.skip(f"{fixture_name}:{method} mock-side: {observation['reason']}")
    assert observation["ok"], (
        f"{fixture_name}:{method} did not round-trip: {observation.get('error')}"
    )


def test_covers_every_reference_endpoint(recordings):
    """The live sweep hit exactly the endpoints the committed reference documents —
    no silently dropped or renamed method between crozier's output and the fixture.
    Strict-coverage fixtures only: a partial corpus groups its sub-clients
    differently from the golden, so its keys legitimately diverge (asserted instead
    by `test_partial_corpus_round_trips`)."""
    for fixture in FIXTURES:
        if not fixture.strict_coverage:
            continue
        expected = set(reference_methods(fixture))
        exercised = set(recordings[fixture.name])
        assert exercised == expected, (
            f"{fixture.name}: live sweep covered {sorted(exercised)} but the reference "
            f"documents {sorted(expected)} (missing={sorted(expected - exercised)}, "
            f"extra={sorted(exercised - expected)})"
        )


def test_partial_corpus_round_trips(recordings):
    """A partially-matched corpus (`strict_coverage=False`) still proves its runtime
    contract: crozier's *own* generated reference is driven end to end, and every
    documented endpoint must either round-trip cleanly or be a classified mock-side
    skip — never a real failure. A count floor guards against a silent collapse where
    crozier drops most of the surface; structural parity with Fern is the byte-diff
    gate's job, not this one's."""
    for fixture in FIXTURES:
        if fixture.strict_coverage:
            continue
        recording = recordings[fixture.name]
        failures = {
            endpoint: obs.get("error")
            for endpoint, obs in recording.items()
            if not obs.get("ok") and not obs.get("skipped")
        }
        assert not failures, f"{fixture.name}: endpoints did not round-trip: {failures}"
        # No silent collapse: crozier must document ~all the operations the golden
        # does (same operations, only grouped differently), even if a handful of
        # keys collide under its grouping. Count, not key identity, is the guard.
        documented = len(reference_methods(fixture))
        assert len(recording) >= 0.9 * documented, (
            f"{fixture.name}: drove only {len(recording)} endpoints but the golden "
            f"documents {documented} — crozier may be dropping endpoints"
        )


def test_partial_corpus_exercises_the_fern_5_20_parsing_error_classifier(recordings):
    """The real Bunq/Prism journey covers Fern 5.20's ParsingError wrapper; only
    missing-required-field validation causes become mock-side skips."""
    recording = recordings["bunq.com"]
    reasons = [obs["reason"] for obs in recording.values() if obs.get("skipped")]
    assert reasons, "Bunq's seeded Prism responses should exercise the skip classifier"
    assert all(
        reason.startswith("mock response omitted schema-required field(s):")
        or reason.startswith("prism 5")
        for reason in reasons
    ), reasons


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
