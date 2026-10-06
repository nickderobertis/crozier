# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py">list_firings</a>(...) -> typing.List[str]</code></summary>
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
    shelf=1,
    glaze="glaze",
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

**shelf:** `ListFiringsRequestShelf` 
    
</dd>
</dl>

<dl>
<dd>

**glaze:** `ListFiringsRequestGlaze` 
    
</dd>
</dl>

<dl>
<dd>

**cone:** `typing.Optional[int]` 
    
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

<details><summary><code>client.firings.<a href="src/fern/firings/client.py">list_cooling_firings</a>(...) -> typing.List[str]</code></summary>
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

client.firings.list_cooling_firings(
    batch=[
        1
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

**kiln:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**batch:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**atmosphere:** `typing.Optional[ListCoolingFiringsRequestAtmosphere]` 
    
</dd>
</dl>

<dl>
<dd>

**pyrometer:** `typing.Optional[ListCoolingFiringsRequestPyrometer]` 
    
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

