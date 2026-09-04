

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.background_checks_response import BackgroundChecksResponse
from ..types.basic_customer_data import BasicCustomerData
from ..types.comprehensive_check_response import ComprehensiveCheckResponse
from .types.background_checks_request_check_types_item import BackgroundChecksRequestCheckTypesItem
from .types.background_checks_request_risk_profile import BackgroundChecksRequestRiskProfile
from .types.comprehensive_check_request_check_types_item import ComprehensiveCheckRequestCheckTypesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBackgroundChecksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def perform_background_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[BackgroundChecksRequestCheckTypesItem],
        customer_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        baseline_date: typing.Optional[dt.datetime] = OMIT,
        risk_profile: typing.Optional[BackgroundChecksRequestRiskProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BackgroundChecksResponse]:
        """
        Führt spezifische Background Checks (Sanctions, PEP, etc.) durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[BackgroundChecksRequestCheckTypesItem]

        customer_data : typing.Optional[typing.Dict[str, typing.Any]]

        baseline_date : typing.Optional[dt.datetime]
            Datum für inkrementelle Updates

        risk_profile : typing.Optional[BackgroundChecksRequestRiskProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BackgroundChecksResponse]
            Background Checks erfolgreich durchgeführt
        """
        _response = self._client_wrapper.httpx_client.request(
            "checks/perform",
            method="POST",
            json={
                "customerId": customer_id,
                "customerData": customer_data,
                "checkTypes": check_types,
                "baselineDate": baseline_date,
                "riskProfile": risk_profile,
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
                    BackgroundChecksResponse,
                    parse_obj_as(
                        type_=BackgroundChecksResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def perform_comprehensive_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[ComprehensiveCheckRequestCheckTypesItem],
        customer_data: typing.Optional[BasicCustomerData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ComprehensiveCheckResponse]:
        """
        Führt KYC, AML, PEP und andere regulatorische Checks durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[ComprehensiveCheckRequestCheckTypesItem]

        customer_data : typing.Optional[BasicCustomerData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComprehensiveCheckResponse]
            Checks erfolgreich durchgeführt
        """
        _response = self._client_wrapper.httpx_client.request(
            "checks/comprehensive",
            method="POST",
            json={
                "customerId": customer_id,
                "customerData": convert_and_respect_annotation_metadata(
                    object_=customer_data, annotation=BasicCustomerData, direction="write"
                ),
                "checkTypes": check_types,
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
                    ComprehensiveCheckResponse,
                    parse_obj_as(
                        type_=ComprehensiveCheckResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBackgroundChecksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def perform_background_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[BackgroundChecksRequestCheckTypesItem],
        customer_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        baseline_date: typing.Optional[dt.datetime] = OMIT,
        risk_profile: typing.Optional[BackgroundChecksRequestRiskProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BackgroundChecksResponse]:
        """
        Führt spezifische Background Checks (Sanctions, PEP, etc.) durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[BackgroundChecksRequestCheckTypesItem]

        customer_data : typing.Optional[typing.Dict[str, typing.Any]]

        baseline_date : typing.Optional[dt.datetime]
            Datum für inkrementelle Updates

        risk_profile : typing.Optional[BackgroundChecksRequestRiskProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BackgroundChecksResponse]
            Background Checks erfolgreich durchgeführt
        """
        _response = await self._client_wrapper.httpx_client.request(
            "checks/perform",
            method="POST",
            json={
                "customerId": customer_id,
                "customerData": customer_data,
                "checkTypes": check_types,
                "baselineDate": baseline_date,
                "riskProfile": risk_profile,
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
                    BackgroundChecksResponse,
                    parse_obj_as(
                        type_=BackgroundChecksResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def perform_comprehensive_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[ComprehensiveCheckRequestCheckTypesItem],
        customer_data: typing.Optional[BasicCustomerData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ComprehensiveCheckResponse]:
        """
        Führt KYC, AML, PEP und andere regulatorische Checks durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[ComprehensiveCheckRequestCheckTypesItem]

        customer_data : typing.Optional[BasicCustomerData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComprehensiveCheckResponse]
            Checks erfolgreich durchgeführt
        """
        _response = await self._client_wrapper.httpx_client.request(
            "checks/comprehensive",
            method="POST",
            json={
                "customerId": customer_id,
                "customerData": convert_and_respect_annotation_metadata(
                    object_=customer_data, annotation=BasicCustomerData, direction="write"
                ),
                "checkTypes": check_types,
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
                    ComprehensiveCheckResponse,
                    parse_obj_as(
                        type_=ComprehensiveCheckResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
