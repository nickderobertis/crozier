# Runtime (wire) tests

A **pytest** suite that verifies a **generated** SDK's runtime behavior — the
compiled client's behavior, not its source text (that is the byte-diff e2e's
job) — **differentially against Fern**. Driven by
`crates/crozier-e2e/tests/e2e.rs::sdk_env_crozier_matches_fern_runtime_behavior`, which generates the
`airbyte.local-config` SDK, prepares a cached venv (httpx + pydantic + pytest), and runs
`pytest` here with `CROZIER_SDK_SRC` / `FERN_SDK_SRC` pointing at the two SDKs.
Installing those from PyPI puts it in the SDK Python-environment tier, promoted
out of the affected tier.

- **`_recorder.py`** (helper, not collected) drives one SDK through an injected
  `httpx.MockTransport` — the generated client accepts an `httpx_client` — and
  records, per journey, the request (method, URL, canonical headers, serialized
  body) and the outcome (response model dumped to a dict, or the typed error's
  class/status/body). The SDK import is **lazy** (`load_sdk`) so importing the
  module for `JOURNEY_NAMES` never loads a `fern` package.
- **`test_wire.py`** records **both** the Fern fixture SDK (`airbyte.local-config/expected/src`, generated from the registered API) and the crozier SDK — each in its own
  subprocess, since both packages are named `fern` and can't coexist in one
  process — and a parametrized test asserts the recordings match **per journey**.
  So the expected behavior is *derived from Fern*, not authored here.
- **How it drives the wire.** Journeys call the real generated clients with an
  injected `httpx.MockTransport`; `_recorder.JOURNEYS` is the inventory. Every
  request-shaping path the generator emits needs a journey, sync and async alike,
  so a generator change that alters what goes on the wire cannot go unrecorded.
- **The only allowed difference** is the deliberate SDK-identity branding
  (`X-Crozier-*` vs `X-Fern-*`). `_recorder._canonical_headers` folds either
  vendor prefix to a common `x-sdk-*` via one prefix rule. Every SDK-identity
  field is compared after that prefix change. This is the runtime analog of
  the byte-diff's `sdk-identity-header-prefix` departure. Do not add other
  normalizations to hide a real divergence — fix the generator instead.
- **Adding a journey.** Add a function `(sdk) -> observation dict` to
  `_recorder.JOURNEYS`; it must raise on a broken structural contract (e.g. a
  declared 4xx that fails to raise) so it can never record nothing and match
  trivially. `test_wire.py` picks it up via `JOURNEY_NAMES`. Keep to the SDK's own
  runtime deps + pytest. When a new generated shape lands, add a journey that
  *calls* it — the Fern fixture supplies the expected behavior for free.
- **No skip.** Missing Python / venv / deps fails the test (see
  `runtime_python_env`): the tier exists to run it, so it never passes unrun.

- Python: `format`, `lint` and `typecheck` only. `test` keeps its own runner and
  these files stay out of the combined coverage floor, because its suite needs
  the generated SDKs' PyPI venv.
