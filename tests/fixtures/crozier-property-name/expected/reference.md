# Reference
## Harbor
<details><summary><code>client.harbor.<a href="src/fern/harbor/client.py">create_berth_assignment</a>(...) -> HarborBerthAssignment</code></summary>
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

client.harbor.create_berth_assignment(
    harbor_id="harbor_id",
    harbor_berth_assignment_create_harbor_id="harbor_id",
    vessel_name="vessel_name",
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

**harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**harbor_berth_assignment_create_harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vessel_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stay_hours:** `typing.Optional[int]` 
    
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

<details><summary><code>client.harbor.<a href="src/fern/harbor/client.py">create_voyage</a>(...) -> HarborVoyage</code></summary>
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

client.harbor.create_voyage(
    harbor_id="harbor_id",
    harbor_voyage_create_harbor_id="harbor_id",
    route="route",
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

**harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**harbor_voyage_create_harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**route:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.harbor.<a href="src/fern/harbor/client.py">create_mooring_permit</a>(...) -> HarborEvent</code></summary>
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

client.harbor.create_mooring_permit(
    harbor_id="harbor_id",
    mooring_permit_harbor_id="harbor_id",
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

**harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mooring_permit_harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vessel:** `typing.Optional[CreateMooringPermitRequestVessel]` 
    
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

<details><summary><code>client.harbor.<a href="src/fern/harbor/client.py">create_log_entry</a>(...)</code></summary>
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

client.harbor.create_log_entry(
    harbor_id="harbor_id",
    log_entry_harbor_id="harbor_id",
    body="body",
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

**harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**log_entry_harbor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
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

