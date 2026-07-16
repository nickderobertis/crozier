

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.driver import Driver
from ..types.driver_attributes import DriverAttributes
from .raw_client import AsyncRawDriversClient, RawDriversClient


OMIT = typing.cast(typing.Any, ...)


class DriversClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDriversClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDriversClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDriversClient
        """
        return self._raw_client

    def fetch_a_list_of_drivers(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Driver]:
        """
        Without params, it returns a list of Drivers the user has access to

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
        typing.List[Driver]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drivers.fetch_a_list_of_drivers()
        """
        _response = self._raw_client.fetch_a_list_of_drivers(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_a_driver(
        self,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Driver:
        """
        Parameters
        ----------
        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Driver
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drivers.create_a_driver()
        """
        _response = self._raw_client.create_a_driver(
            attributes=attributes, id=id, name=name, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    def update_a_driver(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Driver:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Driver
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.drivers.update_a_driver(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_driver(
            id_, attributes=attributes, id=id, name=name, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    def delete_a_driver(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.drivers.delete_a_driver(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_driver(id, request_options=request_options)
        return _response.data


class AsyncDriversClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDriversClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDriversClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDriversClient
        """
        return self._raw_client

    async def fetch_a_list_of_drivers(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Driver]:
        """
        Without params, it returns a list of Drivers the user has access to

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
        typing.List[Driver]
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
            await client.drivers.fetch_a_list_of_drivers()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_drivers(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_a_driver(
        self,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Driver:
        """
        Parameters
        ----------
        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Driver
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
            await client.drivers.create_a_driver()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_driver(
            attributes=attributes, id=id, name=name, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    async def update_a_driver(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Driver:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Driver
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
            await client.drivers.update_a_driver(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_driver(
            id_, attributes=attributes, id=id, name=name, unique_id=unique_id, request_options=request_options
        )
        return _response.data

    async def delete_a_driver(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.drivers.delete_a_driver(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_driver(id, request_options=request_options)
        return _response.data
