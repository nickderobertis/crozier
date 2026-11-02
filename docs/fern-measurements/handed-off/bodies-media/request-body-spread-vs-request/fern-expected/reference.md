# Reference
## Hives
<details><summary><code>client.hives.<a href="src/fern/hives/client.py">register_hive</a>(...)</code></summary>
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

client.hives.register_hive(
    apiary="apiary",
    queen_marked=True,
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

**apiary:** `str` — The apiary the hive stands in.
    
</dd>
</dl>

<dl>
<dd>

**queen_marked:** `bool` — Whether the queen carries a paint mark.
    
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

<details><summary><code>client.hives.<a href="src/fern/hives/client.py">upload_frame</a>(...)</code></summary>
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

client.hives.upload_frame(
    hive_id="hiveId",
    photo="example_photo",
    position=1,
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

**hive_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**photo:** `core.File` — The frame photo.
    
</dd>
</dl>

<dl>
<dd>

**position:** `int` — The frame's slot, counted from the entrance.
    
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

