# Reference
## Stalls
<details><summary><code>client.stalls.<a href="src/fern/stalls/client.py">check_availability</a>(...) -> CheckAvailabilityResponse</code></summary>
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

client.stalls.check_availability(
    market="riverside",
    row="B",
    stall=1,
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

**row:** `str` — The stall row.
    
</dd>
</dl>

<dl>
<dd>

**stall:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[str]` — The market's short name.
    
</dd>
</dl>

<dl>
<dd>

**week:** `typing.Optional[int]` 
    
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

