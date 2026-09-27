

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.sibling_discount import SiblingDiscount
from .types.get_sibling_discounts_v3request_active_sibling_filter import GetSiblingDiscountsV3RequestActiveSiblingFilter
from .types.get_sibling_discounts_v3request_sibling_filter import GetSiblingDiscountsV3RequestSiblingFilter
from .types.get_sibling_discounts_v3request_sort_by import GetSiblingDiscountsV3RequestSortBy
from .types.get_sibling_discounts_v3request_status import GetSiblingDiscountsV3RequestStatus
from pydantic import ValidationError


class RawSiblingDiscountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_sibling_discounts_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        status: typing.Optional[GetSiblingDiscountsV3RequestStatus] = None,
        sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter] = None,
        active_sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetSiblingDiscountsV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SiblingDiscount]]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Students from families with siblings and resolved billing-plan discounts.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        status : typing.Optional[GetSiblingDiscountsV3RequestStatus]
            Optional status filter, case-insensitive.

        sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter]
            Optional sibling-family filter, case-insensitive.

        active_sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter]
            Require all siblings to be active, case-insensitive.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetSiblingDiscountsV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SiblingDiscount]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "sibling_discounts",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "status": status,
                "sibling_filter": sibling_filter,
                "active_sibling_filter": active_sibling_filter,
                "has_alerts": has_alerts,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SiblingDiscount],
                    parse_obj_as(
                        type_=typing.List[SiblingDiscount],
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

    def get_sibling_discounts_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SiblingDiscount]:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiblingDiscount]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sibling_discounts/{encode_path_param(student_id)}",
            method="GET",
            params={
                "company_id": company_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiblingDiscount,
                    parse_obj_as(
                        type_=SiblingDiscount,
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawSiblingDiscountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_sibling_discounts_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        status: typing.Optional[GetSiblingDiscountsV3RequestStatus] = None,
        sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter] = None,
        active_sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetSiblingDiscountsV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SiblingDiscount]]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Students from families with siblings and resolved billing-plan discounts.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        status : typing.Optional[GetSiblingDiscountsV3RequestStatus]
            Optional status filter, case-insensitive.

        sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter]
            Optional sibling-family filter, case-insensitive.

        active_sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter]
            Require all siblings to be active, case-insensitive.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetSiblingDiscountsV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SiblingDiscount]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sibling_discounts",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "status": status,
                "sibling_filter": sibling_filter,
                "active_sibling_filter": active_sibling_filter,
                "has_alerts": has_alerts,
                "sort_by": sort_by,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SiblingDiscount],
                    parse_obj_as(
                        type_=typing.List[SiblingDiscount],
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

    async def get_sibling_discounts_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SiblingDiscount]:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiblingDiscount]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sibling_discounts/{encode_path_param(student_id)}",
            method="GET",
            params={
                "company_id": company_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiblingDiscount,
                    parse_obj_as(
                        type_=SiblingDiscount,
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
            if _response.status_code == 404:
                raise NotFoundError(
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
