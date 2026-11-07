

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_search_result import UserSearchResult
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

    def search_users(
        self, *, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserSearchResult]:
        """
        Parameters
        ----------
        search : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserSearchResult]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.users.search_users(
            search="search",
        )
        """
        _response = self._raw_client.search_users(search=search, request_options=request_options)
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

    async def search_users(
        self, *, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserSearchResult]:
        """
        Parameters
        ----------
        search : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserSearchResult]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.search_users(
                search="search",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_users(search=search, request_options=request_options)
        return _response.data
