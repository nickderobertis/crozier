

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTrackClient, RawTrackClient
from .types.track_event_request_identification import TrackEventRequestIdentification
from .types.track_event_request_metadata_value import TrackEventRequestMetadataValue
from .types.track_event_response import TrackEventResponse


OMIT = typing.cast(typing.Any, ...)


class TrackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrackClient
        """
        return self._raw_client

    def event(
        self,
        *,
        identification: TrackEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackEventResponse:
        """
        Endpoint used to track an event for a user or an account.

        Parameters
        ----------
        identification : TrackEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackEventResponse
            Object was created

        Examples
        --------
        from fern.track import TrackEventRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.track.event(
            identification=TrackEventRequestIdentification(),
            name="name",
        )
        """
        _response = self._raw_client.event(
            identification=identification,
            name=name,
            metadata=metadata,
            triggered_at=triggered_at,
            request_options=request_options,
        )
        return _response.data


class AsyncTrackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrackClient
        """
        return self._raw_client

    async def event(
        self,
        *,
        identification: TrackEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackEventResponse:
        """
        Endpoint used to track an event for a user or an account.

        Parameters
        ----------
        identification : TrackEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackEventResponse
            Object was created

        Examples
        --------
        import asyncio

        from fern.track import TrackEventRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.track.event(
                identification=TrackEventRequestIdentification(),
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.event(
            identification=identification,
            name=name,
            metadata=metadata,
            triggered_at=triggered_at,
            request_options=request_options,
        )
        return _response.data
