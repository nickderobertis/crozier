

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.kitty import Kitty
from .raw_client import AsyncRawListClient, RawListClient


class ListClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawListClient
        """
        return self._raw_client

    def show_all_kitties(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Kitty]:
        """
        Get all kitties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kitty]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_.show_all_kitties()
        """
        _response = self._raw_client.show_all_kitties(request_options=request_options)
        return _response.data

    def show_owned_kitties(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Kitty]:
        """
        Get owned kitties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kitty]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_.show_owned_kitties()
        """
        _response = self._raw_client.show_owned_kitties(request_options=request_options)
        return _response.data


class AsyncListClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawListClient
        """
        return self._raw_client

    async def show_all_kitties(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Kitty]:
        """
        Get all kitties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kitty]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_.show_all_kitties()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_all_kitties(request_options=request_options)
        return _response.data

    async def show_owned_kitties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Kitty]:
        """
        Get owned kitties

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kitty]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_.show_owned_kitties()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_owned_kitties(request_options=request_options)
        return _response.data
