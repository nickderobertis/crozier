# Reference
<details><summary><code>client.<a href="src/fern/client.py">patch_shelf_links</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LinkPatchItemZero

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.patch_shelf_links(
    shelf_id="shelfId",
    request=[
        LinkPatchItemZero()
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

**shelf_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LinkPatch` 
    
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

