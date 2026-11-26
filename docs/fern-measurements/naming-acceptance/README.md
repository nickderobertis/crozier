# Naming, imports and document acceptance

Each case below is a document authored from scratch for one ticket, and its
`fern-expected/` (with `expected-literals/fern-expected/`, the literals overlay)
is the complete, comment-stripped tree Fern CLI 5.216.0 with
`fernapi/fern-python-sdk` 5.42.0 generated from it, through `just
fern-references measurements naming-acceptance/<case>` (a
[`../cases.tsv`](../cases.tsv) row each) under the shared Fern generation lock.
Nothing in them was edited. A case whose document names a sibling file reaches
Fern with that file beside it.

`crates/crozier-e2e/tests/e2e/naming_acceptance.rs` generates every case with
the real binary in both enum modes and compares the whole tree through
`src/parity.rs`, the departures pinned in `tests/fixtures/departures-ledger.tsv`.
A repaired rule's characteristic bytes are then written back the way crozier
wrote them before, and the comparison must name the file; an accepted document
is one crozier refused, so its generating at all is the regression.

| case | ticket | what the certified pair does |
|---|---|---|
| `model-api-field-names` | [#536](https://github.com/nickderobertis/crozier/issues/536), [#923](https://github.com/nickderobertis/crozier/issues/923) | A model field named for a Pydantic v1 or v2 model API (`construct`, `copy`, `dict`, `from_orm`, `json`, `kwargs`, `parse_file`, `parse_obj`, `parse_raw`, `schema`, `schema_json`, `self`, `update_forward_refs`, `validate` and every public `model_*` name, 30 in all) gets a `_` suffix and its wire alias; `fields`, `Config`, `args`, `cls`, `type`, `id`, `str`, `validator` and the rest keep their spelling. An inline body's `self` and `kwargs` arguments are `self_` and `kwargs_`, sent as `"self"` and `"kwargs"`; every other body name keeps its spelling. |
| `request-local-union-payloads` | [#919](https://github.com/nickderobertis/crozier/issues/919) | The payload models of a union coined for one operation's request-local property (`UpdateDataLiteInputInputOptionsCsv`, `…Parquet`) sit beside the union in `column_operations/types/`. |
| `root-import-order` | [#920](https://github.com/nickderobertis/crozier/issues/920) | The root `__init__.py`'s `TYPE_CHECKING` block writes `.types`, `.errors` and the `from . import` of the tag packages, then every other statement sorted by module: `._default_clients`, `.agent_runtime`, `.client`, `.environment`, `.version`, `.versions`, `.zones`. |
| `head-shadowed-get-imports` | [#921](https://github.com/nickderobertis/crozier/issues/921) | Where a `HEAD` operation shares a `GET`'s operationId, the high-level client's `HEAD` method returns the headers and imports no response model; `GetSiteResponse` stays a type. |
| `recursive-alias-dependents` | [#922](https://github.com/nickderobertis/crozier/issues/922) | `FitSummary`, which reaches the `JsonObjectOutput`/`JsonValueOutput`/`JsonArrayOutput` alias cycle only through `InferenceReport`, gets `from __future__ import annotations` and a bare `update_forward_refs(FitSummary)`. A single self-recursive alias reached that way gets none (corpus `ramu-shogi`, `supabase-api-v1`). |
| `dotted-operation-tag-names` | [#924](https://github.com/nickderobertis/crozier/issues/924) | `agent.host.pairing.create`, `agent.host.list` and `agent.host.harnesses.list` under the tag `agent_host` are `pairing_create`, `list` and `harnesses_list`; the tags `Agent Surfaces (Me)` and `Agent Surfaces (Ingress)` are the modules `agent_surfaces_me` and `agent_surfaces_ingress`. |
| `relative-response-ref` | [#942](https://github.com/nickderobertis/crozier/issues/942) | A `404` that is `./components.yml#/components/responses/NotFound`, whose schema points at that file's own `Problem`, which points at its `Detail`, types `NotFoundError`'s body `Problem`, with `Problem` and `Detail` models. |
| `nullable-enum-headers` | [#946](https://github.com/nickderobertis/crozier/issues/946) | A nullable enum header, whether a `$ref`, inline, or `allOf: [$ref]` beside `nullable: true` (tonik's `X-Nullable-Enum`), is sent as `<arg>.value` in python-enums mode. |
| `xml-helper-import` | [#948](https://github.com/nickderobertis/crozier/issues/948) | `AlertAtomEntry`, with two element lists of one item class and so neither an `append` nor a child builder, imports no `append_xml_child`. |
| `boolean-component-schemas` | [#941](https://github.com/nickderobertis/crozier/issues/941) | `Never: false` and `Anything: true` are both `typing.Any` aliases; an object with an inline boolean property is `typing.Any` whole. |
| `discriminator-only-parent` | [#955](https://github.com/nickderobertis/crozier/issues/955) | `InstanceProvider`, a `type: object` holding only a discriminator mapping, is the discriminated union of its mapped schemas, and each schema extending it through `allOf` generates. |
| `ignored-accept-header-enum` | [#956](https://github.com/nickderobertis/crozier/issues/956) | An optional `accept` header over `application/json`, `text/plain` and `*/*`, defaulting to `*/*`, is the constant `"accept": "*/*"` and no argument; no member of its enum is named. |
| `path-query-same-name` | [#943](https://github.com/nickderobertis/crozier/issues/943) | A path parameter and a query parameter both named `type`: `fern check` exits 1 (`Parameters query parameter 'type', path parameter 'type' all normalize to 'type'`), a check-only finding, and `fern generate` exits 0 with `type_path_param` beside `type`. crozier already matched it. |
| `invalid-response-examples` | [#940](https://github.com/nickderobertis/crozier/issues/940) | A `200` example whose `kind` is outside its enum and a `404` example whose `title` is a number: Fern refuses (its [`fern-refusal.txt`](invalid-response-examples/fern-refusal.txt), `Expected example to be a string. Example is: 12345`). The document is valid OpenAPI (manager ruling `a0`), so crozier generates it in both modes, with and without `--fern-strict`. Neither tool writes a response or error example into any file: with the examples made valid, Fern's tree holds neither value, so there is no emitted value to repair. |
| `normalized-component-identity` | [#944](https://github.com/nickderobertis/crozier/issues/944) | Components `kiln/glaze-coat` and `kiln-glaze/coat`, both `KilnGlazeCoat`, reached from one request body: one class, the last declaration's (`right: int`), so `left` is typed with it. crozier keeps that class and gives `kiln/glaze-coat` its own `KilnGlazeCoat2`: the [`colliding-component-own-class`](../../departures/evidence/colliding-component-own-class.md) departure. |
| `normalized-component-identity-responses` | #944 | The same components, each an operation's `200`: Fern refuses (its [`fern-refusal.txt`](normalized-component-identity-responses/fern-refusal.txt), `Example is missing required property "response.body.right"`) because it validates its example of one against the merged other. The document is valid OpenAPI and the refusal only Fern's limitation (manager ruling `a3`), so crozier generates it, each response typed with its own component's class. |
| `normalized-component-identity-control` | #944 | One component `kiln/glaze-coat`: `KilnGlazeCoat`, as crozier writes it. |
| `single-letter-component-words` | [#992](https://github.com/nickderobertis/crozier/issues/992) | A run of one-letter words in a component name is one class word: `a/b-c` is `Abc`, `p-q-r` `Pqr`, `m_n` `Mn`, `u/v-w` `Uvw` and `k/l-mn` `KlMn`, while `ab/c-d` is `AbCd` and a lone one-letter word beside longer ones keeps its capital (`e/fg-h` is `EFgH`). Every annotation and return type naming one spells it the same way. Each is named by an unescaped pointer (`#/components/schemas/a/b-c`), which the pair resolves. |

One measured difference is outside these tickets and recorded as a follow-up:
Fern types an operation whose response, or a property, is a `~1`-escaped
pointer to a slash-named component as `typing.Any` (crozier resolves it). A
first measurement of `single-letter-component-words` with escaped pointers
showed it again for every property and the response.
