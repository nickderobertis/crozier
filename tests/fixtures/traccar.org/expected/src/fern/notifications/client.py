

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification import Notification
from ..types.notification_attributes import NotificationAttributes
from ..types.notification_type import NotificationType
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

    def fetch_a_list_of_notifications(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Notification]:
        """
        Without params, it returns a list of Notifications the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Notification]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.fetch_a_list_of_notifications()
        """
        _response = self._raw_client.fetch_a_list_of_notifications(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_a_notification(
        self,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Notification:
        """
        Parameters
        ----------
        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.create_a_notification()
        """
        _response = self._raw_client.create_a_notification(
            always=always,
            attributes=attributes,
            calendar_id=calendar_id,
            id=id,
            mail=mail,
            sms=sms,
            type=type,
            web=web,
            request_options=request_options,
        )
        return _response.data

    def send_test_notification_to_current_user_via_email_and_sms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.send_test_notification_to_current_user_via_email_and_sms()
        """
        _response = self._raw_client.send_test_notification_to_current_user_via_email_and_sms(
            request_options=request_options
        )
        return _response.data

    def fetch_a_list_of_available_notification_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationType]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationType]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.fetch_a_list_of_available_notification_types()
        """
        _response = self._raw_client.fetch_a_list_of_available_notification_types(request_options=request_options)
        return _response.data

    def update_a_notification(
        self,
        id_: int,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Notification:
        """
        Parameters
        ----------
        id_ : int

        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.update_a_notification(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_notification(
            id_,
            always=always,
            attributes=attributes,
            calendar_id=calendar_id,
            id=id,
            mail=mail,
            sms=sms,
            type=type,
            web=web,
            request_options=request_options,
        )
        return _response.data

    def delete_a_notification(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifications.delete_a_notification(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_notification(id, request_options=request_options)
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

    async def fetch_a_list_of_notifications(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Notification]:
        """
        Without params, it returns a list of Notifications the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Notification]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.fetch_a_list_of_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_notifications(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_a_notification(
        self,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Notification:
        """
        Parameters
        ----------
        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.create_a_notification()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_notification(
            always=always,
            attributes=attributes,
            calendar_id=calendar_id,
            id=id,
            mail=mail,
            sms=sms,
            type=type,
            web=web,
            request_options=request_options,
        )
        return _response.data

    async def send_test_notification_to_current_user_via_email_and_sms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.send_test_notification_to_current_user_via_email_and_sms()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_test_notification_to_current_user_via_email_and_sms(
            request_options=request_options
        )
        return _response.data

    async def fetch_a_list_of_available_notification_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationType]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationType]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.fetch_a_list_of_available_notification_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_available_notification_types(request_options=request_options)
        return _response.data

    async def update_a_notification(
        self,
        id_: int,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Notification:
        """
        Parameters
        ----------
        id_ : int

        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notification
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.update_a_notification(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_notification(
            id_,
            always=always,
            attributes=attributes,
            calendar_id=calendar_id,
            id=id,
            mail=mail,
            sms=sms,
            type=type,
            web=web,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_notification(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifications.delete_a_notification(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_notification(id, request_options=request_options)
        return _response.data
