# Golden-reach witness evidence

What the golden-reach witness search fetched from GitHub, and why a candidate was
or was not registered. The search itself is described in
[`../../openapi-surface-coverage.md`](../../openapi-surface-coverage.md#golden-reach-row-by-row);
the corpus rows it registered are `CORPUS.md` batch 19.

- `acquisitions.jsonl` — every document, licence file, repository record and
  commit this search read from GitHub, one line per call, with its URL, HTTP
  status, and for a fetched body its SHA-256 and size. Every call went through
  [`../../../scripts/rate_limit_guard.py`](../../../scripts/rate_limit_guard.py) by way
  of `scripts/witness-acquire-github.py`.
- `rate-limit-calls.jsonl` — the guard's own record of each admitted call: host,
  REST bucket, the reservation it held, and the response status. A wait the guard
  made would be in `rate-limit-waits.jsonl`; none of these calls needed one, so
  that file does not exist.

A registered candidate's pin, licence and Fern screen are its `CORPUS.md` row. A
screened candidate Fern refused is recorded, with the diagnostic Fern printed, in
`CORPUS.md`'s DROPPED list so nobody screens it again.

## Arm searches

Each owned `golden` row with a handling site still unreached has an arm search:
the six declared sources searched for a real-world document that declares the
row and executes the site. `scripts/golden-reach-search.py` does each stage and
files it here.

- `searches/<key>.md` — the row's record, linked from its reach cell: one
  Contract B line per declared source, a per-source tally of the declarers and how
  the instrumented run fared on each (its `outstanding` column is what the
  search still owes), whether `src/` has moved since the build those probes ran
  on, and what became of every candidate that passed all three screens. A row a
  registered witness has since reached keeps the arm its record searched for and
  reads `witness-found`; `probe` still probes its declarers on the counted
  build, against that arm as it resolves in today's `src/` (or the row's
  handling sites, where a repair restructured the whole arm away).
- A `searches/<key>.md` with a `### Configuration gate` section reads
  `config-gated`: the arm runs only under a generation setting no probe sets,
  so no search ran for it. In place of the per-source lines, the record states
  the setting and the code path that shows it, the gate as `just
  handwritten-reach` measured it on a hand-written fixture (with the setting
  and without it), and per source the committed files that show the key was
  never walked or queried there. `outstanding`, `retire` and `fern-rescreen`
  pass it by, and `RankedBacklogTests` checks its three parts.
- `<source>/records.tsv` — the evidence those lines rest on, in Contract B's
  `key kind subject result file` form. A walked or fetched declarer is a
  `document` row; a declarer becomes a `candidate` only when it is screened.
- `<source>/enumeration.tsv.gz` — a walk's census over every pinned document of
  the source, with the keys each declares or the reason it could not be read.
  `github-publisher-trees/pins.tsv` resolves that source's shared pins to bytes.
- `<source>/census-refused.tsv` — the documents the census could not read that
  a full standard parser refuses too: Python's `json` module for a `.json`
  document, ruamel.yaml (YAML 1.2) for YAML. Each line names the document, its
  digest, the parser and its version, and the verdict — `syntax` with the
  parser's error, or `not-openapi` when the document parses but names no
  `openapi` or `swagger` version. A refused document is no description a
  witness could be, so it is not outstanding; one only the census fails on
  stays outstanding as the census's own bug until `recensus` reads it.
  `refuse` writes it (run as `uv run scripts/golden-reach-search.py refuse`,
  whose inline metadata pins ruamel.yaml), and a refusal never makes a search
  `exhausted` on its own.
- `<source>/census-fallback.tsv` — the documents the census's stdlib loader
  refuses that ruamel.yaml reads as one description, each with its digest and
  the loader that read it. `recensus` counts them with the census's own
  object-model walk over that reading, so each leaves the unread list as a
  read document does; it also counts a query source's every fetched document
  again, so a loader repair reaches them. The fallback is the search's alone:
  the registered-corpus census and `just check` read with the stdlib loader,
  and `just test-census-fallback` holds the two readings to identical counts
  on every registered YAML source.
