

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.queue_job import QueueJob
from .raw_client import AsyncRawQueueClient, RawQueueClient


class QueueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueueClient
        """
        return self._raw_client

    def get_active_queue(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[QueueJob]:
        """
        Return the snapshot of active kits.  Empty list when idle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QueueJob]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.queue.get_active_queue()
        """
        _response = self._raw_client.get_active_queue(request_options=request_options)
        return _response.data


class AsyncQueueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueueClient
        """
        return self._raw_client

    async def get_active_queue(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QueueJob]:
        """
        Return the snapshot of active kits.  Empty list when idle.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QueueJob]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.queue.get_active_queue()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_queue(request_options=request_options)
        return _response.data
