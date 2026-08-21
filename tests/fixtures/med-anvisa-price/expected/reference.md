# Reference
## Medication
<details><summary><code>client.medication.<a href="src/fern/medication/client.py">route_for_getting_filtered_medication_requests</a>(...) -> GetMedicationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.medication.route_for_getting_filtered_medication_requests()

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

**filter:** `typing.Optional[GetMedicationRequestFilter]` — Pass the filter parameter you want to filter by
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value for the filter
    
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

