# Reference
## Items
<details><summary><code>client.items.<a href="src/fern/items/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.items import ItemsCreateRequestInfo, ItemsCreateRequestMetaItemUnitId, ItemsCreateRequestMetaItemUnitIdKind, ItemsCreateRequestData, ItemsCreateRequestDataProps
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.items.create(
    info=ItemsCreateRequestInfo(
        label="first",
    ),
    created=datetime.datetime.fromisoformat("2024-01-02T03:04:05+00:00"),
    meta=[
        ItemsCreateRequestMetaItemUnitId(
            kind=ItemsCreateRequestMetaItemUnitIdKind.UNIT,
            ref="{\"a\":\"b\"}",
        )
    ],
    data=ItemsCreateRequestData(
        props=ItemsCreateRequestDataProps(
            path="/a",
        ),
        ext={
            "key": "value"
        },
    ),
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

**info:** `ItemsCreateRequestInfo` 
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.List[ItemsCreateRequestMetaItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[ItemsCreateRequestData]` 
    
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

## Widgetpart
<details><summary><code>client.widgetpart.<a href="src/fern/widgetpart/client.py">get</a>(...)</code></summary>
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

client.widgetpart.get(
    id="id",
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

**id:** `str` 
    
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

## WidgetPart
<details><summary><code>client.widget_part.<a href="src/fern/widget_part/client.py">widget_part_list</a>()</code></summary>
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

client.widget_part.widget_part_list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

