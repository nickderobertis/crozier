

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_users import PaginatedUsers
from ..types.user import User
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

    def list_users(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedUsers:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedUsers
            Users ordered by creation time descending.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_users()
        """
        _response = self._raw_client.list_users(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def create_a_user(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        id : typing.Optional[str]
            Optional caller-provided user id. A UUID is generated when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.create_a_user()
        """
        _response = self._raw_client.create_a_user(id=id, request_options=request_options)
        return _response.data

    def get_a_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User found.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_a_user(
            user_id="user-123",
        )
        """
        _response = self._raw_client.get_a_user(user_id, request_options=request_options)
        return _response.data

    def delete_a_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi()
        client.users.delete_a_user(
            user_id="user-123",
        )
        """
        _response = self._raw_client.delete_a_user(user_id, request_options=request_options)
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

    async def list_users(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedUsers:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedUsers
            Users ordered by creation time descending.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    async def create_a_user(
        self, *, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        id : typing.Optional[str]
            Optional caller-provided user id. A UUID is generated when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_a_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_user(id=id, request_options=request_options)
        return _response.data

    async def get_a_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_a_user(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_user(user_id, request_options=request_options)
        return _response.data

    async def delete_a_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete_a_user(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_user(user_id, request_options=request_options)
        return _response.data
