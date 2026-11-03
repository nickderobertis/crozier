# Reference
## Calibrations
<details><summary><code>client.calibrations.<a href="src/fern/calibrations/client.py">record_calibration</a>(...) -> RecordCalibrationResponse</code></summary>
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

client.calibrations.record_calibration(
    gain=0.9345407030264767,
    offsets=[
        0.1234567890123456,
        2.718281828459045
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

**gain:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**offsets:** `typing.List[float]` 
    
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

