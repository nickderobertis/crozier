

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.maintenance import Maintenance
from ..types.maintenance_attributes import MaintenanceAttributes
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient


OMIT = typing.cast(typing.Any, ...)


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    def fetch_a_list_of_maintenance(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Maintenance]:
        """
        Without params, it returns a list of Maintenance the user has access to

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
        typing.List[Maintenance]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.fetch_a_list_of_maintenance()
        """
        _response = self._raw_client.fetch_a_list_of_maintenance(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_a_maintenance(
        self,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Parameters
        ----------
        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.create_a_maintenance()
        """
        _response = self._raw_client.create_a_maintenance(
            attributes=attributes,
            id=id,
            name=name,
            period=period,
            start=start,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def update_a_maintenance(
        self,
        id_: int,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.update_a_maintenance(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_maintenance(
            id_,
            attributes=attributes,
            id=id,
            name=name,
            period=period,
            start=start,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_a_maintenance(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.maintenance.delete_a_maintenance(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_maintenance(id, request_options=request_options)
        return _response.data


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    async def fetch_a_list_of_maintenance(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Maintenance]:
        """
        Without params, it returns a list of Maintenance the user has access to

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
        typing.List[Maintenance]
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
            await client.maintenance.fetch_a_list_of_maintenance()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_maintenance(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_a_maintenance(
        self,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Parameters
        ----------
        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
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
            await client.maintenance.create_a_maintenance()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_maintenance(
            attributes=attributes,
            id=id,
            name=name,
            period=period,
            start=start,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def update_a_maintenance(
        self,
        id_: int,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Maintenance:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Maintenance
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
            await client.maintenance.update_a_maintenance(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_maintenance(
            id_,
            attributes=attributes,
            id=id,
            name=name,
            period=period,
            start=start,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_maintenance(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.maintenance.delete_a_maintenance(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_maintenance(id, request_options=request_options)
        return _response.data
