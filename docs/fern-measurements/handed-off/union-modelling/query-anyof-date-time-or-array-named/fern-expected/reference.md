# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_parcels</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.list_parcels()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shipped_at:** `typing.Optional[ListParcelsRequestShippedAt]` — When the parcel shipped, or any of several moments.
    
</dd>
</dl>

<dl>
<dd>

**weight:** `typing.Optional[ListParcelsRequestWeight]` 
    
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

