

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.download_dto_in import DownloadDtoIn
from ..types.download_dto_out import DownloadDtoOut
from ..types.download_status_dto import DownloadStatusDto
from ..types.status_dto import StatusDto
from ..types.success_response import SuccessResponse
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

    def file_count(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusDto
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_count()
        """
        _response = self._raw_client.file_count(request_options=request_options)
        return _response.data

    def file_download(
        self, *, request: typing.Sequence[DownloadDtoIn], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DownloadDtoOut]:
        """
        Parameters
        ----------
        request : typing.Sequence[DownloadDtoIn]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DownloadDtoOut]
            Successful Response

        Examples
        --------
        from fern import DownloadDtoIn, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_download(
            request=[
                DownloadDtoIn(
                    name="name",
                    path="path",
                    url="url",
                )
            ],
        )
        """
        _response = self._raw_client.file_download(request=request, request_options=request_options)
        return _response.data

    def file_status(self, hash: str, *, request_options: typing.Optional[RequestOptions] = None) -> DownloadDtoOut:
        """
        Parameters
        ----------
        hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadDtoOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_status(
            hash="hash",
        )
        """
        _response = self._raw_client.file_status(hash, request_options=request_options)
        return _response.data

    def file_retry(self, hash: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Parameters
        ----------
        hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_retry(
            hash="hash",
        )
        """
        _response = self._raw_client.file_retry(hash, request_options=request_options)
        return _response.data

    def file_retry_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_retry_all()
        """
        _response = self._raw_client.file_retry_all(request_options=request_options)
        return _response.data

    def file_status_bulk(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadStatusDto:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadStatusDto
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.file_status_bulk(
            request=["string"],
        )
        """
        _response = self._raw_client.file_status_bulk(request=request, request_options=request_options)
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

    async def file_count(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusDto
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_count()


        asyncio.run(main())
        """
        _response = await self._raw_client.file_count(request_options=request_options)
        return _response.data

    async def file_download(
        self, *, request: typing.Sequence[DownloadDtoIn], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DownloadDtoOut]:
        """
        Parameters
        ----------
        request : typing.Sequence[DownloadDtoIn]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DownloadDtoOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DownloadDtoIn

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_download(
                request=[
                    DownloadDtoIn(
                        name="name",
                        path="path",
                        url="url",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_download(request=request, request_options=request_options)
        return _response.data

    async def file_status(
        self, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadDtoOut:
        """
        Parameters
        ----------
        hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadDtoOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_status(
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_status(hash, request_options=request_options)
        return _response.data

    async def file_retry(
        self, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_retry(
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_retry(hash, request_options=request_options)
        return _response.data

    async def file_retry_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_retry_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.file_retry_all(request_options=request_options)
        return _response.data

    async def file_status_bulk(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadStatusDto:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadStatusDto
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.file_status_bulk(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_status_bulk(request=request, request_options=request_options)
        return _response.data
