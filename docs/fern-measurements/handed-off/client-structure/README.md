# Client-structure handed-off documents

The documents the three fixture-only witness-search records hand off under this
area's root causes, re-compared on the finished tree. The causes and their
verdicts are [`../client-structure.tsv`](../client-structure.tsv); each cause's
measurement is the directory of its name here.

## How each document was compared

Each document was fetched at its recorded revision through the shared GitHub
response cache (the raw lane `tools/witness-search/rate_limit_guard.py`
documents; most were already cached), and its SHA-256 was checked against the
record before use. The certified pair's tree for it (Fern CLI 5.163.1,
`fernapi/fern-python-sdk` 5.41.3, `enum_type: python_enums`) was generated once
under the shared Fern lock into the shared certified-tree cache,
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/certified-trees/fern-5.163.1_python-5.41.3/<sha256>/python_enums/`,
and every generation exited 0 with a complete tree. `crozier compare`, with
every catalogued departure applied, then compared crozier's SDK (`package-name:
fern`, `project-name: default_package_name`) with that tree, using crozier built
at `fd957cb9d`.

`record` names the source record (`witness-search-fixture-only-<record>`);
`causes` gives this area's causes first and, after "also", the other causes the
record lists for the document. Every file a document still differs in is listed
with its attributed cause in
[`remaining-differences.tsv`](remaining-differences.tsv); none is attributed to
a cause of this area.

| document | sha256 | record | causes | on the finished tree |
|---|---|---|---|---|
| `tranphita/skyvern:fern/openapi/skyvern_openapi.json@efe6ae1c2088ed6aa1c09268e786fef4136070be` | `0f3a701b83bed92d75c832b566b4549e53683d1e9dafbd57fe79a68b09f18ac5` | bodies-paths | untagged-operation-grouping | byte-matches |
| `CryptoTyson/n8n-skyvern:fern/openapi/skyvern_openapi.json@6fcaa74efb6160921f1c1ef9c8f39f47e242ea07` | `117c4acb2687f08da9f15bc02367f0d8dc144bbdbec5ab3fe933b4065f8b01f5` | bodies-paths | untagged-operation-grouping | byte-matches |
| `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `7989ab3e2c034eeb9d5b29ed652d77737d3f0d79eaf4e9278c20aee612963749` | bodies-paths | untagged-operation-grouping; also readme-endpoint-choice, example-value-source | 1 files differ, each attributed to another area's cause: `R6` (1) |
| `Skyvern-AI/skyvern:fern/openapi/skyvern_openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `a61ee2be694a329a0c65609c7069eded7640fdf42a9c331c2a9eb28adb02834f` | bodies-paths | untagged-operation-grouping; also type-placement, readme-endpoint-choice | 1 files differ, each attributed to another area's cause: `R6` (1) |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e0f80e71997209aba985eff6ef34869cd7` | `dc3a906517cbde5e334ba386760ead5e1c36ec6756d5b9547b25cdcef96a2f5d` | bodies-paths | subpackage-order, environment-shape; also type-placement, inline-type-naming, union-modelling | 80 files differ, each attributed to another area's cause: `inline-type-naming` (39), `type-placement` (20), `union-modelling` (21) |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e0f80e71997209aba985eff6ef34869cd7` | `ffab94be1fc5a3db201bc8818eb57c0135620492ca5fb6ed2bff3c2c520f99a8` | bodies-paths | subpackage-order, environment-shape; also type-placement, inline-type-naming, union-modelling | 80 files differ, each attributed to another area's cause: `inline-type-naming` (39), `type-placement` (20), `union-modelling` (21) |
| `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `614a2b05e6528484e08ccc58d2f5a1df7cbdf00d6c7962a96a81a48c12bbdc59` | bodies-paths | auth-shape, init-import-order; also union-modelling, description-source, example-enum-member | 17 files differ, each attributed to another area's cause: `description-source` (2), `example-enum-member` (2), `union-modelling` (13) |
| `jentic/jentic-public-apis:apis/openapi/ironcladapp.com/ironclad/1/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a96f8580c841a37fa0196dfd24051d4375f9fe28bb413451c35d2cacca3c2caa` | bodies-paths | auth-shape, init-import-order; also union-modelling, orphan-type-emission, description-source, example-enum-member | 18 files differ, each attributed to another area's cause: `description-source` (2), `example-enum-member` (2), `orphan-type-emission` (1), `union-modelling` (13) |
| `zalando-incubator/agentic-identity-broker:api/enduser/openapi.yaml@d500f36378dd914f8a516604a08525f737e8ddff` | `c7fb9242356484e677698b557588686e1d461e2f920fbd53042cea345357ceb6` | bodies-paths | auth-shape; also example-value-source | 2 files differ, each attributed to another area's cause: `example-value-source` (2) |
| `msgbyte/tianji:website/static/openapi.json@20124bb953eae609b8b5c003cae48633af3e4207` | `1843a239e5d93eaa9c9906daffcb64748723b6bb155fa9bcb7f3bce53c5f6ce5` | bodies-paths | method-name-derivation; also union-modelling, response-type-resolution, map-value-modelling | 79 files differ, each attributed to another area's cause: `response-type-resolution` (60), `union-modelling` (19) |
| `malach-it/boruta-server:boruta-web.openapi.json@9a32a89c224367a97e8f5af69031bcd8b867ddad` | `26683af54aab78eb9c65cb3640ce65121763d73ef657a81e47b150261f0c3b3b` | bodies-paths | method-name-derivation; also example-presence | 2 files differ, each attributed to another area's cause: `example-presence` (2) |
| `aldinokemal/go-whatsapp-web-multidevice:docs/openapi.yaml@831a851e677f48e25aa671170daade586f798551` | `b52e7995b921c67666f972946b753a4dba3cd8344b4ce3873269aafea3e1d4fa` | bodies-paths | method-name-derivation; also example-value-source | 2 files differ, each attributed to another area's cause: `example-value-source` (2) |
| `radio-aktywne/jasmine:openapi/numbat.yaml@9e8b7f6b965bff0ad7765a2d6db8a623bfd6660f` | `bf07beed1848ad54419a10565cd7b1b792362db3c93e26da1ca2437641ccff19` | bodies-paths | method-name-derivation; also union-modelling, parameter-type-resolution, response-type-resolution | 13 files differ, each attributed to another area's cause: `parameter-type-resolution` (7), `union-modelling` (6) |
| `radio-aktywne/magnolia:openapi/gecko.yaml@51d280e261cee506a6290a0fc8c9f78475c18069` | `f02e99f9ace84d4e8abe420d952516223cb130b172f6aac443b8b4f23a2ef522` | bodies-paths | method-name-derivation; also union-modelling, parameter-type-resolution, response-type-resolution | 13 files differ, each attributed to another area's cause: `parameter-type-resolution` (7), `union-modelling` (6) |
| `GravitLauncher/Launcher:openapi.yaml@fef9bae63da1afc0518d32e3333db20f409ab196` | `e883f6981ac00d25446ad4742052a00849cc9d008d38f1986d0ab2442d30ac19` | bodies-paths | method-name-derivation, reserved-name-suffix | byte-matches |
| `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd41b18fbf3509e0028c1f5e15c11822f3e0` | `48c5814b117a1009a89b28fc48628cfe70706b411297b385a644f3349fd8717a` | bodies-paths | reserved-name-suffix; also example-value-source | 2 files differ, each attributed to another area's cause: `example-value-source` (2) |
| `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d32682f659b11fbb223ad189c1e77d5fafd7c` | `895f35189bd7aa82339426400a096442551c820801dd9f712854bfdae5b9b9a8` | bodies-paths | reserved-name-suffix, init-import-order; also union-modelling, response-type-resolution, request-content-type-header, example-value-source | 66 files differ, each attributed to another area's cause: `request-content-type-header` (1), `response-type-resolution` (15), `union-modelling` (50) |
| `whatwatt-ch/whatwatt-go-documentation:openapi/api-clean.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `29ffa2656e29034f5243327dc6152d997d2852348e5c3763eb26ab4f118885a2` | bodies-paths | init-import-order; also orphan-type-emission, example-presence | 8 files differ, each attributed to another area's cause: `example-presence` (2), `orphan-type-emission` (6) |
| `whatwatt-ch/whatwatt-go-documentation:openapi/api-complete-bundle.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `4cd56f724b38b1766080f870f357c01f5ec3c093dceac5abd6ec7210fa28463a` | bodies-paths | init-import-order; also orphan-type-emission, example-presence | 8 files differ, each attributed to another area's cause: `example-presence` (2), `orphan-type-emission` (6) |
| `core-ncsrd/katana:katana-swagger/swagger.json@2c55159fabe40a5b5428b213dba3b0fa791db846` | `7ddfc4202f397446b2a932fd41712c4b2bd62f7f828ef54e9a32a046a07a8d1e` | bodies-paths | init-import-order; also media-type-recognition, request-content-type-header | 7 files differ, each attributed to another area's cause: `media-type-recognition` (6), `request-content-type-header` (1) |
| `crystalshards/monorepo:apps/crystalshards/openapi.yml@f5c7a1de82d7d397a31e234189fc9f1edb844a80` | `b29a3a4e8ea20deeb6b100e53f180e431abb054443fcaeac1eeea032187eea1c` | bodies-paths | init-import-order; also union-modelling, example-value-source | 6 files differ, each attributed to another area's cause: `example-value-source` (2), `union-modelling` (4) |
| `APIs-guru/openapi-directory:APIs/osf.io/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `cdcf786527cbc25296204b370846686f3e76083f12c7a50e419b19aa53b03e5b` | bodies-paths | reference-section-title; also media-type-recognition, orphan-type-emission, snippet-rendering | 520 files differ, each attributed to another area's cause: `media-type-recognition` (493), `orphan-type-emission` (26), `snippet-rendering` (1) |
| `AMRC-FactoryPlus/documentation:static/spec/cluster-manager.yaml@cfb2f488ff2f4b29c90235b12e9f8ed497772b59` | `be5e37894ab0582a6f6498609754319fcccdbbb140e7a055902d74534616fd8f` | operations-extensions | R2 | byte-matches |
| `darwin-studios/darwin-cli:openapi.json@0ae98a805869b7acabd737365c193b0afcbd0d7e` | `ee5e2a219e2f0911107a11eab0d98405e91f2b6d8fddf0f0d5730f445421a952` | operations-extensions | R10; also R9 | 11 files differ, each attributed to another area's cause: `R9` (11) |
| `fern-api/docs:fern/apis/fai/openapi.json@e82e7289d69f082c6ee1d950bb7cb8d2c2d4b4a2` | `74ff1c45451650d7c723802727cea799f18174e9e72291777a5b81f013c678a4` | operations-extensions | R12; also R13 | 7 files differ, each attributed to another area's cause: `R13` (7) |
| `fern-api/docs:fern/apis/fai/openapi.json@6f9d392f0d7f48e9a86f3ead50ba72340567bd62` | `5aa6dbf5778778503f76e63dea7f13313434d0d883f25a93792190fba0a6f621` | operations-extensions | R12; also R13 | 7 files differ, each attributed to another area's cause: `R13` (7) |
| `nextcloud/client-sdks:go/api/openapi.yaml@02bc7281ee36fe8862a61e94e12c91381c5866bf` | `adbf311837cc8d83ef91b6c826c003e0fa25b437abebe8f902180600109443b9` | operations-extensions | R16; also R15 | 6 files differ, each attributed to another area's cause: `R15` (5), `union-modelling` (1) |
| `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `748ff9ba7fba914537047a5198e24da9d32e64608cede2a67f9561cd53cee743` | operations-extensions | R18; also R17, R19 (repaired by vtex-output-parity) | byte-matches |
| `hey-api/hey-api:specs/openapi/val-town.json@9d56b7e1aa05434a34d6e1dbb35b786d8f69dc4e` | `30fbd0e53946ee2af6180a3ef05bdda12dc2ce838c0e42eb7a2f0a624724cab8` | schemas | operation-id-tag-prefix-digit | 9 files differ, each attributed to another area's cause: `description-source` (1), `response-type-resolution` (8) |
| `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/brex/expenses/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `1115ef925b93ae8f8d0314077e3ee78bce413f55c24942f503000a9cb9357ac9` | schemas | single-operation-tag-root-method | byte-matches |

