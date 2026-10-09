# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py">book_firing</a>(...)</code></summary>
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

client.firings.book_firing(
    kiln_number="kilnNumber",
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

**kiln_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**atmosphere:** `typing.Optional[BookFiringRequestAtmosphere]` 
    
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

