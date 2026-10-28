# Reference
## SortExtension
<details><summary><code>client.sort_extension.<a href="src/fern/sort_extension/client.py">sortables</a>() -> SortablesSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.sort_extension.sortables()

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

<details><summary><code>client.sort_extension.<a href="src/fern/sort_extension/client.py">collection_sortables</a>(...) -> SortablesSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.sort_extension.collection_sortables(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

<details><summary><code>client.sort_extension.<a href="src/fern/sort_extension/client.py">collections_catalog_sortables</a>() -> SortablesSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.sort_extension.collections_catalog_sortables()

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

## AdgsFilterExtension
<details><summary><code>client.adgs_filter_extension.<a href="src/fern/adgs_filter_extension/client.py">queryables</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_filter_extension.queryables()

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

<details><summary><code>client.adgs_filter_extension.<a href="src/fern/adgs_filter_extension/client.py">collection_queryables</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_filter_extension.collection_queryables(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

## AdgsStations
<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">search</a>(...) -> ItemCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.search()

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

**request:** `SearchPostRequest` 
    
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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_root_catalog</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the RSPY ADGS Search catalog landing page.

This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
page for the RSPY ADGS service. The catalog includes basic metadata about the service and links to
available collections.

The resulting catalog contains:
- `id`: A unique identifier for the catalog, generated as a UUID.
- `description`: A brief description of the catalog.
- `title`: The title of the catalog.
- `stac_version`: The version of the STAC specification to which the catalog conforms.
- `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
- `links`: A link to the `/adgs/collections` endpoint where users can find available collections.

The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
`links` field, allowing users to discover available collections in the ADGS service.

Parameters:
- request: The HTTP request object which includes details about the incoming request.

Returns:
- dict: A dictionary representation of the STAC catalog, including metadata and links.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_root_catalog()

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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_conformance</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the STAC/OGC conformance classes implemented by this server.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_conformance()

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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_allowed_adgs_collections</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the ADGS collections to which the user has access to.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_allowed_adgs_collections()

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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_adgs_collection</a>(...) -> GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a specific ADGS collection.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_adgs_collection(
    collection_id="collection_id",
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

**collection_id:** `str` — E.G. 
    
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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_adgs_collection_items</a>(...) -> GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of items from a specified AUXIP collection.

This endpoint returns a collection of items associated with the given AUXIP
collection ID. It utilizes the collection ID to validate access and fetches
the items based on defined query parameters.

Args:
    request (Request): The incoming HTTP request used for authentication and routing.
    collection_id (str): AUXIP collection ID. Must be a valid collection identifier
                         (e.g., 'ins_s1').
    bbox (BBoxType): Bounding box spatial filter, as [west, south, east, north] coordinates.
    datetime (DateTimeType): Temporal filter as an RFC 3339 timestamp or interval.
    filter_ (FilterType): CQL2 filter expression to further restrict results.
    filter_lang (FilterLangType): Language for the CQL2 filter, either "cql2-text" or "cql2-json".
    sortby (SortByType): Field and direction to sort results by.
    limit (LimitType): Maximum number of items to return per page.
    page (PageType): 1-based page index for pagination.

Returns:
    list[dict]: A FeatureCollection of items belonging to the specified collection, or an
                error message if the collection is not found.

Raises:
    HTTPException: If the authentication fails, or if there are issues with the
                   collection ID provided.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_adgs_collection_items(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `typing.Optional[str]` — Bounding box (geospatial footprint or extent, four or six comma-separated numbers).
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` — Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

A CQL2 filter expression for filtering items.

Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html
    
</dd>
</dl>

<dl>
<dd>

**filter_lang:** `typing.Optional[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang]` — The CQL2 filter encoding that the 'filter' value uses.
    
</dd>
</dl>

<dl>
<dd>

**sortby:** `typing.Optional[str]` — Sort by +/-fieldName (ascending/descending)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results that are included in each page of the response (between 1000 and 10_000)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number to be displayed, defaults to first one.
    
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

<details><summary><code>client.adgs_stations.<a href="src/fern/adgs_stations/client.py">get_adgs_collection_specific_item</a>(...) -> GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific item from a specified AUXIP collection.

This endpoint fetches details of a specific item within the given AUXIP collection
by its unique item ID. It utilizes the provided collection ID and item ID to
validate access and return item information.

Args:
    request (Request): The incoming HTTP request used for authentication and routing.
    collection_id (str): AUXIP collection ID. Must be a valid collection identifier
        (e.g., 'ins_s1').
    item_id (str): AUXIP item ID. Must be a valid item identifier
        (e.g., 'S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF').

Returns:
- dict: A JSON object containing details of the specified item, or an error
        message if the item is not found.

Raises:
- HTTPException: If the authentication fails, or if the specified item is
                not found in the collection.

Example:
A successful response will return: 

    {
        "id": "S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF",
        "type": "Feature",
        "properties": {
            ...  # Detailed properties of the item
        },
        "geometry": {
            ...  # Geometry details of the item
        },
        "links": [
            ...  # Links associated with the item
        ]
    }
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.adgs_stations.get_adgs_collection_specific_item(
    collection_id="collection_id",
    item_id="item_id",
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

**collection_id:** `str` — E.G. 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — E.G. S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF
    
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

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">show_my_information</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show user information.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.authentication.show_my_information()

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

## CadipFilterExtension
<details><summary><code>client.cadip_filter_extension.<a href="src/fern/cadip_filter_extension/client.py">queryables</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_filter_extension.queryables()

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

<details><summary><code>client.cadip_filter_extension.<a href="src/fern/cadip_filter_extension/client.py">collection_queryables</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_filter_extension.collection_queryables(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

## CadipStations
<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">search</a>(...) -> ItemCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.search()

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

**request:** `SearchPostRequest` 
    
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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_root_catalog</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the RSPY CADIP Search catalog landing page.

This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
page for the RSPY CADIP service. The catalog includes basic metadata about the service and links to
available collections.

The resulting catalog contains:
- `id`: A unique identifier for the catalog, generated as a UUID.
- `description`: A brief description of the catalog.
- `title`: The title of the catalog.
- `stac_version`: The version of the STAC specification to which the catalog conforms.
- `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
- `links`: A link to the `/cadip/collections` endpoint where users can find available collections.

The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
`links` field, allowing users to discover available collections in the CADIP service.

Parameters:
- request: The HTTP request object which includes details about the incoming request.

Returns:
- dict: A dictionary representation of the STAC catalog, including metadata and links.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_root_catalog()

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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_conformance</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the STAC/OGC conformance classes implemented by this server.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_conformance()

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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_allowed_cadip_collections</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to retrieve an object containing collections and links that a user is authorized to
    access based on their API key.

This endpoint reads the API key from the request to determine the roles associated with the user.
Using these roles, it identifies the stations the user can access and filters the available collections
accordingly. The endpoint then constructs a JSON, which includes links to the collections that match the allowed
stations.

- It begins by extracting roles from the `request.state.auth_roles` and derives the station names
  the user has access to.
- Then, it filters the collections from the configuration to include only those belonging to the
  allowed stations.
- For each filtered collection, a corresponding STAC collection is created with links to detailed
  session searches.

The final response is a dictionary representation of the STAC catalog, which includes details about
the collections the user is allowed to access.

Returns:
    dict: Object containing an array of Collection objects in the Catalog, and Link relations.

Raises:
    HTTPException: If there are issues with reading configurations or processing session searches.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_allowed_cadip_collections()

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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_cadip_collection</a>(...) -> GetCadipCollectionCadipCollectionsCollectionIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a STAC-Compliant Collection for a Specific CADIP Station.

This endpoint fetches and returns session data from an external CADIP server, structured as a STAC-compliant
Collection. By specifying a `collection_id`, the client can retrieve a collection of session metadata related to
that CADIP station.

### Path Parameters:
- `collection_id` (string): The unique identifier of the CADIP collection to retrieve.

### Response:
The response is a STAC Collection object formatted as a dictionary, which contains links to session details.
Each session is represented as a link inside the `links` array, following the STAC specification. These links point
 to the detailed metadata for each session.

### Key Operations:
1. **Configuration Lookup**: Reads the relevant configuration from `RSPY_CADIP_SEARCH_CONFIG`.
2. **CADIP Server Request**: Sends a request to the CADIP server to retrieve session data.
3. **STAC Formatting**: Transforms the session data into a STAC Collection format.
4. **Link Creation**: Adds links to session details in the response.

### Responses:
- **200 OK**: Returns the STAC Collection containing links to session metadata. If multiple collections are
available, returns a list of collections.
- **422 Unprocessable Entity**: Returns an error if the STAC Collection cannot be created due to missing or invalid
configuration details.

### Raises:
- **HTTPException**:
  - **422 Unprocessable Entity**: If any configuration data is missing, invalid, or causes an error when creating
  the STAC Collection.

This endpoint is secured by an API key validator, ensuring that only authorized users can retrieve data from the
CADIP station.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_cadip_collection(
    collection_id="collection_id",
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

**collection_id:** `str` — E.G. ins_s1
    
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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_cadip_collection_items</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a List of items for a specific collection.

This endpoint provides access to a list of sessions for a given collection from the CADIP station.
By specifying the `collection_id` in the path, clients can retrieve session metadata in the form of a STAC
(SpatioTemporal Asset Catalog) ItemCollection.

### Path Parameters:
- `collection_id` (string): The unique identifier of the collection from which session data is being requested.

### Response:
Returns a STAC ItemCollection containing metadata for each session in the specified collection.
Each session is represented as a STAC Item, containing key information such as:
- **Session metadata**: Information about the session's time, satellite, and session ID.

### Responses:
- **200 OK**: If sessions are found, returns the ItemCollection in JSON format.
- **404 Not Found**: If no matching sessions or collection is found.

### Errors:
- **500 Internal Server Error**: If an error occurs in reading configurations, creating query parameters, or
processing the session search.

This endpoint is protected by an API key validator, ensuring appropriate access to the CADIP station.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_cadip_collection_items(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `typing.Optional[str]` — Bounding box (geospatial footprint or extent, four or six comma-separated numbers).
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` — Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

A CQL2 filter expression for filtering items.

Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html
    
</dd>
</dl>

<dl>
<dd>

**filter_lang:** `typing.Optional[GetCadipCollectionItemsCadipCollectionsCollectionIdItemsGetRequestFilterLang]` — The CQL2 filter encoding that the 'filter' value uses.
    
</dd>
</dl>

<dl>
<dd>

**sortby:** `typing.Optional[str]` — Sort by +/-fieldName (ascending/descending)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results that are included in each page of the response (between 1000 and 10_000)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number to be displayed, defaults to first one.
    
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

<details><summary><code>client.cadip_stations.<a href="src/fern/cadip_stations/client.py">get_cadip_collection_item_details</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Detailed Information for a specific session in a collection.

This endpoint fetches metadata and asset details for a specific session within a collection from the CADIP station.
Clients can request session details by providing the `collection_id` and `session_id` as path parameters.
The session data is retrieved and converted from the original OData format into the STAC format,
which provides standardized metadata for spatiotemporal datasets.

### Path Parameters:
- `collection_id` (string): The unique identifier of the collection from which the session is being retrieved.
- `session_id` (string): The identifier of the specific session within the collection for which details are
requested.

### Response:
Returns a STAC Item containing metadata and asset details about the requested session, including:
- **Session metadata**: Contains important temporal information (e.g., `datetime`, `start_datetime`, and
`end_datetime`),
  the platform (`platform`), and session-specific details such as `externalIds`, `cadip:num_channels`,
  `cadip:station_id`, `cadip:station_unit_id`, `cadip:antenna_id`, and more.
- **Satellite information**: Includes satellite attributes such as `sat:absolute_orbit`, `cadip:acquisition_id`, and
status fields like `cadip:antenna_status_ok`, `cadip:front_end_status_ok`, and `cadip:downlink_status_ok`.
- **Assets**: A collection of asset objects associated with the session. Each asset contains:
  - A unique asset `href` (link) pointing to the asset resource.
  - Metadata such as `externalIds`, `cadip:retransfer`, `cadip:block_number`, `cadip:channel`,
    `created`, `eviction_datetime`, and `file:size`.
  - Asset `roles`, indicating the type of resource (e.g., "cadu").
  - Asset title and name.

### Responses:
- **200 OK**: If the session details are found, returns the STAC Item in JSON format.
- **404 Not Found**: If the `session_id` is not found within the specified collection.

The endpoint is protected by an API key validator, which requires appropriate access permissions.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.cadip_stations.get_cadip_collection_item_details(
    collection_id="collection_id",
    session_id="session_id",
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

**collection_id:** `str` — E.G. ins_s1
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` — E.G. S1A_20231120061537234567
    
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

## PripFilterExtension
<details><summary><code>client.prip_filter_extension.<a href="src/fern/prip_filter_extension/client.py">queryables</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_filter_extension.queryables()

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

<details><summary><code>client.prip_filter_extension.<a href="src/fern/prip_filter_extension/client.py">collection_queryables</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_filter_extension.collection_queryables(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

## PripStations
<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">search</a>(...) -> ItemCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.search()

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

**request:** `SearchPostRequest` 
    
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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_root_catalog</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Redirect to the landing page.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_root_catalog()

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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_conformance</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the STAC/OGC conformance classes implemented by this server.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_conformance()

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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_allowed_prip_collections</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the PRIP collections to which the user has access to.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_allowed_prip_collections()

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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_prip_collection</a>(...) -> GetPripCollectionPripCollectionsCollectionIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a specific PRIP collection.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_prip_collection(
    collection_id="collection_id",
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

**collection_id:** `str` 
    
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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_prip_collection_items</a>(...) -> GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of items from a specified PRIP collection.

This endpoint returns a collection of items associated with the given PRIP
collection ID. It utilizes the collection ID to validate access and fetches
the items based on defined query parameters.

Args:
    request (Request): Incoming HTTP request used for authentication and routing.
    collection_id (str): PRIP collection ID. Must be a valid collection identifier
                         (e.g., 'ins_s1').
    bbox (BBoxType, optional): Bounding box filter as four or six numbers
        [west, south, east, north] or [west, south, minz, east, north, maxz].
        Defaults to None. If provided, items intersecting the bbox are returned.

    datetime (DateTimeType, optional): Temporal filter. Either a single RFC 3339
        timestamp/interval (e.g., "2024-01-01T00:00:00Z") or a closed/open interval
        (e.g., "2024-01-01T00:00:00Z/2024-01-31T23:59:59Z", "../2024-01-01T00:00:00Z").
        Defaults to None.

    filter_ (FilterType, optional): CQL2 filter expression (text or JSON depending
        on `filter_lang`). Defaults to None.

    filter_lang (FilterLangType, optional): CQL2 language for `filter_`. One of
        "cql2-text" or "cql2-json". Defaults to "cql2-text".

    sortby (SortByType, optional): Sort specification. Single field or list of fields
        with optional direction, e.g., {"field": "published", "direction": "desc"}.
        Defaults to None (implementation default ordering).

    limit (LimitType, optional): Page size (maximum number of items to return).
        Defaults to None (service default / configured max).

    page (PageType, optional): 1-based page index.
        Defaults to None (first page).
Returns:
    list[dict]: A FeatureCollection of items belonging to the specified collection, or an
                error message if the collection is not found.

Raises:
    HTTPException: If the authentication fails, or if there are issues with the
                   collection ID provided.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_prip_collection_items(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `typing.Optional[str]` — Bounding box (geospatial footprint or extent, four or six comma-separated numbers).
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` — Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

A CQL2 filter expression for filtering items.

Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html
    
</dd>
</dl>

<dl>
<dd>

**filter_lang:** `typing.Optional[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang]` — The CQL2 filter encoding that the 'filter' value uses.
    
</dd>
</dl>

<dl>
<dd>

**sortby:** `typing.Optional[str]` — Sort by +/-fieldName (ascending/descending)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results that are included in each page of the response (between 1000 and 10_000)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number to be displayed, defaults to first one.
    
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

<details><summary><code>client.prip_stations.<a href="src/fern/prip_stations/client.py">get_prip_collection_specific_item</a>(...) -> GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific item from a specified PRIP collection.

This endpoint fetches details of a specific item within the given PRIP collection
by its unique item ID. It utilizes the provided collection ID and item ID to
validate access and return item information.

Args:
    request (Request): Incoming HTTP request used for authentication and routing.
    collection_id (str): PRIP collection ID. Must be a valid collection identifier (e.g., 'ins_s1').
    item_id (str): PRIP item ID. Must be a valid item identifier.

Returns:
- dict: A JSON object containing details of the specified item, or an error
        message if the item is not found.

Raises:
- HTTPException: If the authentication fails, or if the specified item is
                not found in the collection.

Example:
A successful response will return: 

    {
        "id": "S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF",
        "type": "Feature",
        "properties": {
            ...  # Detailed properties of the item
        },
        "geometry": {
            ...  # Geometry details of the item
        },
        "links": [
            ...  # Links associated with the item
        ]
    }
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.prip_stations.get_prip_collection_specific_item(
    collection_id="collection_id",
    item_id="item_id",
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

**collection_id:** `str` — E.G. 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — E.G. S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF
    
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

## OsamService
<details><summary><code>client.osam_service.<a href="src/fern/osam_service/client.py">create_and_delete_obs_accounts</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is called by an RS operator with the *rs_osam_update* role.
It triggers the synchronization of the creation and deletion of S3 Object Storage (OBS) accounts for all RS users,
associated to their Keycloak account.

How it works:

1. When a new Keycloak user account is created, an associated OBS access account **with no rights** is created
and linked to it.

2. When a Keycloak user account is deleted, the associated OBS access account is also deleted.

NOTE: to synchronize OBS user rights from Keycloak you then need to call the endpoint
* /storage/account/{user}/update*.

### Returns:
JSONResponse — Always a success message saying that the synchronization algorithm of the accounts started.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.osam_service.create_and_delete_obs_accounts()

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

<details><summary><code>client.osam_service.<a href="src/fern/osam_service/client.py">update_obs_user_rights</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is called by an RS operator with the *rs_osam_update* role. It updates the S3 Object Storage (OBS)
rights of any user, calculated from their associated Keycloak account.

When called, this endpoint will:

1. Read the user's roles from their Keycloak account.

2. Calculate the associated OBS access policy rights: they describe the buckets, paths, and permission levels
(such as read, write and download) that the user has access to.

3. Apply the access policy to the user's OBS account.

The operation ensures that the user's OBS permissions match their Keycloak permissions.

### Args
user (str) — The Keycloak username for which the access policy should be applied.

### Returns
JSONResponse — A JSON response confirming that the access policy has been applied.

### Raises
404 — If the user does not exist in Keycloak.<br>
400 — If the policy could not be applied by the Object Storage provider.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.osam_service.update_obs_user_rights(
    user="user",
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

**user:** `str` 
    
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

<details><summary><code>client.osam_service.<a href="src/fern/osam_service/client.py">get_your_s3credentials</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is called by any anthenticated user.
It returns your personnal S3 credentials, so you can connect to the bucket where your products have been generated.

### Returns
dict — A dictionary containing 'access_key', 'secret_key', 'endpoint', 'region' for the user's S3 storage.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.osam_service.get_your_s3credentials()

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

## Catalog
<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">landing_page</a>() -> LandingPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.landing_page()

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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">conformance_classes</a>() -> Conformance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.conformance_classes()

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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">get_item</a>(...) -> StacPydanticApiItemItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.get_item(
    collection_id="collection_id",
    item_id="item_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Item ID
    
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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">search</a>(...) -> ItemCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.search()

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

**request:** `SearchPostRequest` 
    
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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">get_collections</a>(...) -> Collections</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.get_collections()

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

**bbox:** `typing.Optional[str]` — Only return items intersecting this bounding box. Mutually exclusive with **intersects**.
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` 

Only return items that have a temporal property that intersects this value.

Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results that are included in each page of the response.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Allows additional filtering based on the properties of Item objects
    
</dd>
</dl>

<dl>
<dd>

**sortby:** `typing.Optional[str]` — An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Include or exclude fields from items body.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

A CQL2 filter expression for filtering items.

Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
Remember to URL encode the CQL2-JSON if using GET
    
</dd>
</dl>

<dl>
<dd>

**filter_crs:** `typing.Optional[str]` — The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`
    
</dd>
</dl>

<dl>
<dd>

**filter_lang:** `typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang]` — The CQL filter encoding that the 'filter' value uses.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Parameter to perform free-text queries against STAC metadata
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">get_collection</a>(...) -> StacPydanticApiCollectionCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.get_collection(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">get_item_collection</a>(...) -> ItemCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog.get_item_collection(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results that are included in each page of the response (capped to 10_000).
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `typing.Optional[str]` — Only return items intersecting this bounding box. Mutually exclusive with **intersects**.
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[str]` 

Only return items that have a temporal property that intersects this value.

Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Allows additional filtering based on the properties of Item objects
    
</dd>
</dl>

<dl>
<dd>

**sortby:** `typing.Optional[str]` — An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Include or exclude fields from items body.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 

A CQL2 filter expression for filtering items.

Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
Remember to URL encode the CQL2-JSON if using GET
    
</dd>
</dl>

<dl>
<dd>

**filter_crs:** `typing.Optional[str]` — The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`
    
</dd>
</dl>

<dl>
<dd>

**filter_lang:** `typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang]` — The CQL filter encoding that the 'filter' value uses.
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` 
    
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

## CatalogTransactionExtension
<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">update_item</a>(...) -> StacPydanticItemItemOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, ItemInputType, ItemProperties, Asset, Link

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.update_item(
    collection_id="collection_id",
    item_id="item_id",
    type=ItemInputType.FEATURE,
    geometry=None,
    properties=ItemProperties(
        datetime=None,
    ),
    id="id",
    assets={
        "key": Asset(
            href="href",
        )
    },
    links=[
        Link(
            href="href",
            rel="rel",
        )
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ItemInput` 
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">delete_item</a>(...) -> StacPydanticItemItemOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.delete_item(
    collection_id="collection_id",
    item_id="item_id",
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Item ID
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">patch_item</a>(...) -> StacPydanticItemItemOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, PartialItem

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.patch_item(
    collection_id="collection_id",
    item_id="item_id",
    request=PartialItem(),
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody` — Partial STAC Item.
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">create_collection</a>(...) -> StacPydanticCollectionCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, Link, CollectionInputType, Extent, SpatialExtent, TimeInterval

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.create_collection(
    id="id",
    description="description",
    links=[
        Link(
            href="href",
            rel="rel",
        )
    ],
    type=CollectionInputType.COLLECTION,
    license="license",
    extent=Extent(
        spatial=SpatialExtent(
            bbox=[
                []
            ],
        ),
        temporal=TimeInterval(
            interval=[
                [
                    None
                ]
            ],
        ),
    ),
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

**request:** `CollectionInput` 
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">update_collection</a>(...) -> StacPydanticCollectionCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, Link, CollectionInputType, Extent, SpatialExtent, TimeInterval

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.update_collection(
    collection_id="collection_id",
    id="id",
    description="description",
    links=[
        Link(
            href="href",
            rel="rel",
        )
    ],
    type=CollectionInputType.COLLECTION,
    license="license",
    extent=Extent(
        spatial=SpatialExtent(
            bbox=[
                []
            ],
        ),
        temporal=TimeInterval(
            interval=[
                [
                    None
                ]
            ],
        ),
    ),
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CollectionInput` 
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">delete_collection</a>(...) -> StacPydanticCollectionCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.delete_collection(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">patch_collection</a>(...) -> StacPydanticCollectionCollectionOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, PartialCollection

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.patch_collection(
    collection_id="collection_id",
    request=PartialCollection(),
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody` — Partial STAC Collection.
    
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

<details><summary><code>client.catalog_transaction_extension.<a href="src/fern/catalog_transaction_extension/client.py">create_item</a>(...) -> StacPydanticItemItemOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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
from fern import FernApi, ItemProperties, Asset, Link, ItemInputType
from fern.catalog_transaction_extension import CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_transaction_extension.create_item(
    collection_id="collection_id",
    request=CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature(
        geometry=None,
        properties=ItemProperties(
            datetime=None,
        ),
        id="id",
        assets={
            "key": Asset(
                href="href",
            )
        },
        links=[
            Link(
                href="href",
                rel="rel",
            )
        ],
        type=ItemInputType.FEATURE,
    ),
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

**collection_id:** `str` — Collection ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody` 
    
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

## CatalogFilterExtension
<details><summary><code>client.catalog_filter_extension.<a href="src/fern/catalog_filter_extension/client.py">queryables</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_filter_extension.queryables()

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

<details><summary><code>client.catalog_filter_extension.<a href="src/fern/catalog_filter_extension/client.py">collection_queryables</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_filter_extension.collection_queryables(
    collection_id="collection_id",
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

**collection_id:** `str` — Collection ID
    
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

## CatalogBulkTransactionExtension
<details><summary><code>client.catalog_bulk_transaction_extension.<a href="src/fern/catalog_bulk_transaction_extension/client.py">bulk_create_item</a>(...) -> BulkTransactionModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_bulk_transaction_extension.bulk_create_item(
    collection_id="collection_id",
    items={
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

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[BulkTransactionMethod]` 
    
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

## CatalogLivelinessReadiness
<details><summary><code>client.catalog_liveliness_readiness.<a href="src/fern/catalog_liveliness_readiness/client.py">ping_catalog_mgmt_ping_get</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Liveliness probe.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_liveliness_readiness.ping_catalog_mgmt_ping_get()

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

<details><summary><code>client.catalog_liveliness_readiness.<a href="src/fern/catalog_liveliness_readiness/client.py">health_catalog_mgmt_health_get</a>() -> HealthCheck</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PgSTAC HealthCheck.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.catalog_liveliness_readiness.health_catalog_mgmt_health_get()

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

## StagingService
<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">get_processes</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of all available processes from config.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.get_processes()

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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">get_resource</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Should return info about a specific resource.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.get_resource(
    resource="resource",
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

**resource:** `str` 
    
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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">execute_process</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to execute processing jobs.
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
from fern import FernApi, InputModel, ItemsModel

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.execute_process(
    resource="resource",
    inputs=InputModel(
        collection="collection",
        items=ItemsModel(),
    ),
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

**resource:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `InputModel` 
    
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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">get_job_status_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get status of processing job.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.get_job_status_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">delete_job_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific job from the database.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.delete_job_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">get_jobs_endpoint</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of all jobs.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.get_jobs_endpoint()

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

<details><summary><code>client.staging_service.<a href="src/fern/staging_service/client.py">get_specific_job_result_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get result from a specific job.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.staging_service.get_specific_job_result_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

## ProcessingService
<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">get_processes</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of all available processes from config.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.get_processes()

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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">get_resource</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Should return info about a specific resource.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.get_resource(
    resource="resource",
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

**resource:** `str` 
    
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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">execute_process</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to execute processing jobs.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.execute_process(
    resource="resource",
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

**resource:** `str` 
    
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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">get_job_logs_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to stream logs of a processing job.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.get_job_logs_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">get_job_status_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get status of processing job.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.get_job_status_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">delete_job_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific job from the database.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.delete_job_endpoint(
    job_id="job_id",
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

**job_id:** `typing.Any` 
    
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

<details><summary><code>client.processing_service.<a href="src/fern/processing_service/client.py">get_jobs_endpoint</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of all jobs from database.
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

client = FernApi(
    api_key="<value>",
    base_url="https://yourhost.com/path/to/api",
)

client.processing_service.get_jobs_endpoint()

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

