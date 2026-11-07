# Reference
## Checkouts
<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">get_payment_methods</a>(...) -> GetPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get payment methods available for the given merchant to use with a checkout.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.get_payment_methods(
    merchant_code="MH4H92C7",
    amount=9.99,
    currency="EUR",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — The amount for which the payment methods should be eligible, in major units.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency for which the payment methods should be eligible.
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">list_checkouts</a>(...) -> typing.List[CheckoutSuccess]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists created checkout resources according to the applied `checkout_reference`.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.list_checkouts(
    checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
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

**checkout_reference:** `typing.Optional[str]` — Filters the list of checkout resources by the unique reference of the checkout.
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">create_checkout</a>(...) -> Checkout</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a payment checkout for the specified merchant, amount, and currency. Supply a `checkout_reference` to identify the payment attempt in your own systems. Creating a checkout does not charge a payment instrument.

Set `hosted_checkout.enabled` to `true` to receive a [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) URL where the customer can complete the payment.
Use `redirect_url` for redirect-based payment and 3DS flows. If `return_url` is provided, SumUp sends processing updates to that backend callback URL.

Complete the payment through [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) or the [Payment Widget](https://developer.sumup.com/online-payments/checkouts/card-widget).
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.create_checkout(
    checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
    amount=10.1,
    currency="EUR",
    merchant_code="MH4H92C7",
    description="Purchase",
    valid_until=datetime.datetime.fromisoformat("2020-02-29T10:56:56+00:00"),
    redirect_url="https://sumup.com",
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

**checkout_reference:** `str` — Merchant-defined reference for the new checkout. It should be unique enough for you to identify the payment attempt in your own systems.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — Amount to be charged to the payer, expressed in major units.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `Currency` 
    
</dd>
</dl>

<dl>
<dd>

**merchant_code:** `str` — Short unique identifier for the merchant that should receive the payment.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Short merchant-defined description shown in SumUp tools and reporting for easier identification of the checkout.
    
</dd>
</dl>

<dl>
<dd>

**return_url:** `typing.Optional[str]` — Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Merchant-scoped customer identifier. Required when setting up recurring payments and useful when the checkout should be linked to a returning payer.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[CheckoutCreateRequestPurpose]` — Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.
    
</dd>
</dl>

<dl>
<dd>

**valid_until:** `typing.Optional[datetime.datetime]` — Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — URL where the payer should be sent after a redirect-based payment or SCA flow completes. This is required for [APMs](https://developer.sumup.com/online-payments/apm/introduction) and recommended for card checkouts that may require [3DS](https://developer.sumup.com/online-payments/features/3ds). If it is omitted, the [Payment Widget](https://developer.sumup.com/online-payments/checkouts) can render the challenge in an iframe instead of using a full-page redirect.
    
</dd>
</dl>

<dl>
<dd>

**hosted_checkout:** `typing.Optional[HostedCheckout]` 
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">get_checkout</a>(...) -> CheckoutSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an identified checkout resource. Use this request after processing a checkout to confirm its status and inform the end user respectively.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.get_checkout(
    checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
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

**checkout_id:** `str` — Unique identifier of the checkout resource.
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">process_checkout</a>(...) -> ProcessCheckoutResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

:::caution[PCI DSS compliance required]
When you submit raw card details directly to the Checkout API, your systems store, process, or transmit cardholder data and are therefore subject to applicable [PCI DSS requirements](https://www.pcisecuritystandards.org/document_library/). You should only use this integration if your environment is appropriately PCI DSS compliant.
:::

Processing a checkout will attempt to charge the provided payment instrument for the amount of the specified checkout resource initiated in the `Create a checkout` endpoint.

Follow this request with `Retrieve a checkout` to confirm its status.
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
from fern import FernApi, MandatePayload, Card
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.process_checkout(
    checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
    payment_type="card",
    installments=1,
    mandate=MandatePayload(
        type="recurrent",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        user_ip="172.217.169.174",
    ),
    card=Card(
        name="John Doe",
        number="1234567890123456",
        expiry_year="2023",
        expiry_month="01",
        cvv="123",
        zip_code="12345",
        type="VISA",
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

**checkout_id:** `str` — Unique identifier of the checkout resource.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `ProcessCheckoutPaymentType` — Payment method used for this processing attempt. It determines which additional request fields are required.
    
</dd>
</dl>

<dl>
<dd>

**installments:** `typing.Optional[int]` — Number of installments for deferred payments. Available only to merchant users in Brazil.
    
</dd>
</dl>

<dl>
<dd>

**mandate:** `typing.Optional[MandatePayload]` 
    
</dd>
</dl>

<dl>
<dd>

**card:** `typing.Optional[Card]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pay:** `typing.Optional[typing.Dict[str, typing.Any]]` — Raw `PaymentData` object received from Google Pay. Send the Google Pay response payload as-is.
    
</dd>
</dl>

<dl>
<dd>

**apple_pay:** `typing.Optional[typing.Dict[str, typing.Any]]` — Raw payment token object received from Apple Pay. Send the Apple Pay response payload as-is.
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — Saved-card token to use instead of raw card details when processing with a previously stored payment instrument.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer identifier associated with the saved payment instrument. Required when `token` is provided.
    
</dd>
</dl>

<dl>
<dd>

**personal_details:** `typing.Optional[PersonalDetails]` 
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">deactivate_checkout</a>(...) -> Checkout</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivates an identified checkout resource. If the checkout has already been processed it can not be deactivated.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.deactivate_checkout(
    checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
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

**checkout_id:** `str` — Unique identifier of the checkout resource.
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">update_checkout</a>(...) -> Checkout</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the amount, currency, description, reference, expiration, or customer associated with an existing checkout. Only the supplied fields are updated.

This request changes the checkout details; it does not charge a payment instrument. Process the checkout separately to attempt a payment.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.update_checkout(
    checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
    amount=12.5,
    currency="EUR",
    description="Updated purchase",
    checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
    valid_until=datetime.datetime.fromisoformat("2020-02-29T10:56:56+00:00"),
    customer_id="831ff8d4cd5958ab5670",
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

**checkout_id:** `str` — Unique identifier of the checkout resource.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Updated amount to be charged to the payer, expressed in major units.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated short merchant-defined description shown in SumUp tools and reporting.
    
</dd>
</dl>

<dl>
<dd>

**checkout_reference:** `typing.Optional[str]` — Updated merchant-defined reference for the checkout.
    
</dd>
</dl>

<dl>
<dd>

**valid_until:** `typing.Optional[datetime.datetime]` — Updated expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Updated merchant-scoped customer identifier associated with the checkout.
    
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

<details><summary><code>client.checkouts.<a href="src/fern/checkouts/client.py">create_apple_pay_session</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Apple Pay merchant session for the specified checkout.

Use this endpoint after the customer selects Apple Pay and before calling
`ApplePaySession.completeMerchantValidation(...)` in the browser.
SumUp validates the merchant session request and returns the Apple Pay
session object that your frontend should pass to Apple's JavaScript API.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.checkouts.create_apple_pay_session(
    checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
    context="example.com",
    target="https://apple-pay-gateway-cert.apple.com/paymentservices/startSession",
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

**checkout_id:** `str` — Unique identifier of the checkout resource.
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` — the context to create this apple pay session.
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — The target url to create this apple pay session.
    
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

## Customers
<details><summary><code>client.customers.<a href="src/fern/customers/client.py">create_customer</a>(...) -> Customer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new saved customer resource which you can later manipulate and save payment instruments to.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.create_customer(
    customer_id="831ff8d4cd5958ab5670",
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

**request:** `Customer` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">get_customer</a>(...) -> Customer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an identified saved customer resource through the unique `customer_id` parameter, generated upon customer creation.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.get_customer(
    customer_id="831ff8d4cd5958ab5670",
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

**customer_id:** `str` — Unique identifier of the saved customer resource.
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">update_customer</a>(...) -> Customer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an identified saved customer resource's personal details.

The request only overwrites the parameters included in the request, all other parameters will remain with their initially assigned values.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.update_customer(
    customer_id="831ff8d4cd5958ab5670",
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

**customer_id:** `str` — Unique identifier of the saved customer resource.
    
</dd>
</dl>

<dl>
<dd>

**personal_details:** `typing.Optional[PersonalDetails]` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">list_payment_instruments</a>(...) -> typing.List[PaymentInstrumentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all payment instrument resources that are saved for an identified customer.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.list_payment_instruments(
    customer_id="831ff8d4cd5958ab5670",
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

**customer_id:** `str` — Unique identifier of the saved customer resource.
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">deactivate_payment_instrument</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivates an identified card payment instrument resource for a customer.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.deactivate_payment_instrument(
    customer_id="831ff8d4cd5958ab5670",
    token="bcfc8e5f-3b47-4cb9-854b-3b7a4cce7be3",
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

**customer_id:** `str` — Unique identifier of the saved customer resource.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — Unique token identifying the card saved as a payment instrument resource.
    
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

## Transactions
<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">refund_transaction</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refunds an identified transaction either in full or partially.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.transactions.refund_transaction(
    merchant_code="MH4H92C7",
    transaction_id="4ffb8dfc-7f2b-413d-a497-2ad00766585e",
    amount=5,
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — Unique identifier of the transaction.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Amount to be refunded. Eligible amount can't exceed the amount of the transaction and varies based on country and currency. If you do not specify a value, the system performs a full refund of the transaction.
    
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

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">get_transaction_v21</a>(...) -> TransactionFull</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the full details of an identified transaction. The transaction resource is identified by a query parameter and *one* of following parameters is required:
- `id`
- `transaction_code`
- `foreign_transaction_id`
- `client_transaction_id`
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
    environment=FernApiEnvironment.DEFAULT,
)

client.transactions.get_transaction_v21(
    merchant_code="MH4H92C7",
    id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
    transaction_code="TEENSK4W2K",
    foreign_transaction_id="J13253253x1",
    client_transaction_id="urn:sumup:pos:sale:MNKKNGST:1D4E3B2D-111D-48D7-9AF0-832DAEF63DD7;2",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Retrieves the transaction resource with the specified transaction ID (the `id` parameter in the transaction resource).
    
</dd>
</dl>

<dl>
<dd>

**transaction_code:** `typing.Optional[str]` — Retrieves the transaction resource with the specified transaction code.
    
</dd>
</dl>

<dl>
<dd>

**foreign_transaction_id:** `typing.Optional[str]` — External transaction identifier supplied by the client.
    
</dd>
</dl>

<dl>
<dd>

**client_transaction_id:** `typing.Optional[str]` — Client-supplied identifier of the transaction.
    
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

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">list_transactions_v21</a>(...) -> ListTransactionsV21Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists detailed history of all transactions associated with the merchant profile.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transactions.list_transactions_v21(
    merchant_code="MH4H92C7",
    transaction_code="TEENSK4W2K",
    limit=10,
    changes_since=datetime.datetime.fromisoformat("2019-08-28T09:00:00+00:00"),
    newest_time=datetime.datetime.fromisoformat("2019-08-29T09:00:00+00:00"),
    newest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
    oldest_time=datetime.datetime.fromisoformat("2019-08-28T09:00:00+00:00"),
    oldest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**transaction_code:** `typing.Optional[str]` — Retrieves the transaction resource with the specified transaction code.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTransactionsV21RequestOrder]` — Specifies the order in which the returned results are displayed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Specifies the maximum number of results per page. Value must be a positive integer and if not specified, will return 10 results.
    
</dd>
</dl>

<dl>
<dd>

**users_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters the returned results by user email.
    
</dd>
</dl>

<dl>
<dd>

**statuses_array:** `typing.Optional[typing.Union[ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]]]` — Filters the returned results by the specified list of final statuses of the transactions.
    
</dd>
</dl>

<dl>
<dd>

**payment_types_array:** `typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]]` — Filters the returned results by the specified list of payment types used for the transactions.
    
</dd>
</dl>

<dl>
<dd>

**entry_modes_array:** `typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]]` — Filters the returned results by the specified list of entry modes.
    
</dd>
</dl>

<dl>
<dd>

**types_array:** `typing.Optional[typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]]` — Filters the returned results by the specified list of transaction types.
    
</dd>
</dl>

<dl>
<dd>

**changes_since:** `typing.Optional[datetime.datetime]` — Filters the results by the latest modification time of resources and returns only transactions that are modified *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).
    
</dd>
</dl>

<dl>
<dd>

**newest_time:** `typing.Optional[datetime.datetime]` — Filters the results by the creation time of resources and returns only transactions that are created *before* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).
    
</dd>
</dl>

<dl>
<dd>

**newest_ref:** `typing.Optional[str]` — Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *smaller* than the specified value. This parameters supersedes the `newest_time` parameter (if both are provided in the request).
    
</dd>
</dl>

<dl>
<dd>

**oldest_time:** `typing.Optional[datetime.datetime]` — Filters the results by the creation time of resources and returns only transactions that are created *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).
    
