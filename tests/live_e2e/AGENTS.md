# Live e2e (mock-server) tests

A **pytest** suite that proves a **generated** SDK round-trips over **real HTTP**
against a **spec-shaped mock server**: for every endpoint the SDK documents, it
makes a live request and asserts a value of the method's *declared return type*
comes back. It is the runtime complement to the two static checks — the byte-diff
e2e proves the generated *source*, and the wire tests (`tests/runtime/`) prove the
client's request/response *shaping* matches Fern — this proves the compiled client
actually talks to a server.

Run it with `just test-live-e2e` (or `./scripts/live-e2e.sh`). It is **separate
from `just check`** so the core gate stays Node-free; CI runs it as its own
required leg (`live-e2e`, aggregated into `gate`).

## How it works

- **Spec-driven, not hand-authored.** The endpoint list and the example arguments
  come from the SDK's own generated `reference.md` — one runnable `client.<sub>.
  <method>(...)` usage snippet per typed method, already carrying valid example
  values. `_driver.py` executes each snippet verbatim except that it repoints the
  placeholder `base_url` at the running mock. So coverage tracks the spec, and the
  suite extends to another corpus by adding one line to `conftest.FIXTURES` — no
  per-endpoint code.
- **The mock is Prism** (`@stoplight/prism-cli`, pinned in `conftest.PRISM_PKG`),
  booted per fixture on an ephemeral port. It serves spec-shaped example responses,
  so a successful parse is a real deserialization, not a canned dict.
- **`_relax.py` loosens only the request side.** Prism also validates the *request*
  and 422s (never reaching a response) when a body is absent or a scalar fails a
  `format`/`pattern` — and Fern's own example snippets do exactly that (they omit
  all-optional bodies and pass placeholder `uuid`/`byte` strings). Request
  construction is already covered exactly by the wire tests, so the mock is fed a
  copy of the spec with `requestBody.required` cleared and request-body
  `format`/`pattern`/`required` stripped. **Every response schema — the thing under
  test — is untouched.** Do not relax anything under `responses` to make a test
  pass; fix the generator instead.
- **The assertion is typed, not just "no error".** `_driver._observe` validates the
  returned value against the method's resolved return type
  (`typing.get_type_hints` + `pydantic.TypeAdapter`). A raised `ApiError` or a
  type-mismatched result records a failure; `test_live_e2e.py` asserts every
  endpoint recorded a clean round-trip, that the sweep covered *exactly* the
  reference's endpoints (no silent drop/rename), and that real pydantic models come
  back (no trivial all-primitive pass).
- **One SDK per subprocess.** Every fixture's package is named `fern`, so two
  cannot coexist in one interpreter; `_driver.py` runs as a subprocess per fixture
  (as `tests/runtime/_recorder.py` does), printing its recording as JSON.

## Adding a fixture

Add a `Fixture(...)` to `conftest.FIXTURES` with the generation flags crozier is
driven with (the runtime analog of the byte-diff `Corpus` in `tests/e2e.rs`); the
package must generate as `fern` so the reference snippets import. Everything else —
endpoint discovery, the mock, the assertions — is automatic. Pick corpora whose
generated SDK is runnable end to end; `exhaustive` (55 endpoints across 15
sub-clients) is the deliberately complicated seed.

## Skip vs fail

Missing tooling — the `crozier` binary, Node/Prism, or the Python deps — is a
**skip** locally and a hard **failure** under `CI` (`conftest._require`), matching
the wire suite's posture so the mock e2e can never silently no-op in the gate.
`scripts/live-e2e.sh` additionally gates each tool with an actionable error when
invoked directly.
