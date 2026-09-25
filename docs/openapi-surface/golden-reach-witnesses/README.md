# Golden-reach witness evidence

What the golden-reach witness search fetched from GitHub, and why a candidate was
or was not registered. The search itself is described in
[`../../openapi-surface-coverage.md`](../../openapi-surface-coverage.md#golden-reach-row-by-row);
the corpus rows it registered are `CORPUS.md` batch 17.

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
  on, and what became of every candidate that passed all three screens.
- `<source>/records.tsv` — the evidence those lines rest on, in Contract B's
  `key kind subject result file` form. A walked or fetched declarer is a
  `document` row; a declarer becomes a `candidate` only when it is screened.
- `<source>/enumeration.tsv.gz` — a walk's census over every pinned document of
  the source, with the keys each declares or the reason it could not be read.
  `github-publisher-trees/pins.tsv` resolves that source's shared pins to bytes.
- `<source>/probe.jsonl` — every declarer's instrumented `crozier generate`: the
  unreached sites it executed, or how the run ended (a timeout or a crozier
  failure leaves the declarer outstanding). Each row carries the `build` it ran:
  a probe is only meaningful when `src/` equals the commit the instrumented build
  was measured at, since a site's span is read from `src/` and its regions from
  the build. `probe` refuses to run otherwise, and a record counts only the
  current build's rows. Rows with no `build` predate that rule; some ran while
  `src/` had moved on, read another arm's regions, and are counted nowhere.
- `<source>/screens.jsonl` — each screen as it was filed, with its evidence.
- `<source>/queries.jsonl`, `candidates.jsonl` and the guard's logs — the
  text-query sources' calls, as `scripts/witness-search-github.py`'s acquirer
  writes them. Raw downloads at an exact commit sit outside the REST guard by
  ruling and record their commit and digest.
- `queries.tsv` — the two phrasings each text-query source was given per row.
- `handoff.tsv` — candidates that pass every screen but that this node did not
  register: one declaring a `gap` selector, or one crozier cannot yet generate.
  `register-witnesses-continue` takes each up.
