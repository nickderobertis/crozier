# Reference
## Glazes
<details><summary><code>client.glazes.<a href="src/fern/glazes/client.py#L27-L66">list_glazes</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.glazes.list_glazes(
    palette=[
        "celadon"
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

**finish:** `typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]` 
    
</dd>
</dl>

<dl>
<dd>

**firing:** `typing.Optional[typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**palette:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.glazes.<a href="src/fern/glazes/client.py#L68-L97">list_required_glazes</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.glazes.list_required_glazes(
    finish=[
        "matte"
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

**finish:** `typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]` 
    
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

