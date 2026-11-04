

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.storage_dashboard import StorageDashboard
from .raw_client import AsyncRawStorageClient, RawStorageClient


class StorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStorageClient
        """
        return self._raw_client

    def get_storage_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> StorageDashboard:
        """
        Return the authenticated user's storage statistics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageDashboard
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.storage.get_storage_stats()
        """
        _response = self._raw_client.get_storage_stats(request_options=request_options)
        return _response.data


class AsyncStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStorageClient
        """
        return self._raw_client

    async def get_storage_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> StorageDashboard:
        """
        Return the authenticated user's storage statistics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageDashboard
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
            await client.storage.get_storage_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_storage_stats(request_options=request_options)
        return _response.data
