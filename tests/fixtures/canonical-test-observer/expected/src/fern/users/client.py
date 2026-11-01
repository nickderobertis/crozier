

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_response import UserResponse
from ..types.users_response import UsersResponse
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

    def get_authenticated_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[UserResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[UserResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.get_authenticated_user()
        """
        _response = self._raw_client.get_authenticated_user(request_options=request_options)
        return _response.data

    def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        q : typing.Optional[str]
            Search term for user email, name, launchpad handle, or id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(limit=limit, offset=offset, q=q, request_options=request_options)
        return _response.data

    def get_user(self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UserResponse:
        """
        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.get_user(
            user_id=1,
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    def delete_user(self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.delete_user(
            user_id=1,
        )
        """
        _response = self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    def update_user(
        self,
        user_id: int,
        *,
        is_admin: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserResponse:
        """
        Parameters
        ----------
        user_id : int

        is_admin : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.update_user(
            user_id=1,
        )
        """
        _response = self._raw_client.update_user(user_id, is_admin=is_admin, request_options=request_options)
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

    async def get_authenticated_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[UserResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[UserResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.get_authenticated_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authenticated_user(request_options=request_options)
        return _response.data

    async def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        q : typing.Optional[str]
            Search term for user email, name, launchpad handle, or id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(limit=limit, offset=offset, q=q, request_options=request_options)
        return _response.data

    async def get_user(self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UserResponse:
        """
        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.get_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    async def delete_user(self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user_id : int

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
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.delete_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    async def update_user(
        self,
        user_id: int,
        *,
        is_admin: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserResponse:
        """
        Parameters
        ----------
        user_id : int

        is_admin : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.update_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(user_id, is_admin=is_admin, request_options=request_options)
        return _response.data
