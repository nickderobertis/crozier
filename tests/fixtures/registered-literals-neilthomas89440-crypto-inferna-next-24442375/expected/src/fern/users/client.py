

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_out import UserOut
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

    def list_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.list_users()
        """
        _response = self._raw_client.list_users(request_options=request_options)
        return _response.data

    def create_user(
        self,
        *,
        username: str,
        password: str,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserOut:
        """
        Parameters
        ----------
        username : str

        password : str

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.create_user(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.create_user(
            username=username, password=password, role=role, request_options=request_options
        )
        return _response.data

    def delete_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.delete_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    def change_password(
        self, user_id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserOut:
        """
        Parameters
        ----------
        user_id : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.change_password(
            user_id="user_id",
            password="password",
        )
        """
        _response = self._raw_client.change_password(user_id, password=password, request_options=request_options)
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

    async def list_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(request_options=request_options)
        return _response.data

    async def create_user(
        self,
        *,
        username: str,
        password: str,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserOut:
        """
        Parameters
        ----------
        username : str

        password : str

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.create_user(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            username=username, password=password, role=role, request_options=request_options
        )
        return _response.data

    async def delete_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.delete_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    async def change_password(
        self, user_id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserOut:
        """
        Parameters
        ----------
        user_id : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.change_password(
                user_id="user_id",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_password(user_id, password=password, request_options=request_options)
        return _response.data
