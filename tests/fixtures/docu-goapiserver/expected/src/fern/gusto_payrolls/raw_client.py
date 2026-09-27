

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
from ..types.error import Error
from ..types.payroll import Payroll
from ..types.payroll_total import PayrollTotal
from pydantic import ValidationError


class RawGustoPayrollsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_gusto_payrolls_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[Payroll]]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. Omitting selectors reads the available payroll records for the school.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[Payroll]]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "gusto_payrolls",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "period": str(period) if period is not None else None,
                "period_from": str(period_from) if period_from is not None else None,
                "period_to": str(period_to) if period_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[Payroll]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[Payroll]],
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

    def get_gusto_payrolls_totals_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[PayrollTotal]]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. When selectors are omitted the totals return the most recent nine periods. Any period selector removes that cap.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[PayrollTotal]]]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "gusto_payrolls/totals",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "period": str(period) if period is not None else None,
                "period_from": str(period_from) if period_from is not None else None,
                "period_to": str(period_to) if period_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[PayrollTotal]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[PayrollTotal]],
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


class AsyncRawGustoPayrollsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_gusto_payrolls_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[Payroll]]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. Omitting selectors reads the available payroll records for the school.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[Payroll]]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "gusto_payrolls",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "period": str(period) if period is not None else None,
                "period_from": str(period_from) if period_from is not None else None,
                "period_to": str(period_to) if period_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[Payroll]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[Payroll]],
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

    async def get_gusto_payrolls_totals_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        period: typing.Optional[dt.date] = None,
        period_from: typing.Optional[dt.date] = None,
        period_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[PayrollTotal]]]:
        """
        Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. When selectors are omitted the totals return the most recent nine periods. Any period selector removes that cap.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        period : typing.Optional[dt.date]
            Exact pay-period end date; mutually exclusive with range bounds.

        period_from : typing.Optional[dt.date]
            Earliest pay-period end date, inclusive.

        period_to : typing.Optional[dt.date]
            Latest pay-period end date, inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[PayrollTotal]]]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "gusto_payrolls/totals",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "period": str(period) if period is not None else None,
                "period_from": str(period_from) if period_from is not None else None,
                "period_to": str(period_to) if period_to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[PayrollTotal]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[PayrollTotal]],
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
