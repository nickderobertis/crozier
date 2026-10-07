# corpus-match

- `match.sh` lists one `cargo test` per registered corpus. crozier-e2e's
  `every_registered_corpus_is_wired_into_the_gate` holds that list to the
  registry in both directions: add a corpus there and here together.
- The offline proof runs `just` recipes with sockets denied, so it runs Nx with
  no network: the gate keeps the Nx daemon off, and the proof skips the Nx cache
  so a replay cannot pass for an offline run. It moves the ignored corpus caches
  aside while it runs, so its target runs alone (`parallelism: false`).
