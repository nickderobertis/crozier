

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.kitty import Kitty
from .raw_client import AsyncRawMintingClient, RawMintingClient


OMIT = typing.cast(typing.Any, ...)


class MintingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMintingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMintingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMintingClient
        """
        return self._raw_client

    def mint_kitty(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> Kitty:
        """
        Mint new kitty

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
        client.minting.mint_kitty(
            request="Bella",
        )
        """
        _response = self._raw_client.mint_kitty(request=request, request_options=request_options)
        return _response.data

    def mint_tradable_kitty(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        is_available_for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kitty:
        """
        Mint new tradable kitty

        Parameters
        ----------
        name : typing.Optional[str]
            name of the new kitty, if not present random name will be selected

        is_available_for_sale : typing.Optional[bool]
            false by default

        price : typing.Optional[float]
            Price of Kitty if is-available-for-sale is false, then the price will be ignored. If  is-available-for-sale is false and price is not provided then default price will be selected.

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
        client.minting.mint_tradable_kitty()
        """
        _response = self._raw_client.mint_tradable_kitty(
            name=name, is_available_for_sale=is_available_for_sale, price=price, request_options=request_options
        )
        return _response.data


class AsyncMintingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMintingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMintingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMintingClient
        """
        return self._raw_client

    async def mint_kitty(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> Kitty:
        """
        Mint new kitty

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
            await client.minting.mint_kitty(
                request="Bella",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mint_kitty(request=request, request_options=request_options)
        return _response.data

    async def mint_tradable_kitty(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        is_available_for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Kitty:
        """
        Mint new tradable kitty

        Parameters
        ----------
        name : typing.Optional[str]
            name of the new kitty, if not present random name will be selected

        is_available_for_sale : typing.Optional[bool]
            false by default

        price : typing.Optional[float]
            Price of Kitty if is-available-for-sale is false, then the price will be ignored. If  is-available-for-sale is false and price is not provided then default price will be selected.

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
            await client.minting.mint_tradable_kitty()


        asyncio.run(main())
        """
        _response = await self._raw_client.mint_tradable_kitty(
            name=name, is_available_for_sale=is_available_for_sale, price=price, request_options=request_options
        )
        return _response.data
