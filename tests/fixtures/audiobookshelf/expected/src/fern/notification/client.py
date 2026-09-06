

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apprise_api_url import AppriseApiUrl
from ..types.body_template import BodyTemplate
from ..types.enabled import Enabled
from ..types.library_id import LibraryId
from ..types.library_id_nullable import LibraryIdNullable
from ..types.max_failed_attempts import MaxFailedAttempts
from ..types.max_notification_queue import MaxNotificationQueue
from ..types.notification_event_name import NotificationEventName
from ..types.notification_id import NotificationId
from ..types.notification_type import NotificationType
from ..types.title_template import TitleTemplate
from ..types.urls import Urls
from .raw_client import AsyncRawNotificationClient, RawNotificationClient
from .types.create_notification_response import CreateNotificationResponse
from .types.delete_notification_response import DeleteNotificationResponse
from .types.get_notification_event_data_response import GetNotificationEventDataResponse
from .types.get_notifications_response import GetNotificationsResponse
from .types.update_notification_response import UpdateNotificationResponse


OMIT = typing.cast(typing.Any, ...)


class NotificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationClient
        """
        return self._raw_client

    def get_notifications(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetNotificationsResponse:
        """
        Get all Apprise notification events and notification settings for server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.get_notifications()
        """
        _response = self._raw_client.get_notifications(request_options=request_options)
        return _response.data

    def create_notification(
        self,
        *,
        event_name: NotificationEventName,
        urls: Urls,
        title_template: TitleTemplate,
        body_template: BodyTemplate,
        library_id: typing.Optional[LibraryIdNullable] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateNotificationResponse:
        """
        Create or update Notification settings.

        Parameters
        ----------
        event_name : NotificationEventName

        urls : Urls

        title_template : TitleTemplate

        body_template : BodyTemplate

        library_id : typing.Optional[LibraryIdNullable]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNotificationResponse
            Success

        Examples
        --------
        from fern import FernApi, NotificationEventName

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.create_notification(
            event_name=NotificationEventName.ON_PODCAST_EPISODE_DOWNLOADED,
            urls=["urls"],
            title_template="New {{podcastTitle}} Episode!",
            body_template="{{episodeTitle}} has been added to {{libraryName}} library.",
        )
        """
        _response = self._raw_client.create_notification(
            event_name=event_name,
            urls=urls,
            title_template=title_template,
            body_template=body_template,
            library_id=library_id,
            enabled=enabled,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def configure_notification_settings(
        self,
        *,
        apprise_api_url: typing.Optional[AppriseApiUrl] = OMIT,
        max_failed_attempts: typing.Optional[MaxFailedAttempts] = OMIT,
        max_notification_queue: typing.Optional[MaxNotificationQueue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Update the URL, max failed attempts, and maximum notifications that can be queued for Apprise.

        Parameters
        ----------
        apprise_api_url : typing.Optional[AppriseApiUrl]

        max_failed_attempts : typing.Optional[MaxFailedAttempts]

        max_notification_queue : typing.Optional[MaxNotificationQueue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.configure_notification_settings()
        """
        _response = self._raw_client.configure_notification_settings(
            apprise_api_url=apprise_api_url,
            max_failed_attempts=max_failed_attempts,
            max_notification_queue=max_notification_queue,
            request_options=request_options,
        )
        return _response.data

    def get_notification_event_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNotificationEventDataResponse:
        """
        Get all Apprise notification event data for the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationEventDataResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.get_notification_event_data()
        """
        _response = self._raw_client.get_notification_event_data(request_options=request_options)
        return _response.data

    def send_default_test_notification(
        self, *, fail: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Send a test notification.

        Parameters
        ----------
        fail : typing.Optional[int]
            Whether to intentionally cause the notification to fail. `0` for false, `1` for true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.send_default_test_notification()
        """
        _response = self._raw_client.send_default_test_notification(fail=fail, request_options=request_options)
        return _response.data

    def delete_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteNotificationResponse:
        """
        Delete the notification by ID and return the notification settings.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNotificationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.delete_notification(
            id="notification-settings",
        )
        """
        _response = self._raw_client.delete_notification(id, request_options=request_options)
        return _response.data

    def update_notification(
        self,
        id: NotificationId,
        *,
        library_id: typing.Optional[LibraryId] = OMIT,
        event_name: typing.Optional[NotificationEventName] = OMIT,
        urls: typing.Optional[Urls] = OMIT,
        title_template: typing.Optional[TitleTemplate] = OMIT,
        body_template: typing.Optional[BodyTemplate] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateNotificationResponse:
        """
        Update an individual Notification by ID

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        library_id : typing.Optional[LibraryId]

        event_name : typing.Optional[NotificationEventName]

        urls : typing.Optional[Urls]

        title_template : typing.Optional[TitleTemplate]

        body_template : typing.Optional[BodyTemplate]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateNotificationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.update_notification(
            id="notification-settings",
        )
        """
        _response = self._raw_client.update_notification(
            id,
            library_id=library_id,
            event_name=event_name,
            urls=urls,
            title_template=title_template,
            body_template=body_template,
            enabled=enabled,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def send_test_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Send a test to the given notification by ID.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notification.send_test_notification(
            id="id",
        )
        """
        _response = self._raw_client.send_test_notification(id, request_options=request_options)
        return _response.data


class AsyncNotificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationClient
        """
        return self._raw_client

    async def get_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNotificationsResponse:
        """
        Get all Apprise notification events and notification settings for server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.get_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notifications(request_options=request_options)
        return _response.data

    async def create_notification(
        self,
        *,
        event_name: NotificationEventName,
        urls: Urls,
        title_template: TitleTemplate,
        body_template: BodyTemplate,
        library_id: typing.Optional[LibraryIdNullable] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateNotificationResponse:
        """
        Create or update Notification settings.

        Parameters
        ----------
        event_name : NotificationEventName

        urls : Urls

        title_template : TitleTemplate

        body_template : BodyTemplate

        library_id : typing.Optional[LibraryIdNullable]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNotificationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, NotificationEventName

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.create_notification(
                event_name=NotificationEventName.ON_PODCAST_EPISODE_DOWNLOADED,
                urls=["urls"],
                title_template="New {{podcastTitle}} Episode!",
                body_template="{{episodeTitle}} has been added to {{libraryName}} library.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification(
            event_name=event_name,
            urls=urls,
            title_template=title_template,
            body_template=body_template,
            library_id=library_id,
            enabled=enabled,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def configure_notification_settings(
        self,
        *,
        apprise_api_url: typing.Optional[AppriseApiUrl] = OMIT,
        max_failed_attempts: typing.Optional[MaxFailedAttempts] = OMIT,
        max_notification_queue: typing.Optional[MaxNotificationQueue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Update the URL, max failed attempts, and maximum notifications that can be queued for Apprise.

        Parameters
        ----------
        apprise_api_url : typing.Optional[AppriseApiUrl]

        max_failed_attempts : typing.Optional[MaxFailedAttempts]

        max_notification_queue : typing.Optional[MaxNotificationQueue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.configure_notification_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.configure_notification_settings(
            apprise_api_url=apprise_api_url,
            max_failed_attempts=max_failed_attempts,
            max_notification_queue=max_notification_queue,
            request_options=request_options,
        )
        return _response.data

    async def get_notification_event_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNotificationEventDataResponse:
        """
        Get all Apprise notification event data for the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationEventDataResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.get_notification_event_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notification_event_data(request_options=request_options)
        return _response.data

    async def send_default_test_notification(
        self, *, fail: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Send a test notification.

        Parameters
        ----------
        fail : typing.Optional[int]
            Whether to intentionally cause the notification to fail. `0` for false, `1` for true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.send_default_test_notification()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_default_test_notification(fail=fail, request_options=request_options)
        return _response.data

    async def delete_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteNotificationResponse:
        """
        Delete the notification by ID and return the notification settings.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNotificationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.delete_notification(
                id="notification-settings",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_notification(id, request_options=request_options)
        return _response.data

    async def update_notification(
        self,
        id: NotificationId,
        *,
        library_id: typing.Optional[LibraryId] = OMIT,
        event_name: typing.Optional[NotificationEventName] = OMIT,
        urls: typing.Optional[Urls] = OMIT,
        title_template: typing.Optional[TitleTemplate] = OMIT,
        body_template: typing.Optional[BodyTemplate] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateNotificationResponse:
        """
        Update an individual Notification by ID

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        library_id : typing.Optional[LibraryId]

        event_name : typing.Optional[NotificationEventName]

        urls : typing.Optional[Urls]

        title_template : typing.Optional[TitleTemplate]

        body_template : typing.Optional[BodyTemplate]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateNotificationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.update_notification(
                id="notification-settings",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_notification(
            id,
            library_id=library_id,
            event_name=event_name,
            urls=urls,
            title_template=title_template,
            body_template=body_template,
            enabled=enabled,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def send_test_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Send a test to the given notification by ID.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Notification endpoint success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notification.send_test_notification(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_test_notification(id, request_options=request_options)
        return _response.data
