# Refusal parity: an error response naming an undeclared component response

A `response-status-space-suffixed` witness search reported that the certified
pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) generates from a
document crozier refuses. That finding was wrong. The pair exits 0 on the
document but parses none of it. This record gives the root cause, the crozier
code the work changed, and the document's outcome.

| document (sha256) | root cause | outcome |
|---|---|---|
| `jentic/jentic-public-apis` `apis/openapi/setu.co/main/1.0.0/openapi.json` at `eb9d12a2684b` (`d2dc23e9…`) | Fern parses nothing and writes its empty SDK | excepted: refused by both |

The full digest is
`d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414`, and the
revision is `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743`. The repository
redistributes the document as a CC0 aggregation.

## Root cause

The document's `POST /users/login` declares `400` as
`{"$ref": "#/components/responses/BAD_REQUEST"}`. The document has no
`components.responses` at all, and this is its only `components/responses`
reference. crozier refuses it with
`unresolved-reference: paths//users/login/post/responses/400: #/components/responses/BAD_REQUEST`.

The certified pair, run on the exact document
([log](fern-refusals/unresolved-reference/evaluation-logs/fern-setu-document.log)),
reads `Failed to parse openapi document API Setu` and then
`CliError: Failed to resolve #/components/responses/BAD_REQUEST` out of
`resolveResponseReference`, and exits 0. It writes the 35-file empty SDK:
`client.py` declares `FernApi` and `AsyncFernApi` with `__init__` as their only
method. There is no resource package and no `types/` module, and `reference.md`
is the bare `# Reference` heading. Outside `src/fern/core/`, the tree holds the
same 13 files that [class A](refusal-parity-ten-documents.md#a-a-ref-into-another-paths-definition)
lists. The document declares 157 operations over 150 paths and 1,083 schemas,
and none of them reaches Fern's output.

The same failure happens on a from-scratch shape. A non-success response that
names an undeclared `components/responses` entry
([probe](fern-refusals/unresolved-reference/undeclared-error-response-probe.yml))
gets the same parse failure and the same 35 files. Declaring that response
([control](fern-refusals/unresolved-reference/undeclared-error-response-control.yml))
generates 40 files. Both runs are recorded in
[`shapes.tsv`](openapi-surface/fern-refusals/shapes.tsv).

## Ruling

This is the "exit 0, parsed nothing" failure that class A of
[`refusal-parity-ten-documents.md`](refusal-parity-ten-documents.md) records.
The planner ruled that class A is a Fern refusal, not output to match. The
manager applied that ruling to this document, and the user has not yet
confirmed it. If the user reverses class A, this document follows that
decision. Matching the pair would mean emitting an SDK with no endpoints from a
157-operation document. crozier's refusal names the dangling pointer, which is
more useful.

## Outcome

- **crozier code changed:** none in `src/`. crozier's refusal of this shape
  stays as it was. The real-binary journey
  `undeclared_error_response_component_is_refused_until_declared`
  (`crates/crozier-e2e/tests/e2e.rs`) refuses the probe by default, with
  `--enum-type literals` and with `--fern-strict`. In the same three modes it
  generates the control, and also the probe with the response inlined.
- **The exact document on the finished tree:** crozier exits 1 and writes
  nothing, by default, with `--enum-type literals` and with `--fern-strict`. It
  prints the `unresolved-reference` diagnostic above, and under `--fern-strict`
  adds `(fern-strict refusal)`. No SDK is written, so there are no files to
  compare. This is the same as crozier at this work's base (`1748b7946`),
  because `src/` is unchanged.
- **Corpus registration:** not registered. The corpus admits a document only
  if Fern accepts it ([`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md#choosing-a-real-world-spec--fern-must-accept-it-first)),
  and the pair never parsed this one. Its golden would be the empty SDK, which
  shows none of the document's features.
