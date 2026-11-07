

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
from .types.get_ethernet_settings_response import GetEthernetSettingsResponse
from .types.replace_ethernet_settings_response import ReplaceEthernetSettingsResponse
from .types.update_ethernet_settings_response import UpdateEthernetSettingsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEthernetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_ethernet_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEthernetSettingsResponse]:
        """
        Reads Ethernet configuration. Changes usually apply dynamically.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEthernetSettingsResponse]
            Current Ethernet settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEthernetSettingsResponse,
                    parse_obj_as(
                        type_=GetEthernetSettingsResponse,
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

    def replace_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReplaceEthernetSettingsResponse]:
        """
        Replaces Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplaceEthernetSettingsResponse]
            Replaced Ethernet settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="POST",
            json={
                "enable": enable,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
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
                    ReplaceEthernetSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceEthernetSettingsResponse,
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

    def update_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateEthernetSettingsResponse]:
        """
        Partially updates Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateEthernetSettingsResponse]
            Updated Ethernet settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="PUT",
            json={
                "enable": enable,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
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
                    UpdateEthernetSettingsResponse,
                    parse_obj_as(
                        type_=UpdateEthernetSettingsResponse,
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


class AsyncRawEthernetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_ethernet_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEthernetSettingsResponse]:
        """
        Reads Ethernet configuration. Changes usually apply dynamically.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEthernetSettingsResponse]
            Current Ethernet settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEthernetSettingsResponse,
                    parse_obj_as(
                        type_=GetEthernetSettingsResponse,
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

    async def replace_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReplaceEthernetSettingsResponse]:
        """
        Replaces Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplaceEthernetSettingsResponse]
            Replaced Ethernet settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="POST",
            json={
                "enable": enable,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
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
                    ReplaceEthernetSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceEthernetSettingsResponse,
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

    async def update_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateEthernetSettingsResponse]:
        """
        Partially updates Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateEthernetSettingsResponse]
            Updated Ethernet settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/eth/settings",
            method="PUT",
            json={
                "enable": enable,
                "static_ip": static_ip,
                "ip": ip,
                "netmask": netmask,
                "gateway": gateway,
                "dns": dns,
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
                    UpdateEthernetSettingsResponse,
                    parse_obj_as(
                        type_=UpdateEthernetSettingsResponse,
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
