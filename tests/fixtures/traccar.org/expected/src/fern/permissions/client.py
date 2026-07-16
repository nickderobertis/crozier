

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.permission import Permission
from .raw_client import AsyncRawPermissionsClient, RawPermissionsClient


OMIT = typing.cast(typing.Any, ...)


class PermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermissionsClient
        """
        return self._raw_client

    def link_an_object_to_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Permission:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Permission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.permissions.link_an_object_to_another_object()
        """
        _response = self._raw_client.link_an_object_to_another_object(
            attribute_id=attribute_id,
            calendar_id=calendar_id,
            device_id=device_id,
            driver_id=driver_id,
            geofence_id=geofence_id,
            group_id=group_id,
            managed_user_id=managed_user_id,
            notification_id=notification_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def unlink_an_object_from_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

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
        client.permissions.unlink_an_object_from_another_object()
        """
        _response = self._raw_client.unlink_an_object_from_another_object(
            attribute_id=attribute_id,
            calendar_id=calendar_id,
            device_id=device_id,
            driver_id=driver_id,
            geofence_id=geofence_id,
            group_id=group_id,
            managed_user_id=managed_user_id,
            notification_id=notification_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data


class AsyncPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermissionsClient
        """
        return self._raw_client

    async def link_an_object_to_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Permission:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Permission
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
            await client.permissions.link_an_object_to_another_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.link_an_object_to_another_object(
            attribute_id=attribute_id,
            calendar_id=calendar_id,
            device_id=device_id,
            driver_id=driver_id,
            geofence_id=geofence_id,
            group_id=group_id,
            managed_user_id=managed_user_id,
            notification_id=notification_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def unlink_an_object_from_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

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
            await client.permissions.unlink_an_object_from_another_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.unlink_an_object_from_another_object(
            attribute_id=attribute_id,
            calendar_id=calendar_id,
            device_id=device_id,
            driver_id=driver_id,
            geofence_id=geofence_id,
            group_id=group_id,
            managed_user_id=managed_user_id,
            notification_id=notification_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data
