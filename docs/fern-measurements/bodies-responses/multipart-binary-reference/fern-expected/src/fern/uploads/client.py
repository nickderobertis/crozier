

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.form_file import FormFile
from .raw_client import AsyncRawUploadsClient, RawUploadsClient


OMIT = typing.cast(typing.Any, ...)


class UploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadsClient
        """
        return self._raw_client

    def upload_log(
        self,
        *,
        file: FormFile,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file : FormFile

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.upload_log(
            file="file",
        )
        """
        _response = self._raw_client.upload_log(file=file, note=note, request_options=request_options)
        return _response.data

    def transcribe_recording(
        self,
        *,
        model: str,
        file: typing.Optional[FormFile] = OMIT,
        file_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        model : str

        file : typing.Optional[FormFile]

        file_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.transcribe_recording(
            model="model",
        )
        """
        _response = self._raw_client.transcribe_recording(
            model=model, file=file, file_url=file_url, request_options=request_options
        )
        return _response.data


class AsyncUploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadsClient
        """
        return self._raw_client

    async def upload_log(
        self,
        *,
        file: FormFile,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        file : FormFile

        note : typing.Optional[str]

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
            await client.uploads.upload_log(
                file="file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_log(file=file, note=note, request_options=request_options)
        return _response.data

    async def transcribe_recording(
        self,
        *,
        model: str,
        file: typing.Optional[FormFile] = OMIT,
        file_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        model : str

        file : typing.Optional[FormFile]

        file_url : typing.Optional[str]

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
            await client.uploads.transcribe_recording(
                model="model",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transcribe_recording(
            model=model, file=file, file_url=file_url, request_options=request_options
        )
        return _response.data
