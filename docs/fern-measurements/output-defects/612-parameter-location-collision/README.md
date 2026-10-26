# Parameters in different locations that share a name

Issue [#612](https://github.com/nickderobertis/crozier/issues/612).
[`openapi.yml`](openapi.yml) was authored from scratch. Every operation
carries two headers, `branch` and `Page-Size`, so both are lifted to the
client. Beside them:

- `getShelf` has a path `shelf` and a query `shelf`, and a path `branch`
  beside the lifted `branch` header;
- `listEditionScans` has a path `edition` and a header `edition` on that
  operation alone;
- `listLoans` has a query `page_size`, which normalizes to the lifted
  `Page-Size` header's name, and a query `patron` beside a cookie `patron`.

`fern-expected/` is the complete, comment-stripped tree Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3 generated from it, through
`just fern-references measurements
output-defects/612-parameter-location-collision` (a
[`../../cases.tsv`](../../cases.tsv) row). Nothing in it was edited.

## Comparison

`fern check` exits 1, reporting each pair as `Parameters … all normalize to …`,
a check-only finding
([`parameter-normalization-collision`](../../../fern-refusals/findings.tsv)).
`fern generate` still exits 0 and writes this tree:

- A path parameter whose wire name a query parameter or header also carries
  becomes `{name}_path_param`: `shelf_path_param`, `edition_path_param` and
  `branch_path_param`. The last is renamed even though its header is lifted
  to the client. The query `shelf` and the header `edition` keep their names.
- The cookie `patron` is dropped, as Fern drops every cookie parameter.
- The client takes `branch` and `page_size` and sends them as the `branch` and
  `Page-Size` headers. The method's own `page_size` is sent as the query
  parameter.

crozier refused the document
(`request-property-camelcase-collision: GET /branches/{branch}/shelves/{shelf}
parameters "shelf" and "shelf" in different locations`).

## Verdict: parity gap, repaired

Fern's output is callable, and it keeps every parameter's wire name.
[`runtime.txt`](runtime.txt) calls each method with every colliding parameter
against a local HTTP server, sync and async, and asserts each one's path
segment, query key or header name in the request received. A valid document
Fern generates from is not refused, so crozier now generates it and
byte-matches this tree apart from the catalogued `sdk-identity-header-prefix`
lines:

- `name_refusals::generated_location_pair` admits a cookie pair, and a path
  parameter that declares no name of its own beside a query parameter or
  header of the same wire name;
- the normalized-name check skips a lifted header;
- `ir::rename_claimed_path_params` lets a lifted header claim its name.

Fern's refusals were measured at the same pair, and crozier still refuses
them:

- `shelf_id` beside `shelfId` (`Multiple request properties resolve to the
  same generated name shelfId after camelCase normalization`);
- a `page-size` header beside a `page_size` query when the header rides only
  one of two operations, so it is not lifted (the same diagnostic);
- a query `name` beside a header `name` that is not lifted (`Multiple request
  properties have the name name`, the
  [`request-property-camelcase-collision`](../../../fern-refusals/request-property-camelcase-collision/evaluation.md)
  class's `query-header-subset` probe).

The shapes are held by:

- `output_defect_measurements_match_fern` in
  [`crates/crozier-e2e/tests/e2e.rs`](../../../../crates/crozier-e2e/tests/e2e.rs);
- `sdk_env_output_defect_sdks_parse_and_send_what_fern_does`;
- the unit tests
  `parameters_fern_generates_past_in_different_locations_are_not_refused`
  (`src/name_refusals.rs`) and
  `path_parameters_a_query_or_header_names_take_the_path_param_suffix`
  (`src/ir.rs`).

No registered corpus, hand-written or measurement document other than this
one carries these shapes, so the repair moves no golden.
