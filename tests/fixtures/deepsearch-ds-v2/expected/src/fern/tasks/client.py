

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.task_context import TaskContext
from ..types.task_result import TaskResult
from .raw_client import AsyncRawTasksClient, RawTasksClient
from .types.list_project_tasks_request_sort_order import ListProjectTasksRequestSortOrder


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

    def get_project_celery_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskResult:
        """
        Get a celery task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[float]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tasks.get_project_celery_task(
            proj_key="proj_key",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_project_celery_task(
            proj_key, task_id, wait=wait, request_options=request_options
        )
        return _response.data

    def list_project_tasks(
        self,
        proj_key: str,
        *,
        task_type: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListProjectTasksRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TaskContext]:
        """
        List tasks for a project.

        Parameters
        ----------
        proj_key : str

        task_type : typing.Optional[str]

        skip : typing.Optional[int]

        limit : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_order : typing.Optional[ListProjectTasksRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskContext]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tasks.list_project_tasks(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.list_project_tasks(
            proj_key,
            task_type=task_type,
            skip=skip,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def get_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskContext:
        """
        Get a task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskContext
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tasks.get_project_task(
            proj_key="proj_key",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_project_task(proj_key, task_id, request_options=request_options)
        return _response.data

    def abort_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Abort a task.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tasks.abort_project_task(
            proj_key="proj_key",
            task_id="task_id",
        )
        """
        _response = self._raw_client.abort_project_task(proj_key, task_id, request_options=request_options)
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

    async def get_project_celery_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskResult:
        """
        Get a celery task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[float]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tasks.get_project_celery_task(
                proj_key="proj_key",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_celery_task(
            proj_key, task_id, wait=wait, request_options=request_options
        )
        return _response.data

    async def list_project_tasks(
        self,
        proj_key: str,
        *,
        task_type: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListProjectTasksRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TaskContext]:
        """
        List tasks for a project.

        Parameters
        ----------
        proj_key : str

        task_type : typing.Optional[str]

        skip : typing.Optional[int]

        limit : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_order : typing.Optional[ListProjectTasksRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskContext]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tasks.list_project_tasks(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_tasks(
            proj_key,
            task_type=task_type,
            skip=skip,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def get_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskContext:
        """
        Get a task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskContext
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tasks.get_project_task(
                proj_key="proj_key",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_task(proj_key, task_id, request_options=request_options)
        return _response.data

    async def abort_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Abort a task.

        Parameters
        ----------
        proj_key : str

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

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tasks.abort_project_task(
                proj_key="proj_key",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_project_task(proj_key, task_id, request_options=request_options)
        return _response.data
