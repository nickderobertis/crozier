

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
from ..types.break_type import BreakType
from ..types.create_break_type_response import CreateBreakTypeResponse
from ..types.create_shift_response import CreateShiftResponse
from ..types.delete_break_type_response import DeleteBreakTypeResponse
from ..types.delete_shift_response import DeleteShiftResponse
from ..types.get_break_type_response import GetBreakTypeResponse
from ..types.get_employee_wage_response import GetEmployeeWageResponse
from ..types.get_shift_response import GetShiftResponse
from ..types.get_team_member_wage_response import GetTeamMemberWageResponse
from ..types.list_break_types_response import ListBreakTypesResponse
from ..types.list_employee_wages_response import ListEmployeeWagesResponse
from ..types.list_team_member_wages_response import ListTeamMemberWagesResponse
from ..types.list_workweek_configs_response import ListWorkweekConfigsResponse
from ..types.search_shifts_response import SearchShiftsResponse
from ..types.shift import Shift
from ..types.shift_query import ShiftQuery
from ..types.update_break_type_response import UpdateBreakTypeResponse
from ..types.update_shift_response import UpdateShiftResponse
from ..types.update_workweek_config_response import UpdateWorkweekConfigResponse
from ..types.workweek_config import WorkweekConfig
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLaborClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_break_types(
        self,
        *,
        location_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListBreakTypesResponse]:
        """
        Returns a paginated list of `BreakType` instances for a business.

        Parameters
        ----------
        location_id : typing.Optional[str]
            Filter the returned `BreakType` results to only those that are associated with the
            specified location.

        limit : typing.Optional[int]
            The maximum number of `BreakType` results to return per page. The number can range between 1
            and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `BreakType` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListBreakTypesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/break-types",
            method="GET",
            params={
                "location_id": location_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBreakTypesResponse,
                    parse_obj_as(
                        type_=ListBreakTypesResponse,
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

    def create_break_type(
        self,
        *,
        break_type: BreakType,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateBreakTypeResponse]:
        """
        Creates a new `BreakType`.

        A `BreakType` is a template for creating `Break` objects.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `break_name`
        - `expected_duration`
        - `is_paid`

        You can only have three `BreakType` instances per location. If you attempt to add a fourth
        `BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
        is returned.

        Parameters
        ----------
        break_type : BreakType

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBreakTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/break-types",
            method="POST",
            json={
                "break_type": convert_and_respect_annotation_metadata(
                    object_=break_type, annotation=BreakType, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateBreakTypeResponse,
                    parse_obj_as(
                        type_=CreateBreakTypeResponse,
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

    def get_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBreakTypeResponse]:
        """
        Returns a single `BreakType` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBreakTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBreakTypeResponse,
                    parse_obj_as(
                        type_=GetBreakTypeResponse,
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

    def update_break_type(
        self, id: str, *, break_type: BreakType, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateBreakTypeResponse]:
        """
        Updates an existing `BreakType`.

        Parameters
        ----------
        id : str
             The UUID for the `BreakType` being updated.

        break_type : BreakType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateBreakTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="PUT",
            json={
                "break_type": convert_and_respect_annotation_metadata(
                    object_=break_type, annotation=BreakType, direction="write"
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
                    UpdateBreakTypeResponse,
                    parse_obj_as(
                        type_=UpdateBreakTypeResponse,
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

    def delete_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteBreakTypeResponse]:
        """
        Deletes an existing `BreakType`.

        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteBreakTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBreakTypeResponse,
                    parse_obj_as(
                        type_=DeleteBreakTypeResponse,
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

    def list_employee_wages(
        self,
        *,
        employee_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListEmployeeWagesResponse]:
        """
        Returns a paginated list of `EmployeeWage` instances for a business.

        Parameters
        ----------
        employee_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the specified employee.

        limit : typing.Optional[int]
            The maximum number of `EmployeeWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEmployeeWagesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/employee-wages",
            method="GET",
            params={
                "employee_id": employee_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmployeeWagesResponse,
                    parse_obj_as(
                        type_=ListEmployeeWagesResponse,
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

    def get_employee_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEmployeeWageResponse]:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEmployeeWageResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/employee-wages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeeWageResponse,
                    parse_obj_as(
                        type_=GetEmployeeWageResponse,
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

    def create_shift(
        self,
        *,
        shift: Shift,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateShiftResponse]:
        """
        Creates a new `Shift`.

        A `Shift` represents a complete workday for a single employee.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `employee_id`
        - `start_at`

        An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
        - The `status` of the new `Shift` is `OPEN` and the employee has another
        shift with an `OPEN` status.
        - The `start_at` date is in the future.
        - The `start_at` or `end_at` date overlaps another shift for the same employee.
        - The `Break` instances are set in the request and a break `start_at`
        is before the `Shift.start_at`, a break `end_at` is after
        the `Shift.end_at`, or both.

        Parameters
        ----------
        shift : Shift

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateShiftResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/shifts",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "shift": convert_and_respect_annotation_metadata(object_=shift, annotation=Shift, direction="write"),
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
                    CreateShiftResponse,
                    parse_obj_as(
                        type_=CreateShiftResponse,
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

    def search_shifts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[ShiftQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchShiftsResponse]:
        """
        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs.
        - Employee IDs.
        - Shift status (`OPEN` and `CLOSED`).
        - Shift start.
        - Shift end.
        - Workday details.

        The list can be sorted by:
        - `start_at`.
        - `end_at`.
        - `created_at`.
        - `updated_at`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            An opaque cursor for fetching the next page.

        limit : typing.Optional[int]
            The number of resources in a page (200 by default).

        query : typing.Optional[ShiftQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchShiftsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/shifts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=ShiftQuery, direction="write"
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
                    SearchShiftsResponse,
                    parse_obj_as(
                        type_=SearchShiftsResponse,
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

    def get_shift(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetShiftResponse]:
        """
        Returns a single `Shift` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetShiftResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetShiftResponse,
                    parse_obj_as(
                        type_=GetShiftResponse,
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

    def update_shift(
        self, id: str, *, shift: Shift, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateShiftResponse]:
        """
        Updates an existing `Shift`.

        When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.

        When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
        set on each `Break`.

        Parameters
        ----------
        id : str
            The ID of the object being updated.

        shift : Shift

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateShiftResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="PUT",
            json={
                "shift": convert_and_respect_annotation_metadata(object_=shift, annotation=Shift, direction="write"),
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
                    UpdateShiftResponse,
                    parse_obj_as(
                        type_=UpdateShiftResponse,
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

    def delete_shift(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteShiftResponse]:
        """
        Deletes a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteShiftResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteShiftResponse,
                    parse_obj_as(
                        type_=DeleteShiftResponse,
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

    def list_team_member_wages(
        self,
        *,
        team_member_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTeamMemberWagesResponse]:
        """
        Returns a paginated list of `TeamMemberWage` instances for a business.

        Parameters
        ----------
        team_member_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the
            specified team member.

        limit : typing.Optional[int]
            The maximum number of `TeamMemberWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTeamMemberWagesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/team-member-wages",
            method="GET",
            params={
                "team_member_id": team_member_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTeamMemberWagesResponse,
                    parse_obj_as(
                        type_=ListTeamMemberWagesResponse,
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

    def get_team_member_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTeamMemberWageResponse]:
        """
        Returns a single `TeamMemberWage` specified by `id `.

        Parameters
        ----------
        id : str
            The UUID for the `TeamMemberWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTeamMemberWageResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/team-member-wages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamMemberWageResponse,
                    parse_obj_as(
                        type_=GetTeamMemberWageResponse,
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

    def list_workweek_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWorkweekConfigsResponse]:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWorkweekConfigsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/labor/workweek-configs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWorkweekConfigsResponse,
                    parse_obj_as(
                        type_=ListWorkweekConfigsResponse,
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

    def update_workweek_config(
        self, id: str, *, workweek_config: WorkweekConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateWorkweekConfigResponse]:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateWorkweekConfigResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/workweek-configs/{encode_path_param(id)}",
            method="PUT",
            json={
                "workweek_config": convert_and_respect_annotation_metadata(
                    object_=workweek_config, annotation=WorkweekConfig, direction="write"
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
                    UpdateWorkweekConfigResponse,
                    parse_obj_as(
                        type_=UpdateWorkweekConfigResponse,
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


class AsyncRawLaborClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_break_types(
        self,
        *,
        location_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListBreakTypesResponse]:
        """
        Returns a paginated list of `BreakType` instances for a business.

        Parameters
        ----------
        location_id : typing.Optional[str]
            Filter the returned `BreakType` results to only those that are associated with the
            specified location.

        limit : typing.Optional[int]
            The maximum number of `BreakType` results to return per page. The number can range between 1
            and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `BreakType` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListBreakTypesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/break-types",
            method="GET",
            params={
                "location_id": location_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBreakTypesResponse,
                    parse_obj_as(
                        type_=ListBreakTypesResponse,
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

    async def create_break_type(
        self,
        *,
        break_type: BreakType,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateBreakTypeResponse]:
        """
        Creates a new `BreakType`.

        A `BreakType` is a template for creating `Break` objects.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `break_name`
        - `expected_duration`
        - `is_paid`

        You can only have three `BreakType` instances per location. If you attempt to add a fourth
        `BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
        is returned.

        Parameters
        ----------
        break_type : BreakType

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBreakTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/break-types",
            method="POST",
            json={
                "break_type": convert_and_respect_annotation_metadata(
                    object_=break_type, annotation=BreakType, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateBreakTypeResponse,
                    parse_obj_as(
                        type_=CreateBreakTypeResponse,
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

    async def get_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBreakTypeResponse]:
        """
        Returns a single `BreakType` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBreakTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBreakTypeResponse,
                    parse_obj_as(
                        type_=GetBreakTypeResponse,
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

    async def update_break_type(
        self, id: str, *, break_type: BreakType, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateBreakTypeResponse]:
        """
        Updates an existing `BreakType`.

        Parameters
        ----------
        id : str
             The UUID for the `BreakType` being updated.

        break_type : BreakType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateBreakTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="PUT",
            json={
                "break_type": convert_and_respect_annotation_metadata(
                    object_=break_type, annotation=BreakType, direction="write"
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
                    UpdateBreakTypeResponse,
                    parse_obj_as(
                        type_=UpdateBreakTypeResponse,
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

    async def delete_break_type(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteBreakTypeResponse]:
        """
        Deletes an existing `BreakType`.

        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `BreakType` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteBreakTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/break-types/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBreakTypeResponse,
                    parse_obj_as(
                        type_=DeleteBreakTypeResponse,
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

    async def list_employee_wages(
        self,
        *,
        employee_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListEmployeeWagesResponse]:
        """
        Returns a paginated list of `EmployeeWage` instances for a business.

        Parameters
        ----------
        employee_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the specified employee.

        limit : typing.Optional[int]
            The maximum number of `EmployeeWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEmployeeWagesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/employee-wages",
            method="GET",
            params={
                "employee_id": employee_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmployeeWagesResponse,
                    parse_obj_as(
                        type_=ListEmployeeWagesResponse,
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

    async def get_employee_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEmployeeWageResponse]:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEmployeeWageResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/employee-wages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeeWageResponse,
                    parse_obj_as(
                        type_=GetEmployeeWageResponse,
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

    async def create_shift(
        self,
        *,
        shift: Shift,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateShiftResponse]:
        """
        Creates a new `Shift`.

        A `Shift` represents a complete workday for a single employee.
        You must provide the following values in your request to this
        endpoint:

        - `location_id`
        - `employee_id`
        - `start_at`

        An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
        - The `status` of the new `Shift` is `OPEN` and the employee has another
        shift with an `OPEN` status.
        - The `start_at` date is in the future.
        - The `start_at` or `end_at` date overlaps another shift for the same employee.
        - The `Break` instances are set in the request and a break `start_at`
        is before the `Shift.start_at`, a break `end_at` is after
        the `Shift.end_at`, or both.

        Parameters
        ----------
        shift : Shift

        idempotency_key : typing.Optional[str]
            A unique string value to ensure the idempotency of the operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateShiftResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/shifts",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "shift": convert_and_respect_annotation_metadata(object_=shift, annotation=Shift, direction="write"),
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
                    CreateShiftResponse,
                    parse_obj_as(
                        type_=CreateShiftResponse,
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

    async def search_shifts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[ShiftQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchShiftsResponse]:
        """
        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs.
        - Employee IDs.
        - Shift status (`OPEN` and `CLOSED`).
        - Shift start.
        - Shift end.
        - Workday details.

        The list can be sorted by:
        - `start_at`.
        - `end_at`.
        - `created_at`.
        - `updated_at`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            An opaque cursor for fetching the next page.

        limit : typing.Optional[int]
            The number of resources in a page (200 by default).

        query : typing.Optional[ShiftQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchShiftsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/shifts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=ShiftQuery, direction="write"
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
                    SearchShiftsResponse,
                    parse_obj_as(
                        type_=SearchShiftsResponse,
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

    async def get_shift(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetShiftResponse]:
        """
        Returns a single `Shift` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetShiftResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetShiftResponse,
                    parse_obj_as(
                        type_=GetShiftResponse,
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

    async def update_shift(
        self, id: str, *, shift: Shift, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateShiftResponse]:
        """
        Updates an existing `Shift`.

        When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.

        When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
        set on each `Break`.

        Parameters
        ----------
        id : str
            The ID of the object being updated.

        shift : Shift

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateShiftResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="PUT",
            json={
                "shift": convert_and_respect_annotation_metadata(object_=shift, annotation=Shift, direction="write"),
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
                    UpdateShiftResponse,
                    parse_obj_as(
                        type_=UpdateShiftResponse,
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

    async def delete_shift(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteShiftResponse]:
        """
        Deletes a `Shift`.

        Parameters
        ----------
        id : str
            The UUID for the `Shift` being deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteShiftResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/shifts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteShiftResponse,
                    parse_obj_as(
                        type_=DeleteShiftResponse,
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

    async def list_team_member_wages(
        self,
        *,
        team_member_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTeamMemberWagesResponse]:
        """
        Returns a paginated list of `TeamMemberWage` instances for a business.

        Parameters
        ----------
        team_member_id : typing.Optional[str]
            Filter the returned wages to only those that are associated with the
            specified team member.

        limit : typing.Optional[int]
            The maximum number of `TeamMemberWage` results to return per page. The number can range between
            1 and 200. The default is 200.

        cursor : typing.Optional[str]
            A pointer to the next page of `EmployeeWage` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTeamMemberWagesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/team-member-wages",
            method="GET",
            params={
                "team_member_id": team_member_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTeamMemberWagesResponse,
                    parse_obj_as(
                        type_=ListTeamMemberWagesResponse,
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

    async def get_team_member_wage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTeamMemberWageResponse]:
        """
        Returns a single `TeamMemberWage` specified by `id `.

        Parameters
        ----------
        id : str
            The UUID for the `TeamMemberWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTeamMemberWageResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/team-member-wages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTeamMemberWageResponse,
                    parse_obj_as(
                        type_=GetTeamMemberWageResponse,
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

    async def list_workweek_configs(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWorkweekConfigsResponse]:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWorkweekConfigsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/labor/workweek-configs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWorkweekConfigsResponse,
                    parse_obj_as(
                        type_=ListWorkweekConfigsResponse,
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

    async def update_workweek_config(
        self, id: str, *, workweek_config: WorkweekConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateWorkweekConfigResponse]:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateWorkweekConfigResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/workweek-configs/{encode_path_param(id)}",
            method="PUT",
            json={
                "workweek_config": convert_and_respect_annotation_metadata(
                    object_=workweek_config, annotation=WorkweekConfig, direction="write"
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
                    UpdateWorkweekConfigResponse,
                    parse_obj_as(
                        type_=UpdateWorkweekConfigResponse,
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
