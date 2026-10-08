# workspace

- `coverage` reports on the profiles `crozier:test` left in
  `target/llvm-cov-gate`, under the same cache key. Under a warm Nx cache with a
  cleaned target dir those profiles are gone, so it fails rather than report on
  nothing — rerun with `just test --sweep`.
