

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.workflow_approve_job_response import WorkflowApproveJobResponse
from ..types.workflow_cancel_workflow_response import WorkflowCancelWorkflowResponse
from ..types.workflow_get_by_id_response import WorkflowGetByIdResponse
from ..types.workflow_get_jobs_response import WorkflowGetJobsResponse
from ..types.workflow_rerun_workflow_response import WorkflowRerunWorkflowResponse
from .raw_client import AsyncRawWorkflowClient, RawWorkflowClient


OMIT = typing.cast(typing.Any, ...)


class WorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowClient
        """
        return self._raw_client

    def getbyid(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WorkflowGetByIdResponse:
        """
        Returns summary fields of a workflow by ID.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowGetByIdResponse
            A workflow object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflow.getbyid(
            id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.getbyid(id, request_options=request_options)
        return _response.data

    def approvejob(
        self, id: str, approval_request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowApproveJobResponse:
        """
        Approves a pending approval job in a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        approval_request_id : str
            The ID of the job being approved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowApproveJobResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflow.approvejob(
            id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            approval_request_id="approval_request_id",
        )
        """
        _response = self._raw_client.approvejob(id, approval_request_id, request_options=request_options)
        return _response.data

    def cancelworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowCancelWorkflowResponse:
        """
        Cancels a running workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowCancelWorkflowResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflow.cancelworkflow(
            id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.cancelworkflow(id, request_options=request_options)
        return _response.data

    def getjobs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WorkflowGetJobsResponse:
        """
        Returns a sequence of jobs for a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowGetJobsResponse
            A paginated sequence of jobs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflow.getjobs(
            id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.getjobs(id, request_options=request_options)
        return _response.data

    def rerunworkflow(
        self,
        id: str,
        *,
        enable_ssh: typing.Optional[bool] = OMIT,
        from_failed: typing.Optional[bool] = OMIT,
        jobs: typing.Optional[typing.Sequence[str]] = OMIT,
        sparse_tree: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRerunWorkflowResponse:
        """
        Reruns a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        enable_ssh : typing.Optional[bool]
            Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter.

        from_failed : typing.Optional[bool]
            Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter.

        jobs : typing.Optional[typing.Sequence[str]]
            A list of job IDs to rerun.

        sparse_tree : typing.Optional[bool]
            Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRerunWorkflowResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.workflow.rerunworkflow(
            id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.rerunworkflow(
            id,
            enable_ssh=enable_ssh,
            from_failed=from_failed,
            jobs=jobs,
            sparse_tree=sparse_tree,
            request_options=request_options,
        )
        return _response.data


class AsyncWorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowClient
        """
        return self._raw_client

    async def getbyid(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowGetByIdResponse:
        """
        Returns summary fields of a workflow by ID.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowGetByIdResponse
            A workflow object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflow.getbyid(
                id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbyid(id, request_options=request_options)
        return _response.data

    async def approvejob(
        self, id: str, approval_request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowApproveJobResponse:
        """
        Approves a pending approval job in a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        approval_request_id : str
            The ID of the job being approved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowApproveJobResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflow.approvejob(
                id="5034460f-c7c4-4c43-9457-de07e2029e7b",
                approval_request_id="approval_request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approvejob(id, approval_request_id, request_options=request_options)
        return _response.data

    async def cancelworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowCancelWorkflowResponse:
        """
        Cancels a running workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowCancelWorkflowResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflow.cancelworkflow(
                id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelworkflow(id, request_options=request_options)
        return _response.data

    async def getjobs(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowGetJobsResponse:
        """
        Returns a sequence of jobs for a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowGetJobsResponse
            A paginated sequence of jobs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflow.getjobs(
                id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getjobs(id, request_options=request_options)
        return _response.data

    async def rerunworkflow(
        self,
        id: str,
        *,
        enable_ssh: typing.Optional[bool] = OMIT,
        from_failed: typing.Optional[bool] = OMIT,
        jobs: typing.Optional[typing.Sequence[str]] = OMIT,
        sparse_tree: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRerunWorkflowResponse:
        """
        Reruns a workflow.

        Parameters
        ----------
        id : str
            The unique ID of the workflow.

        enable_ssh : typing.Optional[bool]
            Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter.

        from_failed : typing.Optional[bool]
            Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter.

        jobs : typing.Optional[typing.Sequence[str]]
            A list of job IDs to rerun.

        sparse_tree : typing.Optional[bool]
            Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRerunWorkflowResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflow.rerunworkflow(
                id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rerunworkflow(
            id,
            enable_ssh=enable_ssh,
            from_failed=from_failed,
            jobs=jobs,
            sparse_tree=sparse_tree,
            request_options=request_options,
        )
        return _response.data
