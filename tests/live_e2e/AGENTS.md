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
  values. `_driver.py` executes each snippet, pointing the client at the mock
  (swapping the placeholder `base_url`, or injecting one when the spec's own
  `servers` made the snippet omit it). Endpoints are keyed by the full
  `sub_client.method` path, since a real API reuses a method name (`add`, `all_`)
  across sub-clients. Coverage tracks the spec, and the suite extends to another
  corpus by adding one line to `conftest.FIXTURES` — no per-endpoint code.
- **The mock is Prism** (`@stoplight/prism-cli`, pinned in `conftest.PRISM_PKG`),
  booted per fixture on an ephemeral port in **dynamic, seeded** mode (`-d --seed`):
  it generates each response *from the schema* rather than echoing the spec's
  committed `example`, because real specs carry examples that violate their own
  declared types (a `format: date` field whose example is a full datetime), which
  the SDK correctly rejects. The fixed seed keeps it reproducible.
- **`_relax.py` neutralizes only the request side.** Prism also validates the
  *request* and serves a 4xx (never reaching the success response) when a body is
  absent, a scalar fails a `format`, a required field is missing, or auth is unmet —
  and the generated example snippets trip all of these. Request construction, auth
  included, is covered exactly by the wire tests, so the mock is fed a copy with
  `security` dropped, `requestBody.required` cleared, and each request-body schema
  replaced by `{}` (match-anything). Replacing the schema — rather than editing it —
  is deliberate: a request body is usually a `$ref` into `components.schemas`, which
  is **shared with responses**, so mutating it in place would weaken the response
  validation the test relies on. **Nothing under `responses` is touched.** Do not
  relax responses to make a test pass; fix the generator instead.
- **The assertion is typed, not just "no error".** `_driver._observe` validates the
  returned value against the method's resolved return type
  (`typing.get_type_hints` + `pydantic.TypeAdapter`). A raised `ApiError` or a
  type-mismatched result records a failure; `test_live_e2e.py` asserts every
  endpoint recorded a clean round-trip, that the sweep covered *exactly* the
  reference's endpoints (no silent drop/rename), and that real pydantic models come
  back (no trivial all-primitive pass).
- **Mock-side failures are skipped, not failed.** A large real spec outruns Prism's
  dynamic response generator: some endpoints 5xx (json-schema-faker crashes) and some
  return a body that omits a field its *own* response schema marks `required`. Both
  are the mock failing to honor the spec, provably independent of which SDK calls it
  (Fern's own client hits them identically), so `_driver._mock_side_reason`
  classifies exactly these two cases — an `ApiError` with `status_code >= 500`, and a
  direct `pydantic.ValidationError` whose every error is `missing` (or Fern 5.20's
  exact generated `ParsingError` wrapping that same cause) — as a **skip** carrying
  the reason. Everything else (a 4xx, a wrong-type field, a failed constraint) still
  fails the gate. This can't mask a crozier bug: the byte-diff e2e independently
  proves each model's required/optional shape against Fern. Do **not** widen this to
  silence a real failure — fix the generator instead.
- **One SDK per subprocess.** Every fixture's package is named `fern`, so two
  cannot coexist in one interpreter; `_driver.py` runs as a subprocess per fixture
  (as `tests/runtime/_recorder.py` does), printing its recording as JSON.

## Two corpus kinds

- **Vendored synthetic seeds** (`exhaustive`, …): the spec is committed at
  `tests/fixtures/<name>/openapi.yml`. `exhaustive` (55 endpoints, 15 sub-clients)
  is the deliberately complicated seed.
- **`link-ok` real-world corpus** (`apideck.com-crm`, 40 endpoints across 8
  sub-clients; `bunq.com`, 421 endpoints across 118 sub-clients — the at-scale
  target): a real API from `tests/fixtures/CORPUS.md`. Its licence permits
  redistribution but, per the corpus policy, **only the generated Fern golden is
  vendored — not the spec**. The `Fixture.spec_url` points at the pinned upstream
  URL, and the harness fetches the spec (with retries) at run time. This is the
  proof that crozier's parameter/response `$ref` resolution and Fern-matching method
  naming hold up on a messy real-world document, not just curated seeds.

## Adding a fixture

Add a `Fixture(...)` to `conftest.FIXTURES` — the generation flags are the runtime
analog of the byte-diff `Corpus` in `tests/e2e.rs`; the package must generate as
`fern` so the reference snippets import. For a real-world corpus entry, set
`spec_url` to its CORPUS.md row and commit the Fern golden `expected/` (the
`reference.md` drives collection). Everything else — endpoint discovery, fetch, the
mock, the assertions — is automatic. Pick corpora whose *Fern* output generates
cleanly (a spec Fern itself rejects is not a valid target) and whose crozier output
is runnable end to end.

## Skip vs fail

Missing tooling — the `crozier` binary, Node/Prism, or the Python deps — is a
**skip** locally and a hard **failure** under `CI` (`conftest._require`), matching
the wire suite's posture so the mock e2e can never silently no-op in the gate.
`scripts/live-e2e.sh` additionally gates each tool with an actionable error when
invoked directly.
