# Reference
## Loans
<details><summary><code>client.loans.<a href="src/fern/loans/client.py">set_due</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DueMarker_Calendar
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.loans.set_due(
    loan_id="loanId",
    request=DueMarker_Calendar(
        value=datetime.date.fromisoformat("2023-01-15"),
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

**loan_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DueMarker` 
    
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

