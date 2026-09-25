

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUtilitiesClient, RawUtilitiesClient
from .types.get_customer_hub_embed_response import GetCustomerHubEmbedResponse
from .types.ping_response import PingResponse


OMIT = typing.cast(typing.Any, ...)


class UtilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUtilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUtilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUtilitiesClient
        """
        return self._raw_client

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> PingResponse:
        """
        Test your API key and connection to the ThriveCart API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PingResponse
            Successful ping response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.utilities.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data

    def get_customer_hub_embed(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerHubEmbedResponse:
        """
        Generate an embeddable customer hub URL for a specific customer.

        Parameters
        ----------
        email : str
            Customer email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerHubEmbedResponse
            Embed URL

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.utilities.get_customer_hub_embed(
            email="email",
        )
        """
        _response = self._raw_client.get_customer_hub_embed(email=email, request_options=request_options)
        return _response.data


class AsyncUtilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUtilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUtilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUtilitiesClient
        """
        return self._raw_client

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> PingResponse:
        """
        Test your API key and connection to the ThriveCart API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PingResponse
            Successful ping response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.utilities.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data

    async def get_customer_hub_embed(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerHubEmbedResponse:
        """
        Generate an embeddable customer hub URL for a specific customer.

        Parameters
        ----------
        email : str
            Customer email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerHubEmbedResponse
            Embed URL

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.utilities.get_customer_hub_embed(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer_hub_embed(email=email, request_options=request_options)
        return _response.data
