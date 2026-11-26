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

## Richer documentation

Where Fern's output is valid but documents less of the specification than
crozier's, crozier may keep its own: a departure of kind `richer-documentation`.
It admits only output where **both sides are valid** — every documented call
binds to the generated signature, every value is valid for its schema — and
**crozier's documents more of what the specification declares**: an example or
description the document itself states, never a value crozier synthesizes.
Where crozier's only addition would be a placeholder, it matches Fern instead.
The entry's evidence note shows the specification's own declared example or
description and its validity for the schema it documents.

## Usefulness

Where both outputs are valid but crozier's behaves more usefully for the
specification as written, crozier may keep its own: a departure of kind
`usefulness`. Such an entry exists only by a planner's ruling. Its reason
cites the specification text crozier follows, and its evidence note names an
end-to-end test of the behaviour through the generated SDK.

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
or a line only crozier writes — recognised from its text alone, or from its
position among crozier's lines where its meaning depends on its neighbours (an
item of a wrapped list argument, a line of a docstring). An entry without a rule, or a rule without an
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
   applied. No rule excuses a file both sides have.

A **file rule** accounts for a whole file only one side has, and only where it
has checked what stands in its place: `empty-namespace-package` accepts a file
crozier writes under `_/` only when it is Fern's root-level copy unchanged.

Every departure applied is reported by catalog id, file, and crozier's 1-based
line: the first line of crozier's replacement, or, where crozier writes no line,
the line before which Fern's stand; a file rule's departure is reported at line
0.

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
only one side is a difference unless a file rule accounts for it), a symbolic link is refused rather than followed,
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
  reads, a file that is not a plain relative path inside its golden, or (at a
  line other than 0) a file no comparison of that golden reads;
