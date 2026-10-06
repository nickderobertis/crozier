# Reference
## Harvests
<details><summary><code>client.harvests.<a href="src/fern/harvests/client.py">list_harvests</a>(...) -> typing.List[str]</code></summary>
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

client.harvests.list_harvests()

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

**ripeness:** `typing.Optional[ListHarvestsRequestRipeness]` 
    
</dd>
</dl>

<dl>
<dd>

**crate:** `typing.Optional[ListHarvestsRequestCrate]` 
    
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

<details><summary><code>client.harvests.<a href="src/fern/harvests/client.py">list_weighed_harvests</a>(...) -> typing.List[str]</code></summary>
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

client.harvests.list_weighed_harvests()

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

**unit:** `typing.Optional[ListWeighedHarvestsRequestUnit]` 
    
</dd>
</dl>

<dl>
<dd>

**grade:** `typing.Optional[ListWeighedHarvestsRequestGrade]` 
    
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

## Rows
<details><summary><code>client.rows.<a href="src/fern/rows/client.py">get_row</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetRowRequestPickerZero

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.rows.get_row(
    row="row",
    season="season",
    picker=GetRowRequestPickerZero.MORNING,
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

**row:** `GetRowRequestRow` 
    
</dd>
</dl>

<dl>
<dd>

**season:** `GetRowRequestSeason` 
    
</dd>
</dl>

<dl>
<dd>

**picker:** `typing.Optional[GetRowRequestPicker]` 
    
</dd>
</dl>

<dl>
<dd>

**orchard_block:** `typing.Optional[GetRowRequestXOrchardBlock]` 
    
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

