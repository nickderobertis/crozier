# Refusal parity: ten documents the certified pair generates from

A search for `discriminator-mapping` witnesses ran the certified pair (Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3) over ten public documents that
crozier refused or failed on, and the pair exited 0 on all ten. This record gives each its root
cause, the crozier code each repair changed, and its outcome. A document is
*excepted* when its root cause is a defect the certified pair shares, or a
refusal crozier keeps for the user to rule on; crozier's output or refusal for
an excepted document's shape is unchanged.

| document (sha256) | root cause | outcome |
|---|---|---|
| APIs.guru `APIs/digitalocean.com/2.0/openapi.yaml` (`5bd3a480…`) | A | excepted: refused by both |
| `dltkddnr04/propresenter-remote` `openapi/propresenter.openapi.json` at `b273aeec98db` (`44695afa…`) | A | excepted: refused by both |
| `jeffmikels/ProPresenter-API` `pro7.9.openapi-spec.json` at `6e7490671c94` (`694f7ec9…`) | A | excepted: refused by both |
| OpenAPI Generator `samples/client/petstore/csharp/generichost/net10/AllOf/api/openapi.yaml` at `10e6c21c97ab` (`cc2fa0a1…`) | B | owned by `refusal-parity-discriminant-names` |
| `Carapacik/swagger_parser` `swagger_parser/test/schemas/null-types-with-type-array.yaml` at `1fec2df2fd07` (`55071fd9…`) | B | owned by `refusal-parity-discriminant-names` |
| `ToolJet/ToolJet` `marketplace/plugins/microsoft_graph/openapi-specs/teams.yaml` at `63c2b08614b7` (`09ac0c7b…`) | B | owned by `refusal-parity-discriminant-names` |
| `RS-PYTHON/rs-server` `services/frontend/resources/openapi.json` at `83ebcafb173c` (`a8771072…`) | C | owned by `refusal-parity-example-collision` |
| `ingef/conquery` `openapi.yaml` at `0379408a4b68` (`c3a52b3c…`) | D | owned by `refusal-parity-lenient-yaml` |
| `outstack/enveloper` `docs/api/openapi.yaml` at `cd8150d6d78c` (`95595ff6…`) | E | excepted: a departure candidate for the user |
| OpenAPI Generator `modules/openapi-generator/src/test/resources/3_1/cpp-boost-beast-client/composed-schema-lowering.yaml` at `10e6c21c97ab` (`981444e6…`) | F | repaired; registered as corpus row 3476 |

The draft's full digests, and the Fern log of each run, are those of the
`discriminator-mapping` arm probe
(`docs/openapi-surface/witness-search-unproven-features/discriminator-mapping-fern.tsv`,
rows with `fern_exit` 0).

## A: a `$ref` into another path's definition

