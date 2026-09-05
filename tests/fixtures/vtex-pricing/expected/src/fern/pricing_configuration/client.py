

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pricing_configuration import PricingConfiguration
from .raw_client import AsyncRawPricingConfigurationClient, RawPricingConfigurationClient
from .types.get_pricingv2status_response import GetPricingv2StatusResponse


class PricingConfigurationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPricingConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPricingConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPricingConfigurationClient
        """
        return self._raw_client

    def get_pricing_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> PricingConfiguration:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PricingConfiguration
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.pricing_configuration.get_pricing_config()
        """
        _response = self._raw_client.get_pricing_config(request_options=request_options)
        return _response.data

    def get_pricingv2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPricingv2StatusResponse:
        """
        Retrieves Pricing v2 Status.
        ## Response body example

        ```json
        {
            "isActive": true,
            "hasMigrated": true
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingv2StatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.pricing_configuration.get_pricingv2status()
        """
        _response = self._raw_client.get_pricingv2status(request_options=request_options)
        return _response.data


class AsyncPricingConfigurationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPricingConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPricingConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPricingConfigurationClient
        """
        return self._raw_client

    async def get_pricing_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PricingConfiguration:
        """
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

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PricingConfiguration
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
            await client.pricing_configuration.get_pricing_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_config(request_options=request_options)
        return _response.data

    async def get_pricingv2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPricingv2StatusResponse:
        """
        Retrieves Pricing v2 Status.
        ## Response body example

        ```json
        {
            "isActive": true,
            "hasMigrated": true
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingv2StatusResponse
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
            await client.pricing_configuration.get_pricingv2status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricingv2status(request_options=request_options)
        return _response.data
