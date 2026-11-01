

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.caption_media_request_speed import CaptionMediaRequestSpeed
from .raw_client import AsyncRawMediaClient, RawMediaClient
from .types.caption_media_request_dialect import CaptionMediaRequestDialect
from .types.caption_media_response import CaptionMediaResponse


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

    def caption_url(
        self,
        *,
        url: str,
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaptionMediaResponse:
        """
        Parameters
        ----------
        url : str

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaptionMediaResponse
            The captions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.captions.media.caption_url(
            url="url",
        )
        """
        _response = self._raw_client.caption_url(url=url, dialect=dialect, speed=speed, request_options=request_options)
        return _response.data

    def caption_file(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaptionMediaResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaptionMediaResponse
            The captions
        """
        _response = self._raw_client.caption_file(
            request=request, dialect=dialect, speed=speed, request_options=request_options
        )
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

    async def caption_url(
        self,
        *,
        url: str,
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaptionMediaResponse:
        """
        Parameters
        ----------
        url : str

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaptionMediaResponse
            The captions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.captions.media.caption_url(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.caption_url(
            url=url, dialect=dialect, speed=speed, request_options=request_options
        )
        return _response.data

    async def caption_file(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaptionMediaResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaptionMediaResponse
            The captions
        """
        _response = await self._raw_client.caption_file(
            request=request, dialect=dialect, speed=speed, request_options=request_options
        )
        return _response.data
