# `method-name-derivation`

Root cause `method-name-derivation` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** One rule, the certified importer's: the first tag and the operationId are each split into lowercase words (a purely camelCase spelling, `^[a-z]+(?:[A-Z][a-z]+)*$`, at its capitals; anything else at runs of characters other than letters and digits). Equal words make the root client's method, named by the tag; the tag's words leading the id's leave the rest camelCased as the method; anything else keeps the whole id. A summary's full stop breaks words, and one-letter words join as one capital run.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `PingPing` under `ping`, `appInfo` under `app`, `relayGateway-info` and `relay-currentStatus` under `Relay`, `relayGateway-bandPricing` and `relayGateway-all` under `RelayGateway`, the summaries `Serve robots.txt` and `List badges, e.g. a page of them`, and `Lookup__` alone under `Lookup`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `ping_ping`, `deep`, `info`, `version`, `relay_gateway_info`, `currentstatus`, `bandpricing`, `all_`, `serve_robots_txt`, `list_badges_ega_page_of_them` and the root client's `lookup`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier failed outright: `Lookup__` split at its underscore left an empty method, which `ruff format` rejected; on the handed-off documents it wrote `ping`, `app_info`, `gateway_info` (for `aiGateway-info` under `AI`), `serve_robotstxt` and `…_eg_a_…`.
`crozier compare` could therefore compare no tree at all.

**Change.** `src/ir.rs::tag_location` (with `TagLocation`, `camel_join`, `id_spells_tag`) replaces the per-shape prefix heuristics in `method_from_groupless_id`, `endpoint_module` and `module_title`; `src/naming.rs::summary_identifier` breaks words at a full stop. The same rule holds `operation-id-tag-prefix-digit` and `single-operation-tag-root-method`.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
