

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deactivated_workflow_response_object import DeactivatedWorkflowResponseObject
from ..types.workflow_object import WorkflowObject
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient
from .types.post_v1query_workflows_response import PostV1QueryWorkflowsResponse
from .types.post_v1workflows_request_tasks_item import PostV1WorkflowsRequestTasksItem
from .types.post_v1workflows_response import PostV1WorkflowsResponse


OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowsClient
        """
        return self._raw_client

    def post_v1query_workflows(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryWorkflowsResponse:
        """
        Queries and returns a list of workflow objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

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
        PostV1QueryWorkflowsResponse
            Matching workflows and pagination metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.post_v1query_workflows(
            query={"key": "value"},
        )
        """
        _response = self._raw_client.post_v1query_workflows(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    def post_v1workflows(
        self,
        *,
        tasks: typing.Sequence[PostV1WorkflowsRequestTasksItem],
        public_queue_aliases: typing.Sequence[str],
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1WorkflowsResponse:
        """
        Creates a new workflow along with its associated task directives and taskforces. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        tasks : typing.Sequence[PostV1WorkflowsRequestTasksItem]

        public_queue_aliases : typing.Sequence[str]
            User-defined aliases for queues listed in 'input_queue_aliases' and 'output_queue_aliases' that will be used externally. The actual IDs will be generated after submission.

        priority : typing.Optional[int]
            The workflow's priority level relative to other workflows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1WorkflowsResponse
            The created workflow, task directives, and taskforces.

        Examples
        --------
        from fern.workflows import (
            PostV1WorkflowsRequestTasksItem,
            PostV1WorkflowsRequestTasksItemWorkerConfig,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.post_v1workflows(
            tasks=[
                PostV1WorkflowsRequestTasksItem(
                    cluster_locations=["cluster_locations"],
                    task_image="task_image",
                    task_args="task_args",
                    input_queue_aliases=["input_queue_aliases"],
                    output_queue_aliases=["output_queue_aliases"],
                    worker_config=PostV1WorkflowsRequestTasksItemWorkerConfig(
                        do_transfer_worker_stdouterr=True,
                        max_worker_runtime=1,
                        n_cores=1,
                        priority=1,
                        worker_disk="worker_disk",
                        worker_memory="worker_memory",
                        condor_requirements="condor_requirements",
                    ),
                )
            ],
            public_queue_aliases=["public_queue_aliases"],
        )
        """
        _response = self._raw_client.post_v1workflows(
            tasks=tasks, public_queue_aliases=public_queue_aliases, priority=priority, request_options=request_options
        )
        return _response.data

    def get_v1workflows_workflow_id(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowObject:
        """
        Retrieves the workflow object that matches the specified workflow ID. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowObject
            The matching workflow object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.get_v1workflows_workflow_id(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.get_v1workflows_workflow_id(workflow_id, request_options=request_options)
        return _response.data

    def post_v1workflows_workflow_id_actions_abort(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeactivatedWorkflowResponseObject:
        """
        Aborts the specified workflow, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeactivatedWorkflowResponseObject
            Summary of the deactivated workflow.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.post_v1workflows_workflow_id_actions_abort(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.post_v1workflows_workflow_id_actions_abort(
            workflow_id, request_options=request_options
        )
        return _response.data

    def post_v1workflows_workflow_id_actions_finished(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeactivatedWorkflowResponseObject:
        """
        Marks the specified workflow as finished, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeactivatedWorkflowResponseObject
            Summary of the deactivated workflow.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.post_v1workflows_workflow_id_actions_finished(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.post_v1workflows_workflow_id_actions_finished(
            workflow_id, request_options=request_options
        )
        return _response.data


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowsClient
        """
        return self._raw_client

    async def post_v1query_workflows(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryWorkflowsResponse:
        """
        Queries and returns a list of workflow objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

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
        PostV1QueryWorkflowsResponse
            Matching workflows and pagination metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.post_v1query_workflows(
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1query_workflows(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    async def post_v1workflows(
        self,
        *,
        tasks: typing.Sequence[PostV1WorkflowsRequestTasksItem],
        public_queue_aliases: typing.Sequence[str],
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1WorkflowsResponse:
        """
        Creates a new workflow along with its associated task directives and taskforces. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        tasks : typing.Sequence[PostV1WorkflowsRequestTasksItem]

        public_queue_aliases : typing.Sequence[str]
            User-defined aliases for queues listed in 'input_queue_aliases' and 'output_queue_aliases' that will be used externally. The actual IDs will be generated after submission.

        priority : typing.Optional[int]
            The workflow's priority level relative to other workflows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1WorkflowsResponse
            The created workflow, task directives, and taskforces.

        Examples
        --------
        import asyncio

        from fern.workflows import (
            PostV1WorkflowsRequestTasksItem,
            PostV1WorkflowsRequestTasksItemWorkerConfig,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.post_v1workflows(
                tasks=[
                    PostV1WorkflowsRequestTasksItem(
                        cluster_locations=["cluster_locations"],
                        task_image="task_image",
                        task_args="task_args",
                        input_queue_aliases=["input_queue_aliases"],
                        output_queue_aliases=["output_queue_aliases"],
                        worker_config=PostV1WorkflowsRequestTasksItemWorkerConfig(
                            do_transfer_worker_stdouterr=True,
                            max_worker_runtime=1,
                            n_cores=1,
                            priority=1,
                            worker_disk="worker_disk",
                            worker_memory="worker_memory",
                            condor_requirements="condor_requirements",
                        ),
                    )
                ],
                public_queue_aliases=["public_queue_aliases"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1workflows(
            tasks=tasks, public_queue_aliases=public_queue_aliases, priority=priority, request_options=request_options
        )
        return _response.data

    async def get_v1workflows_workflow_id(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowObject:
        """
        Retrieves the workflow object that matches the specified workflow ID. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowObject
            The matching workflow object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.get_v1workflows_workflow_id(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1workflows_workflow_id(workflow_id, request_options=request_options)
        return _response.data

    async def post_v1workflows_workflow_id_actions_abort(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeactivatedWorkflowResponseObject:
        """
        Aborts the specified workflow, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeactivatedWorkflowResponseObject
            Summary of the deactivated workflow.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.post_v1workflows_workflow_id_actions_abort(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1workflows_workflow_id_actions_abort(
            workflow_id, request_options=request_options
        )
        return _response.data

    async def post_v1workflows_workflow_id_actions_finished(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeactivatedWorkflowResponseObject:
        """
        Marks the specified workflow as finished, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeactivatedWorkflowResponseObject
            Summary of the deactivated workflow.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.post_v1workflows_workflow_id_actions_finished(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1workflows_workflow_id_actions_finished(
            workflow_id, request_options=request_options
        )
        return _response.data
