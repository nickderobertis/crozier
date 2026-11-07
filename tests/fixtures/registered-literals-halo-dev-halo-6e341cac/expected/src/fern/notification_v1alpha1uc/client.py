

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification import Notification
from ..types.notification_list import NotificationList
from ..types.reason_type_notifier_matrix import ReasonTypeNotifierMatrix
from ..types.reason_type_notifier_request import ReasonTypeNotifierRequest
from .raw_client import AsyncRawNotificationV1Alpha1UcClient, RawNotificationV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class NotificationV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationV1Alpha1UcClient
        """
        return self._raw_client

    def list_user_notification_preferences(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReasonTypeNotifierMatrix:
        """
        List notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReasonTypeNotifierMatrix
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.list_user_notification_preferences(
            username="username",
        )
        """
        _response = self._raw_client.list_user_notification_preferences(username, request_options=request_options)
        return _response.data

    def save_user_notification_preferences(
        self,
        username: str,
        *,
        reason_type_notifiers: typing.Sequence[ReasonTypeNotifierRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReasonTypeNotifierMatrix:
        """
        Save notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        reason_type_notifiers : typing.Sequence[ReasonTypeNotifierRequest]
            notifier selections grouped by reason type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReasonTypeNotifierMatrix
            default response

        Examples
        --------
        from fern import FernApi, ReasonTypeNotifierRequest

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.save_user_notification_preferences(
            username="username",
            reason_type_notifiers=[
                ReasonTypeNotifierRequest(
                    notifiers=["notifiers"],
                    reason_type="reasonType",
                )
            ],
        )
        """
        _response = self._raw_client.save_user_notification_preferences(
            username, reason_type_notifiers=reason_type_notifiers, request_options=request_options
        )
        return _response.data

    def list_user_notifications(
        self,
        username: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationList:
        """
        List notifications for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.list_user_notifications(
            username="username",
        )
        """
        _response = self._raw_client.list_user_notifications(
            username,
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def mark_notifications_as_read(
        self, username: str, *, names: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Mark the specified notifications as read.

        Parameters
        ----------
        username : str
            User metadata.name

        names : typing.Sequence[str]
            notification <code>metadata.name</code> values to mark as read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.mark_notifications_as_read(
            username="username",
            names=["names"],
        )
        """
        _response = self._raw_client.mark_notifications_as_read(username, names=names, request_options=request_options)
        return _response.data

    def delete_specified_notification(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Notification:
        """
        Delete the specified notification.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.delete_specified_notification(
            username="username",
            name="name",
        )
        """
        _response = self._raw_client.delete_specified_notification(username, name, request_options=request_options)
        return _response.data

    def mark_notification_as_read(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Notification:
        """
        Mark the specified notification as read.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notification_v1alpha1uc.mark_notification_as_read(
            username="username",
            name="name",
        )
        """
        _response = self._raw_client.mark_notification_as_read(username, name, request_options=request_options)
        return _response.data


class AsyncNotificationV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationV1Alpha1UcClient
        """
        return self._raw_client

    async def list_user_notification_preferences(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReasonTypeNotifierMatrix:
        """
        List notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReasonTypeNotifierMatrix
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.list_user_notification_preferences(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_notification_preferences(username, request_options=request_options)
        return _response.data

    async def save_user_notification_preferences(
        self,
        username: str,
        *,
        reason_type_notifiers: typing.Sequence[ReasonTypeNotifierRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReasonTypeNotifierMatrix:
        """
        Save notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        reason_type_notifiers : typing.Sequence[ReasonTypeNotifierRequest]
            notifier selections grouped by reason type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReasonTypeNotifierMatrix
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ReasonTypeNotifierRequest

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.save_user_notification_preferences(
                username="username",
                reason_type_notifiers=[
                    ReasonTypeNotifierRequest(
                        notifiers=["notifiers"],
                        reason_type="reasonType",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_user_notification_preferences(
            username, reason_type_notifiers=reason_type_notifiers, request_options=request_options
        )
        return _response.data

    async def list_user_notifications(
        self,
        username: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationList:
        """
        List notifications for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationList
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.list_user_notifications(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_notifications(
            username,
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    async def mark_notifications_as_read(
        self, username: str, *, names: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Mark the specified notifications as read.

        Parameters
        ----------
        username : str
            User metadata.name

        names : typing.Sequence[str]
            notification <code>metadata.name</code> values to mark as read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.mark_notifications_as_read(
                username="username",
                names=["names"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_notifications_as_read(
            username, names=names, request_options=request_options
        )
        return _response.data

    async def delete_specified_notification(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Notification:
        """
        Delete the specified notification.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.delete_specified_notification(
                username="username",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_specified_notification(
            username, name, request_options=request_options
        )
        return _response.data

    async def mark_notification_as_read(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Notification:
        """
        Mark the specified notification as read.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notification_v1alpha1uc.mark_notification_as_read(
                username="username",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_notification_as_read(username, name, request_options=request_options)
        return _response.data
