# corpus-match

- `match.sh` lists one `cargo test` per registered corpus. crozier-e2e's
  `every_registered_corpus_is_wired_into_the_gate` holds that list to the
  registry in both directions: add a corpus there and here together.
- The offline proof runs `just` recipes with sockets denied, so it runs Nx with
  no socket at all: the daemon off (as the gate keeps it) and plugins loaded
  in-process (`NX_ISOLATE_PLUGINS=false`, since an isolated plugin worker talks
  over one), and it skips the Nx cache so a replay cannot pass for an offline run. It moves the ignored corpus caches
  aside while it runs, so its target runs alone (`parallelism: false`).
