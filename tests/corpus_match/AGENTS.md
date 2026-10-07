# corpus-match

The real-world corpus byte-match over the committed sources (`match.sh`, also
`--strict` with Fern-strict compatibility on) and its offline proof
(`corpus_offline_test.py`: the real recipes with sockets denied and the ignored
caches absent; `corpus_offline_recovery_test.py`: a failed run restores the
cache it found). `corpus_surface_census_test.py` is the census check the match
runs. Promoted (`tier:promoted`); CI's live-e2e leg runs every target.

- `match.sh` lists one `cargo test` per registered corpus. crozier-e2e's
  `every_registered_corpus_is_wired_into_the_gate` holds that list to the
  registry in both directions: add a corpus there and here together.
- The offline proof runs `just` recipes, so it runs Nx with sockets denied; the
  gate keeps the Nx daemon off, which is what lets it.
