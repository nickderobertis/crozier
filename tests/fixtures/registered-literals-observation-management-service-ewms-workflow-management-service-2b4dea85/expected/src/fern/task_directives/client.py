

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.task_directive_object import TaskDirectiveObject
from ..types.taskforce_object import TaskforceObject
from .raw_client import AsyncRawTaskDirectivesClient, RawTaskDirectivesClient
from .types.post_v1query_task_directives_response import PostV1QueryTaskDirectivesResponse


OMIT = typing.cast(typing.Any, ...)


class TaskDirectivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaskDirectivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaskDirectivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaskDirectivesClient
        """
        return self._raw_client

    def post_v1query_task_directives(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryTaskDirectivesResponse:
        """
        Queries and returns a list of task directive objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1QueryTaskDirectivesResponse
            Matching task directives and pagination metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.task_directives.post_v1query_task_directives(
            query={"key": "value"},
        )
        """
        _response = self._raw_client.post_v1query_task_directives(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    def get_v1task_directives_task_id(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDirectiveObject:
        """
        Retrieves the task directive that matches the specified task ID. See `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDirectiveObject
            The matching task directive

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.task_directives.get_v1task_directives_task_id(
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_v1task_directives_task_id(task_id, request_options=request_options)
        return _response.data

    def post_v1task_directives_task_id_actions_add_workers(
        self,
        task_id: str,
        *,
        cluster_location: str,
        n_workers: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskforceObject:
        """
        Creates a new taskforce (and associated workers) for an existing task directive. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive to which the taskforce (and workers) will be added.

        cluster_location : str

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskforceObject
            The created taskforce object with its details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.task_directives.post_v1task_directives_task_id_actions_add_workers(
            task_id="task_id",
            cluster_location="cluster_location",
        )
        """
        _response = self._raw_client.post_v1task_directives_task_id_actions_add_workers(
            task_id, cluster_location=cluster_location, n_workers=n_workers, request_options=request_options
        )
        return _response.data


class AsyncTaskDirectivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaskDirectivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaskDirectivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaskDirectivesClient
        """
        return self._raw_client

    async def post_v1query_task_directives(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryTaskDirectivesResponse:
        """
        Queries and returns a list of task directive objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1QueryTaskDirectivesResponse
            Matching task directives and pagination metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.task_directives.post_v1query_task_directives(
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1query_task_directives(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    async def get_v1task_directives_task_id(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDirectiveObject:
        """
        Retrieves the task directive that matches the specified task ID. See `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDirectiveObject
            The matching task directive

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.task_directives.get_v1task_directives_task_id(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1task_directives_task_id(task_id, request_options=request_options)
        return _response.data

    async def post_v1task_directives_task_id_actions_add_workers(
        self,
        task_id: str,
        *,
        cluster_location: str,
        n_workers: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskforceObject:
        """
        Creates a new taskforce (and associated workers) for an existing task directive. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive to which the taskforce (and workers) will be added.

        cluster_location : str

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskforceObject
            The created taskforce object with its details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.task_directives.post_v1task_directives_task_id_actions_add_workers(
                task_id="task_id",
                cluster_location="cluster_location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1task_directives_task_id_actions_add_workers(
            task_id, cluster_location=cluster_location, n_workers=n_workers, request_options=request_options
        )
        return _response.data
