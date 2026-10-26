# Reference
## Loads
<details><summary><code>client.loads.<a href="src/fern/loads/client.py">schedule_load</a>(...) -> Load</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Kiln
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.loads.schedule_load(
    label="label",
    kiln=Kiln(
        name="name",
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

**request:** `Load` 
    
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

<details><summary><code>client.loads.<a href="src/fern/loads/client.py">transfer_load</a>(...) -> Load</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Kiln
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.loads.transfer_load(
    load_id="loadId",
    destination=Kiln(
        name="name",
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

**load_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `Kiln` 
    
</dd>
</dl>

<dl>
<dd>

**fallback:** `typing.Optional[TransferLoadRequestFallback]` — Kiln to use when the destination is full.
    
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

