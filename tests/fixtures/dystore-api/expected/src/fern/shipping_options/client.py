

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawShippingOptionsClient, RawShippingOptionsClient


class ShippingOptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShippingOptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShippingOptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShippingOptionsClient
        """
        return self._raw_client

    def list_shipping_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List shipping options

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
        client.shipping_options.list_shipping_options()
        """
        _response = self._raw_client.list_shipping_options(request_options=request_options)
        return _response.data


class AsyncShippingOptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShippingOptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShippingOptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShippingOptionsClient
        """
        return self._raw_client

    async def list_shipping_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List shipping options

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
            await client.shipping_options.list_shipping_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_shipping_options(request_options=request_options)
        return _response.data
