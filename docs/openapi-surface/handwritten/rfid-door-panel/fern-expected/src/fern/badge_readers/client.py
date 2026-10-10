

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.reader import Reader
from .raw_client import AsyncRawBadgeReadersClient, RawBadgeReadersClient


class BadgeReadersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBadgeReadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBadgeReadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBadgeReadersClient
        """
        return self._raw_client

    def badge_readers_get(self, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Reader:
        """
        Parameters
        ----------
        reader_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            The reader.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badge_readers.badge_readers_get(
            reader_id="readerId",
        )
        """
        _response = self._raw_client.badge_readers_get(reader_id, request_options=request_options)
        return _response.data


class AsyncBadgeReadersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBadgeReadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBadgeReadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBadgeReadersClient
        """
        return self._raw_client

    async def badge_readers_get(
        self, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Reader:
        """
        Parameters
        ----------
        reader_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            The reader.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badge_readers.badge_readers_get(
                reader_id="readerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.badge_readers_get(reader_id, request_options=request_options)
        return _response.data
