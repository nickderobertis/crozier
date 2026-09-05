

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_task_get import EnvelopeListTaskGet
from ..types.envelope_task_status import EnvelopeTaskStatus
from .raw_client import AsyncRawLongRunningTasksLegacyClient, RawLongRunningTasksLegacyClient


class LongRunningTasksLegacyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLongRunningTasksLegacyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLongRunningTasksLegacyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLongRunningTasksLegacyClient
        """
        return self._raw_client

    def list_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTaskGet:
        """
        Lists all long running tasks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks_legacy.list_tasks()
        """
        _response = self._raw_client.list_tasks(request_options=request_options)
        return _response.data

    def get_task_status(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskStatus:
        """
        Retrieves the status of a task

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks_legacy.get_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_status(task_id, request_options=request_options)
        return _response.data

    def remove_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancels and removes a task

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks_legacy.remove_task(
            task_id="task_id",
        )
        """
        _response = self._raw_client.remove_task(task_id, request_options=request_options)
        return _response.data

    def get_task_result(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieves the result of a task

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks_legacy.get_task_result(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_result(task_id, request_options=request_options)
        return _response.data


class AsyncLongRunningTasksLegacyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLongRunningTasksLegacyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLongRunningTasksLegacyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLongRunningTasksLegacyClient
        """
        return self._raw_client

    async def list_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTaskGet:
        """
        Lists all long running tasks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.long_running_tasks_legacy.list_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tasks(request_options=request_options)
        return _response.data

    async def get_task_status(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskStatus:
        """
        Retrieves the status of a task

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.long_running_tasks_legacy.get_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_status(task_id, request_options=request_options)
        return _response.data

    async def remove_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancels and removes a task

        Parameters
        ----------
        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.long_running_tasks_legacy.remove_task(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_task(task_id, request_options=request_options)
        return _response.data

    async def get_task_result(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves the result of a task

        Parameters
        ----------
        task_id : str

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.long_running_tasks_legacy.get_task_result(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_result(task_id, request_options=request_options)
        return _response.data
