

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

    def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get basic information about a user

        Parameters
        ----------
        user_id : str
            User Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get(user_id, request_options=request_options)
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

    async def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get basic information about a user

        Parameters
        ----------
        user_id : str
            User Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(user_id, request_options=request_options)
        return _response.data
