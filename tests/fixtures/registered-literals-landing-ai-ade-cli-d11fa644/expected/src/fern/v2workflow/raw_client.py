

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.prebuilt_workflow_step import PrebuiltWorkflowStep
from ..types.workflow_document_input import WorkflowDocumentInput
from .types.v2workflow_create_job_request_service_tier import V2WorkflowCreateJobRequestServiceTier
from .types.v2workflow_create_job_response import V2WorkflowCreateJobResponse
from .types.v2workflow_get_job_response import V2WorkflowGetJobResponse
from .types.v2workflow_list_jobs_response import V2WorkflowListJobsResponse
from .types.v2workflow_run_sync_response import V2WorkflowRunSyncResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawV2WorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_sync(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2WorkflowRunSyncResponse]:
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
        HttpResponse[V2WorkflowRunSyncResponse]
            v2-workflow result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/workflow",
            method="POST",
            json={
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Dict[str, WorkflowDocumentInput], direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[PrebuiltWorkflowStep], direction="write"
                ),
                "output": output,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowRunSyncResponse,
                    parse_obj_as(
                        type_=V2WorkflowRunSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2WorkflowListJobsResponse]:
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
        HttpResponse[V2WorkflowListJobsResponse]
            The caller's jobs, newest first
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/workflow/jobs",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowListJobsResponse,
                    parse_obj_as(
                        type_=V2WorkflowListJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_job(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        service_tier: typing.Optional[V2WorkflowCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2WorkflowCreateJobResponse]:
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
        HttpResponse[V2WorkflowCreateJobResponse]
            Job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/workflow/jobs",
            method="POST",
            json={
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Dict[str, WorkflowDocumentInput], direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[PrebuiltWorkflowStep], direction="write"
                ),
                "output": output,
                "service_tier": service_tier,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowCreateJobResponse,
                    parse_obj_as(
                        type_=V2WorkflowCreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2WorkflowGetJobResponse]:
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
        HttpResponse[V2WorkflowGetJobResponse]
            Job status / result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/workflow/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowGetJobResponse,
                    parse_obj_as(
                        type_=V2WorkflowGetJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawV2WorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_sync(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2WorkflowRunSyncResponse]:
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
        AsyncHttpResponse[V2WorkflowRunSyncResponse]
            v2-workflow result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/workflow",
            method="POST",
            json={
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Dict[str, WorkflowDocumentInput], direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[PrebuiltWorkflowStep], direction="write"
                ),
                "output": output,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowRunSyncResponse,
                    parse_obj_as(
                        type_=V2WorkflowRunSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2WorkflowListJobsResponse]:
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
        AsyncHttpResponse[V2WorkflowListJobsResponse]
            The caller's jobs, newest first
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/workflow/jobs",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowListJobsResponse,
                    parse_obj_as(
                        type_=V2WorkflowListJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_job(
        self,
        *,
        inputs: typing.Dict[str, WorkflowDocumentInput],
        steps: typing.Sequence[PrebuiltWorkflowStep],
        output: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        service_tier: typing.Optional[V2WorkflowCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2WorkflowCreateJobResponse]:
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
        AsyncHttpResponse[V2WorkflowCreateJobResponse]
            Job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/workflow/jobs",
            method="POST",
            json={
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Dict[str, WorkflowDocumentInput], direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[PrebuiltWorkflowStep], direction="write"
                ),
                "output": output,
                "service_tier": service_tier,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowCreateJobResponse,
                    parse_obj_as(
                        type_=V2WorkflowCreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2WorkflowGetJobResponse]:
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
        AsyncHttpResponse[V2WorkflowGetJobResponse]
            Job status / result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/workflow/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2WorkflowGetJobResponse,
                    parse_obj_as(
                        type_=V2WorkflowGetJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
