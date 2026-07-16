

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.server import Server
from ..types.server_attributes import ServerAttributes


OMIT = typing.cast(typing.Any, ...)


class RawServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_server_information(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Server]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Server]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Server,
                    parse_obj_as(
                        type_=Server,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_server_information(
        self,
        *,
        attributes: typing.Optional[ServerAttributes] = OMIT,
        bing_key: typing.Optional[str] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        force_settings: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        map_url: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        registration: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        version: typing.Optional[str] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Server]:
        """
        Parameters
        ----------
        attributes : typing.Optional[ServerAttributes]

        bing_key : typing.Optional[str]

        coordinate_format : typing.Optional[str]

        device_readonly : typing.Optional[bool]

        force_settings : typing.Optional[bool]

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        map_url : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        registration : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        version : typing.Optional[str]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Server]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "server",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=ServerAttributes, direction="write"
                ),
                "bingKey": bing_key,
                "coordinateFormat": coordinate_format,
                "deviceReadonly": device_readonly,
                "forceSettings": force_settings,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "mapUrl": map_url,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "registration": registration,
                "twelveHourFormat": twelve_hour_format,
                "version": version,
                "zoom": zoom,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Server,
                    parse_obj_as(
                        type_=Server,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_server_information(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Server]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Server]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Server,
                    parse_obj_as(
                        type_=Server,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_server_information(
        self,
        *,
        attributes: typing.Optional[ServerAttributes] = OMIT,
        bing_key: typing.Optional[str] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        force_settings: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        map_url: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        registration: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        version: typing.Optional[str] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Server]:
        """
        Parameters
        ----------
        attributes : typing.Optional[ServerAttributes]

        bing_key : typing.Optional[str]

        coordinate_format : typing.Optional[str]

        device_readonly : typing.Optional[bool]

        force_settings : typing.Optional[bool]

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        map_url : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        registration : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        version : typing.Optional[str]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Server]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "server",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=ServerAttributes, direction="write"
                ),
                "bingKey": bing_key,
                "coordinateFormat": coordinate_format,
                "deviceReadonly": device_readonly,
                "forceSettings": force_settings,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "mapUrl": map_url,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "registration": registration,
                "twelveHourFormat": twelve_hour_format,
                "version": version,
                "zoom": zoom,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Server,
                    parse_obj_as(
                        type_=Server,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
