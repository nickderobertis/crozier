# workspace

- `coverage` reports on the profiles `crozier:test` left in
  `target/llvm-cov-gate`, under the same cache key. Under a warm Nx cache with a
  cleaned target dir those profiles are gone, so it fails rather than report on
  nothing — rerun with `just test --sweep`.
- `test` reconciles release-plz.toml's `release = false` roster with the
  workspace's `publish = false` members (through `cargo metadata`); adding a
  test-only crate means adding its release-plz entry in the same change.
