

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawShippingClient, RawShippingClient


class ShippingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShippingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShippingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShippingClient
        """
        return self._raw_client

    def list_of_supported_shipping_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of supported shipping providers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shipping.list_of_supported_shipping_providers()
        """
        _response = self._raw_client.list_of_supported_shipping_providers(request_options=request_options)
        return _response.data

    def get_shipping_regions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.shipping.get_shipping_regions()
        """
        _response = self._raw_client.get_shipping_regions(request_options=request_options)
        return _response.data


class AsyncShippingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShippingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShippingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShippingClient
        """
        return self._raw_client

    async def list_of_supported_shipping_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported shipping providers

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shipping.list_of_supported_shipping_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_shipping_providers(request_options=request_options)
        return _response.data

    async def get_shipping_regions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.shipping.get_shipping_regions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shipping_regions(request_options=request_options)
        return _response.data
