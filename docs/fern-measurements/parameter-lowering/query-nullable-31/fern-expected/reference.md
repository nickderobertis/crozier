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

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.beds.list_beds(
    soil="soil",
    rows=[
        None
    ],
    trays=[
        None
    ],
    shade="shade",
    pots=[
        1
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

**soil:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**crops:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**rows:** `typing.Optional[typing.Union[typing.Optional[int], typing.Sequence[typing.Optional[int]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**trays:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**shade:** `typing.Optional[ListBedsRequestShade]` 
    
</dd>
</dl>

<dl>
<dd>

**pots:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
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

