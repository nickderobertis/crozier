# Remeasurement area

The [triage](../remeasure.tsv) contains the additional measured causes and the
non-table causes the planner moved here from the repair areas. The independent
measurement documents are under each cause directory; the enum-mode trees are
fresh output of the certified pair. Existing named causes also have additional
regression measurements here: nullable response unions and titled request
headers, parent map examples, and the split-media orphan-model control.

The table below is this node’s final measurement snapshot, derived from
[`documents.tsv`](../documents.tsv) and [`residuals.tsv`](../residuals.tsv).
Those files are the authority for later status changes. `byte-matches` means
comparison with every catalogued departure applied; missing literals evidence
is registration work, listed separately from byte differences. The planner’s
land-now ruling leaves the named remaining differences for follow-on repairs.

| document (recorded revision) | SHA-256 | cause / regression | final comparison |
|---|---|---|---|
| `APIs-guru/openapi-directory:APIs/digitalocean.com/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63.txt)) |
| `OLeier/IBLeier.VictronEnergy:Monitor/OpenAPIs/VrmApi/VrmApi_BundledReferences.yaml@774baffe059489634f310640d004a42a5e28f8fe` | `21f398c40ee6b173dd661fe1435fc565f1f2af277d2098fad3ece22cf2bce77c` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/21f398c40ee6b173dd661fe1435fc565f1f2af277d2098fad3ece22cf2bce77c.txt)) |
| `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d32682f659b11fbb223ad189c1e77d5fafd7c` | `895f35189bd7aa82339426400a096442551c820801dd9f712854bfdae5b9b9a8` | `x-fern-type-extension` | byte-matches; registration-incomplete ([record](../comparisons/895f35189bd7aa82339426400a096442551c820801dd9f712854bfdae5b9b9a8.txt)) |
| `api-platform/schema-generator:tests/e2e/openapi.yml@22635fbacac8011c73cdbbb5c20507c77c02d89d` | `978fbacd3483f78d34c90ff71bdc8429223ef8409e531b4960cb0c78dec31206` | `never-compared-request-property-camelcase-collision` | refused-by-ruling ([record](../comparisons/978fbacd3483f78d34c90ff71bdc8429223ef8409e531b4960cb0c78dec31206.txt)) |
| `atacan/AssemblyAI:openapi.yaml@ed31d2fbb08b69633e7d1bcc31bc4cf8eacc8718` | `b306bf4455446eb3bc38f0e687888206b017b5e89c6047a5592e2fbdd88160b7` | `enum-member-digit-separator`; `group-placed-nested-type-placement`; `typed-single-ref-allof-alias` | differs ([record](../comparisons/b306bf4455446eb3bc38f0e687888206b017b5e89c6047a5592e2fbdd88160b7.txt)) |
| `atacan/AssemblyAI:original_openapi.yaml@ed31d2fbb08b69633e7d1bcc31bc4cf8eacc8718` | `10ca68affcc55d46649da53ca342ee804c56af96b0a963d584562c8b21e20824` | `enum-member-digit-separator`; `group-placed-nested-type-placement`; `typed-single-ref-allof-alias` | differs ([record](../comparisons/10ca68affcc55d46649da53ca342ee804c56af96b0a963d584562c8b21e20824.txt)) |
| `beeequeue/arm-server:docs/openapi.yaml@86c9359fc9df49b9d42cf21dc67bdc99b1658fbf` | `79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c.txt)) |
| `confluentinc/schema-registry-sdk-go:api/openapi.yaml@77f22d67c4d6bfe86842da77f76a3f1d5b69da5b` | `aa65c204008962962222defeea2e801476d3aa6a932ef981b4728b95690b39b7` | `example-value-source residual (parent-example-map-values)` | byte-matches; registration-incomplete ([record](../comparisons/aa65c204008962962222defeea2e801476d3aa6a932ef981b4728b95690b39b7.txt)) |
| `dltkddnr04/propresenter-remote:openapi/propresenter.openapi.json@b273aeec98db96f4766d0b4e0d2a8305627396a4` | `44695afa34c9d6e1fce938a62844cf07b30ed296a5e3d2be1779827947394219` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/44695afa34c9d6e1fce938a62844cf07b30ed296a5e3d2be1779827947394219.txt)) |
| `fossology/FOSSology.REST.dotnet:openapi/FOSSology REST API 1.6.2.yaml@b362ec94ddf8ab6da0f8606183dfc2bc79b157b9` | `7da1db69e60df38ffa4ae477eee68eab2e29932dad65de682d4d22bac71b9872` | `never-compared-request-property-name-collision` | differs ([record](../comparisons/7da1db69e60df38ffa4ae477eee68eab2e29932dad65de682d4d22bac71b9872.txt)) |
| `hashgraph/guardian:docs/.gitbook/assets/swagger (2) (1) (1).yaml@e585ead1c74b04dfb70e714363dc6a78f2d077ed` | `63ba2735ef533eef9a5bcb1fffc770f9e88a57f8ee058e9c5c4e2521bcf3abf4` | `json-ref-body-kept-whole` | differs ([record](../comparisons/63ba2735ef533eef9a5bcb1fffc770f9e88a57f8ee058e9c5c4e2521bcf3abf4.txt)) |
| `jeffmikels/ProPresenter-API:pro7.9.openapi-spec.json@6e7490671c94a7c9e588274bdf5df6ece1934248` | `694f7ec93b5aafa776ab61f7e049432f2ac01f8db5ffce4aedbde9f1a38616cc` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/694f7ec93b5aafa776ab61f7e049432f2ac01f8db5ffce4aedbde9f1a38616cc.txt)) |
| `jentic/jentic-public-apis:apis/openapi/assemblyai.com/main/1.3.4/meta/import/input-bundle.json@c72e13e0f80e71997209aba985eff6ef34869cd7` | `2011299d2095426af64fdf2209daa58c58152a09d34980717a048cf406b67a87` | `enum-member-digit-separator`; `group-placed-nested-type-placement`; `typed-single-ref-allof-alias`; `unresolved-reference` | differs ([record](../comparisons/2011299d2095426af64fdf2209daa58c58152a09d34980717a048cf406b67a87.txt)) |
| `jentic/jentic-public-apis:apis/openapi/codat.io/sync-for-expenses/prealpha/openapi.json@1700c576aa658b5dc3bd06cb376cc959d84e12f8` | `827e170f0c2a997418cfe3682b68f42cd81481396d663c0013d5ddae00128679` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/827e170f0c2a997418cfe3682b68f42cd81481396d663c0013d5ddae00128679.txt)) |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e0f80e71997209aba985eff6ef34869cd7` | `ffab94be1fc5a3db201bc8818eb57c0135620492ca5fb6ed2bff3c2c520f99a8` | `orphan-type-emission control (split-media-body-orphan-model)` | byte-matches; byte-matches-not-admissible ([record](../comparisons/ffab94be1fc5a3db201bc8818eb57c0135620492ca5fb6ed2bff3c2c520f99a8.txt)) |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e0f80e71997209aba985eff6ef34869cd7` | `dc3a906517cbde5e334ba386760ead5e1c36ec6756d5b9547b25cdcef96a2f5d` | `orphan-type-emission control (split-media-body-orphan-model)` | byte-matches; byte-matches-not-admissible ([record](../comparisons/dc3a906517cbde5e334ba386760ead5e1c36ec6756d5b9547b25cdcef96a2f5d.txt)) |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0.txt)) |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936.txt)) |
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `be0196359ca1794934d5c9622d42d608da3426b1f993db7c91e995b7a54815f7` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/be0196359ca1794934d5c9622d42d608da3426b1f993db7c91e995b7a54815f7.txt)) |
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414.txt)) |
| `konfig-sdks/openapi-examples:peach-payments/openapi.yaml@161ab49c45e45825ca3832945c59a3ba904321ba` | `d7497fa8a725dfea1f77f5c50653f3ee1d9d866e27b1592b6f6c7911ea77f972` | `never-compared-type-name-collision` | differs ([record](../comparisons/d7497fa8a725dfea1f77f5c50653f3ee1d9d866e27b1592b6f6c7911ea77f972.txt)) |
| `msgbyte/tianji:website/static/openapi.json@20124bb953eae609b8b5c003cae48633af3e4207` | `1843a239e5d93eaa9c9906daffcb64748723b6bb155fa9bcb7f3bce53c5f6ce5` | `union-modelling residual (nullable-union-and-unknown-body)` | byte-matches; registration-incomplete ([record](../comparisons/1843a239e5d93eaa9c9906daffcb64748723b6bb155fa9bcb7f3bce53c5f6ce5.txt)) |
| `neilthomas89440-crypto/inferna-next:docs/openapi.yaml@3c1bc6fde017130ac9335b2d4192d0400f956689` | `244423758c587aff156c4763e1491ab3ac6be494a9e3f447c8f244775b586ee1` | `ignored-multipart-query-collision` | byte-matches; registration-incomplete ([record](../comparisons/244423758c587aff156c4763e1491ab3ac6be494a9e3f447c8f244775b586ee1.txt)) |
| `ogcincubator/developer-website-v3:api/dggs/openapi.yaml@d123c2c2df80940a8af30f9dd2a45c382a7ecff7` | `9ccb483ad815ad25c876c7317b7edfb167452a6325164887cc888b67aa49a382` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/9ccb483ad815ad25c876c7317b7edfb167452a6325164887cc888b67aa49a382.txt)) |
| `outstack/enveloper:docs/api/openapi.yaml@cd8150d6d78c64ff48acdfb886c833a4600515df` | `95595ff60c5a51617e5bd497fb94eeba13e6b3566c271b5bf59403a5789145bf` | `missing-relative-file` | byte-matches; byte-matches-not-admissible ([record](../comparisons/95595ff60c5a51617e5bd497fb94eeba13e6b3566c271b5bf59403a5789145bf.txt)) |
| `speakeasy-sdks/bolt-embedded-go:openapi.yaml@61fde63b20a4638aed45d9cef13bb702c8d48dd0` | `ddae331c90d254f9fca6e516417ace183f9ee131bf88869098451ea02182d861` | `unresolved-reference` | refused-by-ruling ([record](../comparisons/ddae331c90d254f9fca6e516417ace183f9ee131bf88869098451ea02182d861.txt)) |
| `stripe/openapi:stripe--openapi/latest/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a` | `extension-reference-cycle` | refused-by-ruling ([record](../comparisons/92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a.txt)) |
| `stripe/openapi:stripe--openapi/preview/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4` | `extension-reference-cycle` | refused-by-ruling ([record](../comparisons/60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4.txt)) |
| `tryAGI/AssemblyAI:src/libs/AssemblyAI/openapi.yaml@1028f8b61cda3f1dc8777d732093fd3e4558d9c9` | `215ec23ddd849ffd78349383788255dfeb417532c81f6dc5c2cdd6b5c577ab02` | `enum-member-digit-separator`; `group-placed-nested-type-placement`; `typed-single-ref-allof-alias` | differs ([record](../comparisons/215ec23ddd849ffd78349383788255dfeb417532c81f6dc5c2cdd6b5c577ab02.txt)) |

