

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEventsClient, RawEventsClient
from .types.get_events_response import GetEventsResponse
from .types.track_journey_event_request_identification import TrackJourneyEventRequestIdentification
from .types.track_journey_event_request_metadata_value import TrackJourneyEventRequestMetadataValue
from .types.track_journey_event_response import TrackJourneyEventResponse


OMIT = typing.cast(typing.Any, ...)


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def get_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetEventsResponse:
        """
        Endpoint to list events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
            Events

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.get_events()
        """
        _response = self._raw_client.get_events(request_options=request_options)
        return _response.data

    def track_journey_event(
        self,
        *,
        identification: TrackJourneyEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackJourneyEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackJourneyEventResponse:
        """
        Endpoint used to track an event for a user or an account.

        This endpoint is moved to [Track](#operation/trackEvent).

        Parameters
        ----------
        identification : TrackJourneyEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackJourneyEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackJourneyEventResponse
            Object was created

        Examples
        --------
        from fern.events import TrackJourneyEventRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.events.track_journey_event(
            identification=TrackJourneyEventRequestIdentification(),
            name="name",
        )
        """
        _response = self._raw_client.track_journey_event(
            identification=identification,
            name=name,
            metadata=metadata,
            triggered_at=triggered_at,
            request_options=request_options,
        )
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def get_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetEventsResponse:
        """
        Endpoint to list events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
            Events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.get_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events(request_options=request_options)
        return _response.data

    async def track_journey_event(
        self,
        *,
        identification: TrackJourneyEventRequestIdentification,
        name: str,
        metadata: typing.Optional[typing.Dict[str, TrackJourneyEventRequestMetadataValue]] = OMIT,
        triggered_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackJourneyEventResponse:
        """
        Endpoint used to track an event for a user or an account.

        This endpoint is moved to [Track](#operation/trackEvent).

        Parameters
        ----------
        identification : TrackJourneyEventRequestIdentification
            Event identification requires a user, account or both

        name : str

        metadata : typing.Optional[typing.Dict[str, TrackJourneyEventRequestMetadataValue]]
            Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        triggered_at : typing.Optional[str]
            If left blank this defaults to the current datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackJourneyEventResponse
            Object was created

        Examples
        --------
        import asyncio

        from fern.events import TrackJourneyEventRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.track_journey_event(
                identification=TrackJourneyEventRequestIdentification(),
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.track_journey_event(
            identification=identification,
            name=name,
            metadata=metadata,
            triggered_at=triggered_at,
            request_options=request_options,
        )
        return _response.data
