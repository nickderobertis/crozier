

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_reference_api_touch_provider200response import CoreReferenceApiTouchProvider200Response
from ..types.provisioning_api_groups_get_sub_admins_of_group200response import (
    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
)
from ..types.weather_status_weather_status_get_forecast200response import (
    WeatherStatusWeatherStatusGetForecast200Response,
)
from ..types.weather_status_weather_status_get_location200response import (
    WeatherStatusWeatherStatusGetLocation200Response,
)
from ..types.weather_status_weather_status_use_personal_address200response import (
    WeatherStatusWeatherStatusUsePersonalAddress200Response,
)
from pydantic import ValidationError


class RawWeatherStatusWeatherStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_mode(
        self, *, mode: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        mode : int
            New mode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/mode",
            method="PUT",
            params={
                "mode": mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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

    def use_personal_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/use-personal",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusUsePersonalAddress200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusUsePersonalAddress200Response,
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

    def get_location(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WeatherStatusWeatherStatusGetLocation200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WeatherStatusWeatherStatusGetLocation200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/location",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusGetLocation200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusGetLocation200Response,
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

    def set_location(
        self,
        *,
        address: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lon: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]:
        """
        Parameters
        ----------
        address : typing.Optional[str]
            Any approximative or exact address

        lat : typing.Optional[float]
            Latitude in decimal degree format

        lon : typing.Optional[float]
            Longitude in decimal degree format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/location",
            method="PUT",
            params={
                "address": address,
                "lat": lat,
                "lon": lon,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusUsePersonalAddress200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusUsePersonalAddress200Response,
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

    def get_forecast(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WeatherStatusWeatherStatusGetForecast200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WeatherStatusWeatherStatusGetForecast200Response]
            Forecast returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/forecast",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusGetForecast200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusGetForecast200Response,
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

    def get_favorites(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/favorites",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
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

    def set_favorites(
        self, *, favorites: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        favorites : str
            Favorite addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/favorites",
            method="PUT",
            params={
                "favorites": favorites,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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


class AsyncRawWeatherStatusWeatherStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_mode(
        self, *, mode: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        mode : int
            New mode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/mode",
            method="PUT",
            params={
                "mode": mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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

    async def use_personal_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/use-personal",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusUsePersonalAddress200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusUsePersonalAddress200Response,
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

    async def get_location(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WeatherStatusWeatherStatusGetLocation200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WeatherStatusWeatherStatusGetLocation200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/location",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusGetLocation200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusGetLocation200Response,
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

    async def set_location(
        self,
        *,
        address: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lon: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]:
        """
        Parameters
        ----------
        address : typing.Optional[str]
            Any approximative or exact address

        lat : typing.Optional[float]
            Latitude in decimal degree format

        lon : typing.Optional[float]
            Longitude in decimal degree format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WeatherStatusWeatherStatusUsePersonalAddress200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/location",
            method="PUT",
            params={
                "address": address,
                "lat": lat,
                "lon": lon,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusUsePersonalAddress200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusUsePersonalAddress200Response,
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

    async def get_forecast(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WeatherStatusWeatherStatusGetForecast200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WeatherStatusWeatherStatusGetForecast200Response]
            Forecast returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/forecast",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeatherStatusWeatherStatusGetForecast200Response,
                    parse_obj_as(
                        type_=WeatherStatusWeatherStatusGetForecast200Response,
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

    async def get_favorites(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/favorites",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
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

    async def set_favorites(
        self, *, favorites: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]:
        """
        Parameters
        ----------
        favorites : str
            Favorite addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreReferenceApiTouchProvider200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/weather_status/api/v1/favorites",
            method="PUT",
            params={
                "favorites": favorites,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreReferenceApiTouchProvider200Response,
                    parse_obj_as(
                        type_=CoreReferenceApiTouchProvider200Response,
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
