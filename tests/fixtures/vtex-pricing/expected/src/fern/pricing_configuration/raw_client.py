

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.pricing_configuration import PricingConfiguration
from .types.get_pricingv2status_response import GetPricingv2StatusResponse
from pydantic import ValidationError


class RawPricingConfigurationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pricing_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PricingConfiguration]:
        """
        Retrieves Pricing Configuration.
        ## Response body example

        ```json
        {
            "hasMigrated": true,
            "migrationStatus": "Completed",
            "defaultMarkup": 100,
            "priceVariation": {
                "upperLimit": null,
                "lowerLimit": null
            },
            "minimumMarkups": {
                "1": 100,
                "2": 90
            },
            "tradePolicyConfigs": [],
            "sellersToOverride": [],
            "hasPriceInheritance": false,
            "priceInheritance": "never",
            "hasOptionalBasePrice": false,
            "blockAccount": false,
            "blockedRoutes": null,
            "priceTableSelectionStrategy": "first",
            "priceTableLimit": null
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PricingConfiguration]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricing/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PricingConfiguration,
                    parse_obj_as(
                        type_=PricingConfiguration,
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

    def get_pricingv2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPricingv2StatusResponse]:
        """
        Retrieves Pricing v2 Status.
        ## Response body example

        ```json
        {
            "isActive": true,
            "hasMigrated": true
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricingv2StatusResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricing/migration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingv2StatusResponse,
                    parse_obj_as(
                        type_=GetPricingv2StatusResponse,
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


class AsyncRawPricingConfigurationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pricing_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PricingConfiguration]:
        """
        Retrieves Pricing Configuration.
        ## Response body example

        ```json
        {
            "hasMigrated": true,
            "migrationStatus": "Completed",
            "defaultMarkup": 100,
            "priceVariation": {
                "upperLimit": null,
                "lowerLimit": null
            },
            "minimumMarkups": {
                "1": 100,
                "2": 90
            },
            "tradePolicyConfigs": [],
            "sellersToOverride": [],
            "hasPriceInheritance": false,
            "priceInheritance": "never",
            "hasOptionalBasePrice": false,
            "blockAccount": false,
            "blockedRoutes": null,
            "priceTableSelectionStrategy": "first",
            "priceTableLimit": null
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PricingConfiguration]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricing/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PricingConfiguration,
                    parse_obj_as(
                        type_=PricingConfiguration,
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

    async def get_pricingv2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPricingv2StatusResponse]:
        """
        Retrieves Pricing v2 Status.
        ## Response body example

        ```json
        {
            "isActive": true,
            "hasMigrated": true
        }
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricingv2StatusResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricing/migration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingv2StatusResponse,
                    parse_obj_as(
                        type_=GetPricingv2StatusResponse,
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
