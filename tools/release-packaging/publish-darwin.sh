#!/usr/bin/env bash
# Publish only the previously verified staged products; compilation stays Mac-side.
set -euo pipefail
staged="${1:?usage: publish-darwin.sh STAGED TAG INTEL_BUNDLE ARM_BUNDLE}"
tag="${2:?tag required}"
intel="${3:?Intel attestation required}"
arm="${4:?ARM attestation required}"
if [[ ! "$tag" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(-[A-Za-z0-9.-]+)?(\+[A-Za-z0-9.-]+)?$ ]]; then
    echo "error: unsupported release tag '$tag'; use the Cargo.toml version tag" >&2
    exit 1
fi
if [[ ! "${GITHUB_REPOSITORY:-}" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
    echo "error: GITHUB_REPOSITORY missing or malformed; set it to owner/repository before publishing" >&2
    exit 1
fi
assets=()
for target in x86_64-apple-darwin aarch64-apple-darwin; do
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
done
for target in x86_64-apple-darwin aarch64-apple-darwin; do
    source="$intel"
    [ "$target" != aarch64-apple-darwin ] || source="$arm"
    if ! cp "$source" "$staged/$tag/crozier-$tag-$target.sigstore.json"; then
        echo "error: cannot stage $target attestation; rerun the Linux attestation steps before publishing" >&2
        exit 1
    fi
done
if ! gh release upload "$tag" --repo "$GITHUB_REPOSITORY" "${assets[@]}" --clobber; then
    echo "error: staged Darwin upload failed; retry this Linux publication job without rebuilding" >&2
    exit 1
fi
