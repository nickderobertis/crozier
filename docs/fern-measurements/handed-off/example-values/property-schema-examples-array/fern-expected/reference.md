# Reference
## Plots
<details><summary><code>client.plots.<a href="src/fern/plots/client.py">plot_course</a>(...) -> PlotCourseResponse</code></summary>
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

client.plots.plot_course(
    waypoints=[
        "50.1N 5.0W",
        "hold at \"Wolf Rock\"",
        "log\tthen \"sound\" at C:\\charts",
        "50.3N 4.8W"
    ],
    vessel="Morwenna",
    legs=4,
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

**waypoints:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**vessel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**legs:** `int` 
    
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

