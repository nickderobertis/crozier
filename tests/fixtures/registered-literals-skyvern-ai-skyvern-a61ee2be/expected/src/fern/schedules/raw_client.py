

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.delete_schedule_response import DeleteScheduleResponse
from ..types.organization_schedule_list_response import OrganizationScheduleListResponse
from ..types.workflow_schedule_list_response import WorkflowScheduleListResponse
from ..types.workflow_schedule_response import WorkflowScheduleResponse
from .types.schedules_list_all_request_status import SchedulesListAllRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSchedulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[SchedulesListAllRequestStatus] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OrganizationScheduleListResponse]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        status : typing.Optional[SchedulesListAllRequestStatus]
            Filter by status: 'active' or 'paused'

        search : typing.Optional[str]
            Search by workflow title or schedule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OrganizationScheduleListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/schedules",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationScheduleListResponse,
                    parse_obj_as(
                        type_=OrganizationScheduleListResponse,
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

    def list(
        self, workflow_permanent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowScheduleListResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleListResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleListResponse,
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

    def create(
        self,
        workflow_permanent_id: str,
        *,
        timezone: str,
        cron_expression: typing.Optional[str] = OMIT,
        interval_seconds: typing.Optional[int] = OMIT,
        first_fire_at: typing.Optional[dt.datetime] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowScheduleResponse]:
        """
        Create a cron or fixed-interval schedule that runs the given agent automatically with a fixed set of parameters. An interval schedule first runs at first_fire_at, or one interval after creation. Returns the stored schedule and its next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        timezone : str

        cron_expression : typing.Optional[str]

        interval_seconds : typing.Optional[int]
            Fixed elapsed interval between runs, in seconds. Mutually exclusive with cron_expression.

        first_fire_at : typing.Optional[dt.datetime]
            First run of an interval schedule; later runs follow every interval_seconds from it. Must be in the future when changed. Defaults to one interval after creation.

        enabled : typing.Optional[bool]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules",
            method="POST",
            json={
                "cron_expression": cron_expression,
                "interval_seconds": interval_seconds,
                "first_fire_at": first_fire_at,
                "timezone": timezone,
                "enabled": enabled,
                "parameters": parameters,
                "name": name,
                "description": description,
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
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    def get(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowScheduleResponse]:
        """
        Fetch one schedule belonging to an agent. Returns the schedule's cron expression or interval, timezone, parameters, enabled state, and next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    def update(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        timezone: str,
        cron_expression: typing.Optional[str] = OMIT,
        interval_seconds: typing.Optional[int] = OMIT,
        first_fire_at: typing.Optional[dt.datetime] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowScheduleResponse]:
        """
        Replace a schedule's cron expression or interval, timezone, run parameters, and enabled state. Returns the updated schedule and its next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        timezone : str

        cron_expression : typing.Optional[str]

        interval_seconds : typing.Optional[int]
            Fixed elapsed interval between runs, in seconds. Mutually exclusive with cron_expression.

        first_fire_at : typing.Optional[dt.datetime]
            First run of an interval schedule; later runs follow every interval_seconds from it. Must be in the future when changed. Defaults to one interval after creation.

        enabled : typing.Optional[bool]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="PUT",
            json={
                "cron_expression": cron_expression,
                "interval_seconds": interval_seconds,
                "first_fire_at": first_fire_at,
                "timezone": timezone,
                "enabled": enabled,
                "parameters": parameters,
                "name": name,
                "description": description,
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
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    def delete(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteScheduleResponse,
                    parse_obj_as(
                        type_=DeleteScheduleResponse,
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

    def enable(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}/enable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    def disable(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkflowScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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


class AsyncRawSchedulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[SchedulesListAllRequestStatus] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OrganizationScheduleListResponse]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        status : typing.Optional[SchedulesListAllRequestStatus]
            Filter by status: 'active' or 'paused'

        search : typing.Optional[str]
            Search by workflow title or schedule name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OrganizationScheduleListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/schedules",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationScheduleListResponse,
                    parse_obj_as(
                        type_=OrganizationScheduleListResponse,
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

    async def list(
        self, workflow_permanent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowScheduleListResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleListResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleListResponse,
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

    async def create(
        self,
        workflow_permanent_id: str,
        *,
        timezone: str,
        cron_expression: typing.Optional[str] = OMIT,
        interval_seconds: typing.Optional[int] = OMIT,
        first_fire_at: typing.Optional[dt.datetime] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowScheduleResponse]:
        """
        Create a cron or fixed-interval schedule that runs the given agent automatically with a fixed set of parameters. An interval schedule first runs at first_fire_at, or one interval after creation. Returns the stored schedule and its next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        timezone : str

        cron_expression : typing.Optional[str]

        interval_seconds : typing.Optional[int]
            Fixed elapsed interval between runs, in seconds. Mutually exclusive with cron_expression.

        first_fire_at : typing.Optional[dt.datetime]
            First run of an interval schedule; later runs follow every interval_seconds from it. Must be in the future when changed. Defaults to one interval after creation.

        enabled : typing.Optional[bool]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules",
            method="POST",
            json={
                "cron_expression": cron_expression,
                "interval_seconds": interval_seconds,
                "first_fire_at": first_fire_at,
                "timezone": timezone,
                "enabled": enabled,
                "parameters": parameters,
                "name": name,
                "description": description,
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
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    async def get(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowScheduleResponse]:
        """
        Fetch one schedule belonging to an agent. Returns the schedule's cron expression or interval, timezone, parameters, enabled state, and next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    async def update(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        timezone: str,
        cron_expression: typing.Optional[str] = OMIT,
        interval_seconds: typing.Optional[int] = OMIT,
        first_fire_at: typing.Optional[dt.datetime] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowScheduleResponse]:
        """
        Replace a schedule's cron expression or interval, timezone, run parameters, and enabled state. Returns the updated schedule and its next upcoming run times.

        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        timezone : str

        cron_expression : typing.Optional[str]

        interval_seconds : typing.Optional[int]
            Fixed elapsed interval between runs, in seconds. Mutually exclusive with cron_expression.

        first_fire_at : typing.Optional[dt.datetime]
            First run of an interval schedule; later runs follow every interval_seconds from it. Must be in the future when changed. Defaults to one interval after creation.

        enabled : typing.Optional[bool]

        parameters : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="PUT",
            json={
                "cron_expression": cron_expression,
                "interval_seconds": interval_seconds,
                "first_fire_at": first_fire_at,
                "timezone": timezone,
                "enabled": enabled,
                "parameters": parameters,
                "name": name,
                "description": description,
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
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    async def delete(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteScheduleResponse,
                    parse_obj_as(
                        type_=DeleteScheduleResponse,
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

    async def enable(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}/enable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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

    async def disable(
        self,
        workflow_permanent_id: str,
        workflow_schedule_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkflowScheduleResponse]:
        """
        Parameters
        ----------
        workflow_permanent_id : str

        workflow_schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowScheduleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(workflow_permanent_id)}/schedules/{encode_path_param(workflow_schedule_id)}/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowScheduleResponse,
                    parse_obj_as(
                        type_=WorkflowScheduleResponse,
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
