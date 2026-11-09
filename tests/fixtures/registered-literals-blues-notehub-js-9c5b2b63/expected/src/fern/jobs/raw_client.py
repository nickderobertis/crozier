

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.batch_job_requests import BatchJobRequests
from ..types.job_definition_report_options import JobDefinitionReportOptions
from ..types.job_definition_select import JobDefinitionSelect
from ..types.job_detail import JobDetail
from ..types.job_run import JobRun
from .types.cancel_job_run_response import CancelJobRunResponse
from .types.create_job_response import CreateJobResponse
from .types.delete_job_response import DeleteJobResponse
from .types.get_job_run_request_view import GetJobRunRequestView
from .types.get_job_runs_response import GetJobRunsResponse
from .types.get_jobs_response import GetJobsResponse
from .types.run_job_response import RunJobResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jobs(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetJobsResponse]:
        """
        List all batch jobs for a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetJobsResponse]
            List of batch jobs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobsResponse,
                    parse_obj_as(
                        type_=GetJobsResponse,
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

    def create_job(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        comment: typing.Optional[str] = OMIT,
        default_requests: typing.Optional[BatchJobRequests] = OMIT,
        device_requests: typing.Optional[typing.Dict[str, BatchJobRequests]] = OMIT,
        report_options: typing.Optional[JobDefinitionReportOptions] = OMIT,
        select: typing.Optional[JobDefinitionSelect] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateJobResponse]:
        """
        Create a new batch job with an optional name

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            Name for the job

        comment : typing.Optional[str]
            Human-readable description of the job

        default_requests : typing.Optional[BatchJobRequests]

        device_requests : typing.Optional[typing.Dict[str, BatchJobRequests]]
            Device-specific request overrides, keyed by device UID

        report_options : typing.Optional[JobDefinitionReportOptions]
            Controls what data is included in the job report

        select : typing.Optional[JobDefinitionSelect]
            Device selection criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateJobResponse]
            Job created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs",
            method="POST",
            params={
                "name": name,
            },
            json={
                "comment": comment,
                "default_requests": convert_and_respect_annotation_metadata(
                    object_=default_requests, annotation=BatchJobRequests, direction="write"
                ),
                "device_requests": convert_and_respect_annotation_metadata(
                    object_=device_requests, annotation=typing.Dict[str, BatchJobRequests], direction="write"
                ),
                "report_options": convert_and_respect_annotation_metadata(
                    object_=report_options, annotation=JobDefinitionReportOptions, direction="write"
                ),
                "select": convert_and_respect_annotation_metadata(
                    object_=select, annotation=JobDefinitionSelect, direction="write"
                ),
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
                    CreateJobResponse,
                    parse_obj_as(
                        type_=CreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobDetail]:
        """
        Get a specific batch job definition

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobDetail]
            Batch job details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobDetail,
                    parse_obj_as(
                        type_=JobDetail,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteJobResponse]:
        """
        Delete a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteJobResponse]
            Job deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteJobResponse,
                    parse_obj_as(
                        type_=DeleteJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def run_job(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunJobResponse]:
        """
        Execute a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        dry_run : typing.Optional[bool]
            Run job in dry-run mode without making actual changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunJobResponse]
            Job execution started
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}/run",
            method="POST",
            params={
                "dry_run": dry_run,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunJobResponse,
                    parse_obj_as(
                        type_=RunJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def get_job_runs(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        status: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetJobRunsResponse]:
        """
        List all runs for a specific job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        status : typing.Optional[str]
            Filter runs by status

        dry_run : typing.Optional[bool]
            Filter runs by dry run flag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetJobRunsResponse]
            List of job runs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}/runs",
            method="GET",
            params={
                "status": status,
                "dry_run": dry_run,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobRunsResponse,
                    parse_obj_as(
                        type_=GetJobRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def get_job_run(
        self,
        project_or_product_uid: str,
        report_uid: str,
        *,
        view: typing.Optional[GetJobRunRequestView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobRun]:
        """
        Get the result of a job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        view : typing.Optional[GetJobRunRequestView]
            Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobRun]
            Job run details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}",
            method="GET",
            params={
                "view": view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobRun,
                    parse_obj_as(
                        type_=JobRun,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete the results of a job run

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def cancel_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelJobRunResponse]:
        """
        Cancel a running job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelJobRunResponse]
            Cancel operation completed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelJobRunResponse,
                    parse_obj_as(
                        type_=CancelJobRunResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jobs(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetJobsResponse]:
        """
        List all batch jobs for a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetJobsResponse]
            List of batch jobs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobsResponse,
                    parse_obj_as(
                        type_=GetJobsResponse,
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

    async def create_job(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        comment: typing.Optional[str] = OMIT,
        default_requests: typing.Optional[BatchJobRequests] = OMIT,
        device_requests: typing.Optional[typing.Dict[str, BatchJobRequests]] = OMIT,
        report_options: typing.Optional[JobDefinitionReportOptions] = OMIT,
        select: typing.Optional[JobDefinitionSelect] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateJobResponse]:
        """
        Create a new batch job with an optional name

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            Name for the job

        comment : typing.Optional[str]
            Human-readable description of the job

        default_requests : typing.Optional[BatchJobRequests]

        device_requests : typing.Optional[typing.Dict[str, BatchJobRequests]]
            Device-specific request overrides, keyed by device UID

        report_options : typing.Optional[JobDefinitionReportOptions]
            Controls what data is included in the job report

        select : typing.Optional[JobDefinitionSelect]
            Device selection criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateJobResponse]
            Job created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs",
            method="POST",
            params={
                "name": name,
            },
            json={
                "comment": comment,
                "default_requests": convert_and_respect_annotation_metadata(
                    object_=default_requests, annotation=BatchJobRequests, direction="write"
                ),
                "device_requests": convert_and_respect_annotation_metadata(
                    object_=device_requests, annotation=typing.Dict[str, BatchJobRequests], direction="write"
                ),
                "report_options": convert_and_respect_annotation_metadata(
                    object_=report_options, annotation=JobDefinitionReportOptions, direction="write"
                ),
                "select": convert_and_respect_annotation_metadata(
                    object_=select, annotation=JobDefinitionSelect, direction="write"
                ),
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
                    CreateJobResponse,
                    parse_obj_as(
                        type_=CreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobDetail]:
        """
        Get a specific batch job definition

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobDetail]
            Batch job details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobDetail,
                    parse_obj_as(
                        type_=JobDetail,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteJobResponse]:
        """
        Delete a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteJobResponse]
            Job deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteJobResponse,
                    parse_obj_as(
                        type_=DeleteJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def run_job(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunJobResponse]:
        """
        Execute a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        dry_run : typing.Optional[bool]
            Run job in dry-run mode without making actual changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunJobResponse]
            Job execution started
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}/run",
            method="POST",
            params={
                "dry_run": dry_run,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunJobResponse,
                    parse_obj_as(
                        type_=RunJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def get_job_runs(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        status: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetJobRunsResponse]:
        """
        List all runs for a specific job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        status : typing.Optional[str]
            Filter runs by status

        dry_run : typing.Optional[bool]
            Filter runs by dry run flag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetJobRunsResponse]
            List of job runs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/{encode_path_param(job_uid)}/runs",
            method="GET",
            params={
                "status": status,
                "dry_run": dry_run,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobRunsResponse,
                    parse_obj_as(
                        type_=GetJobRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def get_job_run(
        self,
        project_or_product_uid: str,
        report_uid: str,
        *,
        view: typing.Optional[GetJobRunRequestView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobRun]:
        """
        Get the result of a job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        view : typing.Optional[GetJobRunRequestView]
            Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobRun]
            Job run details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}",
            method="GET",
            params={
                "view": view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobRun,
                    parse_obj_as(
                        type_=JobRun,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete the results of a job run

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def cancel_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelJobRunResponse]:
        """
        Cancel a running job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelJobRunResponse]
            Cancel operation completed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/jobs/runs/{encode_path_param(report_uid)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelJobRunResponse,
                    parse_obj_as(
                        type_=CancelJobRunResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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
