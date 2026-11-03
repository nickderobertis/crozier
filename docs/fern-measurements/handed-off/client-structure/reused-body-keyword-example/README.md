# `R12` residual: a query clash on a reused body (`repeated-query-body-example-keyword`)

The last difference of [`R12`](../R12/README.md)'s two handed-off documents
(`fern-api/docs:fern/apis/fai/openapi.json` at `e82e728` and `6f9d392`), measured
after `R12` itself and the merged union-modelling repairs cleared everything
else. It is not one of this area's root causes: it is the catalogued
`fern-defect` departure
[`repeated-query-body-example-keyword`](../../../../departures/evidence/repeated-query-body-example-keyword.md),
added by this node under the manager's ruling once this document reproduced it.

**Rule.** A required query parameter sharing its name with a property of its
operation's `$ref`'d JSON body, where that component is referenced somewhere
else too and so stays a named model: the certified pair's signature and
docstring rename the body argument `<model>_<name>`, but its `README.md` and
`reference.md` worked calls pass the query keyword twice. crozier passes the
renamed argument.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: `POST
/questions` with a required query `bench` and body `Question` (`bench`,
`asked_by`, `urgent`), which `GET /questions` lists again in
`OpenQuestions.questions`.

**How the trigger was pinned.** Seven from-scratch documents, each generated
alone by the certified pair under the host locks with the manager's approval:

| # | shape | certified pair's worked call |
|---|---|---|
| 1 | path `bench` beside a body property `bench` (body used once) | correct (`bench_path_param`) |
| 2 | query `bench` beside a property of `$ref` body `Planting` (used once) | correct (`planting_bench`) |
| 3 | 2, plus bearer auth and two named servers | correct |
| 4 | 3, with the body schema named `Query` | correct (`query_bench`) |
| 5 | 4 as OpenAPI 3.1, FastAPI-style titles, the colliding property not first | correct |
| 6 | 2's clash with the body schema also listed by a response (this document) | **`bench=` twice** in `README.md` and `reference.md` |
| 7 | 6's reuse with a path-parameter clash instead | correct (`bench_`) |

The deciding contrast came from FAI's own certified tree: its faulty
`create_query` body `Query` is also listed by `GetQueriesResponse.queries`, and
the certified pair writes `types/query.py` for it, while its other clash,
`create_feedback`'s path `domain` beside the once-used, inlined
`CreateFeedbackRequest`, comes out correct.

**Certified pair.** `fern-expected/` is the complete, comment-stripped tree Fern
CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 (`enum_type: python_enums`)
freshly generated from `openapi.yml` through
`tools/fern-goldens/fern-references.py`'s `generated_tree` pipeline. The enum
mode cannot change this result (the document declares no enum), so no
literals tree is committed.

**Behaviour.** [`runtime.txt`](runtime.txt) records the run: the certified
pair's `README.md` snippet fails to compile (`SyntaxError: keyword argument
repeated: bench`), as both FAI trees' `reference.md` snippets do for `domain`;
crozier's compiles and sends `POST …/questions?bench=bench` with body
`{"bench":"bench","asked_by":"asked_by"}`, each keyword passed once.

**Comparison on the finished tree.** crozier's output byte-matches
`fern-expected/` with `repeated-query-body-example-keyword` applied to
`README.md` (one region, lines 44–77, holding both the synchronous and the async
call) and `reference.md` line 73, and with the catalogued
`body-query-parameter-value` applied to `src/fern/questions/raw_client.py` line
101 (the certified pair sends the query variable as the body's `bench`, which
crozier sends from `question_bench`), held by
`a_query_clash_on_a_reused_body_keeps_the_renamed_keyword` in
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also requires a
crozier output renaming the keyword other than the signature does to fail in
both files. Both
FAI documents then byte-match their certified-pair trees under `crozier
compare` ([`../README.md`](../README.md)).
