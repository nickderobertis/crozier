# Reference
## Keepers
<details><summary><code>client.keepers.<a href="src/fern/keepers/client.py">list_keeper_shifts</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.keepers.list_keeper_shifts(
    keeper_id="KPR-from-schema",
    season="winter",
    rostered_on=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**keeper_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**season:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rostered_on:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**rostered_after:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.keepers.<a href="src/fern/keepers/client.py">list_keeper_callbacks</a>(...) -> typing.List[str]</code></summary>
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

client.keepers.list_keeper_callbacks()

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

**since:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.keepers.<a href="src/fern/keepers/client.py">search_keepers</a>(...) -> typing.List[str]</code></summary>
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

client.keepers.search_keepers()

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

**q:** `typing.Optional[str]` 
    
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

