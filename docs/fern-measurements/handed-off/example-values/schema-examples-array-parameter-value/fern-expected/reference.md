# Reference
## Lamps
<details><summary><code>client.lamps.<a href="src/fern/lamps/client.py">get_lamp</a>(...) -> GetLampResponse</code></summary>
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

client.lamps.get_lamp(
    lamp_id="lmp_8f2kq",
    wattage=60,
    shade="amber-glass",
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

**lamp_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**wattage:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**shade:** `str` 
    
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

<details><summary><code>client.lamps.<a href="src/fern/lamps/client.py">get_lamp_manual</a>(...)</code></summary>
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

client.lamps.get_lamp_manual(
    lamp_id="lmp_8f2kq",
    edition="second",
    shade="amber-glass",
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

**lamp_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**edition:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**shade:** `str` 
    
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

<details><summary><code>client.lamps.<a href="src/fern/lamps/client.py">update_lamp_settings</a>(...) -> UpdateLampSettingsResponse</code></summary>
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

client.lamps.update_lamp_settings(
    lamp_id="lampId",
    request={"key": "value"},
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

**lamp_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
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

