

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1permission import V1Permission
from .raw_client import AsyncRawPermissionsClient, RawPermissionsClient


class PermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermissionsClient
        """
        return self._raw_client

    def list_current_user_permissions(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Permission]:
        """
        Retrieve all resource permissions for the currently authenticated user.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Permission]
            Permissions retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.permissions.list_current_user_permissions(
            account_id=1,
        )
        """
        _response = self._raw_client.list_current_user_permissions(account_id, request_options=request_options)
        return _response.data

    def list_user_permissions(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Permission]:
        """
        Retrieve all resource permissions for a specific user. Requires read access to users.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Permission]
            Permissions retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.permissions.list_user_permissions(
            account_id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.list_user_permissions(account_id, user_id, request_options=request_options)
        return _response.data


class AsyncPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermissionsClient
        """
        return self._raw_client

    async def list_current_user_permissions(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Permission]:
        """
        Retrieve all resource permissions for the currently authenticated user.

        Parameters
        ----------
        account_id : int
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Permission]
            Permissions retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.permissions.list_current_user_permissions(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_current_user_permissions(account_id, request_options=request_options)
        return _response.data

    async def list_user_permissions(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Permission]:
        """
        Retrieve all resource permissions for a specific user. Requires read access to users.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Permission]
            Permissions retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.permissions.list_user_permissions(
                account_id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_permissions(account_id, user_id, request_options=request_options)
        return _response.data
