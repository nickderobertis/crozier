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
  `FERN_AUDIENCES=public[,internal]` (audience filtering), `CLIENT_CLASS_NAME=<Name>`
  (the root client class name, issue #61), and `EXTRA_FIELDS=allow|ignore|forbid`
  (pydantic extra-fields behavior, issue #63) — match them to the crozier flags the
  corpus is driven with (`--audience`, `--client-class-name`, `--extra-fields`).

Then wire a `Corpus { api, package_name, project_name, matched: &[] }` into
`tests/e2e.rs` (`FEATURE_TARGETS`, or a `const` for a headline corpus). Start
`matched` **empty** — the smoke test then only asserts crozier consumes the spec
without panicking.

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

`scripts/`-free pre-screen: parse the spec and count, per operation, request bodies
without a `$ref` schema, plus `format: date` fields whose example contains a time.
Zero of both is the green light; then run `scripts/generate-fern-fixture.sh`.

### Specs already tried and REJECTED (do not re-attempt without a fix upstream)

Fern rejected these raw specs — an agent burned a full generate on each, so they
are logged here to stop the next one repeating it. Fern's *own* published SDK for
these is built from a spec with Fern overrides applied, not the raw document.

| spec | source | why Fern rejects it |
|---|---|---|
| `deepgram` | `deepgram/deepgram-api-specs@main/openapi.yml` | 342 errors: duplicate inline `ListRequest` across sub-clients, and integer enums (`16000`, `48000`, …) with no `x-fern-enum` names |
| `asana` (api-guru `asana.com/1.0`) | already attempted by a prior agent too | 17 errors: inline request-body collisions (`AddFollowersRequest`, `RemoveFollowersRequest`, `ProjectSaveAsTemplateRequest`) and `date` fields with datetime examples |

Accepted so far: `apideck.com-crm` (fully matched) and `bunq.com` (all request
bodies `$ref`ed; fully matched, all 956 files — see [`../../docs/matching.md`](../../docs/matching.md)).

## Growing `matched` — don't diff by hand

After a generator change, `just fixtures-candidates` reports every `expected/`
file crozier now reproduces byte-for-byte that isn't yet listed, as ready-to-paste
array entries. Paste them into that corpus's `matched`; the gate then locks them
in. This is the loop — not a manual tree diff.

## Why a file *doesn't* match — `just fixtures-diff`

The inverse tool. `just fixtures-diff [<corpus> [<file-substring>]]` prints the
**normalized** unified diff of every fixture file crozier does *not* reproduce
(`-` = Fern golden, `+` = crozier). It diffs exactly the bytes the gate compares —
comments, SDK-identity headers, and `__init__.py` import order are already
normalized out — so a raw `diff tempdir fixture` won't mislead you with
differences the gate ignores. Narrow to one file with the substring arg while
iterating on the generator. The gate's own failure message prints the same diff
inline, so a regression in a `matched` file is diagnosable straight from
`just test-e2e` without a second pass.

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
