# Reference
<details><summary><code>client.<a href="src/fern/client.py">book_bench</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AWing, BenchSlot

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.book_bench(
    rig=AWing(
        serial="serial",
    ),
    slot=BenchSlot(
        hour=1,
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

**rig:** `AWing` 
    
</dd>
</dl>

<dl>
<dd>

**slot:** `BenchSlot` 
    
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

