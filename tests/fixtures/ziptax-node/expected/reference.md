# Reference
## Account
<details><summary><code>client.account.<a href="src/fern/account/client.py">get_account_metrics</a>(...) -> MetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns usage metrics for the authenticated account
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.account.get_account_metrics()

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

**key:** `typing.Optional[str]` — API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.
    
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_account_metrics_v60</a>(...) -> MetricsV60Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns usage metrics for the authenticated account in the simplified v6.0 format. In v6.0 all keys are geo keys, so the counters reflect geo usage.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.account.get_account_metrics_v60()

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

**key:** `typing.Optional[str]` — API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.
    
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

## Data
<details><summary><code>client.data.<a href="src/fern/data/client.py">get_tic_data</a>(...) -> TicResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Taxability Information Code (TIC) data
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.data.get_tic_data()

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

**format:** `typing.Optional[GetTicDataRequestFormat]` — Serialization format of the response body: 'json' (default) or 'xml'.
    
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

## MerchantTaxCloud
<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_cart_calculate</a>(...) -> MerchantCartCalculateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculates sales tax for one or more carts on behalf of a merchant. The request contract is the same for both merchant management modes, so a caller does not have to know which mode a merchant is in. TaxCloud-managed merchant: the request is forwarded to TaxCloud (POST /connections/{connectionId}/carts) using the merchant's stored credentials and TaxCloud's response is returned verbatim; capture the returned cartId with /merchant/order/create-from-cart to record the sale. Self-managed merchant: the cart is calculated in-process by the Ziptax rate engine, US destinations only, and nothing is persisted - the returned cartId correlates the response with the request and cannot be captured as an order, and the other stateful /merchant endpoints return 403. Self-managed calculation rejects (rather than ignores) fields it cannot honour: discounts, exemption, deliveredBySeller, productId, and any currency other than USD. A value that asks for nothing is accepted, so a caller that always emits the TaxCloud shape is not refused: deliveredBySeller false, and an exemption claiming no exemption ({} or {"isExempt": false}). TIC vocabulary also differs: self-managed carts use Ziptax TICs, where 10001 is shipping and 11000 is handling, and TaxCloud's shipping TICs 11010-11015 and the Colorado retail delivery fee TIC 11098 are rejected with 400 because they cannot be mapped onto the in-process shipping and handling treatment. A self-managed interstate cart whose destination address cannot be resolved returns 422 rather than being sourced at its origin, which would quote another state's rate. A self-managed request may contain at most 2500 line items summed across all carts; a larger batch is rejected with 400 before any cart is calculated. Calculation has no lasting side effect in either mode and is safe to retry.
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
from fern import FernApi, TaxCloudCart, TaxCloudCurrency, TaxCloudAddress, TaxCloudCartItem
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_cart_calculate(
    items=[
        TaxCloudCart(
            currency=TaxCloudCurrency(),
            customer_id="customer-453",
            destination=TaxCloudAddress(
                city="Minneapolis",
                line1="323 Washington Ave N",
                state="MN",
                zip="55401-2427",
            ),
            line_items=[
                TaxCloudCartItem(
                    index=0,
                    item_id="item-1",
                    price=10.75,
                    quantity=1.5,
                )
            ],
            origin=TaxCloudAddress(
                city="Minneapolis",
                line1="323 Washington Ave N",
                state="MN",
                zip="55401-2427",
            ),
        )
    ],
    merchant_id="merchantId",
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

**items:** `typing.List[TaxCloudCart]` — The carts to calculate tax for. Most integrations send a single cart; up to 100 carts may be calculated in one call.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant whose TaxCloud connection is used. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date:** `typing.Optional[datetime.datetime]` — RFC3339 datetime the carts are calculated for. Defaults to the current time when omitted.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_cert_create</a>(...) -> TaxCloudCertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an exemption certificate for one of the merchant's customers. The request is forwarded to TaxCloud POST /connections/{connectionId}/exemption-certificates using the merchant's stored credentials and TaxCloud's response is returned verbatim. Reference the returned certificateId as exemptionId on carts and orders to apply the exemption. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
from fern import FernApi, TaxCloudAddress, TaxCloudExemptState
from fern.environment import FernApiEnvironment
from fern.merchant_tax_cloud import MerchantCertCreateRequestCustomerBusinessType, MerchantCertCreateRequestReason

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_cert_create(
    address=TaxCloudAddress(
        city="Minneapolis",
        line1="323 Washington Ave N",
        state="MN",
        zip="55401-2427",
    ),
    customer_business_type=MerchantCertCreateRequestCustomerBusinessType.ACCOMMODATION_AND_FOOD_SERVICES,
    customer_id="customer-453",
    customer_name="Mr. Francis Exempt",
    merchant_id="merchantId",
    reason=MerchantCertCreateRequestReason.FEDERAL_GOVERNMENT,
    reason_description="reasonDescription",
    states=[
        TaxCloudExemptState(
            abbreviation="MN",
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

**address:** `TaxCloudAddress` — Address of the exempt customer.
    
</dd>
</dl>

<dl>
<dd>

**customer_business_type:** `MerchantCertCreateRequestCustomerBusinessType` — The type of business the customer is.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — Your identifier for the exempt customer. Carts and orders submitted with this customerId can use the certificate.
    
</dd>
</dl>

<dl>
<dd>

**customer_name:** `str` — Name of the customer or organization the certificate is issued to.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `MerchantCertCreateRequestReason` — The reason the customer is exempt from sales tax.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `str` — Short free-text elaboration of the exemption reason (maximum 20 characters).
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.List[TaxCloudExemptState]` — The states the certificate is valid in, each as a two-letter abbreviation object.
    
</dd>
</dl>

<dl>
<dd>

**customer_business_description:** `typing.Optional[str]` — Free-text description of the business. Provide when customerBusinessType is Other.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_cert_delete</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes (disables) an exemption certificate so it can no longer be applied to new transactions. The request is forwarded to TaxCloud DELETE /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_cert_delete(
    certificate_id="certificateId",
    merchant_id="merchantId",
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

**certificate_id:** `str` — The certificateId returned when the exemption certificate was created.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_cert_get</a>(...) -> TaxCloudCertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a single exemption certificate. The request is forwarded to TaxCloud GET /connections/{connectionId}/exemption-certificates/{certificateId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_cert_get(
    certificate_id="certificateId",
    merchant_id="merchantId",
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

**certificate_id:** `str` — The certificateId returned when the exemption certificate was created.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_cert_list</a>(...) -> TaxCloudCertListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the merchant's exemption certificates with cursor-based pagination. The request is forwarded to TaxCloud GET /exemption-certificates, scoped to the merchant's connection, with the optional filter fields mapped onto the query string; TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_cert_list(
    merchant_id="merchantId",
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

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort results in ascending order. Defaults to false (descending).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from the nextCursor field of a previous response. Omit to start at the first page.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter results to certificates belonging to this customerId.
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Set true to list disabled (revoked) certificates instead of active ones. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of certificates to return per page. Defaults to 20; maximum 100.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[MerchantCertListRequestSortBy]` — The field to sort results by: 'createdDate' or 'id'. Defaults to 'id'.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_order_create</a>(...) -> TaxCloudOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records an order directly, without a prior cart calculation; the tax amounts on each line item are the amounts your checkout collected. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
from fern import FernApi, TaxCloudCurrency, TaxCloudAddress, TaxCloudCartItemWithTax, TaxCloudTax
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_order_create(
    completed_date=datetime.datetime.fromisoformat("2024-08-01T14:00:00+00:00"),
    currency=TaxCloudCurrency(),
    customer_id="customer-453",
    destination=TaxCloudAddress(
        city="Minneapolis",
        line1="323 Washington Ave N",
        state="MN",
        zip="55401-2427",
    ),
    line_items=[
        TaxCloudCartItemWithTax(
            index=0,
            item_id="item-1",
            price=10.75,
            quantity=1.5,
            tax=TaxCloudTax(
                amount=1.31,
                rate=0.08125,
            ),
        )
    ],
    merchant_id="merchantId",
    order_id="my-order-1",
    origin=TaxCloudAddress(
        city="Minneapolis",
        line1="323 Washington Ave N",
        state="MN",
        zip="55401-2427",
    ),
    transaction_date=datetime.datetime.fromisoformat("2024-08-01T14:00:00+00:00"),
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

**completed_date:** `datetime.datetime` — RFC3339 datetime the order was shipped on, which created the tax liability.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `TaxCloudCurrency` — The currency the line-item prices and tax amounts are denominated in.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — Your identifier for the customer in your own system. Used to match exemption certificates and order history.
    
</dd>
</dl>

<dl>
<dd>

**destination:** `TaxCloudAddress` — The ship-to (destination) address of the sale.
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.List[TaxCloudCartItemWithTax]` — The items on the order, each including the tax rate and amount that was collected.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — Your identifier for the order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `TaxCloudAddress` — The ship-from (origin) address of the sale.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date:** `datetime.datetime` — RFC3339 datetime the order was purchased on.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` — Optional batch ID for grouping related orders.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — The sales channel the order came from. Pass one of amazon, ebay, or walmart to exclude marketplace-collected tax from filing.
    
</dd>
</dl>

<dl>
<dd>

**delivered_by_seller:** `typing.Optional[bool]` — Whether the seller delivers the order directly (own vehicles) rather than via common carrier. Affects taxability of delivery charges in some states.
    
</dd>
</dl>

<dl>
<dd>

**discounts:** `typing.Optional[TaxCloudDiscounts]` — Optional line-item and order-level discounts to apply. If omitted, prices are used as is.
    
</dd>
</dl>

<dl>
<dd>

**exclude_from_filing:** `typing.Optional[bool]` — Whether to exclude the order from tax filing.
    
</dd>
</dl>

<dl>
<dd>

**exemption:** `typing.Optional[TaxCloudExemption]` — Optional exemption information for the customer.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[MerchantOrderCreateRequestKind]` — The kind of order: 'order' for a sale (default) or 'credit' for a credit order.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_order_create_from_cart</a>(...) -> TaxCloudOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Captures a cart previously calculated with /merchant/cart/calculate as a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/carts/orders using the merchant's stored credentials and TaxCloud's response is returned verbatim. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_order_create_from_cart(
    cart_id="my-cart-1",
    merchant_id="merchantId",
    order_id="my-order-1",
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

**cart_id:** `str` — The cartId returned by (or supplied to) /merchant/cart/calculate identifying the calculated cart to convert into an order.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — Your identifier for the resulting order in your own system. Used later with /merchant/order/get, /merchant/order/update, and /merchant/refund/create.
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[bool]` — Whether the order has shipped, creating a tax liability. Defaults to false. Ignored when completedDate is provided.
    
</dd>
</dl>

<dl>
<dd>

**completed_date:** `typing.Optional[datetime.datetime]` — RFC3339 datetime the order was shipped on, which created the tax liability. Takes precedence over the completed field when provided.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[MerchantOrderCreateFromCartRequestKind]` — The kind of order to create: 'order' for a sale (default) or 'credit' for a credit order.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_order_get</a>(...) -> TaxCloudOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a recorded order. The request is forwarded to TaxCloud GET /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. This is a read and is safe to retry. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_order_get(
    merchant_id="merchantId",
    order_id="my-order-1",
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

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — Your identifier for the order to retrieve, as supplied when the order was created.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[MerchantOrderGetRequestExpand]` — Set to 'refunds' to include the order's refunds in the response. Forwarded to TaxCloud as a query parameter.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_order_update</a>(...) -> TaxCloudOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modifies a recorded order; currently the completedDate can be set to mark the order shipped, creating the tax liability. The request is forwarded to TaxCloud PATCH /connections/{connectionId}/orders/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Updates overwrite the fields you send, so do not retry them blindly. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_order_update(
    merchant_id="merchantId",
    order_id="my-order-1",
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

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — Your identifier for the order to update, as supplied when the order was created. Consumed for routing and not forwarded in the update payload.
    
</dd>
</dl>

<dl>
<dd>

**completed_date:** `typing.Optional[datetime.datetime]` — RFC3339 datetime the order was shipped on, which creates the tax liability.
    
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

<details><summary><code>client.merchant_tax_cloud.<a href="src/fern/merchant_tax_cloud/client.py">merchant_refund_create</a>(...) -> TaxCloudRefundResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refunds all or part of a recorded order. The request is forwarded to TaxCloud POST /connections/{connectionId}/orders/refunds/{orderId} using the merchant's stored credentials and TaxCloud's response is returned verbatim. Refund prices and tax amounts are calculated automatically from the order; when the order had discounts, refunds use the discounted prices actually paid. Do not retry refunds blindly - a duplicate submission records a duplicate refund. Available only for TaxCloud-managed merchants: a self-managed merchant has no TaxCloud connection to store or read this state in, so the request is refused with 403 and only /merchant/cart/calculate is supported.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant_tax_cloud.merchant_refund_create(
    merchant_id="merchantId",
    order_id="my-order-1",
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

**merchant_id:** `str` — UUID of the merchant. Must be owned by the calling account. Consumed by the Ziptax layer for routing and not forwarded to TaxCloud.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — Your identifier for the order to refund, as supplied when the order was created. Consumed for routing and not forwarded in the refund payload.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` — Optional batch ID for grouping related refunds.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[RefundItem]]` — The line items and quantities to refund. Omit (or send an empty array) to refund the entire order.
    
</dd>
</dl>

<dl>
<dd>

**returned_date:** `typing.Optional[datetime.datetime]` — Include only if this return amends a previously filed sales tax return; providing it triggers an Amended Sales Tax Return. Not typically recommended.
    
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

## Merchant
<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">create_merchant</a>(...) -> CreateMerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new merchant under the authenticated account. Requires X-API-KEY header.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.create_merchant(
    merchant_name="merchantName",
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

**merchant_name:** `str` — Legal or trading name of the merchant business. Required; must be 1–255 characters.
    
</dd>
</dl>

<dl>
<dd>

**contact_first:** `typing.Optional[str]` — First name of the merchant's primary contact. Optional.
    
</dd>
</dl>

<dl>
<dd>

**contact_last:** `typing.Optional[str]` — Last name of the merchant's primary contact. Optional.
    
</dd>
</dl>

<dl>
<dd>

**contact_email:** `typing.Optional[str]` — Email address of the merchant's primary contact; used for TaxCloud invitations and notifications. Optional.
    
</dd>
</dl>

<dl>
<dd>

**send_taxcloud_invite:** `typing.Optional[bool]` — Sends invite to set up and connect a TaxCloud account to a merchant who does not already use TaxCloud. To connect a TaxCloud account for a merchant who already uses TaxCloud, use the "Set Merchant Credentials" function. Ignored when merchant_type is 'self-managed'.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — The ID you use in your own system to identify this merchant.
    
</dd>
</dl>

<dl>
<dd>

**merchant_type:** `typing.Optional[CreateMerchantRequestMerchantType]` — The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">delete_merchant_credentials</a>(...) -> DeleteMerchantCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes TaxCloud credentials for a merchant. The caller must own the merchant.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.delete_merchant_credentials(
    merchant_id="merchantId",
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

**merchant_id:** `str` — UUID of the merchant whose TaxCloud credentials are being deleted. The merchant must be owned by the calling account.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">get_merchant_credentials</a>(...) -> GetMerchantCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves TaxCloud credentials for a merchant. The caller must own the merchant.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.get_merchant_credentials(
    merchant_id="merchantId",
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

**merchant_id:** `str` — UUID of the merchant whose TaxCloud credentials are being retrieved. The merchant must be owned by the calling account.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">set_merchant_credentials</a>(...) -> SetMerchantCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets or updates TaxCloud credentials for a merchant. Credentials are encrypted at rest with AES-256-GCM. On success an asynchronous webhook notification is sent to the configured endpoint.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.set_merchant_credentials(
    api_key="apiKey",
    connection_id="connectionId",
    merchant_id="merchantId",
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

**api_key:** `str` — TaxCloud API key to associate with the merchant. Stored encrypted at rest with AES-256-GCM.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — TaxCloud connection ID that pairs with the API key to identify the merchant's TaxCloud integration.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `str` — UUID of the merchant whose TaxCloud credentials are being set. The merchant must be owned by the calling account.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">delete_merchant</a>(...) -> DeleteMerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-deletes a merchant by setting deleted_at to now. The caller must own the merchant. If the merchant is not owned by the caller, or is already soft-deleted (deleted_at <= now), the ownership check returns 403. A 404 is only reachable in a rare race after the ownership check passes.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.delete_merchant(
    merchant_id="merchantId",
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

**merchant_id:** `str` — UUID of the merchant to soft-delete. The merchant must be owned by the calling account.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">get_merchant</a>(...) -> GetMerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single merchant by UUID. The caller must own the merchant. Cross-account reads are blocked. Soft-deleted merchants (deleted_at <= now) are treated as non-existent and return 404.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.get_merchant(
    merchant_id="merchantId",
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

**merchant_id:** `str` — UUID of the merchant to retrieve. The merchant must be owned by the calling account.
    
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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">list_merchants</a>() -> typing.Optional[typing.List[Item]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every active merchant owned by the calling account. A merchant is considered active when its deleted_at is NULL or set to a future date. Soft-deleted merchants (deleted_at <= now) are excluded from results.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.list_merchants()

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

<details><summary><code>client.merchant.<a href="src/fern/merchant/client.py">update_merchant</a>(...) -> UpdateMerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing merchant. The caller must own the merchant. Cross-account modification is blocked. Soft-deleted merchants (deleted_at <= now), and merchants owned by another account, fail the ownership check and return 403.
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
from fern import FernApi, UpdateStruct
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.merchant.update_merchant(
    merchant_id="merchantId",
    update=UpdateStruct(
        merchant_name="merchantName",
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

**merchant_id:** `str` — UUID of the merchant to update. The merchant must be owned by the calling account.
    
</dd>
</dl>

<dl>
<dd>

**update:** `UpdateStruct` — New field values for the merchant
    
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

## Tax Rates
<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">get_tax_rates_v60</a>(...) -> V60Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns tax rates in a new structured format with separate base rates,
			service/shipping taxability, and tax summaries. Built on v5.0 data but with enhanced organization. Note: postal-code-only lookups (no address or lat/lng) return the legacy v5.0-style response body (version, rCode, results) rather than the structured object documented here.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tax_rates.get_tax_rates_v60(
    key="your-api-key",
    taxability_code="20010",
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

**key:** `typing.Optional[str]` — API key that authenticates the request and resolves the account's plan, entitlements, and rate limits. Supply it either as this query parameter or the X-API-KEY request header. A missing, malformed, or unknown key returns response code 101.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetTaxRatesV60RequestFormat]` — Serialization format of the response body. 'json' (default) returns a JSON object; 'xml' returns the same data as an XML document.
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[GetTaxRatesV60RequestCountryCode]` — Country of the lookup: 'USA' (default), 'CAN', or a US territory (ASM, GUM, MNP, PRI, VIR). 'CAN' requires the Canadian rates (rate_loc_can) entitlement; otherwise the request returns response code 112. US territories are looked up via the USA path and require no additional entitlement.
    
</dd>
</dl>

<dl>
<dd>

**postalcode:** `typing.Optional[str]` — 5-digit US ZIP code to look up. When supplied on its own the response may contain rates for multiple overlapping jurisdictions. An invalid format returns response code 104.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[str]` — Street address to geocode to a single rooftop-level jurisdiction. Geocoding requires the geo_enabled entitlement; an incomplete or ungeocodable address returns response code 109.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — State name or two-letter abbreviation. Used with city or postal code to disambiguate the location. An invalid format returns response code 102.
    
</dd>
</dl>

<dl>
<dd>

**state_code:** `typing.Optional[str]` — Two-letter state code (e.g. CA). Alternative to 'state' for supplying the state as a code rather than a name.
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` — City name used together with state to narrow the lookup when no street address is supplied. An invalid format returns response code 103.
    
</dd>
</dl>

<dl>
<dd>

**county:** `typing.Optional[str]` — County name used to refine the lookup when supplied without a street address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).
    
</dd>
</dl>

<dl>
<dd>

**lng:** `typing.Optional[float]` — Longitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).
    
</dd>
</dl>

<dl>
<dd>

**adjustment:** `typing.Optional[GetTaxRatesV60RequestAdjustment]` — Sourcing/unincorporated-area handling. Defaults to 'auto', which applies the appropriate sourcing adjustment on geo (address) lookups in unincorporated areas. The values 'origin' and 'destination' are accepted but currently do not change the resolved result.
    
</dd>
</dl>

<dl>
<dd>

**sat_item_total:** `typing.Optional[float]` — Single-article item total in dollars, used for Tennessee Single Article Tax (SAT) calculation on TN address lookups. Note: the v6.0 response does not currently return a SAT breakdown object; the SAT detail (satTaxDetail) is available in the v5.0 response.
    
</dd>
</dl>

<dl>
<dd>

**historical:** `typing.Optional[str]` — Historical period to price the lookup against, formatted YYYYMM (6 digits, e.g. 202401). Returns the rates that were in effect for that month. Requires historical data to be enabled; an invalid format returns response code 111.
    
</dd>
</dl>

<dl>
<dd>

**taxability_code:** `typing.Optional[str]` — Product Taxability Information Code (TIC). When supplied, the response includes a productDetail object describing the rate rules that apply to that product category in the resolved jurisdiction. Accepts numeric standard TIC codes (e.g., 20010) or alphanumeric override codes (e.g., CIR00001). Requires the product_rates entitlement for standard codes.
    
</dd>
</dl>

<dl>
<dd>

**address_detail_extended:** `typing.Optional[bool]` — When true, returns a full geocoding object in the response broken into address parts (street, city, postal code, etc.). Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**shipping_extended:** `typing.Optional[bool]` — When true, returns a detailed shipping object to help navigate collection complexity. The GENERAL_RULE value will be one of: EXEMPT, EXEMPT_WHEN_SEPARATELY_STATED, ITEM_SPECIFIC, CONDITIONAL, or TAXABLE. For EXEMPT_WHEN_SEPARATELY_STATED, the response includes a boolean flag, and a natural-language description is included for clarity. Defaults to false.
    
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

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py">get_tic_search_schema</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the JSON Schema describing the TIC search response body. Public; no authentication required.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.get_tic_search_schema()

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

<details><summary><code>client.search.<a href="src/fern/search/client.py">search_tic</a>(...) -> TicSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches Taxability Information Codes (TIC) by free-text product description and returns ranked matches. Requires authentication via the X-API-KEY header or key query parameter.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.search_tic(
    query="Ceramic & Pottery Kilns",
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

**query:** `str` — Free-text product description to match against TIC codes
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py">recommend_tic</a>(...) -> TicRecommendResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a recommended Taxability Information Code (TIC) for a free-text product description using a machine-learning model. Requires authentication via the X-API-KEY header or key query parameter.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.recommend_tic(
    query="wireless bluetooth headphones",
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

**query:** `str` — Free-text product description to get a recommended TIC for
    
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

## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">get_health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the health status of the API and its components
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_health()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_metadata</a>() -> MetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns system metadata including version and environment information
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_metadata()

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

