# Streaming shapes

The twelve streaming keys: four `text/event-stream` media shapes in
[`bodies-media.md`](../bodies-media.md) and eight forms of the
`x-fern-streaming` extension in [`oas31-extensions.md`](../oas31-extensions.md).
Each media key is searched on its own census predicate. The extension keys are
searched on the extension's own selector, `operation.x-fern-streaming`, and each
document declaring it is screened for the key's exact form, because a field
selector cannot tell a `terminator` from a boolean.

## Witness search

**The registered corpus.** The census walk read all 243 registered golden sources
at `a2ed5e75a`. None declares a media predicate below. Four declare
`x-fern-streaming`: `crozier-sdk-extensions`, `sse-streaming` and the two
TrueForge rows. None declares an extension form below. The nearest is
`crozier-sdk-extensions`: its stream-condition body is a `$ref` with no required
property, but its Request Body Object is `required: true`, and that keeps the
JSON content-type header, which is the behaviour at issue.

**GitHub code search.** Eight phrasings, each excluding the `fern-api`
organisation, went through
`tools/witness-search/witness-search-github.py`'s guarded `Acquirer`. Each read page 1
at `per_page=20` from `/search/code` on the guarded `code_search` bucket.
[`queries.tsv`](queries.tsv) records each answer and how many results it
reported. No later page, size partition, publisher tree or other registry was
searched.

The 116 distinct results were each fetched at their indexed commit on the guarded raw lane
and read by the census and the screen below; [`census.tsv`](census.tsv) records
each one's pinned identity, SHA-256, declarations and verdict. 27 documents
declare a key, and [`screens.tsv`](screens.tsv) screens each of them:

- **Registered.** The PrivateGPT API (`zylon-ai/private-gpt`, Apache-2.0) declares
  `fern-streaming-condition-json-lines` and `fern-streaming-condition-operation-id`
  completely. Seven copies of it sit in other repositories. The publisher's own
  revision `8119842ae6f1f5ecfaf42b06fa0d1ffec675def4` is corpus row 1600,
  `zylon-private-gpt`. It is the last revision before the publisher's 2026
  revamp dropped the extension.
- **Deferred.** Mozilla's Tabstack API (`Mozilla-Ocho/tabstack-cli`, MIT) is an
  admissible, complete candidate. It is the publisher's own description, its
  repository licence is one [`docs/corpus-licensing.md`](../../corpus-licensing.md)
  admits, and it declares `media-type-event-stream-event-dispatch` completely.
  Fern generates it. crozier's event-field dispatch blocks in its `automate` and
  `research` raw clients match the certified pair byte for byte. Its registration
  is deferred to a follow-up because its complete golden depends on seams outside
  streaming, which other work owns. The rest of its tree differs in four classes:
  - an `operationId` read with its tag (`automateV1` under `Automate` is Fern's
    `automate_v1`);
  - deep inline union variant hoisting;
  - forward-reference emission;
  - a 400 body Fern types `typing.Any`.

  By the manager's ruling this record does not register it, and a follow-up
  waits on those repairs.
- **Blocked** on redistribution (no grant):
  - Snowflake's Cortex Agents description: its own `info.license` reads
    `Not licensed`;
  - `inkeep/chat-api-openapi-schema` and `octoml/fern-config`: no licence
    anywhere;
  - API Evangelist's unlicensed third-party profiles of the ElevenLabs, Vital
    and Terminal Use APIs, which declare the boolean form and the format-only
    form.
- **Excluded** on publisher provenance:
  - the Spiceflow framework's generated sample documents, which declare the
    format-only form completely;
  - an examples directory declaring `terminator`;
  - a documentation platform's test input.

These are search candidates; only row 1600 is a registered real-specification match.

