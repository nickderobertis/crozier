# Reference
<details><summary><code>client.<a href="src/fern/client.py#L101-L137">get_almanac</a>(...)</code></summary>
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

client.get_almanac(
    day=datetime.date.fromisoformat("2031-06-21"),
    since=datetime.date.fromisoformat("2031-06-21"),
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

**day:** `Day` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[Day]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L139-L168">get_chart</a>(...)</code></summary>
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

client.get_chart(
    day=datetime.date.fromisoformat("2031-06-21"),
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

**day:** `Day` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L170-L233">log_voyage</a>(...)</code></summary>
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

client.log_voyage(
    vessel="Kestrel",
    sailed_on=datetime.date.fromisoformat("2023-01-15"),
    returned_on=datetime.date.fromisoformat("2023-01-15"),
    logged_on=datetime.date.fromisoformat("2031-04-10"),
    checked_on=datetime.date.fromisoformat("2023-01-15"),
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

**vessel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sailed_on:** `datetime.date` 
    
</dd>
</dl>

<dl>
<dd>

**returned_on:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**logged_on:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**checked_on:** `typing.Optional[datetime.date]` 
    
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

