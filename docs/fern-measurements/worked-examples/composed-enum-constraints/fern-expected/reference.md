# Reference
<details><summary><code>client.<a href="src/fern/client.py#L100-L131">register_parcel</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ParcelState

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.register_parcel(
    label="label",
    state=ParcelState.DRAFTED,
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

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `ParcelState` — Where a parcel is in its journey.
    
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

