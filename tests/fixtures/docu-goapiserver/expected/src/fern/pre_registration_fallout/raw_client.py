

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
from ..types.error import Error
from .types.get_pre_registration_fallout_v3request_sort_by import GetPreRegistrationFalloutV3RequestSortBy
from .types.get_pre_registration_fallout_v3request_view import GetPreRegistrationFalloutV3RequestView
from .types.get_pre_registration_fallout_v3response import GetPreRegistrationFalloutV3Response
from pydantic import ValidationError


class RawPreRegistrationFalloutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pre_registration_fallout_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetPreRegistrationFalloutV3RequestView] = None,
        year: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        withdrew_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetPreRegistrationFalloutV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPreRegistrationFalloutV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Omitting view returns a PreRegistrationFalloutReport object containing years, school_summaries and total_summary. view=students returns a paginated array of PreRegistrationFalloutStudent.

        The report accepts only company_id, school_id and view. The students view additionally accepts year, query, withdrew_only, sort_by, page and per_page. Any other parameter, including a students-only parameter on the report view, returns 400. year defaults to the current year; all includes every supported year. Supported years run from 2024 to the current year. Pagination headers are emitted only for view=students.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetPreRegistrationFalloutV3RequestView]
            Omit for the full report; students selects paginated detail.

        year : typing.Optional[str]
            Students view only: a year from 2024 through the current year, or all (case-insensitive). Defaults to the current year.

        query : typing.Optional[str]
            Students view only: student search text.

        withdrew_only : typing.Optional[bool]
            Students view only: restrict to withdrawals in the same year. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetPreRegistrationFalloutV3RequestSortBy]
            Students view only: sort column with _asc/_desc.

        page : typing.Optional[int]
            One-based page number. Applies only to view=students.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Applies only to view=students.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPreRegistrationFalloutV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pre_registration_fallout",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "year": year,
                "query": query,
                "withdrew_only": withdrew_only,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPreRegistrationFalloutV3Response,
                    parse_obj_as(
                        type_=GetPreRegistrationFalloutV3Response,
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


class AsyncRawPreRegistrationFalloutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pre_registration_fallout_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetPreRegistrationFalloutV3RequestView] = None,
        year: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        withdrew_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetPreRegistrationFalloutV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPreRegistrationFalloutV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Omitting view returns a PreRegistrationFalloutReport object containing years, school_summaries and total_summary. view=students returns a paginated array of PreRegistrationFalloutStudent.

        The report accepts only company_id, school_id and view. The students view additionally accepts year, query, withdrew_only, sort_by, page and per_page. Any other parameter, including a students-only parameter on the report view, returns 400. year defaults to the current year; all includes every supported year. Supported years run from 2024 to the current year. Pagination headers are emitted only for view=students.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetPreRegistrationFalloutV3RequestView]
            Omit for the full report; students selects paginated detail.

        year : typing.Optional[str]
            Students view only: a year from 2024 through the current year, or all (case-insensitive). Defaults to the current year.

        query : typing.Optional[str]
            Students view only: student search text.

        withdrew_only : typing.Optional[bool]
            Students view only: restrict to withdrawals in the same year. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetPreRegistrationFalloutV3RequestSortBy]
            Students view only: sort column with _asc/_desc.

        page : typing.Optional[int]
            One-based page number. Applies only to view=students.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Applies only to view=students.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPreRegistrationFalloutV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pre_registration_fallout",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "year": year,
                "query": query,
                "withdrew_only": withdrew_only,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPreRegistrationFalloutV3Response,
                    parse_obj_as(
                        type_=GetPreRegistrationFalloutV3Response,
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
