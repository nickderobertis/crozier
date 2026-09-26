# Reference
## VectorOperations
<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">delete</a>(...) -> PostV1VectorDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one or more entities from a collection.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.delete(
    db_name="default",
    collection_name="my_collection",
    id="4321034832910",
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

**collection_name:** `str` — The name of the collection to which this operation applies.
    
</dd>
</dl>

<dl>
<dd>

**id:** `PostV1VectorDeleteRequestId` 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
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

<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">insert</a>(...) -> PostV1VectorInsertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inserts one or more entities into a collection. You can add a maximum of 100 entities at a time. To insert large volumn of data, you are advised to use the bulk-insert API. For details, refer to [Data Import](/docs/data-import).
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
from fern.vector_operations import PostV1VectorInsertRequestDataZero

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.insert(
    collection_name="my_collection",
    data=PostV1VectorInsertRequestDataZero(),
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

**collection_name:** `str` — The name of the collection to which entities will be inserted.
    
</dd>
</dl>

<dl>
<dd>

**data:** `PostV1VectorInsertRequestData` — An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `typing.Optional[str]` — The name of the partition to which this operation applies.
    
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

<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">upsert</a>(...) -> PostV1VectorUpsertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upserts one or more entities into a collection.
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
from fern.vector_operations import PostV1VectorUpsertRequestDataZero

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.upsert(
    collection_name="quick_setup",
    data=PostV1VectorUpsertRequestDataZero(),
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

**collection_name:** `str` — The name of the collection to which entities will be upserted.
    
</dd>
</dl>

<dl>
<dd>

**data:** `PostV1VectorUpsertRequestData` — An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
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

<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">search</a>(...) -> PostV1VectorSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Conducts a similarity search on the vector field in a collection. 
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.search(
    collection_name="quick_setup",
    limit=3,
    output_fields=[
        "color"
    ],
    vector=[
        1.1
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

**collection_name:** `str` — The name of the collection to which this operation applies.
    
</dd>
</dl>

<dl>
<dd>

**vector:** `typing.List[float]` — The query vector in the form of a list of floating numbers. The length of the query vector should match the dimension of the vector field in the collection.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies. Setting this parameter indicates that the search scope should be limited to the specified partitions. If not specified, the search scope is the entire collection.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter used to find matches for the search
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of entities to return.
The sum of this value of that of `offset` should be less than **16,384**.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of entities to skip in the search results.<br>The sum of this value and that of `limit` should not be greater than **16,384**.
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the search results.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[PostV1VectorSearchRequestParams]` — List of search parameters
    
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

<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">query</a>(...) -> PostV1VectorQueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Conducts a query on scalar fields in a collection.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.query(
    collection_name="medium_articles",
    filter="id in [443300716234671427, 443300716234671426]",
    limit=100,
    offset=0,
    output_fields=[
        "id",
        "title",
        "link"
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

**collection_name:** `str` — The name of the collection to which this operation applies.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — The filter used to find matches for the query.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of entities to return.<br/>The sum of this value and that of `offset` should be less than **16384**.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of entities to skip in the search results.<br/>The sum of this value and that of `limit` should be less than **16384**.
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the search results. When setting this to `count(*)`, you need to set `limit` to 0 to get the total count of the entities that match the filter.
    
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

<details><summary><code>client.vector_operations.<a href="src/fern/vector_operations/client.py">get</a>(...) -> PostV1VectorGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets entities by the specified IDs. You can set an ID in string or integer or set a set of IDs in a list of strings or a list of integers as shown in the four types of request bodies below.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations.get(
    collection_name="quick_setup",
    output_fields=[
        "color"
    ],
    id=[
        1,
        3,
        5
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

**collection_name:** `str` — The name of the collection to which this operation applies.
    
</dd>
</dl>

<dl>
<dd>

**id:** `PostV1VectorGetRequestId` 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies. Setting this indicates that the operation should be applied to only these partitions. If not set, the operation will be applied to all partitions in the collection.
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the query results.
    
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

