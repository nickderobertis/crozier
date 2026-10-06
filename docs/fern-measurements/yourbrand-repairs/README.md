# The measurement behind two `src/ir.rs` repairs

Registering `yourbrand-ticketing` (corpus row 308) exposed two places crozier
diverged from its Fern 5.20.0 golden. Each repair rests on what Fern does, so
this directory holds the run that measured it, re-runnable rather than taken on
trust:

- [`probe.yaml`](probe.yaml) — a locally authored 3.0 document. `CreateA` posts
  a schema no other operation uses; `CreateD` posts one `GetD` also answers;
  `CreateE` posts one `PutE` also posts. Each body's `owner` collides with a
  query parameter `owner`. `ListSorted` takes `sortDirection` as
  `oneOf: [{nullable: true, oneOf: [$ref SortDirection]}]`, YourBrand's shape.
- [`measurement.json`](measurement.json) — the pinned run
  `scripts/witness_screen.py`'s `fern_screen_document` took: Fern CLI and
  `fernapi/fern-python-sdk` versions, both exit statuses, and the SHA-256 of
  each redacted log.
- [`fern.log`](fern.log) — those redacted logs.
- [`fern-raw_client.py.txt`](fern-raw_client.py.txt) — Fern's generated
  `src/fern/raw_client.py`, its bytes unedited, kept as text: it is evidence,
  not code this repository runs.

What it shows: `CreateA` sends `"owner": a_owner` while `CreateD` and `CreateE`
send `"owner": owner` — a colliding field is sent from its renamed argument only
where Fern drops the body schema from the type layer — and `ListSorted` types
`sort_direction: typing.Optional[SortDirection]`. `tests/generation.rs`
(`measured_yourbrand_repair_probe_matches_its_fern_output`) renders this probe
with crozier and compares this file through the shared departures engine.
The query-value serialization is a [Fern defect](../../departures/evidence/body-query-parameter-value.md);
crozier keeps the signature but sends the caller’s renamed body argument.

This is no corpus fixture and no coverage probe: it is never a `CORPUS.md` row
and settles no coverage row. The real-specification evidence for both shapes is
`yourbrand-ticketing`'s golden, which byte-matches.
