# Reference
<details><summary><code>client.<a href="src/fern/client.py">store_measurement</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MeasurementPhase

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.store_measurement(
    phase=MeasurementPhase.PREPARATION,
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

**phase:** `MeasurementPhase` — The phase permitted for a stored measurement.
    
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

<details><summary><code>client.<a href="src/fern/client.py">store_inline_measurement</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, StoreInlineMeasurementRequestPhase

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.store_inline_measurement(
    phase=StoreInlineMeasurementRequestPhase.PREPARATION,
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

**phase:** `StoreInlineMeasurementRequestPhase` — The phase permitted for a stored measurement.
    
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

