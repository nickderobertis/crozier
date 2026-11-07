#!/usr/bin/env bash
# The visual-docs capture CI's lint lane runs, in the container that pins its renderer
# inputs to crozier's toolchain, twice: the second capture is screencomp's
# reproducibility gate. Writes shots/current/x86_64 and shots/verify/x86_64, owned by
# the caller. The build stays in a volume of its own, off the host's target/: root-owned
# and built against another registry path, it would dirty every later cargo run.
set -euo pipefail

image="rust:$(sed -n 's/^channel = "\(.*\)"$/\1/p' rust-toolchain.toml)-bookworm"
toolchain="${image#rust:}"
toolchain="${toolchain%-bookworm}"

docker run --rm -v "$PWD":/work -v crozier-visual-docs-target:/work/target -w /work \
  -e RUSTUP_TOOLCHAIN="$toolchain" \
  -e HOST_OWNER="$(id -u):$(id -g)" \
  "$image" bash -euc '
    # Whatever the capture leaves is the caller'\''s, including after a failed capture.
    trap '\''chown -R "$HOST_OWNER" shots'\'' EXIT
    git config --global --add safe.directory /work
    # freeze renders the deterministic SVGs; ruff is what crozier defers Python
    # wrapping to. Both prebuilt, pinned to the files the local recipes read, so the
    # local and CI renderers cannot silently diverge.
    freeze_ver="$(cat .freeze-version)"
    curl -fsSL -o /tmp/freeze.tgz "https://github.com/charmbracelet/freeze/releases/download/v${freeze_ver}/freeze_${freeze_ver}_Linux_x86_64.tar.gz"
    tar -xzf /tmp/freeze.tgz -C /tmp
    install "$(find /tmp -type f -name freeze | head -1)" /usr/local/bin/freeze
    ruff_ver="$(cat .ruff-version)"
    curl -fsSL -o /tmp/ruff.tgz "https://github.com/astral-sh/ruff/releases/download/${ruff_ver}/ruff-x86_64-unknown-linux-gnu.tar.gz"
    tar -xzf /tmp/ruff.tgz -C /tmp
    install "$(find /tmp -type f -name ruff | head -1)" /usr/local/bin/ruff
    SHOTS_OUT=shots/current/x86_64 bash scripts/screenshots.sh
    SHOTS_OUT=shots/verify/x86_64 bash scripts/screenshots.sh
  '
