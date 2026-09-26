

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
from ..errors.forbidden_error import ForbiddenError
from ..types.v1report_totals import V1ReportTotals
from .types.filter_reports_request_billed import FilterReportsRequestBilled
from .types.filter_reports_request_scope import FilterReportsRequestScope
from pydantic import ValidationError


class RawReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1ReportTotals]]:
        """
        Retrieve report totals grouped by clients and projects. This endpoint provides aggregated time tracking data including durations, costs, and billing information. The response includes clients with their associated projects and calculated metrics.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1ReportTotals]]
            Report totals retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/reports",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "client_ids": client_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1ReportTotals],
                    parse_obj_as(
                        type_=typing.List[V1ReportTotals],
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

    def filter_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        label_ids: typing.Optional[str] = None,
        team_ids: typing.Optional[str] = None,
        state_ids: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        scope: typing.Optional[FilterReportsRequestScope] = None,
        billed: typing.Optional[FilterReportsRequestBilled] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Filter and retrieve report data with flexible grouping options. Returns aggregated totals grouped by clients, projects, users, labels, days, or teams. Use scope=events to retrieve individual time entries instead of aggregated totals.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        label_ids : typing.Optional[str]
            Comma-separated list of label IDs to filter by

        team_ids : typing.Optional[str]
            Comma-separated list of team IDs to filter by (requires teams feature)

        state_ids : typing.Optional[str]
            Comma-separated list of state IDs to filter by

        group_by : typing.Optional[str]
            Comma-separated list of grouping keys: clients, users, labels, days, teams. Default: all groups

        scope : typing.Optional[FilterReportsRequestScope]
            Result scope: totals (aggregated data) or events (individual entries). Default: totals

        billed : typing.Optional[FilterReportsRequestBilled]
            Filter by billed status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            Report events retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/reports/filter",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "client_ids": client_ids,
                "label_ids": label_ids,
                "team_ids": team_ids,
                "state_ids": state_ids,
                "group_by": group_by,
                "scope": scope,
                "billed": billed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncRawReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1ReportTotals]]:
        """
        Retrieve report totals grouped by clients and projects. This endpoint provides aggregated time tracking data including durations, costs, and billing information. The response includes clients with their associated projects and calculated metrics.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1ReportTotals]]
            Report totals retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/reports",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "client_ids": client_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1ReportTotals],
                    parse_obj_as(
                        type_=typing.List[V1ReportTotals],
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

    async def filter_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        label_ids: typing.Optional[str] = None,
        team_ids: typing.Optional[str] = None,
        state_ids: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        scope: typing.Optional[FilterReportsRequestScope] = None,
        billed: typing.Optional[FilterReportsRequestBilled] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Filter and retrieve report data with flexible grouping options. Returns aggregated totals grouped by clients, projects, users, labels, days, or teams. Use scope=events to retrieve individual time entries instead of aggregated totals.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        label_ids : typing.Optional[str]
            Comma-separated list of label IDs to filter by

        team_ids : typing.Optional[str]
            Comma-separated list of team IDs to filter by (requires teams feature)

        state_ids : typing.Optional[str]
            Comma-separated list of state IDs to filter by

        group_by : typing.Optional[str]
            Comma-separated list of grouping keys: clients, users, labels, days, teams. Default: all groups

        scope : typing.Optional[FilterReportsRequestScope]
            Result scope: totals (aggregated data) or events (individual entries). Default: totals

        billed : typing.Optional[FilterReportsRequestBilled]
            Filter by billed status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            Report events retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/reports/filter",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "client_ids": client_ids,
                "label_ids": label_ids,
                "team_ids": team_ids,
                "state_ids": state_ids,
                "group_by": group_by,
                "scope": scope,
                "billed": billed,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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
