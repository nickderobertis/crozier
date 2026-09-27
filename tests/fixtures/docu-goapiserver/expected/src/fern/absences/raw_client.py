

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.absence import Absence
from ..types.error import Error
from .types.get_absences_v3request_sort_by import GetAbsencesV3RequestSortBy
from pydantic import ValidationError


class RawAbsencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_absences_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        student_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        sort_by: typing.Optional[GetAbsencesV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Absence]]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide school_id or student_id; student_id takes precedence when both are supplied (both IDs are still validated). Provide date_from, optionally date_to (defaults to today), OR a positive last_n_days. last_n_days cannot be combined with either date bound. Default order is date descending.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        student_id : typing.Optional[str]
            Required when school_id is omitted; takes precedence over school_id.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        last_n_days : typing.Optional[int]
            Rolling date window; mutually exclusive with explicit dates.

        sort_by : typing.Optional[GetAbsencesV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Absence]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "absences",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "student_id": student_id,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Absence],
                    parse_obj_as(
                        type_=typing.List[Absence],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawAbsencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_absences_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        student_id: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        sort_by: typing.Optional[GetAbsencesV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Absence]]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide school_id or student_id; student_id takes precedence when both are supplied (both IDs are still validated). Provide date_from, optionally date_to (defaults to today), OR a positive last_n_days. last_n_days cannot be combined with either date bound. Default order is date descending.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        student_id : typing.Optional[str]
            Required when school_id is omitted; takes precedence over school_id.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.

        last_n_days : typing.Optional[int]
            Rolling date window; mutually exclusive with explicit dates.

        sort_by : typing.Optional[GetAbsencesV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Absence]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "absences",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "student_id": student_id,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Absence],
                    parse_obj_as(
                        type_=typing.List[Absence],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
