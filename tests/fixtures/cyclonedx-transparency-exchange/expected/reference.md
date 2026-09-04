# Reference
## TEA Product
<details><summary><code>client.tea_product.<a href="src/fern/tea_product/client.py">get_tea_product_by_uuid</a>(...) -> Product</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a TEA Product by UUID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product.get_tea_product_by_uuid(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of the TEA product in the TEA server
    
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

<details><summary><code>client.tea_product.<a href="src/fern/tea_product/client.py">query_tea_products</a>(...) -> PaginatedProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of TEA products. Note that multiple products may match.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product.query_tea_products()

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

**id_type:** `typing.Optional[IdentifierType]` — Type of identifier specified in the `idValue` parameter
    
</dd>
</dl>

<dl>
<dd>

**id_value:** `typing.Optional[str]` — If present, only the objects with the given identifier value will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[QueryTeaProductsRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[QueryTeaProductsRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

## TEA Product Release
<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">get_releases_by_product_id</a>(...) -> PaginatedProductReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get releases of the product
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.get_releases_by_product_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetReleasesByProductIdRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.

When `version` is selected, ordering is by the stored version string according to
the server's documented string collation; semantic-version precedence is not implied.
Servers MUST apply a stable and deterministic string collation for version sorting,
and the same collation MUST be used consistently across pages for a pagination sequence.

When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
consistently. Missing `releaseDate` values sort after populated `releaseDate` values
for ascending order and before populated `releaseDate` values for descending order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetReleasesByProductIdRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">get_tea_product_release_by_uuid</a>(...) -> ProductRelease</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a TEA Product Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.get_tea_product_release_by_uuid(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product Release in the TEA server
    
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

<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">query_tea_product_releases</a>(...) -> PaginatedProductReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of TEA product releases. Note that multiple product releases may match.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.query_tea_product_releases()

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

**id_type:** `typing.Optional[IdentifierType]` — Type of identifier specified in the `idValue` parameter
    
</dd>
</dl>

<dl>
<dd>

**id_value:** `typing.Optional[str]` — If present, only the objects with the given identifier value will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[QueryTeaProductReleasesRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.

When `version` is selected, ordering is by the stored version string according to
the server's documented string collation; semantic-version precedence is not implied.
Servers MUST apply a stable and deterministic string collation for version sorting,
and the same collation MUST be used consistently across pages for a pagination sequence.

When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
consistently. Missing `releaseDate` values sort after populated `releaseDate` values
for ascending order and before populated `releaseDate` values for descending order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[QueryTeaProductReleasesRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">get_latest_collection_for_product_release</a>(...) -> Collection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the latest TEA Collection belonging to the TEA Product Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.get_latest_collection_for_product_release(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product Release in the TEA server
    
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

<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">get_collections_by_product_release_id</a>(...) -> PaginatedCollectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the TEA Collections belonging to the TEA Product Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.get_collections_by_product_release_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product Release in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetCollectionsByProductReleaseIdRequestSortField]` 

The field by which to sort the results.

Paginated collection results MUST be ordered first by the selected `sortField`,
then by `version` as the deterministic secondary key if additional tie-breaking
is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
match the associated release UUID and can be shared across collection revisions.

The only currently supported collection `sortField` is `version`, so the secondary
`version` key is redundant unless additional collection sort fields are added later.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetCollectionsByProductReleaseIdRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_product_release.<a href="src/fern/tea_product_release/client.py">get_collection_for_product_release</a>(...) -> Collection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific Collection (by version) for a TEA Product Release by its UUID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_product_release.get_collection_for_product_release(
    uuid_="uuid",
    collection_version=1,
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

**uuid:** `Uuid` — UUID of TEA Product Release in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**collection_version:** `int` — Version of TEA Collection
    
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

## CLE
<details><summary><code>client.cle.<a href="src/fern/cle/client.py">get_cle_by_product_release_id</a>(...) -> Cle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the CLE (Common Lifecycle Enumeration) data for a TEA Product Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cle.get_cle_by_product_release_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product Release in the TEA server
    
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

<details><summary><code>client.cle.<a href="src/fern/cle/client.py">get_cle_by_product_id</a>(...) -> Cle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the CLE (Common Lifecycle Enumeration) data for a TEA Product
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cle.get_cle_by_product_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Product in the TEA server
    
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

<details><summary><code>client.cle.<a href="src/fern/cle/client.py">get_cle_by_component_id</a>(...) -> Cle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the CLE (Common Lifecycle Enumeration) data for a TEA Component
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cle.get_cle_by_component_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component in the TEA server
    
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

<details><summary><code>client.cle.<a href="src/fern/cle/client.py">get_cle_by_component_release_id</a>(...) -> Cle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the CLE (Common Lifecycle Enumeration) data for a TEA Component Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cle.get_cle_by_component_release_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component Release in the TEA server
    
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

## TEA Component
<details><summary><code>client.tea_component.<a href="src/fern/tea_component/client.py">get_tea_component_by_id</a>(...) -> Component</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a TEA Component
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component.get_tea_component_by_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component in the TEA server
    
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

<details><summary><code>client.tea_component.<a href="src/fern/tea_component/client.py">get_releases_by_component_id</a>(...) -> PaginatedComponentReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get releases of the component
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component.get_releases_by_component_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetReleasesByComponentIdRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.

When `version` is selected, ordering is by the stored version string according to
the server's documented string collation; semantic-version precedence is not implied.
Servers MUST apply a stable and deterministic string collation for version sorting,
and the same collation MUST be used consistently across pages for a pagination sequence.

When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
consistently. Missing `releaseDate` values sort after populated `releaseDate` values
for ascending order and before populated `releaseDate` values for descending order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetReleasesByComponentIdRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_component.<a href="src/fern/tea_component/client.py">query_tea_components</a>(...) -> PaginatedComponentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of TEA components. Note that multiple components may match.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component.query_tea_components()

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

**id_type:** `typing.Optional[IdentifierType]` — Type of identifier specified in the `idValue` parameter
    
</dd>
</dl>

<dl>
<dd>

**id_value:** `typing.Optional[str]` — If present, only the objects with the given identifier value will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[QueryTeaComponentsRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[QueryTeaComponentsRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

## TEA Component Release
<details><summary><code>client.tea_component_release.<a href="src/fern/tea_component_release/client.py">query_tea_component_releases</a>(...) -> PaginatedComponentReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of TEA component releases. Note that multiple component releases may match.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component_release.query_tea_component_releases()

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

**id_type:** `typing.Optional[IdentifierType]` — Type of identifier specified in the `idValue` parameter
    
</dd>
</dl>

<dl>
<dd>

**id_value:** `typing.Optional[str]` — If present, only the objects with the given identifier value will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[QueryTeaComponentReleasesRequestSortField]` 

The field by which to sort the results.

Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
as a deterministic secondary tie-breaker.

When `version` is selected, ordering is by the stored version string according to
the server's documented string collation; semantic-version precedence is not implied.
Servers MUST apply a stable and deterministic string collation for version sorting,
and the same collation MUST be used consistently across pages for a pagination sequence.

When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
consistently. Missing `releaseDate` values sort after populated `releaseDate` values
for ascending order and before populated `releaseDate` values for descending order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[QueryTeaComponentReleasesRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_component_release.<a href="src/fern/tea_component_release/client.py">get_component_release_by_id</a>(...) -> ComponentReleaseWithCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the TEA Component Release with its latest collection
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component_release.get_component_release_by_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component Release in the TEA server
    
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

<details><summary><code>client.tea_component_release.<a href="src/fern/tea_component_release/client.py">get_latest_collection</a>(...) -> Collection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the latest TEA Collection belonging to the TEA Component Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component_release.get_latest_collection(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component Release in the TEA server
    
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

<details><summary><code>client.tea_component_release.<a href="src/fern/tea_component_release/client.py">get_collections_by_release_id</a>(...) -> PaginatedCollectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the TEA Collections belonging to the TEA Component Release
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component_release.get_collections_by_release_id(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Component Release in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

An opaque continuation token produced by a previous response.
This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
Clients MUST NOT parse, construct, or modify this token.

The token represents continuation state for the original query, including
`sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
and path parameters such as parent `uuid`.
When `pageToken` is supplied, clients MUST NOT change those result-affecting query
parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
parameters conflict with the token state. To change any result-affecting parameter,
clients MUST start a new pagination sequence without `pageToken`.

A `pageToken` is only valid with the same request path and same path parameter values
used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
when a `pageToken` is used with a different path or different path parameter values.

Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
`pageToken` values.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetCollectionsByReleaseIdRequestSortField]` 

The field by which to sort the results.

Paginated collection results MUST be ordered first by the selected `sortField`,
then by `version` as the deterministic secondary key if additional tie-breaking
is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
match the associated release UUID and can be shared across collection revisions.

The only currently supported collection `sortField` is `version`, so the secondary
`version` key is redundant unless additional collection sort fields are added later.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetCollectionsByReleaseIdRequestSortOrder]` 

The direction of the sort.

The selected sort order applies to both the primary `sortField` and the
resource-specific deterministic secondary tie-breaker. For products, components,
product releases, and component releases, the secondary key is `uuid`. For collections,
the secondary key is `version` if additional tie-breaking is needed.
    
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

<details><summary><code>client.tea_component_release.<a href="src/fern/tea_component_release/client.py">get_collection</a>(...) -> Collection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific Collection (by version) for a TEA Component Release by its UUID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_component_release.get_collection(
    uuid_="uuid",
    collection_version=1,
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

**uuid:** `Uuid` — UUID of TEA Collection in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**collection_version:** `int` — Version of TEA Collection
    
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

## TEA Artifact
<details><summary><code>client.tea_artifact.<a href="src/fern/tea_artifact/client.py">get_latest_artifact</a>(...) -> Artifact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata for latest revision of a specific TEA Artifact
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_artifact.get_latest_artifact(
    uuid_="uuid",
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

**uuid:** `Uuid` — UUID of TEA Artifact in the TEA server
    
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

<details><summary><code>client.tea_artifact.<a href="src/fern/tea_artifact/client.py">get_artifact_by_version</a>(...) -> Artifact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata for a specific revision of a specific TEA Artifact
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_artifact.get_artifact_by_version(
    uuid_="uuid",
    artifact_version=1,
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

**uuid:** `Uuid` — UUID of TEA Artifact in the TEA server
    
</dd>
</dl>

<dl>
<dd>

**artifact_version:** `int` — Version of TEA Artifact
    
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

## TEA Discovery
<details><summary><code>client.tea_discovery.<a href="src/fern/tea_discovery/client.py">discovery_by_tei</a>(...) -> typing.List[DiscoveryInfo]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discovery endpoint which resolves TEI into product release UUID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tea_discovery.discovery_by_tei(
    tei="urn%3Atei%3Auuid%3Aproducts.example.com%3Ad4d9f54a-abcf-11ee-ac79-1a52914d44b",
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

**tei:** `str` — Transparency Exchange Identifier (TEI) for the product being discovered. Provide the TEI as a URL-encoded string per RFC 3986, RFC 3987.
    
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

