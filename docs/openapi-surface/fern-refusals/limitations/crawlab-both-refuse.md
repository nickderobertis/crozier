# Crawlab: both tools refuse, at different stages

The source digest is
`12d7d4949ad2a113e8cc75652359d010b21bc2d954512b711b04b16cb72b8666`.
Its immutable publisher locator is retained in the
[refused-document registry](../../../fern-refusals/documents.tsv).

At the certified pair, Fern's check succeeds and generation fails with
`generator-lint-failure`. Crozier refuses at its OpenAPI boundary with
`path-parameter-unreferenced`: `PUT /schedules` declares the required path
parameter `id`, but the path has no corresponding template slot.

The whole original document fails `openapi-spec-validator` first because an
operation lacks `responses`. To exercise the path error independently, a second
validation retained that original path, operation and parameter list and supplied
only a `204` response. It failed with:

```text
UnresolvableParameterError: Path parameter 'id' for 'put' operation in '/schedules' was not resolved
```

Both validations ran against the cached source with the scratch evaluation
environment's real `openapi-spec-validator`. The second input is a deliberate
reduction, not a claim about which error the original document reports first.

The [native reduction measurement](../reductions/e6224c963a9349f68d1210e1544d6b1100cbb1a399989cb54a7f9b2a19cec99b.log)
still has the derived verdict `over-broad`: Fern accepts its check and refuses
only during generation. The document-level `both-refuse` disposition preserves
that measurement and records why crozier's independent boundary refusal agrees
with the final outcome. It does not admit an unexplained refusal of a document
Fern generates successfully.
