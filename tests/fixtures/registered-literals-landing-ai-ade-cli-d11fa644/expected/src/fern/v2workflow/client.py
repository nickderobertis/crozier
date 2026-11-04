

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.prebuilt_workflow_step import PrebuiltWorkflowStep
from ..types.workflow_document_input import WorkflowDocumentInput
from .raw_client import AsyncRawV2WorkflowClient, RawV2WorkflowClient
from .types.v2workflow_create_job_request_service_tier import V2WorkflowCreateJobRequestServiceTier
from .types.v2workflow_create_job_response import V2WorkflowCreateJobResponse
from .types.v2workflow_get_job_response import V2WorkflowGetJobResponse
from .types.v2workflow_list_jobs_response import V2WorkflowListJobsResponse
from .types.v2workflow_run_sync_response import V2WorkflowRunSyncResponse


OMIT = typing.cast(typing.Any, ...)


class V2WorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV2WorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV2WorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV2WorkflowClient
        """
        return self._raw_client

    def run_sync(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowRunSyncResponse:
        """
        Run synchronously and return the result inline.

        Accepts ``application/json`` (the request fields as the body) or
        ``multipart/form-data`` (file fields are staged automatically).

        Returns **504** if the work does not finish within the wait
        window — long-running work belongs on the async ``POST
        {path}/jobs`` route, which returns 202 immediately and is polled
        via ``GET {path}/jobs/{job_id}``. On a 504 the workflow is
        CANCELLED (a sync caller can never collect the result); a retry
        starts the work over as a fresh job.

        Parameters
        ----------
        inputs : typing.Dict[str, WorkflowDocumentInput]
            Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.

        steps : typing.Sequence[PrebuiltWorkflowStep]
            Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.

        output : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowRunSyncResponse
            v2-workflow result

        Examples
        --------
        from fern import (
            FernApi,
            PrebuiltWorkflowStep,
            PrebuiltWorkflowStepName,
            WorkflowDocumentInput,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.v2workflow.run_sync(
            inputs={
                "report": WorkflowDocumentInput(
                    document="report_pdf",
                )
            },
            steps=[
                PrebuiltWorkflowStep(
                    name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
                    document="$inputs.report",
                    schema={
                        "properties": {"revenue": {"type": "string"}},
                        "type": "object",
                    },
                )
            ],
        )
        """
        _response = self._raw_client.run_sync(
            inputs=inputs, steps=steps, output=output, request_options=request_options
        )
        return _response.data

    def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowListJobsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.v2workflow.list_jobs()
        """
        _response = self._raw_client.list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    def create_job(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        service_tier: typing.Optional[V2WorkflowCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowCreateJobResponse:
        """
        Parameters
        ----------
        inputs : typing.Dict[str, WorkflowDocumentInput]
            Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.

        steps : typing.Sequence[PrebuiltWorkflowStep]
            Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.

        output : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.

        service_tier : typing.Optional[V2WorkflowCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowCreateJobResponse
            Job created

        Examples
        --------
        from fern import (
            FernApi,
            PrebuiltWorkflowStep,
            PrebuiltWorkflowStepName,
            WorkflowDocumentInput,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.v2workflow.create_job(
            inputs={
                "report": WorkflowDocumentInput(
                    document="report_pdf",
                )
            },
            steps=[
                PrebuiltWorkflowStep(
                    name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
                    document="$inputs.report",
                    schema={
                        "properties": {"revenue": {"type": "string"}},
                        "type": "object",
                    },
                )
            ],
        )
        """
        _response = self._raw_client.create_job(
            inputs=inputs, steps=steps, output=output, service_tier=service_tier, request_options=request_options
        )
        return _response.data

    def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2WorkflowGetJobResponse:
        """
        Poll a job.

        Returns ``{job_id, status, created_at}`` plus ``completed_at`` and
        ``result`` (on ``completed``) or ``error: {code, message}`` (on
        ``failed``). Statuses: ``pending`` → ``processing`` →
        ``completed`` | ``failed``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowGetJobResponse
            Job status / result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.v2workflow.get_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data


class AsyncV2WorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV2WorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV2WorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV2WorkflowClient
        """
        return self._raw_client

    async def run_sync(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowRunSyncResponse:
        """
        Run synchronously and return the result inline.

        Accepts ``application/json`` (the request fields as the body) or
        ``multipart/form-data`` (file fields are staged automatically).

        Returns **504** if the work does not finish within the wait
        window — long-running work belongs on the async ``POST
        {path}/jobs`` route, which returns 202 immediately and is polled
        via ``GET {path}/jobs/{job_id}``. On a 504 the workflow is
        CANCELLED (a sync caller can never collect the result); a retry
        starts the work over as a fresh job.

        Parameters
        ----------
        inputs : typing.Dict[str, WorkflowDocumentInput]
            Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.

        steps : typing.Sequence[PrebuiltWorkflowStep]
            Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.

        output : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowRunSyncResponse
            v2-workflow result

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PrebuiltWorkflowStep,
            PrebuiltWorkflowStepName,
            WorkflowDocumentInput,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.v2workflow.run_sync(
                inputs={
                    "report": WorkflowDocumentInput(
                        document="report_pdf",
                    )
                },
                steps=[
                    PrebuiltWorkflowStep(
                        name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
                        document="$inputs.report",
                        schema={
                            "properties": {"revenue": {"type": "string"}},
                            "type": "object",
                        },
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_sync(
            inputs=inputs, steps=steps, output=output, request_options=request_options
        )
        return _response.data

    async def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowListJobsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.v2workflow.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    async def create_job(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        service_tier: typing.Optional[V2WorkflowCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2WorkflowCreateJobResponse:
        """
        Parameters
        ----------
        inputs : typing.Dict[str, WorkflowDocumentInput]
            Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.

        steps : typing.Sequence[PrebuiltWorkflowStep]
            Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.

        output : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.

        service_tier : typing.Optional[V2WorkflowCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowCreateJobResponse
            Job created

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PrebuiltWorkflowStep,
            PrebuiltWorkflowStepName,
            WorkflowDocumentInput,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.v2workflow.create_job(
                inputs={
                    "report": WorkflowDocumentInput(
                        document="report_pdf",
                    )
                },
                steps=[
                    PrebuiltWorkflowStep(
                        name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
                        document="$inputs.report",
                        schema={
                            "properties": {"revenue": {"type": "string"}},
                            "type": "object",
                        },
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_job(
            inputs=inputs, steps=steps, output=output, service_tier=service_tier, request_options=request_options
        )
        return _response.data

    async def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2WorkflowGetJobResponse:
        """
        Poll a job.

        Returns ``{job_id, status, created_at}`` plus ``completed_at`` and
        ``result`` (on ``completed``) or ``error: {code, message}`` (on
        ``failed``). Statuses: ``pending`` → ``processing`` →
        ``completed`` | ``failed``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2WorkflowGetJobResponse
            Job status / result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.v2workflow.get_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data
