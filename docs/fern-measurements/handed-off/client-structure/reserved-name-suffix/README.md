# `reserved-name-suffix`

Root cause `reserved-name-suffix` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A path parameter `uuid` is `uuid_` on every operation; a model property `dict` is `dict_` (pydantic's `BaseModel.dict()`, as `copy` and `json` already were); and a whitespace-separated word that folds to nothing keeps its separator, so `viability (%)` is `viability_`, a lone `moisture (%)` is `moisture_` and `seed % weight` is `seed__weight`. It is not a de-duplication: `lotCode` and `lotCode_` both stay `lot_code`, as the certified pair writes them (and as corpus row `ere-ps-app` already shows).

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `GET` and `PUT /packets/{uuid}` (the `PUT` with a JSON body used once), and a `Packet` model with `viability`, `viability (%)`, `dict`, `moisture (%)`, `seed % weight`, `lotCode` and `lotCode_`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `uuid_` on both operations, and `viability_`, `dict_`, `moisture_`, `seed__weight` and two `lot_code` fields.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier wrote `uuid` on the `PUT` beside its dropped body, `dict`, and two `viability` fields.
`crozier compare` against the tree then reported these files differing:
['reference.md', 'src/fern/packets/client.py', 'src/fern/packets/raw_client.py', 'src/fern/types/packet.py'].

**Change.** `src/ir.rs` un-suffixes a path parameter beside a dropped body only where the suffix came from a collision; `src/naming.rs::model_field_name` protects `dict`; `src/naming.rs::field_snake_case` keeps an empty word's separator after the first word.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
