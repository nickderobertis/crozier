

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cart import Cart
from .raw_client import AsyncRawCartsClient, RawCartsClient


class CartsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCartsClient
        """
        return self._raw_client

    def get_cart(self, cart_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cart:
        """
        Parameters
        ----------
        cart_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cart
            The cart.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.carts.get_cart(
            cart_id="cartId",
        )
        """
        _response = self._raw_client.get_cart(cart_id, request_options=request_options)
        return _response.data


class AsyncCartsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCartsClient
        """
        return self._raw_client

    async def get_cart(self, cart_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cart:
        """
        Parameters
        ----------
        cart_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cart
            The cart.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.carts.get_cart(
                cart_id="cartId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cart(cart_id, request_options=request_options)
        return _response.data
