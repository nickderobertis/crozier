

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
from .types.get_enrollments_v3request_group_by import GetEnrollmentsV3RequestGroupBy
from .types.get_enrollments_v3request_view import GetEnrollmentsV3RequestView
from .types.get_enrollments_v3response import GetEnrollmentsV3Response
from pydantic import ValidationError


class RawEnrollmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_enrollments_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetEnrollmentsV3RequestView] = None,
        group_by: typing.Optional[GetEnrollmentsV3RequestGroupBy] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        year_from: typing.Optional[str] = None,
        year_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetEnrollmentsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The response representation is selected in this order:

        | Selection | Response | Date selectors |
        | --- | --- | --- |
        | view=trend | EnrollmentTrend array | Optional period_from/period_to |
        | group_by=period (unless trend) | EnrollmentPeriodAnalytics array | year_from/year_to |
        | view=analytics, group_by=month | EnrollmentAnalytics array | period_from/period_to |
        | Default: view=basic, group_by=month | EnrollmentMonthly array | period_from/period_to |

        Monthly basic/analytics default to 2023-01 through the current month. Period analytics defaults to 2023 through the current year. Trend uses the available calculated periods when bounds are omitted. No pagination is implemented. Each representation returns its row count in X-Total-Count. For view=trend, omit both range bounds or provide both; endpoints must lie within the available horizon. Incomplete, invalid, inverted or out-of-horizon trend ranges fail in the data layer and currently return HTTP 500.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetEnrollmentsV3RequestView]
            Select the representation.

        group_by : typing.Optional[GetEnrollmentsV3RequestGroupBy]
            period implies period analytics unless view=trend.

        period_from : typing.Optional[str]
            First monthly period for monthly or trend views.

        period_to : typing.Optional[str]
            Last monthly period for monthly or trend views.

        year_from : typing.Optional[str]
            First year for group_by=period; defaults to 2023.

        year_to : typing.Optional[str]
            Last year for group_by=period; defaults to the current year.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEnrollmentsV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "enrollments",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "group_by": group_by,
                "period_from": period_from,
                "period_to": period_to,
                "year_from": year_from,
                "year_to": year_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEnrollmentsV3Response,
                    parse_obj_as(
                        type_=GetEnrollmentsV3Response,
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


class AsyncRawEnrollmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_enrollments_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        view: typing.Optional[GetEnrollmentsV3RequestView] = None,
        group_by: typing.Optional[GetEnrollmentsV3RequestGroupBy] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        year_from: typing.Optional[str] = None,
        year_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetEnrollmentsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The response representation is selected in this order:

        | Selection | Response | Date selectors |
        | --- | --- | --- |
        | view=trend | EnrollmentTrend array | Optional period_from/period_to |
        | group_by=period (unless trend) | EnrollmentPeriodAnalytics array | year_from/year_to |
        | view=analytics, group_by=month | EnrollmentAnalytics array | period_from/period_to |
        | Default: view=basic, group_by=month | EnrollmentMonthly array | period_from/period_to |

        Monthly basic/analytics default to 2023-01 through the current month. Period analytics defaults to 2023 through the current year. Trend uses the available calculated periods when bounds are omitted. No pagination is implemented. Each representation returns its row count in X-Total-Count. For view=trend, omit both range bounds or provide both; endpoints must lie within the available horizon. Incomplete, invalid, inverted or out-of-horizon trend ranges fail in the data layer and currently return HTTP 500.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        view : typing.Optional[GetEnrollmentsV3RequestView]
            Select the representation.

        group_by : typing.Optional[GetEnrollmentsV3RequestGroupBy]
            period implies period analytics unless view=trend.

        period_from : typing.Optional[str]
            First monthly period for monthly or trend views.

        period_to : typing.Optional[str]
            Last monthly period for monthly or trend views.

        year_from : typing.Optional[str]
            First year for group_by=period; defaults to 2023.

        year_to : typing.Optional[str]
            Last year for group_by=period; defaults to the current year.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEnrollmentsV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "enrollments",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "group_by": group_by,
                "period_from": period_from,
                "period_to": period_to,
                "year_from": year_from,
                "year_to": year_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEnrollmentsV3Response,
                    parse_obj_as(
                        type_=GetEnrollmentsV3Response,
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
