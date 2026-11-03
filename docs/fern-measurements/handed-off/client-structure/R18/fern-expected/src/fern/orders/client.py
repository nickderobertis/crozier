

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrdersClient, RawOrdersClient
from .types.place_order_response import PlaceOrderResponse


OMIT = typing.cast(typing.Any, ...)


class OrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrdersClient
        """
        return self._raw_client

    def place_order(self, *, sku: str, request_options: typing.Optional[RequestOptions] = None) -> PlaceOrderResponse:
        """
        Parameters
        ----------
        sku : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaceOrderResponse
            The placed order.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            channel="YOUR_CHANNEL",
        )
        client.orders.place_order(
            sku="sku",
        )
        """
        _response = self._raw_client.place_order(sku=sku, request_options=request_options)
        return _response.data


class AsyncOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrdersClient
        """
        return self._raw_client

    async def place_order(
        self, *, sku: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaceOrderResponse:
        """
        Parameters
        ----------
        sku : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaceOrderResponse
            The placed order.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            channel="YOUR_CHANNEL",
        )


        async def main() -> None:
            await client.orders.place_order(
                sku="sku",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.place_order(sku=sku, request_options=request_options)
        return _response.data
