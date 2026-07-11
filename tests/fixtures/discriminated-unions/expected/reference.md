# Reference
## Shapes
<details><summary><code>client.shapes.<a href="src/fern/shapes/client.py">createshape</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Shape_Circle

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.shapes.createshape(
    request=Shape_Circle(
        radius=1.1,
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

**request:** `Shape` 
    
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

