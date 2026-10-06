# Reference
## OddsCalculations
<details><summary><code>client.odds_calculations.<a href="src/fern/odds_calculations/client.py">odds</a>(...) -> float</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EmpireConfiguration, BountyHunters

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.odds_calculations.odds(
    empire_config=EmpireConfiguration(
        countdown=1,
        bounty_hunters=[
            BountyHunters(
                day=1,
                planet="planet",
            )
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

**empire_config:** `EmpireConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**falcon_config:** `typing.Optional[FalconConfiguration]` 
    
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

