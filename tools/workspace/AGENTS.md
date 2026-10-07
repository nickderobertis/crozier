# workspace

The workspace-wide Rust checks, which belong to no one crate: `coverage` (the
95% line floor over `src/` minus `main.rs`, reported from the profiles
`crozier:test` writes, which it depends on), `supply-chain` (`cargo deny` +
`cargo machete` over every member) and `doc` (rustdoc, warnings as errors).
Tagged `type:aggregate`; it has an implicit dependency on `crozier`, so the
affected tier runs `coverage` whenever the crate is affected.

- `coverage` shares `crozier:test`'s inputs, so a replayed test is a replayed
  report. It reads the profiles in `target/llvm-cov-gate`; if they are gone (a
  cleaned target dir under a warm Nx cache) it fails rather than reporting on
  nothing — rerun with `just test --sweep`.
- Lower the floor only with a reason in the root AGENTS.md.
