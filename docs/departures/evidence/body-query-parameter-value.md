# `body-query-parameter-value`

**Kind:** `fern-defect`, as the user ruled. A JSON body property and query
parameter share a name, or a body property and a header share an argument
name. Fern renames the body argument in the signature, then sends the query or
header value under the body's key; the body argument is ignored.

## Certified real specification

The Waylay query API, corpus row 329, at immutable commit
`8ab6c18e10f96c3665dbb849ebe2193c16a1659c`. The publisher's `LICENSE.txt`
at that same commit grants redistribution. The manually dispatched **Fern
goldens** workflow generated the complete comment-stripped golden,
`tests/fixtures/waylay-queries/expected/`, at Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3 (its `.fern/metadata.json` records both):
174 files beside the `.crozier-fern-golden.json` provenance record, which pins
the source URL at that commit. No Fern artifact was edited.

`execute_query` accepts both `resource` and `query_input_resource`
(`src/fern/execute/raw_client.py` line 50). Its query mapping uses `resource`
(line 165); its JSON mapping also uses `resource` (line 177, the golden's
`body-query-parameter-value` row). The correct
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

## Header collisions

The same substitution happens with a header, measured at Fern CLI 5.216.0 with
`fernapi/fern-python-sdk` 5.42.0 (its `.fern/metadata.json` records both). The
measurement document
[`header-body-collision/openapi.yml`](../../fern-measurements/bodies-responses/header-body-collision/openapi.yml)
declares `runActionBatch`: a nullable `Idempotency-Key` header beside the
`$ref ActionBatchRequest` body, whose nullable `idempotency_key` property the
header's argument name claims. `ActionBatchRequest` is also the body of
`previewActionBatch`, so its model survives and Fern does not refuse the
document. In the committed tree,
[`fern-expected/src/fern/actions/raw_client.py`](../../fern-measurements/bodies-responses/header-body-collision/fern-expected/src/fern/actions/raw_client.py),
`run_action_batch` takes `idempotency_key` and
`action_batch_request_idempotency_key` (lines 143-144), maps the header from
`idempotency_key` (line 173) and sends `"idempotency_key": idempotency_key` in
the JSON (line 169, and line 402 in the async client). The ticket's own real
specification, modal-computer-use's `docs/openapi.json` (witness
`ebe5c74e88881756ca72b850a19189c8f410ceb79089080a602cf9207da10db5`), does the same
on `POST /v1/actions/run` at this pair in both enum modes. The same document's
`runAction` and `queueAction`, whose bodies are not shared, are the control:
both generators send each value in its own place there.

The executed evidence is the runtime wire suite's
`tests/runtime/test_header_body_collision.py`, driven by
`sdk_env_crozier_matches_fern_runtime_behavior`. Its
`shared_body_header_collision` journey (`tests/runtime/_recorder.py`) calls
`run_action_batch` with `idempotency_key="header-value"` and
`action_batch_request_idempotency_key="body-value"` through an injected
`httpx.MockTransport`, sync and async, and records each request:

```text
fern sync header Idempotency-Key = header-value | body = {"actions": ["fire"], "idempotency_key": "header-value"}
fern async header Idempotency-Key = header-value | body = {"actions": ["fire"], "idempotency_key": "header-value"}
crozier sync header Idempotency-Key = header-value | body = {"actions": ["fire"], "idempotency_key": "body-value"}
crozier async header Idempotency-Key = header-value | body = {"actions": ["fire"], "idempotency_key": "body-value"}
```

`test_the_certified_pair_sends_the_header_value_as_the_body` asserts the
certified pair's recording, and that the two requests differ in nothing but that
body value; `test_crozier_sends_a_shared_bodys_value_beside_the_header` holds
crozier to the header value in the header and the body value in the body. The
golden comparison
(`crates/crozier-e2e/tests/e2e/bodies_responses.rs`) accepts the substitution
only through this departure, which the ledger pins at those lines.
