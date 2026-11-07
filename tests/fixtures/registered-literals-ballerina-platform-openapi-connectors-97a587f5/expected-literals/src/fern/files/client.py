

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file import File
from ..types.file_list import FileList
from ..types.purpose import Purpose
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.files_upload_request_purpose import FilesUploadRequestPurpose


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

    def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> FileList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.list(
            api_version="api-version",
        )
        """
        _response = self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data

    def upload(
        self,
        *,
        api_version: str,
        purpose: FilesUploadRequestPurpose,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : FilesUploadRequestPurpose
            The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            The file has been successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.upload(
            api_version="api-version",
            purpose="fine-tune",
        )
        """
        _response = self._raw_client.upload(
            api_version=api_version, purpose=purpose, file=file, request_options=request_options
        )
        return _response.data

    def get(self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.get(
            file_id="file-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.get(file_id, api_version=api_version, request_options=request_options)
        return _response.data

    def delete(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.delete(
            file_id="file-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.delete(file_id, api_version=api_version, request_options=request_options)
        return _response.data

    def getcontent(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Success
        """
        with self._raw_client.getcontent(file_id, api_version=api_version, request_options=request_options) as r:
            yield from r.data

    def import_(
        self,
        *,
        api_version: str,
        purpose: Purpose,
        filename: str,
        content_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : Purpose

        filename : str
            The name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
            If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields representing your training examples.

        content_url : str
            The url to download the document from (can be SAS url of a blob or any other external url accessible with a GET request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            The file has been successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.import_(
            api_version="api-version",
            purpose="fine-tune",
            filename="filename",
            content_url="content_url",
        )
        """
        _response = self._raw_client.import_(
            api_version=api_version,
            purpose=purpose,
            filename=filename,
            content_url=content_url,
            request_options=request_options,
        )
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

    async def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> FileList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.list(
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data

    async def upload(
        self,
        *,
        api_version: str,
        purpose: FilesUploadRequestPurpose,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : FilesUploadRequestPurpose
            The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            The file has been successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.upload(
                api_version="api-version",
                purpose="fine-tune",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload(
            api_version=api_version, purpose=purpose, file=file, request_options=request_options
        )
        return _response.data

    async def get(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> File:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.get(
                file_id="file-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(file_id, api_version=api_version, request_options=request_options)
        return _response.data

    async def delete(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.delete(
                file_id="file-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(file_id, api_version=api_version, request_options=request_options)
        return _response.data

    async def getcontent(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Success
        """
        async with self._raw_client.getcontent(file_id, api_version=api_version, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def import_(
        self,
        *,
        api_version: str,
        purpose: Purpose,
        filename: str,
        content_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : Purpose

        filename : str
            The name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
            If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields representing your training examples.

        content_url : str
            The url to download the document from (can be SAS url of a blob or any other external url accessible with a GET request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            The file has been successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.import_(
                api_version="api-version",
                purpose="fine-tune",
                filename="filename",
                content_url="content_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_(
            api_version=api_version,
            purpose=purpose,
            filename=filename,
            content_url=content_url,
            request_options=request_options,
        )
        return _response.data
