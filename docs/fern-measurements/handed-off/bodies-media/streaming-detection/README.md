# `streaming-detection`

The handed-off root cause `streaming-detection` from the bodies-and-paths record ([`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md)), which names it as blocking generative-manim; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** any 2xx response offering text/event-stream and nothing else streams the whole method as SSE, typed by the first success response Fern reads.

`openapi.yml` ("Loom Pattern Weaver") was authored from scratch for this measurement. It holds `weave_pattern` answers a `200` JSON `WovenPattern` and a `207` that offers only `text/event-stream`; `get_pattern` is a plain JSON read beside it. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/streaming-detection` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier read only the `200`, so `weave_pattern` returned one `WovenPattern` and its README had no Streaming section; the certified pair streams `typing.Iterator[WovenPattern]` and documents it. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**On the wire.** `runtime.txt` records `crates/crozier-e2e/tests/e2e/bodies_media_wire.py` driving the certified pair's SDK, crozier's repaired SDK and crozier's SDK from before the repair against a local HTTP server: each step's request (method, path, `content-type`, body or multipart parts) or returned value. The certified and repaired SDKs agree line for line; `sdk_env_bodies_media_wire_journeys_hold_for_crozier_and_fern` re-runs the first two and requires every line to be one `runtime.txt` records.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
