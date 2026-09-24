# Relative-file Path Item search: GitHub code index

This is discovery evidence for `relative-file-ref`, whose outcome is
`witness-found`. The two REST `/search/code` requests used the guarded
`code_search` bucket, with `cost=1` each. Their exact query strings and counts
are in `results.tsv`; `acquisition.json` and `acquisition-2.json` are the raw
first-page responses. The first reported 104 total and returned 100; the second
reported 136 total and returned 100. `results.tsv` accounts for all 200 returned
entries. A result left uninspected after the Raybot golden matched is marked as
such, never as a negative census or licence screen.

`raybot-census.json` and `kitcc-census.json` are outputs of the real census
selector engine on the two candidates taken through the screen. `screens.tsv`
records their licence, immutable revision and Fern acceptance. Raybot is the
registered witness; KITCC was refused by Fern. `quota-waits.jsonl` is empty:
the authenticated code-search acquisitions did not wait on a quota bucket.