## Remaining files: b306bf4455446eb3bc38f0e687888206b017b5e89c6047a5592e2fbdd88160b7

- `README.md` — `example-optional-members` (example-values).
- `reference.md` — `example-optional-members` (example-values).
- `src/fern/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/transcripts/client.py` — `remaining-b306bf44-src-fern-transcripts-client-py` (remeasure).
- `src/fern/transcripts/raw_client.py` — `remaining-b306bf44-src-fern-transcripts-raw-client-py` (remeasure).
- `src/fern/transcripts/types/transcript_list_item.py` — `x-fern-type-extension` (remeasure).
- `src/fern/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).

## Remaining files: 10ca68affcc55d46649da53ca342ee804c56af96b0a963d584562c8b21e20824

- `src/fern/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/transcripts/raw_client.py` — `remaining-10ca68af-src-fern-transcripts-raw-client-py` (remeasure).
- `src/fern/transcripts/types/transcript_list_item.py` — `x-fern-type-extension` (remeasure).
- `src/fern/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).

## Remaining files: 7da1db69e60df38ffa4ae477eee68eab2e29932dad65de682d4d22bac71b9872

- `README.md` — `remaining-7da1db69-readme-md` (remeasure).
- `reference.md` — `example-presence` (snippet-rendering).
- `src/fern/auth/client.py` — `remaining-7da1db69-src-fern-auth-client-py` (remeasure).
- `src/fern/auth/raw_client.py` — `remaining-7da1db69-src-fern-auth-raw-client-py` (remeasure).
- `src/fern/license/client.py` — `remaining-7da1db69-src-fern-license-client-py` (remeasure).
- `src/fern/license/raw_client.py` — `remaining-7da1db69-src-fern-license-raw-client-py` (remeasure).
- `src/fern/report/client.py` — `remaining-7da1db69-src-fern-report-client-py` (remeasure).
- `src/fern/report/raw_client.py` — `remaining-7da1db69-src-fern-report-raw-client-py` (remeasure).
- `src/fern/user/client.py` — `remaining-7da1db69-src-fern-user-client-py` (remeasure).
- `src/fern/user/raw_client.py` — `remaining-7da1db69-src-fern-user-raw-client-py` (remeasure).

