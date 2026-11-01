# Reference
## Buoys
<details><summary><code>client.buoys.<a href="src/fern/buoys/client.py">register_buoy</a>(...) -> RegisterBuoyResponse</code></summary>
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

client.buoys.register_buoy(
    survey_ref="X-Survey-Ref",
    label="label",
    depth_metres=1,
    harbour="harbour",
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

**survey_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth_metres:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**harbour:** `str` 
    
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

<details><summary><code>client.buoys.<a href="src/fern/buoys/client.py">record_reading</a>(...) -> RecordReadingResponse</code></summary>
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

client.buoys.record_reading(
    buoy_id="buoyId",
    berth=1,
    note="",
    swell=0,
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

**buoy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**berth:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**swell:** `int` 
    
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

