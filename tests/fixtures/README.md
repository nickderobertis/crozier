# Fixtures

These fixtures are the golden target crozier is verified against. They are
**Fern's own output and test specs**, vendored under the Apache License 2.0.

- **Source:** The legacy offline seed is vendored from
  [fern-api/fern](https://github.com/fern-api/fern), commit
  `3a471b03d4778f291849adc03bacfcd40340fc26`; `exhaustive/expected/` was generated
  from `exhaustive/openapi.yml` with `fernapi/fern-python-sdk:4.35.0`. Numbered
  real-world corpus sources and refs live in [`CORPUS.md`](CORPUS.md). The
  **Fern goldens** workflow checks the latest stable generator from `main`
  weekly; each managed golden records its current exact version in provenance.
- **License / attribution:** [`../../licenses/fern-APACHE-2.0.txt`](../../licenses/fern-APACHE-2.0.txt)
  and [`../../NOTICE`](../../NOTICE) (with the statement of changes required by
  Apache-2.0 §4). Keep them; regeneration must preserve them.

## Layout

Each `<api>/` directory holds:

- `openapi.yml` for vendored fixtures, or a numbered `CORPUS.md` URL whose source
  is fetched to the ignored `.local/corpus` cache. Fern's own *definition* files
  are intentionally excluded — crozier reads only OpenAPI.
- `expected/` — Fern's Python SDK output for that spec, **comment-stripped** (a
  string-safe removal of `#` comments, the only change from Fern's output). The
  same stripper normalizes crozier's output before the byte comparison, so
  generator-identifying comments never affect the match.
- `expected/.crozier-fern-golden.json` on workflow-managed goldens — the exact
  Fern generator version and manifest name/ref/URL. It is automation provenance,
  not Fern output, so the comparison excludes it.
- `known-fern-failure.json` only when an exact generator/version/spec-bound
  upstream failure prevents a current golden. Its fingerprint is revalidated on
  every generation retry; it never makes an arbitrary Fern failure non-fatal.

## Corpus

The real-world source manifest and historical batch ledger live in
[`CORPUS.md`](CORPUS.md). Add or change one numbered row per feature branch, then
manually run **Fern goldens** on that branch. The same workflow runs from `main`
every Monday with blank inputs to resolve the latest Fern version across managed
goldens. See [`../../docs/fern-goldens.md`](../../docs/fern-goldens.md) for the
event/input contract, expected-red upgrade branches, best-effort publication,
known failures, provenance, and the final green/no-change rerun.

- **`query-parameters-openapi/`** — legacy offline seed; its source and committed
  `expected/` snapshot came directly from Fern's repository.
- **`exhaustive/`** — the broad target. `openapi.yml` (+ the source
  `generators.yml.source`, for reference) is vendored; its `expected/` tree is
  packaged Fern Python output generated from that OpenAPI document.
- **Feature-coverage targets** — hand-authored specs for the shapes crozier does
  not fully generate yet (the roadmap gaps in
  [`../../docs/matching.md`](../../docs/matching.md)): `auth-schemes`,
  `inline-request-response`, `cookie-parameters`, `form-bodies`,
  `discriminated-unions`, `schema-constraints`, `integer-enums`,
  `servers-webhooks`, and the issue-#84–#86 targets `recursive-types`,
  `nested-core-imports`, and `malformed-property-schema`. Their `FEATURE_TARGETS`
  entries in `tests/e2e.rs` also provide compile/smoke coverage independently of
  how many golden paths are matched.

Each `Corpus` in `tests/e2e.rs` carries the `matched` list that is the source of
truth for which files are byte-matched today. To add a fixture or grow that list,
see [`AGENTS.md`](AGENTS.md); `just fixtures-candidates` reports which committed
files Crozier already reproduces so growing the manifest is copy-paste.
