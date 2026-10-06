# `body-query-parameter-value`

**Kind:** `fern-defect`, as the user ruled. A JSON body property and query
parameter share a name. Fern renames the body argument in the signature, then
sends the query value under the body's key; the body argument is ignored.

## Certified real specification

The Waylay query API, corpus row 329, at immutable commit
`8ab6c18e10f96c3665dbb849ebe2193c16a1659c`. The publisher's `LICENSE.txt`
at that same commit grants redistribution. Route A generated the complete
comment-stripped golden at Fern CLI 5.67.1 and Python SDK generator 5.20.0;
`fern generate --group python-sdk --local --preview --force` exited 0 and
reported `All checks passed` and `Finished`, writing 174 files.

Generation used `TMPDIR` outside the crozier tree, with
`GIT_CEILING_DIRECTORIES` pointing to that directory so an enclosing repository
could not stamp its commit into Fern's metadata. No Fern artifact was edited.

`execute_query` accepts both `resource` and `query_input_resource`. Its query
mapping uses `resource`; its JSON mapping also uses `resource`. The correct
body mapping uses `query_input_resource`. Converted colliding properties have
the same substitution inside their converter, whose annotation stays unchanged.

## Run the generated clients

The [wire journey](body-query-parameter-value.py) imports the generated package
and sends real requests through httpx's transport boundary. It drives both
sync and async clients through a 200, a 400 and another 200, checking typed
responses, the raised error and recovery. It observes the URL and JSON body
separately. Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --no-project --python 3.12 --with httpx --with pydantic \
  python docs/departures/evidence/body-query-parameter-value.py \
  tests/fixtures/waylay-queries/expected/src query-value
```

Result, exit 0:

```text
sync and async: query=query-value, body=query-value; 400 raises and next request recovers
```

Asserting `body-value` against that same Fern package exits 1 and reports six
captured requests whose query and body both hold `query-value`. This is the
induced failure proving the assertion detects the defect.

Generate crozier's SDK from the committed source with package `fern` and project
`default_package_name`, then run the same script with that SDK's `src` directory
and expectation `body-value`. Result, exit 0:

```text
sync and async: query=query-value, body=body-value; 400 raises and next request recovers
```

The deterministic golden comparison and the real `crozier compare` journey
accept only this catalogued substitution. The comparison journey also changes
one more line in the same raw client and must fail; its departure is reported by
id, file and line. The per-golden ledger pins every application.
