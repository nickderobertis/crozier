# Reference
## External Marketplace
<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">fulfillment_simulation_external_marketplace</a>(...) -> FulfillmentSimulationExternalMarketplaceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint can be triggered by marketplaces to simulate the fulfillment of an item in the cart.

The fulfillment information is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.fulfillment_simulation_external_marketplace(
    sc=1,
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

**affiliate_id:** `typing.Optional[str]` — The affiliate ID code created by the seller.
    
</dd>
</dl>

<dl>
<dd>

**sc:** `typing.Optional[int]` — Trade Policy (Sales Channel) identification.
    
</dd>
</dl>

<dl>
<dd>

**client_profile_data:** `typing.Optional[FulfillmentSimulationExternalMarketplaceRequestClientProfileData]` — Customer's profile information.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Three letter ISO code of the country of the shipping address. This value must be sent along with the `postalCode` or `geoCoordinates` values.
    
</dd>
</dl>

<dl>
<dd>

**geo_coordinates:** `typing.Optional[typing.List[float]]` — Array containing two floats with geocoordinates, first longitude, then latitude.
    
</dd>
</dl>

<dl>
<dd>

**is_checked_in:** `typing.Optional[bool]` — Indicates whether order is checked in.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[FulfillmentSimulationExternalMarketplaceRequestItemsItem]]` — Array containing information about the SKUs inside the cart to be simulated.
    
</dd>
</dl>

<dl>
<dd>

**marketing_data:** `typing.Optional[FulfillmentSimulationExternalMarketplaceRequestMarketingData]` — Object containing promotion data such as coupon tracking information and internal or external UTMs.
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — Postal code.
    
</dd>
</dl>

<dl>
<dd>

**selected_sla:** `typing.Optional[str]` — SLA selected by the customer.
    
</dd>
</dl>

<dl>
<dd>

**store_id:** `typing.Optional[str]` — ID of the store.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">send_category_mapping_vtex_mapper</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree. 

To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace. 

This endpoint allows connectors to send the marketplace's category tree mapped in the integration. 

Connectors should send the payload compacted in .gzip format. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
from fern.external_marketplace import SendCategoryMappingToVtexMapperCategoriesItem

client = FernApi(
    api_key="<value>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.send_category_mapping_vtex_mapper(
    id="id",
    categories=[
        SendCategoryMappingToVtexMapperCategoriesItem()
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

**id:** `str` — Code identifying returned in the *VTEX Mapper Registration* endpoint.
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.List[SendCategoryMappingToVtexMapperCategoriesItem]` — Array with Marketplace parent categories and their information.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">vtex_mapper_registration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree. 

To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace. 

This endpoint allows connectors to register the external marketplace integration in VTEX Mapper. 

