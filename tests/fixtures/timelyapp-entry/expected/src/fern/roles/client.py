

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1role import V1Role
from .raw_client import AsyncRawRolesClient, RawRolesClient


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

    def list_roles(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Role]:
        """
        Retrieve all roles available in the account. Roles define permissions and access levels for users, including admin, manager, employee, and team lead roles.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Role]
            Roles list retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.roles.list_roles(
            account_id=1,
        )
        """
        _response = self._raw_client.list_roles(account_id, request_options=request_options)
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

    async def list_roles(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Role]:
        """
        Retrieve all roles available in the account. Roles define permissions and access levels for users, including admin, manager, employee, and team lead roles.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Role]
            Roles list retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.roles.list_roles(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_roles(account_id, request_options=request_options)
        return _response.data