crozier refuses each with `unresolved-reference`, naming the pointer:
DigitalOcean's `#/paths/~1v2~11-clicks/get/responses/200/headers/ratelimit-limit`,
propresenter-remote's `#/paths/~1v1~1looks/get/parameters/0`, and pro7.9's
`#/paths/~1version/get/responses/404`. The certified pair exits 0 on all three,
but it never parses them. Each log reads `Failed to parse openapi document`
(`DigitalOcean API`, `ProPresenter API` twice) and then `CliError: Failed to resolve`
on the pointers `#/paths/~1v2~11-clicks/get/responses/401`,
`#/paths/~1v1~1looks/get/parameters/0` and `#/paths/~1version/get/responses/404`.
What it writes is the 35-file empty SDK: no endpoint and no type. This is the
exit-0 failure in which Fern parses nothing, which
[`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md#specs-already-tried-and-rejected-do-not-re-attempt-without-a-fix-upstream)
already logs for `digitalocean-jentic` and `opensuse-obs`.

The certified pair was re-run on each exact document, keeping its tree:
DigitalOcean (sha256 `5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63`),
propresenter-remote (`44695afa34c9d6e1fce938a62844cf07b30ed296a5e3d2be1779827947394219`)
and pro7.9 (`694f7ec93b5aafa776ab61f7e049432f2ac01f8db5ffce4aedbde9f1a38616cc`).
The documents declare 290, 231 and 129 operations. Each run logs the same failure
again and writes 35 files, and the three trees are byte-identical, so nothing in
any of the documents reaches the output. Outside `src/fern/core/`, the trees hold
`README.md`, `CONTRIBUTING.md`, `reference.md`, `pyproject.toml`,
`requirements.txt`, `.fern/metadata.json`, the package's `__init__.py`,
`_default_clients.py`, `client.py`, `py.typed`, `version.py` and two test files.
`client.py` declares `FernApi` and `AsyncFernApi` with `__init__` as their only
method. `__init__.py` exports those two, the default HTTP clients and
`__version__`. There is no resource package and no `types/` module, and
`reference.md` is the bare `# Reference` heading. The SDK therefore omits every operation
the documents declare.

By the planner's ruling, A is a Fern refusal, not output to match. A scenario Fern refuses is
refused in both modes, so crozier's refusal stays as it is. No crozier code
changed for A. Run on each exact document, crozier built at this work's base
(`2a298364e`) and on the finished tree prints the same `unresolved-reference`
refusal and exits 1. That holds by default, with `--enum-type literals` and with
`--fern-strict`.

## E: a `$ref` to a file that does not exist

crozier refuses enveloper because `./build/endpoints/outbox/preview/post.requestBody.schema.openapi`
cannot be read. The document names nine relative files under `./build/`, which its
repository does not carry at the revision: two of them, read raw at
`cd8150d6d78c`, answer 404 where the document itself answers 200. The certified pair exits 0 and
writes 44 files. Measured on the exact document, it reads every missing
reference as `typing.Any`, so it writes no `types/` module at all. Its one
`messages` client has four operations:

- `preview_message(*, request: typing.Any) -> typing.Any` for `POST /outbox/preview`,
  whose request and response bodies are both missing files;
- `send_message(*, request: typing.Any) -> None` for `POST /outbox`, whose request
  body is a missing file;
- `list_sent_messages() -> typing.Any` for `GET /outbox`;
- `get_sent_message_by_id(id: str) -> typing.Any` for `GET /outbox/{id}`.

Its error classes, `BadRequestError`, `NotFoundError`, `NotAcceptableError` and
`InternalServerError`, each take `body: typing.Any`. The two
`components.schemas` entries that are references to missing files
(`syntax-error`, `failed-json-schema-validation`) declare nothing. Fern's SDK
therefore drops every type the document means to declare, and gives no
diagnostic. crozier's refusal names the file. By the manager's ruling this goes
to the user as a departure candidate, and crozier's refusal is unchanged until
they rule. On the exact document, crozier at the base (`2a298364e`) and on
the finished tree prints the same refusal in both enum modes.

## F: unions of only `null`, and of one string enum

crozier generated composed-schema-lowering, but `ruff format` rejected its
`types/all_null_test.py`, `AllNullTest = typing.Union[]`, which comes from
`anyOf: [{type: "null"}, {type: "null"}]`. Repairing that exposed two more
residuals in the document, and a nested form of the first:

- **All-`null` alternatives.** Fern reads such a union as the `type: null` it
  amounts to, which is `Optional[Any]`, as a component, a property and an array
  item, nested ones included. `normalize_null_only_compositions` and
  `fold_null_only` in `src/openapi.rs` fold it so before any other pass sees it.
  `simple_nullable_member` in `src/ir.rs` no longer indexes an empty member list
  (`then_some(non_null[0])` was evaluated eagerly, and it panicked).
- **One string-enum alternative.** Fern declares the enum itself under the
  owner's name, with the alternative's own description and not the owner's, so
  `SingleBranchTest` is an `enum.StrEnum`. crozier declared a
  `SingleBranchTestZero` behind an alias. `lone_inline_string_enum` in
  `src/ir.rs` is read by `Builder::add_named` for a component, by
  `Builder::field_type_ref` for a component's property and by
  `InlineHoister::prop_type_ref` for a hoisted model's.
- **A union example after a `str`-admitting alias.** `ModelIdsResponses`,
  `Union[ModelIdsShared, ModelIdsResponsesOne]` with `ModelIdsShared =
  Union[str, ModelIdsSharedOne]`, is exampled `request="ids"` by Fern, where
  crozier wrote `ModelIdsResponsesOne.IDS`. `ExampleCtx::union_value` in
  `src/emit.rs` now asks `names_bare_str` whether an earlier alternative names
  a bare `str` itself or through a union or an alias.

The hand-written fixture
[`dormant-sensor-unions`](openapi-surface/handwritten/dormant-sensor-unions/)
declares each shape in both spellings, and crozier byte-matches its
certified-pair tree. The witness search over the documents on the host, and the
witnesses it left unregistered, are in
[`witness-search-null-and-lone-enum-alternatives`](openapi-surface/witness-search-null-and-lone-enum-alternatives/README.md).

**Comparison on the exact document.** crozier run on composed-schema-lowering
(sha256 `981444e6ec1bee5347b267610c0b2b98f884c01c0a9b771255231f84214e3da8`)
byte-matches the certified pair's 86-file output, apart from the lines the
departures ledger records under `sdk-identity-header-prefix` and
`stream-reference-return-type`. The document is the committed source of
corpus row 3476, `openapi-generator-composed-schema-lowering`, whose complete
golden and `expected-literals` overlay `openapi_generator_composed_schema_lowering_matches_fern_output`
holds crozier to. Its Python passes the pinned `ruff format`, which every
generation runs.

## Derived records

Each derived record the branch commits was generated over the `src/` of
`be0ba0f1c`, the branch's last merge of main (`src/` there is the branch's
final source; that merge brought no `src/` change):

- `docs/openapi-surface/golden-reach.tsv` and the golden rows' reach cells,
  with the census JSON they join: `just golden-reach` over 274 golden tests.
  The reach ranking in `docs/openapi-surface-coverage.md` is restated from
  that ledger, and `golden-reach-witnesses/outstanding.tsv` is
  `golden-reach-search.py outstanding` over the same tree.
- `docs/openapi-surface/handwritten-reach.tsv`: `just handwritten-reach`,
  which left it unchanged.
- The arm counts and arm table in `docs/openapi-surface-coverage.md`:
  `just golden-reach-arms`, which left them unchanged.
- `tests/fixtures/departures-ledger.tsv` and
  `docs/departures/evidence/invalid-example-values/inventory.tsv`:
  `just departures-ledger`, which left both unchanged and
  passed every golden comparison it ran.

## Found on the way

The witness search ran crozier over OpenAPI Generator's
`3_0_3_unit_test_spec.yaml`. Beyond the nested all-`null` union (repaired
above), it fails at `ruff format` on `properties_with_escaped_characters.py`,
where a property name holding escaped characters becomes an unterminated
string literal. A union of a single-member `anyOf: [null]` beside a
`oneOf` of two `null`s is measured too: Fern hoists the `oneOf` as
`…One = Optional[Any]` and drops the component itself, where crozier now
declares the component `Optional[Any]`. Both are recorded as follow-ups, not
repaired here.
