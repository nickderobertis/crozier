

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_filter_email import NotificationFilterEmail
from ..types.notification_filter_email_create import NotificationFilterEmailCreate
from ..types.notification_filter_email_listing import NotificationFilterEmailListing
from .raw_client import AsyncRawNotificationFilterEmailClient, RawNotificationFilterEmailClient


OMIT = typing.cast(typing.Any, ...)


class NotificationFilterEmailClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationFilterEmailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationFilterEmailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationFilterEmailClient
        """
        return self._raw_client

    def list_all_notification_filter_email_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterEmailListing]:
        """
        Manage the email notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterEmailListing]
            Manage the email notification filters for a user.

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
        client.notification_filter_email.list_all_notification_filter_email_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_notification_filter_email_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def create_notification_filter_email_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterEmail]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterEmailCreate:
        """
        Manage the email notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterEmail]]
            The types of notifications that will result in a email notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterEmailCreate
            Manage the email notification filters for a user.

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
        client.notification_filter_email.create_notification_filter_email_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.create_notification_filter_email_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data


class AsyncNotificationFilterEmailClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationFilterEmailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationFilterEmailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationFilterEmailClient
        """
        return self._raw_client

    async def list_all_notification_filter_email_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterEmailListing]:
        """
        Manage the email notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterEmailListing]
            Manage the email notification filters for a user.

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
            await client.notification_filter_email.list_all_notification_filter_email_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_notification_filter_email_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_notification_filter_email_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterEmail]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterEmailCreate:
        """
        Manage the email notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterEmail]]
            The types of notifications that will result in a email notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterEmailCreate
            Manage the email notification filters for a user.

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
            await client.notification_filter_email.create_notification_filter_email_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification_filter_email_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data
