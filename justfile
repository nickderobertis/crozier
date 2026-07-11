# Canonical command surface for crozier. Keep this list small and memorable.
# `just bootstrap` must work from a clean clone; `just check` is the full gate
# and must fail on any issue (no warnings-only mode).

# List available recipes.
default:
    @just --list

# Set up from a clean clone: toolchain (from rust-toolchain.toml), deps, dev tools.
bootstrap:
    @rustup show active-toolchain >/dev/null 2>&1 || rustup toolchain install
    @rustup component add rustfmt clippy llvm-tools-preview >/dev/null 2>&1 || true
    cargo fetch --locked
    @./scripts/install-dev-tools.sh
    @./scripts/install-ruff.sh

# Full quality gate. Fails on any issue. e2e is part of the gate, not opt-in.
check: fmt-check lint test test-e2e supply-chain doc
    @echo "check: ok"

# Format check (does not modify files).
fmt-check:
    cargo fmt --all -- --check

# Lint; warnings are errors.
lint:
    cargo clippy --all-targets --all-features --locked -- -D warnings

# Fast tests (unit + integration, excluding the e2e binary target) with coverage
# enforced. 95% line coverage is the gate; lower it only with a reason in AGENTS.md.
test:
    cargo llvm-cov --locked --fail-under-lines 95 \
        --ignore-filename-regex 'main\.rs$' \
        nextest -E 'not binary(e2e)'

# End-to-end: drive the compiled binary the way a user runs it (assert_cmd),
# byte-comparing its stripped output to the committed Fern fixtures. Also run by
# `check`; this recipe runs the journeys in isolation.
test-e2e:
    cargo nextest run --locked -E 'binary(e2e)'

# Format the codebase in place.
format:
    cargo fmt --all

# Supply-chain gate (Linux; run once, not across an OS matrix).
supply-chain:
    cargo deny --locked check
    cargo machete

# Docs must build cleanly (broken intra-doc links are errors).
doc:
    RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features --locked

# Upgrade dependencies, then re-run the full gate.
upgrade:
    cargo update
    @just check

# Re-vendor the Fern reference fixtures (comment-stripped) into tests/fixtures.
# The offline corpus needs no Docker; pass `exhaustive` to also run Fern's
# container generator for the exhaustive spec. See docs/matching.md.
fixtures-refresh *args:
    ./scripts/fixtures-refresh.sh {{args}}

# Install/refresh the llmlint toolchain (oneharness + llmlint). Idempotent.
setup-llmlint:
    ./scripts/setup-llmlint.sh

# LLM-judge lint (llmlint) — non-deterministic, harness-backed; kept OUT of
# `check`. Run on demand over the configured set (or pass paths). See llmlint.yml.
lint-llm *paths:
    @command -v llmlint >/dev/null 2>&1 || { echo "llmlint not installed — run 'just setup-llmlint'"; exit 1; }
    llmlint {{paths}}

# `--diff` self-discovers the changed files (a three-dot compare against the base
# that skips files main also touched) and honors llmlint.yml's excludes, so no
# wrapper script is needed — it lints only what this branch introduced.
# Blocking `llmlint` PR check; run before pushing. BASE defaults to origin/main.
lint-llm-diff base="origin/main" *args:
    llmlint --diff git --diff-base {{base}} {{args}}
