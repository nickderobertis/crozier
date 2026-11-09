

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_file_response import DeleteFileResponse
from ..types.list_files_response import ListFilesResponse
from ..types.open_ai_file import OpenAiFile
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.create_file_request_purpose import CreateFileRequestPurpose


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

    def list_files(
        self, *, purpose: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFilesResponse:
        """
        Parameters
        ----------
        purpose : typing.Optional[str]
            Only return files with the given purpose.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.list_files()
        """
        _response = self._raw_client.list_files(purpose=purpose, request_options=request_options)
        return _response.data

    def create_file(
        self,
        *,
        file: core.File,
        purpose: CreateFileRequestPurpose,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiFile:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        purpose : CreateFileRequestPurpose
            The intended purpose of the uploaded file.

            Use "fine-tune" for [Fine-tuning](/docs/api-reference/fine-tuning) and "assistants" for [Assistants](/docs/api-reference/assistants) and [Messages](/docs/api-reference/messages). This allows us to validate the format of the uploaded file is correct for fine-tuning.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiFile
            OK

        Examples
        --------
        from fern.files import CreateFileRequestPurpose

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.create_file(
            purpose=CreateFileRequestPurpose.FINE_TUNE,
        )
        """
        _response = self._raw_client.create_file(file=file, purpose=purpose, request_options=request_options)
        return _response.data

    def retrieve_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAiFile:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiFile
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.retrieve_file(
            file_id="file_id",
        )
        """
        _response = self._raw_client.retrieve_file(file_id, request_options=request_options)
        return _response.data

    def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFileResponse:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFileResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.delete_file(
            file_id="file_id",
        )
        """
        _response = self._raw_client.delete_file(file_id, request_options=request_options)
        return _response.data

    def download_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.download_file(
            file_id="file_id",
        )
        """
        _response = self._raw_client.download_file(file_id, request_options=request_options)
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

    async def list_files(
        self, *, purpose: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFilesResponse:
        """
        Parameters
        ----------
        purpose : typing.Optional[str]
            Only return files with the given purpose.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.list_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files(purpose=purpose, request_options=request_options)
        return _response.data

    async def create_file(
        self,
        *,
        file: core.File,
        purpose: CreateFileRequestPurpose,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiFile:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        purpose : CreateFileRequestPurpose
            The intended purpose of the uploaded file.

            Use "fine-tune" for [Fine-tuning](/docs/api-reference/fine-tuning) and "assistants" for [Assistants](/docs/api-reference/assistants) and [Messages](/docs/api-reference/messages). This allows us to validate the format of the uploaded file is correct for fine-tuning.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiFile
            OK

        Examples
        --------
        import asyncio

        from fern.files import CreateFileRequestPurpose

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.create_file(
                purpose=CreateFileRequestPurpose.FINE_TUNE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_file(file=file, purpose=purpose, request_options=request_options)
        return _response.data

    async def retrieve_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OpenAiFile:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiFile
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.retrieve_file(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_file(file_id, request_options=request_options)
        return _response.data

    async def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFileResponse:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFileResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.delete_file(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file(file_id, request_options=request_options)
        return _response.data

    async def download_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        file_id : str
            The ID of the file to use for this request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.download_file(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_file(file_id, request_options=request_options)
        return _response.data
