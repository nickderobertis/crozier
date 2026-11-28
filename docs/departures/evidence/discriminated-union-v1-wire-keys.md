# A discriminated union tagged by an aliased wire key fails to parse under Pydantic v1

The from-scratch document
[`aliased-union-discriminator/openapi.yml`](../../fern-measurements/naming-acceptance/aliased-union-discriminator/openapi.yml)
declares `QueryResponse`, a `oneOf` of `TableResult` and `GraphResult`
discriminated by the property `schema`, as `GET /queries/{id}`'s response. Fern
CLI 5.216.0 with `fernapi/fern-python-sdk` 5.42.0 generated its complete tree in
both enum modes
([`fern-expected/`](../../fern-measurements/naming-acceptance/aliased-union-discriminator/fern-expected),
packaged, organization/package `fern`, project `default_package_name`, through
`just fern-references measurements naming-acceptance/aliased-union-discriminator`).

The pair names the tag field `schema_` (wire alias `schema`) on
`QueryResponse_Table` and `QueryResponse_Graph`. Its `core/pydantic_utilities.py`
`parse_obj_as`, through which every generated client parses a response,
dealiases every input that is not a model class with
`convert_and_respect_annotation_metadata(..., direction="read")` before
validating it, so the payload `{"schema": "table", "rowCount": 3}` reaches
Pydantic as `{"schema_": "table", "row_count": 3}`. Pydantic v1 looks a
discriminated union's tag up under the tag field's alias only, so it rejects the
dealiased payload, while validating the received one directly succeeds. The
generated `pyproject.toml` admits `pydantic >= 1.9.2`, so this is a valid
response the SDK cannot parse: a defect under the defect rule's runtime clause,
shown by the run below.

(The pair's union also declares `discriminator="schema"`, the wire key rather
than the field, which Pydantic refuses at import under both majors: `Model
'QueryResponse_Table' needs a discriminator field for key 'schema'`. crozier
writes `discriminator="schema_"`, the
[`escaped-discriminator-field-name`](escaped-discriminator-field-name.md)
departure; the run below is of the runtime that SDK then parses through.)

crozier's `core/pydantic_utilities.py` is the certified one with one change, in
one region: a `_has_discriminated_union` helper defined just before
`parse_obj_as`, and, under Pydantic v1 only, an input whose type holds a
discriminated union outside any model (the union itself, or a list, map or
optional of one) validated as received. A model's input already is where the
model declares Pydantic aliases, and Pydantic v2's path is unchanged. The rule
`discriminated_union_v1_wire_keys` in `src/departures.rs` accepts exactly that
region, so a golden's only row for it is the helper's first line.

## The run

`crates/crozier-e2e/tests/e2e/naming_acceptance_runtime.py aliased-discriminator`
serves both payloads over real HTTP and calls `get_query` through the SDK's async
client, under `uv run --no-project --python 3.11 --with pydantic==<v> --with
httpx==0.28.1 --with typing_extensions==4.16.0`. With the certified runtime
(crozier's SDK before this departure, its `pydantic_utilities.py` byte-identical
to the pair's), Pydantic 1.10.26:

```text
pydantic.error_wrappers.ValidationError: 1 validation error for ParsingModel[Annotated[Union[fern.types.query_response.QueryResponse_Table, fern.types.query_response.QueryResponse_Graph], FieldInfo(default=PydanticUndefined, discriminator='schema_', extra={})]]
__root__
  Discriminator 'schema_' is missing in value (type=value_error.discriminated_union.missing_discriminator; discriminator_key=schema_)
```

while `pydantic.parse_obj_as(QueryResponse, {"schema": "table", "rowCount": 3})`
in the same environment returns `QueryResponse_Table`, and Pydantic 2.14.1
parses both payloads through the SDK. With crozier's runtime the journey prints
`aliased-discriminator: ok` under both majors, in both enum modes:
`sdk_env_aliased_discriminated_unions_parse_under_both_pydantic_majors` in
`crates/crozier-e2e/tests/e2e/naming_acceptance.rs` (run by `just test-sdk-env`).
