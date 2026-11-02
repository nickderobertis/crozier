# `media-type-recognition`

The handed-off root cause `media-type-recognition` from the bodies-and-paths record ([`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md)), which names it as blocking katana, runzero (input-entry), runzero (openapi.json), osf.io; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a content key is JSON when it contains json anywhere (case-sensitively) or is exactly */*, so text/json and Application/json bodies are spread and sent under their own key, and a */* response is typed from its schema.

`openapi.yml` ("Seed Bank Catalogue") was authored from scratch for this measurement. It holds a `text/json` body (`record_deposit`), a capitalised `Application/json` body (`record_germination`) and a `*/*` response (`get_vault`). `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/media-type-recognition` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier dropped the `text/json` body entirely (`record_deposit()` took no fields, and `runtime.txt` shows the call failing) and recognised only lower-case `application/...json` keys. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**On the wire.** `runtime.txt` records `crates/crozier-e2e/tests/e2e/bodies_media_wire.py` driving the certified pair's SDK, crozier's repaired SDK and crozier's SDK from before the repair against a local HTTP server: each step's request (method, path, `content-type`, body or multipart parts) or returned value. The certified and repaired SDKs agree line for line; `sdk_env_bodies_media_wire_journeys_hold_for_crozier_and_fern` re-runs the first two and requires every line to be one `runtime.txt` records.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
