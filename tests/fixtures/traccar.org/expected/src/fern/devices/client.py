

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.device import Device
from ..types.device_attributes import DeviceAttributes
from .raw_client import AsyncRawDevicesClient, RawDevicesClient


OMIT = typing.cast(typing.Any, ...)


class DevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDevicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDevicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDevicesClient
        """
        return self._raw_client

    def fetch_a_list_of_devices(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        unique_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Device]:
        """
        Without any params, returns a list of the user's devices

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        id : typing.Optional[int]
            To fetch one or more devices. Multiple params can be passed like `id=31&id=42`

        unique_id : typing.Optional[str]
            To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Device]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.devices.fetch_a_list_of_devices()
        """
        _response = self._raw_client.fetch_a_list_of_devices(
            all_=all_, user_id=user_id, id=id, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    def create_a_device(
        self,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Device:
        """
        Parameters
        ----------
        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.devices.create_a_device()
        """
        _response = self._raw_client.create_a_device(
            attributes=attributes,
            category=category,
            contact=contact,
            disabled=disabled,
            geofence_ids=geofence_ids,
            group_id=group_id,
            id=id,
            last_update=last_update,
            model=model,
            name=name,
            phone=phone,
            position_id=position_id,
            status=status,
            unique_id=unique_id,
            request_options=request_options,
        )
        return _response.data

    def update_a_device(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Device:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.devices.update_a_device(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_device(
            id_,
            attributes=attributes,
            category=category,
            contact=contact,
            disabled=disabled,
            geofence_ids=geofence_ids,
            group_id=group_id,
            id=id,
            last_update=last_update,
            model=model,
            name=name,
            phone=phone,
            position_id=position_id,
            status=status,
            unique_id=unique_id,
            request_options=request_options,
        )
        return _response.data

    def delete_a_device(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.devices.delete_a_device(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_device(id, request_options=request_options)
        return _response.data

    def update_total_distance_and_hours_of_the_device(
        self,
        id: int,
        *,
        device_id: typing.Optional[int] = OMIT,
        hours: typing.Optional[float] = OMIT,
        total_distance: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        device_id : typing.Optional[int]

        hours : typing.Optional[float]

        total_distance : typing.Optional[float]
            in meters

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
        client.devices.update_total_distance_and_hours_of_the_device(
            id=1,
        )
        """
        _response = self._raw_client.update_total_distance_and_hours_of_the_device(
            id, device_id=device_id, hours=hours, total_distance=total_distance, request_options=request_options
        )
        return _response.data


class AsyncDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDevicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDevicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDevicesClient
        """
        return self._raw_client

    async def fetch_a_list_of_devices(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        unique_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Device]:
        """
        Without any params, returns a list of the user's devices

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        id : typing.Optional[int]
            To fetch one or more devices. Multiple params can be passed like `id=31&id=42`

        unique_id : typing.Optional[str]
            To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Device]
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
            await client.devices.fetch_a_list_of_devices()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_devices(
            all_=all_, user_id=user_id, id=id, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    async def create_a_device(
        self,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Device:
        """
        Parameters
        ----------
        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
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
            await client.devices.create_a_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_device(
            attributes=attributes,
            category=category,
            contact=contact,
            disabled=disabled,
            geofence_ids=geofence_ids,
            group_id=group_id,
            id=id,
            last_update=last_update,
            model=model,
            name=name,
            phone=phone,
            position_id=position_id,
            status=status,
            unique_id=unique_id,
            request_options=request_options,
        )
        return _response.data

    async def update_a_device(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Device:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
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
            await client.devices.update_a_device(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_device(
            id_,
            attributes=attributes,
            category=category,
            contact=contact,
            disabled=disabled,
            geofence_ids=geofence_ids,
            group_id=group_id,
            id=id,
            last_update=last_update,
            model=model,
            name=name,
            phone=phone,
            position_id=position_id,
            status=status,
            unique_id=unique_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_device(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.devices.delete_a_device(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_device(id, request_options=request_options)
        return _response.data

    async def update_total_distance_and_hours_of_the_device(
        self,
        id: int,
        *,
        device_id: typing.Optional[int] = OMIT,
        hours: typing.Optional[float] = OMIT,
        total_distance: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        device_id : typing.Optional[int]

        hours : typing.Optional[float]

        total_distance : typing.Optional[float]
            in meters

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
            await client.devices.update_total_distance_and_hours_of_the_device(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_total_distance_and_hours_of_the_device(
            id, device_id=device_id, hours=hours, total_distance=total_distance, request_options=request_options
        )
        return _response.data
