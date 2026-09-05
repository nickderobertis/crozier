# Reference
## Probe
<details><summary><code>client.probe.<a href="src/fern/probe/client.py">rules</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.probe import ProbeRulesRequestRulesItem, ProbeRulesRequestRulesItemContext, ProbeRulesRequestRulesItemContextDateRange, ProbeRulesRequestRulesItemContextMarkupRange

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.probe.rules(
    id="id",
    rules=[
        ProbeRulesRequestRulesItem(
            context=ProbeRulesRequestRulesItemContext(
                brands={
                    "Brand ID": "2000002",
                    "Brand Name": "Whiskas"
                },
                categories={
                    "Category ID": "1",
                    "Category Name": "Alimentação"
                },
                date_range=ProbeRulesRequestRulesItemContextDateRange(
                    from_="2022-01-23T19:00:00.000Z",
                    to="2023-10-26T00:00:00.000Z",
                ),
                markup_range=ProbeRulesRequestRulesItemContextMarkupRange(
                    from_=0,
                    to=200,
                ),
            ),
            id=1,
            percentual_modifier=0,
        )
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.List[ProbeRulesRequestRulesItem]` — Array of rules for the price table.
    
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

