# Intended departures from Fern's output

crozier's output matches Fern's byte for byte, comments aside — except where
crozier departs on purpose. Every such place is one entry of the **departure
catalog**, [`assets/departures.yml`](../../assets/departures.yml), which is
compiled into the `crozier` binary. One comparison engine
([`src/parity.rs`](../../src/parity.rs)) applies it everywhere crozier's output is
compared with Fern's: [`crozier compare`](../compare.md#intended-departures) and
every golden comparison in crozier's own test suite. No comparison keeps a
private copy of a departure.

## The defect rule

Matching Fern does not mean copying its bugs.

- A Fern **defect** is docs or examples that contradict the generated code (for
  example, `reference.md` documenting a return type or argument the method does
  not have); an example call that does not match the generated signature (a
  missing required argument, an argument the method does not take, a repeated
  keyword, an empty argument value); an example value invalid for its own
  schema; or a generated package whose own entry point cannot be imported.
- crozier's docs and examples always match crozier's code.
- Simplifications in illustrative snippets, such as a streaming example's
  `yield` at module level, are Fern behaviour and are matched byte for byte. So
  is everything else that is merely surprising.

A departure of kind `fern-defect` is a place crozier corrects a defect under this
rule. Its entry says why Fern's output is wrong under it, and its evidence note
shows it.

## What an entry holds

| Key | Holds |
| --- | --- |
| `id` | a unique lower-kebab slug naming the shape in crozier's own terms; entries are sorted by it |
| `kind` | one of the kinds below |
| `trigger` | the input and file that produce the departure |
| `fern` | what Fern writes there |
| `crozier` | what crozier writes instead |
| `reason` | why it is intended; for a `fern-defect`, why Fern's output is wrong under the defect rule |
| `evidence` | a committed note under `docs/departures/evidence/` recording the command that shows the departure and its result |

Each entry's **rule** is the function of the same id in
[`src/departures.rs`](../../src/departures.rs). It recognises exactly Fern's
construct and crozier's replacement in a pair of files, in one of three shapes:
a region of the pair found from the files' structure, an aligned pair of lines,
or a line only crozier writes. An entry without a rule, or a rule without an
entry, fails the catalog's validation, as does an id out of order or repeated,
an empty field, or evidence outside `docs/departures/evidence/`.

## How the engine compares two files

1. **Mechanics** run on both sides, keeping every line where it is: a `.py`
   file's Python comments are stripped.
2. A **region rule** may recognise a whole construct and replace crozier's
   region with Fern's.
3. The two sides' lines are aligned, and inside each run of differing lines a
   **line rule** may pair one Fern line with the crozier line aligned to it, or
   account for a line only crozier writes. Each line it accounts for is
   replaced with Fern's.
4. **The verdict**: what remains is compared exactly. Any difference no rule
   explained fails the file — even on a line, or in a file, where a departure
   applied. A rule never excuses a whole file.

Every departure applied is reported by catalog id, file, and crozier's 1-based
line: the first line of crozier's replacement, or, where crozier writes no line,
the line before which Fern's stand.

## Comparison mechanics outside the catalog

Two normalizations remain outside the catalog, because they record no departure:

- **Python comments are not compared.** The byte-match contract is over
  comment-stripped output, and every committed golden is stored stripped, so a
  comment is not part of either side's compared output; there is no Fern line
  for a comment departure to be recorded against. Stripping leaves a
  comment-only line blank, so line numbers are unchanged.
