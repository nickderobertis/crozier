

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.lock import Lock
from .raw_client import AsyncRawLocksClient, RawLocksClient


class LocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocksClient
        """
        return self._raw_client

    def get_lock(self, lock_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Lock:
        """
        Parameters
        ----------
        lock_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lock
            The lock.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.locks.get_lock(
            lock_id="lockId",
        )
        """
        _response = self._raw_client.get_lock(lock_id, request_options=request_options)
        return _response.data


class AsyncLocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocksClient
        """
        return self._raw_client

    async def get_lock(self, lock_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Lock:
        """
        Parameters
        ----------
        lock_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lock
            The lock.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.locks.get_lock(
                lock_id="lockId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lock(lock_id, request_options=request_options)
        return _response.data
