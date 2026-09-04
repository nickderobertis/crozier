

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.video import Video
from .raw_client import AsyncRawVideosClient, RawVideosClient


OMIT = typing.cast(typing.Any, ...)


class VideosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVideosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVideosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVideosClient
        """
        return self._raw_client

    def post_videos_video_id_source(
        self,
        video_id: str,
        *,
        file: core.File,
        content_range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Video:
        """
        Ingest a video from a source or file.

        Parameters
        ----------
        video_id : str
            Enter the videoId you want to use to upload your video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            `part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Video
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.videos.post_videos_video_id_source(
            video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
            content_range="bytes 209715200-419430399/524288000 OR part 2/3",
        )
        """
        _response = self._raw_client.post_videos_video_id_source(
            video_id, file=file, content_range=content_range, request_options=request_options
        )
        return _response.data

    def post_upload(
        self,
        *,
        token: str,
        file: core.File,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Video:
        """
        Uploading a video with the delegated upload token.

        Parameters
        ----------
        token : str
            The unique identifier for the token you want to use to upload a video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.

        video_id : typing.Optional[str]
            The video id returned by the first call to this endpoint in a large video upload scenario.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Video
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.videos.post_upload(
            content_range="Content-Range: bytes 200-100/5000",
            token="to1tcmSFHeYY5KzyhOqVKMKb",
        )
        """
        _response = self._raw_client.post_upload(
            token=token, file=file, content_range=content_range, video_id=video_id, request_options=request_options
        )
        return _response.data


class AsyncVideosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVideosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVideosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVideosClient
        """
        return self._raw_client

    async def post_videos_video_id_source(
        self,
        video_id: str,
        *,
        file: core.File,
        content_range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Video:
        """
        Ingest a video from a source or file.

        Parameters
        ----------
        video_id : str
            Enter the videoId you want to use to upload your video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            `part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Video
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.videos.post_videos_video_id_source(
                video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
                content_range="bytes 209715200-419430399/524288000 OR part 2/3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_videos_video_id_source(
            video_id, file=file, content_range=content_range, request_options=request_options
        )
        return _response.data

    async def post_upload(
        self,
        *,
        token: str,
        file: core.File,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Video:
        """
        Uploading a video with the delegated upload token.

        Parameters
        ----------
        token : str
            The unique identifier for the token you want to use to upload a video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.

        video_id : typing.Optional[str]
            The video id returned by the first call to this endpoint in a large video upload scenario.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Video
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.videos.post_upload(
                content_range="Content-Range: bytes 200-100/5000",
                token="to1tcmSFHeYY5KzyhOqVKMKb",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_upload(
            token=token, file=file, content_range=content_range, video_id=video_id, request_options=request_options
        )
        return _response.data
