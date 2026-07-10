# AGENTS.md

Durable instructions for humans and agents working in this repo. Write for a
future maintainer, not as a session log. Put deterministic steps in scripts and
keep this file for constraints, tradeoffs, and judgment.

> Keep this file terse — it is always-loaded context. Add a line only if it is
> future-relevant **and** wouldn't surface anyway (a failing gate, `just --list`,
> the code, or a linked doc). Folder-scoped rules go in a nested `AGENTS.md`;
> longer material goes in a `docs/` reference linked from here, not inlined.

> `CLAUDE.md` is a symlink to this file. Edit `AGENTS.md` only.

## What this repo is

`crozier` is a Rust CLI that generates client SDKs from an OpenAPI 3.x document,
matching [Fern](https://github.com/fern-api/fern)'s generator output byte-for-byte
(comments aside). Python is the only target today. It ships as a single static
binary. Generators are Rust + [minijinja](https://github.com/mitsuhiko/minijinja)
templates — there is no plugin-in-target-language model and no per-project config
file: the OpenAPI document plus a few naming flags are the entire input.

The north star: **`crozier`'s output, with comments stripped, equals Fern's
output with comments stripped.** See [`docs/matching.md`](docs/matching.md) for
the strategy, the fixture corpus, and what is implemented vs. planned.

## Two standing goals on every task

The user drives product features; their request is the priority. Carry two goals
into *every* task, folding either in when it's the lowest-error path to the ask
and surfacing the rest as follow-ups:

1. **Engineer the context for next time** — realistic e2e that exercises what the
   user sees, scripts that shrink repetitive work to signal, terse `AGENTS.md`
   notes for what the code doesn't make obvious.
2. **Engineer the codebase and environment** — keep it clean, repeatable, and
   automated (`just bootstrap` from a clean clone; local/CI parity).

## Stack and composition

- **Product shape:** cli
- **Language(s):** rust
- **References composed:** base, shapes/cli, languages/rust, intersections/rust-cli, ci, llmlint, releasing
- **Excluded, and why:**
  - **MSRV pin / `just msrv`** — no MSRV is promised yet (pre-1.0, single
    maintainer); `rust-toolchain.toml` pins one stable channel and CI installs
    from it. Add an MSRV when external consumers appear.
  - **crates.io publish** — binary-only tool; distribution is GitHub Releases +
    `cargo install --git` / `install.sh` (`publish = false`). crates.io is a
    later, optional surface.
  - **Bench tier** — performance is a goal, but the informational Criterion/
    hyperfine tier is deferred until there's a hot path worth tracking; it never
    gates, so its absence costs no correctness.

## Command surface

Use the `just` recipes; do not hand-roll equivalents.

- `just bootstrap` — set up from a clean clone.
- `just check` — full gate (fmt check, clippy `-D warnings`, tests incl. e2e with
  coverage, `cargo deny`, `cargo machete`, doc). Must pass before any commit/PR.
- `just test` / `just test-e2e` / `just lint` / `just format` — individual steps.
- `just upgrade` — `cargo update`, then re-run `just check`.
- `just fixtures-refresh` — re-vendor the Fern reference fixtures (see below).
- `just lint-llm` / `just lint-llm-diff` — LLM-judge tier (llmlint), separate from
  `check` and non-deterministic; config in `llmlint.yml`. `just setup-llmlint`
  installs it.

## Commits, releases, and merging

- **Squash-merge only, via PR, with auto-merge.** The default branch is
  protected: merge/rebase disabled, so one PR is one squash commit whose subject
  is the PR title. Queue with `gh pr merge --auto --squash`; merged branches
  auto-delete. Admins may break-glass.
- **All gating checks required:** `gate` (aggregates the e2e-inclusive `check`
  and `install` matrix legs), `commitlint` (PR-title Conventional Commits), and
  `llmlint` — plus linear history, conversation resolution, no
  force-push/branch-deletion. **Required secrets:** `CLAUDE_CODE_OAUTH_TOKEN`
  (llmlint's Claude Code harness) and `RELEASE_PLZ_TOKEN` (a PAT for releases)
  must be set in repo settings, or those checks fail fast by design. Sync them
  from Bitwarden via `gh-secrets sync` — the manifest is `gh-secrets.json`.
- **PRs follow `.github/pull_request_template.md`** (What / Why); it becomes the
  squash body.
- **Releases:** `release-plz` opens a release PR from merged Conventional Commits;
  merging it bumps the version, writes `CHANGELOG.md`, and pushes the `vX.Y.Z`
  tag, which triggers `release.yml` (build + upload per-platform archives). Fully
  automated — the only human action is merging a PR. **Bump policy (pre-1.0):**
  `feat`/`feat!`/`BREAKING CHANGE` → minor; `fix`/`perf`/`refactor`/`build` →
  patch; `chore`/`docs`/`ci`/`test`/`style` → no release.

## Invariants (non-negotiable)

- The gate is strict: no warnings-only mode. A diagnostic is an error or is
  suppressed with a documented, tracked rationale.
- **Byte-exact output is the product.** Any change to emitted Python is validated
  by the fixture-diff e2e (see below); never "fix" a mismatch by editing a
  committed fixture to match a regression — fix the generator.
- **Tests are realistic, not mocked, and complete, not minimal.** E2E drives the
  compiled `crozier` binary as a subprocess (`assert_cmd`) over real temp dirs and
  real spec files; a feature isn't done until a real journey covers it.
- Validate the OpenAPI document at the boundary; a malformed spec fails with a
  non-zero exit and an actionable message, never a panic.
- Portable across the Linux/macOS/Windows release matrix.
- **Security is gate-level.** No secrets/credentials in the tree; every grant
  (agent allowlist, CI token) least-privilege.

## Fern fixtures, licensing, and matching

- The `tests/fixtures/` corpus is Fern's own output (Apache-2.0), vendored as the
  golden target. **Retain the attribution:** `licenses/fern-APACHE-2.0.txt` and
  `NOTICE` must stay, and any regeneration must preserve them. Fern's *definition*
  files are ignored on purpose — crozier consumes only the OpenAPI document.
- Fixtures are comment-stripped (Fern-vs-crozier comments differ by design); the
  same string-safe stripper produces the committed fixtures and normalizes
  crozier's output in the e2e. Regenerate with `just fixtures-refresh`.
- **The exhaustive target needs Docker.** Fern's generator only runs under a
  container runtime, unavailable in some envs. `scripts/generate-fern-fixture.sh`
  produces the exhaustive fixture where Docker exists; the offline corpus
  (`query-parameters-openapi`, ...) needs no Docker and gates on every run. See
  [`docs/matching.md`](docs/matching.md).

## Scripts and output are context

- Every script is quiet on success (a line or nothing); on failure it prints the
  exact error and a concrete next action.

## Tests are context engineering

The suite is the only QA loop. E2E runs the real binary and byte-compares its
(comment-stripped) output to the committed fixtures — never mock the generator or
the filesystem it writes. Done means complete, not minimal: cover malformed-spec
failure and missing-file recovery, not just the happy path. Coverage is a floor
(95%), not the target. The e2e fixture manifest ([`docs/matching.md`]) is the
source of truth for which files are matched; it grows as generation lands.

## Keeping the allowlist current

The allowlist lives in `.claude/settings.json`; the tool enforces it. When a new
routine command joins the workflow, add it there rather than re-approving it.
Keep it narrow.

## After the main task: refine and hand off

Act on the two standing goals: automate a step you did by hand, record a gotcha
here, propose materially-helpful follow-ups (note each one's impact). Skip
busywork; if nothing helps, say so.
