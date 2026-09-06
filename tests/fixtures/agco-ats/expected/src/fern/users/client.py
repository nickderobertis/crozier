

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_user import ApiModelsUser
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

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get(
            id=1,
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def post(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.post()
        """
        _response = self._raw_client.post(
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def getcurrentuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.getcurrentuser()
        """
        _response = self._raw_client.getcurrentuser(request_options=request_options)
        return _response.data

    def putcurrentuser(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.putcurrentuser()
        """
        _response = self._raw_client.putcurrentuser(
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        id: int,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.put(
            id=1,
        )
        """
        _response = self._raw_client.put(
            id,
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.delete(
            id=1,
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
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

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def post(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.post()


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def getcurrentuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsUser:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.getcurrentuser()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcurrentuser(request_options=request_options)
        return _response.data

    async def putcurrentuser(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.putcurrentuser()


        asyncio.run(main())
        """
        _response = await self._raw_client.putcurrentuser(
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        id: int,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.put(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id,
            change_password=change_password,
            email=email,
            name=name,
            password=password,
            user_id=user_id,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data
