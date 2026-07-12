# tests/fixtures/AGENTS.md

Folder-scoped notes for the golden fixture corpus. Layout, provenance, and the
matched manifest live in [`README.md`](README.md) and
[`../../docs/matching.md`](../../docs/matching.md) — this file is the judgment a
script can't encode. See the root [`AGENTS.md`](../../AGENTS.md) for the rest.

## Adding a fixture

A fixture is `<name>/` holding `openapi.yml` (the spec crozier consumes) and
`expected/**` (Fern's output, comment-stripped). The mechanical steps are
scripted; the two `expected/`-producing paths differ by source:

- **Offline corpus** (Fern commits the output, no Docker): add a `<name>:<spec>:<seed>`
  entry to `CORPUS` in `scripts/fixtures-refresh.sh`, then `just fixtures-refresh`.
- **Feature target / exhaustive** (Fern's committed output isn't OpenAPI-derived,
  needs a container runtime): `scripts/fixture-new.sh <name>` scaffolds the dir;
  drop in the real spec, then `scripts/generate-fern-fixture.sh <name>` (Docker +
  the `fern` CLI) generates and installs `expected/`. Two env vars drive Fern's
  optional generator config for the spec/flag a fixture exercises:
  `FERN_AUDIENCES=public[,internal]` (audience filtering) and
  `CLIENT_CLASS_NAME=<Name>` (the root client class name, issue #61) — match them
  to the crozier flags the corpus is driven with (`--audience`,
  `--client-class-name`).

Then wire a `Corpus { api, package_name, project_name, matched: &[] }` into
`tests/e2e.rs` (`FEATURE_TARGETS`, or a `const` for a headline corpus). Start
`matched` **empty** — the smoke test then only asserts crozier consumes the spec
without panicking.

## Growing `matched` — don't diff by hand

After a generator change, `just fixtures-candidates` reports every `expected/`
file crozier now reproduces byte-for-byte that isn't yet listed, as ready-to-paste
array entries. Paste them into that corpus's `matched`; the gate then locks them
in. This is the loop — not a manual tree diff.

## Non-negotiable

- **A file joins `matched` only after crozier byte-matches it.** Never edit a
  committed fixture to match crozier — the fixture is Fern's golden output; fix
  the generator instead. `just fixtures-candidates` reports *matches*, never
  rewrites fixtures.
- **Keep attribution.** The corpus is Fern's output (Apache-2.0); `../../NOTICE`
  and `../../licenses/fern-APACHE-2.0.txt` must survive any regeneration (the
  refresh scripts preserve them).
- **`.py` is comment-stripped, scaffolding is verbatim.** The comparison uses the
  same `crozier internal-strip` that produced the fixtures; that normalization is
  the *only* difference allowed between crozier's output and Fern's.
