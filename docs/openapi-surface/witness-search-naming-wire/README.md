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
| `openapi31-titled-array-body-content-type` | `registered` | `tamoss`: its complete certified golden and missing-header negative regression prove the shape; the declaring `langchain` witness retains independent residuals. |
| `enum-visit-kwargs-parameter` | `search-incomplete` | `langchain`: the same independent residuals prevent complete registration. |

## Renewed search

The corresponding hand-written documents isolate each shape, including nearby
controls. Their complete certified trees are compared in both enum modes by
the real-binary golden gates. They do not establish public-specification parity.

| key | outcome | reason |
|---|---|---|
| `camel-case-tag-group-and-prefix` | `none-registrable` | The declaring `kompaz` document still differs outside the owned naming shape. |
| `multipart-optional-enum-part-plain-field` | `none-registrable` | The declaring `speech-ai` document still differs outside the owned multipart shape. |
| `openapi31-titled-array-body-content-type` | `registered` | `tamoss` supersedes the authored feature cover. The unchanged array control is retained as a naming-wire measurement. |
| `enum-visit-kwargs-parameter` | `none-registrable` | The declaring `langchain` document still differs outside the owned enum visitor shape. |

## Nullable enum-reference arm

The new `src/ir.rs::nullable_enum_part[    member$]` reading of
`media-type-multipart` has no executed regions in the freshly measured
registered golden tier. The public `speech-ai` document declares the enum
reference beside null, but remains blocked by its independent request-body
residuals. The authored transcript fixture reaches this arm; its object part
remains JSON-encoded.

| key | verdict | declaring public witness |
|---|---|---|
| `media-type-multipart` | `search-incomplete` | `speech-ai`: independent one-member allOf body residuals prevent registration. |

| key | outcome | reason |
|---|---|---|
| `media-type-multipart` | `none-registrable` | The declaring `speech-ai` document still differs outside this arm. |
