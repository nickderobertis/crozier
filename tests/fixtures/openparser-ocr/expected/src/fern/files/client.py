

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_file_response import DeleteFileResponse
from ..types.public_file import PublicFile
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

    def create_file(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> PublicFile:
        """
        Upload bytes directly to OpenParser's Eigenpal-compatible tenant file pool. Files may be
        reused by later parse or extract requests through `file_id`; bytes do not pass through
        Vercel.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicFile
            Uploaded reusable file

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.create_file()
        """
        _response = self._raw_client.create_file(file=file, request_options=request_options)
        return _response.data

    def get_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PublicFile:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicFile
            Reusable file metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.get_file(
            id="id",
        )
        """
        _response = self._raw_client.get_file(id, request_options=request_options)
        return _response.data

    def delete_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteFileResponse:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFileResponse
            File deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.delete_file(
            id="id",
        )
        """
        _response = self._raw_client.delete_file(id, request_options=request_options)
        return _response.data

    def get_file_content(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            File content

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.get_file_content(
            id="id",
        )
        """
        with self._raw_client.get_file_content(id, request_options=request_options) as r:
            yield from r.data


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

    async def create_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicFile:
        """
        Upload bytes directly to OpenParser's Eigenpal-compatible tenant file pool. Files may be
        reused by later parse or extract requests through `file_id`; bytes do not pass through
        Vercel.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicFile
            Uploaded reusable file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.create_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_file(file=file, request_options=request_options)
        return _response.data

    async def get_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PublicFile:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicFile
            Reusable file metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_file(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file(id, request_options=request_options)
        return _response.data

    async def delete_file(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFileResponse:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFileResponse
            File deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.delete_file(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file(id, request_options=request_options)
        return _response.data

    async def get_file_content(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        id : str
            Tenant-scoped reusable file identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            File content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_file_content(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_file_content(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
