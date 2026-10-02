# duplicate-example-name: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. Its [wire journey](evaluation-logs/probe.wire.log)
sends both declared example bodies, `{"id": "a"}` and `{"id": "b"}`, to
`POST /probe` under the declared wire name, and parses the empty 204 as
`None`. Example names never reach the SDK: `reference.md` and the docstring
show only the first example. On the probe alone the output is valid and useful.

Representatives come from the three publishers in the population:

- [Adyen's CheckoutService v46,
  `0109022564565a67857d84bd61ba8dd618ab71c09474786ed5e51d60c37168ab`](evaluation-logs/adyen.log),
  imports with **zero mypy errors** over 332 files. Its `POST /paypal/updateOrder`
  200 response has two examples summarised "Order updated with delivery
  methods in an Advanced flow integration". The
  [wire log](evaluation-logs/adyen.wire.log) sends `pspReference`,
  `paymentData` and `amount` as declared and parses `PaypalUpdateOrderResponse`.
- [hootrhino's rhilex REST API,
  `9791479038e38468cdac23b741406f63d08cf384b0df70c35fa8fa644643f341`](evaluation-logs/rhilex.log),
  whose `GET /api/v1/menu/distConfig` responses repeat the summary `成功示例`,
  gets **no SDK** from the baseline. `ruff` cannot parse the generated
  `src/fern/raw_client.py` (line 42, "Expected an identifier"), so crozier exits 1.
- GitHub's REST descriptions (48 documents, plus Jentic's copies) reach the
  class through `POST /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses`.
  Thirty-one of them already carry the registered `object-extends-non-object`
  refusal. The baseline writes about 7,200 files for the others. They were
  not typed, because rhilex already settles the verdict.

The class is `refuse` in both modes. Under the brief, a population document
the baseline cannot generate counts against `generate`. That failure is not
caused by the duplicate names (see the follow-up in the agent report), but it
disqualifies the class. No generated SDK changes.

## What pinned Fern names and compares

Every case below was run through pinned `fern check`; each refused shape is a
`*-probe.yml` and each accepted near miss a `*-control.yml`, with its log in
[`evaluation-logs/`](evaluation-logs/).

- **Within one example map only.** Fern compares the request examples among
  themselves, and the success response's examples among themselves. A request
  and a response sharing a summary are accepted
  ([control](req-resp-summary-control.yml)), and so are two operations sharing
  one ([control](across-operations-control.yml)).
- **The name** is the Example Object's `summary` when present and non-null,
  otherwise its map key. An empty summary counts
  ([probe](empty-summaries-probe.yml)), and a summary can collide with another
  example's key ([probe](summary-equals-key-probe.yml)). A `null` summary
  falls back to the key ([control](request-null-summary-control.yml)). Values
  compare with their YAML type: `1` and `1` collide
  ([probe](numeric-summaries-probe.yml)) but `1` and `"1"` do not
  ([control](number-vs-string-summary-control.yml)). Comparison is
  case- and whitespace-exact ([different case](different-case-control.yml),
  [trailing space](trailing-space-control.yml)). A `$ref` example takes its
  target's summary ([probe](referenced-summary-probe.yml)) and ignores a
  sibling `summary` ([probe](ref-summary-override-probe.yml)). Without one it
  takes its own key ([control](ref-no-summary-same-target-control.yml)).
  `x-fern-ignore` on an Example Object is not honoured
  ([probe](ignored-example-probe.yml)).
- **Request media.** Fern reads the first media type in document order whose
  key contains `json` (case-sensitive) or is `*/*`
  ([probe](req-vnd-dupe-then-json-probe.yml),
  [control](second-json-media-type-control.yml)). It falls back to an
  `application/x-www-form-urlencoded` body
  ([probe](form-request-dupe-probe.yml),
  [control](req-json-then-form-dupe-control.yml)). Multipart and XML examples
  are never read ([multipart](multipart-request-dupe-control.yml),
  [XML](req-xml-dupe-only-control.yml)). Component request bodies and
  responses are followed ([request](component-request-body-probe.yml),
  [response](component-response-probe.yml)). Unused components are not read
  ([control](unused-component-response-control.yml)).
- **Response.** Fern reads the lowest numeric 2xx code, regardless of document
  order ([probe](first-2xx-dupe-201-202-probe.yml),
  [control](second-2xx-dupe-control.yml)). A response with no content
  ([probe](resp-200-nocontent-201-dupe-probe.yml)) or only `application/xml`
  ([probe](resp-200-xml-201-dupe-probe.yml)) passes the search to the next
  code. A `204` ends it ([control](resp-204-206-dupe-control.yml)), and so
  does text or HTML content ([control](resp-200-html-201-dupe-control.yml)).
  `default` is read only when no numeric 2xx is declared
  ([probe](default-response-dupe-probe.yml),
  [probe](resp-400-and-default-dupe-probe.yml),
  [control](resp-201-nocontent-default-dupe-control.yml)). A `2XX` range
  ([control](resp-2XX-dupe-control.yml)) and error responses
  ([control](error-response-dupe-control.yml)) are never read.
- **`x-fern-examples`.** A non-empty list replaces the OpenAPI examples:
  duplicates there are accepted ([control](x-fern-examples-plus-openapi-dupe-control.yml)),
  while two equal `name`s are refused ([probe](x-fern-examples-dupe-probe.yml)).
  Unnamed entries never collide ([control](x-fern-examples-unnamed-control.yml)).
  An empty list leaves the OpenAPI examples in force
  ([probe](x-fern-examples-empty-list-probe.yml)).
- **Not read.** Parameter examples
  ([control](parameter-examples-dupe-control.yml)), webhooks
  ([control](webhook-dupe-control.yml)), ignored operations and Path Items
  ([operation](ignored-operation-control.yml), [Path Item](ignored-path-item-control.yml))
  are not read. Per the planner's ruling, neither is `x-crozier-examples`:
  pinned Fern accepts duplicate names there
  ([control](x-crozier-examples-dupe-control.yml)).

The detector applies exactly these rules. Where a shape was not measured, it
does not refuse: other media types end the response search, and an
unresolvable reference skips the example. Every accepted control generates
identical bytes in both crozier modes.

The [CLI assertion failed with only the predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 36 files. It passed again once the predicate was restored. Making the
second summary distinct recovers generation in both modes.

[All 109 population documents](evaluation-logs/population-refusals.jsonl)
were retrieved at their digests and run with the finished detector's release
build. All were refused in both modes: exit 1, no files, and one stderr line
naming the class and element, plus the strict cause where it applies. 78
were refused as this class. The other 31 GitHub descriptions hit the
registered `object-extends-non-object` refusal first.
