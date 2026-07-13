

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_listing import EventListing
from ..types.event_read import EventRead
from .raw_client import AsyncRawEventClient, RawEventClient


class EventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventClient
        """
        return self._raw_client

    def list_all_event_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EventListing]:
        """
        Get a collection of events for a given user. You can add query the parameters monetary_account_id, status and/or display_user_event to filter the response. When monetary_account_id={id,id} is provided only events that relate to these monetary account ids are returned. When status={AWAITING_REPLY/FINALIZED} is provided the response only contains events with the status AWAITING_REPLY or FINALIZED. When display_user_event={true/false} is set to false user events are excluded from the response, when not provided user events are displayed. User events are events that are not related to a monetary account (for example: connect invites).

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventListing]
            Used to view events. Events are automatically created and contain information about everything that happens to your bunq account. In the bunq app events are shown in your 'overview'. Examples of when events are created or modified: payment sent, payment received, request for payment received or connect invite received.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.event.list_all_event_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_event_for_user(user_id, request_options=request_options)
        return _response.data

    def read_event_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventRead:
        """
        Get a specific event for a given user.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRead
            Used to view events. Events are automatically created and contain information about everything that happens to your bunq account. In the bunq app events are shown in your 'overview'. Examples of when events are created or modified: payment sent, payment received, request for payment received or connect invite received.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.event.read_event_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_event_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventClient
        """
        return self._raw_client

    async def list_all_event_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EventListing]:
        """
        Get a collection of events for a given user. You can add query the parameters monetary_account_id, status and/or display_user_event to filter the response. When monetary_account_id={id,id} is provided only events that relate to these monetary account ids are returned. When status={AWAITING_REPLY/FINALIZED} is provided the response only contains events with the status AWAITING_REPLY or FINALIZED. When display_user_event={true/false} is set to false user events are excluded from the response, when not provided user events are displayed. User events are events that are not related to a monetary account (for example: connect invites).

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventListing]
            Used to view events. Events are automatically created and contain information about everything that happens to your bunq account. In the bunq app events are shown in your 'overview'. Examples of when events are created or modified: payment sent, payment received, request for payment received or connect invite received.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.event.list_all_event_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_event_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_event_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventRead:
        """
        Get a specific event for a given user.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRead
            Used to view events. Events are automatically created and contain information about everything that happens to your bunq account. In the bunq app events are shown in your 'overview'. Examples of when events are created or modified: payment sent, payment received, request for payment received or connect invite received.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.event.read_event_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_event_for_user(user_id, item_id, request_options=request_options)
        return _response.data
