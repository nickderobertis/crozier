# corpus-match

- The offline proof runs `just` recipes with sockets denied, so it runs Nx with
  no socket at all: the daemon off (as the gate keeps it) and plugins loaded
  in-process (`NX_ISOLATE_PLUGINS=false`, since an isolated plugin worker talks
  over one), and it skips the Nx cache so a replay cannot pass for an offline
  run. It moves the ignored corpus caches aside while it runs, so its target
  runs alone (`parallelism: false`).
- Python: `format`, `lint` and `typecheck` only. `test` keeps its own runner and
  these files stay out of the combined coverage floor, because its suites need a
  release build and the denied-socket environment.
- In `live-e2e` the job's first dev build is `cold-registry-build`: an empty
  `CARGO_HOME`, sockets denied, and the real test build. Cargo fingerprints a crate's
  absolute source path, so every later step shares that `CARGO_HOME`. A target here
  or in a sibling tier that compiles crozier depends on it, not on `crozier:build`,
  or the race can put a sockets-up build first. The proof then rejects that build
  and compiles again.
