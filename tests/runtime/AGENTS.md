# Runtime (wire) tests

`wire_test.py` records a **generated** SDK's runtime behavior — the compiled
client's behavior, not its source text (that is the byte-diff e2e's job). It is
driven by `tests/e2e.rs::crozier_matches_fern_runtime_behavior`, which runs it
against **both** the committed Fern fixture SDK (`exhaustive/expected/src`, real
runnable Fern output) and the crozier-generated SDK and asserts the two
recordings are **identical**. So the expected behavior is *derived from Fern*,
not authored here — any divergence beyond the normalized SDK-identity headers
fails. It runs in a cached venv (httpx + pydantic — the SDK's only runtime deps)
under `just test-e2e` / `just check`.

- **How it mocks the wire.** The generated client accepts an `httpx_client`; the
  recorder injects one whose `httpx.MockTransport` captures the outgoing request
  and returns a scripted response. That is the in-process analog of Fern's own
  wire tests (a WireMock server in Docker, verified via its admin API) — crozier
  does not emit that Docker/`enable_wire_tests` tree, so we assert the same
  behaviors without it.
- **What a journey records.** Per journey: the request (method, URL, canonical
  headers, serialized body) and the outcome (the response model dumped to a dict,
  or the typed error's class/status/body). Between them the journeys cover
  request/URL construction, bearer auth + SDK headers, body aliasing + `OMIT`
  filtering, query encoding, typed deserialization, and typed error raising —
  sync + async.
- **The only allowed difference** is the deliberate SDK-identity branding
  (`X-Crozier-*` vs `X-Fern-*`), canonicalized on both sides by
  `_canonical_headers` exactly as `tests/e2e.rs::normalize_sdk_headers` does for
  the byte-diff. Do not add other normalizations to hide a real behavioral
  divergence — fix the generator instead.
- **Adding a journey.** Add a function to `JOURNEYS` that performs a call and
  returns its observation dict; it must raise on a broken structural contract
  (e.g. a declared 4xx that fails to raise) so it can never record nothing and
  match trivially. Keep to the SDK's own runtime deps (no pytest). When a new
  generated shape lands, add a journey that *calls* it — the Fern fixture supplies
  the expected behavior for free.
- **Skip vs fail.** Missing Python / venv / deps is a skip locally and a hard
  failure under `CI` (see `runtime_python_env`), matching the Python-validity
  check's posture.