</dd>
</dl>

<dl>
<dd>

**oldest_ref:** `typing.Optional[str]` — Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *greater* than the specified value. This parameters supersedes the `oldest_time` parameter (if both are provided in the request).
    
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

## Payouts
<details><summary><code>client.payouts.<a href="src/fern/payouts/client.py">list_payouts_v1</a>(...) -> FinancialPayouts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists payout and payout-deduction records for the specified merchant account within the requested date range.

The response can include:
- regular payouts (`type = PAYOUT`)
- deduction records for refunds, chargebacks, direct debit returns, or balance adjustments

Results are sorted by payout date in the requested `order`.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payouts.list_payouts_v1(
    merchant_code="MH4H92C7",
    start_date=datetime.date.fromisoformat("2024-02-01"),
    end_date=datetime.date.fromisoformat("2024-02-29"),
    limit=10,
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`). Must be greater than or equal to `start_date`.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ListPayoutsV1RequestFormat]` — Response format for the payout list.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of payout records to return.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListPayoutsV1RequestOrder]` — Sort direction for the returned payouts.
    
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

## Receipts
<details><summary><code>client.receipts.<a href="src/fern/receipts/client.py">get_receipt</a>(...) -> Receipt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves receipt specific data for a transaction.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.receipts.get_receipt(
    transaction_id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
    mid="MH4H92C7",
    tx_event_id=9567461191,
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

**transaction_id:** `str` — SumUp unique transaction ID or transaction code, e.g. TS7HDYLSKD.
    
</dd>
</dl>

<dl>
<dd>

**mid:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**tx_event_id:** `typing.Optional[int]` — Unique identifier of the transaction event to include on the receipt.
    
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

## Readers
<details><summary><code>client.readers.<a href="src/fern/readers/client.py">create_go_reader_checkout</a>(...) -> ReaderPaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates a payment on the SumUp Go terminal identified by the reader ID.

Use `client_transaction_id` as an idempotency key: retrying the request with the same value returns the result of the original payment instead of creating a duplicate.
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
from fern import FernApi, Amount
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.create_go_reader_checkout(
    merchant_code="MK10CL2A",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
    client_transaction_id="19e12390-72cf-4f9f-80b5-b0c8a67fa43f",
    total_amount=Amount(
        currency="MXN",
        value=1000,
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `ReaderId` — The unique identifier of the reader.
    
</dd>
</dl>

<dl>
<dd>

**client_transaction_id:** `str` — Caller-supplied correlation identifier, used as the idempotency key.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `Amount` 
    
</dd>
</dl>

<dl>
<dd>

**affiliate:** `typing.Optional[Affiliate]` 
    
</dd>
</dl>

<dl>
<dd>

**tip_amount:** `typing.Optional[int]` — Optional tip amount in minor units, added on top of total_amount.
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">list_readers</a>(...) -> ListReadersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all readers of the merchant.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.list_readers(
    merchant_code="MK10CL2A",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">create_reader</a>(...) -> Reader</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Reader for the merchant account.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.create_reader(
    merchant_code="MK10CL2A",
    pairing_code="4WLFDSBF",
    name="Frontdesk",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**pairing_code:** `ReaderPairingCode` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `ReaderName` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` 
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">get_reader</a>(...) -> Reader</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a Reader.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.get_reader(
    merchant_code="MK10CL2A",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `ReaderId` — The unique identifier of the reader.
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` 

Return the reader only if it has been modified after the specified timestamp given in the headers.

Timestamps are accepted in the following formats:

 - HTTP Standard: [IMF format (RFC 5322)](https://www.rfc-editor.org/rfc/rfc5322#section-3.3), sometimes also referred to as [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.1.1).
 - RFC 3339: Used for timestamps in JSON payloads on this API.
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">delete_reader</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a reader.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.delete_reader(
    merchant_code="MK10CL2A",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `ReaderId` — The unique identifier of the reader.
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">update_reader</a>(...) -> Reader</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a reader's name or metadata and returns the updated reader.

Providing `metadata` replaces the entire metadata object; include all entries that should be retained. Omitted fields remain unchanged.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.update_reader(
    merchant_code="MK10CL2A",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `ReaderId` — The unique identifier of the reader.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ReaderName]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` 
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">create_reader_checkout</a>(...) -> CreateReaderCheckoutResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Checkout for a Reader.

