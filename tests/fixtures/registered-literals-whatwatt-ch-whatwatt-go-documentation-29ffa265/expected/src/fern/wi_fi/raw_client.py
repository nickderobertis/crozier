

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.get_wifi_sta_settings_response import GetWifiStaSettingsResponse
from .types.replace_wifi_sta_settings_response import ReplaceWifiStaSettingsResponse
from .types.scan_wifi_response_item import ScanWifiResponseItem
from .types.update_wifi_sta_settings_response import UpdateWifiStaSettingsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWiFiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def scan_wifi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ScanWifiResponseItem]]:
        """
        Performs a scan and returns visible access points with RSSI and channel information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ScanWifiResponseItem]]
            Array of detected networks
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/wifi/scan",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScanWifiResponseItem],
                    parse_obj_as(
                        type_=typing.List[ScanWifiResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def get_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWifiStaSettingsResponse]:
        """
        Reads the STA (client) configuration. Changes apply without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWifiStaSettingsResponse]
            Current station settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=GetWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def replace_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReplaceWifiStaSettingsResponse]:
        """
        Replaces the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplaceWifiStaSettingsResponse]
            Replaced settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="POST",
            json={
                "enable": enable,
                "name": name,
                "password": password,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
                "max_power": max_power,
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
                    ReplaceWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def update_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWifiStaSettingsResponse]:
        """
        Partially updates the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateWifiStaSettingsResponse]
            Updated settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="PUT",
            json={
                "enable": enable,
                "name": name,
                "password": password,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
                "max_power": max_power,
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
                    UpdateWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=UpdateWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def delete_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Clears the STA (client) configuration and disables the client.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawWiFiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def scan_wifi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ScanWifiResponseItem]]:
        """
        Performs a scan and returns visible access points with RSSI and channel information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ScanWifiResponseItem]]
            Array of detected networks
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/wifi/scan",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScanWifiResponseItem],
                    parse_obj_as(
                        type_=typing.List[ScanWifiResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def get_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWifiStaSettingsResponse]:
        """
        Reads the STA (client) configuration. Changes apply without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWifiStaSettingsResponse]
            Current station settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=GetWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def replace_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReplaceWifiStaSettingsResponse]:
        """
        Replaces the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplaceWifiStaSettingsResponse]
            Replaced settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="POST",
            json={
                "enable": enable,
                "name": name,
                "password": password,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
                "max_power": max_power,
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
                    ReplaceWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def update_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateWifiStaSettingsResponse]:
        """
        Partially updates the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateWifiStaSettingsResponse]
            Updated settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="PUT",
            json={
                "enable": enable,
                "name": name,
                "password": password,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
                "max_power": max_power,
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
                    UpdateWifiStaSettingsResponse,
                    parse_obj_as(
                        type_=UpdateWifiStaSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def delete_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Clears the STA (client) configuration and disables the client.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/wifi/sta/settings",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
