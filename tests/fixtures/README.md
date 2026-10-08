# Fixtures

These fixtures hold Fern-generated SDK goldens that crozier byte-compares.
Inputs are independently authored OpenAPI documents or registered publisher
specifications; their provenance lives in [`CORPUS.md`](CORPUS.md) and the
per-golden metadata.

- **Generation:** Each local fixture's `expected/` tree is generated from its
  own `openapi.yml` by `tools/fern-goldens/generate-fern-fixture.sh`. Numbered publisher
  sources and immutable references live in [`CORPUS.md`](CORPUS.md). The
  **Fern goldens** workflow checks the latest stable generator from `main`
  weekly; each managed golden records its exact version in provenance.
- **License / attribution:** [`../../licenses/fern-APACHE-2.0.txt`](../../licenses/fern-APACHE-2.0.txt)
  and [`../../NOTICE`](../../NOTICE) (with the statement of changes required by
  Apache-2.0 §4). Keep them; regeneration must preserve them.

## Layout

Each `<api>/` directory holds:

- `openapi.yml` for vendored fixtures, or a numbered `CORPUS.md` row whose source
  is committed under `corpus-sources/` and recorded in `corpus-sources.tsv`.
- `expected/` — Fern's Python SDK output for that spec, **comment-stripped** (a
  string-safe removal of `#` comments, the only change from Fern's output). The
  same stripper normalizes crozier's output before the byte comparison, so
  generator-identifying comments never affect the match. This directory is
  required unless a validated `known-fern-failure.json` records that Fern cannot
  produce a current SDK.
- `expected/.crozier-fern-golden.json` — the exact Fern generator version, plus
  the manifest name/ref/URL on a workflow-managed corpus golden or the vendored
  spec path and any non-default generator knob on a vendored one. It is automation
  provenance, not Fern output, so the comparison excludes it.
- `expected-flat/` — for the fixtures [`flat-goldens.txt`](flat-goldens.txt)
  declares, Fern's **flat** output for the same spec and settings: what
  `fern generate --local` writes to a `local-file-system` output path, which
  crozier reproduces with `--layout flat`. Produced by
  `tools/fern-goldens/generate-fern-fixture.sh --layout flat <fixture>` (or, for a
  `CORPUS.md` row, by the Fern goldens workflow beside its packaged golden). It
  follows the same comment-stripping and provenance rules as `expected/`, and its
  `.crozier-fern-golden.json` adds `"layout": "flat"`. A flat golden may sit in a
  directory with no spec of its own (`swagger-petstore-distribution/`), generating from
  the fixture its `flat-goldens.txt` row names. See
  [`../../docs/matching.md`](../../docs/matching.md#the-flat-layout).
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

- **Feature-coverage targets** — hand-authored specs pinning one shape each,
  all matched in full (the shape-by-shape rationale is in
  [`../../docs/matching.md`](../../docs/matching.md)). `FEATURE_TARGETS` in
  `crates/crozier-e2e/tests/e2e.rs` is the list; those entries also provide compile/smoke coverage
  independently of the byte comparison.

Declared fixtures also carry a flat golden (`FLAT_GOLDENS` in `crates/crozier-e2e/tests/e2e.rs`, one
`*_flat_matches_fern` test each), chosen so that between them they exercise every
setting that changes the flat tree.

Every `Corpus` in `crates/crozier-e2e/tests/e2e.rs` carries an empty `unmatched` residual list: the
whole corpus reproduces its Fern goldens byte-for-byte, apart from the one
accepted upstream exception (`calorieninjas.com`, which has no golden because
Fern cannot produce one). Every file in every golden tree is gated in both
directions, including newly emitted files. See [`AGENTS.md`](AGENTS.md);
`just fixtures-gaps` re-measures the census.
