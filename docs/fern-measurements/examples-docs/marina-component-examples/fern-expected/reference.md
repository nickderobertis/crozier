# Reference
## Berths
<details><summary><code>client.berths.<a href="src/fern/berths/client.py">set_hull</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.berths import HullRequestHull_Steel

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.berths.set_hull(
    berth_id="berth_id",
    hull=HullRequestHull_Steel(
        length_m=24,
        beam_m=6,
        draft_cm=180,
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

**berth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**hull:** `HullRequestHull` 
    
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

## Permits
<details><summary><code>client.permits.<a href="src/fern/permits/client.py">issue_permits</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PermitBatchItem

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.permits.issue_permits(
    request=[
        PermitBatchItem(
            vessel="Sea Lark",
            zone="north-basin",
        ),
        PermitBatchItem(
            vessel="Tern",
            zone="fuel-dock",
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

**request:** `PermitBatch` 
    
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

<details><summary><code>client.permits.<a href="src/fern/permits/client.py">revoke_permits</a>(...)</code></summary>
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

client.permits.revoke_permits(
    request=[
        "PRM-0042"
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

**request:** `PermitCodes` 
    
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

## Session
<details><summary><code>client.session.<a href="src/fern/session/client.py">open_session</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SessionFormGrant

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.session.open_session(
    grant=SessionFormGrant.HARBOUR_PASS,
    skipper_id="SK-118",
    pin="4471",
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

**request:** `SessionForm` 
    
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

