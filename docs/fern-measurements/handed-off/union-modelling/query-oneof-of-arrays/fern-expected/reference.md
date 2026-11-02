# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_tiles</a>(...) -> typing.List[str]</code></summary>
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

client.list_tiles()

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

**corners:** `typing.Optional[typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]]` — Two or three corner objects bounding the tiles.
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[ListTilesRequestZoom]` 
    
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

