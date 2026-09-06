

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.directory_listing_dto import DirectoryListingDto
from .raw_client import AsyncRawFileSystemClient, RawFileSystemClient


OMIT = typing.cast(typing.Any, ...)


class FileSystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileSystemClient
        """
        return self._raw_client

    def get_directory_listing(
        self, *, path: str, show_files: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> DirectoryListingDto:
        """
        List folders and files from the host server's file system. If no request body is passed then the root directories are returned.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        show_files : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DirectoryListingDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.file_system.get_directory_listing(
            path="path",
            show_files=True,
        )
        """
        _response = self._raw_client.get_directory_listing(
            path=path, show_files=show_files, request_options=request_options
        )
        return _response.data


class AsyncFileSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileSystemClient
        """
        return self._raw_client

    async def get_directory_listing(
        self, *, path: str, show_files: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> DirectoryListingDto:
        """
        List folders and files from the host server's file system. If no request body is passed then the root directories are returned.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        show_files : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DirectoryListingDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.file_system.get_directory_listing(
                path="path",
                show_files=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_directory_listing(
            path=path, show_files=show_files, request_options=request_options
        )
        return _response.data
