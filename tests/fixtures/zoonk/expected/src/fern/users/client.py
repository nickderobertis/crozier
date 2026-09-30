

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.username_availability_response import UsernameAvailabilityResponse
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

    def get_username_availability(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsernameAvailabilityResponse:
        """
        Availability is advisory. A later profile update can still conflict if another account claims the username first.

        Parameters
        ----------
        username : str
            Normalized username candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsernameAvailabilityResponse
            Current username availability

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_username_availability(
            username="username",
        )
        """
        _response = self._raw_client.get_username_availability(username, request_options=request_options)
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

    async def get_username_availability(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsernameAvailabilityResponse:
        """
        Availability is advisory. A later profile update can still conflict if another account claims the username first.

        Parameters
        ----------
        username : str
            Normalized username candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsernameAvailabilityResponse
            Current username availability

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_username_availability(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_username_availability(username, request_options=request_options)
        return _response.data
