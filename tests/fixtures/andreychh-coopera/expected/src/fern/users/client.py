

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from ..types.username import Username
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

    def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Who the caller is and whether they have named themselves yet. The state is read from here rather than inferred elsewhere: it outlives any single moment, and someone who closed the app on the naming screen still has to be asked again.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_me()
        """
        _response = self._raw_client.get_me(request_options=request_options)
        return _response.data

    def create_introduction(
        self, *, username: Username, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Names the person for the first time. Until this happens almost everything is closed to them: a name is what others see, and until there is one there is nothing to show. Doing it twice is not a malformed request but a sign that it is long done — hence 409 rather than 400.

        Parameters
        ----------
        username : Username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Introduced

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.create_introduction(
            username="username",
        )
        """
        _response = self._raw_client.create_introduction(username=username, request_options=request_options)
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

    async def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Who the caller is and whether they have named themselves yet. The state is read from here rather than inferred elsewhere: it outlives any single moment, and someone who closed the app on the naming screen still has to be asked again.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_me()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_me(request_options=request_options)
        return _response.data

    async def create_introduction(
        self, *, username: Username, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Names the person for the first time. Until this happens almost everything is closed to them: a name is what others see, and until there is one there is nothing to show. Doing it twice is not a malformed request but a sign that it is long done — hence 409 rather than 400.

        Parameters
        ----------
        username : Username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Introduced

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.create_introduction(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_introduction(username=username, request_options=request_options)
        return _response.data