## Notes on the comparison

- **Byte-matching documents.** Six documents list only this area's causes:
  both third-party Skyvern copies, GravitLauncher, AMRC's cluster manager,
  Brex's expenses API and val-town. All but val-town (below) byte-match, the
  Skyvern copies with their root-client inline types moving to the root
  `types/` along with their method. VTEX's Marketplace Protocol, whose other two
  causes the `vtex-output-parity` node repaired, byte-matches too. Registering
  any of them is `remeasure-and-register`'s work, not this node's.
- **val-town.** The schemas record lists only `operation-id-tag-prefix-digit`
  for it, the cause of its first differing line, and that cause is repaired
  (`alias_val2` now matches). Its remaining files belong to causes the
  bodies-and-paths record names for other documents: a `const` response hoisted
  into a named type (`response-type-resolution`) and an `allOf` member's
  description (`description-source`).
- **Skyvern's two first-party documents** now match everywhere but three
  `reference.md` parameter descriptions that begin with a line break, the
  operations-and-extensions record's `R6`.
- **`init-import-order` (ruling 7).** In each of its seven documents, sorting
  both `__init__.py` type-checking blocks with ruff's isort leaves only names
  another cause adds or drops (whatwatt's `GetSdPath*` types,
  `orphan-type-emission`; Ironclad's and Nussknacker's union variants,
  `union-modelling`; katana's `Bootstrap`, `media-type-recognition`;
  crystalshards' `ValidationErrorErrorsItemItem`, `union-modelling`). The
  `init-type-checking-import-order` departure therefore still absorbs this
  cause's whole difference: those blocks clear with their other cause, as the
  record states, and where nothing else changes the block (katana's root
  `__init__.py`, this cause's measurement) the departure applies and the file
  matches.
- **FAI.** Beside `R13`, its `reference.md` shows one more line: where a path and
  a query parameter are both `domain`, the certified pair's worked call passes
  `domain=` twice, where its own signature and docstring, and crozier, say
  `query_domain`.
  No record names that difference; it is drafted as a follow-up.
- **`R10` beside `R9`.** darwin-cli's union imports now share one statement as
  the certified pair writes them; its remaining files are `R9`'s hoisted
  `ActActionResponseInteraction`.
