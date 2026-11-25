# Reference
## Orders
<details><summary><code>client.orders.<a href="src/fern/orders/client.py#L33-L95">place_order</a>(...) -> Receipt</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Buyer, Charterer, Lessee, Terms
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.orders.place_order(
    buyer=Buyer(
        name="name",
        phone="phone",
        pier="pier",
        slip=1,
    ),
    charterer=Charterer(
        name="name",
        phone="phone",
        pier="pier",
        slip=1,
    ),
    lessee=Lessee(
        name="name",
        phone="phone",
        pier="pier",
        slip=1,
        deck="deck",
    ),
    terms=Terms(
        kind="kind",
        due_on="due_on",
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

**buyer:** `Buyer` 
    
</dd>
</dl>

<dl>
<dd>

**charterer:** `Charterer` 
    
</dd>
</dl>

<dl>
<dd>

**lessee:** `Lessee` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `Terms` 
    
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

