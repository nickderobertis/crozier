# Reference
## Arboretum
<details><summary><code>client.arboretum.<a href="src/fern/arboretum/client.py">plant_tree</a>(...) -> Tree</code></summary>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.arboretum.plant_tree(
    species="species",
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

**species:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**zone:** `typing.Optional[PlantTreeRequestZone]` 
    
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

## YewWalk
<details><summary><code>client.yew_walk.<a href="src/fern/yew_walk/client.py">trim_hedge</a>(...) -> TrimHedgeResponse</code></summary>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.yew_walk.trim_hedge(
    length=1.1,
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

**length:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[TrimHedgeRequestFinish]` 
    
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

