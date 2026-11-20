# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py#L29-L73">list_firings</a>(...) -> typing.List[str]</code></summary>
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

client.firings.list_firings()

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

**kiln:** `typing.Optional[ListFiringsRequestKiln]` — A kiln name, any or all kilns, or a list of names.
    
</dd>
</dl>

<dl>
<dd>

**glaze:** `typing.Optional[ListFiringsRequestGlaze]` — A glaze filter as text, or an empty object.
    
</dd>
</dl>

<dl>
<dd>

**cone:** `typing.Optional[ListFiringsRequestCone]` — A cone filter as text, or a cone and a shelf.
    
</dd>
</dl>

<dl>
<dd>

**atmosphere:** `typing.Optional[ListFiringsRequestAtmosphere]` — One atmosphere, or several.
    
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

