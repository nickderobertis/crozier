

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_response import NotificationResponse
from ..types.notifications_response import NotificationsResponse
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationsClient
        """
        return self._raw_client

    def get_own_notifications(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationsResponse:
        """
        Get all notifications for the authenticated user

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.get_own_notifications()
        """
        _response = self._raw_client.get_own_notifications(
            limit=limit, offset=offset, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    def get_own_notification_count(
        self, *, unread_only: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Get the count of notifications for the authenticated user

        Parameters
        ----------
        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.get_own_notification_count()
        """
        _response = self._raw_client.get_own_notification_count(
            unread_only=unread_only, request_options=request_options
        )
        return _response.data

    def mark_own_notification_as_read(
        self, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationResponse:
        """
        Mark the authenticated user's own notification as read

        Parameters
        ----------
        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.mark_own_notification_as_read(
            notification_id=1,
        )
        """
        _response = self._raw_client.mark_own_notification_as_read(notification_id, request_options=request_options)
        return _response.data

    def get_notifications(
        self,
        user_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationsResponse:
        """
        Get all notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notifications will be fetched

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.get_notifications(
            user_id=1,
        )
        """
        _response = self._raw_client.get_notifications(
            user_id, limit=limit, offset=offset, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    def get_notification_count(
        self,
        user_id: int,
        *,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notification count will be fetched

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.get_notification_count(
            user_id=1,
        )
        """
        _response = self._raw_client.get_notification_count(
            user_id, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    def mark_notification_as_read(
        self, user_id: int, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationResponse:
        """
        Mark a notification as read

        Parameters
        ----------
        user_id : int
            ID of the user whose notification will be dismissed

        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.notifications.mark_notification_as_read(
            user_id=1,
            notification_id=1,
        )
        """
        _response = self._raw_client.mark_notification_as_read(
            user_id, notification_id, request_options=request_options
        )
        return _response.data


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationsClient
        """
        return self._raw_client

    async def get_own_notifications(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationsResponse:
        """
        Get all notifications for the authenticated user

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.get_own_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_own_notifications(
            limit=limit, offset=offset, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    async def get_own_notification_count(
        self, *, unread_only: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Get the count of notifications for the authenticated user

        Parameters
        ----------
        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.get_own_notification_count()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_own_notification_count(
            unread_only=unread_only, request_options=request_options
        )
        return _response.data

    async def mark_own_notification_as_read(
        self, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationResponse:
        """
        Mark the authenticated user's own notification as read

        Parameters
        ----------
        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.mark_own_notification_as_read(
                notification_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_own_notification_as_read(
            notification_id, request_options=request_options
        )
        return _response.data

    async def get_notifications(
        self,
        user_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationsResponse:
        """
        Get all notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notifications will be fetched

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.get_notifications(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notifications(
            user_id, limit=limit, offset=offset, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    async def get_notification_count(
        self,
        user_id: int,
        *,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notification count will be fetched

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.get_notification_count(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notification_count(
            user_id, unread_only=unread_only, request_options=request_options
        )
        return _response.data

    async def mark_notification_as_read(
        self, user_id: int, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationResponse:
        """
        Mark a notification as read

        Parameters
        ----------
        user_id : int
            ID of the user whose notification will be dismissed

        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notifications.mark_notification_as_read(
                user_id=1,
                notification_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_notification_as_read(
            user_id, notification_id, request_options=request_options
        )
        return _response.data
