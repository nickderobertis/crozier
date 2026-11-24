# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py#L29-L68">clone_firing</a>(...) -> CloneResult</code></summary>
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

client.firings.clone_firing(
    firing_id="firingId",
    region="region",
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

**firing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloneFiringBody` 
    
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

<details><summary><code>client.firings.<a href="src/fern/firings/client.py#L70-L108">copy_firing</a>(...) -> CloneResult</code></summary>
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

client.firings.copy_firing(
    firing_id="firingId",
    shelf="shelf",
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

**firing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CopyFiringBody` 
    
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

