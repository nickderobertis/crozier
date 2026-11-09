

import contextlib
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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.all_server_jobs import AllServerJobs
from ..types.analysis import Analysis
from ..types.get_job_statistics import GetJobStatistics
from ..types.get_scheduler_option import GetSchedulerOption
from ..types.info import Info
from ..types.job import Job
from ..types.license_decider import LicenseDecider
from ..types.reuser import Reuser
from ..types.scancode import Scancode
from ..types.show_job import ShowJob
from .types.get_all_jobs_request_sort import GetAllJobsRequestSort
from .types.get_all_jobs_request_status import GetAllJobsRequestStatus
from .types.get_jobs_request_sort import GetJobsRequestSort
from .types.get_jobs_request_status import GetJobsRequestStatus
from .types.get_reports_by_upload_request_report_format import GetReportsByUploadRequestReportFormat
from .types.get_scheduler_options_by_operation_request_operation_name import (
    GetSchedulerOptionsByOperationRequestOperationName,
)
from .types.handle_scheduler_run_request_operation import HandleSchedulerRunRequestOperation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jobs(
        self,
        *,
        sort: typing.Optional[GetJobsRequestSort] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        upload: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Job]]:
        """
        Returns all jobs with their status created by the logged in user

        Parameters
        ----------
        sort : typing.Optional[GetJobsRequestSort]

        status : typing.Optional[GetJobsRequestStatus]
            Returns only jobs with the selected status.

        upload : typing.Optional[int]
            Return jobs for the given upload id only

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Job]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "sort": sort,
                "status": status,
                "upload": upload,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    def start_jobs(
        self,
        *,
        folder_id: int,
        upload_id: int,
        group_name: typing.Optional[str] = None,
        analysis: typing.Optional[Analysis] = OMIT,
        decider: typing.Optional[LicenseDecider] = OMIT,
        reuse: typing.Optional[Reuser] = OMIT,
        scancode: typing.Optional[Scancode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Schedule an Analysis of an existing upload

        Parameters
        ----------
        folder_id : int

        upload_id : int

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        analysis : typing.Optional[Analysis]

        decider : typing.Optional[LicenseDecider]

        reuse : typing.Optional[Reuser]

        scancode : typing.Optional[Scancode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Job Scheduled with job id in message
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "analysis": convert_and_respect_annotation_metadata(
                    object_=analysis, annotation=Analysis, direction="write"
                ),
                "decider": convert_and_respect_annotation_metadata(
                    object_=decider, annotation=LicenseDecider, direction="write"
                ),
                "reuse": convert_and_respect_annotation_metadata(object_=reuse, annotation=Reuser, direction="write"),
                "scancode": convert_and_respect_annotation_metadata(
                    object_=scancode, annotation=Scancode, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "uploadId": str(upload_id) if upload_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    def get_all_jobs(
        self,
        *,
        status: typing.Optional[GetAllJobsRequestStatus] = None,
        sort: typing.Optional[GetAllJobsRequestSort] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Job]]:
        """
        Returns all jobs with their status created by every user. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        status : typing.Optional[GetAllJobsRequestStatus]
            Returns only jobs with the selected status.

        sort : typing.Optional[GetAllJobsRequestSort]

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Job]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/all",
            method="GET",
            params={
                "status": status,
                "sort": sort,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_scheduler_options_by_operation(
        self,
        operation_name: GetSchedulerOptionsByOperationRequestOperationName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSchedulerOption]:
        """
        Returns the scheduler options for a specific operation

        Parameters
        ----------
        operation_name : GetSchedulerOptionsByOperationRequestOperationName
            Name of the operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSchedulerOption]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/scheduler/operation/{encode_path_param(operation_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchedulerOption,
                    parse_obj_as(
                        type_=GetSchedulerOption,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def handle_scheduler_run(
        self,
        *,
        job: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        operation: typing.Optional[HandleSchedulerRunRequestOperation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Run the scheduler with the selected options from a specific operation

        Parameters
        ----------
        job : typing.Optional[str]
            Name of the selected job

        level : typing.Optional[str]
            Level of the selected verbose

        priority : typing.Optional[str]
            Priority option selected

        operation : typing.Optional[HandleSchedulerRunRequestOperation]
            Operation to be run by the scheduler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Scheduler run successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/scheduler/operation/run",
            method="POST",
            params={
                "job": job,
                "level": level,
                "priority": priority,
            },
            json={
                "operation": operation,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_job_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Job]:
        """
        Returns job with the status

        Parameters
        ----------
        id : int
            Id of the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    def get_jobs_history_per_upload(
        self, *, upload: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ShowJob]]:
        """
        Returns the history of all the jobs queued based on an upload

        Parameters
        ----------
        upload : int
            Return jobs for the given upload id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ShowJob]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/history",
            method="GET",
            params={
                "upload": upload,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShowJob],
                    parse_obj_as(
                        type_=typing.List[ShowJob],
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_job_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetJobStatistics]]:
        """
        Returns the statistics of all the jobs for the Admin Dashboard

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetJobStatistics]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/dashboard/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetJobStatistics],
                    parse_obj_as(
                        type_=typing.List[GetJobStatistics],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_all_server_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AllServerJobs]:
        """
        Returns all jobs with the scheduler status for the Admin Dashboard. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AllServerJobs]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/dashboard",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AllServerJobs,
                    parse_obj_as(
                        type_=AllServerJobs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
        self, id: int, queue: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes a job queue and all the other job queues depending on it

        Parameters
        ----------
        id : int
            Id of the Job

        queue : int
            Id of the job queue to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Job deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/{encode_path_param(queue)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_reports_by_upload(
        self,
        *,
        upload_id: int,
        report_format: GetReportsByUploadRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        List all reports available for a given upload

        Parameters
        ----------
        upload_id : int
            Id of the upload to generate the report for

        report_format : GetReportsByUploadRequestReportFormat
            Which report to be genereated

        group_name : typing.Optional[str]
            The group name to chose while generating a report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Report generation is scheduled. Link to download report will be in message
        """
        _response = self._client_wrapper.httpx_client.request(
            "report",
            method="GET",
            headers={
                "uploadId": str(upload_id) if upload_id is not None else None,
                "reportFormat": str(report_format) if report_format is not None else None,
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    @contextlib.contextmanager
    def get_report_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Get a report by id

        Parameters
        ----------
        id : int
            Id the report to download

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Required report
        """
        with self._client_wrapper.httpx_client.stream(
            f"report/{encode_path_param(id)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jobs(
        self,
        *,
        sort: typing.Optional[GetJobsRequestSort] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        upload: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Job]]:
        """
        Returns all jobs with their status created by the logged in user

        Parameters
        ----------
        sort : typing.Optional[GetJobsRequestSort]

        status : typing.Optional[GetJobsRequestStatus]
            Returns only jobs with the selected status.

        upload : typing.Optional[int]
            Return jobs for the given upload id only

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Job]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "sort": sort,
                "status": status,
                "upload": upload,
            },
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    async def start_jobs(
        self,
        *,
        folder_id: int,
        upload_id: int,
        group_name: typing.Optional[str] = None,
        analysis: typing.Optional[Analysis] = OMIT,
        decider: typing.Optional[LicenseDecider] = OMIT,
        reuse: typing.Optional[Reuser] = OMIT,
        scancode: typing.Optional[Scancode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Schedule an Analysis of an existing upload

        Parameters
        ----------
        folder_id : int

        upload_id : int

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        analysis : typing.Optional[Analysis]

        decider : typing.Optional[LicenseDecider]

        reuse : typing.Optional[Reuser]

        scancode : typing.Optional[Scancode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Job Scheduled with job id in message
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "analysis": convert_and_respect_annotation_metadata(
                    object_=analysis, annotation=Analysis, direction="write"
                ),
                "decider": convert_and_respect_annotation_metadata(
                    object_=decider, annotation=LicenseDecider, direction="write"
                ),
                "reuse": convert_and_respect_annotation_metadata(object_=reuse, annotation=Reuser, direction="write"),
                "scancode": convert_and_respect_annotation_metadata(
                    object_=scancode, annotation=Scancode, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "groupName": str(group_name) if group_name is not None else None,
                "folderId": str(folder_id) if folder_id is not None else None,
                "uploadId": str(upload_id) if upload_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    async def get_all_jobs(
        self,
        *,
        status: typing.Optional[GetAllJobsRequestStatus] = None,
        sort: typing.Optional[GetAllJobsRequestSort] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Job]]:
        """
        Returns all jobs with their status created by every user. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        status : typing.Optional[GetAllJobsRequestStatus]
            Returns only jobs with the selected status.

        sort : typing.Optional[GetAllJobsRequestSort]

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Job]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/all",
            method="GET",
            params={
                "status": status,
                "sort": sort,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_scheduler_options_by_operation(
        self,
        operation_name: GetSchedulerOptionsByOperationRequestOperationName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSchedulerOption]:
        """
        Returns the scheduler options for a specific operation

        Parameters
        ----------
        operation_name : GetSchedulerOptionsByOperationRequestOperationName
            Name of the operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSchedulerOption]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/scheduler/operation/{encode_path_param(operation_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchedulerOption,
                    parse_obj_as(
                        type_=GetSchedulerOption,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def handle_scheduler_run(
        self,
        *,
        job: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        operation: typing.Optional[HandleSchedulerRunRequestOperation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Run the scheduler with the selected options from a specific operation

        Parameters
        ----------
        job : typing.Optional[str]
            Name of the selected job

        level : typing.Optional[str]
            Level of the selected verbose

        priority : typing.Optional[str]
            Priority option selected

        operation : typing.Optional[HandleSchedulerRunRequestOperation]
            Operation to be run by the scheduler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Scheduler run successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/scheduler/operation/run",
            method="POST",
            params={
                "job": job,
                "level": level,
                "priority": priority,
            },
            json={
                "operation": operation,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_job_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Job]:
        """
        Returns job with the status

        Parameters
        ----------
        id : int
            Id of the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    async def get_jobs_history_per_upload(
        self, *, upload: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ShowJob]]:
        """
        Returns the history of all the jobs queued based on an upload

        Parameters
        ----------
        upload : int
            Return jobs for the given upload id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ShowJob]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/history",
            method="GET",
            params={
                "upload": upload,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShowJob],
                    parse_obj_as(
                        type_=typing.List[ShowJob],
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_job_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetJobStatistics]]:
        """
        Returns the statistics of all the jobs for the Admin Dashboard

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetJobStatistics]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/dashboard/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetJobStatistics],
                    parse_obj_as(
                        type_=typing.List[GetJobStatistics],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_all_server_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AllServerJobs]:
        """
        Returns all jobs with the scheduler status for the Admin Dashboard. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AllServerJobs]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/dashboard",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AllServerJobs,
                    parse_obj_as(
                        type_=AllServerJobs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
        self, id: int, queue: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes a job queue and all the other job queues depending on it

        Parameters
        ----------
        id : int
            Id of the Job

        queue : int
            Id of the job queue to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Job deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/{encode_path_param(queue)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_reports_by_upload(
        self,
        *,
        upload_id: int,
        report_format: GetReportsByUploadRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        List all reports available for a given upload

        Parameters
        ----------
        upload_id : int
            Id of the upload to generate the report for

        report_format : GetReportsByUploadRequestReportFormat
            Which report to be genereated

        group_name : typing.Optional[str]
            The group name to chose while generating a report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Report generation is scheduled. Link to download report will be in message
        """
        _response = await self._client_wrapper.httpx_client.request(
            "report",
            method="GET",
            headers={
                "uploadId": str(upload_id) if upload_id is not None else None,
                "reportFormat": str(report_format) if report_format is not None else None,
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    @contextlib.asynccontextmanager
    async def get_report_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Get a report by id

        Parameters
        ----------
        id : int
            Id the report to download

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Required report
        """
        async with self._client_wrapper.httpx_client.stream(
            f"report/{encode_path_param(id)}",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
