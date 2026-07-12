# Canonical real-world OpenAPI corpus (issue #77)

This manifest tracks the 50-spec corpus discovery queue. `decision` is `committed` only when this repo already carries both the spec and Fern golden output; otherwise the spec is link-only until licensing and Fern generation complete. Floating `HEAD` entries must be pinned to immutable commits before their specs or generated output are regenerated.

| # | name | method | source | pinned ref | license | decision | shapes |
|---:|---|---|---|---|---|---|---|
| 1 | `elevenlabs` | method1 | https://github.com/elevenlabs/elevenlabs-python | `HEAD` | unknown | link-only | bearer auth; streaming audio; multipart uploads; large schema graph |
| 2 | `square` | method1 | https://github.com/square/square-python-sdk | `HEAD` | unknown | link-only | oauth; pagination; webhooks; money/value objects |
| 3 | `webflow` | method1 | https://github.com/webflow/js-webflow-api | `HEAD` | unknown | link-only | bearer auth; nested CMS schemas; pagination |
| 4 | `cohere` | method1 | https://github.com/cohere-ai/cohere-python | `HEAD` | unknown | link-only | bearer auth; embeddings; streaming responses |
| 5 | `merge` | method1 | https://github.com/merge-api/merge-python-client | `HEAD` | unknown | link-only | bearer auth; multi-product schema graph; pagination |
| 6 | `assemblyai` | method1 | https://github.com/AssemblyAI/assemblyai-python-sdk | `HEAD` | unknown | link-only | bearer auth; file URLs; async transcript workflows |
| 7 | `flatfile` | method1 | https://github.com/FlatFilers/flatfile-docs-kitchen-sink | `HEAD` | unknown | link-only | bearer auth; events; discriminated resources |
| 8 | `candid-health` | method1 | https://github.com/Candid-Health/candid-python | `HEAD` | unknown | link-only | bearer auth; healthcare schemas; errors |
| 9 | `vapi` | method1 | https://github.com/VapiAI/server-sdk-python | `HEAD` | unknown | link-only | bearer auth; calls; assistants; webhooks |
| 10 | `samsara` | method1 | https://github.com/samsara-dev/samsara-python | `HEAD` | unknown | link-only | bearer auth; pagination; fleet telemetry |
| 11 | `deepgram` | method1 | https://github.com/deepgram/deepgram-python-sdk | `HEAD` | unknown | link-only | bearer auth; streaming; multipart media |
| 12 | `vectara` | method1 | https://github.com/vectara/python-sdk | `HEAD` | unknown | link-only | bearer auth; search/query schemas |
| 13 | `pinecone` | method1 | https://github.com/pinecone-io/pinecone-python-client | `HEAD` | unknown | link-only | api key auth; vector indexes; data-plane/control-plane split |
| 14 | `launchdarkly` | method1 | https://github.com/launchdarkly/api-client-python | `HEAD` | unknown | link-only | api key auth; feature flags; environments |
| 15 | `auth0` | method1 | https://github.com/auth0/auth0-python | `HEAD` | unknown | link-only | oauth; management APIs; errors |
| 16 | `payabli` | method1 | https://github.com/payabli/sdk-python | `HEAD` | unknown | link-only | bearer auth; payments; nested schemas |
| 17 | `payroc` | method1 | https://github.com/payroc/worldnet-python-sdk | `HEAD` | unknown | link-only | payments; auth headers; error responses |
| 18 | `frameio` | method1 | https://github.com/Frameio/python-frameio-client | `HEAD` | unknown | link-only | bearer auth; assets; pagination |
| 19 | `fern-seed-query-parameters` | method1 | https://github.com/fern-api/fern/tree/3a471b03d4778f291849adc03bacfcd40340fc26/seed/query-parameters-openapi | `3a471b03d4778f291849adc03bacfcd40340fc26` | Apache-2.0 | committed | query parameters; nested schemas; SSE runtime |
| 20 | `fern-exhaustive` | method1 | https://github.com/fern-api/fern/tree/3a471b03d4778f291849adc03bacfcd40340fc26/seed/exhaustive | `3a471b03d4778f291849adc03bacfcd40340fc26` | Apache-2.0 | committed | large shape coverage; errors; auth; docs |
| 21 | `readme` | method2 | https://github.com/readmeio/oas | `HEAD` | unknown | link-only | OpenAPI parser corpus; polymorphic schemas |
| 22 | `stainless` | method2 | https://github.com/stainless-api/stainless | `HEAD` | unknown | link-only | openapi config examples; auth; pagination |
| 23 | `speakeasy` | method2 | https://github.com/speakeasy-api/openapi-generation-tests | `HEAD` | unknown | link-only | generator stress specs; unions; pagination |
| 24 | `openai` | method2 | https://github.com/openai/openai-openapi | `HEAD` | MIT | link-only | bearer auth; SSE; multipart; large schemas |
| 25 | `stripe` | method2 | https://github.com/stripe/openapi | `HEAD` | MIT | link-only | api key auth; polymorphic resources; pagination |
| 26 | `twilio` | method2 | https://github.com/twilio/twilio-oai | `HEAD` | MIT | link-only | basic auth; path-heavy APIs; enums |
| 27 | `slack` | method2 | https://github.com/slackapi/slack-api-specs | `HEAD` | MIT | link-only | bearer auth; forms; large enum sets |
| 28 | `sendgrid` | method2 | https://github.com/sendgrid/sendgrid-oai | `HEAD` | MIT | link-only | api key auth; mail payloads; nested arrays |
| 29 | `docusign` | method2 | https://github.com/docusign/OpenAPI-Specifications | `HEAD` | MIT | link-only | oauth; envelopes; multipart |
| 30 | `github-rest` | method2 | https://github.com/github/rest-api-description | `HEAD` | MIT | link-only | api versioning; pagination; error responses |
| 31 | `azure-rest` | method2 | https://github.com/Azure/azure-rest-api-specs | `HEAD` | MIT | link-only | oauth; massive schema graph; long-running operations |
| 32 | `aws-apigateway` | method2 | https://github.com/aws/aws-sdk-js-v3 | `HEAD` | Apache-2.0 | link-only | AWS rest-json shapes; auth extensions; errors |
| 33 | `digitalocean` | method2 | https://github.com/digitalocean/openapi | `HEAD` | Apache-2.0 | link-only | bearer auth; pagination; resource graphs |
| 34 | `adyen` | method2 | https://github.com/Adyen/adyen-openapi | `HEAD` | MIT | link-only | payments; versioned APIs; enums |
| 35 | `box` | method2 | https://github.com/box/box-openapi | `HEAD` | Apache-2.0 | link-only | oauth; file operations; pagination |
| 36 | `atlassian` | method2 | https://github.com/api-evangelist/atlassian | `HEAD` | unknown | link-only | basic/oauth; issue schemas; pagination |
| 37 | `linear` | method2 | https://github.com/linear/linear | `HEAD` | unknown | link-only | graphql-adjacent REST; webhooks; pagination |
| 38 | `shopify` | method2 | https://github.com/Shopify/shopify-api-js | `HEAD` | MIT | link-only | api key/oauth; webhooks; typed resources |
| 39 | `algolia` | method2 | https://github.com/algolia/api-clients-automation | `HEAD` | MIT | link-only | api key auth; search settings; generated clients |
| 40 | `okta` | method2 | https://github.com/okta/okta-management-openapi-spec | `HEAD` | Apache-2.0 | link-only | oauth/api token; identity schemas; pagination |
| 41 | `postman` | method2 | https://github.com/postmanlabs/openapi-to-postman | `HEAD` | Apache-2.0 | link-only | converter corpus; examples; schema edge cases |
| 42 | `kong` | method2 | https://github.com/Kong/spec-renderer | `HEAD` | Apache-2.0 | link-only | gateway/admin APIs; plugin schemas |
| 43 | `nango` | method2 | https://github.com/NangoHQ/nango | `HEAD` | Elastic-2.0 | link-only | integration APIs; auth config; metadata |
| 44 | `supabase` | method2 | https://github.com/supabase/supabase | `HEAD` | Apache-2.0 | link-only | multi-service APIs; auth; storage |
| 45 | `keycloak` | method2 | https://github.com/keycloak/keycloak | `HEAD` | Apache-2.0 | link-only | oauth/admin APIs; realm schemas |
| 46 | `ory` | method2 | https://github.com/ory/sdk | `HEAD` | Apache-2.0 | link-only | identity APIs; error envelopes; pagination |
| 47 | `cloudflare` | method2 | https://github.com/cloudflare/api-schemas | `HEAD` | Apache-2.0 | link-only | api token auth; envelopes; discriminators |
| 48 | `vercel` | method2 | https://github.com/vercel/openapi | `HEAD` | unknown | link-only | bearer auth; deployments; pagination |
| 49 | `nylas` | method2 | https://github.com/nylas/openapi | `HEAD` | unknown | link-only | bearer auth; calendar/email schemas |
| 50 | `fireblocks` | method2 | https://github.com/fireblocks/fireblocks-openapi-spec | `HEAD` | unknown | link-only | api key/JWT; financial schemas; webhooks |
