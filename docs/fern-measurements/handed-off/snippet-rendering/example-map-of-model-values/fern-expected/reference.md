# Reference
## Records
<details><summary><code>client.records.<a href="src/fern/records/client.py">search_records</a>(...) -> typing.List[SearchRecordsResponseItem]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Span
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.records.search_records(
    query="harbour charters",
    filters={
        "language": [
            "Welsh"
        ],
        "accessioned": Span(
            from_="1901-01-01",
            to="1910-12-31",
        ),
        "sealed": [
            Span(
                from_="1921-01-01",
                to="1921-12-31",
            ),
            Span(
                from_="1938-01-01",
                to="1938-12-31",
            )
        ]
    },
    bounds={
        "shelf": Span(
            from_="A",
            to="F",
        )
    },
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

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, SearchRecordsRequestFiltersValue]]` 
    
</dd>
</dl>

<dl>
<dd>

**bounds:** `typing.Optional[typing.Dict[str, Span]]` 
    
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

