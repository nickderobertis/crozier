

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawArchiveClient, RawArchiveClient


class ArchiveClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArchiveClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArchiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArchiveClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Archived filings.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archive.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncArchiveClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArchiveClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArchiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArchiveClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Archived filings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archive.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
