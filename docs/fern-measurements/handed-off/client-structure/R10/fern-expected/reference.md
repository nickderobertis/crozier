# Reference
## Payments
<details><summary><code>client.payments.<a href="src/fern/payments/client.py">pay_toll</a>(...) -> PayTollResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentRequestSource_Tag
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.payments.pay_toll(
    lane=1,
    source=PaymentRequestSource_Tag(
        tag_id="tagId",
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

**lane:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `PaymentRequestSource` 
    
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

