

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file_metadata import FileMetadata
from ..types.upload_response import UploadResponse
from .raw_client import AsyncRawFormsClient, RawFormsClient


OMIT = typing.cast(typing.Any, ...)


class FormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormsClient
        """
        return self._raw_client

    def upload(
        self,
        *,
        file: core.File,
        filename: typing.Optional[str] = OMIT,
        metadata: typing.Optional[FileMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        filename : typing.Optional[str]

        metadata : typing.Optional[FileMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.forms.upload()
        """
        _response = self._raw_client.upload(
            file=file, filename=filename, metadata=metadata, request_options=request_options
        )
        return _response.data

    def submit(
        self,
        *,
        name: str,
        age: typing.Optional[int] = OMIT,
        subscribe: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        age : typing.Optional[int]

        subscribe : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.forms.submit(
            name="name",
        )
        """
        _response = self._raw_client.submit(name=name, age=age, subscribe=subscribe, request_options=request_options)
        return _response.data


class AsyncFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormsClient
        """
        return self._raw_client

    async def upload(
        self,
        *,
        file: core.File,
        filename: typing.Optional[str] = OMIT,
        metadata: typing.Optional[FileMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        filename : typing.Optional[str]

        metadata : typing.Optional[FileMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.forms.upload()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload(
            file=file, filename=filename, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def submit(
        self,
        *,
        name: str,
        age: typing.Optional[int] = OMIT,
        subscribe: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        age : typing.Optional[int]

        subscribe : typing.Optional[bool]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.forms.submit(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit(
            name=name, age=age, subscribe=subscribe, request_options=request_options
        )
        return _response.data
