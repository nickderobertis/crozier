#!/usr/bin/env bash
# Publish only the previously verified staged products; compilation stays Mac-side.
set -euo pipefail
staged="${1:?usage: publish-darwin.sh STAGED TAG INTEL_BUNDLE ARM_BUNDLE}"
tag="${2:?tag required}"
intel="${3:?Intel attestation required}"
arm="${4:?ARM attestation required}"
case "$tag" in
    v[0-9]*.[0-9]*.[0-9]*) ;;
    *) echo "error: unsupported release tag '$tag'; use the Cargo.toml version tag" >&2; exit 1 ;;
esac
for target in x86_64-apple-darwin aarch64-apple-darwin; do
    for ext in tar.gz sha256; do
        if [ ! -s "$staged/$tag/crozier-$tag-$target.$ext" ]; then
            echo "error: missing staged $target.$ext; rerun the Darwin build before publishing" >&2
            exit 1
        fi
    done
    if ! compgen -G "$staged/wheels-$target/*.whl" >/dev/null; then
        echo "error: missing staged $target wheel; rerun the Darwin build before publishing" >&2
        exit 1
    fi
done
cp "$intel" "$staged/$tag/crozier-$tag-x86_64-apple-darwin.sigstore.json"
cp "$arm" "$staged/$tag/crozier-$tag-aarch64-apple-darwin.sigstore.json"
if ! gh release upload "$tag" --repo "$GITHUB_REPOSITORY" "$staged/$tag/"* --clobber; then
    echo "error: staged Darwin upload failed; retry this Linux publication job without rebuilding" >&2
    exit 1
fi
