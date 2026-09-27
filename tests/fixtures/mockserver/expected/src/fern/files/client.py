

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.put_mockserver_files_store_response import PutMockserverFilesStoreResponse


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

    def store_a_file_in_the_file_store(
        self,
        *,
        name: str,
        content: str,
        base64: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverFilesStoreResponse:
        """
        stores a file (text or base64-encoded binary) under the supplied name in the in-memory file store

        Parameters
        ----------
        name : str
            name to store the file under

        content : str
            file content, either plain text or base64-encoded when base64 is true

        base64 : typing.Optional[bool]
            when true, content is treated as base64-encoded binary data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverFilesStoreResponse
            file stored

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.store_a_file_in_the_file_store(
            name="template.json",
            content='{"status":"ok"}',
        )
        """
        _response = self._raw_client.store_a_file_in_the_file_store(
            name=name, content=content, base64=base64, request_options=request_options
        )
        return _response.data

    def retrieve_a_file_from_the_file_store(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        returns the raw bytes of a previously stored file

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            file content returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.retrieve_a_file_from_the_file_store(
            name="name",
        )
        """
        with self._raw_client.retrieve_a_file_from_the_file_store(name=name, request_options=request_options) as r:
            yield from r.data

    def list_files_in_the_file_store(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        returns the names of all files currently held in the in-memory file store

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            list of file names returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.list_files_in_the_file_store()
        """
        _response = self._raw_client.list_files_in_the_file_store(request_options=request_options)
        return _response.data

    def delete_a_file_from_the_file_store(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        removes a previously stored file from the in-memory file store

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.delete_a_file_from_the_file_store(
            name="template.json",
        )
        """
        _response = self._raw_client.delete_a_file_from_the_file_store(name=name, request_options=request_options)
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

    async def store_a_file_in_the_file_store(
        self,
        *,
        name: str,
        content: str,
        base64: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverFilesStoreResponse:
        """
        stores a file (text or base64-encoded binary) under the supplied name in the in-memory file store

        Parameters
        ----------
        name : str
            name to store the file under

        content : str
            file content, either plain text or base64-encoded when base64 is true

        base64 : typing.Optional[bool]
            when true, content is treated as base64-encoded binary data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverFilesStoreResponse
            file stored

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.store_a_file_in_the_file_store(
                name="template.json",
                content='{"status":"ok"}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_a_file_in_the_file_store(
            name=name, content=content, base64=base64, request_options=request_options
        )
        return _response.data

    async def retrieve_a_file_from_the_file_store(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        returns the raw bytes of a previously stored file

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            file content returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.retrieve_a_file_from_the_file_store(
                name="name",
            )


        asyncio.run(main())
        """
        async with self._raw_client.retrieve_a_file_from_the_file_store(
            name=name, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def list_files_in_the_file_store(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        returns the names of all files currently held in the in-memory file store

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            list of file names returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.list_files_in_the_file_store()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files_in_the_file_store(request_options=request_options)
        return _response.data

    async def delete_a_file_from_the_file_store(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        removes a previously stored file from the in-memory file store

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.delete_a_file_from_the_file_store(
                name="template.json",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_file_from_the_file_store(name=name, request_options=request_options)
        return _response.data
