

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.charter import Charter
from .raw_client import AsyncRawChartersClient, RawChartersClient


OMIT = typing.cast(typing.Any, ...)


class ChartersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChartersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChartersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChartersClient
        """
        return self._raw_client

    def book_charter(
        self,
        *,
        skipper: str,
        guests: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        skipper : str

        guests : typing.Optional[int]
            How many guests board.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.charters.book_charter(
            skipper="skipper",
        )
        """
        _response = self._raw_client.book_charter(skipper=skipper, guests=guests, request_options=request_options)
        return _response.data

    def get_charter(self, charter_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Charter:
        """
        Parameters
        ----------
        charter_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Charter
            The charter

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.charters.get_charter(
            charter_id="charter_id",
        )
        """
        _response = self._raw_client.get_charter(charter_id, request_options=request_options)
        return _response.data


class AsyncChartersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChartersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChartersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChartersClient
        """
        return self._raw_client

    async def book_charter(
        self,
        *,
        skipper: str,
        guests: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        skipper : str

        guests : typing.Optional[int]
            How many guests board.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.charters.book_charter(
                skipper="skipper",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book_charter(skipper=skipper, guests=guests, request_options=request_options)
        return _response.data

    async def get_charter(self, charter_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Charter:
        """
        Parameters
        ----------
        charter_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Charter
            The charter

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.charters.get_charter(
                charter_id="charter_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charter(charter_id, request_options=request_options)
        return _response.data
