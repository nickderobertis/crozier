

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from ..types.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from ..types.retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse
from pydantic import ValidationError


class RawCashDrawersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_cash_drawer_shifts(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCashDrawerShiftsResponse]:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[str]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCashDrawerShiftsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/cash-drawers/shifts",
            method="GET",
            params={
                "location_id": location_id,
                "sort_order": sort_order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCashDrawerShiftsResponse,
                    parse_obj_as(
                        type_=ListCashDrawerShiftsResponse,
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

    def retrieve_cash_drawer_shift(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveCashDrawerShiftResponse]:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveCashDrawerShiftResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{encode_path_param(shift_id)}",
            method="GET",
            params={
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCashDrawerShiftResponse,
                    parse_obj_as(
                        type_=RetrieveCashDrawerShiftResponse,
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

    def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCashDrawerShiftEventsResponse]:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCashDrawerShiftEventsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{encode_path_param(shift_id)}/events",
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
                    ListCashDrawerShiftEventsResponse,
                    parse_obj_as(
                        type_=ListCashDrawerShiftEventsResponse,
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


class AsyncRawCashDrawersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_cash_drawer_shifts(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCashDrawerShiftsResponse]:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[str]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCashDrawerShiftsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/cash-drawers/shifts",
            method="GET",
            params={
                "location_id": location_id,
                "sort_order": sort_order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCashDrawerShiftsResponse,
                    parse_obj_as(
                        type_=ListCashDrawerShiftsResponse,
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

    async def retrieve_cash_drawer_shift(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveCashDrawerShiftResponse]:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveCashDrawerShiftResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{encode_path_param(shift_id)}",
            method="GET",
            params={
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCashDrawerShiftResponse,
                    parse_obj_as(
                        type_=RetrieveCashDrawerShiftResponse,
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

    async def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCashDrawerShiftEventsResponse]:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCashDrawerShiftEventsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{encode_path_param(shift_id)}/events",
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
                    ListCashDrawerShiftEventsResponse,
                    parse_obj_as(
                        type_=ListCashDrawerShiftEventsResponse,
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
