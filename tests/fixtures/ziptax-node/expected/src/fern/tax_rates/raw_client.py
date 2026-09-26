

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_model import ErrorModel
from ..types.v60response import V60Response
from .types.get_tax_rates_v60request_adjustment import GetTaxRatesV60RequestAdjustment
from .types.get_tax_rates_v60request_country_code import GetTaxRatesV60RequestCountryCode
from .types.get_tax_rates_v60request_format import GetTaxRatesV60RequestFormat
from pydantic import ValidationError


class RawTaxRatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_tax_rates_v60(
        self,
        *,
        key: typing.Optional[str] = None,
        format: typing.Optional[GetTaxRatesV60RequestFormat] = None,
        country_code: typing.Optional[GetTaxRatesV60RequestCountryCode] = None,
        postalcode: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        county: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lng: typing.Optional[float] = None,
        adjustment: typing.Optional[GetTaxRatesV60RequestAdjustment] = None,
        sat_item_total: typing.Optional[float] = None,
        historical: typing.Optional[str] = None,
        taxability_code: typing.Optional[str] = None,
        address_detail_extended: typing.Optional[bool] = None,
        shipping_extended: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V60Response]:
        """
        Returns tax rates in a new structured format with separate base rates,
                    service/shipping taxability, and tax summaries. Built on v5.0 data but with enhanced organization. Note: postal-code-only lookups (no address or lat/lng) return the legacy v5.0-style response body (version, rCode, results) rather than the structured object documented here.

        Parameters
        ----------
        key : typing.Optional[str]
            API key that authenticates the request and resolves the account's plan, entitlements, and rate limits. Supply it either as this query parameter or the X-API-KEY request header. A missing, malformed, or unknown key returns response code 101.

        format : typing.Optional[GetTaxRatesV60RequestFormat]
            Serialization format of the response body. 'json' (default) returns a JSON object; 'xml' returns the same data as an XML document.

        country_code : typing.Optional[GetTaxRatesV60RequestCountryCode]
            Country of the lookup: 'USA' (default), 'CAN', or a US territory (ASM, GUM, MNP, PRI, VIR). 'CAN' requires the Canadian rates (rate_loc_can) entitlement; otherwise the request returns response code 112. US territories are looked up via the USA path and require no additional entitlement.

        postalcode : typing.Optional[str]
            5-digit US ZIP code to look up. When supplied on its own the response may contain rates for multiple overlapping jurisdictions. An invalid format returns response code 104.

        address : typing.Optional[str]
            Street address to geocode to a single rooftop-level jurisdiction. Geocoding requires the geo_enabled entitlement; an incomplete or ungeocodable address returns response code 109.

        state : typing.Optional[str]
            State name or two-letter abbreviation. Used with city or postal code to disambiguate the location. An invalid format returns response code 102.

        state_code : typing.Optional[str]
            Two-letter state code (e.g. CA). Alternative to 'state' for supplying the state as a code rather than a name.

        city : typing.Optional[str]
            City name used together with state to narrow the lookup when no street address is supplied. An invalid format returns response code 103.

        county : typing.Optional[str]
            County name used to refine the lookup when supplied without a street address.

        lat : typing.Optional[float]
            Latitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).

        lng : typing.Optional[float]
            Longitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).

        adjustment : typing.Optional[GetTaxRatesV60RequestAdjustment]
            Sourcing/unincorporated-area handling. Defaults to 'auto', which applies the appropriate sourcing adjustment on geo (address) lookups in unincorporated areas. The values 'origin' and 'destination' are accepted but currently do not change the resolved result.

        sat_item_total : typing.Optional[float]
            Single-article item total in dollars, used for Tennessee Single Article Tax (SAT) calculation on TN address lookups. Note: the v6.0 response does not currently return a SAT breakdown object; the SAT detail (satTaxDetail) is available in the v5.0 response.

        historical : typing.Optional[str]
            Historical period to price the lookup against, formatted YYYYMM (6 digits, e.g. 202401). Returns the rates that were in effect for that month. Requires historical data to be enabled; an invalid format returns response code 111.

        taxability_code : typing.Optional[str]
            Product Taxability Information Code (TIC). When supplied, the response includes a productDetail object describing the rate rules that apply to that product category in the resolved jurisdiction. Accepts numeric standard TIC codes (e.g., 20010) or alphanumeric override codes (e.g., CIR00001). Requires the product_rates entitlement for standard codes.

        address_detail_extended : typing.Optional[bool]
            When true, returns a full geocoding object in the response broken into address parts (street, city, postal code, etc.). Defaults to false.

        shipping_extended : typing.Optional[bool]
            When true, returns a detailed shipping object to help navigate collection complexity. The GENERAL_RULE value will be one of: EXEMPT, EXEMPT_WHEN_SEPARATELY_STATED, ITEM_SPECIFIC, CONDITIONAL, or TAXABLE. For EXEMPT_WHEN_SEPARATELY_STATED, the response includes a boolean flag, and a natural-language description is included for clarity. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V60Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "request/v60",
            method="GET",
            params={
                "key": key,
                "format": format,
                "countryCode": country_code,
                "postalcode": postalcode,
                "address": address,
                "state": state,
                "stateCode": state_code,
                "city": city,
                "county": county,
                "lat": lat,
                "lng": lng,
                "adjustment": adjustment,
                "sat_item_total": sat_item_total,
                "historical": historical,
                "taxabilityCode": taxability_code,
                "addressDetailExtended": address_detail_extended,
                "shippingExtended": shipping_extended,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V60Response,
                    parse_obj_as(
                        type_=V60Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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


class AsyncRawTaxRatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_tax_rates_v60(
        self,
        *,
        key: typing.Optional[str] = None,
        format: typing.Optional[GetTaxRatesV60RequestFormat] = None,
        country_code: typing.Optional[GetTaxRatesV60RequestCountryCode] = None,
        postalcode: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        state_code: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        county: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lng: typing.Optional[float] = None,
        adjustment: typing.Optional[GetTaxRatesV60RequestAdjustment] = None,
        sat_item_total: typing.Optional[float] = None,
        historical: typing.Optional[str] = None,
        taxability_code: typing.Optional[str] = None,
        address_detail_extended: typing.Optional[bool] = None,
        shipping_extended: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V60Response]:
        """
        Returns tax rates in a new structured format with separate base rates,
                    service/shipping taxability, and tax summaries. Built on v5.0 data but with enhanced organization. Note: postal-code-only lookups (no address or lat/lng) return the legacy v5.0-style response body (version, rCode, results) rather than the structured object documented here.

        Parameters
        ----------
        key : typing.Optional[str]
            API key that authenticates the request and resolves the account's plan, entitlements, and rate limits. Supply it either as this query parameter or the X-API-KEY request header. A missing, malformed, or unknown key returns response code 101.

        format : typing.Optional[GetTaxRatesV60RequestFormat]
            Serialization format of the response body. 'json' (default) returns a JSON object; 'xml' returns the same data as an XML document.

        country_code : typing.Optional[GetTaxRatesV60RequestCountryCode]
            Country of the lookup: 'USA' (default), 'CAN', or a US territory (ASM, GUM, MNP, PRI, VIR). 'CAN' requires the Canadian rates (rate_loc_can) entitlement; otherwise the request returns response code 112. US territories are looked up via the USA path and require no additional entitlement.

        postalcode : typing.Optional[str]
            5-digit US ZIP code to look up. When supplied on its own the response may contain rates for multiple overlapping jurisdictions. An invalid format returns response code 104.

        address : typing.Optional[str]
            Street address to geocode to a single rooftop-level jurisdiction. Geocoding requires the geo_enabled entitlement; an incomplete or ungeocodable address returns response code 109.

        state : typing.Optional[str]
            State name or two-letter abbreviation. Used with city or postal code to disambiguate the location. An invalid format returns response code 102.

        state_code : typing.Optional[str]
            Two-letter state code (e.g. CA). Alternative to 'state' for supplying the state as a code rather than a name.

        city : typing.Optional[str]
            City name used together with state to narrow the lookup when no street address is supplied. An invalid format returns response code 103.

        county : typing.Optional[str]
            County name used to refine the lookup when supplied without a street address.

        lat : typing.Optional[float]
            Latitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).

        lng : typing.Optional[float]
            Longitude of a geographic point. When both lat and lng are supplied the API resolves the single jurisdiction containing that point (coordinate lookup).

        adjustment : typing.Optional[GetTaxRatesV60RequestAdjustment]
            Sourcing/unincorporated-area handling. Defaults to 'auto', which applies the appropriate sourcing adjustment on geo (address) lookups in unincorporated areas. The values 'origin' and 'destination' are accepted but currently do not change the resolved result.

        sat_item_total : typing.Optional[float]
            Single-article item total in dollars, used for Tennessee Single Article Tax (SAT) calculation on TN address lookups. Note: the v6.0 response does not currently return a SAT breakdown object; the SAT detail (satTaxDetail) is available in the v5.0 response.

        historical : typing.Optional[str]
            Historical period to price the lookup against, formatted YYYYMM (6 digits, e.g. 202401). Returns the rates that were in effect for that month. Requires historical data to be enabled; an invalid format returns response code 111.

        taxability_code : typing.Optional[str]
            Product Taxability Information Code (TIC). When supplied, the response includes a productDetail object describing the rate rules that apply to that product category in the resolved jurisdiction. Accepts numeric standard TIC codes (e.g., 20010) or alphanumeric override codes (e.g., CIR00001). Requires the product_rates entitlement for standard codes.

        address_detail_extended : typing.Optional[bool]
            When true, returns a full geocoding object in the response broken into address parts (street, city, postal code, etc.). Defaults to false.

        shipping_extended : typing.Optional[bool]
            When true, returns a detailed shipping object to help navigate collection complexity. The GENERAL_RULE value will be one of: EXEMPT, EXEMPT_WHEN_SEPARATELY_STATED, ITEM_SPECIFIC, CONDITIONAL, or TAXABLE. For EXEMPT_WHEN_SEPARATELY_STATED, the response includes a boolean flag, and a natural-language description is included for clarity. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V60Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "request/v60",
            method="GET",
            params={
                "key": key,
                "format": format,
                "countryCode": country_code,
                "postalcode": postalcode,
                "address": address,
                "state": state,
                "stateCode": state_code,
                "city": city,
                "county": county,
                "lat": lat,
                "lng": lng,
                "adjustment": adjustment,
                "sat_item_total": sat_item_total,
                "historical": historical,
                "taxabilityCode": taxability_code,
                "addressDetailExtended": address_detail_extended,
                "shippingExtended": shipping_extended,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V60Response,
                    parse_obj_as(
                        type_=V60Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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
