

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_preview import NotificationPreview
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

    def get_notifications_contributions_id_preview(
        self, id: str, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationPreview:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to preview a notification for

        message : str
            Type of message to preview.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPreview
            Notification preview

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.get_notifications_contributions_id_preview(
            id="id",
            message="message",
        )
        """
        _response = self._raw_client.get_notifications_contributions_id_preview(
            id, message=message, request_options=request_options
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

    async def get_notifications_contributions_id_preview(
        self, id: str, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationPreview:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to preview a notification for

        message : str
            Type of message to preview.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationPreview
            Notification preview

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.get_notifications_contributions_id_preview(
                id="id",
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notifications_contributions_id_preview(
            id, message=message, request_options=request_options
        )
        return _response.data
