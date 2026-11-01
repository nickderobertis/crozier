

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

    def get_archive_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            File download or directory listing

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.archive.get_archive_path(
            path="path",
        )
        """
        with self._raw_client.get_archive_path(path, request_options=request_options) as r:
            yield from r.data


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

    async def get_archive_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            File download or directory listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.archive.get_archive_path(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_archive_path(path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
