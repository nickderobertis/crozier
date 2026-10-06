

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from ..types.user_id import UserId
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.users_get_response import UsersGetResponse
from .types.users_patch_response import UsersPatchResponse


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

    def get(
        self,
        *,
        q: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        count: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersGetResponse:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Search for users by name

        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Fetch users by ID

        count : typing.Optional[int]

        page : typing.Optional[str]
            Fetch users before this cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.get()
        """
        _response = self._raw_client.get(q=q, id=id, count=count, page=page, request_options=request_options)
        return _response.data

    def post(self, *, name: str, age: int, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        name : str
            Name of the user

        age : int
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.post(
            name="Jack Daniels",
            age=1,
        )
        """
        _response = self._raw_client.post(name=name, age=age, request_options=request_options)
        return _response.data

    def patch(
        self,
        *,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersPatchResponse:
        """
        Parameters
        ----------
        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Edit these specific users

        name : typing.Optional[str]
            Name of the user

        age : typing.Optional[int]
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPatchResponse
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.users.patch(
            id=["id"],
        )
        """
        _response = self._raw_client.patch(id=id, name=name, age=age, request_options=request_options)
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

    async def get(
        self,
        *,
        q: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        count: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersGetResponse:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Search for users by name

        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Fetch users by ID

        count : typing.Optional[int]

        page : typing.Optional[str]
            Fetch users before this cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(q=q, id=id, count=count, page=page, request_options=request_options)
        return _response.data

    async def post(self, *, name: str, age: int, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        name : str
            Name of the user

        age : int
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.post(
                name="Jack Daniels",
                age=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(name=name, age=age, request_options=request_options)
        return _response.data

    async def patch(
        self,
        *,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersPatchResponse:
        """
        Parameters
        ----------
        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Edit these specific users

        name : typing.Optional[str]
            Name of the user

        age : typing.Optional[int]
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersPatchResponse
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.users.patch(
                id=["id"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(id=id, name=name, age=age, request_options=request_options)
        return _response.data
