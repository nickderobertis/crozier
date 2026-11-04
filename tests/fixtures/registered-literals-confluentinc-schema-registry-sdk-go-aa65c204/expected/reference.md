# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_dek_subjects</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_dek_subjects(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_dek</a>(...) -> Dek</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.create_dek(...)
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The create request
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_kek_names</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_kek_names()

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

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_kek</a>(...) -> Kek</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.create_kek(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The create request
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_kek</a>(...) -> Kek</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_kek(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">put_kek</a>(...) -> Kek</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.put_kek(...)
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The update request
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_kek</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_kek(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**permanent:** `typing.Optional[bool]` — Whether to perform a permanent delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_dek</a>(...) -> Dek</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_dek(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[GetDekRequestAlgorithm]` — Algorithm of the dek
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_dek_versions</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_dek_versions(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[DeleteDekVersionsRequestAlgorithm]` — Algorithm of the dek
    
</dd>
</dl>

<dl>
<dd>

**permanent:** `typing.Optional[bool]` — Whether to perform a permanent delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_dek_by_version</a>(...) -> Dek</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_dek_by_version(
    name="name",
    subject="subject",
    version="version",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[GetDekByVersionRequestAlgorithm]` — Algorithm of the dek
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_dek_version</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_dek_version(
    name="name",
    subject="subject",
    version="version",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[DeleteDekVersionRequestAlgorithm]` — Algorithm of the dek
    
</dd>
</dl>

<dl>
<dd>

**permanent:** `typing.Optional[bool]` — Whether to perform a permanent delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_dek_versions</a>(...) -> typing.List[int]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_dek_versions(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[GetDekVersionsRequestAlgorithm]` — Algorithm of the dek
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted keys
    
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

<details><summary><code>client.<a href="src/fern/client.py">undelete_dek_version</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.undelete_dek_version(
    name="name",
    subject="subject",
    version="version",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[UndeleteDekVersionRequestAlgorithm]` — Algorithm of the dek
    
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

<details><summary><code>client.<a href="src/fern/client.py">undelete_dek_versions</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.undelete_dek_versions(
    name="name",
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

**name:** `str` — Name of the kek
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the dek
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `typing.Optional[UndeleteDekVersionsRequestAlgorithm]` — Algorithm of the dek
    
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

<details><summary><code>client.<a href="src/fern/client.py">undelete_kek</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.undelete_kek(
    name="name",
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

**name:** `str` — Name of the kek
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_business_metadata</a>(...) -> typing.List[BusinessMetadataResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk API to create multiple business metadata.
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
from fern import FernApi, BusinessMetadata
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.create_business_metadata(
    request=[
        BusinessMetadata(
            type_name="typeName",
            attributes={
                "key": "{}"
            },
            entity_type="entityType",
            entity_name="entityName",
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

**request:** `typing.List[BusinessMetadata]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_business_metadata</a>(...) -> typing.List[BusinessMetadataResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk API to update multiple business metadata.
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
from fern import FernApi, BusinessMetadata
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.update_business_metadata(
    request=[
        BusinessMetadata(
            type_name="typeName",
            attributes={
                "key": "{}"
            },
            entity_type="entityType",
            entity_name="entityName",
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

**request:** `typing.List[BusinessMetadata]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get</a>() -> typing.Dict[str, GetResponseValue]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Root resource is a no-op.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get()

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

<details><summary><code>client.<a href="src/fern/client.py">post</a>() -> typing.Dict[str, str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.post()

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

<details><summary><code>client.<a href="src/fern/client.py">test_compatibility_for_subject</a>(...) -> CompatibilityCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).
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
client.test_compatibility_for_subject(...)
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

**subject:** `str` — Subject of the schema version against which compatibility is to be tested
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Schema
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">test_compatibility_by_subject_name</a>(...) -> CompatibilityCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

the compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config).
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
client.test_compatibility_by_subject_name(...)
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

**subject:** `str` — Subject of the schema version against which compatibility is to be tested
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the subject's schema against which compatibility is to be tested. Valid values for versionId are between [1,2^31-1] or the string "latest"."latest" checks compatibility of the input schema with the last registered schema under the specified subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Schema
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_top_level_config</a>() -> Config</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the global compatibility level.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_top_level_config()

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

<details><summary><code>client.<a href="src/fern/client.py">update_top_level_config</a>(...) -> ConfigUpdateRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the global compatibility level. On success, echoes the original request back to the client.
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
client.update_top_level_config(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Config Update Request
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_top_level_config</a>() -> DeleteTopLevelConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the global compatibility level config and reverts to the default.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_top_level_config()

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

<details><summary><code>client.<a href="src/fern/client.py">get_subject_level_config</a>(...) -> Config</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_subject_level_config(
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

**subject:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**default_to_global:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_subject_level_config</a>(...) -> ConfigUpdateRequest</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.update_subject_level_config(...)
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Config Update Request
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_subject_config</a>(...) -> DeleteSubjectConfigResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_subject_config(
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

**subject:** `str` — the name of the subject
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_contexts</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list_contexts()

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

**context_prefix:** `typing.Optional[str]` — prefix to filter contexts
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_top_level_mode</a>() -> Mode</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_top_level_mode()

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

<details><summary><code>client.<a href="src/fern/client.py">update_top_level_mode</a>(...) -> ModeUpdateRequest</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.update_top_level_mode(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Update Request
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_mode</a>(...) -> DeleteModeResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_mode()

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

**recursive:** `typing.Optional[bool]` — recursive delete mode across all subjects.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_mode</a>(...) -> Mode</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_mode(
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**default_to_global:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_mode</a>(...) -> ModeUpdateRequest</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.update_mode(...)
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Update Request
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_subject_mode</a>(...) -> DeleteSubjectModeResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_subject_mode(
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

**subject:** `str` — the name of the subject
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[bool]` — recursive delete mode for all subjects under the context if subject parameter is a context
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_schemas</a>(...) -> typing.List[Schema]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_schemas()

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

**subject_prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**latest_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_schema</a>(...) -> SchemaString</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_schema(
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

**id:** `int` — Globally unique identifier of the schema
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fetch_max_id:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_subjects</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_subjects(
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

**id:** `int` — Globally unique identifier of the schema
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_versions</a>(...) -> typing.List[SubjectVersion]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_versions(
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

**id:** `int` — Globally unique identifier of the schema
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_schema_types</a>() -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_schema_types()

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

<details><summary><code>client.<a href="src/fern/client.py">list</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list()

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

**subject_prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted_only:** `typing.Optional[bool]` — Whether to return deleted subjects only
    
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

<details><summary><code>client.<a href="src/fern/client.py">look_up_schema_under_subject</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.look_up_schema_under_subject(...)
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

**subject:** `str` — Subject under which the schema will be registered
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Schema
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Desired output format, dependent on schema type
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_subject</a>(...) -> typing.List[int]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_subject(
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

**subject:** `str` — the name of the subject
    
</dd>
</dl>

<dl>
<dd>

**permanent:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_versions</a>(...) -> typing.List[int]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list_versions(
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted_only:** `typing.Optional[bool]` — Whether to return deleted schemas only
    
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

<details><summary><code>client.<a href="src/fern/client.py">register</a>(...) -> RegisterSchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new schema under the specified subject. If successfully registered, this returns the unique identifier of this schema in the registry. The returned identifier should be used to retrieve this schema from the schemas resource and is different from the schema's version which is associated with the subject. If the same schema is registered under a different subject, the same identifier will be returned. However, the version of the schema may be different under different subjects.
A schema should be compatible with the previously registered schema or schemas (if there are any) as per the configured compatibility level. The configured compatibility level can be obtained by issuing a GET http:get:: /config/(string: subject). If that returns null, then GET http:get:: /config
When there are multiple instances of Schema Registry running in the same cluster, the schema registration request will be forwarded to one of the instances designated as the primary. If the primary is not available, the client will get an error code indicating that the forwarding has failed.
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
client.register(...)
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

**subject:** `str` — Name of the subject
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Schema
    
</dd>
</dl>

<dl>
<dd>

**normalize:** `typing.Optional[bool]` — Whether to register the normalized schema
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Desired output format, dependent on schema type
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_schema_by_version</a>(...) -> Schema</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_schema_by_version(
    subject="subject",
    version="version",
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Desired output format, dependent on schema type
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_schema_version</a>(...) -> int</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_schema_version(
    subject="subject",
    version="version",
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    
</dd>
</dl>

<dl>
<dd>

**permanent:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_referenced_by</a>(...) -> typing.List[int]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_referenced_by(
    subject="subject",
    version="version",
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_schema_only</a>(...) -> str</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_schema_only(
    subject="subject",
    version="version",
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

**subject:** `str` — Name of the Subject
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string "latest". "latest" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Desired output format, dependent on schema type
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_cluster_id</a>() -> ServerClusterId</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_cluster_id()

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

<details><summary><code>client.<a href="src/fern/client.py">get_exporters</a>() -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_exporters()

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

<details><summary><code>client.<a href="src/fern/client.py">create_exporter</a>(...) -> CreateExporterResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.create_exporter(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Info
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_exporter_info</a>(...) -> ExporterInfo</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_exporter_info(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">put_exporter</a>(...) -> UpdateExporterResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.put_exporter(...)
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

**name:** `str` — Name of the exporter
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Info
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_exporter</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_exporter(
    name="name",
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

**name:** `str` — Name of the exporter
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_exporter_config</a>(...) -> typing.Dict[str, str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_exporter_config(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">put_exporter_config</a>(...) -> UpdateExporterResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.put_exporter_config(...)
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

**name:** `str` — Name of the exporter
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Config
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_exporter_cluster_link_config</a>(...) -> typing.Dict[str, str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_exporter_cluster_link_config(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">pause_exporter</a>(...) -> UpdateExporterResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.pause_exporter(
    name="name",
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

**name:** `str` — Name of the exporter
    
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

<details><summary><code>client.<a href="src/fern/client.py">reset_exporter</a>(...) -> UpdateExporterResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reset_exporter(
    name="name",
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

**name:** `str` — Name of the exporter
    
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

<details><summary><code>client.<a href="src/fern/client.py">resume_exporter</a>(...) -> UpdateExporterResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.resume_exporter(
    name="name",
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

**name:** `str` — Name of the exporter
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_exporter_status</a>(...) -> ExporterStatus</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_exporter_status(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_tags</a>(...) -> typing.List[TagResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk API to create multiple tags.
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
from fern import FernApi, Tag, TagEntityStatus, TimeBoundary
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.create_tags(
    request=[
        Tag(
            type_name="typeName",
            attributes={
                "key": {
                    "key": "value"
                }
            },
            entity_guid="entityGuid",
            entity_status=TagEntityStatus.ACTIVE,
            propagate=True,
            validity_periods=[
                TimeBoundary(
                    start_time="startTime",
                    end_time="endTime",
                    time_zone="timeZone",
                ),
                TimeBoundary(
                    start_time="startTime",
                    end_time="endTime",
                    time_zone="timeZone",
                )
            ],
            remove_propagations_on_entity_delete=True,
            entity_type="entityType",
            entity_name="entityName",
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

**request:** `typing.List[Tag]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_tags</a>(...) -> typing.List[TagResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk API to update multiple tags.
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
from fern import FernApi, Tag, TagEntityStatus, TimeBoundary
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.update_tags(
    request=[
        Tag(
            type_name="typeName",
            attributes={
                "key": {
                    "key": "value"
                }
            },
            entity_guid="entityGuid",
            entity_status=TagEntityStatus.ACTIVE,
            propagate=True,
            validity_periods=[
                TimeBoundary(
                    start_time="startTime",
                    end_time="endTime",
                    time_zone="timeZone",
                ),
                TimeBoundary(
                    start_time="startTime",
                    end_time="endTime",
                    time_zone="timeZone",
                )
            ],
            remove_propagations_on_entity_delete=True,
            entity_type="entityType",
            entity_name="entityName",
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

**request:** `typing.List[Tag]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_business_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a business metadata on an entity.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_business_metadata(
    type_name="typeName",
    qualified_name="qualifiedName",
    bm_name="bmName",
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

**type_name:** `str` — The type of the entity
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` — The qualified name of the entity
    
</dd>
</dl>

<dl>
<dd>

**bm_name:** `str` — The name of the business metadata
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tag on an entity.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_tag(
    type_name="typeName",
    qualified_name="qualifiedName",
    tag_name="tagName",
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

**type_name:** `str` — The type of the entity
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` — The qualified name of the entity
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `str` — The name of the tag
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_business_metadata</a>(...) -> typing.List[BusinessMetadataResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the list of business metadata for a given entity represented by a qualified name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_business_metadata(
    type_name="typeName",
    qualified_name="qualifiedName",
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

**type_name:** `str` — The type of the entity
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` — The qualified name of the entity
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_by_unique_attributes</a>(...) -> AtlasEntityWithExtInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch complete definition of an entity given its type and unique attribute.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_by_unique_attributes(
    type_name="typeName",
    qualified_name="qualifiedName",
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

**type_name:** `str` — The type of the entity
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` — The qualified name of the entity
    
</dd>
</dl>

<dl>
<dd>

**min_ext_info:** `typing.Optional[bool]` — Whether to only populate header and schema attributes
    
</dd>
</dl>

<dl>
<dd>

**ignore_relationships:** `typing.Optional[bool]` — Whether to ignore relationships
    
</dd>
</dl>

<dl>
<dd>

**include_internal_prefix:** `typing.Optional[str]` — If not null, include internal attributes that start with this prefix
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_by_unique_attributes</a>(...) -> typing.Any</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_by_unique_attributes(
    type_name="typeName",
    qualified_name="qualifiedName",
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

**type_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_tags</a>(...) -> typing.List[TagResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the list of classifications for a given entity represented by a qualifed name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_tags(
    type_name="typeName",
    qualified_name="qualifiedName",
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

**type_name:** `str` — The type of the entity
    
</dd>
</dl>

<dl>
<dd>

**qualified_name:** `str` — The qualified name of the entity
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_or_update</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AtlasEntity, AtlasEntityStatus, AtlasClassification, AtlasClassificationEntityStatus, TimeBoundary, AtlasTermAssignmentHeader, AtlasTermAssignmentHeaderStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.create_or_update(
    referred_entities={
        "key": AtlasEntity(
            type_name="typeName",
            attributes={
                "key": "{}"
            },
            guid="guid",
            home_id="homeId",
            is_proxy=True,
            is_incomplete=True,
            provenance_type=0,
            status=AtlasEntityStatus.ACTIVE,
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=1000000,
            update_time=1000000,
            version=6,
            relationship_attributes={
                "key": "{}"
            },
            classifications=[
                AtlasClassification(
                    type_name="typeName",
                    attributes={
                        "key": {
                            "key": "value"
                        }
                    },
                    entity_guid="entityGuid",
                    entity_status=AtlasClassificationEntityStatus.ACTIVE,
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        )
                    ],
                    remove_propagations_on_entity_delete=True,
                ),
                AtlasClassification(
                    type_name="typeName",
                    attributes={
                        "key": {
                            "key": "value"
                        }
                    },
                    entity_guid="entityGuid",
                    entity_status=AtlasClassificationEntityStatus.ACTIVE,
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        )
                    ],
                    remove_propagations_on_entity_delete=True,
                )
            ],
            meanings=[
                AtlasTermAssignmentHeader(
                    term_guid="termGuid",
                    relation_guid="relationGuid",
                    description="description",
                    display_text="displayText",
                    expression="expression",
                    created_by="createdBy",
                    steward="steward",
                    source="source",
                    confidence=1,
                    status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
                ),
                AtlasTermAssignmentHeader(
                    term_guid="termGuid",
                    relation_guid="relationGuid",
                    description="description",
                    display_text="displayText",
                    expression="expression",
                    created_by="createdBy",
                    steward="steward",
                    source="source",
                    confidence=1,
                    status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
                )
            ],
            custom_attributes={
                "key": "customAttributes"
            },
            business_attributes={
                "key": {
                    "key": "{}"
                }
            },
            labels=[
                "labels",
                "labels"
            ],
            pending_tasks=[
                "pendingTasks",
                "pendingTasks"
            ],
            proxy=True,
        )
    },
    entity=AtlasEntity(
        type_name="typeName",
        attributes={
            "key": "{}"
        },
        guid="guid",
        home_id="homeId",
        is_proxy=True,
        is_incomplete=True,
        provenance_type=0,
        status=AtlasEntityStatus.ACTIVE,
        created_by="createdBy",
        updated_by="updatedBy",
        create_time=1000000,
        update_time=1000000,
        version=6,
        relationship_attributes={
            "key": "{}"
        },
        classifications=[
            AtlasClassification(
                type_name="typeName",
                attributes={
                    "key": {
                        "key": "value"
                    }
                },
                entity_guid="entityGuid",
                entity_status=AtlasClassificationEntityStatus.ACTIVE,
                propagate=True,
                validity_periods=[
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    ),
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    )
                ],
                remove_propagations_on_entity_delete=True,
            ),
            AtlasClassification(
                type_name="typeName",
                attributes={
                    "key": {
                        "key": "value"
                    }
                },
                entity_guid="entityGuid",
                entity_status=AtlasClassificationEntityStatus.ACTIVE,
                propagate=True,
                validity_periods=[
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    ),
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    )
                ],
                remove_propagations_on_entity_delete=True,
            )
        ],
        meanings=[
            AtlasTermAssignmentHeader(
                term_guid="termGuid",
                relation_guid="relationGuid",
                description="description",
                display_text="displayText",
                expression="expression",
                created_by="createdBy",
                steward="steward",
                source="source",
                confidence=1,
                status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
            ),
            AtlasTermAssignmentHeader(
                term_guid="termGuid",
                relation_guid="relationGuid",
                description="description",
                display_text="displayText",
                expression="expression",
                created_by="createdBy",
                steward="steward",
                source="source",
                confidence=1,
                status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
            )
        ],
        custom_attributes={
            "key": "customAttributes"
        },
        business_attributes={
            "key": {
                "key": "{}"
            }
        },
        labels=[
            "labels",
            "labels"
        ],
        pending_tasks=[
            "pendingTasks",
            "pendingTasks"
        ],
        proxy=True,
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

**request:** `AtlasEntityWithExtInfo` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">partial_update_by_unique_attributes</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AtlasEntity, AtlasEntityStatus, AtlasClassification, AtlasClassificationEntityStatus, TimeBoundary, AtlasTermAssignmentHeader, AtlasTermAssignmentHeaderStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.partial_update_by_unique_attributes(
    referred_entities={
        "key": AtlasEntity(
            type_name="typeName",
            attributes={
                "key": "{}"
            },
            guid="guid",
            home_id="homeId",
            is_proxy=True,
            is_incomplete=True,
            provenance_type=0,
            status=AtlasEntityStatus.ACTIVE,
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=1000000,
            update_time=1000000,
            version=6,
            relationship_attributes={
                "key": "{}"
            },
            classifications=[
                AtlasClassification(
                    type_name="typeName",
                    attributes={
                        "key": {
                            "key": "value"
                        }
                    },
                    entity_guid="entityGuid",
                    entity_status=AtlasClassificationEntityStatus.ACTIVE,
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        )
                    ],
                    remove_propagations_on_entity_delete=True,
                ),
                AtlasClassification(
                    type_name="typeName",
                    attributes={
                        "key": {
                            "key": "value"
                        }
                    },
                    entity_guid="entityGuid",
                    entity_status=AtlasClassificationEntityStatus.ACTIVE,
                    propagate=True,
                    validity_periods=[
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        ),
                        TimeBoundary(
                            start_time="startTime",
                            end_time="endTime",
                            time_zone="timeZone",
                        )
                    ],
                    remove_propagations_on_entity_delete=True,
                )
            ],
            meanings=[
                AtlasTermAssignmentHeader(
                    term_guid="termGuid",
                    relation_guid="relationGuid",
                    description="description",
                    display_text="displayText",
                    expression="expression",
                    created_by="createdBy",
                    steward="steward",
                    source="source",
                    confidence=1,
                    status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
                ),
                AtlasTermAssignmentHeader(
                    term_guid="termGuid",
                    relation_guid="relationGuid",
                    description="description",
                    display_text="displayText",
                    expression="expression",
                    created_by="createdBy",
                    steward="steward",
                    source="source",
                    confidence=1,
                    status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
                )
            ],
            custom_attributes={
                "key": "customAttributes"
            },
            business_attributes={
                "key": {
                    "key": "{}"
                }
            },
            labels=[
                "labels",
                "labels"
            ],
            pending_tasks=[
                "pendingTasks",
                "pendingTasks"
            ],
            proxy=True,
        )
    },
    entity=AtlasEntity(
        type_name="typeName",
        attributes={
            "key": "{}"
        },
        guid="guid",
        home_id="homeId",
        is_proxy=True,
        is_incomplete=True,
        provenance_type=0,
        status=AtlasEntityStatus.ACTIVE,
        created_by="createdBy",
        updated_by="updatedBy",
        create_time=1000000,
        update_time=1000000,
        version=6,
        relationship_attributes={
            "key": "{}"
        },
        classifications=[
            AtlasClassification(
                type_name="typeName",
                attributes={
                    "key": {
                        "key": "value"
                    }
                },
                entity_guid="entityGuid",
                entity_status=AtlasClassificationEntityStatus.ACTIVE,
                propagate=True,
                validity_periods=[
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    ),
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    )
                ],
                remove_propagations_on_entity_delete=True,
            ),
            AtlasClassification(
                type_name="typeName",
                attributes={
                    "key": {
                        "key": "value"
                    }
                },
                entity_guid="entityGuid",
                entity_status=AtlasClassificationEntityStatus.ACTIVE,
                propagate=True,
                validity_periods=[
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    ),
                    TimeBoundary(
                        start_time="startTime",
                        end_time="endTime",
                        time_zone="timeZone",
                    )
                ],
                remove_propagations_on_entity_delete=True,
            )
        ],
        meanings=[
            AtlasTermAssignmentHeader(
                term_guid="termGuid",
                relation_guid="relationGuid",
                description="description",
                display_text="displayText",
                expression="expression",
                created_by="createdBy",
                steward="steward",
                source="source",
                confidence=1,
                status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
            ),
            AtlasTermAssignmentHeader(
                term_guid="termGuid",
                relation_guid="relationGuid",
                description="description",
                display_text="displayText",
                expression="expression",
                created_by="createdBy",
                steward="steward",
                source="source",
                confidence=1,
                status=AtlasTermAssignmentHeaderStatus.DISCOVERED,
            )
        ],
        custom_attributes={
            "key": "customAttributes"
        },
        business_attributes={
            "key": {
                "key": "{}"
            }
        },
        labels=[
            "labels",
            "labels"
        ],
        pending_tasks=[
            "pendingTasks",
            "pendingTasks"
        ],
        proxy=True,
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

**request:** `AtlasEntityWithExtInfo` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">search_using_attribute</a>(...) -> SearchResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve data for the specified attribute search query.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.search_using_attribute()

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

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the result to only entities of specified types
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attr:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One of more additional attributes to return in the response
    
</dd>
</dl>

<dl>
<dd>

**attrs:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attr_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The attribute to search
    
</dd>
</dl>

<dl>
<dd>

**attr_value_prefix:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The prefix for the attribute value to search
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the result to only entities tagged with the given tag
    
</dd>
</dl>

<dl>
<dd>

**time_range_type:** `typing.Optional[SearchUsingAttributeRequestTimeRangeType]` — The type of time range search, default is CUSTOM
    
</dd>
</dl>

<dl>
<dd>

**time_range_attr:** `typing.Optional[str]` — The attribute for a time range search
    
</dd>
</dl>

<dl>
<dd>

**time_range_start:** `typing.Optional[int]` — The start for a custom time range search in ms since the epoch
    
</dd>
</dl>

<dl>
<dd>

**time_range_end:** `typing.Optional[int]` — The end for a custom time range search in ms since the epoch
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — An attribute to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SearchUsingAttributeRequestSortOrder]` — Sort order, either ASCENDING (default) or DESCENDING
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted entities
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the result set to only include the specified number of entries
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start offset of the result set (useful for pagination)
    
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

<details><summary><code>client.<a href="src/fern/client.py">search_using_basic</a>(...) -> SearchResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve data for the specified fulltext query.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.search_using_basic()

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

**query:** `typing.Optional[str]` — The full-text query
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the result to only entities of specified types
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attr:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One of more additional attributes to return in the response
    
</dd>
</dl>

<dl>
<dd>

**attrs:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the result to only entities with the given tag
    
</dd>
</dl>

<dl>
<dd>

**time_range_type:** `typing.Optional[SearchUsingBasicRequestTimeRangeType]` — The type of time range search, default is CUSTOM
    
</dd>
</dl>

<dl>
<dd>

**time_range_attr:** `typing.Optional[str]` — The attribute for a time range search
    
</dd>
</dl>

<dl>
<dd>

**time_range_start:** `typing.Optional[int]` — The start for a custom time range search in ms since the epoch
    
</dd>
</dl>

<dl>
<dd>

**time_range_end:** `typing.Optional[int]` — The end for a custom time range search in ms since the epoch
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — An attribute to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SearchUsingBasicRequestSortOrder]` — Sort order, either ASCENDING (default) or DESCENDING
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to include deleted entities
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the result set to only include the specified number of entries
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start offset of the result set (useful for pagination)
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_all_business_metadata_defs</a>(...) -> typing.List[BusinessMetadataDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk retrieval API for retrieving business metadata definitions.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_business_metadata_defs()

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

**prefix:** `typing.Optional[str]` — The prefix of a business metadata definition name
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_business_metadata_defs</a>(...) -> typing.List[BusinessMetadataDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk create API for business metadata definitions.
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
from fern import FernApi, AtlasBusinessMetadataDef, AtlasBusinessMetadataDefCategory, AtlasAttributeDef, AtlasAttributeDefCardinality, AtlasAttributeDefIndexType, AtlasConstraintDef
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.create_business_metadata_defs(
    request=[
        AtlasBusinessMetadataDef(
            category=AtlasBusinessMetadataDefCategory.PRIMITIVE,
            guid="guid",
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            update_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            version=0,
            name="name",
            description="description",
            type_version="typeVersion",
            service_type="serviceType",
            options={
                "key": "options"
            },
            attribute_defs=[
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                ),
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                )
            ],
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

**request:** `typing.List[AtlasBusinessMetadataDef]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_business_metadata_defs</a>(...) -> typing.List[BusinessMetadataDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk update API for business metadata definitions.
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
from fern import FernApi, AtlasBusinessMetadataDef, AtlasBusinessMetadataDefCategory, AtlasAttributeDef, AtlasAttributeDefCardinality, AtlasAttributeDefIndexType, AtlasConstraintDef
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.update_business_metadata_defs(
    request=[
        AtlasBusinessMetadataDef(
            category=AtlasBusinessMetadataDefCategory.PRIMITIVE,
            guid="guid",
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            update_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            version=0,
            name="name",
            description="description",
            type_version="typeVersion",
            service_type="serviceType",
            options={
                "key": "options"
            },
            attribute_defs=[
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                ),
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                )
            ],
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

**request:** `typing.List[AtlasBusinessMetadataDef]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_all_tag_defs</a>(...) -> typing.List[TagDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk retrieval API for retrieving tag definitions.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_tag_defs()

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

**prefix:** `typing.Optional[str]` — The prefix of a tag definition name
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_tag_defs</a>(...) -> typing.List[TagDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk create API for tag definitions.
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
from fern import FernApi, TagDef, TagDefCategory, AtlasAttributeDef, AtlasAttributeDefCardinality, AtlasAttributeDefIndexType, AtlasConstraintDef
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.create_tag_defs(
    request=[
        TagDef(
            category=TagDefCategory.PRIMITIVE,
            guid="guid",
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=1000000,
            update_time=1000000,
            version=0,
            name="name",
            description="description",
            type_version="typeVersion",
            service_type="serviceType",
            options={
                "key": "options"
            },
            attribute_defs=[
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                ),
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                )
            ],
            super_types=[
                "superTypes",
                "superTypes"
            ],
            entity_types=[
                "entityTypes",
                "entityTypes"
            ],
            sub_types=[
                "subTypes",
                "subTypes"
            ],
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

**request:** `typing.List[TagDef]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_tag_defs</a>(...) -> typing.List[TagDefResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk update API for tag definitions.
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
from fern import FernApi, TagDef, TagDefCategory, AtlasAttributeDef, AtlasAttributeDefCardinality, AtlasAttributeDefIndexType, AtlasConstraintDef
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.update_tag_defs(
    request=[
        TagDef(
            category=TagDefCategory.PRIMITIVE,
            guid="guid",
            created_by="createdBy",
            updated_by="updatedBy",
            create_time=1000000,
            update_time=1000000,
            version=0,
            name="name",
            description="description",
            type_version="typeVersion",
            service_type="serviceType",
            options={
                "key": "options"
            },
            attribute_defs=[
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                ),
                AtlasAttributeDef(
                    name="name",
                    type_name="typeName",
                    is_optional=True,
                    cardinality=AtlasAttributeDefCardinality.SINGLE,
                    values_min_count=6,
                    values_max_count=1,
                    is_unique=True,
                    is_indexable=True,
                    include_in_notification=True,
                    default_value="defaultValue",
                    description="description",
                    search_weight=5,
                    index_type=AtlasAttributeDefIndexType.DEFAULT,
                    constraints=[
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        ),
                        AtlasConstraintDef(
                            type="type",
                            params={
                                "key": {
                                    "key": "value"
                                }
                            },
                        )
                    ],
                    options={
                        "key": "options"
                    },
                    display_name="displayName",
                )
            ],
            super_types=[
                "superTypes",
                "superTypes"
            ],
            entity_types=[
                "entityTypes",
                "entityTypes"
            ],
            sub_types=[
                "subTypes",
                "subTypes"
            ],
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

**request:** `typing.List[TagDef]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_business_metadata_def_by_name</a>(...) -> AtlasBusinessMetadataDef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the business metadata definition with the given name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_business_metadata_def_by_name(
    bm_name="bmName",
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

**bm_name:** `str` — The name of the business metadata definition
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_business_metadata_def</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete API for business metadata definition identified by its name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_business_metadata_def(
    bm_name="bmName",
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

**bm_name:** `str` — The name of the business metadata definition
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_tag_def_by_name</a>(...) -> TagDef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the tag definition with the given name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_tag_def_by_name(
    tag_name="tagName",
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

**tag_name:** `str` — The name of the tag definiton
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_tag_def</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete API for tag definition identified by its name.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_tag_def(
    tag_name="tagName",
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

**tag_name:** `str` — The name of the tag definition
    
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

<details><summary><code>client.<a href="src/fern/client.py">put_asyncapi_parse</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get number of times the cli tool is used to import and parse the spec file
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
    environment=FernApiEnvironment.DEFAULT,
)

client.put_asyncapi_parse()

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

<details><summary><code>client.<a href="src/fern/client.py">put_asyncapi</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get number of times the cli tool is used to export/produce the spec file
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
    environment=FernApiEnvironment.DEFAULT,
)

client.put_asyncapi()

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

