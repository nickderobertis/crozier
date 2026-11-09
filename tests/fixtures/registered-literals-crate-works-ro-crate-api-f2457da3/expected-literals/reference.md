# Reference
## capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_capabilities</a>() -> Capabilities</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declare what this implementation supports — the spec version it targets, the extensions it implements, and the search filters and facets it provides. Every conformant implementation MUST provide this endpoint so that clients can feature-detect rather than relying on per-archive configuration or probing.

See the [Capabilities guide](https://ro-crate-api.crate-works.org/docs/getting-started/capabilities) for how clients should use this endpoint, and the [Extensions guide](https://ro-crate-api.crate-works.org/docs/extensions) for how extensions are registered.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.capabilities.get_capabilities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## entities
<details><summary><code>client.entities.<a href="src/fern/entities/client.py">list_entities</a>(...) -> ListEntitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve and list the entities in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description). The response can be filtered, paginated, and sorted, allowing clients to navigate large archives efficiently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entities.list_entities(
    member_of="https://catalog.paradisec.org.au/repository/NT1",
    entity_type=[
        "http://pcdm.org/models#Collection"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_of:** `typing.Optional[str]` — Indicates that an entity is a member of another entity (e.g., a sub-collection). Use this parameter to filter results to only entities that belong to a certain parent.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[typing.Union[EntityType, typing.Sequence[EntityType]]]` — Restrict the types of entities that are returned by specifying which RO-Crate profiles they conform to. Any valid entity type URI may be used; if no entities match the given type, an empty list is returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning the results, useful for pagination.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListEntitiesRequestSort]` — Field to sort by, such as `name` or `createdAt`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 

Sort order:
* `asc` - Ascending, from A to Z
* `desc` - Descending, from Z to A
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/fern/entities/client.py">get_entity</a>(...) -> Entity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an entity in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entities.get_entity(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The unique RO-Crate ID representing a specific entity in the repository.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/fern/entities/client.py">delete_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Delete an entity that no RO-Crate contributes to — its `roCrateIds` is empty. Such entities (for example an Organisation whose last contributing RO-Crate was deleted but which the implementation chose to retain) cannot be reached by any deposit-session operation, so this is the one entity-level write.

An entity with contributing RO-Crates cannot be deleted directly — its lifecycle is governed by its RO-Crates — and the request is rejected with `409 Conflict`.

After deletion the entity's URI follows the implementation's declared `tombstonePolicy`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entities.delete_entity(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The unique RO-Crate ID representing a specific entity in the repository.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/fern/entities/client.py">get_entity_metadata</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the entity's RO-Crate Metadata Document: the complete JSON-LD conforming to the RO-Crate specification. This is the metadata document itself, not the summary `Entity` object returned by `GET /entity/{id}`.

This endpoint works for any entity type: Collection, Object, or MediaObject.

The returned document's provenance is implementation-defined: it may be a stored metadata document, or a view derived from the metadata documents of the entity's contributing RO-Crates. Either way it MUST be a valid RO-Crate whose root data entity describes this entity. To retrieve the original deposited metadata document verbatim, use `GET /ro-crate/{id}/metadata` (available where the implementation supports deposit).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entities.get_entity_metadata(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate entity ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/fern/entities/client.py">head_entity_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve RO-Crate metadata headers without downloading the metadata content. Returns the same headers as GET but with no response body, useful for checking metadata availability and caching information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entities.head_entity_metadata(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate entity ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## search
<details><summary><code>client.search.<a href="src/fern/search/client.py">entities</a>(...) -> SearchEntitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform advanced or basic searches across the entire RO-Crate collection. This includes free text queries, as well as filters for specific fields such as `inLanguage` or `mediaType`. The search results can be paginated, sorted, and optionally returned alongside facet counts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FilterRange
from fern.environment import FernApiEnvironment
from fern.search import SearchEntitiesRequestBoundingBox, SearchEntitiesRequestBoundingBoxTopRight, SearchEntitiesRequestBoundingBoxBottomLeft

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.entities(
    search_type="advanced",
    query="name: West Alor AND description: linguistic",
    filters={
        "inLanguage": [
            "English"
        ],
        "mediaType": [
            "audio/mpeg"
        ],
        "createdAt": [
            FilterRange(
                gte="1965-01-01",
                lte="1965-12-31",
            ),
            FilterRange(
                gte="1972-01-01",
                lte="1972-12-31",
            )
        ]
    },
    bounding_box=SearchEntitiesRequestBoundingBox(
        top_right=SearchEntitiesRequestBoundingBoxTopRight(
            lat=-33.7,
            lng=151.3,
        ),
        bottom_left=SearchEntitiesRequestBoundingBoxBottomLeft(
            lat=-34.1,
            lng=150.9,
        ),
    ),
    limit=20,
    offset=0,
    order="desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 

The query string used in the search. Behavior depends on `searchType`. For `basic`, this can be free text. For `advanced`, Boolean operators can be used.

When searchType is `basic` this is a free text field of text to search.

When searchType is `advanced` this is a boolean search field.
Examples:
  name: John
  name: John AND description: Engineer
  name: John AND (description: Engineer OR description: developer)

NOTE: This API is implementation-agnostic. The examples above show basic boolean syntax that most search engines support.
API implementors may support additional query syntax - refer to your implementation's documentation for details.
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[SearchEntitiesRequestSearchType]` — Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]]` 

A set of key-value pairs representing additional filters. Keys MUST be filter fields the implementation declares in `/capabilities` under `search.filters`; a request using an undeclared key MUST be rejected with a 400 `ValidationError`.

Each value is either an array of acceptable values (matched as exact terms, valid for any filter type), a single range object with inclusive `gte`/`lte` bounds, or a non-empty array of range objects matched as an OR of the ranges — an entity matches when any of the ranges matches. Ranges, single or in an array, are valid only for filters declared with type `date` or `number`; a range sent to a `string` or `boolean` filter MUST be rejected with a 400 `ValidationError`. An array MUST NOT mix exact terms and range objects; such a request MUST be rejected with a 400 `ValidationError`.
    
</dd>
</dl>

<dl>
<dd>

**bounding_box:** `typing.Optional[SearchEntitiesRequestBoundingBox]` — Will filter the results to entities that exist inside the bounding box.
    
</dd>
</dl>

<dl>
<dd>

**geohash_precision:** `typing.Optional[int]` — If supplied, returns a geohash grid with this precision. Must be between 1 (lowest precision) and 12 (highest precision).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning the results, enabling paging.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchEntitiesRequestSort]` 

The field on which to sort results. Defaults to `relevance`, which orders
results by search score (highest first). When set to `relevance`, the
`order` parameter is ignored. Use `id`, `name`, `createdAt`, or
`updatedAt` to sort by a specific field.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 

Sort order:
* `asc` - Ascending, from A to Z
* `desc` - Descending, from Z to A
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## files
<details><summary><code>client.files.<a href="src/fern/files/client.py">list_files</a>(...) -> ListFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve and list file in the repository. This endpoint returns key metadata describing each file. The response can be filtered by memberOf to show files attached to a specific entity, and supports pagination and sorting.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.list_files(
    member_of="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_of:** `typing.Optional[str]` — Filter to only files that are directly attached to a specific entity (e.g., files within a collection or object).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning the results, useful for pagination.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFilesRequestSort]` — Field to sort by, such as `filename` or `createdAt`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 

Sort order:
* `asc` - Ascending, from A to Z
* `desc` - Descending, from Z to A
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a file. The file can be returned inline (e.g., displayed in the browser) or as an attachment for download (e.g., prompting a save dialog), based on the disposition parameter.
The API can serve the file directly or redirect to the location of the file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
    filename="foo.wav",
    range="bytes=0-1023",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The ID of the file.
    
</dd>
</dl>

<dl>
<dd>

**disposition:** `typing.Optional[GetFileRequestDisposition]` — The HTTP Content-Disposition for how the file should be handled by the client.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — When the file is served as an attachment, the name to use when saving.
    
</dd>
</dl>

<dl>
<dd>

**no_redirect:** `typing.Optional[bool]` — Return the location as JSON instead of a 302 redirect.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` — Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">head_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve file metadata headers without downloading the file content. Returns the same headers as GET but with no response body, useful for checking file availability, size, type, and caching information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.head_file(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
    filename="foo.wav",
    range="bytes=0-1023",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The ID of the file.
    
</dd>
</dl>

<dl>
<dd>

**disposition:** `typing.Optional[HeadFileRequestDisposition]` — The HTTP Content-Disposition for how the file should be handled by the client.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — When the file is served as an attachment, the name to use when saving.
    
</dd>
</dl>

<dl>
<dd>

**no_redirect:** `typing.Optional[bool]` — Return the location as JSON instead of a 302 redirect.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` — Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## deposits
<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">create_deposit</a>(...) -> Deposit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Open a deposit session that will create a new RO-Crate. The RO-Crate comes into existence only at the deposit's first successful finalise — until then nothing is readable and no entities exist.

The request body MAY propose a `roCrateId` where the implementation's `idMinting` capability is `client` or `both`; when the body or the field is absent the server mints one (`server` or `both`). Proposing an ID that is not supported by the declared `idMinting` mode is rejected with `422`; proposing an ID that already exists is rejected with `409`. The RO-Crate ID is returned immediately so the client can reference it from the deposited metadata document; whether the metadata document MUST reference it is implementation-defined and enforced at finalise.

A previously deleted RO-Crate ID MAY be reused; implementations MAY refuse with `409`. Recreation is a new RO-Crate, not a continuation — no relationship to the deleted RO-Crate's history or entities is implied.

To update an existing RO-Crate, use `POST /ro-crate/{id}/deposits` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.create_deposit()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ro_crate_id:** `typing.Optional[Id]` — A client-proposed ID for the new RO-Crate. Only valid when the implementation's `idMinting` capability is `client` or `both`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">get_deposit</a>(...) -> Deposit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Retrieve the deposit, including its lifecycle state, the files staged so far with per-file upload status, and the violations recorded by the most recent failed finalise. This is the polling resource for asynchronous finalisation: after a `202` from finalise, poll here until the state leaves `finalising`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.get_deposit(
    id="dep_8f14e45f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">abort_deposit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Abort an `open` deposit, discarding its staged metadata document and files. Aborting is terminal; the RO-Crate is left at its prior version (or never comes into existence for a create deposit).

Deposits are also subject to implementation-defined expiry — an expired deposit behaves as aborted, and subsequent access MAY return `404`. Where the implementation declares `depositTtlSeconds` in `/capabilities`, that is the expiry horizon.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.abort_deposit(
    id="dep_8f14e45f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">stage_deposit_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Stage the RO-Crate metadata document for this deposit. This is a full replace — staging a new metadata document discards the previously staged one; there is no metadata PATCH and no metadata DELETE. The metadata document and files may be staged in any order; metadata–file association is checked at finalise.

At finalise the staged metadata document becomes the RO-Crate's authoritative file manifest: each file entity in the metadata document resolves to bytes staged in this deposit, else (for update deposits) to the file carried forward by `@id` from the baseline version, else remains an unresolved reference. Unresolved references are not protocol errors — they simply `404` when followed — but implementations MAY reject them at finalise via validation. Files present in the baseline but absent from the new metadata document drop out of the new version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.stage_deposit_metadata(
    id="dep_8f14e45f",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` — RO-Crate metadata conforming to the RO-Crate specification
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">stage_deposit_file</a>(...) -> typing.Optional[FileUploadTarget]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Stage a file in this deposit. `{fileId}` is the file entity's `@id` in the deposited metadata document, percent-encoded — for attached files, its crate-relative path. The metadata document and files may be staged in any order.

Two upload modes share this endpoint, discriminated by the request `Content-Type`; the implementation declares which it supports in the `fileUpload` capability:

- **Inline** (`fileUpload` contains `inline`): the request body is the file's bytes, sent with the file's own media type. Responds `204`.
- **Presigned** (`fileUpload` contains `presigned`): the request body is `application/json` transport metadata (size, checksum, media type) and the response is `200` with an upload target the client sends the bytes to directly. There is no per-file completion call — finalise verifies that the bytes landed and match the declared size and checksum.

Only transport metadata is carried here; descriptive metadata about the file lives in the metadata document. Staging the same `{fileId}` again replaces the earlier staging. Using a mode the implementation does not declare is rejected with `400`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.stage_deposit_file(
    id="dep_8f14e45f",
    file_id="NT1-001-001A.mp3",
    size=2048576,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — The file's size in bytes. Verified at finalise.
    
</dd>
</dl>

<dl>
<dd>

**checksum:** `typing.Optional[str]` — The file's checksum, prefixed with the algorithm (e.g. `sha256:`). Verified at finalise when supplied.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[str]` — The MIME type of the file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">unstage_deposit_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Remove a file staged in this deposit. Valid while the deposit is `open`. This only affects the deposit's staging area — to drop a file from an existing RO-Crate, stage a metadata document that no longer references it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.unstage_deposit_file(
    id="dep_8f14e45f",
    file_id="NT1-001-001A.mp3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">finalise_deposit</a>(...) -> Deposit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Finalise the deposit: validate the staged content, publish it as the RO-Crate's new current version (replacing the prior version wholesale), and materialise catalog entities from it. Validation depth and materialisation rules are implementation-defined.

Finalisation MAY complete synchronously or asynchronously, at the server's discretion per request — there is no capability flag. A `200` returns the deposit in state `complete`; a `202` returns it in state `finalising`, and the client polls `GET /deposit/{id}` until the state leaves `finalising`. One client code path handles both.

For every file staged in presigned mode, finalise verifies the bytes landed and match the declared size and checksum; missing or mismatched files are validation violations.

**Failure atomicity is guaranteed**: a finalise that does not reach `complete` leaves no observable change. On validation failure the deposit returns to `open` with the violations recorded — as a `422` on the synchronous path, and in the deposit's `errors` field on the asynchronous path. Non-validation failures (including the target RO-Crate having been deleted mid-deposit) also return the deposit to `open` with the failure recorded; retry is safe, and abort covers walking away. Once `complete`, the new metadata document and all materialised entities are readable; readers are not guaranteed to observe the transition as a single atomic flip.

For update deposits, carry-forward resolves against the baseline version pinned when the deposit was opened; the last finalise wins as a unit. Implementations MAY reject a finalise whose baseline has been superseded with `409`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.finalise_deposit(
    id="dep_8f14e45f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The deposit ID, as returned when the deposit was created.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deposits.<a href="src/fern/deposits/client.py">create_update_deposit</a>(...) -> Deposit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Open a deposit session against an existing RO-Crate. The deposit starts logically empty; the client stages a new metadata document plus only the files that changed. At finalise the new metadata document is the authoritative file manifest — unchanged files are carried forward from the baseline by `@id`, and files absent from the new metadata document drop out. A metadata-only fix is therefore just `PUT /deposit/{id}/metadata` followed by finalise.

The baseline for carry-forward is the RO-Crate's current version at the moment this deposit is created. Concurrent open deposits against one RO-Crate are allowed; each finalise replaces the RO-Crate wholesale, so the last finalise wins as a unit.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deposits.create_update_deposit(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ro_crates
<details><summary><code>client.ro_crates.<a href="src/fern/ro_crates/client.py">list_ro_crates</a>(...) -> ListRoCratesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

List RO-Crates, paginated and sorted. The response contains whatever the caller is allowed to see under the implementation's visibility model: implementations choose whether RO-Crates are a public surface (listable by anyone, with per-object `access` governing metadata-document retrieval) or a depositor-only management surface (requiring the `write` scope).

There are no content filters — catalog-side questions belong to `/entities` and `/search`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ro_crates.list_ro_crates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning the results, useful for pagination.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListRoCratesRequestSort]` — Field to sort by.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 

Sort order:
* `asc` - Ascending, from A to Z
* `desc` - Descending, from Z to A
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ro_crates.<a href="src/fern/ro_crates/client.py">get_ro_crate</a>(...) -> RoCrate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Retrieve an RO-Crate. The body is deliberately lean: identity, the entities materialised from the current version, timestamps, and access. The deposited metadata document — `GET /ro-crate/{id}/metadata` — is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.

`entityIds` is the authoritative answer to "what did my deposit create". It is the inverse of the entity's `roCrateIds` and can change when later deposits (of this or other RO-Crates) alter the materialisation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ro_crates.get_ro_crate(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ro_crates.<a href="src/fern/ro_crates/client.py">delete_ro_crate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Delete an RO-Crate — its metadata document and files. Deletion is not a deposit session; it is already atomic. Implementations needing slow teardown MAY return `202 Accepted`.

The spec mandates no preconditions; implementations MAY refuse per their own policy (curatorial holds, cross-references) with `409` and a reason. The effect on materialised entities is implementation-defined, mirroring re-deposit pruning: an entity no other RO-Crate contributes to MAY be removed, and deliberate retention is legitimate. An entity with other contributors survives — the deleted RO-Crate simply drops out of its `roCrateIds`.

Open deposits do not block deletion: delete wins, and a subsequent finalise of such a deposit fails back to `open` with the failure recorded. Implementations MAY auto-abort open deposits against the deleted RO-Crate.

After deletion, the RO-Crate's URIs (including `/ro-crate/{id}/metadata`) follow the implementation's declared `tombstonePolicy`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ro_crates.delete_ro_crate(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ro_crates.<a href="src/fern/ro_crates/client.py">get_ro_crate_metadata</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Retrieve the RO-Crate's current RO-Crate metadata document, verbatim as deposited. Unlike `GET /entity/{id}/metadata`, which may return a derived view, this endpoint always returns the original deposited metadata document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ro_crates.get_ro_crate_metadata(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ro_crates.<a href="src/fern/ro_crates/client.py">head_ro_crate_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

Retrieve the deposited metadata document's headers without downloading the content. Returns the same headers as GET but with no response body, useful for checking availability and caching information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ro_crates.head_ro_crate_metadata(
    id="https://catalog.paradisec.org.au/repository/NT1/001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `Id` — The RO-Crate ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

