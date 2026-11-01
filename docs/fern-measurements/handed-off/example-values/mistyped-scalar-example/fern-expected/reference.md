# Reference
## Depots
<details><summary><code>client.depots.<a href="src/fern/depots/client.py">create_depot</a>(...) -> CreateDepotResponse</code></summary>
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

client.depots.create_depot(
    postcode="postcode",
    capacity=1000000,
    code="code",
    aliases=[
        "west quay"
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

**postcode:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capacity:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**aliases:** `typing.List[str]` 
    
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

<details><summary><code>client.depots.<a href="src/fern/depots/client.py">compare_depots</a>(...) -> CompareDepotsResponse</code></summary>
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

client.depots.compare_depots(
    left="dpt-1",
    right="dpt-2",
    level=1.1,
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

**left:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**right:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**level:** `float` 
    
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