- `<source>/probe.jsonl` — every declarer's instrumented `crozier generate`: the
  unreached sites it executed, or how the run ended (a timeout or a crozier
  failure leaves the declarer outstanding). Each row carries the `build` it ran:
  a probe is only meaningful when `src/` equals the commit the instrumented build
  was measured at, since a site's span is read from `src/` and its regions from
  the build. `probe` refuses to run otherwise, and a record counts only the
  current build's rows. Rows with no `build` predate that rule; some ran while
  `src/` had moved on, read another arm's regions, and are counted nowhere.
- `<source>/records.tsv`'s `candidate` rows are the declarers screened because a
  probe once found them reaching the arm. `retire` keeps every one and marks
  the ones the counted build no longer supports: a document the census no
  longer counts reads `census 0`, and one whose probe of the counted build
  reaches no site reads its census count followed by `its probe of build <B> in
  probe.jsonl reaches no unreached site`. Contract B's gate accepts that mark
  only where `probe.jsonl` carries the probe it cites, and then reads the row
  as no candidate.
- A candidate reaching the arm and passing every screen that is a test
  fixture — a document written to exercise a tool — is declined in its screen
  as `not a real-world specification: a test fixture written to exercise a
  tool — <repository, path at the pinned commit, and what makes it one>`. It is
  hand-written, so it is no witness, and an arm whose only such candidates are
  fixtures reads `exhausted` with no real witness (the manager's ruling to
  `thin-goldens-continue-2`, which the gate names).
- `<source>/fern-rescreen.jsonl` — Fern's screen taken again, measured, for each
  reaching declarer whose licence and ref pass and whose earlier Fern screen
  recorded no exit status: `fern-rescreen` runs `fern check` in the workspace
  `scripts/generate-fern-fixture.sh` scaffolds, and where that exits 0, `fern
  generate`, at the Fern CLI and python-sdk versions the goldens'
  `.fern/metadata.json` record. Each line names the document
  and its digest, each command's exit status, the first diagnostic Fern
  printed and the digest of its full output, and the screen is re-filed from it.
- `<source>/screens.jsonl` — each screen as it was filed, with its evidence.
  The `github-code-search` licence screens rest on each repository's licence at
  the pinned commit; 40 of those REST lookups first went out on 2026-09-26
  without a credential, which `rate-limit-calls.jsonl` shows against GitHub's
  unauthenticated limit of 60. All 108 repositories were looked up again on
  2026-09-27 with the request and the guard reading the same `GH_TOKEN` (108
  calls against the 5,000 limit), and each came back identical — status, SPDX
  identifier, licence path and blob — so no screen moves.
- `<source>/queries.jsonl`, `candidates.jsonl` and the guard's logs — the
  text-query sources' calls, as `scripts/witness-search-github.py`'s acquirer
  writes them. Raw downloads at an exact commit sit outside the REST guard by
  ruling and record their commit and digest.
- `queries.tsv` — the two phrasings each text-query source was given per row.
- `outstanding.tsv` — every item a record's `outstanding` column counts, one
  line each: the row, the source, the document, what blocks it (unprobed on the
  record's build, a probe that timed out or left no profile, or the census's
  reason it could not read a document no full parser refused), the build, and the `src/` commits since
  that build that make every probe of it owe a fresh `just golden-reach`. It is
  the continuation node `thin-goldens-continue`'s work list. `outstanding`
  regenerates it from the records and probes; `RankedBacklogTests` holds each
  `(row, source)` group to its record's count.
- `handoff.tsv` — candidates that pass every screen but that this node did not
  register: one declaring a `gap` selector, or one crozier cannot yet generate.
  `register-witnesses-continue` takes each up.