This process is asynchronous and the actual transaction may take some time to be started on the device.


There are some caveats when using this endpoint:
* The target device must be online, otherwise checkout won't be accepted
* After the checkout is accepted, the system has 60 seconds to start the payment on the target device. During this time, any other checkout for the same device will be rejected.


**Note**: If the target device is a Solo, it must be in version 3.3.24.3 or higher.
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
from fern.readers import CreateReaderCheckoutRequestAade, CreateReaderCheckoutRequestAffiliate, CreateReaderCheckoutRequestTotalAmount

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.create_reader_checkout(
    merchant_code="MC0X0ABC",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
    aade=CreateReaderCheckoutRequestAade(
        provider_id="123",
        signature="QjcxRDdBNTU1MDcyRTNFRTREMkZEM0Y0NTdBMjkxMTU4MzBFNkNCQTs7MjAyNTExMTIyMTQ3MTM7Nzk2OzEwNDs5MDA7OTAwOzU0ODg5MDM5",
        signature_data="B71D7A555072E3EE4D2FD3F457A29115830E6CBA;;20251112214713;796;104;900;900;54889039",
    ),
    affiliate=CreateReaderCheckoutRequestAffiliate(
        app_id="com.example.app",
        foreign_transaction_id="123456",
        key="ef7b684a-d6f4-4e93-9b1b-6acdd6564a8e",
        tags={
            "key": "value"
        },
    ),
    card_type="debit",
    description="This is a description...",
    installments=1,
    return_url="https://webhook.site/e21ddbb0-42c4-4358-a981-f5a95cd86fb5",
    tip_rates=[
        0.05,
        0.1,
        0.15
    ],
    tip_timeout=60,
    total_amount=CreateReaderCheckoutRequestTotalAmount(
        currency="EUR",
        minor_unit=2,
        value=5033,
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

**merchant_code:** `str` — Merchant Code
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `str` — The unique identifier of the Reader
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `CreateReaderCheckoutRequestTotalAmount` 

Amount structure.

The amount is represented as an integer value altogether with the currency and the minor unit.

For example, EUR 1.00 is represented as value 100 with minor unit of 2.
    
</dd>
</dl>

<dl>
<dd>

**aade:** `typing.Optional[CreateReaderCheckoutRequestAade]` 

Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.
    
</dd>
</dl>

<dl>
<dd>

**affiliate:** `typing.Optional[CreateReaderCheckoutRequestAffiliate]` 

Affiliate metadata for the transaction.
It is a field that allow for integrators to track the source of the transaction.
    
</dd>
</dl>

<dl>
<dd>

**card_type:** `typing.Optional[CreateReaderCheckoutRequestCardType]` 

The card type of the card used for the transaction.
Is is required only for some countries (e.g: Brazil).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the checkout to be shown in the Merchant Sales
    
</dd>
</dl>

<dl>
<dd>

**installments:** `typing.Optional[int]` 

Number of installments for the transaction.
It may vary according to the merchant country.
For example, in Brazil, the maximum number of installments is 12.

Omit if the merchant country does support installments.
Otherwise, the checkout will be rejected.
    
</dd>
</dl>

<dl>
<dd>

**return_url:** `typing.Optional[str]` 

Webhook URL to which the payment result will be sent.
It must be a HTTPS url.
    
</dd>
</dl>

<dl>
<dd>

**tip_rates:** `typing.Optional[typing.List[float]]` 

List of tipping rates to be displayed to the cardholder.
The rates are in percentage and should be between 0.01 and 0.99.
The list should be sorted in ascending order.
    
</dd>
</dl>

<dl>
<dd>

**tip_timeout:** `typing.Optional[int]` 

Time in seconds the cardholder has to select a tip rate.
If not provided, the default value is 30 seconds.

It can only be set if `tip_rates` is provided.

**Note**: If the target device is a Solo, it must be in version 3.3.38.0 or higher.
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">get_reader_status</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the last known status for a Reader.

This endpoint allows you to retrieve updates from the connected card reader, including the current screen being displayed during the payment process and the device status (battery level, connectivity, and update state).

Supported States

* `IDLE` – Reader ready for next transaction
* `SELECTING_TIP` – Waiting for tip input
* `WAITING_FOR_CARD` – Awaiting card insert/tap
* `WAITING_FOR_PIN` – Waiting for PIN entry
* `WAITING_FOR_SIGNATURE` – Waiting for customer signature
* `UPDATING_FIRMWARE` – Firmware update in progress

Device Status

* `ONLINE` – Device connected and operational
* `OFFLINE` – Device disconnected (last state persisted)

**Note**: If the target device is a Solo, it must be in version 3.3.39.0 or higher.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.get_reader_status(
    merchant_code="MC0X0ABC",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
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

**merchant_code:** `str` — Merchant Code
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `str` — The unique identifier of the Reader
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">create_reader_terminate</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate a Reader Checkout stops the current transaction on the target device.

This process is asynchronous and the actual termination may take some time to be performed on the device.


There are some caveats when using this endpoint:
* The target device must be online, otherwise terminate won't be accepted
* The action will succeed only if the device is waiting for cardholder action: e.g: waiting for card, waiting for PIN, etc.
* There is no confirmation of the termination.

If a transaction is successfully terminated and `return_url` was provided on Checkout, the transaction status will be sent as `failed` to the provided URL.


**Note**: If the target device is a Solo, it must be in version 3.3.28.0 or higher.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.create_reader_terminate(
    merchant_code="MC0X0ABC",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
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

**merchant_code:** `str` — Merchant Code
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `str` — The unique identifier of the Reader
    
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

<details><summary><code>client.readers.<a href="src/fern/readers/client.py">get_reader_checkout</a>(...) -> GetReaderCheckoutResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Checkout for a Reader.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.readers.get_reader_checkout(
    merchant_code="MC0X0ABC",
    reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
    checkout_id="74ecff66-1655-43ed-8ce3-193f49fa602f",
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

**merchant_code:** `str` — Merchant Code
    
</dd>
</dl>

<dl>
<dd>

**reader_id:** `str` — The unique identifier of the Reader
    
</dd>
</dl>

<dl>
<dd>

**checkout_id:** `str` — The unique identifier of the Checkout
    
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

## Memberships
<details><summary><code>client.memberships.<a href="src/fern/memberships/client.py">list_memberships</a>(...) -> ListMembershipsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List memberships of the current user.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.memberships.list_memberships(
    offset=0,
    limit=10,
    kind="merchant",
    resource_type="merchant",
    resource_parent_type="merchant",
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

**offset:** `typing.Optional[int]` — Offset of the first member to return.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of members to return.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[ResourceType]` — Filter memberships by resource kind.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MembershipStatus]` — Filter the returned memberships by the membership status.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[ResourceType]` — Filter memberships by resource kind.
    
</dd>
</dl>

<dl>
<dd>

**resource_attributes_sandbox:** `typing.Optional[bool]` — Filter memberships by the sandbox status of the resource the membership is in.
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `typing.Optional[str]` — Filter memberships by the name of the resource the membership is in.
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Filter memberships by the ID of the resource the membership is in.
    
</dd>
</dl>

<dl>
<dd>

**resource_parent_id:** `typing.Optional[str]` 

Filter memberships by the parent of the resource the membership is in.
Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.
    
</dd>
</dl>

<dl>
<dd>

**resource_parent_type:** `typing.Optional[ResourceType]` 

Filter memberships by the parent of the resource the membership is in.
Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter the returned memberships by role.
    
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

## Members
<details><summary><code>client.members.<a href="src/fern/members/client.py">list_merchant_members</a>(...) -> ListMerchantMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists merchant members.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.list_merchant_members(
    merchant_code="MK10CL2A",
    offset=0,
    limit=10,
    scroll=True,
    email="user",
    user_id="245b2ead-85bf-45ff-856f-311a88a5d454",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset of the first member to return.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of members to return.
    
</dd>
</dl>

<dl>
<dd>

**scroll:** `typing.Optional[bool]` — Indicates to skip count query.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter the returned members by email address prefix.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Search for a member by user id.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MembershipStatus]` — Filter the returned members by the membership status.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter the returned members by role.
    
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

<details><summary><code>client.members.<a href="src/fern/members/client.py">create_merchant_member</a>(...) -> Member</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a member to the merchant account with the specified roles.

By default, sends an invitation email to the provided address. The recipient must accept the invitation to join the account.
When `is_managed_user` is `true`, creates a managed user with the provided password and optional nickname and assigns the roles directly, without sending an invitation.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.create_merchant_member(
    merchant_code="MK10CL2A",
    email="karl.berg@example.com",
    roles=[
        "role_employee"
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the member to add.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — List of roles to assign to the new member.
    
</dd>
</dl>

<dl>
<dd>

**is_managed_user:** `typing.Optional[bool]` — True if the user is managed by the merchant. In this case, we'll created a virtual user with the provided password and nickname.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password of the member to add. Only used if `is_managed_user` is true. In the case of service accounts, the password is not used and can not be defined by the caller.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — Nickname of the member to add. Only used if `is_managed_user` is true. Used for display purposes only.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[Attributes]` 
    
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

<details><summary><code>client.members.<a href="src/fern/members/client.py">get_merchant_member</a>(...) -> Member</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a merchant member.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.get_merchant_member(
    merchant_code="MK10CL2A",
    member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — The ID of the member to retrieve.
    
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

<details><summary><code>client.members.<a href="src/fern/members/client.py">update_merchant_member</a>(...) -> Member</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a merchant member and returns the updated member.

Providing `roles` replaces the member's assigned roles and can grant or revoke access. Providing `metadata` replaces the entire metadata object.
For managed users, `user.nickname` changes the display name and `user.password` replaces the password. Updating the password also enables the managed user account.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.update_merchant_member(
    merchant_code="MK10CL2A",
    member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — The ID of the member to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[Attributes]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[UpdateMerchantMemberRequestUser]` — Allows you to update user data of managed users.
    
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

<details><summary><code>client.members.<a href="src/fern/members/client.py">delete_merchant_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a merchant member.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.delete_merchant_member(
    merchant_code="MK10CL2A",
    member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — The ID of the member to retrieve.
    
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

## Roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">list_merchant_roles</a>(...) -> ListMerchantRolesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List merchant's custom roles.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.list_merchant_roles(
    merchant_code="MK10CL2A",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">create_merchant_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom role for the merchant. Roles are defined by the set of permissions that they grant to the members that they are assigned to.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.create_merchant_role(
    merchant_code="MK10CL2A",
    name="Senior Shop Manager II",
    permissions=[
        "catalog_access",
        "taxes_access",
        "members_access"
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — User-defined name of the role.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.List[str]` — User's permissions.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — User-defined description of the role.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_merchant_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a custom role by ID.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.get_merchant_role(
    merchant_code="MK10CL2A",
    role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — The ID of the role to retrieve.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">delete_merchant_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom role.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.delete_merchant_role(
    merchant_code="MK10CL2A",
    role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — The ID of the role to retrieve.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">update_merchant_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a custom role's name, description, or permissions and returns the updated role.

Providing `permissions` replaces the role's permission list and changes the access granted to members assigned to that role. Omitted fields remain unchanged.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.update_merchant_role(
    merchant_code="MK10CL2A",
    role_id="role_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
    name="Senior Shop Manager III",
    permissions=[
        "catalog_edit",
        "taxes_access",
        "members_edit"
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — The ID of the role to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — User-defined name of the role.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[str]]` — User's permissions.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — User-defined description of the role.
    
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

## Merchants
<details><summary><code>client.merchants.<a href="src/fern/merchants/client.py">get_merchant</a>(...) -> Merchant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a Merchant for a valid Merchant code.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.merchants.get_merchant(
    merchant_code="MK10CL2A",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
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

<details><summary><code>client.merchants.<a href="src/fern/merchants/client.py">list_persons</a>(...) -> ListPersonsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Persons related to a Merchant.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.merchants.list_persons(
    merchant_code="MK10CL2A",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
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

<details><summary><code>client.merchants.<a href="src/fern/merchants/client.py">get_person</a>(...) -> Person</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single Person related to a Merchant.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.merchants.get_person(
    merchant_code="MK10CL2A",
    person_id="pers_5AKFHN2KSK8D3TS79DJE3P3A2Z",
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

**merchant_code:** `str` — Short unique identifier for the merchant.
    
</dd>
</dl>

<dl>
<dd>

**person_id:** `str` — Person ID
    
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

