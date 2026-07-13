

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_filter_push import NotificationFilterPush
from ..types.notification_filter_push_create import NotificationFilterPushCreate
from ..types.notification_filter_push_listing import NotificationFilterPushListing
from .raw_client import AsyncRawNotificationFilterPushClient, RawNotificationFilterPushClient


OMIT = typing.cast(typing.Any, ...)


class NotificationFilterPushClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationFilterPushClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationFilterPushClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationFilterPushClient
        """
        return self._raw_client

    def list_all_notification_filter_push_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterPushListing]:
        """
        Manage the push notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterPushListing]
            Manage the push notification filters for a user.

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
        client.notification_filter_push.list_all_notification_filter_push_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_notification_filter_push_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def create_notification_filter_push_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterPush]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterPushCreate:
        """
        Manage the push notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterPush]]
            The types of notifications that will result in a push notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterPushCreate
            Manage the push notification filters for a user.

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
        client.notification_filter_push.create_notification_filter_push_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.create_notification_filter_push_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data


class AsyncNotificationFilterPushClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationFilterPushClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationFilterPushClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationFilterPushClient
        """
        return self._raw_client

    async def list_all_notification_filter_push_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterPushListing]:
        """
        Manage the push notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterPushListing]
            Manage the push notification filters for a user.

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
            await client.notification_filter_push.list_all_notification_filter_push_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_notification_filter_push_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_notification_filter_push_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterPush]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterPushCreate:
        """
        Manage the push notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterPush]]
            The types of notifications that will result in a push notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterPushCreate
            Manage the push notification filters for a user.

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
            await client.notification_filter_push.create_notification_filter_push_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification_filter_push_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data
