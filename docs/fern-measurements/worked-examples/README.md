# Worked examples and documentation rendering, measured at the certified pair

Each directory here is a complete tree Fern CLI 5.216.0 with
`fernapi/fern-python-sdk` 5.42.0, the certified pair, generated from the
document beside it, comment-stripped by `crozier internal-strip` and never
edited: `fern-expected/` in the default `python_enums` mode and
`expected-literals/fern-expected/` the overlay of what the literals mode (Fern's
`enum_type` unset) writes differently. Each was generated serially under the
host's `fern-generation.lock` with `just fern-references measurements
worked-examples/<case>` (the overlay with `.../expected-literals`). The
documents are written from scratch for the tickets of #966, invented names
throughout.

[`crates/crozier-e2e/tests/e2e/worked_examples.rs`](../../../crates/crozier-e2e/tests/e2e/worked_examples.rs)
generates each document with crozier in both modes, holds each SDK whole to its
certified tree under the corpus gate's normalization, every departure held to
[the ledger](../../../tests/fixtures/departures-ledger.tsv), and asserts the
bytes each ticket decides. Its `sdk_env_` journey type-checks every worked call
each SDK documents with pyright and validates the repaired values against their
schemas with
[`validate.py`](../../departures/evidence/invalid-example-values/validate.py).
No case is a corpus fixture or settles a coverage row; each ticket's real
witness is the specification its issue names.

| case | ticket | what it pins |
|---|---|---|
| `numeric-dict-pairs` | #540 | a README map argument of two pairs is spread one pair per line whatever its values (numbers, strings, booleans); a one-pair control likewise |
| `readme-list-map-items` | #927 | a `{"key": "value"}` placeholder item of a README list argument is spread over lines, as `reference.md` writes it |
| `fenced-docstring-blanks` | #928 | a fenced root docstring leaves its blank lines empty, and keeps them indented where a line ends in a backslash |
| `field-description-tabs` | #929 | a tab in a description is a `\t` escape in the `pydantic.Field(description=…)` literal and four spaces in the docstring |
| `kept-blank-descriptions` | #930 | a keep-chomped (`|+`) description keeps its trailing blank line for the arguments of a body schema used only as that body, of any type, and loses it where the schema is also a response model |
| `restated-reference-descriptions` | #931 | a bare `$ref` restating a described parent field, and a required typeless body property, document no description; an optional typeless one keeps its own |
| `docstring-example-escapes` | #864 | the `docstring-example-escapes` departure: a worked example's escapes doubled in the docstring |
| `composed-enum-constraints` | #541 | the `pattern-narrowed-enum-example` departure over a dropped `allOf` member's `maxLength` |
| `inline-enum-constraints` | #960 | the same departure over an inline enum's own `pattern` and `maxLength`, and its own `not`; a first member already admitted, a member set none is admitted from, and an undecidable `format` keep the pair's first member |
| `declared-date-examples` | #937 | the `declared-timestamp-property-example` departure over unquoted YAML `format: date` values, the `2000-01-23` sentinel included; a quoted `date` component example as the path argument, as the pair writes it |
| `composed-reference-order` | #933 | a docstring constructor of an `allOf` of two `$ref`s lists the later member's fields first, an inline member restating their fields or adding its own beside them, the added field last; one of a `$ref` and an inline member keeps declaration order |
| `union-example-member` | #935 | an undiscriminated union worked from the first member declaring an example, a field that member inherits passed from it |
| `unresolved-response-optional-body` | #891 | an operation whose importer builds no example passes no optional body; a required one, and one beside a resolved response, keep theirs |
| `optional-enum-query-arrays` | #932 | an optional query array of enum items is left out of the worked call; a plain string array keeps its item example |
| `alias-body-reference-order` | #934 | the `request-alias-reference-parameters` departure where a shared body's duplicate operation collapses: `reference.md` lists the flattened arguments in signature order where the pair lists `request` ahead of the queries |
| `typeless-body-values` | #936 | the `typeless-body-required-arguments` departure: operations declaring `x-codeSamples`, whose calls the pair writes bare, keep every required argument; a required nullable typeless field is left out of the docstring call |
| `composite-path-parameters` | #945, #947 | the `list-path-parameter-example` departure over list, map and union path parameters; the README anchors on the first operation the pair can work |

## What the documents isolate, and what they rule out

Three findings narrowed a case to the condition that decides it, each from a
cut-down copy of the ticket's witness generated at the pair:

- **#930** keeps its blank line only where the body schema is used solely as the
  request body. SeequentEvo's `QueryCriteria` is; the first form of this
  document also returned its body schema from a `GET`, and Fern trimmed every
  `|+` description there whatever the property's type, fence or title.
- **#936**'s bare calls follow from `x-codeSamples`: Aether's
  `knowledge.state.post` writes `client.knowledge_state_post()` with its sample
  and `data={"key": "value"}` without it, whatever its tags, query parameters,
  response or `openapi` version.
- **#927**'s document has no required typeless property: one beside the list
  makes Fern's importer build no example, and its fallback writes two items
  nested under the property's name, a different rule from the layout measured
  here.
