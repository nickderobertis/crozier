# tests/fixtures/AGENTS.md

Folder-scoped notes for the golden fixture corpus. Layout, provenance, and the
gap manifest lives in [`README.md`](README.md) and
[`../../docs/matching.md`](../../docs/matching.md); the maintenance lifecycle is
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md). This file is the
judgment a script can't encode. See the root [`AGENTS.md`](../../AGENTS.md) for
the rest.

## Adding a fixture

Add one numbered [`CORPUS.md`](CORPUS.md) row and source URL per feature branch,
then wire a `Corpus { api, package_name, project_name, unmatched: &[] }` into
`tests/e2e.rs`, plus its `#[test]` and its `just test-corpus-match` line —
`every_registered_corpus_is_wired_into_the_gate` fails without both, because a
corpus nothing runs is not coverage. Push the branch and manually dispatch
the **Fern goldens** workflow on that branch for the fixture; red comparison is
expected until Crozier is repaired. A Monday 05:17 UTC run from `main` leaves
both inputs blank to check the latest Fern against every managed golden. Do Fern
upgrade work on an expected-red feature branch, retain the workflow's
best-effort successful commits and exact known-failure evidence, then rerun with
the resolved exact version until the final run is green with no changes to
generate or publish. The complete selection, provenance, partial-success,
publication, and rerun contract is in
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md).

**One non-default Fern setting is corpus-wide.** Every golden — managed or
hand-authored — is generated with `pydantic_config.enum_type: python_enums`,
which `scripts/generate-fern-fixture.sh` writes into `generators.yml`
unconditionally for *all* fixtures rather than per row. It is not a column of the
config table below and no fixture opts out; Fern records it in each golden's
`.fern/metadata.json` (`generatorConfig`), and because crozier renders that enum
shape unconditionally the e2e normalizes the block off both sides
(`tests/e2e.rs::normalize_metadata`). Regenerate through that script, never a
hand-rolled `fern generate`, or the golden silently comes back in Fern's
out-of-the-box open-`Literal`-union enum shape. Rationale:
[`../../docs/matching.md`](../../docs/matching.md).

Per-fixture non-default settings live in **one shared table**,
[`fern-generator-config.txt`](fern-generator-config.txt) — a single file for the
whole corpus keyed by fixture name (`fixture|audiences|audience_strict|
client_class_name|extra_fields`), not a file per fixture directory. A fixture
needing a non-default audience, client-class-name, or extra-fields setting adds
its row there; the generator loads that row and records the settings in the
golden's provenance (`expected/.crozier-fern-golden.json`). Model and test a new
setting there before regenerating; do not silently use different defaults.

## Choosing a real-world spec — Fern must accept it FIRST

A candidate is only viable if **Fern itself generates it cleanly** (`fern check`
passes); crozier byte-matching Fern's output is meaningless if Fern rejected the
spec. Fern's real gate is stricter than "valid OpenAPI", and most raw public specs
fail it, so **screen before you spend a Docker generate**. The two failure modes
that kill most specs:

- **Inline request-body name collisions.** Fern coins `<Operation>Request` for a
  request body defined inline (no `$ref`); two endpoints that coin the same name
  across sub-clients are a hard error (`X is already declared in Y.yml`). Specs
  whose request bodies are all `$ref`s to named `components.schemas` avoid this.
- **Example / declared-type mismatches.** A `format: date` field whose `example`
  is a full datetime (or an integer `enum` value with no `x-fern-enum` name) is a
  hard error. Screen `format: date` examples and numeric `enum`s.

An optional pre-screen can count, per operation, request bodies without a `$ref`
schema and `format: date` fields whose example contains a time. Zero of both is a
good signal, but the dispatched workflow is the authoritative Fern check and
retains any successful sibling results when another selection fails.

### Specs already tried and REJECTED (do not re-attempt without a fix upstream)

