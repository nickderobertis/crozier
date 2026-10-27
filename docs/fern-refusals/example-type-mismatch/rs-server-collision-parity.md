# RS-Server: a nullable string read as a colliding union

The certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3)
generates from `RS-PYTHON/rs-server` `services/frontend/resources/openapi.json`
at `83ebcafb173c53443d92c54aeeba4f221e36f9c2` (sha256
`a87710725b8bdea9cdeab44b61390b10718280a88432f6a4896c757c8704d27a`), and crozier
refused it:

```
example-type-mismatch: GET /auxip/search components/schemas/Item/properties/collection collides with ItemCollection
```

## Root cause

`colliding_property` treats an inline property schema as a named type of its
owner and property (`Item` + `collection`), so a later component of that name
(`ItemCollection`) takes the name, and Fern's example of the property is checked
against it. For an inline `anyOf`/`oneOf` that holds only when the union stays a
union. `string_led_union` counted `{type: 'null'}` as a member, so
`Item.collection: anyOf [{type: string}, {type: 'null'}]` passed as a two-member
string-led union. Fern reads that schema as the optional string it is, a type
with no name of its own, so nothing collides.

## Repair

`src/document_refusals/examples.rs::string_led_union` now requires at least two
members besides the null type. The union must still be led by a plain string,
so the predicate only narrows: a union refused before this change is still
refused unless its only other member is the null type.

## Measurements

