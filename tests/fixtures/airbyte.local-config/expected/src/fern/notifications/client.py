

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customerio_notification_configuration import CustomerioNotificationConfiguration
from ..types.notification_read import NotificationRead
from ..types.notification_type import NotificationType
from ..types.slack_notification_configuration import SlackNotificationConfiguration
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient


OMIT = typing.cast(typing.Any, ...)


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

    def try_notification_config(
        self,
        *,
        notification_type: NotificationType,
        send_on_failure: bool,
        send_on_success: bool,
        customerio_configuration: typing.Optional[CustomerioNotificationConfiguration] = OMIT,
        slack_configuration: typing.Optional[SlackNotificationConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationRead:
        """
        Parameters
        ----------
        notification_type : NotificationType

        send_on_failure : bool

        send_on_success : bool

        customerio_configuration : typing.Optional[CustomerioNotificationConfiguration]

        slack_configuration : typing.Optional[SlackNotificationConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationRead
            Successful operation

        Examples
        --------
        from fern import FernApi, NotificationType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.notifications.try_notification_config(
            notification_type=NotificationType.SLACK,
            send_on_failure=True,
            send_on_success=True,
        )
        """
        _response = self._raw_client.try_notification_config(
            notification_type=notification_type,
            send_on_failure=send_on_failure,
            send_on_success=send_on_success,
            customerio_configuration=customerio_configuration,
            slack_configuration=slack_configuration,
            request_options=request_options,
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

    async def try_notification_config(
        self,
        *,
        notification_type: NotificationType,
        send_on_failure: bool,
        send_on_success: bool,
        customerio_configuration: typing.Optional[CustomerioNotificationConfiguration] = OMIT,
        slack_configuration: typing.Optional[SlackNotificationConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationRead:
        """
        Parameters
        ----------
        notification_type : NotificationType

        send_on_failure : bool

        send_on_success : bool

        customerio_configuration : typing.Optional[CustomerioNotificationConfiguration]

        slack_configuration : typing.Optional[SlackNotificationConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, NotificationType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.notifications.try_notification_config(
                notification_type=NotificationType.SLACK,
                send_on_failure=True,
                send_on_success=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.try_notification_config(
            notification_type=notification_type,
            send_on_failure=send_on_failure,
            send_on_success=send_on_success,
            customerio_configuration=customerio_configuration,
            slack_configuration=slack_configuration,
            request_options=request_options,
        )
        return _response.data
