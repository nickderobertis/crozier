# `multipart-scalar-union-part-encoding`

The handed-off root cause `multipart-scalar-union-part-encoding` from the schemas record ([`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md)), which names it as blocking Grafikart/filemanager-element; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a multipart part that is a union of form primitives is sent as the bare value in data=, neither JSON-encoded nor converted.

`openapi.yml` ("Map Room Drawer Index") was authored from scratch for this measurement. It holds a multipart part typed `oneOf: [string, integer]` beside a file part. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/multipart-scalar-union-part-encoding` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier JSON-encoded the part (`json.dumps(jsonable_encoder(drawer))`, `"A-12"` on the wire, as `runtime.txt` shows); the certified pair sends the bare value. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**On the wire.** `runtime.txt` records `crates/crozier-e2e/tests/e2e/bodies_media_wire.py` driving the certified pair's SDK, crozier's repaired SDK and crozier's SDK from before the repair against a local HTTP server: each step's request (method, path, `content-type`, body or multipart parts) or returned value. The certified and repaired SDKs agree line for line; `sdk_env_bodies_media_wire_journeys_hold_for_crozier_and_fern` re-runs the first two and requires every line to be one `runtime.txt` records.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
