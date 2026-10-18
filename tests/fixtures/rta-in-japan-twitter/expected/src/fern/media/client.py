

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMediaClient, RawMediaClient
from .types.post_media_upload_response import PostMediaUploadResponse


OMIT = typing.cast(typing.Any, ...)


class MediaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMediaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMediaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMediaClient
        """
        return self._raw_client

    def post_media_upload(
        self, *, file: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMediaUploadResponse:
        """
        画像、動画ファイルをアップロードする。

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMediaUploadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.media.post_media_upload()
        """
        _response = self._raw_client.post_media_upload(file=file, request_options=request_options)
        return _response.data


class AsyncMediaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMediaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMediaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMediaClient
        """
        return self._raw_client

    async def post_media_upload(
        self, *, file: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMediaUploadResponse:
        """
        画像、動画ファイルをアップロードする。

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMediaUploadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.media.post_media_upload()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_media_upload(file=file, request_options=request_options)
        return _response.data
