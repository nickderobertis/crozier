#!/usr/bin/env bash
# Install cargo-prune-superseded at the release `just install-pruner` passes (the
# justfile's `prune_superseded_version`), which `just pool-maintenance` runs.
# Idempotent and quiet on success: that release already on PATH is left as-is.
#
# The pruner needs Rust 1.97 or newer, past this repository's rust-toolchain.toml
# pin, so it builds with rustup's `stable` toolchain; the repository's own pinned
# toolchain is untouched.
set -euo pipefail

version="${1:?usage: install-pruner.sh <version>}"
[ "$(cargo-prune-superseded --version 2>/dev/null)" = "cargo-prune-superseded $version" ] && exit 0

command -v rustup >/dev/null 2>&1 || {
  echo "install-pruner: rustup not found — install it (https://rustup.rs), then rerun 'just install-pruner'" >&2
  exit 1
}
echo "install-pruner: installing cargo-prune-superseded $version with the stable toolchain" >&2
rustup toolchain install stable --profile minimal --no-self-update >/dev/null 2>&1 || {
  echo "install-pruner: 'rustup toolchain install stable' failed; run it to see why, then rerun 'just install-pruner'" >&2
  exit 1
}
cargo +stable install --locked --quiet cargo-prune-superseded --version "$version"