- a row names a file the comparison also carves out at file level (an
  `unmatched` entry, a crozier-only file, a file pinned to crozier's own bytes);
- a row repeats the one before it, or is out of order;
- the ledger is not the header and four-field rows with a positive line, or
  line 0 for a file rule's departure: a whole file only one side has, which may
  be one only crozier writes.

An overlay golden takes its base golden's rows for every file it inherits
unchanged. [`tests/fixtures/compared-goldens.json`](../../tests/fixtures/compared-goldens.json)
is the inventory of compared goldens the rows are validated against.

**Regenerate the ledger** with `just departures-ledger`. It runs every golden
comparison with `CROZIER_RECORD_DEPARTURES` set, so each records the departures
it applies instead of holding them to the ledger, then merges the records: each
golden's rows become exactly what its comparisons recorded. Review the diff
before committing it — every new row is a line where crozier now writes
something other than Fern.

The same recipe regenerates
[the inventory of worked-example values their own schema rejects](evidence/invalid-example-values/README.md),
which the same comparisons hold per golden, recorded under
`CROZIER_RECORD_EXAMPLE_INVENTORY`.

The recipe runs only the tests
[`tests/fixtures/departures-contributors.tsv`](../../tests/fixtures/departures-contributors.tsv)
lists as recording a golden, not the whole e2e suite, and refuses to merge a
run that did not record exactly the `(golden, test)` pairs it lists, or that
left a compared golden unrecorded. Its optional arguments:

- `just departures-ledger GOLDEN...` records only those goldens — closed over
  every other golden their tests record — and keeps every other golden's rows.
- `just departures-ledger --rename OLD=NEW` follows a golden tree moved without
  a byte changed: it checks the tree and its source document against `HEAD`,
  renames the golden in the ledger, both inventories and the contributor list,
  then records. A changed tree is regenerated without `--rename`.
- `just departures-ledger --discover-contributors` runs the whole suite and
  rederives the contributor list; run it when the refusal says to (a comparison
  test added, renamed or removed).

## Adding a departure

A fix node that makes crozier depart from Fern on purpose — correcting a Fern
defect, say — adds it this way:

1. **Show it.** Generate the smallest crozier-authored document that triggers
   it with the certified pair (Fern CLI 5.216.0, `fernapi/fern-python-sdk`
   5.42.0, as `assets/scaffolding/metadata.json` declares), and record the
   command and its result in a note under
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
| `fern-defect` | 52 | Fern's output is wrong under the defect rule; crozier writes the correct output. |
| `branding` | 1 | crozier names itself where Fern names itself. |
| `packaging` | 1 | crozier writes the packaged SDK's publishing details from its own settings. |
| `provenance` | 1 | crozier writes a fixed record of how the SDK was generated. |
| `ordering` | 1 | crozier writes statements whose order has no effect in its own deterministic order. |
| `richer-documentation` | 4 | Both outputs are valid; crozier's documents more of what the specification declares. |
| `usefulness` | 6 | Both outputs are valid; crozier's behaves more usefully for the specification as written. |

### `anyof-path-param-schema-example`

- **Kind:** `richer-documentation`
- **Trigger:** A path parameter whose schema is an inline anyOf or oneOf composition declaring a string schema-level example, a required string query parameter with a referenced schema and its own example, or a required property with an example beside an allOf reference and description-only annotations, or a required property referencing a oneOf component whose declared example validates against exactly one supported alternative: the worked examples of README.md, reference.md and each client.py docstring.
- **Fern writes:** The parameter's own name as its placeholder value (branch_id_or_ref="branch_id_or_ref").
- **crozier writes:** The specification's declared example (branch_id_or_ref="abcdefghijklmnopqrst"). Every other argument and line is retained.
- **Why:** Both calls bind and are valid strings for the parameter's str annotation; crozier's passes the value the specification itself declares, where Fern's passes a placeholder or an arbitrary first alternative. The rule rejects invalid declared union examples and abstains on unsupported assertions.
- **Evidence:** [`docs/departures/evidence/anyof-path-param-schema-example.md`](../../docs/departures/evidence/anyof-path-param-schema-example.md)

### `binary-body-example`

- **Kind:** `fern-defect`
- **Trigger:** A request body the method takes as a single request argument annotated bytes (a binary string body under a media type other than application/octet-stream, wildcard media among them), in the worked examples of README.md, reference.md and each client.py docstring.
- **Fern writes:** The body's declared example, or the "string" sample where it declares none, as a str (request="<binary string>"), which the bytes parameter rejects.
- **crozier writes:** The same text as bytes, its UTF-8 encoding: the str literal behind a b prefix where it is ASCII (request=b"<binary string>"), and spelled with \xNN escapes where it is not; the annotation, the request construction and every other byte of the call remain matched.
- **Why:** Type-checking the documented call against the generated signature rejects the str for the bytes parameter, so the example does not match the code; the bytes literal is a value the annotation admits, carrying the text the document declares.
- **Evidence:** [`docs/departures/evidence/binary-body-example.md`](../../docs/departures/evidence/binary-body-example.md)

### `binary-form-part-example`

- **Kind:** `fern-defect`
- **Trigger:** A multipart form part the method annotates bytes (a part referencing a binary string component, `file: FormFile` with `FormFile = bytes`), in the worked examples of README.md, reference.md and each client.py docstring.
- **Fern writes:** The part's string sample (file="file"), a str for the bytes parameter.
- **crozier writes:** The same sample as bytes (file=b"file"); the annotation, the form encoding and every other byte of the call remain matched.
- **Why:** Type-checking the documented call against the generated signature rejects the str for the bytes parameter, so the example does not match the code; the bytes literal is a value the annotation admits.
- **Evidence:** [`docs/departures/evidence/binary-form-part-example.md`](../../docs/departures/evidence/binary-form-part-example.md)

### `binary-json-body-example`

- **Kind:** `fern-defect`
- **Trigger:** An inline application/json binary string body, which the method annotates bytes, in its worked example.
- **Fern writes:** Sync and async client docstrings, README and reference.md pass request="string" to the bytes parameter, which reference.md documents as bytes.
- **crozier writes:** Those exact default example values are b"string"; the bytes annotation, the reference parameter type and json=request remain matched.
- **Why:** Checking the example against the actual generated bytes annotation rejects the plain string. The corrected bytes value has the right type and the matched SDK wrapper serializes it to JSON.
- **Evidence:** [`docs/departures/evidence/binary-json-body-example.md`](../../docs/departures/evidence/binary-json-body-example.md)

### `body-query-parameter-value`

- **Kind:** `fern-defect`
- **Trigger:** An inline JSON body property sharing its wire key with a query parameter, or its argument name with a header, where the method signature renames the body argument to avoid the collision.
- **Fern writes:** The query parameter's or header's variable as the JSON property's value, including inside convert_and_respect_annotation_metadata.
- **crozier writes:** The renamed body argument as the JSON property's value, retaining the signature, query or header mapping, converter annotation and every other statement.
- **Why:** The method accepts a distinct body argument but sends the query or header argument instead, so the caller's body value never reaches its documented body key.
- **Evidence:** [`docs/departures/evidence/body-query-parameter-value.md`](../../docs/departures/evidence/body-query-parameter-value.md)

### `bracket-query-parameter-call-keyword`

- **Kind:** `fern-defect`
- **Trigger:** A query parameter whose wire name ends in [], passed in a README or reference.md worked call; or such a query parameter or a form-encoded or multipart body property, listed in reference.md's parameter list.
- **Fern writes:** The call passes the argument as <name>_array=, and the parameter list documents **<name>_array:**, a name the generated sync and async methods do not declare; their argument is <name>.
- **crozier writes:** The same call with the generated method's own <name>= keyword, and the parameter list entry **<name>:**, every other byte of each line unchanged, so the worked call, the parameter list and the method signature agree.
- **Why:** Binding the documented call to the actual certified methods raises TypeError for an unexpected keyword argument, and the parameter list names an argument no method declares. The corrected keyword binds and sends the values under the [] wire name, and every listed name is a parameter of the method it documents.
- **Evidence:** [`docs/departures/evidence/bracket-query-parameter-call-keyword.md`](../../docs/departures/evidence/bracket-query-parameter-call-keyword.md)

### `closed-empty-object-example`

- **Kind:** `fern-defect`
- **Trigger:** A required argument whose schema is an object closed with `additionalProperties: false` that declares no `properties`, and whose `patternProperties`, if any, cannot hold a string: its usage example in `README.md`, `reference.md` and the method's docstring.
- **Fern writes:** The free-form placeholder `{"key": "value"}`, laid out over three lines in `README.md` and `reference.md` and on one line in a docstring.
- **crozier writes:** `{}`, on one line, which the schema admits.
- **Why:** An example value invalid for its own schema: such an object admits no key holding the string `"value"`, so validating `{"key": "value"}` against it fails, and a snippet sending it sends a body the API's own schema rejects.
- **Evidence:** [`docs/departures/evidence/closed-empty-object-example.md`](../../docs/departures/evidence/closed-empty-object-example.md)

### `collapsed-anyof-property-description`

- **Kind:** `richer-documentation`
- **Trigger:** An object property declaring a description beside an anyOf or oneOf of two or more inline non-null scalar alternatives, the first undescribed, which both sides type as the one scalar they share: its model field, its client.py and raw_client.py docstring parameter entry, and its reference.md row.
- **Fern writes:** The property undocumented: the bare model field (assistant_id: str), a docstring entry with no description, and a reference.md row with no text after its type.
- **crozier writes:** The property's description: the model field declared with pydantic.Field() and a docstring holding it, the docstring entry's description line, and the reference.md row's em-dash description. The type, the field's requiredness and every other line are retained.
- **Why:** Both outputs type and validate the field identically; crozier's documents the description the specification declares on the property itself, where Fern's documents nothing about it.
- **Evidence:** [`docs/departures/evidence/collapsed-anyof-property-description.md`](../../docs/departures/evidence/collapsed-anyof-property-description.md)

### `colliding-component-own-class`

- **Kind:** `fern-defect`
- **Trigger:** Two or more component schemas whose names spell one class (`kiln/glaze-coat` and `kiln-glaze/coat` are both `KilnGlazeCoat`) and whose schemas differ: every file naming the components that are not the last declaration.
- **Fern writes:** One class for the name, holding the last declaration's fields, so every request field, response or error typed by an earlier colliding component is typed with the last one's model (`left: typing.Optional[KilnGlazeCoat]` holding `right: int`).
- **crozier writes:** The last declaration keeps Fern's class and module byte for byte; each earlier, non-identical one is a class of its own named Fern's class followed by the first ordinal from 2 no other component's class spells (`KilnGlazeCoat2` in `types/kiln_glaze_coat2.py`), and everything it types names it, with its import, lazy-import entry and `__all__` entry. Components whose schemas are identical stay one class, as Fern writes them.
- **Why:** Fern's model for the earlier component is another component's: a request built from its documented fields sends the wrong shape, and a response of its declared shape fails the merged model's validation, a runtime failure under the defect rule. Manager rulings a1 and a3 (#944) keep the surviving class Fern's and give every other colliding component its own.
- **Evidence:** [`docs/departures/evidence/colliding-component-own-class.md`](../../docs/departures/evidence/colliding-component-own-class.md)

### `constant-header-docs-arguments`

- **Kind:** `fern-defect`
- **Trigger:** An operation header whose schema defaults to a string (a plain string or an inline string enum, required or not), which the method does not take and the request sends as that constant: `reference.md`.
- **Fern writes:** A parameter block documenting the header under the method as an argument typed `typing.Literal` (`mist_mode`), although its worked call, like README.md's, leaves the header out.
- **crozier writes:** The method's parameter list without it.
- **Why:** The docs contradict the generated code: `reference.md` documents an argument the method does not have, and passing it as documented raises `TypeError` for an unexpected keyword argument.
- **Evidence:** [`docs/departures/evidence/constant-header-docs-arguments.md`](../../docs/departures/evidence/constant-header-docs-arguments.md)

### `dangling-mapping-variant-fields`

- **Kind:** `fern-defect`
- **Trigger:** A discriminated `oneOf` whose `discriminator.mapping` names, for one value, a target that is no component schema, beside targets that are, and one `oneOf` member no mapping target names tags itself with that value: the union's types module.
- **Fern writes:** The value's wrapper holds a required `value: typing.Any` ahead of its `Literal` tag, so a payload of that variant, which carries the member's properties beside the tag and no `value`, fails to parse, and the only payload the wrapper can send nests them under `value`.
- **crozier writes:** The wrapper carries the member's fields beside the tag, as every other wrapper of the union carries its member's, with the imports and the `update_forward_refs` call those fields need. Every other line, the member's own model with its tag enum included, is Fern's.
- **Why:** The certified SDK cannot exchange the payload its own OpenAPI document declares for that variant: through its real client, a response carrying the variant raises a parsing error on the missing `value`, and the request it sends nests the variant's properties under `value`. crozier's wrapper parses the response and sends it back in the shape the member schema declares.
- **Evidence:** [`docs/departures/evidence/dangling-mapping-variant-fields.md`](../../docs/departures/evidence/dangling-mapping-variant-fields.md)

### `date-header-constructor-example`

- **Kind:** `fern-defect`
- **Trigger:** A promoted optional date or date-time header in a client constructor's Python examples.
- **Fern writes:** The constructor receives a YOUR placeholder string despite its dt.date or dt.datetime annotation.
- **crozier writes:** The constructor receives datetime.date.fromisoformat("2023-01-15") or datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00") and the example imports datetime.
- **Why:** The placeholder is invalid for the declared date schema. The correction uses the certified generator's own date-example form and leaves string placeholders intact.
- **Evidence:** [`docs/departures/evidence/date-header-constructor-example.md`](../../docs/departures/evidence/date-header-constructor-example.md)

### `declared-example-over-placeholder`

- **Kind:** `usefulness`
- **Trigger:** A worked example (README.md, reference.md, each client.py docstring) passing a multipart form part, a multipart object part's property or a header parameter that declares an example, a parameter's falsy example (its own or its examples map's), a query parameter declaring one on an operation whose success body is not JSON, a path parameter declaring one beside a path parameter whose schema is empty, a oneOf or anyOf property's own example, a list item of an enum whose schema declares an example member, or the request body example of an operation whose success body is not JSON.
- **Fern writes:** Its own placeholder: the argument's wire name (label="label", survey_ref="X-Survey-Ref"), 1 for an integer, or the enum's first member (AlertKind.ALL).
- **crozier writes:** The value the specification declares for the argument (label="", depth_metres=0, title="Lizard Point", AlertKind.BEACON_LIT), or for the body (request=[StoreLine(item_id=…, crates=4)] where Fern writes [StoreLine(), StoreLine()]), including an optional argument Fern leaves out. A declared scalar its own schema rejects is not kept: Fern's placeholder stands where the schema accepts it, else `schema-rejected-declared-example` repairs it. Every other argument and line is retained.
- **Why:** Design-review ruling 2 (falsy-property-example, 2026-11-01) keeps the value the API's author declared where the certified pair discards it for a synthesized placeholder, and its principle extends to the enum example member (example-enum-member) and to the kept example-value-source sub-rules; synthesized placeholders never count as more useful.
- **Evidence:** [`docs/departures/evidence/declared-example-over-placeholder.md`](../../docs/departures/evidence/declared-example-over-placeholder.md)

### `declared-examples-array-parameter-value`

- **Kind:** `usefulness`
- **Trigger:** A worked example passing a parameter whose (referenced) schema declares a JSON Schema examples array and no example, or which declares its own examples map, where the certified pair does not take that value.
- **Fern writes:** The parameter's wire name as its placeholder (lamp_id="lampId"), or, beside an examples map, its schema's example (keeper_id="KPR-from-schema").
- **crozier writes:** The examples array's first entry or the examples map's first value (lamp_id="lmp_8f2kq", keeper_id="KPR-from-map"). Every other argument and line is retained.
- **Why:** Design-review ruling 5 (declared-examples-array, 2026-11-01) keeps crozier working a parameter's value from the schema's examples array or the parameter's examples map rather than the certified pair's placeholder.
- **Evidence:** [`docs/departures/evidence/declared-examples-array-parameter-value.md`](../../docs/departures/evidence/declared-examples-array-parameter-value.md)

### `declared-timestamp-property-example`

- **Kind:** `usefulness`
- **Trigger:** A worked example constructing a body field or model field whose schema is a date-time or date string and whose enclosing schema-level object example gives it an ISO value the YAML document writes unquoted, which YAML reads as a timestamp or date (the 2000-01-23T04:56:07 date-time sentinel excepted).
- **Fern writes:** Its date-time placeholder (datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00")), or its date placeholder (datetime.date.fromisoformat("2023-01-15")).
- **crozier writes:** The declared timestamp (high_water_at=datetime.datetime.fromisoformat("2031-04-02T08:15:00+00:00")) or date (date_of_birth=datetime.date.fromisoformat("1977-03-15")), and in a wrapped docstring call its string line. Every other argument and line is retained.
- **Why:** Design-review ruling 3 (yaml-timestamp-parameter-example, 2026-11-01) keeps the unquoted ISO timestamp the API's author declared rather than the certified pair's placeholder; its principle extends from a parameter's example to a date-time property's value in a schema-level object example, and (manager ruling a0) to a format: date property's.
- **Evidence:** [`docs/departures/evidence/declared-timestamp-property-example.md`](../../docs/departures/evidence/declared-timestamp-property-example.md)

### `digit-leading-method-reference-identifiers`

- **Kind:** `fern-defect`
- **Trigger:** An operationId starts with an ASCII digit, and a generated method with its identifier-safe underscore prefix exists: README.md and reference.md only.
- **Fern writes:** The digit-leading method spelling without the underscore, in README calls and reference headings, although the generated method has the underscore.
- **crozier writes:** The identifier the generated SDK defines, retaining every other byte of the line.
- **Why:** The documented call fails Python compilation with an invalid decimal literal and contradicts the generated SDK method, which imports and binds correctly.
- **Evidence:** [`docs/departures/evidence/digit-leading-method-reference-identifiers.md`](../../docs/departures/evidence/digit-leading-method-reference-identifiers.md)

### `digit-leading-property-example-keyword`

- **Kind:** `fern-defect`
- **Trigger:** A request-body property whose name starts with a digit (`5gMmCauseValue`) and that declares an example: the argument passing it in the operation's client docstring examples and its `reference.md` worked call.
- **Fern writes:** `f_5g_mm_cause_value=0` in the docstring and `f_value=0` in `reference.md`, although the method's parameter is `_5g_mm_cause_value`.
- **crozier writes:** `_5g_mm_cause_value=0`, the parameter the method declares, with the same value. Every other byte of the line is retained.
- **Why:** The documented call does not bind: the method takes no `f_5g_mm_cause_value` or `f_value`, so Python raises `TypeError` for the unexpected keyword.
- **Evidence:** [`docs/departures/evidence/digit-leading-property-example-keyword.md`](../../docs/departures/evidence/digit-leading-property-example-keyword.md)

### `discriminated-union-v1-wire-keys`

- **Kind:** `fern-defect`
- **Trigger:** Every SDK: `core/pydantic_utilities.py`'s `parse_obj_as`, the entry point every generated client parses a response through.
- **Fern writes:** Every input that is not a model class is dealiased to Python field names before validation, so under Pydantic v1 a discriminated union whose tag property needs an alias (a wire key `schema` declared as field `schema_`) loses the key Pydantic v1 looks its discriminator up by.
- **crozier writes:** The same function, except that under Pydantic v1 an input whose type holds a discriminated union outside any model (the union itself, or a list, map or optional of one) is validated as received, through a `_has_discriminated_union` helper defined just before it. Pydantic v2's path and every other input are unchanged.
- **Why:** The generated package declares `pydantic >= 1.9.2`, and through the certified SDK's own client a valid response of such a union raises a validation error under Pydantic 1.10 ("Discriminator 'schema_' is missing in value") although Pydantic validates the same payload directly. crozier's parser constructs the variant under both Pydantic majors.
- **Evidence:** [`docs/departures/evidence/discriminated-union-v1-wire-keys.md`](../../docs/departures/evidence/discriminated-union-v1-wire-keys.md)

### `docstring-example-escapes`

- **Kind:** `fern-defect`
- **Trigger:** A worked example in a client method docstring whose code holds a backslash: a string literal escaping a line break, a tab, a quote or a backslash, such as a declared multi-line request value.
- **Fern writes:** The example's bytes as its README and reference.md write them, one backslash per escape (`code="a\nb"`), inside an ordinary triple-quoted docstring, which Python evaluates: help() and an IDE show the escape as the character it names, a real line break inside the string argument.
- **crozier writes:** The same example with every backslash doubled (`code="a\\nb"`), so the evaluated docstring shows the example exactly as the Markdown writers do. Every other byte of the line is unchanged.
- **Why:** The documentation a reader sees through help() or an IDE is the evaluated docstring, and Fern's evaluates to code that does not parse: the line break ends the string literal, so the copied call is a SyntaxError (a `\"` becomes a bare quote that closes it). The doubled backslash evaluates to the example crozier and Fern both write in README.md and reference.md, which parses and binds to the method.
- **Evidence:** [`docs/departures/evidence/docstring-example-escapes.md`](../../docs/departures/evidence/docstring-example-escapes.md)

### `docstring-literal-dollar-escape`

- **Kind:** `fern-defect`
- **Trigger:** A required request property declared as a string `const` holding `$`, lowered to a one-value literal under Fern's default literals enum type: the client docstring examples that pass it.
- **Fern writes:** The literal with an escaped backslash before every `$`, `"\\$PS1"` for the const `$PS1`, while its own README and reference.md pass `"$PS1"`.
- **crozier writes:** The const's own value, `"$PS1"`, as Fern's README and reference.md write it. Every other docstring line, the annotation and the request are retained.
- **Why:** Evaluating the documented example yields `\$PS1`, a value the const does not admit, and the docstring contradicts Fern's own Markdown examples. The correction passes the only value the schema admits.
- **Evidence:** [`docs/departures/evidence/docstring-literal-dollar-escape.md`](../../docs/departures/evidence/docstring-literal-dollar-escape.md)

### `emoji-tag-reference-identifiers`

- **Kind:** `fern-defect`
- **Trigger:** A tag whose name holds a character no Python identifier admits, such as an emoji (⚠️ Not supported yet), which both sides' generated packages name by an identifier-safe module (not_supported_yet): the client calls, source links and imports of README.md and reference.md.
- **Fern writes:** The tag's raw spelling in each (client.⚠️_not_supported_yet.get_orders(...), src/fern/⚠️_not_supported_yet/client.py, from fern.⚠️_not_supported_yet import ...), although its own package names the module not_supported_yet.
- **crozier writes:** The identifier the generated package defines (client.not_supported_yet, src/fern/not_supported_yet/client.py, from fern.not_supported_yet import ...), with every other character of each line retained.
- **Why:** The examples contradict the generated code: Python rejects the documented call with a SyntaxError for the invalid character before anything runs, the linked file does not exist, and no such module can be imported.
- **Evidence:** [`docs/departures/evidence/emoji-tag-reference-identifiers.md`](../../docs/departures/evidence/emoji-tag-reference-identifiers.md)

### `empty-namespace-package`

- **Kind:** `fern-defect`
- **Trigger:** Operations Fern groups under the empty namespace it calls `_`: tagged only with the empty string, or an `operationId` with an empty dotted prefix (`.GetThing`).
- **Fern writes:** The `_` package's files written at the package root rather than under `_/`: the root `client.py`, `raw_client.py` and `__init__.py` are the `_` sub-client's and its package marker (importing `..core` from above the package), its hoisted types sit in the root `types/`, the root client is lost, and docstring examples call `client..method()`; `README.md` and `reference.md` call `client._.method()` and link `src/<package>/_/client.py`.
- **crozier writes:** The same `_` package under `_/` (its `client.py` but for its examples, `raw_client.py`, `__init__.py` and `types/` files Fern's root copies), the root `client.py` and `__init__.py` the root client and package exporting it with a `_` property, and examples calling `client._.method()`; `reference.md`'s links into `_/client.py`, which only crozier's tree holds, carry the `#L<start>-L<end>` range of each documented method there.
- **Why:** The tree cannot be imported: the root package exports no client and its `client.py` imports from above the top-level package, so the documented `from <package> import <Client>` and `client._.method()` raise `ImportError`.
- **Evidence:** [`docs/departures/evidence/empty-namespace-package.md`](../../docs/departures/evidence/empty-namespace-package.md)

### `empty-root-security-optional-credential`

- **Kind:** `usefulness`
- **Trigger:** A document whose root `security` is the empty list, with operations that declare no `security` of their own beside operations that require a credential and none whose own `security` is empty: the root `client.py` and `core/client_wrapper.py`.
- **Fern writes:** The credential required, `api_key: str` in each constructor and its docstring, and its header set unconditionally.
- **crozier writes:** The credential optional, `api_key: typing.Optional[str] = None`, and its header set only when a value was given.
- **Why:** An empty root `security` list means what an absent one does: every operation without its own `security` needs no credential. The certified pair already makes the credential optional for the absent spelling, and crozier reads both spellings alike, so an SDK user can call the unauthenticated operations without inventing a key.
- **Evidence:** [`docs/departures/evidence/empty-root-security-optional-credential.md`](../../docs/departures/evidence/empty-root-security-optional-credential.md)

### `escaped-discriminator-field-name`

- **Kind:** `fern-defect`
- **Trigger:** A discriminated union whose tag property is a name pydantic's BaseModel already holds (schema, json, dict, ...), so each variant declares the tag as an escaped field (schema_) aliased to the wire name: the union's pydantic.Field(discriminator=...) in its type module.
- **Fern writes:** discriminator="schema", the wire name, which no variant declares as a field: the module raises on import under pydantic v1 (ConfigError) and v2 (PydanticUserError), "needs a discriminator field for key 'schema'", and so does every module importing it.
- **crozier writes:** discriminator="schema_", the escaped field name every variant declares, every other byte of the line unchanged.
- **Why:** A generated module that cannot be imported is a defect. The escaped field name imports under pydantic v1 and v2, and validates each variant by its wire tag under v2.
- **Evidence:** [`docs/departures/evidence/escaped-discriminator-field-name.md`](../../docs/departures/evidence/escaped-discriminator-field-name.md)

### `escaped-field-alias-literal`

- **Kind:** `fern-defect`
- **Trigger:** A schema property whose declared name holds a double quote or a backslash, so its model field carries a wire alias, in the generated model module.
- **Fern writes:** The FieldMetadata and pydantic.Field aliases interpolate the name between double quotes unescaped, so it reads as Python: a backslash-quote becomes a shorter name, and a balanced expression such as a" + bearing + " becomes executable code naming an undefined variable.
- **crozier writes:** Both aliases are a string literal whose value is exactly the declared name, every other byte of the line unchanged.
- **Why:** A balanced-expression alias makes the certified model fail to import, and a backslash-quote alias parses and writes the field under a name the document does not declare. The literal alias imports and carries every value under its declared wire name.
- **Evidence:** [`docs/departures/evidence/escaped-field-alias-literal.md`](../../docs/departures/evidence/escaped-field-alias-literal.md)

### `fern-metadata-generator-config`

- **Kind:** `provenance`
- **Trigger:** `.fern/metadata.json` at the SDK root, when the reference was generated with any generator configuration other than `pydantic_config.enum_type: python_enums` alone (crozier's `client-class-name`, `enum-type: literals`, `extra-fields` or `default-max-retries`, for example).
- **Fern writes:** A `generatorConfig` object recording the configuration Fern's generator ran with, or no `generatorConfig` key under Fern's defaults.
- **crozier writes:** The one fixed metadata record crozier always writes, whose `generatorConfig` is `pydantic_config.enum_type: python_enums` whatever crozier was configured with.
- **Why:** The block records how a generator was run, not anything the SDK does; crozier ships one fixed provenance record rather than imitating the configuration of a Fern run it did not make.
- **Evidence:** [`docs/departures/evidence/fern-metadata-generator-config.md`](../../docs/departures/evidence/fern-metadata-generator-config.md)

### `flat-reference-link-target`

- **Kind:** `fern-defect`
- **Trigger:** The flat layout (`layout: flat`): every heading link in `reference.md`.
- **Fern writes:** The link names `src/<package>/<module>/client.py`, the packaged path, which the flat tree does not hold (its modules sit at the root), and carries no `#L<start>-L<end>` range.
- **crozier writes:** The link names the module the flat tree holds (`<module>/client.py`) and carries the range of the documented method there, found as for every other heading. Every other byte of the line is retained.
- **Why:** A link to a file the SDK does not contain documents nothing: following it from the generated tree's own `reference.md` finds no file, so the heading cannot lead to the method it documents.
- **Evidence:** [`docs/departures/evidence/flat-reference-link-target.md`](../../docs/departures/evidence/flat-reference-link-target.md)

### `init-type-checking-import-order`

- **Kind:** `ordering`
- **Trigger:** A subpackage's lazy-loading `__init__.py` (never the root package's) whose `if typing.TYPE_CHECKING:` block imports from several modules.
- **Fern writes:** The block's imports in the order Fern's generator collected them (CloudFormation's `types/__init__.py` imports `ResourcesToImport` and `ResourcesToSkip` ahead of `AcceptTermsAndConditions`).
- **crozier writes:** The same import statements, sorted by module. The root package's block is written in the certified pair's own order (issue #920), so no departure covers it.
- **Why:** The block exists only for type checkers and is never executed, and the reordered statements import exactly the same names: sorted with ruff's isort, the two blocks are identical, or, where they differ in another way, the window of statements that moves is one permutation of identical statements and every other difference in the block remains a difference. crozier emits a deterministic sorted order rather than reproducing Fern's collection order.
- **Evidence:** [`docs/departures/evidence/init-type-checking-import-order.md`](../../docs/departures/evidence/init-type-checking-import-order.md)

### `int64-example-rounded-out-of-range`

- **Kind:** `fern-defect`
- **Trigger:** An integer example of a `format: int64` property, array item or parameter whose nearest double lies outside the signed 64-bit range (`9223372036854775807`, `-9223372036854775808`): the README, reference.md and client docstring examples that pass it.
- **Fern writes:** The double's JavaScript spelling, `9223372036854776000` or `-9223372036854776000`, outside the int64 range.
- **crozier writes:** The declared example exactly. An example whose rounding stays inside the range keeps Fern's rounded spelling.
- **Why:** Validating the documented value against the property's declared int64 bounds rejects Fern's value; the declared example is a valid int64 and satisfies them.
- **Evidence:** [`docs/departures/evidence/int64-example-rounded-out-of-range.md`](../../docs/departures/evidence/int64-example-rounded-out-of-range.md)

### `lifted-base-path-docs-examples`

- **Kind:** `fern-defect`
- **Trigger:** A document-level `x-fern-base-path` (or `x-crozier-base-path`) object whose `path` names a `{placeholder}`, which the client lifts out of every method into a constructor argument: `README.md` and `reference.md`.
- **Fern writes:** Method snippets passing the lifted argument (`edition="v2"`) to methods that do not take it, a `reference.md` parameter block documenting it under each such method, and client constructors that leave it out — even where it is required.
- **crozier writes:** Method snippets and parameter lists without it, and every snippet's constructor passing it first, by keyword: its default (`edition="v2"`), or the `YOUR_EDITION` placeholder Fern's own docstrings use when it has none.
- **Why:** The examples contradict the generated code: each method call raises `TypeError` for an unexpected keyword argument, a required lifted argument left out of the constructor raises `TypeError` for the missing one, and `reference.md` documents an argument the method does not have.
- **Evidence:** [`docs/departures/evidence/lifted-base-path-docs-examples.md`](../../docs/departures/evidence/lifted-base-path-docs-examples.md)

### `list-path-parameter-example`

- **Kind:** `fern-defect`
- **Trigger:** A path parameter whose schema is an array or a map, inline or through a component alias, or a union of object components: the worked calls of the operation in `README.md` and `reference.md`, and, where the value is no `typing.Sequence[str]`, its client docstring examples.
- **Fern writes:** The Markdown calls leave the required argument out (`client.probe()`), or, for a union, write no call at all (`client.probe(...)`); the docstring passes the parameter's string placeholder (`id="ID"`, `values="values"`) for a list of non-strings, a `typing.List[str]` alias or a map, and has no `Examples` section for a union.
- **crozier writes:** Every call passes the argument: the string placeholder where the parameter is a `typing.Sequence[str]` (a `str` is one), else a one-item list or map of the item's example (`id=[1]`, `values={"key": "value"}`), or the union's first member constructed, with the `import datetime` only that value uses; every other byte of the call is retained.
- **Why:** The Markdown calls do not bind, the required argument missing (`TypeError`) or passed as an `Ellipsis`, and the docstring's string is not a value a list of non-strings, a `typing.List` or a map admits.
- **Evidence:** [`docs/departures/evidence/list-path-parameter-example.md`](../../docs/departures/evidence/list-path-parameter-example.md)

### `minimal-worked-call-optional-parameter`

- **Kind:** `usefulness`
- **Trigger:** A worked example (README.md, reference.md, each client.py docstring) of an operation with an optional query parameter that either annotates a $ref through allOf whose target declares an example, or is an array over $ref items with a parameter-level array example.
- **Fern writes:** Passes the optional argument with that declared value (sort="created_at desc", entity_type=["http://pcdm.org/models#Collection"]).
- **crozier writes:** Leaves the optional argument out of the call, so the worked call is minimal.
- **Why:** The user's design-review ruling 4, minimal-worked-call: a worked call is a minimal call carrying the required parameters only, so crozier leaves every optional parameter out of it, even one with a declared example. The certified output passes these arguments; the ruling is followed and that evidence is recorded in the note.
- **Evidence:** [`docs/departures/evidence/minimal-worked-call-optional-parameter.md`](../../docs/departures/evidence/minimal-worked-call-optional-parameter.md)

### `multipart-object-required-file-example`

- **Kind:** `fern-defect`
- **Trigger:** A multipart method with a required file part, with or without a JSON-encoded object part beside it: its client docstring example.
- **Fern writes:** A call omitting the required file argument, although the generated method requires it. The object encoding and json module alias remain valid.
- **crozier writes:** The same example with that required file's placeholder in the form Fern's README uses (`image="example_image"`), preserving every other argument, the method signature, imports and request encoding.
- **Why:** Binding the documented call to the actual generated sync or async method raises TypeError for a missing required argument. The correction makes the example bind without changing valid generated SDK behavior.
- **Evidence:** [`docs/departures/evidence/multipart-object-required-file-example.md`](../../docs/departures/evidence/multipart-object-required-file-example.md)

### `nested-discriminator-flat-wire`

- **Kind:** `fern-defect`
- **Trigger:** A discriminated union mapping to another discriminated union, whose public variant holds the inner union in value.
- **Fern writes:** Serializes a kind/value envelope that fails the source schema, rejects the schema-valid flat provider payload for missing value, and writes an empty argument in the README and reference examples.
- **crozier writes:** Retains Fern's public classes, fields and value constructors, flattens the wire payload and parses flat responses under Pydantic v1 and v2. Worked examples construct the inner variant through value.
- **Why:** The certified SDK cannot exchange the payload its own OpenAPI document declares. Runtime schema validation demonstrates the serialization failure and the rejection of a valid provider response in both Pydantic majors.
- **Evidence:** [`docs/departures/evidence/nested-discriminator-flat-wire.md`](../../docs/departures/evidence/nested-discriminator-flat-wire.md)

### `non-string-client-header-example`

- **Kind:** `fern-defect`
- **Trigger:** A promoted client header the document declares boolean, integer or number, a string header with a default that the constructor types as a one-value typing.Literal, or an array header, in the client construction of a client.py docstring example.
- **Fern writes:** The constructor receives the YOUR_<NAME> string placeholder its string headers take, despite the header's bool, int, float, Literal or List annotation.
- **crozier writes:** The constructor receives the generator's own placeholder for the declared type (True, 1 or 1.1), the Literal's one value, or a list of two copies of the item's placeholder (["probeParam", "probeParam"]); other string headers keep their YOUR_<NAME> placeholder and the README and reference.md constructions stay matched.
- **Why:** A YOUR_* placeholder for a non-string type is a standing Fern defect: the certified constructor's annotations reject the string under strict validation, and the client sends it as the header's value. The typed placeholder validates and is sent as the declared value.
- **Evidence:** [`docs/departures/evidence/non-string-client-header-example.md`](../../docs/departures/evidence/non-string-client-header-example.md)

### `nullable-items-docs`

- **Kind:** `fern-defect`
- **Trigger:** A query parameter whose inline array `items` admit `null` (`nullable: true`, or a 3.1 `type` list naming `null`), typed `Optional[Union[T, Sequence[T]]]` in the signature: `README.md` and `reference.md`.
- **Fern writes:** `reference.md` documenting the parameter as `Optional[Union[Optional[T], Sequence[Optional[T]]]]`, and a required one's worked call passing `[None]`.
- **crozier writes:** The signature's own type, and the element Fern's worked call passes for the same items without `nullable` (`[1]`, `["trays"]`).
- **Why:** The docs contradict the generated code: `reference.md` documents a type the method's signature does not have, and the documented call passes `None` items that the signature's `Sequence[T]` rejects.
- **Evidence:** [`docs/departures/evidence/nullable-items-docs.md`](../../docs/departures/evidence/nullable-items-docs.md)

### `optional-lowered-required-query-array-example`

- **Kind:** `richer-documentation`
- **Trigger:** A required query array parameter, which both signatures take as an optional argument, whose parameter or schema declares an array example, on an operation whose worked example Fern writes without required query arrays (a text/* success body, or a required query parameter exampled as an object or map): the worked examples of README.md, reference.md and each client.py docstring.
- **Fern writes:** The call without the parameter.
- **crozier writes:** The call passing the declared example (channels=[1.0, 2.0] in a docstring, wrapped one item per line in reference.md). A parameter declaring no example is left out, as Fern leaves it.
- **Why:** Both calls bind, since the argument is optional in both signatures; crozier's passes the value the specification declares for a parameter it marks required, and that value is valid for the array schema, where Fern's leaves the required input out of the example.
- **Evidence:** [`docs/departures/evidence/optional-lowered-required-query-array-example.md`](../../docs/departures/evidence/optional-lowered-required-query-array-example.md)

### `optional-raw-body-example-argument`

- **Kind:** `fern-defect`
- **Trigger:** An operation whose optional application/octet-stream body the generated method takes as a required request argument, in its worked example.
- **Fern writes:** Sync and async client docstrings, README and reference.md call the method with no arguments.
- **crozier writes:** Those calls pass request=b"string"; the signature and everything else about the operation's worked example remain matched.
- **Why:** Binding the certified call against the generated signature fails: request is a required keyword argument, so the example does not match the signature.
- **Evidence:** [`docs/departures/evidence/optional-raw-body-example-argument.md`](../../docs/departures/evidence/optional-raw-body-example-argument.md)

### `pattern-narrowed-enum-example`

- **Kind:** `fern-defect`
- **Trigger:** A string enum whose first declared value is rejected by the string constraints at its use site, in a generated default usage example: an enum reference intersected with a scalar string pattern (constraints inside an `allOf` load normalization discards included), or an inline enum declaring `pattern`, `minLength`, `maxLength` or `not` beside its `enum`. The comparison has the parsed source document.
- **Fern writes:** The first enum member, or its literal string, as the example argument.
- **crozier writes:** The first declared enum value valid against the complete schema it documents: the enum, the scalar member and the enclosing schema's own constraints. Where no value is valid, or a constraint cannot be decided, Fern's example stands. The enum alias, annotation, description and all other output are retained.
- **Why:** Validating Fern's generated example value against the property's allOf schema rejects it; the replacement satisfies every constraint of it.
- **Evidence:** [`docs/departures/evidence/pattern-narrowed-enum-example.md`](../../docs/departures/evidence/pattern-narrowed-enum-example.md)

### `readme-abbreviated-call-arguments`

- **Kind:** `fern-defect`
- **Trigger:** The README's demonstrated operation takes a required header and no path, query or body argument: the abbreviated calls of its exception-handling, raw-response, retry and timeout snippets in `README.md`.
- **Fern writes:** `client.probe()` and `client.probe(request_options={...})`, a call with no argument, as Fern writes for an operation taking none.
- **crozier writes:** `client.probe(...)` and `client.probe(..., request_options={...})`, the elision Fern itself writes for an operation that takes arguments. Every other byte of the line is retained.
- **Why:** The documented call does not bind: the method's required header argument is missing, so Python raises `TypeError`.
- **Evidence:** [`docs/departures/evidence/readme-abbreviated-call-arguments.md`](../../docs/departures/evidence/readme-abbreviated-call-arguments.md)

### `readme-client-class-casing`

- **Kind:** `fern-defect`
- **Trigger:** No `client-class-name` set, and an organization (crozier's package name) with capitals inside it, such as `LanternHarbor`: `README.md`, and the environment snippet of `reference.md`.
- **Fern writes:** Snippets naming the root client class, its async twin and its environment class with the inner capitals lowered (`LanternharborApi`, `AsyncLanternharborApi`, `LanternharborApiEnvironment`), which the package does not define. The async snippet's import also keeps the correctly cased sync client its own snippet does not use (`from PetStore import AsyncPetstoreApi, PetStoreApi`), because Fern drops only the lowered spelling from the names it imports.
- **crozier writes:** The class names the package defines (`LanternHarborApi`, `AsyncLanternHarborApi`, `LanternHarborApiEnvironment`), and the async snippet imports only the names it uses.
- **Why:** An example that imports a class the generated package does not define contradicts the generated code: the import fails, so the snippet cannot run.
- **Evidence:** [`docs/departures/evidence/readme-client-class-casing.md`](../../docs/departures/evidence/readme-client-class-casing.md)

### `readme-constructor-required-header`

- **Kind:** `fern-defect`
- **Trigger:** A header on every operation, promoted to the client constructor, that is required and typed boolean, number or array: the client constructions of `README.md` and `reference.md`.
- **Fern writes:** The construction leaves the header out (`client = FernApi()`), although the constructor requires it.
- **crozier writes:** The construction passes it with the typed example the client docstrings give it (`probe_param=["probeParam", "probeParam"]`, `strict_mode=True`). Every other byte of the construction is retained.
- **Why:** The documented construction does not bind: Python raises `TypeError` for the missing required keyword argument.
- **Evidence:** [`docs/departures/evidence/readme-constructor-required-header.md`](../../docs/departures/evidence/readme-constructor-required-header.md)

### `readme-environment-constructor-arguments`

- **Kind:** `fern-defect`
- **Trigger:** A client constructor taking a required argument (a credential, a required header) and a server environment: the Environments snippet of `README.md`.
- **Fern writes:** `client = FernApi(environment=FernApiEnvironment.DEFAULT,)`, the environment alone, although the constructor requires the credential.
- **crozier writes:** The same constructor with the arguments the README's usage snippet passes it (`api_key="<value>"`) before the environment. Every other byte of the snippet is retained.
- **Why:** The documented construction does not bind: Python raises `TypeError` for the missing required keyword argument before the client exists.
- **Evidence:** [`docs/departures/evidence/readme-environment-constructor-arguments.md`](../../docs/departures/evidence/readme-environment-constructor-arguments.md)

### `readme-escaped-method-call`

- **Kind:** `fern-defect`
- **Trigger:** An operation whose generated method name is escaped with a trailing `_` (`all_`, `import_`): the calls of it in `README.md`'s exception-handling, raw-response, retry and timeout snippets.
- **Fern writes:** `client.apis.all(...)`, the method name without its escape, which the client does not define.
- **crozier writes:** `client.apis.all_(...)`, the method the client defines (through `with_raw_response` too). Every other byte of the line is retained.
- **Why:** The documented call raises `AttributeError`: the client has no `all`. The usage snippet in the same README already calls `all_`.
- **Evidence:** [`docs/departures/evidence/readme-escaped-method-call.md`](../../docs/departures/evidence/readme-escaped-method-call.md)

### `recursive-alias-named-type`

- **Kind:** `fern-defect`
- **Trigger:** A schema whose own type names itself, as a recursive JSON value does (`anyOf` of scalars, an array of itself and a map of itself), or that closes a cycle made only of aliases (a union of an array alias and a map alias, each holding it): the type alias module of that schema.
- **Fern writes:** The implicit recursive alias `NAME = typing.Union[..., typing.List["NAME"], ...]`, its other cycle members as quoted forward references. pydantic expands it without end, so every model reaching it hangs, crashes or raises RecursionError on import, under pydantic v1 and v2.
- **crozier writes:** The same alias under `if typing.TYPE_CHECKING:`, the alias named through `typing_extensions.TypeAliasType("NAME", ...)` under pydantic v2, and under v1, which cannot validate a recursive alias, the alias with each quoted reference to itself or to an alias of its cycle read as `typing.Any`. It imports `typing_extensions` and the core's `IS_PYDANTIC_V2`; every other byte of the module is retained.
- **Why:** A generated package whose modules cannot be imported is a defect. The named alias imports and validates nested values under every pydantic version the SDK declares, needs no Python 3.12 syntax, and type checkers read the same recursive alias Fern writes.
- **Evidence:** [`docs/departures/evidence/recursive-alias-named-type.md`](../../docs/departures/evidence/recursive-alias-named-type.md)

### `reference-anchor-follows-corrected-client`

- **Kind:** `fern-defect`
- **Trigger:** A `reference.md` heading whose linked `client.py` carries another departure that adds or removes lines above or inside the documented method (a credential keyword Fern repeats in a docstring example, for instance).
- **Fern writes:** The link's `#L<start>-L<end>` range counts the lines of Fern's own client, with its defect in place.
- **crozier writes:** The range of the same method in crozier's client. Each side's range is exactly that method's `def` line through its last line in its own file, and every other byte of the heading is retained.
- **Why:** Fern's range, applied to crozier's corrected client, links lines that are not the documented method: it starts or ends inside a neighbouring statement. The heading must link the method it documents.
- **Evidence:** [`docs/departures/evidence/reference-anchor-follows-corrected-client.md`](../../docs/departures/evidence/reference-anchor-follows-corrected-client.md)

### `reference-heading-escaped-method-name`

- **Kind:** `fern-defect`
- **Trigger:** An operation whose generated method name is escaped with a trailing `_` because it would shadow a Python keyword or builtin (`all_`, `import_`, `async_`): its heading in `reference.md`.
- **Fern writes:** The heading names the method without its escape (`client.applicants.<a href="src/fern/applicants/client.py">all</a>(...)`), and the link has no `#L<start>-L<end>` anchor, because the linked client defines no method of that name.
- **crozier writes:** The heading names the method the client defines (`all_`) and anchors the link at its lines, as every other heading is anchored. Every other byte of the line is retained.
- **Why:** The heading documents a method the generated client does not have: `client.applicants.all(...)` raises `AttributeError`, and the usage example under the same heading already calls `all_`.
- **Evidence:** [`docs/departures/evidence/reference-heading-escaped-method-name.md`](../../docs/departures/evidence/reference-heading-escaped-method-name.md)

### `renamed-request-options-docs`

- **Kind:** `fern-defect`
- **Trigger:** An operation one of whose own arguments (a body property, parameter or header) is named request_options, so both sides' generated methods take the SDK's options as _request_options: its entry in reference.md's parameter list, and README.md's retry and timeout calls when it is the README's first operation.
- **Fern writes:** The options entry is **request_options:** `typing.Optional[RequestOptions]`, listed beside the argument of the same name, and the README calls pass request_options={"max_retries": 1} and request_options={"timeout": 1}.
- **crozier writes:** The method's own name for its options, **_request_options:** and _request_options={; every other byte of each line, and every signature, remain matched.
- **Why:** The generated method declares no second request_options: the documented options entry names the operation's own argument, and the README's calls bind the options dictionary to that argument, so it is sent in the request as the argument's value and no retry or timeout option is applied.
- **Evidence:** [`docs/departures/evidence/renamed-request-options-docs.md`](../../docs/departures/evidence/renamed-request-options-docs.md)

### `repeated-credential-example-keyword`

- **Kind:** `fern-defect`
- **Trigger:** Two credentials that resolve to one constructor parameter: two header `apiKey` schemes naming the same `X-Api-Key` header, two whose headers stem to one name (`X-API-KEY` and `API-KEY`), or a bearer scheme whose `x-fern-token-variable-name` is `apiKey` beside such a header scheme: `README.md`, `reference.md` and every `client.py`.
- **Fern writes:** Client constructor examples passing the shared keyword twice (`FernApi(api_key="YOUR_API_KEY", api_key="YOUR_API_KEY", ...)`).
- **crozier writes:** The keyword once, as the constructor declares it.
- **Why:** A call repeating a keyword argument does not bind: Python rejects it as a `SyntaxError` before the example runs, so the documented client cannot be built as written.
- **Evidence:** [`docs/departures/evidence/repeated-credential-example-keyword.md`](../../docs/departures/evidence/repeated-credential-example-keyword.md)

### `repeated-query-body-example-keyword`

- **Kind:** `fern-defect`
- **Trigger:** An operation whose required query parameter shares its name with a property of its JSON request body, where the body `$ref`s a component referenced somewhere else too (a response's array items, say), so Fern keeps it a named model and the signature renames the body argument `<model>_<name>`: the worked call in `README.md` and `reference.md`.
- **Fern writes:** The worked call passing the query parameter's keyword twice (`bench="bench", bench="bench"`), where its own signature and docstring name the second `question_bench`. The same mechanism as `repeated-credential-example-keyword`, in a method call rather than the client constructor.
- **crozier writes:** The renamed body argument (`question_bench="bench"`), as the signature declares it and as the docstring's example already passes it.
- **Why:** A call repeating a keyword argument does not bind: Python rejects it as a `SyntaxError` before the example runs, and the signature's required `question_bench` is never passed.
- **Evidence:** [`docs/departures/evidence/repeated-query-body-example-keyword.md`](../../docs/departures/evidence/repeated-query-body-example-keyword.md)

### `request-alias-reference-parameters`

- **Kind:** `fern-defect`
- **Trigger:** An aliased or retained shared object JSON body is flattened into method arguments but reference.md advertises a whole request argument.
- **Fern writes:** The reference parameter is request with the model or alias type, although the generated method has no request argument.
- **crozier writes:** The reference lists the actual flattened arguments and their types and descriptions; generated code and usage examples remain matched.
- **Why:** Binding the advertised request argument to the actual generated signature raises an unexpected-keyword error. The correction documents the arguments the method accepts.
- **Evidence:** [`docs/departures/evidence/request-alias-reference-parameters.md`](../../docs/departures/evidence/request-alias-reference-parameters.md)

### `required-null-union-field-example`

- **Kind:** `fern-defect`
- **Trigger:** A worked example in a generated client's docstring or `reference.md` that constructs a model with a required field whose union type opens with an optional alternative (a nested union carrying a `null` member, which Fern makes `Optional`), the field's own value fitting on one line.
- **Fern writes:** The constructor without that field (Vercel's `PatchtEdgeConfigItemsRequestItemsItemValue(key="key", operation=…)`), although the model declares it with no default.
- **crozier writes:** The same constructor with the field's synthesized example (`value="value",`), a value its union admits; every other argument, the imports and the method signature are unchanged.
- **Why:** Executing the documented construction against the generated model raises pydantic's `ValidationError` for the missing required field, so the example does not match the code. The correction passes the field and constructs a valid model.
- **Evidence:** [`docs/departures/evidence/required-null-union-field-example.md`](../../docs/departures/evidence/required-null-union-field-example.md)

### `schema-rejected-array-length-example`

- **Kind:** `fern-defect`
- **Trigger:** A list in a worked example of `README.md`, `reference.md` or a generated client's docstring that Fern writes with its fixed number of items (one, or two in its fallback example writer, or none where it has no item to show), whose schema's `minItems` or `maxItems` rejects that count. The comparison has the parsed source document.
- **Fern writes:** The list with Fern's fixed number of items (discord's `messages=["messages"]` beneath `minItems: 2`), or none (marimo's `x_bounds=[]` beneath `minItems: 2`).
- **crozier writes:** The specification's own declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else Fern's items cut to `maxItems` or padded to `minItems` with copies of the first item, or, beneath `uniqueItems: true`, with pairwise-distinct items the item schema accepts. Where Fern writes the list empty, with no item to copy (a tuple's `prefixItems`, a nullable item an executable docstring leaves out), the items the schema's own shape builds: each `prefixItems` member's value, or `minItems` copies of its items' (`None` for a nullable item). Where no such items can be built, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-array-length-example.md`](../../docs/departures/evidence/schema-rejected-array-length-example.md)

### `schema-rejected-declared-example`

- **Kind:** `fern-defect`
- **Trigger:** A scalar in a worked example of `README.md`, `reference.md` or a generated client's docstring that the specification itself declares — an `example`, `examples` or `default` at any level, an enclosing body's or parameter's example included — whose own schema rejects it by an in-scope keyword or format. The comparison has the parsed source document.
- **Fern writes:** The declared value as written (dot-ai's `execute_choice=42` beneath `maximum: 1`, RayBot's `ip="192.168.1.100/24"` beneath `format: ipv4`).
- **crozier writes:** Another declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else a value constructed deterministically to satisfy every in-scope keyword. Where no such value exists or crozier cannot decide validity, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule, whoever chose it: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-declared-example.md`](../../docs/departures/evidence/schema-rejected-declared-example.md)

### `schema-rejected-name-example`

- **Kind:** `fern-defect`
- **Trigger:** A string parameter or property, in a worked example of `README.md`, `reference.md` or a generated client's docstring, whose schema declares no example Fern uses and rejects the parameter's or property's own name by a `pattern`, `minLength`, `maxLength`, `enum`, `const` or a `date`, `date-time`, `time`, `uuid`, `email`, `uri`, `ipv4`, `ipv6` or `hostname` `format`. The comparison has the parsed source document.
- **Fern writes:** The name as the value (discord's `guild_id="guild_id"` beneath `pattern: ^(0|[1-9][0-9]*)$`).
- **crozier writes:** The specification's own declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else a value constructed deterministically to satisfy every in-scope keyword. Where no such value exists or crozier cannot decide validity, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-name-example.md`](../../docs/departures/evidence/schema-rejected-name-example.md)

### `schema-rejected-number-example`

- **Kind:** `fern-defect`
- **Trigger:** An integer or number parameter or property, in a worked example of `README.md`, `reference.md` or a generated client's docstring, whose schema rejects Fern's fixed placeholder (`1`, `1000000` or `1.1`) by an `enum`, `const`, `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf` or the `int32` or `int64` range. The comparison has the parsed source document.
- **Fern writes:** The fixed placeholder as the value (discord's `trigger_type=1` beneath `enum: [4]`).
- **crozier writes:** The specification's own declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else a value constructed deterministically to satisfy every in-scope keyword. Where no such value exists or crozier cannot decide validity, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-number-example.md`](../../docs/departures/evidence/schema-rejected-number-example.md)

### `schema-rejected-placeholder-string-example`

- **Kind:** `fern-defect`
- **Trigger:** A string in a worked example of `README.md`, `reference.md` or a generated client's docstring that Fern writes as its fixed `"string"` or `"value"` placeholder, whose schema rejects that placeholder by an in-scope keyword or format. The comparison has the parsed source document.
- **Fern writes:** The fixed placeholder `"string"` or `"value"` as the value.
- **crozier writes:** The specification's own declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else a value constructed deterministically to satisfy every in-scope keyword. Where no such value exists or crozier cannot decide validity, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-placeholder-string-example.md`](../../docs/departures/evidence/schema-rejected-placeholder-string-example.md)

### `schema-rejected-sized-string-example`

- **Kind:** `fern-defect`
- **Trigger:** A string in a worked example of `README.md`, `reference.md` or a generated client's docstring that Fern's fallback example writer sizes by the declared `minLength` or `maxLength` alone (`"apricot"` for seven), whose schema rejects that sample by another in-scope keyword or format. The comparison has the parsed source document.
- **Fern writes:** The sized sample word as the value.
- **crozier writes:** The specification's own declared example for that schema when the schema accepts it, else its declared `default` when the schema accepts it, else a value constructed deterministically to satisfy every in-scope keyword. Where no such value exists or crozier cannot decide validity, Fern's value stays. The argument, its place and every other line are unchanged.
- **Why:** An example value invalid for its own schema is a defect under the defect rule: the API rejects the call the example shows. Validating Fern's value against its source schema rejects it; crozier's is accepted.
- **Evidence:** [`docs/departures/evidence/schema-rejected-sized-string-example.md`](../../docs/departures/evidence/schema-rejected-sized-string-example.md)

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

### `text-response-optional-query-examples`

- **Kind:** `richer-documentation`
- **Trigger:** An operation whose successful responses answer only text/* content, with an optional query parameter whose parameter or schema declares an example: the worked examples of README.md, reference.md and each client.py docstring.
- **Fern writes:** The call passing only the required arguments, since Fern builds no example from the document for a text/* success body.
- **crozier writes:** The same call also passing each such optional parameter's declared example (included_schemas="public,auth", pgdelta="true"), as it and Fern both do for a JSON success body.
- **Why:** Both calls bind; crozier's documents the values the specification declares for the operation's optional parameters, each valid for its schema, where Fern's drops them only because the success body is text.
- **Evidence:** [`docs/departures/evidence/text-response-optional-query-examples.md`](../../docs/departures/evidence/text-response-optional-query-examples.md)

### `typeless-body-required-arguments`

- **Kind:** `fern-defect`
- **Trigger:** A JSON operation whose body requires a typeless (`{}`) value — a whole `{}` body, or a required `{}` property of an inline object body — and so takes no importer example: the worked calls of README.md, reference.md and each client.py docstring.
- **Fern writes:** The bare call (`client.knowledge_state_post()`), although the generated method requires the body's arguments (`data: typing.Any`, `request: typing.Any`, `session_id: str`).
- **crozier writes:** The call passing exactly those required arguments, the typeless ones as `{"key": "value"}` and the rest their placeholders; the signature, imports and every other line remain matched.
- **Why:** Binding the documented call to the generated method raises TypeError for the missing required keyword arguments, so the example does not match the code; crozier's call binds, and passes a value each annotation admits.
- **Evidence:** [`docs/departures/evidence/typeless-body-required-arguments.md`](../../docs/departures/evidence/typeless-body-required-arguments.md)

### `unquoted-timestamp-parameter-example`

- **Kind:** `usefulness`
- **Trigger:** A worked example passing a parameter whose example (its own, its examples map's first value, or its referenced schema's example or first examples entry) is an ISO date or date-time the YAML document writes unquoted, which YAML reads as a timestamp.
- **Fern writes:** Its date-time placeholder (datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00")) or the parameter's name for a required parameter, and an optional parameter's declared example left out of the call.
- **crozier writes:** The declared timestamp, as the call's datetime (datetime.datetime.fromisoformat("2031-04-02T08:15:00+00:00")) or string ("2031-04-01T06:00:00Z"), including an optional parameter's, with the import datetime it needs. Every other argument and line is retained.
- **Why:** Design-review ruling 3 (yaml-timestamp-parameter-example, 2026-11-01) keeps the unquoted ISO timestamp the API's author declared rather than the certified pair's placeholder.
- **Evidence:** [`docs/departures/evidence/unquoted-timestamp-parameter-example.md`](../../docs/departures/evidence/unquoted-timestamp-parameter-example.md)

### `wrapped-union-member-docs-example`

- **Kind:** `fern-defect`
- **Trigger:** A discriminated union whose mapping names a oneOf or anyOf of references with no discriminator of its own, which the wrapper holds whole in value: the worked examples of README.md and reference.md.
- **Fern writes:** The wrapper constructed with an empty argument under the mapping value as keyword (SurveyEntry_Level(level=,)).
- **crozier writes:** The constructor its own client.py docstrings write, passing the union's example as value (SurveyEntry_Level(value=1.1)).
- **Why:** Fern's example is not Python: the argument has no value, and the keyword is not a field of the constructor, which rejects it. Its own docstrings construct the same request through value.
- **Evidence:** [`docs/departures/evidence/wrapped-union-member-docs-example.md`](../../docs/departures/evidence/wrapped-union-member-docs-example.md)

<!-- END GENERATED CATALOG -->
