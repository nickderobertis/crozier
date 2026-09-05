# Reference
## Pricing Configuration
<details><summary><code>client.pricing_configuration.<a href="src/fern/pricing_configuration/client.py">get_pricing_config</a>() -> PricingConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves Pricing Configuration.
## Response body example

```json
{
    "hasMigrated": true,
    "migrationStatus": "Completed",
    "defaultMarkup": 100,
    "priceVariation": {
        "upperLimit": null,
        "lowerLimit": null
    },
    "minimumMarkups": {
        "1": 100,
        "2": 90
    },
    "tradePolicyConfigs": [],
    "sellersToOverride": [],
    "hasPriceInheritance": false,
    "priceInheritance": "never",
    "hasOptionalBasePrice": false,
    "blockAccount": false,
    "blockedRoutes": null,
    "priceTableSelectionStrategy": "first",
    "priceTableLimit": null
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricing_configuration.get_pricing_config()

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

<details><summary><code>client.pricing_configuration.<a href="src/fern/pricing_configuration/client.py">get_pricingv2status</a>() -> GetPricingv2StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves Pricing v2 Status. 
## Response body example

```json
{
    "isActive": true,
    "hasMigrated": true
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricing_configuration.get_pricingv2status()

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

## Price Tables
<details><summary><code>client.price_tables.<a href="src/fern/price_tables/client.py">getallpricetablesandrules</a>() -> typing.List[GetallpricetablesandrulesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method will retrieve all price tables and their rules.

## Response body example

```json
[
    {
        "tradePolicyId": "2",
        "rules": [
            {
                "id": 0,
                "context": {
                    "categories": {},
                    "brands": {},
                    "stockStatuses": null,
                    "internalCategories": null,
                    "markupRange": null,
                    "dateRange": null
                },
                "percentualModifier": 20
            }
        ]
    },
    {
        "tradePolicyId": "b2c",
        "rules": [
            {
                "id": 0,
                "context": {
                    "categories": {},
                    "brands": {
                        "2000009": "Whiskas"
                    },
                    "stockStatuses": null,
                    "internalCategories": null,
                    "markupRange": null,
                    "dateRange": null
                },
                "percentualModifier": 15
            }
        ]
    }
]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.price_tables.getallpricetablesandrules()

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

<details><summary><code>client.price_tables.<a href="src/fern/price_tables/client.py">getrulesforapricetable</a>(...) -> GetrulesforapricetableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method will retrieve the rules from a specific Price Table.

## Response body example

```json
{
    "tradePolicyId": "b2c",
    "rules": [{
        "id": 0,
        "context": {
            "categories": {},
            "brands": {
                "2000009": "Whiskas"
            },
            "stockStatuses": null,
            "internalCategories": null,
            "markupRange": null,
            "dateRange": null
        },
        "percentualModifier": 15
    }]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.price_tables.getrulesforapricetable(
    price_table_id="b2c",
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

**price_table_id:** `str` — Price Table Name.
    
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

<details><summary><code>client.price_tables.<a href="src/fern/price_tables/client.py">update_rules_for_a_price_table</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.

## Request body example

```json
{
    "rules": [
          {
               "id": 1,
               "context": {
                    "categories": {
                         "Category ID": "1",
                         "Category Name": "Alimentação"
                    },
                    "brands": {
                         "Brand ID": "2000002",
                         "Brand Name": "Whiskas"
                    },
                    "markupRange": {
                         "from": 0,
                         "to": 200
                    },
                    "dateRange": {
                         "from": "2022-01-23T19:00:00.000Z",
                         "to": "2023-10-26T00:00:00.000Z"
                    }
               },
               "percentualModifier": 0
          }
    ]
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
from fern.price_tables import PutPricingPipelineCatalogPriceTableIdRequestRulesItem, PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext, PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange, PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange

client = FernApi(
    api_key="<value>",
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.price_tables.update_rules_for_a_price_table(
    price_table_id="priceTableId",
    rules=[
        PutPricingPipelineCatalogPriceTableIdRequestRulesItem(
            context=PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext(
                brands={
                    "Brand ID": "2000002",
                    "Brand Name": "Whiskas"
                },
                categories={
                    "Category ID": "1",
                    "Category Name": "Alimentação"
                },
                date_range=PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange(
                    from_="from",
                    to="to",
                ),
                markup_range=PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange(
                    from_=0,
                    to=200,
                ),
            ),
            id=1,
            percentual_modifier=0,
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

**price_table_id:** `str` — Price Table Name.
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.List[PutPricingPipelineCatalogPriceTableIdRequestRulesItem]` — Array of rules for the price table.
    
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

<details><summary><code>client.price_tables.<a href="src/fern/price_tables/client.py">listpricetables</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method will list all price tables.

## Response body example

```json
[
    "1",
    "2",
    "3",
    "b2c",
    "b2b",
    "gold"
]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.price_tables.listpricetables()

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

## Prices and Fixed Prices
<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">get_price</a>(...) -> Getprice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves price data given a specific SKU ID. Within the `fixedPrices` object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.

 ## Response body example

```json
{
    "itemId": "1",
    "listPrice": 50,
    "costPrice": 90,
    "markup": 30,
    "basePrice": 117,
    "fixedPrices": [
        {
            "tradePolicyId": "1",
            "value": 50.5,
            "listPrice": 50.5,
            "minQuantity": 2,
            "dateRange": {
                "from": "2021-12-31T01:00:00Z",
                "to": "2022-12-31T01:00:00Z"
            }
        },
        {
            "tradePolicyId": "2",
            "value": 30,
            "listPrice": 50,
            "minQuantity": 2
        }
    ]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.get_price(
    item_id=1,
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

**item_id:** `int` — SKU ID.
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">create_update_price_or_fixed_price</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.

 <p> You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula <code>costPrice * (1 + markup) = basePrice</code>.</p> <h2>Request body example</h2>

```json
{
    "markup": 30,
    "basePrice": 100,
    "listPrice": 35,
    "fixedPrices": [
        {
            "tradePolicyId": "1",
            "value": 31,
            "listPrice": 32,
            "minQuantity": 1,
            "dateRange": {
                "from": "2022-05-21T22:00:00Z",
                "to": "2023-05-28T22:00:00Z"
            }
        },
        {
            "tradePolicyId": "1",
            "value": 31.5,
            "listPrice": 33,
            "minQuantity": 2
        }
    ]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.create_update_price_or_fixed_price(
    item_id=1,
    base_price=1.1,
    list_price=1.1,
    markup=1,
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

**item_id:** `int` — SKU unique identifier number.
    
</dd>
</dl>

<dl>
<dd>

**base_price:** `float` — SKU selling base price. If you decide to fill only the `basePrice` item, the `markup` and `costPrice` will be automatically generated to adapt to the number inserted in `basePrice`.
    
</dd>
</dl>

<dl>
<dd>

**list_price:** `float` — SKU's suggested selling price.
    
</dd>
</dl>

<dl>
<dd>

**markup:** `int` — The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the `markup` item, you must also fill the `costPrice`. The `basePrice` will be automatically generated based on both values.
    
</dd>
</dl>

<dl>
<dd>

**cost_price:** `typing.Optional[float]` — SKU selling cost price. If you decide to fill the `costPrice` item, you must also fill the `markup` and `basePrice` will be automatically generated based on both values.
    
</dd>
</dl>

<dl>
<dd>

**fixed_prices:** `typing.Optional[typing.List[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]]` 
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">delete_price</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.delete_price(
    item_id=1,
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

**item_id:** `int` — SKU ID.
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">get_computed_pricebypricetable</a>(...) -> Getcomputedprice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the Computed Price, which is the price after all the steps in the Pricing pipeline, for an SKU in a specific price table or trade policy. 

## Response body example

```json
{
    "tradePolicyId": "1",
    "listPrice": 30,
    "costPrice": 76.92,
    "sellingPrice": 18.9,
    "priceValidUntil": "2018-12-20T18:12:14Z"
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.get_computed_pricebypricetable(
    item_id=1,
    price_table_id="gold",
    category_ids=1,
    brand_id=3,
    quantity=2,
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

**item_id:** `int` — SKU ID.
    
</dd>
</dl>

<dl>
<dd>

**price_table_id:** `str` — SKU Price Table Name.
    
</dd>
</dl>

<dl>
<dd>

**category_ids:** `int` — Category ID.
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `int` — Brand ID.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `int` — SKU quantity.
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">get_fixed_prices</a>(...) -> typing.List[FixedPrice]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated. This method retrieves an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.

 The default value for a Minimum Quantity is `1`. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of Minimum Quantity or above, unless a higher Minimum Quantity is specified.

 Fixed prices may, optionally, be scheduled. If so, these objects will contain the `dateRange` object with `from` and `to` properties, indicating the start and end time of the scheduled fixed price in the RFC3339 timestamp format (`YYYY-MM-DDT23:59:60Z`).

 Note that the 'Z', at the end, represents the UTC time (GMT+00:00). If it was in GMT-03:00, for example, it would be (`YYYY-MM-DDT23:59:60-03:00`).

 ## Response body example

```json
[
    {
        "tradePolicyId": "6",
        "value": 20.9,
        "listPrice": 22.9,
        "minQuantity": 1,
        "dateRange": {
            "from": "2021-12-30T22:00:00-03:00",
            "to": "2021-12-30T22:00:00-03:00"
        }
    },
    {
        "tradePolicyId": "1",
        "value": 18.9,
        "listPrice": null,
        "minQuantity": 1,
        "dateRange": {
            "from": "2021-12-30T22:00:00-03:00",
            "to": "2021-12-30T22:00:00-03:00"
        }
    }
]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.get_fixed_prices(
    item_id=1,
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

**item_id:** `int` — SKU ID.
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">get_fixed_pricesonapricetable</a>(...) -> typing.List[FixedPrice]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all Fixed Prices on a price table or trade policy. 

## Response body example

```json
[
    {
        "tradePolicyId": "6",
        "value": 20.9,
        "listPrice": 22.9,
        "minQuantity": 1,
        "dateRange": {
            "from": "2021-12-30T22:00:00-03:00",
            "to": "2021-12-30T22:00:00-04:00"
        }
    },
    {
        "tradePolicyId": "1",
        "value": 18.9,
        "listPrice": null,
        "minQuantity": 1
    }
]
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.get_fixed_pricesonapricetable(
    item_id=1,
    price_table_id="gold",
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

**item_id:** `int` — SKU ID.
    
</dd>
</dl>

<dl>
<dd>

**price_table_id:** `str` — Price Table Name
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">createorupdatefixedpricesonpricetableortradepolicy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates the fixed prices of an SKU for a specific price table or trade policy. You can add one or multiple fixed prices per SKU.

 ## Request body example

```json
[
  {
    "value": 50.5,
    "listPrice": 50.5,
    "minQuantity": 2,
    "dateRange": {
      "from": "2021-12-30T22:00:00-03:00",
      "to": "2021-12-30T22:00:00-04:00"
    }
  }
]
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
from fern.prices_and_fixed_prices import CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem

client = FernApi(
    api_key="<value>",
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.createorupdatefixedpricesonpricetableortradepolicy(
    item_id=1,
    price_table_id="priceTableA",
    request=[
        CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem(
            min_quantity=2,
            value=50.5,
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

**item_id:** `int` — SKU ID.
    
</dd>
</dl>

<dl>
<dd>

**price_table_id:** `str` — SKU **price table** name or **trade policy** ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem]` 
    
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

<details><summary><code>client.prices_and_fixed_prices.<a href="src/fern/prices_and_fixed_prices/client.py">deletefixedpricesonapricetableortradepolicy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.
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
    accept="<Accept>",
    vtex_api_app_token="<X-VTEX-API-AppToken>",
    environment=FernApiEnvironment.DEFAULT,
)

client.prices_and_fixed_prices.deletefixedpricesonapricetableortradepolicy(
    item_id=1,
    price_table_id="gold",
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

**item_id:** `int` — SKU ID.
    
</dd>
</dl>

<dl>
<dd>

**price_table_id:** `str` — Price Table or Trade Policy Name.
    
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

