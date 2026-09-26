# Reference
## VectorOperationsV2
<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">delete</a>(...) -> HttpapiGenericRespCustomerDeleteResp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation deletes entities by their IDs or with a boolean expression.
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

client.vector_operations_v2.delete(
    collection_name="collectionName",
    filter="filter",
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

**collection_name:** `str` — The name of an existing collection.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 

A scalar filtering condition to filter matching entities.    The value defaults to an empty string, indicating that no condition applies. Setting both **id** and **filter** results in an error.
You can set this parameter to an empty string to skip scalar filtering. To build a scalar filtering condition, refer to [Boolean Expression Rules](https://milvus.io/docs/boolean.md). 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the target database.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `typing.Optional[str]` 

The name of a partition in the current collection. 
If specified, the data is to be deleted from the specified partition.
    
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

<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">insert</a>(...) -> HttpapiGenericRespCustomerInsertResp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation inserts data into a specific collection. You can insert a maximum of 100 entities at a time. To insert large volumes of data, please use [the bulk-insert API](https://docs.zilliz.com/docs/data-import).
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
from fern.vector_operations_v2 import PostV2VectordbEntitiesInsertRequestDataZero

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations_v2.insert(
    collection_name="collectionName",
    data=PostV2VectordbEntitiesInsertRequestDataZero(),
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

**collection_name:** `str` — The name of an existing collection.
    
</dd>
</dl>

<dl>
<dd>

**data:** `PostV2VectordbEntitiesInsertRequestData` 

The data to insert into the current collection.
The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries. 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the target database.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `typing.Optional[str]` 

The name of a partition in the current collection. 
If specified, the data is to be inserted into the specified partition.
    
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

<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">query</a>(...) -> PostV2VectordbEntitiesQueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation conducts a filtering on the scalar field with a specified boolean expression.
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

client.vector_operations_v2.query(
    collection_name="collectionName",
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

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter used to find matches for the search.
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the search results.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies.
    
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

<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">upsert</a>(...) -> HttpapiGenericRespCustomerUpsertResp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation inserts new records into the database or updates existing ones.  Currently, this endpoint does not apply to the collections that have autoId enabled.
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
from fern.vector_operations_v2 import PostV2VectordbEntitiesUpsertRequestDataZero

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations_v2.upsert(
    collection_name="collectionName",
    data=PostV2VectordbEntitiesUpsertRequestDataZero(),
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

**collection_name:** `str` — The name of the collection in which to upsert data.
    
</dd>
</dl>

<dl>
<dd>

**data:** `PostV2VectordbEntitiesUpsertRequestData` 

The data to insert into the current collection. 
The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `typing.Optional[str]` 

The name of a partition in the current collection. 
If specified, the data is to be inserted into the specified partition.
    
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

<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">get</a>(...) -> PostV2VectordbEntitiesGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation gets specific entities by their IDs.
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

client.vector_operations_v2.get(
    collection_name="collectionName",
    id=1,
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

**id:** `PostV2VectordbEntitiesGetRequestId` — A specific entity ID or a list of entity IDs.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the search results.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies.
    
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

<details><summary><code>client.vector_operations_v2.<a href="src/fern/vector_operations_v2/client.py">search</a>(...) -> PostV2VectordbEntitiesSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation conducts a vector similarity search with an optional scalar filtering expression.
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
from fern import FernApi, SearchParams

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.vector_operations_v2.search(
    collection_name="collectionName",
    vector=[
        [
            1
        ]
    ],
    search_params=SearchParams(),
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

**vector:** `typing.List[Vector]` 

A list of vector embeddings.
<include target="milvus">Milvus</include><include target="zilliz">Zilliz Cloud</include> searches for the most similar vector embeddings to the specified ones.
    
</dd>
</dl>

<dl>
<dd>

**search_params:** `SearchParams` 

 The parameter settings specific to this operation.
- **metric_type** (*str*) -
  -   The metric type applied to this operation. This should be the same as the one used when you index the vector field specified above. 
  -   Possible values are **L2**, **IP**, and **COSINE**.
- **params** (dict) -
  -   Additional parameters
  - **radius** (float) -
    -    Determines the threshold of least similarity. When setting `metric_type` to `L2`, ensure that this value is greater than that of **range_filter**. Otherwise, this value should be lower than that of **range_filter**. 
  - **range_filter**  (float) -  
    -    Refines the search to vectors within a specific similarity range. When setting `metric_type` to `IP` or `COSINE`, ensure that this value is greater than that of **radius**. Otherwise, this value should be lower than that of **radius**. 
<include target="milvus">
For details on other applicable search parameters, refer to [In-memory Index](https://milvus.io/docs/index.md) and [On-disk Index](https://milvus.io/docs/disk_index.md).
</include>
<include target="zilliz">
For details on other applicable search parameters, read [AUTOINDEX Explained](https://docs.zilliz.com/docs/autoindex-explained) to get more.
</include>
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**anns_field:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter used to find matches for the search.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The total number of entities to return.
You can use this parameter in combination with **offset** in **param** to enable pagination.
The sum of this value and **offset** in **param** should be less than 16,384. 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` —     The number of records to skip in the search result.      You can use this parameter in combination with limit to enable pagination.     The sum of this value and limit should be less than 16,384. 
    
</dd>
</dl>

<dl>
<dd>

**grouping_field:** `typing.Optional[str]` — https://zilliverse.feishu.cn/docx/S3brdwmUHoG33dxhifpcruAYnsb
    
</dd>
</dl>

<dl>
<dd>

**output_fields:** `typing.Optional[typing.List[str]]` — An array of fields to return along with the search results.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[typing.List[str]]` — The name of the partitions to which this operation applies.
    
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

## CollectionOperationsV2
<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">has_collection</a>(...) -> Has</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation checks whether a collection exists.
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

client.collection_operations_v2.has_collection(
    db_name="dbName",
    collection_name="collectionName",
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

**db_name:** `str` — The name of the database in which to check the existence of a collection.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — The name of an existing collection.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">rename_collection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation renames an existing collection and optionally moves the collection to a new database.
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

client.collection_operations_v2.rename_collection(
    collection_name="collectionName",
    new_collection_name="newCollectionName",
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

**collection_name:** `str` 

The name of the target collection.
Setting this to a non-existing collection results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**new_collection_name:** `str` 

The name of the target collection after this operation.
Setting this to the value of **old_collection_name** results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` 

The name of the database to which the collection belongs.
Setting this to a non-existing database results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**new_db_name:** `typing.Optional[str]` 

The name of the database to which the collection belongs after this operation.
The value defaults to **default**. Setting this to a database rather than the one the collection belongs to before this operation moves this collection to the specified database.
Setting this to a non-existing database results in a **MilvusException**.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">get_collection_stats</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operations gets the number of entities in a collection.
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

client.collection_operations_v2.get_collection_stats(
    db_name="dbName",
    collection_name="collectionName",
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

**db_name:** `str` — The name of the database which the collection belongs to. Setting this to a non-existing database results in an error.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` 

The name of the collection to check.
Setting this to a non-existing database results in an error.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">load_collection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation loads the data of the current collection into memory. 
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

client.collection_operations_v2.load_collection(
    request_header=1,
    collection_name="collectionName",
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

**request_header:** `int` — The timeout duration for this operation in seconds. Setting this to None indicates that this operation timeouts when any response arrives or any error occurs.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CollectionName` 
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">release_collection</a>(...) -> PostV2VectordbCollectionsReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation releases the data of the current collection from memory.
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

client.collection_operations_v2.release_collection(
    collection_name="collectionName",
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

**collection_name:** `str` 

The name of the target colletion.
Setting this to a non-existing collection results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` 

The name of the database to which the cpllection belongs.
Setting this to a non-existing database results in a **MilvusException**.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">create_collection</a>(...) -> HttpapiGenericRespCustomerCreateIndexResp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates a collection in a specified cluster.
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

client.collection_operations_v2.create_collection(
    auto_id="autoID",
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

**auto_id:** `str` — Whether the primary field automatically increments. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database. <zilliz>This parameter applies only to dedicated clusters.</zilliz>
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `typing.Optional[str]` — The name of the collection to create.
    
</dd>
</dl>

<dl>
<dd>

**dimension:** `typing.Optional[int]` 

The number of dimensions a vector value should have.
This is required if **dtype** of this field is set to **DataType.FLOAT_VECTOR**.
    
</dd>
</dl>

<dl>
<dd>

**metric_type:** `typing.Optional[str]` 

The metric type applied to this operation. 
Possible values are **L2**, **IP**, and **COSINE**.
    
</dd>
</dl>

<dl>
<dd>

**id_type:** `typing.Optional[str]` — The data type of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
    
</dd>
</dl>

<dl>
<dd>

**primary_field_name:** `typing.Optional[str]` — The name of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
    
</dd>
</dl>

<dl>
<dd>

**vector_field_name:** `typing.Optional[str]` — The name of the vector field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[CollectionSchema]` — The schema is responsible for organizing data in the target collection. A valid schema should have multiple fields, which must include a primary key, a vector field, and several scalar fields.
    
</dd>
</dl>

<dl>
<dd>

**index_params:** `typing.Optional[typing.List[IndexParam]]` — The parameters that apply to the index-building process.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[CollectionParams]` — Extra parameters for the collection.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">get_collection_load_state</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation returns the load status of a specific collection.
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

client.collection_operations_v2.get_collection_load_state(
    collection_name="collectionName",
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

**collection_name:** `str` — The name of a collection.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of a database to which the collection belongs.
    
</dd>
</dl>

<dl>
<dd>

**partition_names:** `typing.Optional[str]` — A list of partition names. If any partition names are specified, releasing any of these partitions results in the return of a NotLoad state.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">list_collections</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists all collections in the database used in the current connection.
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

client.collection_operations_v2.list_collections(
    db_name="dbName",
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

**db_name:** `str` — The name of an existing database.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">describe_collection</a>(...) -> PostV2VectordbCollectionsDescribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describes the details of a collection.
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

client.collection_operations_v2.describe_collection(
    db_name="dbName",
    collection_name="collectionName",
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

**db_name:** `str` — The name of the database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — The name of the collection to describe.
    
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

<details><summary><code>client.collection_operations_v2.<a href="src/fern/collection_operations_v2/client.py">drop_collection</a>(...) -> HttpapiGenericRespCustomerDropCollectionResp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation drops the current collection and all data within the collection.
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

client.collection_operations_v2.drop_collection(
    collection_name="collectionName",
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

**request:** `CollectionName` 
    
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

## PartitionOperationsV2
<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">list_partitions</a>(...) -> PostV2VectordbPartitionsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists all partitions in the database used in the current connection.
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

client.partition_operations_v2.list_partitions(
    db_name="dbName",
    collection_name="collectionName",
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

**db_name:** `str` — The name of the target database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — The name of the target collection to which the partition belongs.
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">create_partition</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates a partition in a collection. 
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

client.partition_operations_v2.create_partition(
    collection_name="collectionName",
    partition_name="partitionName",
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

**request:** `PartitionName` 
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">drop_partition</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation drops the current partition. 
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

client.partition_operations_v2.drop_partition(
    collection_name="collectionName",
    partition_name="partitionName",
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

**request:** `PartitionName` 
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">load_partitions</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation loads the data of the current partition into memory.
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

client.partition_operations_v2.load_partitions(
    collection_name="collectionName",
    partition_names=[
        "partitionNames",
        "partitionNames"
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

**request:** `PartitionNames` 
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">release_partitions</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation releases the data of the current partition from memory.
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

client.partition_operations_v2.release_partitions(
    collection_name="collectionName",
    partition_names=[
        "partitionNames",
        "partitionNames"
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

**request:** `PartitionNames` 
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">has_partition</a>(...) -> Has</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation checks whether a partition exists.
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

client.partition_operations_v2.has_partition(
    collection_name="collectionName",
    partition_name="partitionName",
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

**collection_name:** `str` — The name of an existing collection.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `str` — The name of the partition to test.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of an existing database. The value defaults to __default__.
    
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

<details><summary><code>client.partition_operations_v2.<a href="src/fern/partition_operations_v2/client.py">get_partition_statistics</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operations gets the number of entities in a partition.
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

client.partition_operations_v2.get_partition_statistics(
    collection_name="collectionName",
    partition_name="partitionName",
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

**collection_name:** `str` — The name of an existing collection.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `str` — The name of the target partition of this operation. 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of an existing database. The value defaults to __default__.
    
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

## UserOperationsV2
<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">create_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates a new user with a corresponding password.
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

client.user_operations_v2.create_user(
    user_name="userName",
    password="password",
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

**user_name:** `str` — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 

The corresponding password to the new user to create. 
The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.
    
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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">update_user_password</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation updates the password for a specific user.
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

client.user_operations_v2.update_user_password(
    user_name="userName",
    password="password",
    new_password="newPassword",
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

**user_name:** `str` — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 

The corresponding password to the new user to create. 
The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.
    
</dd>
</dl>

<dl>
<dd>

**new_password:** `str` — The new password for the specified user.    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.
    
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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">drop_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation deletes an existing user.
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

client.user_operations_v2.drop_user(
    user_name="userName",
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

**user_name:** `str` — The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
    
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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">describe_user</a>(...) -> PostV2VectordbUsersDescribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation describes the detailed information of a specific user.
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

client.user_operations_v2.describe_user(
    user_name="userName",
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

**user_name:** `str` —   The name of the user to describe.
    
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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">list_users</a>() -> PostV2VectordbUsersListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists the information of all existing users.
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

client.user_operations_v2.list_users()

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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">grant_role_to_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.
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

client.user_operations_v2.grant_role_to_user(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

<details><summary><code>client.user_operations_v2.<a href="src/fern/user_operations_v2/client.py">revoker_role_from_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation revokes a privilege granted to the current role.
> Notes
> To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).
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

client.user_operations_v2.revoker_role_from_user(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

## RoleOperationsV2
<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">list_roles</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists the information about all existing roles.
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

client.role_operations_v2.list_roles()

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

<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">describe_role</a>(...) -> Privileges</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation describes the details of a specified role.
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

client.role_operations_v2.describe_role(
    role_name="roleName",
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

**request:** `RoleName` 
    
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

<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">create_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates the current role. 
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

client.role_operations_v2.create_role(
    role_name="roleName",
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

**request:** `RoleName` 
    
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

<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">drop_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation drops an existing role. The operation will succeed if the specified role exists. Otherwise, this operation will fail.
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

client.role_operations_v2.drop_role(
    role_name="roleName",
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

**request:** `RoleName` 
    
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

<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">grant_privilege_to_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation grants a privilege to the current role.
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

client.role_operations_v2.grant_privilege_to_role(
    role_name="roleName",
    object_type="objectType",
    object_name="objectName",
    privilege="privilege",
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

**role_name:** `str` — The name of the role.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `str` —  The type of the object to which the privilege belongs.
    
</dd>
</dl>

<dl>
<dd>

**object_name:** `str` —  The name of the object to which the role is granted the specified privilege.
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` —  The privilege that is granted to the role.
    
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

<details><summary><code>client.role_operations_v2.<a href="src/fern/role_operations_v2/client.py">revoke_privilege_from_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation revokes a privilege granted to the current role.
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

client.role_operations_v2.revoke_privilege_from_role(
    role_name="roleName",
    object_type="objectType",
    object_name="objectName",
    privilege="privilege",
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

**role_name:** `str` — The name of the role.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `str` — The type of the object to which the privilege belongs.
    
</dd>
</dl>

<dl>
<dd>

**object_name:** `str` — The name of the object to which the role is granted the specified privilege.
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` — The privilege that is granted to the role.
    
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

## IndexOperationsV2
<details><summary><code>client.index_operations_v2.<a href="src/fern/index_operations_v2/client.py">create_index</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This creates a named index for a target field, which can either be a vector field or a scalar field.
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
from fern import FernApi, IndexParam

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.index_operations_v2.create_index(
    collection_name="collectionName",
    index_params=[
        IndexParam(
            metric_type="metricType",
            field_name="fieldName",
            index_name="indexName",
        ),
        IndexParam(
            metric_type="metricType",
            field_name="fieldName",
            index_name="indexName",
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

**collection_name:** `str` 

The name of the target collection.
Setting this to a non-existing collection results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**index_params:** `typing.List[IndexParam]` —   The parameters that apply to the index-building process.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` 

The name of the database to which the collection belongs.
Setting this to a non-existing database results in a **MilvusException**.
    
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

<details><summary><code>client.index_operations_v2.<a href="src/fern/index_operations_v2/client.py">drop_index</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation deletes index from a specified collection.
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

client.index_operations_v2.drop_index(
    collection_name="collectionName",
    index_name="indexName",
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

**collection_name:** `str` 

The name of the target collection.
Setting this to a non-existing collection results in a **MilvusException**.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — The name fo the target index.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` 

The name of the database to which the collection belongs.
Setting this to a non-existing database results in a **MilvusException**.
    
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

<details><summary><code>client.index_operations_v2.<a href="src/fern/index_operations_v2/client.py">describe_index</a>(...) -> PostV2VectordbIndexesDescribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation describes the current index.
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

client.index_operations_v2.describe_index(
    collection_name="collectionName",
    index_name="indexName",
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

**collection_name:** `str` — The name of an the collection to which the index belongs.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — The name of the index to describe.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database to which the collection belongs.
    
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

<details><summary><code>client.index_operations_v2.<a href="src/fern/index_operations_v2/client.py">list_indexes</a>(...) -> PostV2VectordbIndexesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists all indexes of a specific collection.
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

client.index_operations_v2.list_indexes(
    db_name="dbName",
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

**db_name:** `str` — The name of the database to which the collection belongs.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `typing.Optional[str]` — The name of an existing collection. Setting this to a non-existing collection leads to an error.
    
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

## AliasOperationsV2
<details><summary><code>client.alias_operations_v2.<a href="src/fern/alias_operations_v2/client.py">list_aliases</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation lists all existing collection aliases.
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

client.alias_operations_v2.list_aliases(
    db_name="dbName",
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

**db_name:** `str` — The name of an existing database. The value defaults to __default__.
    
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

<details><summary><code>client.alias_operations_v2.<a href="src/fern/alias_operations_v2/client.py">describe_alias</a>(...) -> PostV2VectordbAliasesDescribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation describes the details of a specific alias.
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

client.alias_operations_v2.describe_alias(
    db_name="dbName",
    alias_name="aliasName",
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

**db_name:** `str` — The name of the database to which the collection belongs.
    
</dd>
</dl>

<dl>
<dd>

**alias_name:** `str` — The name of the alias whose details are to be listed.
    
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

<details><summary><code>client.alias_operations_v2.<a href="src/fern/alias_operations_v2/client.py">alter_alias</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation reassigns the alias of one collection to another.
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

client.alias_operations_v2.alter_alias(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

<details><summary><code>client.alias_operations_v2.<a href="src/fern/alias_operations_v2/client.py">drop_alias</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation drops a specified alias. 
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

client.alias_operations_v2.drop_alias(
    collection_name="collectionName",
    alias_name="aliasName",
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

**collection_name:** `str` — The name of the collection to which the alias is assigned to.
    
</dd>
</dl>

<dl>
<dd>

**alias_name:** `str` 

The alias to drop.
When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `typing.Optional[str]` — The name of the database to which the collection belongs.
    
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

<details><summary><code>client.alias_operations_v2.<a href="src/fern/alias_operations_v2/client.py">create_alias</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates an alias for an existing collection.
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

client.alias_operations_v2.create_alias(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

