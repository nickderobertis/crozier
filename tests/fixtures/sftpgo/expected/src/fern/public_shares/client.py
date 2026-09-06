

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.dir_entry import DirEntry
from .raw_client import AsyncRawPublicSharesClient, RawPublicSharesClient


OMIT = typing.cast(typing.Any, ...)


class PublicSharesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicSharesClient
        """
        return self._raw_client

    def get_share(
        self,
        id: str,
        *,
        compress: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        A zip file, containing the shared files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip. The share must be defined with the read scope and the associated user must have list and download permissions

        Parameters
        ----------
        id : str
            the share id

        compress : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.public_shares.get_share(
            id="id",
        )
        """
        with self._raw_client.get_share(id, compress=compress, request_options=request_options) as r:
            yield from r.data

    def upload_to_share(
        self,
        id: str,
        *,
        filenames: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        The share must be defined with the write scope and the associated user must have the upload permission

        Parameters
        ----------
        id : str
            the share id

        filenames : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.public_shares.upload_to_share(
            id="id",
        )
        """
        _response = self._raw_client.upload_to_share(id, filenames=filenames, request_options=request_options)
        return _response.data

    def download_share_file(
        self, id: str, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns the file contents as response body. The share must have exactly one path defined and it must be a directory for this to work

        Parameters
        ----------
        id : str
            the share id

        path : str
            Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.public_shares.download_share_file(
            id="id",
            path="path",
        )
        """
        with self._raw_client.download_share_file(id, path=path, request_options=request_options) as r:
            yield from r.data

    def get_share_dir_contents(
        self, id: str, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DirEntry]:
        """
        Returns the contents of the specified directory for the specified share. The share must have exactly one path defined and it must be a directory for this to work

        Parameters
        ----------
        id : str
            the share id

        path : typing.Optional[str]
            Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DirEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.public_shares.get_share_dir_contents(
            id="id",
        )
        """
        _response = self._raw_client.get_share_dir_contents(id, path=path, request_options=request_options)
        return _response.data

    def upload_single_to_share(
        self,
        id: str,
        file_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        The share must be defined with the write scope and the associated user must have the upload/overwrite permissions

        Parameters
        ----------
        id : str
            the share id

        file_name : str
            the name of the new file. It must be path encoded. Sub directories are not accepted

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = self._raw_client.upload_single_to_share(
            id, file_name, request=request, request_options=request_options
        )
        return _response.data


class AsyncPublicSharesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicSharesClient
        """
        return self._raw_client

    async def get_share(
        self,
        id: str,
        *,
        compress: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        A zip file, containing the shared files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip. The share must be defined with the read scope and the associated user must have list and download permissions

        Parameters
        ----------
        id : str
            the share id

        compress : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.public_shares.get_share(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_share(id, compress=compress, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def upload_to_share(
        self,
        id: str,
        *,
        filenames: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        The share must be defined with the write scope and the associated user must have the upload permission

        Parameters
        ----------
        id : str
            the share id

        filenames : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.public_shares.upload_to_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_to_share(id, filenames=filenames, request_options=request_options)
        return _response.data

    async def download_share_file(
        self, id: str, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns the file contents as response body. The share must have exactly one path defined and it must be a directory for this to work

        Parameters
        ----------
        id : str
            the share id

        path : str
            Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.public_shares.download_share_file(
                id="id",
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_share_file(id, path=path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_share_dir_contents(
        self, id: str, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DirEntry]:
        """
        Returns the contents of the specified directory for the specified share. The share must have exactly one path defined and it must be a directory for this to work

        Parameters
        ----------
        id : str
            the share id

        path : typing.Optional[str]
            Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DirEntry]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.public_shares.get_share_dir_contents(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_share_dir_contents(id, path=path, request_options=request_options)
        return _response.data

    async def upload_single_to_share(
        self,
        id: str,
        file_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        The share must be defined with the write scope and the associated user must have the upload/overwrite permissions

        Parameters
        ----------
        id : str
            the share id

        file_name : str
            the name of the new file. It must be path encoded. Sub directories are not accepted

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = await self._raw_client.upload_single_to_share(
            id, file_name, request=request, request_options=request_options
        )
        return _response.data
