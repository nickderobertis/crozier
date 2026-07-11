# Runtime (wire) tests

A **pytest** suite that verifies a **generated** SDK's runtime behavior — the
compiled client's behavior, not its source text (that is the byte-diff e2e's
job) — **differentially against Fern**. Driven by
`tests/e2e.rs::crozier_matches_fern_runtime_behavior`, which generates the
`exhaustive` SDK, prepares a cached venv (httpx + pydantic + pytest), and runs
`pytest` here with `CROZIER_SDK_SRC` / `FERN_SDK_SRC` pointing at the two SDKs.
It runs under `just test-e2e` / `just check`.

- **`_recorder.py`** (helper, not collected) drives one SDK through an injected
  `httpx.MockTransport` — the generated client accepts an `httpx_client` — and
  records, per journey, the request (method, URL, canonical headers, serialized
  body) and the outcome (response model dumped to a dict, or the typed error's
  class/status/body). The SDK import is **lazy** (`load_sdk`) so importing the
  module for `JOURNEY_NAMES` never loads a `fern` package.
- **`test_wire.py`** records **both** the Fern fixture SDK (`exhaustive/expected/
  src`, real runnable Fern output) and the crozier SDK — each in its own
  subprocess, since both packages are named `fern` and can't coexist in one
  process — and a parametrized test asserts the recordings match **per journey**.
  So the expected behavior is *derived from Fern*, not authored here.
- **How it mocks the wire.** This is the in-process analog of Fern's own wire
  tests (a WireMock server in Docker, verified via its admin API); crozier does not
  emit that Docker/`enable_wire_tests` tree, so we assert the same behaviors
  without it. Journeys cover request/URL construction, bearer auth + SDK headers,
  body aliasing + `OMIT` filtering, query encoding, typed deserialization, and
  typed error raising — sync + async.
- **The only allowed difference** is the deliberate SDK-identity branding
  (`X-Crozier-*` vs `X-Fern-*`). `_recorder._canonical_headers` folds either
  vendor prefix to a common `x-sdk-*` via one prefix rule (no enumerated list to
  drift) — the runtime analog of the byte-diff's
  `tests/e2e.rs::normalize_sdk_headers`. Do not add other normalizations to hide a
  real divergence — fix the generator instead.
- **Adding a journey.** Add a function `(sdk) -> observation dict` to
  `_recorder.JOURNEYS`; it must raise on a broken structural contract (e.g. a
  declared 4xx that fails to raise) so it can never record nothing and match
  trivially. `test_wire.py` picks it up via `JOURNEY_NAMES`. Keep to the SDK's own
  runtime deps + pytest. When a new generated shape lands, add a journey that
  *calls* it — the Fern fixture supplies the expected behavior for free.
- **Skip vs fail.** Missing Python / venv / deps is a skip locally and a hard
  failure under `CI` (see `runtime_python_env`), matching the Python-validity
  check's posture.
