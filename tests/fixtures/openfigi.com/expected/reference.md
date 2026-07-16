# Reference
<details><summary><code>client.<a href="src/fern/client.py">post_mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows mapping from third-party identifiers to FIGIs.
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
from fern import FernApi, MappingJob, MappingJobIdType

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.post_mapping(
    request=[
        MappingJob(
            id_type=MappingJobIdType.ID_ISIN,
            id_value="idValue",
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

**request:** `BulkMappingJob` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_mapping_values_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get values for enum-like fields.
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
from fern import FernApi, GetMappingValuesKeyRequestKey

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.get_mapping_values_key(
    key=GetMappingValuesKeyRequestKey.ID_TYPE,
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

**key:** `GetMappingValuesKeyRequestKey` — Key of MappingJob for which to get possible values.
    
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

