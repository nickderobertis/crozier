

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def get_permissions(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.permissions.get_permissions()
        """
        _response = self._raw_client.get_permissions(request_options=request_options)
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

    async def get_permissions(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permissions.get_permissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_permissions(request_options=request_options)
        return _response.data
