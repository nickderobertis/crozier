

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from ..types.user_attributes import UserAttributes
from .raw_client import AsyncRawUsersClient, RawUsersClient


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def fetch_a_list_of_users(
        self, *, user_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        user_id : typing.Optional[str]
            Can only be used by admin or manager users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.fetch_a_list_of_users()
        """
        _response = self._raw_client.fetch_a_list_of_users(user_id=user_id, request_options=request_options)
        return _response.data

    def create_a_user(
        self,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.create_a_user()
        """
        _response = self._raw_client.create_a_user(
            administrator=administrator,
            attributes=attributes,
            coordinate_format=coordinate_format,
            device_limit=device_limit,
            device_readonly=device_readonly,
            disabled=disabled,
            email=email,
            expiration_time=expiration_time,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            name=name,
            password=password,
            phone=phone,
            poi_layer=poi_layer,
            readonly=readonly,
            twelve_hour_format=twelve_hour_format,
            user_limit=user_limit,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data

    def update_a_user(
        self,
        id_: int,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        id_ : int

        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.update_a_user(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_user(
            id_,
            administrator=administrator,
            attributes=attributes,
            coordinate_format=coordinate_format,
            device_limit=device_limit,
            device_readonly=device_readonly,
            disabled=disabled,
            email=email,
            expiration_time=expiration_time,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            name=name,
            password=password,
            phone=phone,
            poi_layer=poi_layer,
            readonly=readonly,
            twelve_hour_format=twelve_hour_format,
            user_limit=user_limit,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data

    def delete_a_user(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.users.delete_a_user(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_user(id, request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def fetch_a_list_of_users(
        self, *, user_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        user_id : typing.Optional[str]
            Can only be used by admin or manager users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
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
            await client.users.fetch_a_list_of_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_users(user_id=user_id, request_options=request_options)
        return _response.data

    async def create_a_user(
        self,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
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
            await client.users.create_a_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_user(
            administrator=administrator,
            attributes=attributes,
            coordinate_format=coordinate_format,
            device_limit=device_limit,
            device_readonly=device_readonly,
            disabled=disabled,
            email=email,
            expiration_time=expiration_time,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            name=name,
            password=password,
            phone=phone,
            poi_layer=poi_layer,
            readonly=readonly,
            twelve_hour_format=twelve_hour_format,
            user_limit=user_limit,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data

    async def update_a_user(
        self,
        id_: int,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        id_ : int

        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
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
            await client.users.update_a_user(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_user(
            id_,
            administrator=administrator,
            attributes=attributes,
            coordinate_format=coordinate_format,
            device_limit=device_limit,
            device_readonly=device_readonly,
            disabled=disabled,
            email=email,
            expiration_time=expiration_time,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            name=name,
            password=password,
            phone=phone,
            poi_layer=poi_layer,
            readonly=readonly,
            twelve_hour_format=twelve_hour_format,
            user_limit=user_limit,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_user(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.users.delete_a_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_user(id, request_options=request_options)
        return _response.data
