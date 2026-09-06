# Fern probe documents

Locally authored OpenAPI documents, one per shape, carried through `fern check`
and a real `fern generate` so
[`../../fern-limitations.md`](../../fern-limitations.md) can record what Fern did
with a shape no real-world document supplies. They exist so a verdict there can
be **re-run** rather than taken on trust.

**None of these is a corpus fixture, and none may become one.**
[`../../../tests/fixtures/`](../../../tests/fixtures/) takes real-world
specifications only ([`../../../tests/fixtures/AGENTS.md`](../../../tests/fixtures/AGENTS.md)),
so a probe never produces a `CORPUS.md` row, never counts as parity evidence in
[`../../openapi-surface-coverage.md`](../../openapi-surface-coverage.md), and
never moves a region row to `golden`. What a probe settles is a `limitations` row
on a measured verdict; a real-world witness found later is what promotes it.

## Re-running one

The workspace is the one `scripts/generate-fern-fixture.sh` scaffolds — Fern CLI
`5.67.1` in `fern.config.json`, `fernapi/fern-python-sdk` at the corpus pin,
`pydantic_config.enum_type: python_enums`, `CI=true`/`GITHUB_ACTIONS=true` —
with `openapi/openapi.yml` copied from here. Build it under `mktemp -d` rather
than inside a checkout: Fern stamps `originGitCommit` into `.fern/metadata.json`
when its workspace sits in one, and the corpus goldens carry no such field.

Compare crozier against a probe Fern generated cleanly under the gate's own
normalization — `crozier internal-strip` on both sides, SDK-identity headers
normalized, `__init__.py` import order canonicalized with `ruff` isort,
`.fern/metadata.json`'s `generatorConfig` dropped — which is what `tests/e2e.rs`
does to a corpus golden. A divergence is repaired in `src/`, never written down
as a Fern limitation.

## Naming

`<ledger-key-family>.yml`, plus the variants a measurement needs. A shape whose
verdict depends on a *difference* carries its control beside it
(`…-control.yml`), and a security scheme carries both documents the verdict rests
on (`…-alone.yml`, `…-beside-bearer.yml`) — the pair is what distinguishes a
scheme Fern refuses from one it silently drops.
