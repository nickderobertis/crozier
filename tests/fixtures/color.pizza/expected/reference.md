# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_all_colors_of_the_default_color_name_list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.get_all_colors_of_the_default_color_name_list(
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

**name:** `str` — The name of the color to retrieve (min 3 characters)
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[PossibleLists]` — The name of the color name list to use
    
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

<details><summary><code>client.<a href="src/fern/client.py">generate_a_color_swatch_for_any_color</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi()
client.generate_a_color_swatch_for_any_color(
    color="color",
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

**color:** `str` — The hex value of the color to retrieve without '#'
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the color
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

