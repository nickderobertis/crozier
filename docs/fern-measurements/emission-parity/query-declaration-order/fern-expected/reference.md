# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_readings</a>(...) -> typing.List[Reading]</code></summary>
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

client.list_readings(
    lamp_id="north-tower",
    since="2024-03-01",
    unit="lumen",
    limit=25,
    shift="shift",
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

**unit:** `str` — Unit the readings are reported in.
    
</dd>
</dl>

<dl>
<dd>

**shift:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Earliest reading to include.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">write_logbook</a>(...) -> LogbookEntry</code></summary>
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

client.write_logbook(
    lamp_id="north-tower",
    draft=True,
    tide="high",
    watch_note="calm seas",
    keeper_id="keeper-7",
    text="Fog rolled in at six.",
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

**tide:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keeper_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LogbookEntry` 
    
</dd>
</dl>

<dl>
<dd>

**draft:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**watch_note:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">upload_photo</a>(...)</code></summary>
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

client.upload_photo(
    lamp_id="lampId",
    caption="dusk",
    album="winter",
    camera="brass-lens",
    photo="example_photo",
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

**album:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**photo:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**caption:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**camera:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_lamps</a>(...) -> typing.List[str]</code></summary>
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

client.list_lamps(
    region="coast",
    lit=False,
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

**region:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**lit:** `typing.Optional[bool]` 
    
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

