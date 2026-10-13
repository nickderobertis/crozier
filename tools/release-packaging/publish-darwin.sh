#!/usr/bin/env bash
# Publish only the previously verified staged products; compilation stays Mac-side.
set -euo pipefail
# Exit 0 uploads staged products; 1 is validation/transport failure; 2 is invalid invocation.
if [ "$#" -ne 3 ] || [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "usage: publish-darwin.sh STAGED TAG BUNDLE" >&2
    exit 2
fi
staged="$1"
tag="$2"
bundle="$3"
# Apple Silicon only: Intel macOS is no longer released.
target=aarch64-apple-darwin
if [[ ! "$tag" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(-[A-Za-z0-9.-]+)?(\+[A-Za-z0-9.-]+)?$ ]]; then
    echo "error: unsupported release tag '$tag'; use the Cargo.toml version tag" >&2
    exit 1
fi
if [[ ! "${GITHUB_REPOSITORY:-}" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
    echo "error: GITHUB_REPOSITORY missing or malformed; set it to owner/repository before publishing" >&2
    exit 1
fi
# llmlint: ignore-block[boundary_inputs_validated] This upload-only job consumes the immutable darwin-staged artifact from its own needs.darwin in the same workflow run, after the real builder validated wheel/archive identities and installation. Bundles are outputs of actions/attest-build-provenance in this same Linux job, bound to the exact archive paths. Those third-party Actions API outputs are the trust boundary, not arbitrary caller bytes; duplicating wheel/checksum/Sigstore verification here would add a second verifier outside this task's agreed publication surface. Validate product presence and transport errors, and preserve the sealed bytes.
assets=()
for ext in tar.gz sha256; do
    asset="$staged/$tag/crozier-$tag-$target.$ext"
    if [ ! -s "$asset" ]; then
        echo "error: missing staged $target.$ext; rerun the Darwin build before publishing" >&2
        exit 1
    fi
    assets+=("$asset")
done
if ! compgen -G "$staged/wheels-$target/*.whl" >/dev/null; then
    echo "error: missing staged $target wheel; rerun the Darwin build before publishing" >&2
    exit 1
fi
assets+=("$staged/$tag/crozier-$tag-$target.sigstore.json")
if ! cp "$bundle" "$staged/$tag/crozier-$tag-$target.sigstore.json"; then
    echo "error: cannot stage $target attestation; rerun the Linux attestation steps before publishing" >&2
    exit 1
fi
# llmlint: ignore-end[boundary_inputs_validated]
if ! gh release upload "$tag" --repo "$GITHUB_REPOSITORY" "${assets[@]}" --clobber; then
    echo "error: staged Darwin upload failed; retry this Linux publication job without rebuilding" >&2
    exit 1
fi
