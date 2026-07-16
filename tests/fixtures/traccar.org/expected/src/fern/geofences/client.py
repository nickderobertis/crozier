

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.geofence import Geofence
from ..types.geofence_attributes import GeofenceAttributes
from .raw_client import AsyncRawGeofencesClient, RawGeofencesClient


OMIT = typing.cast(typing.Any, ...)


class GeofencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGeofencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGeofencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGeofencesClient
        """
        return self._raw_client

    def fetch_a_list_of_geofences(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Geofence]:
        """
        Without params, it returns a list of Geofences the user has access to

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
        typing.List[Geofence]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.geofences.fetch_a_list_of_geofences()
        """
        _response = self._raw_client.fetch_a_list_of_geofences(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_a_geofence(
        self,
        *,
        area: typing.Optional[str] = OMIT,
        attributes: typing.Optional[GeofenceAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Geofence:
        """
        Parameters
        ----------
        area : typing.Optional[str]

        attributes : typing.Optional[GeofenceAttributes]

        calendar_id : typing.Optional[int]

        description : typing.Optional[str]

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Geofence
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.geofences.create_a_geofence()
        """
        _response = self._raw_client.create_a_geofence(
            area=area,
            attributes=attributes,
            calendar_id=calendar_id,
            description=description,
            id=id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def update_a_geofence(
        self,
        id_: int,
        *,
        area: typing.Optional[str] = OMIT,
        attributes: typing.Optional[GeofenceAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Geofence:
        """
        Parameters
        ----------
        id_ : int

        area : typing.Optional[str]

        attributes : typing.Optional[GeofenceAttributes]

        calendar_id : typing.Optional[int]

        description : typing.Optional[str]

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Geofence
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.geofences.update_a_geofence(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_geofence(
            id_,
            area=area,
            attributes=attributes,
            calendar_id=calendar_id,
            description=description,
            id=id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def delete_a_geofence(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.geofences.delete_a_geofence(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_geofence(id, request_options=request_options)
        return _response.data


class AsyncGeofencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGeofencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGeofencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGeofencesClient
        """
        return self._raw_client

    async def fetch_a_list_of_geofences(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Geofence]:
        """
        Without params, it returns a list of Geofences the user has access to

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
        typing.List[Geofence]
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
            await client.geofences.fetch_a_list_of_geofences()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_geofences(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_a_geofence(
        self,
        *,
        area: typing.Optional[str] = OMIT,
        attributes: typing.Optional[GeofenceAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Geofence:
        """
        Parameters
        ----------
        area : typing.Optional[str]

        attributes : typing.Optional[GeofenceAttributes]

        calendar_id : typing.Optional[int]

        description : typing.Optional[str]

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Geofence
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
            await client.geofences.create_a_geofence()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_geofence(
            area=area,
            attributes=attributes,
            calendar_id=calendar_id,
            description=description,
            id=id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def update_a_geofence(
        self,
        id_: int,
        *,
        area: typing.Optional[str] = OMIT,
        attributes: typing.Optional[GeofenceAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Geofence:
        """
        Parameters
        ----------
        id_ : int

        area : typing.Optional[str]

        attributes : typing.Optional[GeofenceAttributes]

        calendar_id : typing.Optional[int]

        description : typing.Optional[str]

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Geofence
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
            await client.geofences.update_a_geofence(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_geofence(
            id_,
            area=area,
            attributes=attributes,
            calendar_id=calendar_id,
            description=description,
            id=id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_geofence(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.geofences.delete_a_geofence(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_geofence(id, request_options=request_options)
        return _response.data
