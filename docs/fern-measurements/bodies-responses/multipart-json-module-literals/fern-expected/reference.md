# Reference
<details><summary><code>client.<a href="src/fern/client.py">store_survey</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, StoreSurveyRequestJson
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.store_survey(
    attachment="example_attachment",
    json=StoreSurveyRequestJson(
        bearing=1,
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

**json:** `StoreSurveyRequestJson` 
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `core.File` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">store_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, StoreMetadataRequestMetadata
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.store_metadata(
    metadata=StoreMetadataRequestMetadata(
        bearing=1,
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

**metadata:** `StoreMetadataRequestMetadata` 
    
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

