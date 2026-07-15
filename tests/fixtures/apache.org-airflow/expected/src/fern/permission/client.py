

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_collection import ActionCollection
from .raw_client import AsyncRawPermissionClient, RawPermissionClient


class PermissionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermissionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermissionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermissionClient
        """
        return self._raw_client

    def get_permissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionCollection:
        """
        Get a list of permissions.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.permission.get_permissions()
        """
        _response = self._raw_client.get_permissions(limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncPermissionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermissionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermissionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermissionClient
        """
        return self._raw_client

    async def get_permissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionCollection:
        """
        Get a list of permissions.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.permission.get_permissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_permissions(limit=limit, offset=offset, request_options=request_options)
        return _response.data
