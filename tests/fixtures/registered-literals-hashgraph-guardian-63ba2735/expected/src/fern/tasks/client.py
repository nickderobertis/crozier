

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.task_status import TaskStatus
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

    def returns_task_statuses(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskStatus:
        """
        Returns task statuses by Id.

        Parameters
        ----------
        task_id : str
            Task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskStatus
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tasks.returns_task_statuses(
            task_id="taskId",
        )
        """
        _response = self._raw_client.returns_task_statuses(task_id, request_options=request_options)
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

    async def returns_task_statuses(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskStatus:
        """
        Returns task statuses by Id.

        Parameters
        ----------
        task_id : str
            Task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskStatus
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasks.returns_task_statuses(
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_task_statuses(task_id, request_options=request_options)
        return _response.data
