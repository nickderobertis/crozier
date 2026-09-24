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
