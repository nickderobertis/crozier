

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file import File
from .raw_client import AsyncRawFileClient, RawFileClient
from .types.post_files_request_folder import PostFilesRequestFolder


OMIT = typing.cast(typing.Any, ...)


class FileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileClient
        """
        return self._raw_client

    def get_files(
        self, *, folder: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[File]:
        """
        Retrieve a list of files

        Parameters
        ----------
        folder : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            The list of files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.file.get_files()
        """
        _response = self._raw_client.get_files(folder=folder, request_options=request_options)
        return _response.data

    def post_files(
        self,
        *,
        file: core.File,
        folder: PostFilesRequestFolder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Upload a new file

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        folder : PostFilesRequestFolder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            Uploaded file

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.file.post_files(
            folder="folder",
        )
        """
        _response = self._raw_client.post_files(file=file, folder=folder, request_options=request_options)
        return _response.data

    def delete_files_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a file

        Parameters
        ----------
        id : str

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
        client.file.delete_files_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_files_id(id, request_options=request_options)
        return _response.data


class AsyncFileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileClient
        """
        return self._raw_client

    async def get_files(
        self, *, folder: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[File]:
        """
        Retrieve a list of files

        Parameters
        ----------
        folder : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            The list of files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.file.get_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_files(folder=folder, request_options=request_options)
        return _response.data

    async def post_files(
        self,
        *,
        file: core.File,
        folder: PostFilesRequestFolder,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Upload a new file

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        folder : PostFilesRequestFolder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            Uploaded file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.file.post_files(
                folder="folder",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_files(file=file, folder=folder, request_options=request_options)
        return _response.data

    async def delete_files_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a file

        Parameters
        ----------
        id : str

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
            await client.file.delete_files_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_files_id(id, request_options=request_options)
        return _response.data
