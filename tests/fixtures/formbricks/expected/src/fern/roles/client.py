

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRolesClient, RawRolesClient
from .types.get_roles_response import GetRolesResponse


class RolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRolesClient
        """
        return self._raw_client

    def get_roles(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRolesResponse:
        """
        Gets roles from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRolesResponse
            Roles retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.roles.get_roles()
        """
        _response = self._raw_client.get_roles(request_options=request_options)
        return _response.data


class AsyncRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRolesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRolesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRolesClient
        """
        return self._raw_client

    async def get_roles(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRolesResponse:
        """
        Gets roles from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRolesResponse
            Roles retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.roles.get_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_roles(request_options=request_options)
        return _response.data
