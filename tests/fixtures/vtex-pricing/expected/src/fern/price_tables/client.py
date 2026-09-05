

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPriceTablesClient, RawPriceTablesClient
from .types.getallpricetablesandrules_response_item import GetallpricetablesandrulesResponseItem
from .types.getrulesforapricetable_response import GetrulesforapricetableResponse
from .types.put_pricing_pipeline_catalog_price_table_id_request_rules_item import (
    PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
)


OMIT = typing.cast(typing.Any, ...)


class PriceTablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPriceTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPriceTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPriceTablesClient
        """
        return self._raw_client

    def getallpricetablesandrules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetallpricetablesandrulesResponseItem]:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetallpricetablesandrulesResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.price_tables.getallpricetablesandrules()
        """
        _response = self._raw_client.getallpricetablesandrules(request_options=request_options)
        return _response.data

    def getrulesforapricetable(
        self, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetrulesforapricetableResponse:
        """
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

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetrulesforapricetableResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.price_tables.getrulesforapricetable(
            price_table_id="b2c",
        )
        """
        _response = self._raw_client.getrulesforapricetable(price_table_id, request_options=request_options)
        return _response.data

    def update_rules_for_a_price_table(
        self,
        price_table_id: str,
        *,
        rules: typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        rules : typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.price_tables import (
            PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange,
        )

        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.price_tables.update_rules_for_a_price_table(
            price_table_id="priceTableId",
            rules=[
                PutPricingPipelineCatalogPriceTableIdRequestRulesItem(
                    context=PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext(
                        brands={"Brand ID": "2000002", "Brand Name": "Whiskas"},
                        categories={"Category ID": "1", "Category Name": "Alimentação"},
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
                    percentual_modifier=0.0,
                )
            ],
        )
        """
        _response = self._raw_client.update_rules_for_a_price_table(
            price_table_id, rules=rules, request_options=request_options
        )
        return _response.data

    def listpricetables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.price_tables.listpricetables()
        """
        _response = self._raw_client.listpricetables(request_options=request_options)
        return _response.data


class AsyncPriceTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPriceTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPriceTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPriceTablesClient
        """
        return self._raw_client

    async def getallpricetablesandrules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetallpricetablesandrulesResponseItem]:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetallpricetablesandrulesResponseItem]
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
            await client.price_tables.getallpricetablesandrules()


        asyncio.run(main())
        """
        _response = await self._raw_client.getallpricetablesandrules(request_options=request_options)
        return _response.data

    async def getrulesforapricetable(
        self, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetrulesforapricetableResponse:
        """
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

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetrulesforapricetableResponse
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
            await client.price_tables.getrulesforapricetable(
                price_table_id="b2c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrulesforapricetable(price_table_id, request_options=request_options)
        return _response.data

    async def update_rules_for_a_price_table(
        self,
        price_table_id: str,
        *,
        rules: typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        rules : typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.price_tables import (
            PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange,
            PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.price_tables.update_rules_for_a_price_table(
                price_table_id="priceTableId",
                rules=[
                    PutPricingPipelineCatalogPriceTableIdRequestRulesItem(
                        context=PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext(
                            brands={"Brand ID": "2000002", "Brand Name": "Whiskas"},
                            categories={
                                "Category ID": "1",
                                "Category Name": "Alimentação",
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
                        percentual_modifier=0.0,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_rules_for_a_price_table(
            price_table_id, rules=rules, request_options=request_options
        )
        return _response.data

    async def listpricetables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
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
            await client.price_tables.listpricetables()


        asyncio.run(main())
        """
        _response = await self._raw_client.listpricetables(request_options=request_options)
        return _response.data
