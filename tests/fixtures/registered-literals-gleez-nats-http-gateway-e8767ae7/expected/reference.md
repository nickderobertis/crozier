# Reference
## KvApi
<details><summary><code>client.kv_api.<a href="src/fern/kv_api/client.py">simple_kv_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.kv_api.simple_kv_get(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[float]` — the value of the key at the specified revision. Note the revision may not be available.
    
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

<details><summary><code>client.kv_api.<a href="src/fern/kv_api/client.py">simple_kv_create_entry</a>(...) -> int</code></summary>
<dl>
<dd>

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

client.kv_api.simple_kv_create_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
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

<details><summary><code>client.kv_api.<a href="src/fern/kv_api/client.py">simple_kv_put_entry</a>(...) -> int</code></summary>
<dl>
<dd>

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

client.kv_api.simple_kv_put_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**previous_revision:** `typing.Optional[int]` — the expected previous revision. If specified and the key is not at the specified revision the operation fails.
    
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

<details><summary><code>client.kv_api.<a href="src/fern/kv_api/client.py">simple_kv_delete_entry</a>(...)</code></summary>
<dl>
<dd>

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

client.kv_api.simple_kv_delete_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**purge:** `typing.Optional[bool]` — Purges the deleted entry
    
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

## KvManagementApi
<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">list_kv_stores</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

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

client.kv_management_api.list_kv_stores()

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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">kv_store_info</a>(...) -> KvStoreInfoResponse</code></summary>
<dl>
<dd>

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

client.kv_management_api.kv_store_info(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">add_kv_store</a>(...)</code></summary>
<dl>
<dd>

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

client.kv_management_api.add_kv_store(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_max_value_size:** `typing.Optional[float]` — the maximum size for an entry (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_history:** `typing.Optional[float]` — the number of possible history per key (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_ttl:** `typing.Optional[float]` — the amount of time entries live in the bucket in nanoseconds (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_max_bytes:** `typing.Optional[float]` — the maximum size of the KV in bytes (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_storage:** `typing.Optional[AddKvStoreRequestXNatsKvStorage]` — the underlying storage for the KV (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_replicas:** `typing.Optional[float]` — the underlying number of replicas (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**nats_kv_compression:** `typing.Optional[bool]` — compress the KV store (only on application/text)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_value_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_bytes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[AddKvStoreRequestStorage]` 
    
</dd>
</dl>

<dl>
<dd>

**replicas:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**compression:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">kv_store_destroy</a>(...)</code></summary>
<dl>
<dd>

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

client.kv_management_api.kv_store_destroy(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">kv_store_purge</a>(...)</code></summary>
<dl>
<dd>

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

client.kv_management_api.kv_store_purge(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">kv_store_keys</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

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

client.kv_management_api.kv_store_keys(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 
    
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

<details><summary><code>client.kv_management_api.<a href="src/fern/kv_management_api/client.py">kv_store_watch</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.kv_management_api.kv_store_watch(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[KvStoreWatchRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**ignore_deletes:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**resume_revision:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
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

## ExtendedKvEntryOperations
<details><summary><code>client.extended_kv_entry_operations.<a href="src/fern/extended_kv_entry_operations/client.py">kv_get_entry</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.extended_kv_entry_operations.kv_get_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[float]` — the value of the key at the specified revision. Note the revision may not be available.
    
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

<details><summary><code>client.extended_kv_entry_operations.<a href="src/fern/extended_kv_entry_operations/client.py">kv_create_entry</a>(...) -> int</code></summary>
<dl>
<dd>

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

client.extended_kv_entry_operations.kv_create_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
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

<details><summary><code>client.extended_kv_entry_operations.<a href="src/fern/extended_kv_entry_operations/client.py">kv_put_entry</a>(...) -> int</code></summary>
<dl>
<dd>

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

client.extended_kv_entry_operations.kv_put_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**previous_revision:** `typing.Optional[int]` — the expected previous revision. If specified and the key is not at the specified revision the operation fails.
    
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

<details><summary><code>client.extended_kv_entry_operations.<a href="src/fern/extended_kv_entry_operations/client.py">kv_delete_entry</a>(...)</code></summary>
<dl>
<dd>

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

client.extended_kv_entry_operations.kv_delete_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**purge:** `typing.Optional[bool]` — Purges the deleted entry
    
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

## ObjectStoreApi
<details><summary><code>client.object_store_api.<a href="src/fern/object_store_api/client.py">simple_obj_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.object_store_api.simple_obj_get(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**meta_only:** `typing.Optional[bool]` — if true, only the metadata of the object is returned, the body will not contain any data
    
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

<details><summary><code>client.object_store_api.<a href="src/fern/object_store_api/client.py">simple_obj_put_entry</a>(...)</code></summary>
<dl>
<dd>

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

client.object_store_api.simple_obj_put_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**meta_only:** `typing.Optional[bool]` — if true, only the metadata of the object is returned, the body will not contain any data
    
</dd>
</dl>

<dl>
<dd>

**previous_revision:** `typing.Optional[int]` — the expected previous revision. If specified and the key is not at the specified revision the operation fails.
    
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

<details><summary><code>client.object_store_api.<a href="src/fern/object_store_api/client.py">simple_obj_delete_entry</a>(...)</code></summary>
<dl>
<dd>

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

client.object_store_api.simple_obj_delete_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**meta_only:** `typing.Optional[bool]` — if true, only the metadata of the object is returned, the body will not contain any data
    
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

## ObjectStoreManagementApi
<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">objm_list</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

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

client.object_store_management_api.objm_list()

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

<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">objm_store_info</a>(...) -> ObjmStoreInfoResponse</code></summary>
<dl>
<dd>

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

client.object_store_management_api.objm_store_info(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">objm_store_add</a>(...)</code></summary>
<dl>
<dd>

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

client.object_store_management_api.objm_store_add(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_value_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_bytes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**storage:** `typing.Optional[ObjmStoreAddRequestStorage]` 
    
</dd>
</dl>

<dl>
<dd>

**replicas:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**compression:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
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

<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">objm_store_destroy</a>(...)</code></summary>
<dl>
<dd>

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

client.object_store_management_api.objm_store_destroy(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">obj_store_keys</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

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

client.object_store_management_api.obj_store_keys(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
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

<details><summary><code>client.object_store_management_api.<a href="src/fern/object_store_management_api/client.py">obj_store_watch</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.object_store_management_api.obj_store_watch(
    bucket="bucket",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ObjStoreWatchRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**ignore_deletes:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**resume_revision:** `typing.Optional[int]` 
    
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

## ObjectStoreEntryOperations
<details><summary><code>client.object_store_entry_operations.<a href="src/fern/object_store_entry_operations/client.py">obj_get_entry</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.object_store_entry_operations.obj_get_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
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

<details><summary><code>client.object_store_entry_operations.<a href="src/fern/object_store_entry_operations/client.py">obj_create_entry</a>(...) -> ObjCreateEntryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.object_store_entry_operations.obj_create_entry(...)
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

<details><summary><code>client.object_store_entry_operations.<a href="src/fern/object_store_entry_operations/client.py">obj_delete_entry</a>(...)</code></summary>
<dl>
<dd>

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

client.object_store_entry_operations.obj_delete_entry(
    bucket="bucket",
    key="key",
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

**bucket:** `str` — Bucket name
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key name
    
</dd>
</dl>

<dl>
<dd>

**purge:** `typing.Optional[bool]` — Purges the deleted entry
    
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

## NatsCoreMessagingExperimental
<details><summary><code>client.nats_core_messaging_experimental.<a href="src/fern/nats_core_messaging_experimental/client.py">subscribe</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

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

client.nats_core_messaging_experimental.subscribe(
    subject="subject",
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

**subject:** `str` — subject
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — how long to wait for a response in milliseconds. Default is 2000 milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — the maximum number of keys to return, note internally it is limited to 1000
    
</dd>
</dl>

<dl>
<dd>

**nats_h:** `typing.Optional[str]` — Header prefix - any HTTP request with a header that has the `NatsH-` prefix will have the prefix dropped, and have the header included on the published message.
    
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

<details><summary><code>client.nats_core_messaging_experimental.<a href="src/fern/nats_core_messaging_experimental/client.py">request</a>(...) -> RequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.nats_core_messaging_experimental.request(...)
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

**subject:** `str` — subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — how long to wait for a response in milliseconds. Default is 2000 milliseconds.
    
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

<details><summary><code>client.nats_core_messaging_experimental.<a href="src/fern/nats_core_messaging_experimental/client.py">publish</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.nats_core_messaging_experimental.publish(...)
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

**subject:** `str` — subject
    
</dd>
</dl>

<dl>
<dd>

**reply:** `str` — subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — how long to wait for a response in milliseconds. Default is 2000 milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — queue group for the subscription
    
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

