# Reference
## Items
<details><summary><code>client.items.<a href="src/fern/items/client.py">createbatch</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern.items import ItemsCreateBatchRequestItem

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.items.createbatch(
    request=[
        ItemsCreateBatchRequestItem(
            name="name",
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

**request:** `typing.Sequence[ItemsCreateBatchRequestItem]` 
    
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

