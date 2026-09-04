# Reference
## Widgets
<details><summary><code>client.widgets.<a href="src/fern/widgets/client.py">watch_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
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

client.widgets.watch_stream()

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

**stream:** `typing.Literal` — When true, stream events instead of returning one.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

<details><summary><code>client.widgets.<a href="src/fern/widgets/client.py">watch</a>(...) -> WidgetEvent</code></summary>
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

client.widgets.watch_stream()

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

**stream:** `typing.Literal` — When true, stream events instead of returning one.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

## Catalog Widgets
<details><summary><code>client.catalog.widgets.<a href="src/fern/catalog/widgets/client.py">list</a>(...) -> WidgetPage</code></summary>
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

client.catalog.widgets.list()

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

**page_token:** `typing.Optional[str]` — Opaque cursor from a previous page.
    
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

