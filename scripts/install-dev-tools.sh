#!/usr/bin/env bash
# Install the cargo subcommands the gate needs, if missing. Idempotent and quiet
# on success. Prefers prebuilt binaries (cargo-binstall) over source builds.
#
# In CI these come from taiki-e/install-action (see .github/workflows/ci.yml);
# this script is the clean-clone local path invoked by `just bootstrap`.
set -euo pipefail

# The ruff version Fern's fixtures were produced with. crozier defers Python
# line wrapping to `ruff format` (see src/pyfmt.rs), so `ruff` is a
# generation-time dependency the e2e needs; pinning it matches Fern's output
# byte-for-byte. Any recent ruff formats these shapes identically, so an existing
# `ruff` on PATH is left as-is rather than force-downgraded.
RUFF_VERSION=0.11.5

tools=(cargo-nextest cargo-llvm-cov cargo-deny cargo-machete)

missing=()
for t in "${tools[@]}"; do
  sub="${t#cargo-}"
  cargo "$sub" --version >/dev/null 2>&1 || missing+=("$t")
done

need_ruff=0
command -v ruff >/dev/null 2>&1 || need_ruff=1

if [ "${#missing[@]}" -eq 0 ] && [ "$need_ruff" -eq 0 ]; then
  exit 0
fi

if command -v cargo-binstall >/dev/null 2>&1; then
  [ "${#missing[@]}" -gt 0 ] && {
    echo "install-dev-tools: installing ${missing[*]}" >&2
    cargo binstall --no-confirm --locked "${missing[@]}"
  }
  [ "$need_ruff" -eq 1 ] && {
    echo "install-dev-tools: installing ruff@$RUFF_VERSION" >&2
    cargo binstall --no-confirm "ruff@$RUFF_VERSION"
  }
else
  echo "install-dev-tools: cargo-binstall not found; building from source (slow)." \
       "Install it for faster setup: https://github.com/cargo-bins/cargo-binstall" >&2
  [ "${#missing[@]}" -gt 0 ] && cargo install --locked "${missing[@]}"
  [ "$need_ruff" -eq 1 ] && cargo install --version "$RUFF_VERSION" ruff
fi
