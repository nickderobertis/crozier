

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_task_get import EnvelopeListTaskGet
from ..types.envelope_task_status import EnvelopeTaskStatus
from ..types.envelope_task_stream_response import EnvelopeTaskStreamResponse
from .raw_client import AsyncRawLongRunningTasksClient, RawLongRunningTasksClient


class LongRunningTasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLongRunningTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLongRunningTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLongRunningTasksClient
        """
        return self._raw_client

    def get_async_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTaskGet:
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
        client.long_running_tasks.get_async_jobs()
        """
        _response = self._raw_client.get_async_jobs(request_options=request_options)
        return _response.data

    def get_async_job_status(
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
        client.long_running_tasks.get_async_job_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_async_job_status(task_id, request_options=request_options)
        return _response.data

    def cancel_async_job(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.long_running_tasks.cancel_async_job(
            task_id="task_id",
        )
        """
        _response = self._raw_client.cancel_async_job(task_id, request_options=request_options)
        return _response.data

    def get_async_job_result(
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
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks.get_async_job_result(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_async_job_result(task_id, request_options=request_options)
        return _response.data

    def get_async_job_stream(
        self,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskStreamResponse:
        """
        Retrieves the stream of a task

        Parameters
        ----------
        task_id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskStreamResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.long_running_tasks.get_async_job_stream(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_async_job_stream(task_id, limit=limit, request_options=request_options)
        return _response.data


class AsyncLongRunningTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLongRunningTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLongRunningTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLongRunningTasksClient
        """
        return self._raw_client

    async def get_async_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTaskGet:
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
            await client.long_running_tasks.get_async_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_jobs(request_options=request_options)
        return _response.data

    async def get_async_job_status(
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
            await client.long_running_tasks.get_async_job_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_job_status(task_id, request_options=request_options)
        return _response.data

    async def cancel_async_job(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.long_running_tasks.cancel_async_job(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_async_job(task_id, request_options=request_options)
        return _response.data

    async def get_async_job_result(
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
            await client.long_running_tasks.get_async_job_result(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_job_result(task_id, request_options=request_options)
        return _response.data

    async def get_async_job_stream(
        self,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskStreamResponse:
        """
        Retrieves the stream of a task

        Parameters
        ----------
        task_id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskStreamResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.long_running_tasks.get_async_job_stream(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_job_stream(task_id, limit=limit, request_options=request_options)
        return _response.data
