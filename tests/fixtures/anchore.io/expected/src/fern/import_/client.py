

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.anchore_image_list import AnchoreImageList
from .raw_client import AsyncRawImportClient, RawImportClient


OMIT = typing.cast(typing.Any, ...)


class ImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportClient
        """
        return self._raw_client

    def image_archive(
        self, *, archive_file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AnchoreImageList:
        """
        Parameters
        ----------
        archive_file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchoreImageList
            Successfully imported image to the engine

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.import_.image_archive()
        """
        _response = self._raw_client.image_archive(archive_file=archive_file, request_options=request_options)
        return _response.data


class AsyncImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportClient
        """
        return self._raw_client

    async def image_archive(
        self, *, archive_file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AnchoreImageList:
        """
        Parameters
        ----------
        archive_file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchoreImageList
            Successfully imported image to the engine

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.import_.image_archive()


        asyncio.run(main())
        """
        _response = await self._raw_client.image_archive(archive_file=archive_file, request_options=request_options)
        return _response.data
