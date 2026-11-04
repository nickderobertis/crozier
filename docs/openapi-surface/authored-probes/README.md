# Authored combination measurements

The [tier matrix](evidence-tiers.tsv) decides all 31 original authored cases:
six naming cases have moved to `../handwritten/` with their covers and certified
trees; the remaining 25 are **open combinations**, not undecided tiers. The
[bounded search](../witness-search-ledger-remainders/README.md#authored-verdicts)
names each missing population and every unscreened real declarer. Ruling
`exhausted-combination-fallback` keeps those combinations open until their
search finishes. They are neither admitted hand-written covers nor limitations.

Each remaining case holds `openapi.yml`, `fern.log` and `fern-expected/`.
The log records the certified pair's check and generation exits. The complete
comment-stripped tree is generated through `just fern-references authored-probes --version 5.41.3` at the certified pair in `assets/scaffolding/metadata.json`.
Nothing in the expected tree is edited to repair a difference.

`authored_probe_measurements_match_fern` drives the real CLI and byte-compares
each remaining case against that tree. It proves only the measured document's
output, not real-specification evidence or an admitted combination fixture.
The census suite validates the versioned matrix, each source's SHA-256 and
selector, and the open-case counts in the coverage report. The hand-written
gate separately proves the six moved naming cases.
