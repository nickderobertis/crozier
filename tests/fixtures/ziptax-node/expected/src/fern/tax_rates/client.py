

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v60response import V60Response
from .raw_client import AsyncRawTaxRatesClient, RawTaxRatesClient
from .types.get_tax_rates_v60request_adjustment import GetTaxRatesV60RequestAdjustment
from .types.get_tax_rates_v60request_country_code import GetTaxRatesV60RequestCountryCode
from .types.get_tax_rates_v60request_format import GetTaxRatesV60RequestFormat


class TaxRatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaxRatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaxRatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaxRatesClient
        """
        return self._raw_client

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
    ) -> V60Response:
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
        V60Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.get_tax_rates_v60(
            key="your-api-key",
            taxability_code="20010",
        )
        """
        _response = self._raw_client.get_tax_rates_v60(
            key=key,
            format=format,
            country_code=country_code,
            postalcode=postalcode,
            address=address,
            state=state,
            state_code=state_code,
            city=city,
            county=county,
            lat=lat,
            lng=lng,
            adjustment=adjustment,
            sat_item_total=sat_item_total,
            historical=historical,
            taxability_code=taxability_code,
            address_detail_extended=address_detail_extended,
            shipping_extended=shipping_extended,
            request_options=request_options,
        )
        return _response.data


class AsyncTaxRatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaxRatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaxRatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaxRatesClient
        """
        return self._raw_client

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
    ) -> V60Response:
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
        V60Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.get_tax_rates_v60(
                key="your-api-key",
                taxability_code="20010",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tax_rates_v60(
            key=key,
            format=format,
            country_code=country_code,
            postalcode=postalcode,
            address=address,
            state=state,
            state_code=state_code,
            city=city,
            county=county,
            lat=lat,
            lng=lng,
            adjustment=adjustment,
            sat_item_total=sat_item_total,
            historical=historical,
            taxability_code=taxability_code,
            address_detail_extended=address_detail_extended,
            shipping_extended=shipping_extended,
            request_options=request_options,
        )
        return _response.data
