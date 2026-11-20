# Reference
## Kilns
<details><summary><code>client.kilns.<a href="src/fern/kilns/client.py#L30-L63">register_kiln</a>(...)</code></summary>
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

client.kilns.register_kiln(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]]` 
    
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

<details><summary><code>client.kilns.<a href="src/fern/kilns/client.py#L65-L105">adjust_kiln_settings</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.kilns import AdjustKilnSettingsRequestChangesItem

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.kilns.adjust_kiln_settings(
    kiln_id="kilnId",
    changes=[
        AdjustKilnSettingsRequestChangesItem(
            setting="setting",
        )
    ],
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

**kiln_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.List[AdjustKilnSettingsRequestChangesItem]` 
    
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