- **An `__init__.py`'s leading blank lines** are dropped at the verdict on both
  sides. They are where the file's header comments stood, and the header
  comments differ in length (Fern's carries an `isort: skip_file` line), so
  this is the comment rule's residue, not a difference in code.

The tree rules are mechanics too: the comparison is bidirectional (a file on
only one side is a difference), a symbolic link is refused rather than followed,
and a committed golden's `.crozier-fern-golden.json` provenance record is not
part of either tree.

## How `crozier compare` reports departures

`crozier compare` lists every departure it applied under `intended departures
applied`, as `file:line id`, and in the JSON report's `comparison.departures` as
`{id, file, line}` (report version 2). A generator whose only differences are
departures is `matched`; any other difference makes it `mismatched`, naming the
file.

## The per-golden ledger

[`tests/fixtures/departures-ledger.tsv`](../../tests/fixtures/departures-ledger.tsv)
records, for each committed Fern golden, every departure the engine applies when
it compares crozier's output with that golden. Its first line is the header, and
each row is four tab-separated fields: `golden`, `file`, `line`, `departure` —
the golden's repository-relative path, the file inside it, crozier's line and
the catalog id. Rows are sorted and unique.

Every golden comparison — the corpus byte-match with `fern-strict` off and on,
the overlay and flat goldens, the hand-written fixtures, the probes and authored
probes, the in-process generation comparison of `tests/generation.rs`, and the
`crozier compare` journey over a departure's evidence tree — holds the
departures it observes to its golden's rows, exactly. It fails, quoting the row,
when:

- a row is **stale**: the engine no longer applies that departure there;
- a departure is **unrecorded**: the engine applies it and no row records it;
- a row names a departure the catalog does not hold, a golden no comparison
  reads, a file that is not a plain relative path inside its golden, or a file
  no comparison of that golden reads;
- a row names a file the comparison also carves out at file level (an
  `unmatched` entry, a crozier-only file, a file pinned to crozier's own bytes);
- a row repeats the one before it, or is out of order;
- the ledger is not the header and four-field rows with a positive line.

An overlay golden takes its base golden's rows for every file it inherits
unchanged. [`tests/fixtures/compared-goldens.json`](../../tests/fixtures/compared-goldens.json)
is the inventory of compared goldens the rows are validated against.

**Regenerate the ledger** with `just departures-ledger`. It runs every golden
comparison with `CROZIER_RECORD_DEPARTURES` set, so each records the departures
it applies instead of holding them to the ledger, then merges the records: each
golden's rows become exactly what its comparisons recorded. Review the diff
before committing it — every new row is a line where crozier now writes
something other than Fern.

## Adding a departure

A fix node that makes crozier depart from Fern on purpose — correcting a Fern
defect, say — adds it this way:

1. **Show it.** Generate the smallest crozier-authored document that triggers
   it with the certified pair (Fern CLI 5.67.1, `fernapi/fern-python-sdk`
   5.20.0), and record the command and its result in a note under
   `docs/departures/evidence/<id>.md`. For a `fern-defect`, show why Fern's
   output is wrong under the defect rule — an import that fails, a call that
   does not match the signature. When a test drives the reference tree, commit
   it, comment-stripped, at `docs/departures/evidence/<id>/fern-reference/`.
2. **Catalogue it.** Add the entry to `assets/departures.yml`, in id order, with
   every key.
3. **Write its rule** in `src/departures.rs`: a function recognising exactly
   Fern's construct and crozier's replacement, registered under the id in
   `rule` and `RULE_IDS`, with unit tests showing it holds on the construct and
   nowhere else.
4. **Regenerate the reference** below with `CROZIER_UPDATE_DEPARTURES=1 cargo
   test --lib departures`.
5. **Record its ledger lines** with `just departures-ledger`, and check every
   new row is the departure you meant.

## The catalog

The rest of this page is rendered from `assets/departures.yml`; a test fails
when the two differ.

<!-- BEGIN GENERATED CATALOG: edit assets/departures.yml, then regenerate -->

| Kind | Entries | Meaning |
| --- | --- | --- |
| `fern-defect` | 13 | Fern's output is wrong under the defect rule; crozier writes the correct output. |
| `branding` | 1 | crozier names itself where Fern names itself. |
| `packaging` | 1 | crozier writes the packaged SDK's publishing details from its own settings. |
| `provenance` | 1 | crozier writes a fixed record of how the SDK was generated. |
| `ordering` | 1 | crozier writes statements whose order has no effect in its own deterministic order. |

### `binary-json-body-example`

- **Kind:** `fern-defect`
- **Trigger:** An inline application/json binary string body is annotated bytes and its worked example passes the default plain string.
- **Fern writes:** Sync and async client docstrings, README and reference.md pass request="string" to a bytes parameter; reference.md also documents that argument as str.
- **crozier writes:** Those exact default example values are b"string", and the reference parameter type is bytes; the bytes annotation and json=request remain matched.
- **Why:** Checking the example against the actual generated bytes annotation rejects the plain string. The corrected bytes value has the right type and the matched SDK wrapper serializes it to JSON.
- **Evidence:** [`docs/departures/evidence/binary-json-body-example.md`](../../docs/departures/evidence/binary-json-body-example.md)

### `body-query-parameter-value`

- **Kind:** `fern-defect`
- **Trigger:** An inline JSON body property sharing its wire key with a query parameter, where the method signature renames the body argument to avoid the collision.
- **Fern writes:** The query parameter's variable as the JSON property's value, including inside convert_and_respect_annotation_metadata.
- **crozier writes:** The renamed body argument as the JSON property's value, retaining the signature, query mapping, converter annotation and every other statement.
- **Why:** The method accepts a distinct body argument but sends the query argument instead, so the caller's body value never reaches its documented body key.
- **Evidence:** [`docs/departures/evidence/body-query-parameter-value.md`](../../docs/departures/evidence/body-query-parameter-value.md)

### `closed-empty-object-example`

- **Kind:** `fern-defect`
- **Trigger:** A required argument whose schema is an object closed with `additionalProperties: false` that declares no `properties`, and whose `patternProperties`, if any, cannot hold a string: its usage example in `README.md`, `reference.md` and the method's docstring.
- **Fern writes:** The free-form placeholder `{"key": "value"}`, laid out over three lines in `README.md` and `reference.md` and on one line in a docstring.
- **crozier writes:** `{}`, on one line, which the schema admits.
- **Why:** An example value invalid for its own schema: such an object admits no key holding the string `"value"`, so validating `{"key": "value"}` against it fails, and a snippet sending it sends a body the API's own schema rejects.
- **Evidence:** [`docs/departures/evidence/closed-empty-object-example.md`](../../docs/departures/evidence/closed-empty-object-example.md)

### `constant-header-docs-arguments`

- **Kind:** `fern-defect`
- **Trigger:** An operation header whose schema defaults to a string (a plain string or an inline string enum, required or not), which the method does not take and the request sends as that constant: `README.md` and `reference.md`.
- **Fern writes:** Method snippets passing the header as an argument with its default (`mist_mode="fine"`), and a `reference.md` parameter block documenting it under the method as `typing.Literal`.
- **crozier writes:** Method snippets and parameter lists without it.
- **Why:** The examples contradict the generated code: the method has no such argument, so the documented call raises `TypeError` for an unexpected keyword argument, and `reference.md` documents an argument the method does not have.
- **Evidence:** [`docs/departures/evidence/constant-header-docs-arguments.md`](../../docs/departures/evidence/constant-header-docs-arguments.md)

### `date-header-constructor-example`

- **Kind:** `fern-defect`
- **Trigger:** A promoted optional date header in a client constructor's Python examples.
- **Fern writes:** The constructor receives a YOUR placeholder string despite its dt.date annotation.
- **crozier writes:** The constructor receives datetime.date.fromisoformat("2023-01-15") and the example imports datetime.
- **Why:** The placeholder is invalid for the declared date schema. The correction uses the certified generator's own date-example form and leaves string placeholders intact.
- **Evidence:** [`docs/departures/evidence/date-header-constructor-example.md`](../../docs/departures/evidence/date-header-constructor-example.md)

### `fern-metadata-generator-config`

- **Kind:** `provenance`
- **Trigger:** `.fern/metadata.json` at the SDK root, when the reference was generated with any generator configuration other than `pydantic_config.enum_type: python_enums` alone (crozier's `client-class-name`, `enum-type: literals`, `extra-fields` or `default-max-retries`, for example).
- **Fern writes:** A `generatorConfig` object recording the configuration Fern's generator ran with, or no `generatorConfig` key under Fern's defaults.
- **crozier writes:** The one fixed metadata record crozier always writes, whose `generatorConfig` is `pydantic_config.enum_type: python_enums` whatever crozier was configured with.
- **Why:** The block records how a generator was run, not anything the SDK does; crozier ships one fixed provenance record rather than imitating the configuration of a Fern run it did not make.
- **Evidence:** [`docs/departures/evidence/fern-metadata-generator-config.md`](../../docs/departures/evidence/fern-metadata-generator-config.md)

### `init-type-checking-import-order`

- **Kind:** `ordering`
- **Trigger:** A lazy-loading `__init__.py` whose `if typing.TYPE_CHECKING:` block imports from several sources.
- **Fern writes:** The block's imports in the order Fern's generator collected them.
- **crozier writes:** The same import statements, in crozier's sorted order.
- **Why:** The block exists only for type checkers and is never executed, and the two blocks import exactly the same names: sorted with ruff's isort, they are identical. crozier emits a deterministic sorted order rather than reproducing Fern's collection order.
- **Evidence:** [`docs/departures/evidence/init-type-checking-import-order.md`](../../docs/departures/evidence/init-type-checking-import-order.md)

### `lifted-base-path-docs-examples`

- **Kind:** `fern-defect`
- **Trigger:** A document-level `x-fern-base-path` (or `x-crozier-base-path`) object whose `path` names a `{placeholder}`, which the client lifts out of every method into a constructor argument: `README.md` and `reference.md`.
- **Fern writes:** Method snippets passing the lifted argument (`edition="v2"`) to methods that do not take it, a `reference.md` parameter block documenting it under each such method, and client constructors that leave it out — even where it is required.
- **crozier writes:** Method snippets and parameter lists without it, and every snippet's constructor passing it first, by keyword: its default (`edition="v2"`), or the `YOUR_EDITION` placeholder Fern's own docstrings use when it has none.
- **Why:** The examples contradict the generated code: each method call raises `TypeError` for an unexpected keyword argument, a required lifted argument left out of the constructor raises `TypeError` for the missing one, and `reference.md` documents an argument the method does not have.
- **Evidence:** [`docs/departures/evidence/lifted-base-path-docs-examples.md`](../../docs/departures/evidence/lifted-base-path-docs-examples.md)

### `lifted-base-path-positional-example`

- **Kind:** `fern-defect`
- **Trigger:** A lifted base-path parameter (see `lifted-base-path-docs-examples`) with a string `default`: the client constructor examples in the docstrings of the root client and every resource client.
- **Fern writes:** The default passed positionally, `FernApi("v2",)`.
- **crozier writes:** The default passed by keyword, `FernApi(edition="v2",)`.
- **Why:** The generated constructor is keyword-only, so the example call does not match its signature: it raises `TypeError` (`takes 1 positional argument but 2 were given`).
- **Evidence:** [`docs/departures/evidence/lifted-base-path-positional-example.md`](../../docs/departures/evidence/lifted-base-path-positional-example.md)

### `multipart-object-required-file-example`

- **Kind:** `fern-defect`
- **Trigger:** A multipart method with a required file beside a JSON-encoded object whose type is a component alias, or whose argument is named json: its client docstring example.
- **Fern writes:** A call omitting the required file argument, although the generated method requires it. The object encoding and json module alias remain valid.
- **crozier writes:** The same example with that required file placeholder, preserving every other argument, the method signature, imports and request encoding.
- **Why:** Binding the documented call to the actual generated sync or async method raises TypeError for a missing required argument. The correction makes the example bind without changing valid generated SDK behavior.
- **Evidence:** [`docs/departures/evidence/multipart-object-required-file-example.md`](../../docs/departures/evidence/multipart-object-required-file-example.md)

### `nullable-items-docs`

- **Kind:** `fern-defect`
- **Trigger:** A query parameter whose inline array `items` admit `null` (`nullable: true`, or a 3.1 `type` list naming `null`), typed `Optional[Union[T, Sequence[T]]]` in the signature: `README.md` and `reference.md`.
- **Fern writes:** `reference.md` documenting the parameter as `Optional[Union[Optional[T], Sequence[Optional[T]]]]`, and a required one's worked call passing `[None]`.
- **crozier writes:** The signature's own type, and the element Fern's worked call passes for the same items without `nullable` (`[1]`, `["trays"]`).
- **Why:** The docs contradict the generated code: `reference.md` documents a type the method's signature does not have, and the documented call passes `None` items that the signature's `Sequence[T]` rejects.
- **Evidence:** [`docs/departures/evidence/nullable-items-docs.md`](../../docs/departures/evidence/nullable-items-docs.md)

### `pattern-narrowed-enum-example`

- **Kind:** `fern-defect`
- **Trigger:** A string enum reference intersected with a scalar string pattern, whose first declared enum value is rejected by that pattern, in a generated default usage example. The comparison has the parsed source document.
- **Fern writes:** The first enum member, or its literal string, as the example argument.
- **crozier writes:** The first declared enum value valid against the complete schema it documents: the enum, the scalar member and the enclosing schema's own constraints. Where no value is valid, or a constraint cannot be decided, Fern's example stands. The enum alias, annotation, description and all other output are retained.
- **Why:** Validating Fern's generated example value against the property's allOf schema rejects it; the replacement satisfies every constraint of it.
- **Evidence:** [`docs/departures/evidence/pattern-narrowed-enum-example.md`](../../docs/departures/evidence/pattern-narrowed-enum-example.md)

### `readme-client-class-casing`

- **Kind:** `fern-defect`
- **Trigger:** No `client-class-name` set, and an organization (crozier's package name) with capitals inside it, such as `LanternHarbor`: `README.md`, and the environment snippet of `reference.md`.
- **Fern writes:** Snippets naming the root client class, its async twin and its environment class with the inner capitals lowered (`LanternharborApi`, `AsyncLanternharborApi`, `LanternharborApiEnvironment`), which the package does not define.
- **crozier writes:** The class names the package defines (`LanternHarborApi`, `AsyncLanternHarborApi`, `LanternHarborApiEnvironment`).
- **Why:** An example that imports a class the generated package does not define contradicts the generated code: the import fails, so the snippet cannot run.
- **Evidence:** [`docs/departures/evidence/readme-client-class-casing.md`](../../docs/departures/evidence/readme-client-class-casing.md)

### `request-alias-reference-parameters`

- **Kind:** `fern-defect`
- **Trigger:** An aliased object JSON body is flattened into method arguments but reference.md advertises a whole request argument.
- **Fern writes:** The reference parameter is request with the alias type, although the generated method has no request argument.
- **crozier writes:** The reference lists the actual flattened arguments and their types and descriptions; generated code and usage examples remain matched.
- **Why:** Binding the advertised request argument to the actual generated signature raises an unexpected-keyword error. The correction documents the arguments the method accepts.
- **Evidence:** [`docs/departures/evidence/request-alias-reference-parameters.md`](../../docs/departures/evidence/request-alias-reference-parameters.md)

### `sdk-identity-header-prefix`

- **Kind:** `branding`
- **Trigger:** Every SDK: the default headers in `core/client_wrapper.py`.
- **Fern writes:** `X-Fern-Language`, `X-Fern-Runtime`, `X-Fern-Platform` and, in the packaged layout, `X-Fern-SDK-Name` and `X-Fern-SDK-Version`.
- **crozier writes:** The same headers with the same values, named `X-Crozier-*`.
- **Why:** crozier identifies itself to the API it calls rather than impersonating Fern's generator.
- **Evidence:** [`docs/departures/evidence/sdk-identity-header-prefix.md`](../../docs/departures/evidence/sdk-identity-header-prefix.md)

### `sdk-name-version-headers`

- **Kind:** `packaging`
- **Trigger:** The packaged layout's `core/client_wrapper.py`, against a reference whose publishing metadata differs from crozier's: one generated without it, or published under another name or version.
- **Fern writes:** No `X-Fern-SDK-Name` / `X-Fern-SDK-Version` header, or one carrying the reference's published distribution name and release version.
- **crozier writes:** `X-Crozier-SDK-Name` naming crozier's project name and `X-Crozier-SDK-Version` carrying crozier's fixed packaged version, `0.0.0`.
- **Why:** crozier always writes the packaged wrapper's identity pair from its own settings; which name and version a reference was published under is release metadata outside the generated code.
- **Evidence:** [`docs/departures/evidence/sdk-name-version-headers.md`](../../docs/departures/evidence/sdk-name-version-headers.md)

### `sdk-variable-docs-examples`

- **Kind:** `fern-defect`
- **Trigger:** A path parameter lifted into a required client field by a document SDK variable: README.md and reference.md examples and parameter documentation.
- **Fern writes:** Constructors omit the required field; method documentation retains the lifted parameter and positional placeholder although the method has no positional argument.
- **crozier writes:** Constructors pass the lifted field by keyword and method documentation follows the generated signature.
- **Why:** Constructor examples fail to bind because their required field is missing; method examples pass an argument the generated method does not accept.
- **Evidence:** [`docs/departures/evidence/sdk-variable-docs-examples.md`](../../docs/departures/evidence/sdk-variable-docs-examples.md)

### `stream-reference-return-type`

- **Kind:** `fern-defect`
- **Trigger:** A streaming method (Server-Sent Events or newline-delimited JSON) whose chunk type is not `bytes`: its heading line in `reference.md`.
- **Fern writes:** The heading's return annotation `-> typing.Iterator[bytes]`, whatever the method yields.
- **crozier writes:** The annotation the sync method declares, `-> typing.Iterator[T]` for its chunk type `T`.
- **Why:** The docs contradict the generated code: `reference.md` documents a return type the method does not have, since iterating it yields parsed `T` chunks, never `bytes`.
- **Evidence:** [`docs/departures/evidence/stream-reference-return-type.md`](../../docs/departures/evidence/stream-reference-return-type.md)

<!-- END GENERATED CATALOG -->