## Remaining files: 63ba2735ef533eef9a5bcb1fffc770f9e88a57f8ee058e9c5c4e2521bcf3abf4

- `reference.md` — `remaining-63ba2735-reference-md` (remeasure).

## Remaining files: 2011299d2095426af64fdf2209daa58c58152a09d34980717a048cf406b67a87

- `src/fern/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/lemur/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/transcripts/raw_client.py` — `remaining-2011299d-src-fern-transcripts-raw-client-py` (remeasure).
- `src/fern/transcripts/types/transcript_list_item.py` — `x-fern-type-extension` (remeasure).
- `src/fern/types/__init__.py` — `group-placed-nested-type-placement` (remeasure).
- `src/fern/types/lemur_task_params.py` — `group-placed-nested-type-placement` (remeasure).

## Remaining files: d7497fa8a725dfea1f77f5c50653f3ee1d9d866e27b1592b6f6c7911ea77f972

- `reference.md` — `remaining-d7497fa8-reference-md` (remeasure).
- `src/fern/__init__.py` — `remaining-d7497fa8-src-fern-init-py` (remeasure).
- `src/fern/checkout_generation/client.py` — `remaining-d7497fa8-src-fern-checkout-generation-client-py` (remeasure).
- `src/fern/types/__init__.py` — `remaining-d7497fa8-src-fern-types-init-py` (remeasure).
- `src/fern/types/checkout_pending_webhook_currency.py` — `remaining-d7497fa8-src-fern-types-checkout-pending-webhook-currency-py` (remeasure).
- `src/fern/types/checkout_pending_webhook_payment_type.py` — `remaining-d7497fa8-src-fern-types-checkout-pending-webhook-payment-type-py` (remeasure).
- `src/fern/types/checkout_successful_webhook.py` — `remaining-d7497fa8-src-fern-types-checkout-successful-webhook-py` (remeasure).
- `src/fern/types/payment_link_completed_webhook.py` — `remaining-d7497fa8-src-fern-types-payment-link-completed-webhook-py` (remeasure).
- `src/fern/types/payment_link_completed_webhook_status.py` — `remaining-d7497fa8-src-fern-types-payment-link-completed-webhook-status-py` (remeasure).
- `src/fern/types/payment_link_expired_webhook.py` — `remaining-d7497fa8-src-fern-types-payment-link-expired-webhook-py` (remeasure).
- `src/fern/types/payment_link_expired_webhook_status.py` — `remaining-d7497fa8-src-fern-types-payment-link-expired-webhook-status-py` (remeasure).

## Remaining files: 215ec23ddd849ffd78349383788255dfeb417532c81f6dc5c2cdd6b5c577ab02

- `README.md` — `example-optional-members` (example-values).
- `reference.md` — `example-optional-members` (example-values).
- `src/fern/files/client.py` — `example-presence` (snippet-rendering).
- `src/fern/transcripts/raw_client.py` — `remaining-215ec23d-src-fern-transcripts-raw-client-py` (remeasure).
- `src/fern/transcripts/types/transcript_list_item.py` — `x-fern-type-extension` (remeasure).
