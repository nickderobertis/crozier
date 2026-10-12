

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.caption_format import CaptionFormat
from ..types.margins import Margins
from .raw_client import AsyncRawTranscriptsClient, RawTranscriptsClient


OMIT = typing.cast(typing.Any, ...)


class TranscriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranscriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranscriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranscriptsClient
        """
        return self._raw_client

    def create_transcript(
        self,
        *,
        audio: typing.Optional[core.File] = OMIT,
        format: typing.Optional[CaptionFormat] = OMIT,
        margins: typing.Optional[Margins] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        audio : typing.Optional[core.File]
            See core.File for more documentation

        format : typing.Optional[CaptionFormat]

        margins : typing.Optional[Margins]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.transcripts.create_transcript()
        """
        _response = self._raw_client.create_transcript(
            audio=audio, format=format, margins=margins, request_options=request_options
        )
        return _response.data


class AsyncTranscriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranscriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranscriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranscriptsClient
        """
        return self._raw_client

    async def create_transcript(
        self,
        *,
        audio: typing.Optional[core.File] = OMIT,
        format: typing.Optional[CaptionFormat] = OMIT,
        margins: typing.Optional[Margins] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        audio : typing.Optional[core.File]
            See core.File for more documentation

        format : typing.Optional[CaptionFormat]

        margins : typing.Optional[Margins]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.transcripts.create_transcript()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transcript(
            audio=audio, format=format, margins=margins, request_options=request_options
        )
        return _response.data
