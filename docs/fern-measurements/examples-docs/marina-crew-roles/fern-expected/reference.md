# Reference
## Crews
<details><summary><code>client.crews.<a href="src/fern/crews/client.py">register_crew</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.crews import CrewRequestRoster, CrewRequestRosterRolesValue

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.crews.register_crew(
    vessel="Sea Lark",
    roster=CrewRequestRoster(
        roles={
            "skipper": CrewRequestRosterRolesValue(
                name="Ada",
            ),
            "mate": CrewRequestRosterRolesValue(
                name="Rui",
            ),
            "engineer": CrewRequestRosterRolesValue(
                name="Lin",
            )
        },
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

**vessel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roster:** `typing.Optional[CrewRequestRoster]` 
    
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