| key | verdict | why |
|---|---|---|
| `media-type-event-stream-binary-schema` | `search-incomplete` | none of the 243 registered sources or 116 fetched documents declares it, but the bounded pages exhaust no search source |
| `media-type-event-stream-inline-const-union` | `search-incomplete` | none of the 243 registered sources or 116 fetched documents declares it, but the bounded pages exhaust no search source |
| `media-type-event-stream-item-schema` | `search-incomplete` | none of the 243 registered sources or 116 fetched documents declares it, but the bounded pages exhaust no search source |
| `media-type-event-stream-event-dispatch` | `search-incomplete` | Tabstack declares it completely but its registration is deferred, and the other two declaring documents grant nothing; the bounded pages exhaust no search source |
| `fern-streaming-boolean` | `search-incomplete` | only unlicensed third-party profiles and a test input declare it; the bounded pages exhaust no search source |
| `fern-streaming-format-over-json` | `search-incomplete` | an unlicensed profile and the Spiceflow framework's sample documents declare it; the bounded pages exhaust no search source |
| `fern-streaming-terminator` | `search-incomplete` | only an examples directory declares it; the bounded pages exhaust no search source |
| `fern-streaming-condition-ref-body-header` | `search-incomplete` | no registered source or fetched document declares it with an unrequired body; the bounded pages exhaust no search source |
| `fern-streaming-condition-shared-body` | `search-incomplete` | none of the 243 registered sources or 116 fetched documents declares it, but the bounded pages exhaust no search source |
| `fern-streaming-condition-union-body` | `search-incomplete` | none of the 243 registered sources or 116 fetched documents declares it, but the bounded pages exhaust no search source |
| `media-type-event-stream` | `search-incomplete` | no registered golden reaches the arms `src/ir.rs::sse_event_dispatch[if !discriminator\.mapping\.is_empty\(\) \{]` and `src/emit.rs::raw_stream_method[StreamProtocol::Sse \{ terminator, events \} if !events\.is_empty\(\) => \{]`, and the only declaring document a golden could come from, Tabstack, is deferred; the bounded pages exhaust no search source |
| `fern-streaming-extension` | `search-incomplete` | no registered golden reaches the arms `src/emit.rs::sse_end[=\x7cend\x7c format!]` and `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]`, and no fetched document declaring a terminator or a stream-condition union body is registrable; the bounded pages exhaust no search source |
| `fern-streaming-condition-json-lines` | `witness-found` | registered as corpus row 1600, `zylon-private-gpt` |
| `fern-streaming-condition-operation-id` | `witness-found` | registered as corpus row 1600, `zylon-private-gpt` |

## Renewed search

The renewed search is the same pass, read for registrability. No candidate this
node can register declares a key below.

| key | outcome | selector | declarations | hand-written fixture |
|---|---|---|---|---|
| `media-type-event-stream-binary-schema` | `none-registrable` | `operation.responses:event-stream-binary` | 0 in 243 registered sources; 0 in 116 candidates | `event-stream-binary-download` |
| `media-type-event-stream-inline-const-union` | `none-registrable` | `operation.responses:event-stream-inline-const-union` | 0 in 243 registered sources; 0 in 116 candidates | `event-stream-const-tagged-union` |
| `media-type-event-stream-item-schema` | `none-registrable` | `operation.responses:event-stream-item-schema-ref` | 0 in 243 registered sources; 0 in 116 candidates | `event-stream-item-schema` |
| `media-type-event-stream-event-dispatch` | `none-registrable` | `operation.responses:event-stream-event-dispatch` | 0 in 243 registered sources; 3 in 116 candidates, one deferred and two without a grant | `event-stream-event-dispatch` |
| `fern-streaming-boolean` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 11 in 116 candidates: ten unlicensed profiles and one test input | `streaming-extension-boolean` |
| `fern-streaming-format-over-json` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 3 in 116 candidates, none with publisher provenance and a grant | `streaming-extension-sse-format` |
| `fern-streaming-terminator` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 2 in 116 candidates, both examples | `streaming-extension-terminator` |
| `fern-streaming-condition-ref-body-header` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 0 in 116 candidates | `stream-condition-ref-body-header` |
| `fern-streaming-condition-shared-body` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 0 in 116 candidates | `stream-condition-shared-body` |
| `fern-streaming-condition-union-body` | `none-registrable` | `operation.x-fern-streaming` | 0 in 243 registered sources; 0 in 116 candidates | `stream-condition-union-body` |
| `media-type-event-stream` | `none-registrable` | `operation.responses:event-stream-event-dispatch` | the two arms: 0 registered sources; Tabstack deferred | `event-stream-event-dispatch` |
| `fern-streaming-extension` | `none-registrable` | `operation.x-fern-streaming` | the two arms: 0 registered sources; 2 terminator candidates, both examples; 0 union-body candidates | `streaming-extension-terminator`, `stream-condition-union-body` |

Each fixture is weaker evidence than a real specification. It declares only its
key's shape, and it is not a corpus registration.
