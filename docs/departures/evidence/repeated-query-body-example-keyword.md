# `repeated-query-body-example-keyword`

**Kind:** `fern-defect`. When a required query parameter and a property of a
reused `$ref` JSON body share a name, Fern's signature renames the body
argument `<model>_<name>`, but its `README.md` and `reference.md` worked calls
pass the query parameter's keyword twice. It is the mechanism of
[`repeated-credential-example-keyword`](repeated-credential-example-keyword.md)
in a method call rather than the client constructor.

## The input

[`reused-body-keyword-example/openapi.yml`](../../fern-measurements/handed-off/client-structure/reused-body-keyword-example/openapi.yml),
authored from scratch: `POST /questions` takes a required query parameter
`bench` and a JSON body `$ref: '#/components/schemas/Question'`, whose required
properties are `bench` and `asked_by`; `GET /questions` returns
`OpenQuestions`, whose `questions` array items reference `Question` again.

The trigger is narrow, and seven from-scratch generations pinned it (the
measurement's [README](../../fern-measurements/handed-off/client-structure/reused-body-keyword-example/README.md)
lists them): the same clash with a body schema referenced only by that body
(which Fern inlines), with or without auth, named servers, a body schema named
`Query`, or OpenAPI 3.1 and FastAPI-style titles, writes the renamed keyword
correctly, and so does a path-parameter clash on the reused schema (Fern renames
the path argument `bench_` instead). Only the query clash on a body schema that
stays a named model repeats the keyword. Two real documents carry it: both
revisions of `fern-api/docs:fern/apis/fai/openapi.json` (`create_query`, a
query `domain` beside `Query.domain`, `Query` also listed by
`GetQueriesResponse.queries`).

## Fern's output

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 (`enum_type:
python_enums`), through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline under the shared Fern lock, exits 0; the
comment-stripped tree is the measurement's `fern-expected/`. Its
`src/fern/questions/client.py` declares `file_question(self, *, bench: str,
question_bench: str, asked_by: str, urgent=..., request_options=...)`, and the
docstring's example passes `question_bench="bench"`. But `README.md` (lines
42–46 and the async twin at 75–79) and `reference.md` (lines 71–75) write:

```python
client.questions.file_question(
    bench="bench",
    bench="bench",
    asked_by="asked_by",
)
```

## Why it is a defect

A call that repeats a keyword argument does not bind. Compiling the `README.md`
snippet under Python 3.12.14, recorded in the measurement's
[`runtime.txt`](../../fern-measurements/handed-off/client-structure/reused-body-keyword-example/runtime.txt):

```text
SyntaxError: keyword argument repeated: bench (line 7)
```

FAI's two certified trees fail the same way on their `reference.md`
`create_query` snippet: `SyntaxError: keyword argument repeated: domain`. The
example also never passes the signature's required `question_bench`. It
contradicts the generated method, a defect under the defect rule; the
signature, the docstring and the wire behaviour are Fern's and crozier matches
them.

## crozier's output

crozier writes the same trees but for those lines, which pass
`question_bench="bench"` as the signature declares. Its `README.md` snippet
compiles and runs, sending the query parameter and the body property each
once (`runtime.txt`, through `httpx.MockTransport`):

```text
POST https://desk.greenhouse.test/questions?bench=bench {"bench":"bench","asked_by":"asked_by"}
```

`crates/crozier-e2e/tests/e2e/client_structure.rs`'s
`a_query_clash_on_a_reused_body_keeps_the_renamed_keyword` generates the
measurement with the real binary and requires it to byte-match
`fern-expected/` with exactly the ledger's departures applied: this one over
`README.md` lines 44–77 (both calls) and `reference.md` line 73, and the
catalogued `body-query-parameter-value` in `raw_client.py`, where the
certified pair also sends the query variable as the body value. It then
rewrites crozier's `question_bench=` to a keyword the signature does not
declare and requires the comparison to fail in both files, and the unit test
`the_query_body_keyword_rule_takes_only_a_reused_body_s_renamed_keyword`
requires the rule to refuse a once-used body, a path-parameter clash, a missing
source document, a client docstring, another value or any other differing line.
