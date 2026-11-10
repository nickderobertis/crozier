

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_dto import NotificationDto
from ..types.progress_dto import ProgressDto
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

    def notifications_api_get_all_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns all notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns notifications and count.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.notifications_api_get_all_notifications()
        """
        _response = self._raw_client.notifications_api_get_all_notifications(request_options=request_options)
        return _response.data

    def notifications_api_get_new_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns new notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns new notifications.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.notifications_api_get_new_notifications()
        """
        _response = self._raw_client.notifications_api_get_new_notifications(request_options=request_options)
        return _response.data

    def notifications_api_get_progresses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProgressDto]:
        """
        Returns progresses.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProgressDto]
            Successful operation. Returns progresses.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.notifications_api_get_progresses()
        """
        _response = self._raw_client.notifications_api_get_progresses(request_options=request_options)
        return _response.data

    def notifications_api_read_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns new notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns notifications.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.notifications_api_read_all()
        """
        _response = self._raw_client.notifications_api_read_all(request_options=request_options)
        return _response.data

    def notifications_api_delete(
        self, notification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Returns deleted notifications count.

        Parameters
        ----------
        notification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful operation. Returns deleted notifications count.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.notifications_api_delete(
            notification_id="notificationId",
        )
        """
        _response = self._raw_client.notifications_api_delete(notification_id, request_options=request_options)
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

    async def notifications_api_get_all_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns all notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns notifications and count.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.notifications_api_get_all_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.notifications_api_get_all_notifications(request_options=request_options)
        return _response.data

    async def notifications_api_get_new_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns new notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns new notifications.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.notifications_api_get_new_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.notifications_api_get_new_notifications(request_options=request_options)
        return _response.data

    async def notifications_api_get_progresses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProgressDto]:
        """
        Returns progresses.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProgressDto]
            Successful operation. Returns progresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.notifications_api_get_progresses()


        asyncio.run(main())
        """
        _response = await self._raw_client.notifications_api_get_progresses(request_options=request_options)
        return _response.data

    async def notifications_api_read_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationDto]:
        """
        Returns new notifications.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationDto]
            Successful operation. Returns notifications.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.notifications_api_read_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.notifications_api_read_all(request_options=request_options)
        return _response.data

    async def notifications_api_delete(
        self, notification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Returns deleted notifications count.

        Parameters
        ----------
        notification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful operation. Returns deleted notifications count.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.notifications_api_delete(
                notification_id="notificationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.notifications_api_delete(notification_id, request_options=request_options)
        return _response.data
