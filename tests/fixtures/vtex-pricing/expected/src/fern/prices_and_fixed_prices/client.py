

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fixed_price import FixedPrice
from ..types.getcomputedprice import Getcomputedprice
from ..types.getprice import Getprice
from .raw_client import AsyncRawPricesAndFixedPricesClient, RawPricesAndFixedPricesClient
from .types.create_update_price_or_fixed_price_request_fixed_prices_item import (
    CreateUpdatePriceOrFixedPriceRequestFixedPricesItem,
)
from .types.createorupdatefixedpricesonpricetableortradepolicy_request_body_item import (
    CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem,
)


OMIT = typing.cast(typing.Any, ...)


class PricesAndFixedPricesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPricesAndFixedPricesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPricesAndFixedPricesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPricesAndFixedPricesClient
        """
        return self._raw_client

    def get_price(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Getprice:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Getprice
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.get_price(
            item_id=1,
        )
        """
        _response = self._raw_client.get_price(item_id, request_options=request_options)
        return _response.data

    def create_update_price_or_fixed_price(
        self,
        item_id: int,
        *,
        base_price: float,
        list_price: float,
        markup: int,
        cost_price: typing.Optional[float] = OMIT,
        fixed_prices: typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        item_id : int
            SKU unique identifier number.

        base_price : float
            SKU selling base price. If you decide to fill only the `basePrice` item, the `markup` and `costPrice` will be automatically generated to adapt to the number inserted in `basePrice`.

        list_price : float
            SKU's suggested selling price.

        markup : int
            The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the `markup` item, you must also fill the `costPrice`. The `basePrice` will be automatically generated based on both values.

        cost_price : typing.Optional[float]
            SKU selling cost price. If you decide to fill the `costPrice` item, you must also fill the `markup` and `basePrice` will be automatically generated based on both values.

        fixed_prices : typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.create_update_price_or_fixed_price(
            item_id=1,
            base_price=1.1,
            list_price=1.1,
            markup=1,
        )
        """
        _response = self._raw_client.create_update_price_or_fixed_price(
            item_id,
            base_price=base_price,
            list_price=list_price,
            markup=markup,
            cost_price=cost_price,
            fixed_prices=fixed_prices,
            request_options=request_options,
        )
        return _response.data

    def delete_price(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.delete_price(
            item_id=1,
        )
        """
        _response = self._raw_client.delete_price(item_id, request_options=request_options)
        return _response.data

    def get_computed_pricebypricetable(
        self,
        item_id: int,
        price_table_id: str,
        *,
        category_ids: int,
        brand_id: int,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Getcomputedprice:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU Price Table Name.

        category_ids : int
            Category ID.

        brand_id : int
            Brand ID.

        quantity : int
            SKU quantity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Getcomputedprice
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.get_computed_pricebypricetable(
            item_id=1,
            price_table_id="gold",
            category_ids=1,
            brand_id=3,
            quantity=2,
        )
        """
        _response = self._raw_client.get_computed_pricebypricetable(
            item_id,
            price_table_id,
            category_ids=category_ids,
            brand_id=brand_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    def get_fixed_prices(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FixedPrice]:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FixedPrice]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.get_fixed_prices(
            item_id=1,
        )
        """
        _response = self._raw_client.get_fixed_prices(item_id, request_options=request_options)
        return _response.data

    def get_fixed_pricesonapricetable(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FixedPrice]:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FixedPrice]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.get_fixed_pricesonapricetable(
            item_id=1,
            price_table_id="gold",
        )
        """
        _response = self._raw_client.get_fixed_pricesonapricetable(
            item_id, price_table_id, request_options=request_options
        )
        return _response.data

    def createorupdatefixedpricesonpricetableortradepolicy(
        self,
        item_id: int,
        price_table_id: str,
        *,
        request: typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU **price table** name or **trade policy** ID.

        request : typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.prices_and_fixed_prices import (
            CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem,
        )

        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
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
        """
        _response = self._raw_client.createorupdatefixedpricesonpricetableortradepolicy(
            item_id, price_table_id, request=request, request_options=request_options
        )
        return _response.data

    def deletefixedpricesonapricetableortradepolicy(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table or Trade Policy Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.prices_and_fixed_prices.deletefixedpricesonapricetableortradepolicy(
            item_id=1,
            price_table_id="gold",
        )
        """
        _response = self._raw_client.deletefixedpricesonapricetableortradepolicy(
            item_id, price_table_id, request_options=request_options
        )
        return _response.data


class AsyncPricesAndFixedPricesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPricesAndFixedPricesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPricesAndFixedPricesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPricesAndFixedPricesClient
        """
        return self._raw_client

    async def get_price(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Getprice:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Getprice
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.get_price(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_price(item_id, request_options=request_options)
        return _response.data

    async def create_update_price_or_fixed_price(
        self,
        item_id: int,
        *,
        base_price: float,
        list_price: float,
        markup: int,
        cost_price: typing.Optional[float] = OMIT,
        fixed_prices: typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        item_id : int
            SKU unique identifier number.

        base_price : float
            SKU selling base price. If you decide to fill only the `basePrice` item, the `markup` and `costPrice` will be automatically generated to adapt to the number inserted in `basePrice`.

        list_price : float
            SKU's suggested selling price.

        markup : int
            The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the `markup` item, you must also fill the `costPrice`. The `basePrice` will be automatically generated based on both values.

        cost_price : typing.Optional[float]
            SKU selling cost price. If you decide to fill the `costPrice` item, you must also fill the `markup` and `basePrice` will be automatically generated based on both values.

        fixed_prices : typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.create_update_price_or_fixed_price(
                item_id=1,
                base_price=1.1,
                list_price=1.1,
                markup=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_update_price_or_fixed_price(
            item_id,
            base_price=base_price,
            list_price=list_price,
            markup=markup,
            cost_price=cost_price,
            fixed_prices=fixed_prices,
            request_options=request_options,
        )
        return _response.data

    async def delete_price(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.delete_price(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_price(item_id, request_options=request_options)
        return _response.data

    async def get_computed_pricebypricetable(
        self,
        item_id: int,
        price_table_id: str,
        *,
        category_ids: int,
        brand_id: int,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Getcomputedprice:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU Price Table Name.

        category_ids : int
            Category ID.

        brand_id : int
            Brand ID.

        quantity : int
            SKU quantity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Getcomputedprice
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.get_computed_pricebypricetable(
                item_id=1,
                price_table_id="gold",
                category_ids=1,
                brand_id=3,
                quantity=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_computed_pricebypricetable(
            item_id,
            price_table_id,
            category_ids=category_ids,
            brand_id=brand_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    async def get_fixed_prices(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FixedPrice]:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FixedPrice]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.get_fixed_prices(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fixed_prices(item_id, request_options=request_options)
        return _response.data

    async def get_fixed_pricesonapricetable(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FixedPrice]:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FixedPrice]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.get_fixed_pricesonapricetable(
                item_id=1,
                price_table_id="gold",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fixed_pricesonapricetable(
            item_id, price_table_id, request_options=request_options
        )
        return _response.data

    async def createorupdatefixedpricesonpricetableortradepolicy(
        self,
        item_id: int,
        price_table_id: str,
        *,
        request: typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU **price table** name or **trade policy** ID.

        request : typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.prices_and_fixed_prices import (
            CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.createorupdatefixedpricesonpricetableortradepolicy(
                item_id=1,
                price_table_id="priceTableA",
                request=[
                    CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem(
                        min_quantity=2,
                        value=50.5,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createorupdatefixedpricesonpricetableortradepolicy(
            item_id, price_table_id, request=request, request_options=request_options
        )
        return _response.data

    async def deletefixedpricesonapricetableortradepolicy(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table or Trade Policy Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prices_and_fixed_prices.deletefixedpricesonapricetableortradepolicy(
                item_id=1,
                price_table_id="gold",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletefixedpricesonapricetableortradepolicy(
            item_id, price_table_id, request_options=request_options
        )
        return _response.data
