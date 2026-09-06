

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
from ..types.api_paged_response_build_system_shared_dto_activity_run import (
    ApiPagedResponseBuildSystemSharedDtoActivityRun,
)
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_activity_run_status import BuildSystemSharedDtoActivityRunStatus
from ..types.build_system_shared_dto_activity_run_status_status import BuildSystemSharedDtoActivityRunStatusStatus
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from .types.activity_runs_get_activity_runs_request_status import ActivityRunsGetActivityRunsRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawActivityrunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getactivityruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ActivityRunsGetActivityRunsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoActivityRun]:
        """
        Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        status : typing.Optional[ActivityRunsGetActivityRunsRequestStatus]
            Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.
                        If not specified, the default status filter is “InProgress”.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoActivityRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/activityRuns",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoActivityRun,
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

    def getactivityrun(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoActivityRun]:
        """
        Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
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

    def putactivityrun(
        self,
        activity_run_id_: int,
        *,
        status: BuildSystemSharedDtoActivityRunStatus,
        activity_run_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_activity_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id_ : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        status : BuildSystemSharedDtoActivityRunStatus
            The status of this ActivityRun

        activity_run_id : typing.Optional[int]
            The identifier for the ActivityRun

        end_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity completed

        job_activity_id : typing.Optional[int]
            Read Only. The ID of the Job Activity that defines this activity run

        job_run_id : typing.Optional[int]
            Read Only. The ID of the JobRun under which this ActivityRun is executing

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.

        start_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity started

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id_)}",
            method="PUT",
            json={
                "ActivityRunID": activity_run_id,
                "EndDate": end_date,
                "JobActivityID": job_activity_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoActivityRunStatus, direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getactivityrunstatus(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoActivityRunStatus]:
        """
        Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get ActivityRunStatus for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoActivityRunStatus]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRunStatus,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRunStatus,
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

    def putactivityrunstatus(
        self,
        activity_run_id: int,
        *,
        current_step: typing.Optional[int] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus] = OMIT,
        step_progress: typing.Optional[int] = OMIT,
        step_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        current_step : typing.Optional[int]
            The activity step currently executing, indicated by numeric order

        status : typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus]
            The status of the ActivityRun

        step_progress : typing.Optional[int]
            The percent progress from the currently executing step.  This value shall be null if progress is not available

        step_status : typing.Optional[str]
            The status text from the currently executing step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}/status",
            method="PUT",
            json={
                "CurrentStep": current_step,
                "Status": status,
                "StepProgress": step_progress,
                "StepStatus": step_status,
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


class AsyncRawActivityrunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getactivityruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ActivityRunsGetActivityRunsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoActivityRun]:
        """
        Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        status : typing.Optional[ActivityRunsGetActivityRunsRequestStatus]
            Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.
                        If not specified, the default status filter is “InProgress”.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoActivityRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/activityRuns",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoActivityRun,
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

    async def getactivityrun(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoActivityRun]:
        """
        Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
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

    async def putactivityrun(
        self,
        activity_run_id_: int,
        *,
        status: BuildSystemSharedDtoActivityRunStatus,
        activity_run_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_activity_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id_ : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        status : BuildSystemSharedDtoActivityRunStatus
            The status of this ActivityRun

        activity_run_id : typing.Optional[int]
            The identifier for the ActivityRun

        end_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity completed

        job_activity_id : typing.Optional[int]
            Read Only. The ID of the Job Activity that defines this activity run

        job_run_id : typing.Optional[int]
            Read Only. The ID of the JobRun under which this ActivityRun is executing

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.

        start_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity started

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id_)}",
            method="PUT",
            json={
                "ActivityRunID": activity_run_id,
                "EndDate": end_date,
                "JobActivityID": job_activity_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoActivityRunStatus, direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getactivityrunstatus(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoActivityRunStatus]:
        """
        Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get ActivityRunStatus for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoActivityRunStatus]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRunStatus,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRunStatus,
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

    async def putactivityrunstatus(
        self,
        activity_run_id: int,
        *,
        current_step: typing.Optional[int] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus] = OMIT,
        step_progress: typing.Optional[int] = OMIT,
        step_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        current_step : typing.Optional[int]
            The activity step currently executing, indicated by numeric order

        status : typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus]
            The status of the ActivityRun

        step_progress : typing.Optional[int]
            The percent progress from the currently executing step.  This value shall be null if progress is not available

        step_status : typing.Optional[str]
            The status text from the currently executing step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activityRuns/{encode_path_param(activity_run_id)}/status",
            method="PUT",
            json={
                "CurrentStep": current_step,
                "Status": status,
                "StepProgress": step_progress,
                "StepStatus": step_status,
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
