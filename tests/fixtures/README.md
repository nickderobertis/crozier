# Fixtures

These fixtures are the golden target crozier is verified against. They are
**Fern's own output and test specs**, vendored under the Apache License 2.0.

- **Source:** [fern-api/fern](https://github.com/fern-api/fern), commit
  `3a471b03d4778f291849adc03bacfcd40340fc26`.
- **License / attribution:** [`../../licenses/fern-APACHE-2.0.txt`](../../licenses/fern-APACHE-2.0.txt)
  and [`../../NOTICE`](../../NOTICE) (with the statement of changes required by
  Apache-2.0 §4). Keep them; regeneration must preserve them.

## Layout

Each `<api>/` directory holds:

- `openapi.yml` — the source OpenAPI document crozier consumes (vendored
  verbatim). Fern's own *definition* files are intentionally excluded — crozier
  reads only OpenAPI.
- `expected/` — Fern's Python SDK output for that spec, **comment-stripped** (a
  string-safe removal of `#` comments, the only change from Fern's output). The
  same stripper normalizes crozier's output before the byte comparison, so
  generator-identifying comments never affect the match.

## Corpus

- **`query-parameters-openapi/`** — offline; refresh with `just fixtures-refresh`
  (needs no Docker). Its `expected/` tree is committed.
- **`exhaustive/`** — the broad target. Only `openapi.yml` (+ the source
  `generators.yml.source`, for reference) is vendored; `expected/` is produced by
  running Fern's generator, which needs a container runtime — see
  `scripts/generate-fern-fixture.sh` and [`../../docs/matching.md`](../../docs/matching.md).

`tests/e2e.rs`'s `MATCHED` list is the source of truth for which files are
byte-matched today.
