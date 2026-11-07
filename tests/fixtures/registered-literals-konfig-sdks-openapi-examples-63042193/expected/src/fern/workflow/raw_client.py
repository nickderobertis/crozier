

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.workflow_approve_job_response import WorkflowApproveJobResponse
from ..types.workflow_cancel_workflow_response import WorkflowCancelWorkflowResponse
from ..types.workflow_get_by_id_response import WorkflowGetByIdResponse
from ..types.workflow_get_jobs_response import WorkflowGetJobsResponse
from ..types.workflow_rerun_workflow_response import WorkflowRerunWorkflowResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getbyid(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowGetByIdResponse]:
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
        HttpResponse[WorkflowGetByIdResponse]
            A workflow object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowGetByIdResponse,
                    parse_obj_as(
                        type_=WorkflowGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def approvejob(
        self, id: str, approval_request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowApproveJobResponse]:
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
        HttpResponse[WorkflowApproveJobResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/approve/{encode_path_param(approval_request_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowApproveJobResponse,
                    parse_obj_as(
                        type_=WorkflowApproveJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancelworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowCancelWorkflowResponse]:
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
        HttpResponse[WorkflowCancelWorkflowResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowCancelWorkflowResponse,
                    parse_obj_as(
                        type_=WorkflowCancelWorkflowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getjobs(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowGetJobsResponse]:
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
        HttpResponse[WorkflowGetJobsResponse]
            A paginated sequence of jobs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/job",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowGetJobsResponse,
                    parse_obj_as(
                        type_=WorkflowGetJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def rerunworkflow(
        self,
        id: str,
        *,
        enable_ssh: typing.Optional[bool] = OMIT,
        from_failed: typing.Optional[bool] = OMIT,
        jobs: typing.Optional[typing.Sequence[str]] = OMIT,
        sparse_tree: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowRerunWorkflowResponse]:
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
        HttpResponse[WorkflowRerunWorkflowResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/rerun",
            method="POST",
            json={
                "enable_ssh": enable_ssh,
                "from_failed": from_failed,
                "jobs": jobs,
                "sparse_tree": sparse_tree,
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
                    WorkflowRerunWorkflowResponse,
                    parse_obj_as(
                        type_=WorkflowRerunWorkflowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getbyid(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowGetByIdResponse]:
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
        AsyncHttpResponse[WorkflowGetByIdResponse]
            A workflow object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowGetByIdResponse,
                    parse_obj_as(
                        type_=WorkflowGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def approvejob(
        self, id: str, approval_request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowApproveJobResponse]:
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
        AsyncHttpResponse[WorkflowApproveJobResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/approve/{encode_path_param(approval_request_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowApproveJobResponse,
                    parse_obj_as(
                        type_=WorkflowApproveJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancelworkflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowCancelWorkflowResponse]:
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
        AsyncHttpResponse[WorkflowCancelWorkflowResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowCancelWorkflowResponse,
                    parse_obj_as(
                        type_=WorkflowCancelWorkflowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getjobs(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowGetJobsResponse]:
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
        AsyncHttpResponse[WorkflowGetJobsResponse]
            A paginated sequence of jobs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/job",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowGetJobsResponse,
                    parse_obj_as(
                        type_=WorkflowGetJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def rerunworkflow(
        self,
        id: str,
        *,
        enable_ssh: typing.Optional[bool] = OMIT,
        from_failed: typing.Optional[bool] = OMIT,
        jobs: typing.Optional[typing.Sequence[str]] = OMIT,
        sparse_tree: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowRerunWorkflowResponse]:
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
        AsyncHttpResponse[WorkflowRerunWorkflowResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflow/{encode_path_param(id)}/rerun",
            method="POST",
            json={
                "enable_ssh": enable_ssh,
                "from_failed": from_failed,
                "jobs": jobs,
                "sparse_tree": sparse_tree,
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
                    WorkflowRerunWorkflowResponse,
                    parse_obj_as(
                        type_=WorkflowRerunWorkflowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
