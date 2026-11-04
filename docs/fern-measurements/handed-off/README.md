# Handed-off measurements

The source records define the root causes:
[bodies and paths](../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md),
[operations and extensions](../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md),
and [schemas](../../openapi-surface/witness-search-fixture-only-schemas/README.md).

Each area is a tab-separated file with a header and exactly these columns,
in order: `source`, `root_cause`, `verdict`, `measurement`, `departure`, `note`.
`source` names the source record or follow-up ticket; `root_cause` preserves
its spelling (including numbered `R7`-style causes). `measurement` names the
repository-relative measurement directory; `departure` names its catalog entry,
or `-`; `note` states the measured rule on one line.

The closed verdict set is `parity-gap-repaired`, `already-matching`,
`fern-defect-departed`, `user-ruling`, `default-matched`,
`ruling-applied:<ruling id>`, and `refusal-kept`. A `user-ruling` note names
the ruling; `ruling-applied:<ruling id>` applies that ruling's principle to
a different cause. Every verdict is decided.

The area records are [bodies and media](bodies-media.tsv),
[client structure](client-structure.tsv),
[document acceptance](document-acceptance.tsv),
[empty SDK documents](empty-sdk-documents.tsv),
[example values](example-values.tsv),
[snippet rendering](snippet-rendering.tsv),
[type declarations](type-declarations.tsv), and
[union modelling](union-modelling.tsv), plus the
[follow-up ticket area](follow-up-tickets.tsv). Additional causes found while
re-measuring, including the non-table causes moved here under the planner’s
ruling, are [remeasure](remeasure.tsv); their notes retain their original
source records and evidence directories.

## Final document measurement

[`documents.tsv`](documents.tsv) records all 146 source hashes; its header
names the fields of each document record.
The planner's land-now amendments allow `differs` and `registration-incomplete`
only with a corresponding [`residuals.tsv`](residuals.tsv) record; the latter
means the `python_enums` comparison matches but the literals overlay is missing.
The residual record’s header names its fields.
A registration residual names `expected-literals/`, rather than claiming a file
already differs. Newly named residual causes describe missing behavior in their
note; they are repair work, not undecided triage verdicts.

The four disjoint outcomes are **7 registered** (5 new, 2 pre-existing),
**36 decided** (26 `refused-by-ruling`, 10 `byte-matches-not-admissible`),
**102 listed residuals** (28 `differs`, 74 `registration-incomplete`), and
**1 could-not-check** (lolesports' evaluated valid-OpenAPI exception: its useful
crozier SDK cannot byte-match the certified pair's empty scaffold). They sum to
146. Each comparison record names the exact command and source digest; refusals
include both crozier modes and the certified pair's diagnostic. License evidence
is retained beside the measurement, with the rule stated only in
[`docs/corpus-licensing.md`](../../corpus-licensing.md).

The comparison binary was copied before the behavior-preserving boolean
simplification clippy requested in `name_refusals`; the nine focused SDK
journeys passed again after that simplification. No later edit changes generator
behavior. Prior area reports describe their own repair-node measurements;
`documents.tsv` is the present status of each real document.

## Coverage measurement provenance

The golden-only measurement first ran all 319 tests at `29df35b9c`: 317
passed, and AMRC and OpenIAP found departure-ledger pin drift. After the
existing ledger writer regenerated those pins, the two failed tests were
measured again at `2e6bdfd88` and passed. Their exports join the 317 successful
exports from the full run. The generator's `src/`, templates and assets trees
are identical across these commits, and SHA-256 checks of both instrumented
executables match before and after the scoped completion. The ledger header
names the last, source-equivalent measurement commit. Both instrumented golden
runs held the host measurement lock. The earlier hand-written reach run
finished before that lock requirement was delivered. The later retirement of
`thermostat-nullable-member` moved its unchanged source and certified tree into
the probe inventory and reran its union and probe gates and hand-written reach.
The closed-empty-object request-property site now names `base_type_ref`, the
inline-property path the registered witness actually executes, rather than the
component-field builder. Its reach was rejoined from the same 319 exports.
The census snapshot was regenerated after the Hashicorp registration-name fix:
it includes all 319 registered sources (31 original and 288 corpus sources).
The earlier 318-source snapshot omitted that witness and is superseded. The
feature search-verdict prose was derived with the existing `region_rows` helper
(36 exhausted, 74 search-incomplete); the scenario index rows for the two
retired feature fixtures and the retained nullable-union probes were derived
through the existing source, settings, catalog and TSV helpers.

Including the Hashicorp witness also superseded the sole cover of
`harbor-nullable-inline-object`. Its unchanged source and certified tree moved
into the probe inventory and keep both union-mode comparisons. Under the
planner’s scoped-regeneration approval, the existing reach-ledger reader and
serialization dropped only that cover’s contribution: the other 116 measured
rows retain identical sources, sites and measurements. The arm headline and
feature aggregates were then regenerated from the remaining evidence.
The remaining reach-ranking rows, blind-spot arm counts and scenario summary
were also regenerated through their existing readers. The enum-name
compatibility annotation preserves the source line count and changes no
generation behavior. The census scalar mirror now follows string datetime
overrides; its Rust-body fingerprints were regenerated after review,
and a new complete corpus census produces identical rows over the same 319
sources.

## Newly admitted documents

- `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `748ff9ba7fba914537047a5198e24da9d32e64608cede2a67f9561cd53cee743` | 3479 (vtex-marketplace-protocol)
- `Grafikart/filemanager-element:openapi.yml@af6fc5f6be961b14b2b2a218ddadac1fe6bbeb46` | `e36a74ce6e86cf994ab1dbc54e4103b8d500590c160a54f61b749345462f2d28` | 5050 (remeasured-grafikart-filemanager-element-e36a74ce)
- `arawa/workspace:openapi.json@926f6093e68261c94f4dcd536b0c4451f2013ee8` | `0c8259f6f991dbd2985005b14731e7df52d59496a17249394fefcbaa2ef52689` | 5051 (remeasured-arawa-workspace-0c8259f6)
- `clencyc/MozillaFestivalBackend:openapi.yaml@e70f0150f414d216743311be79d005d900ab81f1` | `b2264b38f17b99bd722b94f94029916705be39cd6359b1b341bc8696f29e6092` | 5052 (remeasured-clencyc-mozillafestivalbackend-b2264b38)
- `hashicorp/terraform-plugin-codegen-openapi:internal/cmd/testdata/edgecase/openapi_spec.yml@55b2a49774f094d0d8aff834bce5eabe9e8a7345` | `1f6aea4c5e340b482e6441711f83780f2a6026a4755452530094d160747d2427` | 5053 (remeasured-hashicorp-terraform-plugin-codegen-openapi-1f6aea4c)
- `membrane/api-gateway:core/src/test/resources/openapi/specs/oas31/boolean-schemas.yaml@c24a0204aaa9d07ee5237c44e43e8e9ef4129f2c` | `8340f5da585023194c7154cb6e72a111e5643bb9cd3364cb75e0eacb0b1fcb89` | 5054 (remeasured-membrane-api-gateway-8340f5da)
- `ourofoundation/wrappers:nixtla/timegpt/timegpt-openapi.json@79688dd65e7fb2fb670ad30b01b5db5208c1d928` | `9165e7b94aa026f4924cc6bd8bc627719680fc028af864e0c2649168ded7705b` | 4301 (nixtla-timegpt)

The [follow-up ticket area](follow-up-tickets/README.md) reconciles its ticket-URL
rows as its own causes: each cause is the issue number in its source URL.
