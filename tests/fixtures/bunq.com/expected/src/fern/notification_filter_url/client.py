

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_filter_url import NotificationFilterUrl
from ..types.notification_filter_url_create import NotificationFilterUrlCreate
from ..types.notification_filter_url_listing import NotificationFilterUrlListing
from ..types.notification_filter_url_monetary_account_create import NotificationFilterUrlMonetaryAccountCreate
from ..types.notification_filter_url_monetary_account_listing import NotificationFilterUrlMonetaryAccountListing
from .raw_client import AsyncRawNotificationFilterUrlClient, RawNotificationFilterUrlClient


OMIT = typing.cast(typing.Any, ...)


class NotificationFilterUrlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationFilterUrlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationFilterUrlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationFilterUrlClient
        """
        return self._raw_client

    def list_all_notification_filter_url_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterUrlMonetaryAccountListing]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterUrlMonetaryAccountListing]
            Manage the url notification filters for a user.

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
        client.notification_filter_url.list_all_notification_filter_url_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_notification_filter_url_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_notification_filter_url_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterUrlMonetaryAccountCreate:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this monetary account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterUrlMonetaryAccountCreate
            Manage the url notification filters for a user.

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
        client.notification_filter_url.create_notification_filter_url_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.create_notification_filter_url_for_user_monetary_account(
            user_id, monetary_account_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data

    def list_all_notification_filter_url_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterUrlListing]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterUrlListing]
            Manage the url notification filters for a user.

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
        client.notification_filter_url.list_all_notification_filter_url_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_notification_filter_url_for_user(user_id, request_options=request_options)
        return _response.data

    def create_notification_filter_url_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterUrlCreate:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterUrlCreate
            Manage the url notification filters for a user.

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
        client.notification_filter_url.create_notification_filter_url_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.create_notification_filter_url_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data


class AsyncNotificationFilterUrlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationFilterUrlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationFilterUrlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationFilterUrlClient
        """
        return self._raw_client

    async def list_all_notification_filter_url_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterUrlMonetaryAccountListing]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterUrlMonetaryAccountListing]
            Manage the url notification filters for a user.

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
            await client.notification_filter_url.list_all_notification_filter_url_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_notification_filter_url_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_notification_filter_url_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterUrlMonetaryAccountCreate:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this monetary account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterUrlMonetaryAccountCreate
            Manage the url notification filters for a user.

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
            await client.notification_filter_url.create_notification_filter_url_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification_filter_url_for_user_monetary_account(
            user_id, monetary_account_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data

    async def list_all_notification_filter_url_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationFilterUrlListing]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationFilterUrlListing]
            Manage the url notification filters for a user.

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
            await client.notification_filter_url.list_all_notification_filter_url_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_notification_filter_url_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_notification_filter_url_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationFilterUrlCreate:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationFilterUrlCreate
            Manage the url notification filters for a user.

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
            await client.notification_filter_url.create_notification_filter_url_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification_filter_url_for_user(
            user_id, notification_filters=notification_filters, request_options=request_options
        )
        return _response.data
