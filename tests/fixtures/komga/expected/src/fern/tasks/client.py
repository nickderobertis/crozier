

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTasksClient, RawTasksClient


class TasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTasksClient
        """
        return self._raw_client

    def empty_task_queue(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Cancel all tasks queued

        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tasks.empty_task_queue()
        """
        _response = self._raw_client.empty_task_queue(request_options=request_options)
        return _response.data


class AsyncTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTasksClient
        """
        return self._raw_client

    async def empty_task_queue(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Cancel all tasks queued

        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tasks.empty_task_queue()


        asyncio.run(main())
        """
        _response = await self._raw_client.empty_task_queue(request_options=request_options)
        return _response.data
