

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_lamp_response import GetLampResponse
from .types.update_lamp_settings_response import UpdateLampSettingsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLampsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_lamp(
        self, lamp_id: str, *, wattage: int, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLampResponse]:
        """
        Parameters
        ----------
        lamp_id : str

        wattage : int

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLampResponse]
            The lamp
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}",
            method="GET",
            params={
                "wattage": wattage,
                "shade": shade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLampResponse,
                    parse_obj_as(
                        type_=GetLampResponse,
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

    def get_lamp_manual(
        self, lamp_id: str, *, edition: str, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        lamp_id : str

        edition : str

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/manual",
            method="GET",
            params={
                "edition": edition,
                "shade": shade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_lamp_settings(
        self, lamp_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateLampSettingsResponse]:
        """
        Parameters
        ----------
        lamp_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLampSettingsResponse]
            Updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/settings",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLampSettingsResponse,
                    parse_obj_as(
                        type_=UpdateLampSettingsResponse,
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


class AsyncRawLampsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_lamp(
        self, lamp_id: str, *, wattage: int, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLampResponse]:
        """
        Parameters
        ----------
        lamp_id : str

        wattage : int

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLampResponse]
            The lamp
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}",
            method="GET",
            params={
                "wattage": wattage,
                "shade": shade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLampResponse,
                    parse_obj_as(
                        type_=GetLampResponse,
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

    async def get_lamp_manual(
        self, lamp_id: str, *, edition: str, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        lamp_id : str

        edition : str

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/manual",
            method="GET",
            params={
                "edition": edition,
                "shade": shade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_lamp_settings(
        self, lamp_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateLampSettingsResponse]:
        """
        Parameters
        ----------
        lamp_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLampSettingsResponse]
            Updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/settings",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLampSettingsResponse,
                    parse_obj_as(
                        type_=UpdateLampSettingsResponse,
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
