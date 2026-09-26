# Reference
<details><summary><code>client.<a href="src/fern/client.py">healthcheck_get</a>() -> str</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.healthcheck_get()

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

## Auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">login_to_create_access_token</a>(...) -> Token</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.auth.login_to_create_access_token(
    username="username",
    password="password",
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

**request:** `BodyLoginToCreateAccessToken` 
    
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

## Meta
<details><summary><code>client.meta.<a href="src/fern/meta/client.py">get_service_metadata</a>() -> Meta</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.meta.get_service_metadata()

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

## Acks
<details><summary><code>client.acks.<a href="src/fern/acks/client.py">acknowledge_payment</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

completes (ie. ack) request initiated by `/init` on the payments-gateway API
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
from fern import FernApi, SavedPaymentMethod

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.acks.acknowledge_payment(
    payment_id="payment_id",
    success=True,
    provider_payment_id="pi_123ABC",
    invoice_url="https://invoices.com/id=12345",
    saved=SavedPaymentMethod(
        success=True,
        payment_method_id="3FA85F64-5717-4562-B3FC-2C963F66AFA6",
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

**payment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**success:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_payment_id:** `typing.Optional[str]` — Payment ID from the provider (e.g. stripe payment ID)
    
</dd>
</dl>

<dl>
<dd>

**invoice_url:** `typing.Optional[str]` — Link to invoice is required when success=true
    
</dd>
</dl>

<dl>
<dd>

**invoice_pdf:** `typing.Optional[str]` — Link to invoice PDF
    
</dd>
</dl>

<dl>
<dd>

**stripe_invoice_id:** `typing.Optional[str]` — Stripe invoice ID
    
</dd>
</dl>

<dl>
<dd>

**stripe_customer_id:** `typing.Optional[str]` — Stripe customer ID
    
</dd>
</dl>

<dl>
<dd>

**saved:** `typing.Optional[SavedPaymentMethod]` — Gets the payment-method if user opted to save it during payment.If used did not opt to save of payment-method was already saved, then it defaults to None
    
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

<details><summary><code>client.acks.<a href="src/fern/acks/client.py">acknowledge_payment_method</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

completes (ie. ack) request initiated by `/payments-methods:init` on the payments-gateway API
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

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.acks.acknowledge_payment_method(
    payment_method_id="payment_method_id",
    success=True,
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

**payment_method_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**success:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
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

