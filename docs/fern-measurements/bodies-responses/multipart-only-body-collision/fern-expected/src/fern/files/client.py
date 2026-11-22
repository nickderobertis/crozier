

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stored_file import StoredFile
from .raw_client import AsyncRawFilesClient, RawFilesClient


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def upload_file(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> StoredFile:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoredFile
            Stored.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.upload_file()
        """
        _response = self._raw_client.upload_file(file=file, request_options=request_options)
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def upload_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> StoredFile:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoredFile
            Stored.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.upload_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file(file=file, request_options=request_options)
        return _response.data
