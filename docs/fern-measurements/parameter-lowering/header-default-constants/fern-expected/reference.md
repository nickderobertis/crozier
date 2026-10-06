# Reference
## Beds
<details><summary><code>client.beds.<a href="src/fern/beds/client.py">list_beds</a>(...) -> typing.List[str]</code></summary>
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
from fern.beds import ListBedsRequestXVentMode

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.beds.list_beds(
    section="section",
    lamp_watts=1,
    vent_mode=ListBedsRequestXVentMode.OPEN,
    valve_mode="drip",
    mist_mode="fine",
    hatch_mode="down",
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

**section:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**lamp_watts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**vent_mode:** `ListBedsRequestXVentMode` 
    
</dd>
</dl>

<dl>
<dd>

**valve_mode:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**mist_mode:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**hatch_mode:** `typing.Literal` — Which way the roof hatch rests.
    
</dd>
</dl>

<dl>
<dd>

**fan_speed:** `typing.Optional[int]` 
    
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

<details><summary><code>client.beds.<a href="src/fern/beds/client.py">get_bed</a>(...) -> str</code></summary>
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

client.beds.get_bed(
    bed_id="bed_id",
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

**bed_id:** `str` 
    
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

