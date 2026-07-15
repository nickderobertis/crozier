

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_d_id import AppDId
from ..types.app_pkg_id import AppPkgId
from ..types.app_pkg_notification_id import AppPkgNotificationId
from ..types.app_pkg_notification_links import AppPkgNotificationLinks
from ..types.app_pkg_notification_type import AppPkgNotificationType
from ..types.subscription_id import SubscriptionId
from ..types.time_stamp import TimeStamp
from .raw_client import AsyncRawAppPkgmNotificationsClient, RawAppPkgmNotificationsClient
from .types.app_pkg_notification_operational_state import AppPkgNotificationOperationalState


OMIT = typing.cast(typing.Any, ...)


class AppPkgmNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppPkgmNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppPkgmNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppPkgmNotificationsClient
        """
        return self._raw_client

    def app_pkg_notification_post(
        self,
        *,
        links: AppPkgNotificationLinks,
        app_d_id: AppDId,
        app_pkg_id: AppPkgId,
        id: AppPkgNotificationId,
        notification_type: AppPkgNotificationType,
        operational_state: AppPkgNotificationOperationalState,
        subscription_id: SubscriptionId,
        time_stamp: TimeStamp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Registers a notification endpoint to notify application package operations

        Parameters
        ----------
        links : AppPkgNotificationLinks

        app_d_id : AppDId

        app_pkg_id : AppPkgId

        id : AppPkgNotificationId

        notification_type : AppPkgNotificationType

        operational_state : AppPkgNotificationOperationalState

        subscription_id : SubscriptionId

        time_stamp : TimeStamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.app_pkgm_notifications import AppPkgNotificationOperationalState

        from fern import (
            AppPkgNotificationLinks,
            AppPkgNotificationType,
            FernApi,
            LinkType,
            TimeStamp,
        )

        client = FernApi()
        client.app_pkgm_notifications.app_pkg_notification_post(
            links=AppPkgNotificationLinks(
                subscription=LinkType(
                    href="href",
                ),
            ),
            app_d_id="appDId",
            app_pkg_id="appPkgId",
            id="id",
            notification_type=AppPkgNotificationType.APP_PACKAGE_ON_BOARDED,
            operational_state=AppPkgNotificationOperationalState.DISABLED,
            subscription_id="subscriptionId",
            time_stamp=TimeStamp(
                nano_seconds=1,
                seconds=1,
            ),
        )
        """
        _response = self._raw_client.app_pkg_notification_post(
            links=links,
            app_d_id=app_d_id,
            app_pkg_id=app_pkg_id,
            id=id,
            notification_type=notification_type,
            operational_state=operational_state,
            subscription_id=subscription_id,
            time_stamp=time_stamp,
            request_options=request_options,
        )
        return _response.data


class AsyncAppPkgmNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppPkgmNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppPkgmNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppPkgmNotificationsClient
        """
        return self._raw_client

    async def app_pkg_notification_post(
        self,
        *,
        links: AppPkgNotificationLinks,
        app_d_id: AppDId,
        app_pkg_id: AppPkgId,
        id: AppPkgNotificationId,
        notification_type: AppPkgNotificationType,
        operational_state: AppPkgNotificationOperationalState,
        subscription_id: SubscriptionId,
        time_stamp: TimeStamp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Registers a notification endpoint to notify application package operations

        Parameters
        ----------
        links : AppPkgNotificationLinks

        app_d_id : AppDId

        app_pkg_id : AppPkgId

        id : AppPkgNotificationId

        notification_type : AppPkgNotificationType

        operational_state : AppPkgNotificationOperationalState

        subscription_id : SubscriptionId

        time_stamp : TimeStamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.app_pkgm_notifications import AppPkgNotificationOperationalState

        from fern import (
            AppPkgNotificationLinks,
            AppPkgNotificationType,
            AsyncFernApi,
            LinkType,
            TimeStamp,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm_notifications.app_pkg_notification_post(
                links=AppPkgNotificationLinks(
                    subscription=LinkType(
                        href="href",
                    ),
                ),
                app_d_id="appDId",
                app_pkg_id="appPkgId",
                id="id",
                notification_type=AppPkgNotificationType.APP_PACKAGE_ON_BOARDED,
                operational_state=AppPkgNotificationOperationalState.DISABLED,
                subscription_id="subscriptionId",
                time_stamp=TimeStamp(
                    nano_seconds=1,
                    seconds=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_pkg_notification_post(
            links=links,
            app_d_id=app_d_id,
            app_pkg_id=app_pkg_id,
            id=id,
            notification_type=notification_type,
            operational_state=operational_state,
            subscription_id=subscription_id,
            time_stamp=time_stamp,
            request_options=request_options,
        )
        return _response.data
