# Runtime (wire) tests

`wire_test.py` exercises a **generated** SDK at runtime — the compiled client's
behavior, not its source text (that is the byte-diff e2e's job). It is driven by
`tests/e2e.rs::generated_sdk_runtime_behavior`, which generates the `exhaustive`
SDK and runs this file against it in a cached venv (httpx + pydantic — the SDK's
only runtime deps), so it runs under `just test-e2e` / `just check`.

- **How it mocks the wire.** The generated client accepts an `httpx_client`; the
  driver injects one whose `httpx.MockTransport` captures the outgoing request and
  returns a scripted response. That is the in-process analog of Fern's own wire
  tests (which run a WireMock server in Docker and verify via its admin API) —
  crozier does not emit that Docker/`enable_wire_tests` tree, so we assert the same
  behaviors without it.
- **What a journey asserts.** URL/method construction, bearer-auth + `X-Crozier-*`
  SDK headers, request-body serialization (wire aliasing + `OMIT` filtering), query
  encoding, typed pydantic deserialization, and typed error raising — sync + async.
- **Adding a journey.** Add a function to `JOURNEYS`; it should `assert` and raise
  on failure. Keep to the SDK's own runtime deps (no pytest) so the venv stays
  thin. When a new generated shape lands, add a journey that *calls* it.
- **Skip vs fail.** Missing Python / venv / deps is a skip locally and a hard
  failure under `CI` (see `runtime_python_env`), matching the Python-validity
  check's posture. Assert on the crozier-real output (`X-Crozier-*` headers), not
  the Fern fixture's `X-Fern-*`.
