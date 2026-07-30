# Reference
## Items
<details><summary><code>client.items.<a href="src/fern/items/client.py">createbatch</a>(...) -> typing.List[Item]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.items import ItemsCreateBatchRequestItem

client = FernApi(
    token="<token>",
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

**request:** `typing.List[ItemsCreateBatchRequestItem]` 
    
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

