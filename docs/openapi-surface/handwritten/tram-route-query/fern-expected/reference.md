# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_departures</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RouteFilter

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.list_departures(
    route=RouteFilter(
        platforms=[
            "platforms",
            "platforms"
        ],
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

**route:** `RouteFilter` 
    
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

