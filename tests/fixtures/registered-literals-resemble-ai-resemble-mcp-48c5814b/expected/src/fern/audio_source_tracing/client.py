

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioSourceTracingClient, RawAudioSourceTracingClient
from .types.get_audio_source_tracing_response import GetAudioSourceTracingResponse
from .types.list_audio_source_tracings_response import ListAudioSourceTracingsResponse


class AudioSourceTracingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioSourceTracingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioSourceTracingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioSourceTracingClient
        """
        return self._raw_client

    def list_audio_source_tracings(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAudioSourceTracingsResponse:
        """
        Retrieve a paginated list of all source tracing reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioSourceTracingsResponse
            List of source tracing reports

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_source_tracing.list_audio_source_tracings(
            page=1,
        )
        """
        _response = self._raw_client.list_audio_source_tracings(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_audio_source_tracing(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioSourceTracingResponse:
        """
        Retrieve a single source tracing report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the source tracing report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioSourceTracingResponse
            Source tracing report

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_source_tracing.get_audio_source_tracing(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_audio_source_tracing(uuid_, request_options=request_options)
        return _response.data


class AsyncAudioSourceTracingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioSourceTracingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioSourceTracingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioSourceTracingClient
        """
        return self._raw_client

    async def list_audio_source_tracings(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAudioSourceTracingsResponse:
        """
        Retrieve a paginated list of all source tracing reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioSourceTracingsResponse
            List of source tracing reports

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_source_tracing.list_audio_source_tracings(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_audio_source_tracings(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_audio_source_tracing(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioSourceTracingResponse:
        """
        Retrieve a single source tracing report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the source tracing report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioSourceTracingResponse
            Source tracing report

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_source_tracing.get_audio_source_tracing(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_source_tracing(uuid_, request_options=request_options)
        return _response.data
