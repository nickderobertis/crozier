# `json-binary-body-snippet`

The handed-off root cause `json-binary-body-snippet` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A weaving guild's `PUT /patterns/{patternId}/draft` sends a required body offered as `application/json` and `text/plain`, each `{type: string, format: binary}`; `PUT /patterns/{patternId}/chart` offers only the JSON one.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/json-binary-body-snippet` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

Both methods take `request: bytes` and send it with `json=request`. The certified pair's docstrings and `reference.md` pass `request="string"`; crozier passes `request=b"string"` in every writer, as the catalogued `binary-json-body-example` departure (kind `fern-defect`) already corrects. `runtime.txt` (its `binary-json-body-example` sections) records the certified examples failing strict validation against the methods' actual `bytes` annotation and crozier's passing it, both SDKs sending the bytes as JSON.

**Verdict: `fern-defect-departed` (`binary-json-body-example`, catalogued before this node).** The record's appveyor document differs because that departure's `reference.md` region did not apply there: the same file also differs in an enum field's example (`PermissionName`, a value naming no member), which no departure explains, so the region's window fails (`../README.md`). With it applied, crozier's tree for this document byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `catalogued_snippet_defects_are_what_crozier_writes` reads the line on both sides; `snippet_departures_and_repairs_hold_only_their_lines` fails a different certified spelling beside it; `sdk_env_snippet_defect_journeys_hold_for_crozier_and_fern` reruns the `runtime.txt` journey (`crates/crozier-e2e/tests/e2e/snippet_rendering_wire.py`) over both SDKs.
