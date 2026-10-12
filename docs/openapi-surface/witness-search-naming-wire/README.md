# Client naming and request encoding witness search

## Bounded public witnesses

The publisher documents in
`docs/fern-measurements/blocked-witnesses/witnesses.tsv` declare these shapes.
Their immutable revisions and SHA-256 digests identify the input bytes. They
remain unsuitable as complete golden proofs because their independent residuals
are still open; their fresh whole-tree comparisons are recorded in the blocked
witness diffs. This bounded search makes no claim about other public documents.

| key | verdict | declaring public witness and remaining blocker |
|---|---|---|
| `camel-case-tag-group-and-prefix` | `search-incomplete` | `kompaz`: problem-response model emission still differs. |
| `multipart-optional-enum-part-plain-field` | `search-incomplete` | `speech-ai`: one-member allOf request bodies still differ. |
| `openapi31-titled-array-body-content-type` | `search-incomplete` | `langchain`: stream-mode enum hoisting, collapsed-union descriptions and union examples still differ. |
| `enum-visit-kwargs-parameter` | `search-incomplete` | `langchain`: the same independent residuals prevent complete registration. |

## Renewed search

The corresponding hand-written documents isolate each shape, including nearby
controls. Their complete certified trees are compared in both enum modes by
the real-binary golden gates. They do not establish public-specification parity.

| key | outcome | reason |
|---|---|---|
| `camel-case-tag-group-and-prefix` | `none-registrable` | The declaring `kompaz` document still differs outside the owned naming shape. |
| `multipart-optional-enum-part-plain-field` | `none-registrable` | The declaring `speech-ai` document still differs outside the owned multipart shape. |
| `openapi31-titled-array-body-content-type` | `none-registrable` | The declaring OpenAPI 3.1 `langchain` document still differs outside the owned body shape. |
| `enum-visit-kwargs-parameter` | `none-registrable` | The declaring `langchain` document still differs outside the owned enum visitor shape. |
