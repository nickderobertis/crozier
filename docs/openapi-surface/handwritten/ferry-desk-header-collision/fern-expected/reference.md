# Reference
## Sailings
<details><summary><code>client.sailings.<a href="src/fern/sailings/client.py">list_sailings</a>() -> typing.List[Sailing]</code></summary>
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

client.sailings.list_sailings()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sailings.<a href="src/fern/sailings/client.py">book_vehicle</a>(...) -> Booking</code></summary>
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

client.sailings.book_vehicle(
    sailing_id="sailingId",
    registration="registration",
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

**sailing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**registration:** `str` — The vehicle's number plate.
    
</dd>
</dl>

<dl>
<dd>

**deck:** `typing.Optional[str]` — The deck the desk prefers to fill first.
    
</dd>
</dl>

<dl>
<dd>

**book_vehicle_request_deck:** `typing.Optional[str]` — The deck the driver asked for.
    
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

