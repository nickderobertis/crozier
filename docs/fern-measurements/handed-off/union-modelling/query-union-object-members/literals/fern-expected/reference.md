# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py#L28-L70">list_firings</a>(...) -> typing.List[str]</code></summary>
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

client.firings.list_firings(
    cone=1,
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

**cone:** `ListFiringsRequestCone` — A cone number, or a range of cones.
    
</dd>
</dl>

<dl>
<dd>

**glaze:** `typing.Optional[ListFiringsRequestGlaze]` — A glaze name, or the glaze document to match.
    
</dd>
</dl>

<dl>
<dd>

**kiln_id:** `typing.Optional[ListFiringsRequestKilnId]` — Kiln identifiers, or `?[any]=true` for any kiln.
    
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

