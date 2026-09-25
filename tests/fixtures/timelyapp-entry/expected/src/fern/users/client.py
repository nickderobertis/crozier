

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1user import V1User
from ..types.v1users_create_user import V1UsersCreateUser
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.list_users_request_filter import ListUsersRequestFilter


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

    def get_current_user(self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> V1User:
        """
        Returns the current user information for the authenticated user.

        Parameters
        ----------
        account_id : int
            Workspace id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            current user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_current_user(
            account_id=1,
        )
        """
        _response = self._raw_client.get_current_user(account_id, request_options=request_options)
        return _response.data

    def list_users(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListUsersRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1User]:
        """
        Lists users in the account. Requires global user read permission or project update permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip

        order : typing.Optional[str]
            Sort order

        filter : typing.Optional[ListUsersRequestFilter]
            Filter for deleted users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1User]
            users list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.list_users(
            account_id=1,
        )
        """
        _response = self._raw_client.list_users(
            account_id, limit=limit, offset=offset, order=order, filter=filter, request_options=request_options
        )
        return _response.data

    def invite_user(
        self, account_id: int, *, user: V1UsersCreateUser, request_options: typing.Optional[RequestOptions] = None
    ) -> V1User:
        """
        Invites user to the account. Requires trial/active subscription as also available seats in the workspace to accommodate additional users.

        Parameters
        ----------
        account_id : int
            Workspace id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user invited

        Examples
        --------
        from fern import (
            FernApi,
            V1UsersCreateUser,
            V1UsersCreateUserProjectsOneItem,
            V1UsersCreateUserUserLevel,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.invite_user(
            account_id=1,
            user=V1UsersCreateUser(
                admin=False,
                projects=[
                    V1UsersCreateUserProjectsOneItem(
                        project_id=1,
                        hour_rate=10.0,
                    )
                ],
                user_level=V1UsersCreateUserUserLevel.NORMAL,
                name="Marija Petrovic",
                email="marija@timely.com",
            ),
        )
        """
        _response = self._raw_client.invite_user(account_id, user=user, request_options=request_options)
        return _response.data

    def get_user(self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> V1User:
        """
        Get specific user details. Requires read permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_user(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.get_user(account_id, id, request_options=request_options)
        return _response.data

    def update_user(
        self,
        account_id: int,
        id: int,
        *,
        user: V1UsersCreateUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1User:
        """
        Update user details. Requires update permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user updated

        Examples
        --------
        from fern import FernApi, V1UsersCreateUser

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.update_user(
            account_id=1,
            id=1,
            user=V1UsersCreateUser(
                role_id=1,
                name="Updated Name",
                email="updated@timely.com",
            ),
        )
        """
        _response = self._raw_client.update_user(account_id, id, user=user, request_options=request_options)
        return _response.data

    def delete_user(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete/remove user from account. Requires delete permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            user deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.delete_user(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_user(account_id, id, request_options=request_options)
        return _response.data

    def search_users(
        self,
        account_id: int,
        *,
        q: str,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1User]:
        """
        Search users. Requires create or update project permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        q : str
            Search query

        per_page : typing.Optional[int]
            Results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1User]
            search results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.search_users(
            account_id=1,
            q="q",
        )
        """
        _response = self._raw_client.search_users(
            account_id, q=q, per_page=per_page, page=page, request_options=request_options
        )
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

    async def get_current_user(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1User:
        """
        Returns the current user information for the authenticated user.

        Parameters
        ----------
        account_id : int
            Workspace id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            current user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_current_user(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(account_id, request_options=request_options)
        return _response.data

    async def list_users(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListUsersRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1User]:
        """
        Lists users in the account. Requires global user read permission or project update permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip

        order : typing.Optional[str]
            Sort order

        filter : typing.Optional[ListUsersRequestFilter]
            Filter for deleted users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1User]
            users list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.list_users(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(
            account_id, limit=limit, offset=offset, order=order, filter=filter, request_options=request_options
        )
        return _response.data

    async def invite_user(
        self, account_id: int, *, user: V1UsersCreateUser, request_options: typing.Optional[RequestOptions] = None
    ) -> V1User:
        """
        Invites user to the account. Requires trial/active subscription as also available seats in the workspace to accommodate additional users.

        Parameters
        ----------
        account_id : int
            Workspace id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user invited

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1UsersCreateUser,
            V1UsersCreateUserProjectsOneItem,
            V1UsersCreateUserUserLevel,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.invite_user(
                account_id=1,
                user=V1UsersCreateUser(
                    admin=False,
                    projects=[
                        V1UsersCreateUserProjectsOneItem(
                            project_id=1,
                            hour_rate=10.0,
                        )
                    ],
                    user_level=V1UsersCreateUserUserLevel.NORMAL,
                    name="Marija Petrovic",
                    email="marija@timely.com",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite_user(account_id, user=user, request_options=request_options)
        return _response.data

    async def get_user(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1User:
        """
        Get specific user details. Requires read permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_user(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(account_id, id, request_options=request_options)
        return _response.data

    async def update_user(
        self,
        account_id: int,
        id: int,
        *,
        user: V1UsersCreateUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1User:
        """
        Update user details. Requires update permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1User
            user updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1UsersCreateUser

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.update_user(
                account_id=1,
                id=1,
                user=V1UsersCreateUser(
                    role_id=1,
                    name="Updated Name",
                    email="updated@timely.com",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(account_id, id, user=user, request_options=request_options)
        return _response.data

    async def delete_user(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete/remove user from account. Requires delete permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            user deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.delete_user(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(account_id, id, request_options=request_options)
        return _response.data

    async def search_users(
        self,
        account_id: int,
        *,
        q: str,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1User]:
        """
        Search users. Requires create or update project permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        q : str
            Search query

        per_page : typing.Optional[int]
            Results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1User]
            search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.search_users(
                account_id=1,
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_users(
            account_id, q=q, per_page=per_page, page=page, request_options=request_options
        )
        return _response.data
