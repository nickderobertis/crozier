# Reference
## CheckoutSessions
<details><summary><code>client.checkout_sessions.<a href="src/fern/checkout_sessions/client.py">create_checkout_session</a>(...) -> CheckoutSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initializes a new checkout session from items and (optionally) buyer and fulfillment info.
MUST return 201 with a rich, authoritative cart state.

Agents MAY include `affiliate_attribution` with `touchpoint: "first"` to record first-touch attribution.
This enables multi-touch attribution models where networks can capture both first and last touch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Item
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_version="<API-Version>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkout_sessions.create_checkout_session(
    items=[
        Item(
            id="item_123",
            quantity=1,
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

**items:** `typing.List[Item]` 
    
</dd>
</dl>

<dl>
<dd>

**buyer:** `typing.Optional[Buyer]` 
    
</dd>
</dl>

<dl>
<dd>

**fulfillment_details:** `typing.Optional[FulfillmentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**affiliate_attribution:** `typing.Optional[AffiliateAttribution]` 
    
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

<details><summary><code>client.checkout_sessions.<a href="src/fern/checkout_sessions/client.py">get_checkout_session</a>(...) -> CheckoutSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest authoritative state for the checkout session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_version="<API-Version>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkout_sessions.get_checkout_session(
    checkout_session_id="checkout_session_id",
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

**checkout_session_id:** `str` 
    
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

<details><summary><code>client.checkout_sessions.<a href="src/fern/checkout_sessions/client.py">update_checkout_session</a>(...) -> CheckoutSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies changes (items, fulfillment address, fulfillment option) and returns an updated authoritative cart state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SelectedFulfillmentOptionZero, SelectedFulfillmentOptionZeroType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_version="<API-Version>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkout_sessions.update_checkout_session(
    checkout_session_id="checkout_session_id",
    selected_fulfillment_options=[
        SelectedFulfillmentOptionZero(
            type=SelectedFulfillmentOptionZeroType.SHIPPING,
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

**checkout_session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**buyer:** `typing.Optional[Buyer]` 
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[Item]]` 
    
</dd>
</dl>

<dl>
<dd>

**fulfillment_details:** `typing.Optional[FulfillmentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_fulfillment_options:** `typing.Optional[typing.List[SelectedFulfillmentOption]]` 
    
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

<details><summary><code>client.checkout_sessions.<a href="src/fern/checkout_sessions/client.py">complete_checkout_session</a>(...) -> CheckoutSessionWithOrder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finalizes the checkout by applying a payment method. MUST create an order and return completed state on success.

Agents MAY include `affiliate_attribution` to ensure the merchant receives final attribution context.
Attribution is stored alongside the resulting order but not returned in the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Buyer, PaymentData, PaymentDataProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_version="<API-Version>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkout_sessions.complete_checkout_session(
    checkout_session_id="checkout_session_id",
    buyer=Buyer(
        first_name="John",
        last_name="Smith",
        email="johnsmith@mail.com",
    ),
    payment_data=PaymentData(
        token="spt_123",
        provider=PaymentDataProvider.STRIPE,
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

**checkout_session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payment_data:** `PaymentData` 
    
</dd>
</dl>

<dl>
<dd>

**buyer:** `typing.Optional[Buyer]` 
    
</dd>
</dl>

<dl>
<dd>

**authentication_result:** `typing.Optional[AuthenticationResult]` 
    
</dd>
</dl>

<dl>
<dd>

**affiliate_attribution:** `typing.Optional[AffiliateAttribution]` 
    
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

<details><summary><code>client.checkout_sessions.<a href="src/fern/checkout_sessions/client.py">cancel_checkout_session</a>(...) -> CheckoutSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a session if not already completed or canceled.
Agents MAY include an intent_trace to communicate why the session is being abandoned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_version="<API-Version>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkout_sessions.cancel_checkout_session(
    checkout_session_id="checkout_session_id",
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

**checkout_session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**intent_trace:** `typing.Optional[IntentTrace]` 
    
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

