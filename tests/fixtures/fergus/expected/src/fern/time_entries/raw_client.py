

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.time_entries_response import TimeEntriesResponse
from .types.get_time_entries_request_sort_field import GetTimeEntriesRequestSortField
from .types.get_time_entries_request_sort_order import GetTimeEntriesRequestSortOrder
from pydantic import ValidationError


class RawTimeEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_time_entries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetTimeEntriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetTimeEntriesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        filter_locked_only: typing.Optional[bool] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_no: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_date_from: typing.Optional[dt.date] = None,
        filter_date_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TimeEntriesResponse]:
        """
        Get all time entries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetTimeEntriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetTimeEntriesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `user`
            - `employee's username`
            - `jobPhaseTitle`,
            - `jobPhaseDetails`

        filter_locked_only : typing.Optional[bool]

        filter_user_id : typing.Optional[float]
            The user id to filter time entries by

        filter_job_no : typing.Optional[float]
            The job no to filter time entries by

        filter_job_phase_id : typing.Optional[float]
            The job phase id to filter time entries by

        filter_date_from : typing.Optional[dt.date]
            The start date in yyyy-mm-dd format

        filter_date_to : typing.Optional[dt.date]
            The end date in yyyy-mm-dd format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TimeEntriesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "timeEntries",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "filterLockedOnly": filter_locked_only,
                "filterUserId": filter_user_id,
                "filterJobNo": filter_job_no,
                "filterJobPhaseId": filter_job_phase_id,
                "filterDateFrom": str(filter_date_from) if filter_date_from is not None else None,
                "filterDateTo": str(filter_date_to) if filter_date_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimeEntriesResponse,
                    parse_obj_as(
                        type_=TimeEntriesResponse,
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


class AsyncRawTimeEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_time_entries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetTimeEntriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetTimeEntriesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        filter_locked_only: typing.Optional[bool] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_no: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_date_from: typing.Optional[dt.date] = None,
        filter_date_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TimeEntriesResponse]:
        """
        Get all time entries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetTimeEntriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetTimeEntriesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `user`
            - `employee's username`
            - `jobPhaseTitle`,
            - `jobPhaseDetails`

        filter_locked_only : typing.Optional[bool]

        filter_user_id : typing.Optional[float]
            The user id to filter time entries by

        filter_job_no : typing.Optional[float]
            The job no to filter time entries by

        filter_job_phase_id : typing.Optional[float]
            The job phase id to filter time entries by

        filter_date_from : typing.Optional[dt.date]
            The start date in yyyy-mm-dd format

        filter_date_to : typing.Optional[dt.date]
            The end date in yyyy-mm-dd format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TimeEntriesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "timeEntries",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "filterLockedOnly": filter_locked_only,
                "filterUserId": filter_user_id,
                "filterJobNo": filter_job_no,
                "filterJobPhaseId": filter_job_phase_id,
                "filterDateFrom": str(filter_date_from) if filter_date_from is not None else None,
                "filterDateTo": str(filter_date_to) if filter_date_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimeEntriesResponse,
                    parse_obj_as(
                        type_=TimeEntriesResponse,
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
