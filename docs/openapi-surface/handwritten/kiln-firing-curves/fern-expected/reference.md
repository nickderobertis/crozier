# Reference
## Curves
<details><summary><code>client.curves.<a href="src/fern/curves/client.py">record_curve</a>(...) -> Curve</code></summary>
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

client.curves.record_curve(
    tolerance=0.9584673068551939,
    glaze=0.9921600467158583,
    readings=[
        ["kiln-east-b", "2026-03-01", 0.24200106749781558, 0.36454792138880565],
        ["kiln-north-a", "2026-03-01", 0.24200106749781558, 0.36454792138880565],
        ["kiln-east-b", "2026-03-02", 0.38480342994262373, 0.46566309815988427]
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

**tolerance:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Curve` 
    
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

