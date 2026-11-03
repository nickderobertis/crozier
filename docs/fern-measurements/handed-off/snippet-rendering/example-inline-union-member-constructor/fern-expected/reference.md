# Reference
## Checkouts
<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">update_checkout</a>(...) -> UpdateCheckoutResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DeliveryChoiceZero, DeliveryChoiceZeroMethod
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.update_checkout(
    checkout_id="checkoutId",
    deliveries=[
        DeliveryChoiceZero(
            method=DeliveryChoiceZeroMethod.LOCKER,
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

**checkout_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**deliveries:** `typing.List[DeliveryChoice]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

