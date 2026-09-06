

import datetime as dt
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
from ..types.api_paged_response_build_system_shared_dto_job_run import ApiPagedResponseBuildSystemSharedDtoJobRun
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_job_run import BuildSystemSharedDtoJobRun
from ..types.build_system_shared_dto_job_run_status import BuildSystemSharedDtoJobRunStatus
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobrunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getjobruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoJobRun]:
        """
        Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoJobRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/jobRuns",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoJobRun,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoJobRun,
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

    def postjobrun(
        self,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on
                    creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/jobRuns",
            method="POST",
            json={
                "ActivityRuns": convert_and_respect_annotation_metadata(
                    object_=activity_runs,
                    annotation=typing.Sequence[BuildSystemSharedDtoActivityRun],
                    direction="write",
                ),
                "EndDate": end_date,
                "JobID": job_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": status,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def getjobrun(
        self,
        job_run_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildSystemSharedDtoJobRun]:
        """
        Gets a JobRun by ID. When successful, the response is the requested JobRun.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The ID of the JobRun to get.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoJobRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id)}",
            method="GET",
            params={
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoJobRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoJobRun,
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

    def putjobrun(
        self,
        job_run_id_: int,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        ///
                    Updates a JobRun.  The body of the PUT is the updated JobRun.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id_ : int
            The id of the JobRun to update

        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id_)}",
            method="PUT",
            json={
                "ActivityRuns": convert_and_respect_annotation_metadata(
                    object_=activity_runs,
                    annotation=typing.Sequence[BuildSystemSharedDtoActivityRun],
                    direction="write",
                ),
                "EndDate": end_date,
                "JobID": job_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletejobrun(
        self, job_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The id of the JobRun to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawJobrunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getjobruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoJobRun]:
        """
        Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoJobRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/jobRuns",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoJobRun,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoJobRun,
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

    async def postjobrun(
        self,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on
                    creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/jobRuns",
            method="POST",
            json={
                "ActivityRuns": convert_and_respect_annotation_metadata(
                    object_=activity_runs,
                    annotation=typing.Sequence[BuildSystemSharedDtoActivityRun],
                    direction="write",
                ),
                "EndDate": end_date,
                "JobID": job_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": status,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def getjobrun(
        self,
        job_run_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildSystemSharedDtoJobRun]:
        """
        Gets a JobRun by ID. When successful, the response is the requested JobRun.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The ID of the JobRun to get.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoJobRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id)}",
            method="GET",
            params={
                "includeActivityRunDetails": include_activity_run_details,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoJobRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoJobRun,
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

    async def putjobrun(
        self,
        job_run_id_: int,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        ///
                    Updates a JobRun.  The body of the PUT is the updated JobRun.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id_ : int
            The id of the JobRun to update

        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id_)}",
            method="PUT",
            json={
                "ActivityRuns": convert_and_respect_annotation_metadata(
                    object_=activity_runs,
                    annotation=typing.Sequence[BuildSystemSharedDtoActivityRun],
                    direction="write",
                ),
                "EndDate": end_date,
                "JobID": job_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletejobrun(
        self, job_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The id of the JobRun to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobRuns/{encode_path_param(job_run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
