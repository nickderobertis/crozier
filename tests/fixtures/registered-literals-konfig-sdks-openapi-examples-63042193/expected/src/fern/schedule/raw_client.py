

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
from ..types.schedule_create_new_schedule_response import ScheduleCreateNewScheduleResponse
from ..types.schedule_get_all_schedules_response import ScheduleGetAllSchedulesResponse
from ..types.schedule_get_by_id_response import ScheduleGetByIdResponse
from ..types.schedule_remove_by_id_response import ScheduleRemoveByIdResponse
from ..types.schedule_update_schedule_response import ScheduleUpdateScheduleResponse
from .types.schedule_create_new_schedule_request_attribution_actor import (
    ScheduleCreateNewScheduleRequestAttributionActor,
)
from .types.schedule_create_new_schedule_request_parameters_value import ScheduleCreateNewScheduleRequestParametersValue
from .types.schedule_create_new_schedule_request_timetable import ScheduleCreateNewScheduleRequestTimetable
from .types.schedule_update_schedule_request_attribution_actor import ScheduleUpdateScheduleRequestAttributionActor
from .types.schedule_update_schedule_request_parameters_value import ScheduleUpdateScheduleRequestParametersValue
from .types.schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScheduleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getallschedules(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleGetAllSchedulesResponse]:
        """
        Returns all schedules for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleGetAllSchedulesResponse]
            A sequence of schedules.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/schedule",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleGetAllSchedulesResponse,
                    parse_obj_as(
                        type_=ScheduleGetAllSchedulesResponse,
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

    def createnewschedule(
        self,
        project_slug: str,
        *,
        parameters: typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
        name: str,
        timetable: ScheduleCreateNewScheduleRequestTimetable,
        attribution_actor: ScheduleCreateNewScheduleRequestAttributionActor,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleCreateNewScheduleResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : str
            Name of the schedule.

        timetable : ScheduleCreateNewScheduleRequestTimetable
            Timetable that specifies when a schedule triggers.

        attribution_actor : ScheduleCreateNewScheduleRequestAttributionActor
            The attribution-actor of the scheduled pipeline.

        description : typing.Optional[str]
            Description of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleCreateNewScheduleResponse]
            A schedule object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/schedule",
            method="POST",
            json={
                "description": description,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
                    direction="write",
                ),
                "name": name,
                "timetable": convert_and_respect_annotation_metadata(
                    object_=timetable, annotation=ScheduleCreateNewScheduleRequestTimetable, direction="write"
                ),
                "attribution-actor": attribution_actor,
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
                    ScheduleCreateNewScheduleResponse,
                    parse_obj_as(
                        type_=ScheduleCreateNewScheduleResponse,
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

    def getbyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ScheduleGetByIdResponse]:
        """
        Get a schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleGetByIdResponse]
            A schedule object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleGetByIdResponse,
                    parse_obj_as(
                        type_=ScheduleGetByIdResponse,
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

    def removebyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ScheduleRemoveByIdResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleRemoveByIdResponse]
            A confirmation message.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleRemoveByIdResponse,
                    parse_obj_as(
                        type_=ScheduleRemoveByIdResponse,
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

    def updateschedule(
        self,
        schedule_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]] = OMIT,
        name: typing.Optional[str] = OMIT,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = OMIT,
        attribution_actor: typing.Optional[ScheduleUpdateScheduleRequestAttributionActor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleUpdateScheduleResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        description : typing.Optional[str]
            Description of the schedule.

        parameters : typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : typing.Optional[str]
            Name of the schedule.

        timetable : typing.Optional[ScheduleUpdateScheduleRequestTimetable]
            Timetable that specifies when a schedule triggers.

        attribution_actor : typing.Optional[ScheduleUpdateScheduleRequestAttributionActor]
            The attribution-actor of the scheduled pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleUpdateScheduleResponse]
            A schedule object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="PATCH",
            json={
                "description": description,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue],
                    direction="write",
                ),
                "name": name,
                "timetable": convert_and_respect_annotation_metadata(
                    object_=timetable, annotation=ScheduleUpdateScheduleRequestTimetable, direction="write"
                ),
                "attribution-actor": attribution_actor,
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
                    ScheduleUpdateScheduleResponse,
                    parse_obj_as(
                        type_=ScheduleUpdateScheduleResponse,
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


class AsyncRawScheduleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getallschedules(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleGetAllSchedulesResponse]:
        """
        Returns all schedules for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleGetAllSchedulesResponse]
            A sequence of schedules.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/schedule",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleGetAllSchedulesResponse,
                    parse_obj_as(
                        type_=ScheduleGetAllSchedulesResponse,
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

    async def createnewschedule(
        self,
        project_slug: str,
        *,
        parameters: typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
        name: str,
        timetable: ScheduleCreateNewScheduleRequestTimetable,
        attribution_actor: ScheduleCreateNewScheduleRequestAttributionActor,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleCreateNewScheduleResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : str
            Name of the schedule.

        timetable : ScheduleCreateNewScheduleRequestTimetable
            Timetable that specifies when a schedule triggers.

        attribution_actor : ScheduleCreateNewScheduleRequestAttributionActor
            The attribution-actor of the scheduled pipeline.

        description : typing.Optional[str]
            Description of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleCreateNewScheduleResponse]
            A schedule object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/schedule",
            method="POST",
            json={
                "description": description,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
                    direction="write",
                ),
                "name": name,
                "timetable": convert_and_respect_annotation_metadata(
                    object_=timetable, annotation=ScheduleCreateNewScheduleRequestTimetable, direction="write"
                ),
                "attribution-actor": attribution_actor,
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
                    ScheduleCreateNewScheduleResponse,
                    parse_obj_as(
                        type_=ScheduleCreateNewScheduleResponse,
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

    async def getbyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ScheduleGetByIdResponse]:
        """
        Get a schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleGetByIdResponse]
            A schedule object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleGetByIdResponse,
                    parse_obj_as(
                        type_=ScheduleGetByIdResponse,
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

    async def removebyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ScheduleRemoveByIdResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleRemoveByIdResponse]
            A confirmation message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleRemoveByIdResponse,
                    parse_obj_as(
                        type_=ScheduleRemoveByIdResponse,
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

    async def updateschedule(
        self,
        schedule_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]] = OMIT,
        name: typing.Optional[str] = OMIT,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = OMIT,
        attribution_actor: typing.Optional[ScheduleUpdateScheduleRequestAttributionActor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleUpdateScheduleResponse]:
        """
        Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        description : typing.Optional[str]
            Description of the schedule.

        parameters : typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : typing.Optional[str]
            Name of the schedule.

        timetable : typing.Optional[ScheduleUpdateScheduleRequestTimetable]
            Timetable that specifies when a schedule triggers.

        attribution_actor : typing.Optional[ScheduleUpdateScheduleRequestAttributionActor]
            The attribution-actor of the scheduled pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleUpdateScheduleResponse]
            A schedule object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schedule/{encode_path_param(schedule_id)}",
            method="PATCH",
            json={
                "description": description,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue],
                    direction="write",
                ),
                "name": name,
                "timetable": convert_and_respect_annotation_metadata(
                    object_=timetable, annotation=ScheduleUpdateScheduleRequestTimetable, direction="write"
                ),
                "attribution-actor": attribution_actor,
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
                    ScheduleUpdateScheduleResponse,
                    parse_obj_as(
                        type_=ScheduleUpdateScheduleResponse,
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
