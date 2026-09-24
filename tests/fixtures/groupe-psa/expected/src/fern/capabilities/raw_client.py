

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.vehicle_capabilities import VehicleCapabilities
from ..types.vehicle_extension_type_item import VehicleExtensionTypeItem
from pydantic import ValidationError


class RawCapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_vehicles_capabilities(
        self,
        vin: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VehicleCapabilities]:
        """
        Returns vehicle'scharacteristics & capabilities

        Parameters
        ----------
        vin : str
            Results will only be related to this Vehicle Identification Number.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VehicleCapabilities]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vehicles/{encode_path_param(vin)}",
            method="GET",
            params={
                "locale": locale,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VehicleCapabilities,
                    parse_obj_as(
                        type_=VehicleCapabilities,
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


class AsyncRawCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_vehicles_capabilities(
        self,
        vin: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VehicleCapabilities]:
        """
        Returns vehicle'scharacteristics & capabilities

        Parameters
        ----------
        vin : str
            Results will only be related to this Vehicle Identification Number.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VehicleCapabilities]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vehicles/{encode_path_param(vin)}",
            method="GET",
            params={
                "locale": locale,
                "extension": extension,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VehicleCapabilities,
                    parse_obj_as(
                        type_=VehicleCapabilities,
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
