#!/usr/bin/env bash
# Install the cargo subcommands the gate needs, if missing. Idempotent and quiet
# on success. Prefers prebuilt binaries (cargo-binstall) over source builds.
#
# In CI these come from taiki-e/install-action (see .github/workflows/ci.yml);
# this script is the clean-clone local path invoked by `just bootstrap`.
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

# The ruff version Fern's fixtures were produced with, read from the single source
# of truth `.ruff-version`. crozier defers Python line wrapping to `ruff format`
# (see src/pyfmt.rs), so `ruff` is a generation-time dependency the e2e needs;
# pinning it matches Fern's output byte-for-byte. Any recent ruff formats these
# shapes identically, so an existing `ruff` on PATH is left as-is.
RUFF_VERSION="$(cat "$repo_root/.ruff-version")"

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

# One status line naming everything that will be installed, then install quietly.
# (Append guardedly: bash 3.2 on macOS errors on an empty-array expansion here.)
wanted=()
[ "${#missing[@]}" -gt 0 ] && wanted+=("${missing[@]}")
[ "$need_ruff" -eq 1 ] && wanted+=("ruff==$RUFF_VERSION")
echo "install-dev-tools: installing ${wanted[*]}" >&2

# Cargo subcommands: prebuilt binaries via cargo-binstall, else build from source.
if [ "${#missing[@]}" -gt 0 ]; then
  if command -v cargo-binstall >/dev/null 2>&1; then
    cargo binstall --no-confirm --locked "${missing[@]}"
  else
    echo "install-dev-tools: cargo-binstall not found; building ${missing[*]} from source" \
         "(slow). Install it for faster setup: https://github.com/cargo-bins/cargo-binstall" >&2
    cargo install --locked "${missing[@]}"
  fi
fi

# ruff ships as a Python package, not a cargo crate, so install it from PyPI
# (pipx keeps it isolated and on PATH; fall back to uv or pip --user).
if [ "$need_ruff" -eq 1 ]; then
  if command -v pipx >/dev/null 2>&1; then
    pipx install "ruff==$RUFF_VERSION"
  elif command -v uv >/dev/null 2>&1; then
    uv tool install "ruff==$RUFF_VERSION"
  else
    python3 -m pip install --user "ruff==$RUFF_VERSION"
  fi
  # These installers drop the `ruff` shim in ~/.local/bin, which a fresh CI runner
  # does not always have on PATH; expose it to subsequent GitHub Actions steps.
  if [ -n "${GITHUB_PATH:-}" ]; then
    printf '%s\n' "$HOME/.local/bin" >>"$GITHUB_PATH"
  fi
fi
