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

The four disjoint outcomes are **79 registered**,
**36 decided** (26 `refused-by-ruling`, 10 `byte-matches-not-admissible`),
**30 listed residuals** (30 `differs`, 0 `registration-incomplete`), and
**1 could-not-check** (lolesports' evaluated valid-OpenAPI exception: its useful
crozier SDK cannot byte-match the certified pair's empty scaffold). They sum to
146. Each comparison record names the exact command and source digest; refusals
include both crozier modes and the certified pair's diagnostic. License evidence
is retained beside the measurement, with the rule stated only in
[`docs/corpus-licensing.md`](../../corpus-licensing.md).

The missing-overlay batch's 74 normalized `literals` comparisons all match.
Of these, 72 documents now have both-mode corpus registrations. Two remain
`differs` because the stricter corpus example-inventory gate rejects their
evidence, rather than because the normalized CLI comparison finds a byte delta:
`crystalshards/monorepo` applies `schema-rejected-name-example` without a
corresponding repaired inventory value, and `gk0wk/openapi-thrift` records an
empty Fern value where `declared-example-over-placeholder` replaces a named
placeholder. Their comparison records retain the successful CLI comparisons
and the rejecting corpus diagnostics; `residuals.tsv` names every rejected file
under `remeasure` for the residual-repair pass. No missing-overlay case remains.

The Tilecast both-mode recording replay passed in approximately 23 minutes
21 seconds of wall time (1400.57 seconds from test-thread creation, polled once
per second on this shared host). Its base golden has 233 files including
provenance, totaling 2,363,405 bytes. Its matching proof remains registered;
the timing is recorded for a separate performance follow-up.

The comparison binary was copied before the behavior-preserving boolean
simplification clippy requested in `name_refusals`; the nine focused SDK
journeys passed again after that simplification. No later edit changes generator
behavior. Prior area reports describe their own repair-node measurements;
`documents.tsv` is the present status of each real document.

## Coverage measurement provenance

The missing-overlay registration batch supersedes the historical measurement
below with a fresh full golden-only run at `5d35553914adf9923d647acddf37ab3af76b8f72`:
391 tests passed, with zero carried exports. This includes the 72 new
both-mode corpus gates. Tilecast’s normal instrumented replay passed in
974.31 seconds (about 16 minutes 14 seconds, from test-process creation,
polled once per second). The census now includes 391 sources: 31 original
and 360 corpus sources. Registration identifiers use the short
`LITERALS_<owner>_<sha8>` form so rustfmt keeps the helper calls discoverable
by the existing census parser. The subsequent `151b139da` commit adds only
four lint-annotation comment lines and does not change the measured behavior.

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

- `AMRC-FactoryPlus/documentation:static/spec/cluster-manager.yaml@cfb2f488ff2f4b29c90235b12e9f8ed497772b59` | `be5e37894ab0582a6f6498609754319fcccdbbb140e7a055902d74534616fd8f` | 5500 (registered-literals-amrc-factoryplus-documentation-be5e3789)
- `APIs-guru/openapi-directory:APIs/id4i.de/1.0.2/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `2f8c36b995bb40086c763694d2ea7f1570178060dcdbe6ae582ce4a43a5d2a10` | 5501 (registered-literals-apis-guru-openapi-directory-2f8c36b9)
- `APIs-guru/openapi-directory:APIs/journy.io/1.0.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `9031af6a2a41d511b3ef2bf110a262d5c0099cb26a19fee8df49890362b11d32` | 5502 (registered-literals-apis-guru-openapi-directory-9031af6a)
- `APIs-guru/openapi-directory:APIs/keyserv.solutions/1.4.5/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `7edd79beb9c490240ae09a653602cc5260ab66a422751d889ca7d63705b1552c` | 5503 (registered-literals-apis-guru-openapi-directory-7edd79be)
- `APIs-guru/openapi-directory:APIs/nexmo.com/external-accounts/0.1.5/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `72fccf735b91ca2b89dab2f59f0cd393404ae898341ba01828d1d31cb6a8ff75` | 5504 (registered-literals-apis-guru-openapi-directory-72fccf73)
- `APIs-guru/openapi-directory:APIs/openaq.local/2.0.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `468bf5eff16a3ec71979ee470a4e80f233c8f6ce67e93e118457fbe8e8efab91` | 5505 (registered-literals-apis-guru-openapi-directory-468bf5ef)
- `APIs-guru/openapi-directory:APIs/osf.io/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `cdcf786527cbc25296204b370846686f3e76083f12c7a50e419b19aa53b03e5b` | 5506 (registered-literals-apis-guru-openapi-directory-cdcf7865)
- `APIs-guru/openapi-directory:APIs/visualstudio.com/v1/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `a0bd29a9ae19cb1b39aeef5a51b1bfc3e13362235eb5d829795ba42552a42651` | 5507 (registered-literals-apis-guru-openapi-directory-a0bd29a9)
- `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `748ff9ba7fba914537047a5198e24da9d32e64608cede2a67f9561cd53cee743` | 3479 (vtex-marketplace-protocol)
- `CryptoTyson/n8n-skyvern:fern/openapi/skyvern_openapi.json@6fcaa74efb6160921f1c1ef9c8f39f47e242ea07` | `117c4acb2687f08da9f15bc02367f0d8dc144bbdbec5ab3fe933b4065f8b01f5` | 5508 (registered-literals-cryptotyson-n8n-skyvern-117c4acb)
- `Grafikart/filemanager-element:openapi.yml@af6fc5f6be961b14b2b2a218ddadac1fe6bbeb46` | `e36a74ce6e86cf994ab1dbc54e4103b8d500590c160a54f61b749345462f2d28` | 5050 (remeasured-grafikart-filemanager-element-e36a74ce)
- `GravitLauncher/Launcher:openapi.yaml@fef9bae63da1afc0518d32e3333db20f409ab196` | `e883f6981ac00d25446ad4742052a00849cc9d008d38f1986d0ab2442d30ac19` | 5510 (registered-literals-gravitlauncher-launcher-e883f698)
- `Hardonian/Reach:openapi/reach.openapi.yaml@beb7f7f9d28d4b123af2b2d52790225e796f0879` | `f36ad5db387d59597977a7bfd6c72d24470580cc5a61323b7b605cf53af589b2` | 5511 (registered-literals-hardonian-reach-f36ad5db)
- `JHUAPL-DTNMA/dtnma-tools:src/refdm/openapi.json@598da6c6793998ea1d845ec32f1e4107c0c4930a` | `de4dc81fea0801628868bb1cb1576f546e8498404f8ad4b94fd65b2bd0d3bef3` | 5512 (registered-literals-jhuapl-dtnma-dtnma-tools-de4dc81f)
- `Observation-Management-Service/ewms-workflow-management-service:wms/schema/openapi.json@079f9e1f9cf203c439b5ed206ef26d381cf0ba5a` | `2b4dea8588f4e01dad30b53c207b1ded59ff69b3a5743d055724601d52fa3e37` | 5513 (registered-literals-observation-management-service-ewms-workflow-management-service-2b4dea85)
- `OpenAPITools/openapi-generator:modules/openapi-generator/src/test/resources/3_1/cpp-boost-beast-client/oas31-runtime-regression.yaml@10e6c21c97abb098cc67f14dfdd02171ce56b115` | `3d0397413feb522ea9b985a1ea9910b03604cb6ea37a8782dc1228b2b6cf4210` | 5514 (registered-literals-openapitools-openapi-generator-3d039741)
- `OpenAPITools/openapi-generator:modules/openapi-generator/src/test/resources/3_1/polymorphism.yaml@10e6c21c97abb098cc67f14dfdd02171ce56b115` | `98d94419f4faed7ed6e519115f55f38d36b30fd8fe846b3f56e563cf7af174dc` | 5515 (registered-literals-openapitools-openapi-generator-98d94419)
- `OpenAPITools/openapi-generator:samples/client/petstore/csharp/generichost/latest/NullTypes/api/openapi.yaml@10e6c21c97abb098cc67f14dfdd02171ce56b115` | `83482829ad7460149b3ca06ea3b0819d92c0615dacccb05574a23bf093542b12` | 5516 (registered-literals-openapitools-openapi-generator-83482829)
- `OpenBanking-Brasil/areadesenvolvedor:documentation/source/swagger/swagger_pension_apis.yaml@d6770dfcb778e2e938c43455740b3f806a1efea8` | `7fb4ca577cc6dbc1cf49cf89573f786667430e34154cf034e5e05e07e5d64d00` | 5517 (registered-literals-openbanking-brasil-areadesenvolvedor-7fb4ca57)
- `SeekStorm/SeekStorm:seekstorm_server/openapi/openapi.yml@50cb0ddffe1e45eb574f927079d1bcffecf8980b` | `b73096c45484d5d8076a8e6ed80fd25cf2467acf9a8b717925937c5d9eaa0646` | 5518 (registered-literals-seekstorm-seekstorm-b73096c4)
- `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `7989ab3e2c034eeb9d5b29ed652d77737d3f0d79eaf4e9278c20aee612963749` | 5519 (registered-literals-skyvern-ai-skyvern-7989ab3e)
- `Skyvern-AI/skyvern:fern/openapi/skyvern_openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `a61ee2be694a329a0c65609c7069eded7640fdf42a9c331c2a9eb28adb02834f` | 5520 (registered-literals-skyvern-ai-skyvern-a61ee2be)
- `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d32682f659b11fbb223ad189c1e77d5fafd7c` | `895f35189bd7aa82339426400a096442551c820801dd9f712854bfdae5b9b9a8` | 5521 (registered-literals-touk-nussknacker-895f3518)
- `TrueBlocks/trueblocks-core:docs/content/api/openapi.yaml@6892811b0fb1e4e52aa2e82226d109c3335212a2` | `2a176f1485a9160b5ada1140c9276088076afd56ae05b865b87904347409bbec` | 5522 (registered-literals-trueblocks-trueblocks-core-2a176f14)
- `arawa/workspace:openapi.json@926f6093e68261c94f4dcd536b0c4451f2013ee8` | `0c8259f6f991dbd2985005b14731e7df52d59496a17249394fefcbaa2ef52689` | 5051 (remeasured-arawa-workspace-0c8259f6)
- `ballerina-platform/openapi-connectors:openapi/azure.openai.finetunes/openapi.yaml@7c3840c93e80c711a8b317f94339b3cb08c1521c` | `97a587f5a81f68ea2ef3bdf6f12599102c2a254348a6ee8cbf07fde9529943e7` | 5523 (registered-literals-ballerina-platform-openapi-connectors-97a587f5)
- `bytedance/SandboxFusion:docs/src/openapi.json@469de0845cb7d665bc68044d541aa3aa28c5b30a` | `0b64b21d18f81307dd5b23b95fb07a35ff28e8af14f8149844229d91458252e2` | 5524 (registered-literals-bytedance-sandboxfusion-0b64b21d)
- `clencyc/MozillaFestivalBackend:openapi.yaml@e70f0150f414d216743311be79d005d900ab81f1` | `b2264b38f17b99bd722b94f94029916705be39cd6359b1b341bc8696f29e6092` | 5052 (remeasured-clencyc-mozillafestivalbackend-b2264b38)
- `codosseum-org/backend:openapi.yaml@a92699b50e5b57aefb8922525a27ed8bb8d7885f` | `9fa232be1ff3b0c9d753f4b6a91a55ce5bc2cdcb5a026ecf0bdf0254775257b1` | 5525 (registered-literals-codosseum-org-backend-9fa232be)
- `confluentinc/schema-registry-sdk-go:api/openapi.yaml@77f22d67c4d6bfe86842da77f76a3f1d5b69da5b` | `aa65c204008962962222defeea2e801476d3aa6a932ef981b4728b95690b39b7` | 5526 (registered-literals-confluentinc-schema-registry-sdk-go-aa65c204)
- `core-ncsrd/katana:katana-swagger/swagger.json@2c55159fabe40a5b5428b213dba3b0fa791db846` | `7ddfc4202f397446b2a932fd41712c4b2bd62f7f828ef54e9a32a046a07a8d1e` | 5527 (registered-literals-core-ncsrd-katana-7ddfc420)
- `craftgodotdev/craftgo:example/ecommerce/docs/openapi.yaml@0986f22a522528dba13ab2bd1cb3735ebf43dcc3` | `d6e4a55acf6d7008a3b6278bc290cff144922bd60eba5d595e6da09c0002c837` | 5528 (registered-literals-craftgodotdev-craftgo-d6e4a55a)
- `darwin-studios/darwin-cli:openapi.json@0ae98a805869b7acabd737365c193b0afcbd0d7e` | `ee5e2a219e2f0911107a11eab0d98405e91f2b6d8fddf0f0d5730f445421a952` | 5530 (registered-literals-darwin-studios-darwin-cli-ee5e2a21)
- `debezium/debezium-platform:openapi/openapi.yaml@20fd16bf12ac02e750bb770fc4b986afdf824507` | `043f3a5f2fe283197741850d02964865211d10e2af271aa9b344ee7a84507de6` | 5531 (registered-literals-debezium-debezium-platform-043f3a5f)
- `fern-api/docs:fern/apis/fai/openapi.json@6f9d392f0d7f48e9a86f3ead50ba72340567bd62` | `5aa6dbf5778778503f76e63dea7f13313434d0d883f25a93792190fba0a6f621` | 5532 (registered-literals-fern-api-docs-5aa6dbf5)
- `fern-api/docs:fern/apis/fai/openapi.json@e82e7289d69f082c6ee1d950bb7cb8d2c2d4b4a2` | `74ff1c45451650d7c723802727cea799f18174e9e72291777a5b81f013c678a4` | 5533 (registered-literals-fern-api-docs-74ff1c45)
- `gbyo/tilecast:docs/openapi.yaml@9b731f41de1c1387ebd7a7f74c3c783510aa67a0` | `832b9080645151da0612125abdb82afeb90c6dd0b33da87dcdcd5edc1d3178ce` | 5534 (registered-literals-gbyo-tilecast-832b9080)
- `geoserver/geoserver:src/extension/ogcapi/ogcapi-features/src/main/resources/org/geoserver/ogcapi/v1/features/openapi.yaml@e5096dda80eea70d21167f01b08e543019852a7e` | `b34cf5872fab13f73c2d67ff639e8cecaf9260e545e2fb2061bc12d07dcce430` | 5535 (registered-literals-geoserver-geoserver-b34cf587)
- `gleez/nats-http-gateway:openapi.json@cfc5b22883fe4deb88933f9e39d04128a53b6156` | `e8767ae79ab54774728dc226ffc0db0014c32c99b341e019cbbcf3d700def8a0` | 5536 (registered-literals-gleez-nats-http-gateway-e8767ae7)
- `halo-dev/halo:api-docs/openapi/v3_0/apis_console.api_v1alpha1.json@ead7adfb0ca1da810a6a080cf8aeed476668db64` | `7e48a5530dfce8d110f78a1fabd4cb186e93d3008ef4ae95ca0d15dc2325b173` | 5537 (registered-literals-halo-dev-halo-7e48a553)
- `halo-dev/halo:api-docs/openapi/v3_0/apis_uc.api_v1alpha1.json@ead7adfb0ca1da810a6a080cf8aeed476668db64` | `6e341cacc7734304136d06c6289318ae4505b142aac6eb56ba5f863739c5c568` | 5538 (registered-literals-halo-dev-halo-6e341cac)
- `hashicorp/terraform-plugin-codegen-openapi:internal/cmd/testdata/edgecase/openapi_spec.yml@55b2a49774f094d0d8aff834bce5eabe9e8a7345` | `1f6aea4c5e340b482e6441711f83780f2a6026a4755452530094d160747d2427` | 5053 (remeasured-hashicorp-terraform-plugin-codegen-openapi-1f6aea4c)
- `hey-api/hey-api:specs/openapi/val-town.json@9d56b7e1aa05434a34d6e1dbb35b786d8f69dc4e` | `30fbd0e53946ee2af6180a3ef05bdda12dc2ce838c0e42eb7a2f0a624724cab8` | 5539 (registered-literals-hey-api-hey-api-30fbd0e5)
- `i-am-bee/agentstack:docs/development/api-reference/openapi.json@79c786049d39684841d77fef9abfd8457a58b0bf` | `7d68b3f8bf7f0b7d0c0b27a59d5aa5e8a783c6ebd3158abaaee3983504f69068` | 5540 (registered-literals-i-am-bee-agentstack-7d68b3f8)
- `ihulsbus/cookbook:docs/k8s/files/openapi.yaml@9be5a607c9d09820928575972b1ab83aa90e14af` | `0ac7df49edfe6ef2faeed98cf12fd827871539cd70bddd85967acbef8ca85123` | 5541 (registered-literals-ihulsbus-cookbook-0ac7df49)
- `jentic/jentic-public-apis:apis/openapi/ironcladapp.com/ironclad/1/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a96f8580c841a37fa0196dfd24051d4375f9fe28bb413451c35d2cacca3c2caa` | 5542 (registered-literals-jentic-jentic-public-apis-a96f8580)
- `koala73/worldmonitor:docs/api/ScorecardService.openapi.yaml@90dc23a3fd7c9497f85449a7ff7f6fb81d51d137` | `35041bfc80c105422091c39f4ec0e802fe9577fa1b6d442e55fcc536910e0698` | 5543 (registered-literals-koala73-worldmonitor-35041bfc)
- `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/brex/expenses/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `1115ef925b93ae8f8d0314077e3ee78bce413f55c24942f503000a9cb9357ac9` | 5544 (registered-literals-konfig-dev-konfig-1115ef92)
- `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `614a2b05e6528484e08ccc58d2f5a1df7cbdf00d6c7962a96a81a48c12bbdc59` | 5545 (registered-literals-konfig-dev-konfig-614a2b05)
- `konfig-sdks/openapi-examples:circleci/openapi.yaml@161ab49c45e45825ca3832945c59a3ba904321ba` | `63042193a4670a76bdb988512f38658aad1c4a56f3b312c3b57e5fc19f5d9af6` | 5546 (registered-literals-konfig-sdks-openapi-examples-63042193)
- `landing-ai/ade-cli:openapi.json@d1995ffef4e63a2a1c2774d9add93368889353c5` | `d11fa644f12445e8707b6eb8600cb2214fb30a5cfdf8346e1d43aab1f3b20164` | 5547 (registered-literals-landing-ai-ade-cli-d11fa644)
- `malach-it/boruta-server:boruta-web.openapi.json@9a32a89c224367a97e8f5af69031bcd8b867ddad` | `26683af54aab78eb9c65cb3640ce65121763d73ef657a81e47b150261f0c3b3b` | 5548 (registered-literals-malach-it-boruta-server-26683af5)
- `marcelo-earth/generative-manim:api/public/openapi.yaml@f681cc78a6b1cad8443b6af4b3a1adbfed9d3e0e` | `8e1e6b290365eee6b020b146c329b1bd2c1cb4fd3dd6e52be2fee2e72e5a6a30` | 5549 (registered-literals-marcelo-earth-generative-manim-8e1e6b29)
- `medizininformatik-initiative/dataportal-backend:docs/public/openapi.yaml@cafb8aa33d47717c311c1ff438df73a2acf17e94` | `4d419c8a1d83b54d8d71ea0640f9e07012b0e1572da98f7191b261bf8479692f` | 5550 (registered-literals-medizininformatik-initiative-dataportal-backend-4d419c8a)
- `membrane/api-gateway:core/src/test/resources/openapi/specs/oas31/boolean-schemas.yaml@c24a0204aaa9d07ee5237c44e43e8e9ef4129f2c` | `8340f5da585023194c7154cb6e72a111e5643bb9cd3364cb75e0eacb0b1fcb89` | 5054 (remeasured-membrane-api-gateway-8340f5da)
- `msgbyte/tianji:website/static/openapi.json@20124bb953eae609b8b5c003cae48633af3e4207` | `1843a239e5d93eaa9c9906daffcb64748723b6bb155fa9bcb7f3bce53c5f6ce5` | 5551 (registered-literals-msgbyte-tianji-1843a239)
- `neilthomas89440-crypto/inferna-next:docs/openapi.yaml@3c1bc6fde017130ac9335b2d4192d0400f956689` | `244423758c587aff156c4763e1491ab3ac6be494a9e3f447c8f244775b586ee1` | 5552 (registered-literals-neilthomas89440-crypto-inferna-next-24442375)
- `neo773/macgamingdb:openapi.json@71201d5ed52ab0991854f0eac0d153c076ed2907` | `2af442cee107b3b4ed4b22df18abb18280ef43dd3e1bff5a69743ef680666a81` | 5553 (registered-literals-neo773-macgamingdb-2af442ce)
- `nextcloud/client-sdks:go/api/openapi.yaml@02bc7281ee36fe8862a61e94e12c91381c5866bf` | `adbf311837cc8d83ef91b6c826c003e0fa25b437abebe8f902180600109443b9` | 5554 (registered-literals-nextcloud-client-sdks-adbf3118)
- `opengeospatial/T17-API-D166:features/api/openapi.yaml@b4328b9cb3775eb01f3a46b33b73597f33cff8af` | `ffbd86a7c53ee795a01158b18b6fd78e8c59a83bc966b7e442ed39451839cd92` | 5555 (registered-literals-opengeospatial-t17-api-d166-ffbd86a7)
- `openresponses/openresponses:public/openapi/2026-01-15/openapi.json@92c12d96d7b61d6d15e2214daa5e9c6000ab6e1c` | `ee8c96e11e193f052ae2b6aa159ff115123c44a63d9d2f99f50ff261b7b98d0f` | 5556 (registered-literals-openresponses-openresponses-ee8c96e1)
- `openresponses/openresponses:public/openapi/2026-04-24/openapi.json@92c12d96d7b61d6d15e2214daa5e9c6000ab6e1c` | `d598753c3a86fd8a2434828fe39dcc8786a7a694bbe46080a0d24c9fa40e72df` | 5557 (registered-literals-openresponses-openresponses-d598753c)
- `ourofoundation/wrappers:nixtla/timegpt/timegpt-openapi.json@79688dd65e7fb2fb670ad30b01b5db5208c1d928` | `9165e7b94aa026f4924cc6bd8bc627719680fc028af864e0c2649168ded7705b` | 4301 (nixtla-timegpt)
- `radio-aktywne/jasmine:openapi/numbat.yaml@9e8b7f6b965bff0ad7765a2d6db8a623bfd6660f` | `bf07beed1848ad54419a10565cd7b1b792362db3c93e26da1ca2437641ccff19` | 5558 (registered-literals-radio-aktywne-jasmine-bf07beed)
- `radio-aktywne/magnolia:openapi/gecko.yaml@51d280e261cee506a6290a0fc8c9f78475c18069` | `f02e99f9ace84d4e8abe420d952516223cb130b172f6aac443b8b4f23a2ef522` | 5559 (registered-literals-radio-aktywne-magnolia-f02e99f9)
- `rd-alliance/metadata-catalog-v2:openapi.yaml@833c55f1ad8b6a19b77e8fc4f1d16133b8e5d624` | `c5da87bb95be6352daf5b5bda7b163916541e29123b94feb32e778f6367ad80a` | 5560 (registered-literals-rd-alliance-metadata-catalog-v2-c5da87bb)
- `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd41b18fbf3509e0028c1f5e15c11822f3e0` | `48c5814b117a1009a89b28fc48628cfe70706b411297b385a644f3349fd8717a` | 5561 (registered-literals-resemble-ai-resemble-mcp-48c5814b)
- `stripe/sync-engine:apps/engine/src/__generated__/openapi.json@0cb8ca453d7ad266de714f83838f4e38565e8a57` | `7f4c6ed528750623be6a0effa08d57e5c7abd99806ba0ec109fdeedc437ffe78` | 5562 (registered-literals-stripe-sync-engine-7f4c6ed5)
- `stripe/sync-engine:apps/service/src/__generated__/openapi.json@0cb8ca453d7ad266de714f83838f4e38565e8a57` | `0fb02347c6ccf0283f7c324b51b4f8501deea074efa437aca2b8bb6b5add56f5` | 5563 (registered-literals-stripe-sync-engine-0fb02347)
- `sumup/sumup-openapi:openapi.yaml@c359e2f1291fa81bb533298c5958ab95f0ba11c4` | `b1d4ab063c88dcadac6c303e5c7c6bf4fa90b823ba6b408c6437a712cc97c58f` | 5564 (registered-literals-sumup-sumup-openapi-b1d4ab06)
- `teunmooij/payload-tools:packages/openapi/test/integration/basic.expected.json@7a7a33b28f99cda2862a6bd1e7dc61fd5ffacb59` | `ecbf9ccc303cd96d6bcc27d39447f15ac0c880fcd2d7641cdc645a5801c51ddf` | 5565 (registered-literals-teunmooij-payload-tools-ecbf9ccc)
- `teunmooij/payload-tools:packages/openapi/test/integration/named-interfaces.expected.json@7a7a33b28f99cda2862a6bd1e7dc61fd5ffacb59` | `7296685ea113efefbb1c0f26c3b41f6932ba217cd6191044ca7aef3f82f6e0c8` | 5566 (registered-literals-teunmooij-payload-tools-7296685e)
- `tranphita/skyvern:fern/openapi/skyvern_openapi.json@efe6ae1c2088ed6aa1c09268e786fef4136070be` | `0f3a701b83bed92d75c832b566b4549e53683d1e9dafbd57fe79a68b09f18ac5` | 5567 (registered-literals-tranphita-skyvern-0f3a701b)
- `truefoundry/trueforge:docs/openapi.json@47fd7e81f39e66289d9c62ba80c4e7f7b0370d64` | `09fcb1c253845987c65878aa01f03c3cc10eee0d438e1ab22907d453f00c3744` | 5568 (registered-literals-truefoundry-trueforge-09fcb1c2)
- `truefoundry/trueforge:docs/openapi.json@a718e719347c44798ef3d3021a17678b6220640b` | `e259dee6c57f311f2a39344f5714d57d03218229dad1c291d5c5aebeace58f32` | 5569 (registered-literals-truefoundry-trueforge-e259dee6)
- `webr0m/teldrive-nodejs:openapi/teldrive.openapi.yaml@22d9b87d2955d3c9c2ce712b5a9d2aad1f94dd14` | `bb74a9e2c993403d2cdbfe25184ce341f23daf27c04a7f96904533a740c6c4f2` | 5570 (registered-literals-webr0m-teldrive-nodejs-bb74a9e2)
- `whatwatt-ch/whatwatt-go-documentation:openapi/api-clean.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `29ffa2656e29034f5243327dc6152d997d2852348e5c3763eb26ab4f118885a2` | 5571 (registered-literals-whatwatt-ch-whatwatt-go-documentation-29ffa265)
- `whatwatt-ch/whatwatt-go-documentation:openapi/api-complete-bundle.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `4cd56f724b38b1766080f870f357c01f5ec3c093dceac5abd6ec7210fa28463a` | 5572 (registered-literals-whatwatt-ch-whatwatt-go-documentation-4cd56f72)
- `zalando-incubator/agentic-identity-broker:api/enduser/openapi.yaml@d500f36378dd914f8a516604a08525f737e8ddff` | `c7fb9242356484e677698b557588686e1d461e2f920fbd53042cea345357ceb6` | 5573 (registered-literals-zalando-incubator-agentic-identity-broker-c7fb9242)

The [follow-up ticket area](follow-up-tickets/README.md) reconciles its ticket-URL
rows as its own causes: each cause is the issue number in its source URL.
