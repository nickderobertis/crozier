# Reference
## Widgets
<details><summary><code>client.widgets.<a href="src/fern/widgets/client.py">list_widgets</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AcmeClient

client = AcmeClient(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.widgets.list_widgets()

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

<details><summary><code>client.widgets.<a href="src/fern/widgets/client.py">create_widget</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AcmeClient

client = AcmeClient(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.widgets.create_widget(
    id="id",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

