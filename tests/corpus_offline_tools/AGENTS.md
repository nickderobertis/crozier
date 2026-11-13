# corpus-offline-tools

- The tools half of the offline proof: `tests/corpus_match/corpus_offline_test.py` with
  `CORPUS_OFFLINE_RECIPES=tools`, running the census, the refusal-class gate and the
  census-fallback samples with sockets denied. It is a project of its own, not a target of
  `corpus-match`, because Nx selects whole projects: as a target there, an edit to those
  tools would also rerun `corpus-match:test-offline`'s golden byte-match, which is never cached.
- Linux only (the denial is seccomp), in the live step after `corpus-match:cold-registry-build`.
