# workspace

- `coverage` and `crozier:test` read one named input (`crateTestRun` in
  `nx.json`), so a replayed test is a replayed report. It reads the profiles
  `crozier:test` left in `target/llvm-cov-gate`; if they are gone (a cleaned
  target dir under a warm Nx cache) it fails rather than reporting on nothing — rerun with `just test --sweep`.
