

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from .raw_client import AsyncRawUsersClient, RawUsersClient


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

    def look_up_a_user_by_username(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.look_up_a_user_by_username(
            username="username",
        )
        """
        _response = self._raw_client.look_up_a_user_by_username(username, request_options=request_options)
        return _response.data

    def look_up_a_user_by_uuid(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.look_up_a_user_by_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.look_up_a_user_by_uuid(uuid_, request_options=request_options)
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

    async def look_up_a_user_by_username(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        username : str

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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.look_up_a_user_by_username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.look_up_a_user_by_username(username, request_options=request_options)
        return _response.data

    async def look_up_a_user_by_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        uuid_ : str

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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.look_up_a_user_by_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.look_up_a_user_by_uuid(uuid_, request_options=request_options)
        return _response.data
