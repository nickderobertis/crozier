# corpus-fetch

- The corpus scripts' suites that run real `curl` (`tools/corpus/fetch-corpus.sh`
  through `corpus_sources.py vendor|audit` and the remote-`$ref` pin mechanism)
  against a loopback server each suite starts. They are a project of their own
  so an edit to an offline corpus script, or to its offline lint tests, never
  pays for them; a change to a script they exercise reaches them through their
  inputs.
- No case reaches an external host. The synthetic root they fetch into is
  `tools/corpus/tests/corpus_sources_test.py`'s, imported, so the two halves
  build the same tree.