Fern rejected these raw specs — an agent burned a full generate on each, so they
are logged here to stop the next one repeating it. Fern's *own* published SDK for
these is built from a spec with Fern overrides applied, not the raw document.

| spec | source | why Fern rejects it |
|---|---|---|
| `deepgram` | `deepgram/deepgram-api-specs@main/openapi.yml` | 342 errors: duplicate inline `ListRequest` across sub-clients, and integer enums (`16000`, `48000`, …) with no `x-fern-enum` names |
| `asana` (api-guru `asana.com/1.0`) | already attempted by a prior agent too | 17 errors: inline request-body collisions (`AddFollowersRequest`, `RemoveFollowersRequest`, `ProjectSaveAsTemplateRequest`) and `date` fields with datetime examples |
| `xtrf.eu` (api-guru `xtrf.eu/2.0`) | `https://api.apis.guru/v2/specs/xtrf.eu/2.0/openapi.json` | Python 5.20.0 generator rejects seven response-example fields across `getJobFiles` and `getTaskFiles`, despite `fern check` passing |
| `github.com-ghes-3.8` (api-guru `github.com/ghes-3.8/1.1.4`) | `https://api.apis.guru/v2/specs/github.com/ghes-3.8/1.1.4/openapi.json` | Python 5.20.0 generator rejects 29 request collisions, examples, duplicate declarations, and enum names, despite `fern check` passing |

Accepted and matched corpus status lives in [`CORPUS.md`](CORPUS.md); do not
duplicate its batch ledger here.

## Shrinking `unmatched` — don't diff by hand

The corpus is at full byte parity: every `unmatched` list is empty, so a
non-empty one means work in flight, not an accepted state. `just fixtures-gaps`
generates every available corpus and reports the exact divergent files as
ready-to-paste `unmatched` arrays; land the generator fix and empty the list
again. Every expected file outside that list is gated, including files newly
emitted by Fern, and the comparison also walks Crozier's output back, so nothing
can be suppressed by omission. The reporter rejects stale entries that now match.
`fixtures-candidates` is retained as an alias.

A validated `known-fern-failure.json` is the only reason a registered corpus may
have no `expected/` tree; every other missing golden is a hard error. That
registration is bound to one exact generator version, corpus identity, exit code,
and diagnostic fingerprint, so it cannot be copied onto a corpus that merely
diverges — see `a_known_fern_failure_registration_cannot_excuse_anything_else`.
Such a corpus remains a spec-level robustness test until Fern
succeeds, at which point remove the failure registration and use the managed
workflow to publish a provenanced golden so it rejoins byte comparison.

## Why a file *doesn't* match — `just fixtures-diff`

The inverse tool. `just fixtures-diff [<corpus> [<file-substring>]]` prints the
**normalized** unified diff of every fixture file crozier does *not* reproduce
(`-` = Fern golden, `+` = crozier). It diffs exactly the bytes the gate compares —
comments, SDK-identity headers, and `__init__.py` import order are already
normalized out — so a raw `diff tempdir fixture` won't mislead you with
differences the gate ignores. Narrow to one file with the substring arg while
iterating on the generator. The gate's own failure message prints the same diff
inline, so a regression outside `unmatched` is diagnosable straight from
`just test-e2e` without a second pass.

## Non-negotiable

- **`unmatched` holds only measured divergence, never an accepted one.** Never
  edit a committed fixture to match crozier — the fixture is Fern's golden
  output; fix the generator instead. `just fixtures-gaps` reports divergence and
  never rewrites fixtures.
- **Keep attribution.** The corpus is Fern's output (Apache-2.0); `../../NOTICE`
  and `../../licenses/fern-APACHE-2.0.txt` must survive any regeneration (the
  refresh scripts preserve them).
- **`.py` is comment-stripped, scaffolding is verbatim.** The comparison uses the
  same `crozier internal-strip` that produced the fixtures; that normalization is
  the *only* difference allowed between crozier's output and Fern's.