Both new shapes were measured with `fern-refusals.py shapes example-type-mismatch`,
holding `~/.cache/crozier/fern-generation.lock` (`XDG_CACHE_HOME` is unset on
this host). Their rows are in
[`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv).

| shape | certified pair | crozier, both modes |
|---|---|---|
| [`nullable-string-union-collision-control.yml`](nullable-string-union-collision-control.yml): `anyOf [string, null]` beside a later `subscription_schedule` object | generates, 39 files ([log](evaluation-logs/fern-nullable-string-union-collision-control.log)) | generates, identical trees |
| [`nullable-string-union-collision-probe.yml`](nullable-string-union-collision-probe.yml): `anyOf [string, $ref, null]`, same collision | refuses, `Expected example to be an object. Example is: "schedule"` ([log](evaluation-logs/fern-nullable-string-union-collision-probe.log)) | refuses, `example-type-mismatch` |

`a_nullable_string_property_generates_beside_the_name_collisions_fern_refuses`
in `crates/crozier-e2e/tests/e2e.rs` drives crozier's CLI in both modes over
every collision probe the class measures (string-led union, the new null-member
probe, inline enum, scalar taken by an inline object). Each one is still refused
with its element. The same test generates the new control, the
declared-first control and the unreferenced-scalar control identically in both
modes. With the repair reverted the test fails on the new control. The unit test
`a_string_union_whose_only_other_member_is_null_takes_no_colliding_name` drives
`colliding_property` and `string_led_union` over the same documents.

The narrowing also releases no measured real document. Five refused population
documents carry a property-collision diagnostic in
[`population-refusals.jsonl`](evaluation-logs/population-refusals.jsonl) and are
cached on this host (digests `3155c659…`, `7374a3aa…`, `8fdc22dd…`, `af2e5d8e…`,
`e7a38442…`). Re-run on this tree, each is still refused in both modes at the
same element.

## The document's outcome

RS-Server is **not excepted**: the refusal was crozier's alone. On this tree,
crozier generates from the exact document (sha256 above) in both modes:
`crozier generate python` and `--fern-strict` each write 223 files, the same set.

### Comparison against the certified pair's golden

The golden was generated at the certified pair with `just fern-goldens-generate
--version 5.41.3 --fixture rs-server`, plus its literals overlay, under the same
lock. It has 231 files, and its `.fern/metadata.json` records CLI 5.163.1 and SDK
5.41.3. crozier's output under the corpus configuration (package `fern`) was
compared to it by the corpus gate's own comparison, as `just fixtures-gaps
rs-server` and `just fixtures-diff rs-server` report it. That comparison ran on this branch's repair commit with the row wired
in. The wiring has since been removed; the `src/` it ran against is unchanged.

- 199 files byte-match.
- `src/fern/core/client_wrapper.py` matches apart from the
  `sdk-identity-header-prefix` departure lines.
- 31 files differ, 9 of them not emitted by crozier. crozier emits one file the
  golden lacks (`types/time_interval_interval_item_item.py`).

No difference involves the repaired predicate or any example value. They are
emission causes owned by node `rs-server-emission-parity`:

1. **`bbox` and `coordinates` inside inlined discriminated-union variants.** The
   GeoJSON members (`Point`, `LineString`, …, `GeometryCollection`) are inlined
   as variants of `ItemGeometry`, `ItemInputGeometry`,
   `GeometryCollection{Input,Output}GeometriesItem`, and the `stac_pydantic_*`
   geometries. In those variants, `bbox: anyOf [prefixItems tuple arrays, null]`
   is typed `Optional[PointBbox]`-style. The certified pair writes
   `Optional[List[Any]]`, as crozier already does on the standalone models. The
   request body's `Feature`/`FeatureCollection` variants differ the same way
   (`ItemInputBbox`, `ItemCollectionInputBbox`).
   The nested `coordinates` items become `Union[Position2D, Position3D]` where
   the pair names `PolygonCoordinatesItemItem`, `MultiLineStringCoordinatesItemItem`
   and `MultiPolygonCoordinatesItemItemItem` (the last not emitted by crozier).
   **Shown failing:** crozier never emits the `*_bbox` modules those variants
   import, so importing `types.geometry_collection_input_geometries_item` raises
   `ModuleNotFoundError: No module named '….types.geometry_collection_input_bbox'`.
   crozier's SDK for this document does not import.
2. **`type: {type: string, const: …}` on the standalone member models.** The
   pair keeps the property and emits its single-value enum (`PointType`,
   `LineStringType`, `MultiPointType`, `MultiLineStringType`, `PolygonType`,
   `MultiPolygonType`, `GeometryCollectionInputType`, and the request body's
   `PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyType`).
   crozier drops the property and the eight files. The `__init__.py` re-exports
   differ to match.
3. **`TimeInterval.interval`, arrays of arrays of `anyOf [date-time, null]`.** The
   pair writes `List[List[Optional[dt.datetime]]]`; crozier writes a named
   `TimeIntervalIntervalItemItem` union. The worked examples in `reference.md` and
   `catalog_transaction_extension/client.py` follow the types: the pair writes
   `None` and `[[]]`, crozier writes datetimes.
4. **The root client's `api_key`.** The pair has `api_key: str`; crozier has
   `api_key: typing.Optional[str] = None` (`client.py`).
5. **`catalog_transaction_extension/types/__init__.py`.** The pair imports the
   three names of `create_item_catalog_collections_collection_id_items_post_request_body`
   in one statement; crozier writes one statement per name.
6. **The root `__init__.py` import order.** The pair places
   `from .client import AsyncFernApi, FernApi` after the `catalog_transaction_extension`
   block; crozier places it before `adgs_stations`.

### Why it is not registered

The corpus rules admit the document: the repository's `LICENSE` at the pinned
commit is Apache-2.0 (blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`), the
document declares no `info.license`, and the revision is a commit sha. Following
the manager's ruling, it is registered only once it byte-matches, which is node
`rs-server-emission-parity`'s work. That node can reuse the golden, its literals
overlay, the vendored source, the measured diff and the registration patch,
which are kept outside the tree in this dispatch's scratch directory
(`3794034-30/rs-server-golden/`). That registration also gives the narrowed
predicate's arm a real golden witness. Node `reconcile-parity-ledger` restates
the coverage counts afterwards.
