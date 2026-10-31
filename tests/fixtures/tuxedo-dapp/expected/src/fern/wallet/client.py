

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.kitty import Kitty
from .raw_client import AsyncRawWalletClient, RawWalletClient


OMIT = typing.cast(typing.Any, ...)


class WalletClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWalletClient
        """
        return self._raw_client

    def show_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Get amount of money

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallet.show_balance()
        """
        _response = self._raw_client.show_balance(request_options=request_options)
        return _response.data

    def buy_kitty(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> Kitty:
        """
        Trade your money for a kitty, there sign from wallet will be required

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kitty
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallet.buy_kitty(
            request="515315728237564593861820790636439631664048948986843239490053062984016986",
        )
        """
        _response = self._raw_client.buy_kitty(request=request, request_options=request_options)
        return _response.data


class AsyncWalletClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWalletClient
        """
        return self._raw_client

    async def show_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Get amount of money

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallet.show_balance()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_balance(request_options=request_options)
        return _response.data

    async def buy_kitty(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> Kitty:
        """
        Trade your money for a kitty, there sign from wallet will be required

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Kitty
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallet.buy_kitty(
                request="515315728237564593861820790636439631664048948986843239490053062984016986",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.buy_kitty(request=request, request_options=request_options)
        return _response.data
