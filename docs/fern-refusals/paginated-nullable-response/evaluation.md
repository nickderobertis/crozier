# paginated-nullable-response: refuse

Evaluated on starting commit `c14284cdffff6a3190934b97e35acf0552cd5dac`.

The [probe](probe.yml) declares cursor pagination (`x-fern-pagination`:
`cursor: $request.after`, `next_cursor: $response.next`, `results:
$response.jobs`) on an operation whose `200` response `$ref`s `JobPage`, an
object component declared `nullable: true`. Fern CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0 passes `fern check` and fails generation:
"Response must be an object in order to return property next as a response."
([record](fern-refusal.txt)).

The offset form is the same class: with the probe's contract rewritten to
`offset: $request.page`, `results: $response.jobs` (and an integer `page`
query parameter in place of `after`), the same pair's `fern generate` passes
its validation ("All checks passed") and the generator fails, exit 1, with the
class's diagnostic: "Response must be an object in order to return property
jobs as a response." Reading no next cursor, the
offset contract's element names the items property it reads.

The class is `refuse` in both modes because the document contradicts itself:
the pagination extension reads each page's next cursor and items off the
response, while the response is declared to be possibly `null`, which carries
neither. A generated pager has no page to read from a `null` response, and
generating the method without its pager would silently drop the contract the
document declares, so crozier generates neither. This is a fault in the
specification, not a Fern limitation, so no default generation is evaluated.

crozier refuses the probe with exit 1 and nothing written, by default and under
`--fern-strict` ([log](evaluation-logs/paginated-nullable-response.log)),
naming the operation, the response property the contract reads and the nullable
component, for the cursor form and the offset form alike. A response
component without `nullable` generates its pager
(`paginated_nullable_response_refuses_in_both_modes_beside_a_generating_control`
in `crates/crozier-e2e/tests/e2e.rs`).

No document of the refused population carries the class (`documents` 0).