In case VTEX Mapper detects an error and the call fails, the connector should check if mandatory information was sent correctly. Ex. are URLs correctly registered in the properties categoryTreeEndPoint and mappingEndPoint? 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.vtex_mapper_registration(
    an="accountName",
    category_tree_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/categories",
    display_name="Marketplace A",
    mapping_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/mapping",
    properties={
        "key": "value"
    },
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

**an:** `str` — Name of the VTEX account. Used as part of the URL.
    
</dd>
</dl>

<dl>
<dd>

**category_tree_end_point:** `str` — Endpoint that returns categories and attributes according to VTEX  Mapper specifications.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — Marketplace Name, that will be displayed in VTEX Mapper.
    
</dd>
</dl>

<dl>
<dd>

**mapping_end_point:** `str` — Secure endpoint that will receive the category mapping sent by VTEX Mapper.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Dict[str, typing.Any]` — Refers to the `allowsRemap` property.
    
</dd>
</dl>

<dl>
<dd>

**category_tree_processing_notification_endpoint:** `typing.Optional[str]` — The `CategoryTreeProcessingNotificationEndpoint` is optional, and should be an endpoint from the external marketplace, that will be notified after the marketplace's category tree is successfully processed or not.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">enqueue_new_order</a>(...) -> Deliverybyseller</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to integrate an external channel's order into the VTEX plataform.

This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectorEndpoint** field in [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. If the account is not informed in the URL host, it should also be defined as a query string parameter in the route: `an={account}`. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
from fern import FernApi, ClientProfileData, CustomData, CustomApp, Fields, InvoiceData, UserPaymentInfo, Item, ShippingData, LogisticsInfo, DeliveryIds, SelectedAddress, GeoCoordinates
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.enqueue_new_order(
    account_name="accountName",
    an="apiexamples",
    affiliate_id="MKP",
    allow_franchises=False,
    client_profile_data=ClientProfileData(
        corporate_document=None,
        corporate_name=None,
        corporate_phone=None,
        document="99999999999",
        email="email@email.com.br",
        first_name="John",
        last_name="Doe",
        phone="99999999999",
        state_inscription=None,
        trade_name=None,
    ),
    connector_endpoint="https://connector-endpoint.com/api/vtex",
    connector_name="SkyHub",
    custom_data=CustomData(
        custom_apps=[
            CustomApp(
                fields=Fields(
                    marketplace_payment_method="credit card",
                ),
                id="marketplace-integration",
                major=1,
            )
        ],
    ),
    invoice_data=InvoiceData(
        user_payment_info=UserPaymentInfo(
            payment_methods=[
                "creditCardPaymentGroup"
            ],
        ),
    ),
    items=[
        Item(
            id="1",
            price=975,
            quantity=1,
        )
    ],
    marketplace_order_id="{{$guid}}",
    marketplace_order_status="NEW",
    marketplace_payment_value=3025,
    pickup_account_name="",
    shipping_data=ShippingData(
        is_fob=True,
        is_marketplace_fulfillment=True,
        logistics_info=[
            LogisticsInfo(
                delivery_ids=DeliveryIds(
                    warehouse_id="AR1",
                ),
                lock_ttl="1d",
                price=2050,
                selected_delivery_channel="delivery",
                selected_sla="Express",
                shipping_estimate="2d",
            )
        ],
        selected_addresses=[
            SelectedAddress(
                address_id="1",
                address_type="Residential",
                city="Curitiba",
                complement="101",
                country="BRA",
                geo_coordinates=GeoCoordinates(
                    latitude="-29.5",
                    longitude="-45.8",
                ),
                neighborhood="Portão",
                number="4125",
                postal_code="81020-235",
                receiver_name="John Doe",
                state="PR",
                street="Rua Eduardo Carlos Pereira",
            )
        ],
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

**account_name:** `str` — Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.
    
</dd>
</dl>

<dl>
<dd>

**affiliate_id:** `str` — ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**allow_franchises:** `bool` — Boolean indicating whether franchise accounts linked to the main seller should be considered. That is, if the order delivery pickup/SLA can belong to a [franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl), for example. This field is optional and defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**client_profile_data:** `ClientProfileData` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_data:** `InvoiceData` 
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[Item]` 
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — String that indicates the order's ID in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_status:** `str` 

Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance it’s status in VTEX after integrating it. This field accepts the following values:  

- `new`  

- `approved`
    
</dd>
</dl>

<dl>
<dd>

**marketplace_payment_value:** `int` — Integer that indicates the order’s total value, which the marketplace will pay to the seller. It’s important to note that this value should include interest, if that’s the case. If the value is `USD110.50`, convert it to the format → `11050`.
    
</dd>
</dl>

<dl>
<dd>

**shipping_data:** `ShippingData` 
    
</dd>
</dl>

<dl>
<dd>

**an:** `typing.Optional[str]` — Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.
    
</dd>
</dl>

<dl>
<dd>

**connector_endpoint:** `typing.Optional[str]` 

String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field accepts query strings. You can use the models below:  

- `https://{{externalconnector}}.com`  

- `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint. 

This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.  

It is required if the connector is native or does not use the App Template.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `typing.Optional[str]` 

String with the identifier code of the connector responsible for the order.  

This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.  

It is required if the connector is native or does not use the App Template.
    
</dd>
</dl>

<dl>
<dd>

**custom_data:** `typing.Optional[CustomData]` 
    
</dd>
</dl>

<dl>
<dd>

**pickup_account_name:** `typing.Optional[str]` — String that indicates the name of the account responsible for the order’s pickup point. It is only required for pickup-in-point orders from franchise accounts, when franchise accounts `allowFranchises` is `true` and the order in question has a `pickup-in-point` delivery type. It is optional otherwise.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">update_order_status</a>(...) -> Approveorder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API request used to update an order status in VTEX.

This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectiorEndpoint** field or the **connectiorEndpoint** [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.update_order_status(
    account_name="accountName",
    an="apiexamples",
    connector_endpoint="https://connector-endpoint.com/api/vtex",
    connector_name="Skyhub",
    marketplace_order_id="{{$guid}}",
    marketplace_order_status="APPROVED",
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

**account_name:** `str` — Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.
    
</dd>
</dl>

<dl>
<dd>

**connector_endpoint:** `str` 

String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field does not accept query strings. You can use the models below:  

- `https://{{externalconnector}}.com`  

- `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint. 

This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.  

It is required if the connector is native or does not use the App Template.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` 

String with the identifier code of the connector responsible for the order.  

This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.  

It is required if the connector is native or does not use the App Template.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — String that indicates the order's ID in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_status:** `str` 

Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance its status in VTEX after integrating it. This field accepts the following values:  

- `new`  

- `approved`.
    
</dd>
</dl>

<dl>
<dd>

**an:** `typing.Optional[str]` — Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">place_fulfillment_order</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.

> If you plan to integrate external orders with possible [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#) be mindful of the `isCreatedAsync` request body field. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
from fern.external_marketplace import PlaceFulfillmentOrderRequestClientProfileData, PlaceFulfillmentOrderRequestItemsItem, PlaceFulfillmentOrderRequestShippingData

client = FernApi(
    api_key="<value>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.place_fulfillment_order(
    account_name="accountName",
    environment="environment",
    sc="1",
    affiliate_id="MKP",
    client_profile_data=PlaceFulfillmentOrderRequestClientProfileData(
        document="123456789",
        document_type="cpf",
        email="customer@examplemail.com",
        first_name="first-name",
        last_name="last-name",
    ),
    items=[
        PlaceFulfillmentOrderRequestItemsItem(
            id="123456789",
            quantity=1,
            seller="1",
        )
    ],
    marketplace_order_id="123456789",
    marketplace_payment_value=100,
    marketplace_services_endpoint="https://exampleseller.marketplaceservices.com",
    shipping_data=PlaceFulfillmentOrderRequestShippingData(),
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

**account_name:** `str` — Name of the VTEX account. Used as part of the URL.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` — Environment to be used. It is passed as part of the URL.
    
</dd>
</dl>

<dl>
<dd>

**affiliate_id:** `str` — ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**client_profile_data:** `PlaceFulfillmentOrderRequestClientProfileData` — Customer's profile information.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[PlaceFulfillmentOrderRequestItemsItem]` — Array of objects containing information on each of the order's items.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — ID of the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_payment_value:** `int` — Value of the payment made to the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_services_endpoint:** `str` — Endpoint provided by the marketplace for post purchase communication. Should be an URL, containing protocol, host, path and query string (in case it applies).
    
</dd>
</dl>

<dl>
<dd>

**shipping_data:** `PlaceFulfillmentOrderRequestShippingData` — Shipping information.
    
</dd>
</dl>

<dl>
<dd>

**sc:** `typing.Optional[str]` — Sales channel.
    
</dd>
</dl>

<dl>
<dd>

**is_created_async:** `typing.Optional[bool]` — Indicates whether an order is created. It must be `true` if an order is being placed with [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#), otherwise the request will not work.
    
</dd>
</dl>

<dl>
<dd>

**marketing_data:** `typing.Optional[PlaceFulfillmentOrderRequestMarketingData]` 
    
</dd>
</dl>

<dl>
<dd>

**open_text_field:** `typing.Optional[str]` — Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)
    
</dd>
</dl>

<dl>
<dd>

**payment_data:** `typing.Optional[typing.Dict[str, typing.Any]]` — In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.
    
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

<details><summary><code>client.external_marketplace.<a href="src/fern/external_marketplace/client.py">authorize_dispatch_for_fulfillment_order</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_marketplace.authorize_dispatch_for_fulfillment_order(
    account_name="accountName",
    environment="environment",
    order_id="orderId",
    sc="1",
    affiliate_id="MKP",
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

**account_name:** `str` — Name of the VTEX account. Used as part of the URL.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` — Environment to be used. It is passed as part of the URL.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — ID of the order that is to be authorized. It is composed of the `afilliateId` and the `marketplaceOrderId` joined with a `-`. For instance, an order with an ID `"123"` coming from the marketplace `"MKP"` has an `orderId` of `"MKP-123"`.
    
</dd>
</dl>

<dl>
<dd>

**affiliate_id:** `str` — ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**sc:** `typing.Optional[str]` — Sales channel.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `typing.Optional[str]` — ID of the order in the marketplace. It is the same as the `orderId` without the `afilliateId` at the beginning. For instance, if the `orderId` is `"MKP-123"`, the `marketplaceOrderId` is `"123"`.
    
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

## External Seller
<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">fulfillment_simulation</a>(...) -> FulfillmentSimulationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint may be called upon by VTEX for fulfillment simulation in the external seller different contexts. See examples below.

When a [price](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) or [inventory](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory) notification request returns a response with status `200 OK`, it means that the SKU already exists in the marketplace. Whenever this happens, the marketplace will call the seller to get two updated information about the SKU: Price and Inventory.

The seller needs to have an endpoint implemented in order to receive this call and send a response containing the requested information to the marketplace. We call it the Fulfillment Simulation endpoint.

If the seller wishes to include other parameters in this call (like account name, or [sales channel](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) ID), this should be done within their {fulfillmentEndpoint}. This path is then inserted in the marketplace's VTEX admin when [configuring a seller](https://help.vtex.com/en/tutorial/configurando-seller--tutorials_392). 

The marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference. 

This call is also applied in the Storefront simulation scenario, in which case the request from VTEX does not send the paramenters `country` and `postalCode`. 
The call's payload can be adapted into two scenarios: 

- **Displaying items in the storefront**: the address information can be nulled in the request, since they are not mandatory data for this context.   
- **Making a shopping cart simulation during checkout**: address information must be sent, since this data is needed to calculate freight values. If the address information (including `postalCode` and `country`) is not sent through the call, VTEX interprets the stock balance as zero. Without a valid stock balance, the seller will not be shown as an option during checkout. 
  
## Request body example - Indexing simulation

```
{
    "items": [
      {
        "id": "7908010136043",
        "quantity": 1,
        "seller": "1",
      }
    ],
    "isCheckedIn": false,
  }
``` 
## Request body example - Checkout simulation

```
{
    "items": [
      {
        "id": "7908010136043",
        "quantity": 1,
        "seller": "1",
      }
    ],
    "postalCode": "22270-030",
    "country": "BRA",
  }
```
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.fulfillment_simulation(
    fulfillment_endpoint="marketplaceexample.externalseller.com",
    postal_code="12345678",
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

**fulfillment_endpoint:** `str` — This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `str` — Delivery address postal code. This field is mandatory for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — ISO 3-digit code of the country where the delivery address is located.  This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.
    
</dd>
</dl>

<dl>
<dd>

**geo_coordinates:** `typing.Optional[typing.List[str]]` — Geographic coordinates of the delivery address. This may be used instead of the postalCode, in case the marketplace is configured to accept geolocation. Example of value: `[-22.9443504,-43.1825635]`.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[FulfillmentItem]]` — Array containing the cart items.
    
</dd>
</dl>

<dl>
<dd>

**sc:** `typing.Optional[str]` — Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) associated to the seller account created.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">order_placement</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent by VTEX to the external seller once the customer finishes their checkout, to let the seller know there is a newly placed order. It does that by calling the **Order Placement** endpoint, which needs to be implemented by the seller.

The marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With all that, the seller will be able to create the order in their own store.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.order_placement(
    fulfillment_endpoint="https://marketplaceexample.externalseller.com",
    authorization="VTEX key=\"appKey\" token=\"appToken\"",
    vtex_api_appkey="appKey",
    vtex_api_apptoken="appToken",
    accept="application/json",
    accept_enconding="gzip, deflate",
    vtex_operation_id="8032114b-63e9-4e64-b30c-f7afcf676d7a",
    forwarded_proto="https",
    vtex_cache_client_bypass="1",
    traceparent="00-083c0ca18bc8d94183f333809a70cd64-bf5e9a641e230540-00",
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

**fulfillment_endpoint:** `str` — This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `str` — Indicates authorization.
    
</dd>
</dl>

<dl>
<dd>

**vtex_api_appkey:** `str` — VTEX API app key.
    
</dd>
</dl>

<dl>
<dd>

**vtex_api_apptoken:** `str` — VTEX API app token.
    
</dd>
</dl>

<dl>
<dd>

**accept:** `str` — HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    
</dd>
</dl>

<dl>
<dd>

**accept_enconding:** `str` — Indicates the types of response enconding the client can understand.
    
</dd>
</dl>

<dl>
<dd>

**vtex_operation_id:** `str` — VTEX operation ID.
    
</dd>
</dl>

<dl>
<dd>

**forwarded_proto:** `str` — Determines the protocol used by the client in the request.
    
</dd>
</dl>

<dl>
<dd>

**vtex_cache_client_bypass:** `str` — VTEX cache client bypass.
    
</dd>
</dl>

<dl>
<dd>

**traceparent:** `str` — Identifies the incoming request in a tracing system.
    
</dd>
</dl>

<dl>
<dd>

**client_profile_data:** `typing.Optional[OrderPlacementClientProfileData]` — Customer's profile information.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[OrderPlacementItemsItem]]` — Array of objects containing data about each SKU in the cart.
    
</dd>
</dl>

<dl>
<dd>

**marketing_data:** `typing.Optional[OrderPlacementMarketingData]` — Marketing tracking data. If the order has no tracking data, the value will be `null`.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `typing.Optional[str]` — Identifies the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_payment_value:** `typing.Optional[int]` — Amount that the marketplace agrees to pay to the seller. The last two digits are the cents. For example, $24.99 is represented 2499.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_services_endpoint:** `typing.Optional[str]` — Endpoint sent by VTEX to the seller, that will be used to send the invoice and tracking data to the marketplace. This endpoint will also be used in [change order in Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/change-orders-multilevel-omnichannel-inventory-external-marketplaces#implementators) operations in external marketplaces.
    
</dd>
</dl>

<dl>
<dd>

**open_text_field:** `typing.Optional[str]` — Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `json` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)
    
</dd>
</dl>

<dl>
<dd>

**payment_data:** `typing.Optional[typing.Dict[str, typing.Any]]` — In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.
    
</dd>
</dl>

<dl>
<dd>

**shipping_data:** `typing.Optional[OrderPlacementShippingData]` — Shipping information.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">mkp_order_cancellation</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed. 

For the seller to: 

- **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not. 

- **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`). 

- **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/vtex-rest-api/reference/external-seller#send-invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#order-invoicing) step, and the ones that follow it. 

This call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.mkp_order_cancellation(
    fulfillment_endpoint="marketplaceexample.externalseller.com",
    order_id="orderId",
    marketplace_order_id="1138342255777-01",
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

**fulfillment_endpoint:** `str` — This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — ID of the order being fulfilled
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order. The seller should use this ID to trigger the cancellation of the corresponding order.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">authorize_fulfillment</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent from VTEX to the seller after the payment is approved, to notify them that the fulfillment process can start.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.authorize_fulfillment(
    fulfillment_endpoint="https://marketplaceexample.externalseller.com",
    seller_order_id="00-1268540501456-01",
    marketplace_order_id="1138342255777-01",
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

**fulfillment_endpoint:** `str` — This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.
    
</dd>
</dl>

<dl>
<dd>

**seller_order_id:** `str` — Seller's order ID of the order ready for fulfillment. The seller can be a VTEX seller or an external one.
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order. The seller should use this ID to trigger the fulfillment process of the corresponding order.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">cancel_order_in_marketplace</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent by the external seller to the VTEX marketplace to cancel an order.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.cancel_order_in_marketplace(
    marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
    marketplace_order_id="1138342255777-01",
    reason="Product is unavailable",
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

**marketplace_services_endpoint:** `str` — This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Insert here the reason for the order's cancellation.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">send_invoice</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent by the external seller to the VTEX marketplace to send invoice information.

This can be necessary in a regular order or in the case of a return. The `type` field is used to indicate which of these is the case.
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
from fern.external_seller import SendInvoiceRequestItemsItem

client = FernApi(
    api_key="<value>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.send_invoice(
    marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
    marketplace_order_id="1138342255777-01",
    invoice_number="NFe-00002",
    items=[
        SendInvoiceRequestItemsItem(
            id="6",
            price=5500,
            quantity=1,
        )
    ],
    type="Output",
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

**marketplace_services_endpoint:** `str` — This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**invoice_number:** `str` — Invoice number
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[SendInvoiceRequestItemsItem]` — Array containing the order items.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Indicates the type of the invoice. Use `"Output"` for regular orders and `"Input"` for returns.
    
</dd>
</dl>

<dl>
<dd>

**courier:** `typing.Optional[str]` — Courier, if available on invoice.
    
</dd>
</dl>

<dl>
<dd>

**invoice_value:** `typing.Optional[int]` — Invoice value.
    
</dd>
</dl>

<dl>
<dd>

**issuance_date:** `typing.Optional[str]` — Issuance date.
    
</dd>
</dl>

<dl>
<dd>

**tracking_number:** `typing.Optional[str]` — Tracking number.
    
</dd>
</dl>

<dl>
<dd>

**tracking_url:** `typing.Optional[str]` — Tracking URL.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">send_tracking_information</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent by the external seller to the VTEX marketplace to add tracking information to a given order's invoice, in case it is necessary to do so after the invoice has been sent.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.send_tracking_information(
    marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
    marketplace_order_id="1138342255777-01",
    invoice_number="NFe-00002",
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

**marketplace_services_endpoint:** `str` — This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**invoice_number:** `str` — Invoice number.
    
</dd>
</dl>

<dl>
<dd>

**courier:** `typing.Optional[str]` — Courier.
    
</dd>
</dl>

<dl>
<dd>

**dispatched_date:** `typing.Optional[str]` — Date of order dispatch.
    
</dd>
</dl>

<dl>
<dd>

**tracking_number:** `typing.Optional[str]` — Tracking number.
    
</dd>
</dl>

<dl>
<dd>

**tracking_url:** `typing.Optional[str]` — Tracking URL.
    
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

<details><summary><code>client.external_seller.<a href="src/fern/external_seller/client.py">update_tracking_status</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This request is sent by the external seller to the VTEX marketplace to update a given order's tracking status.
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
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_seller.update_tracking_status(
    marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
    marketplace_order_id="1138342255777-01",
    invoice_number="NFe-00002",
    is_delivered=True,
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

**marketplace_services_endpoint:** `str` — This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).
    
</dd>
</dl>

<dl>
<dd>

**marketplace_order_id:** `str` — Identifies the order in the marketplace.
    
</dd>
</dl>

<dl>
<dd>

**invoice_number:** `str` — Invoice number.
    
</dd>
</dl>

<dl>
<dd>

**is_delivered:** `bool` — Indicates if order has been delivered. `false` if it is in transit.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[UpdateTrackingStatusRequestEventsItem]]` — Array containing information on each tracking event received.
    
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

