

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.get_tile_v2tiles_coastal_zxy_pbf_get_request_shading import GetTileV2TilesCoastalZxyPbfGetRequestShading
from .types.get_tile_v2tiles_coastal_zxy_pbf_get_response import GetTileV2TilesCoastalZxyPbfGetResponse
from .types.read_abcd_tile_request_palette import ReadAbcdTileRequestPalette
from .types.read_abcd_tile_response import ReadAbcdTileResponse
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_tile_v2tiles_coastal_z_x_y_pbf_get(
        self,
        z: int,
        x: int,
        y: int,
        *,
        shading: typing.Optional[GetTileV2TilesCoastalZxyPbfGetRequestShading] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTileV2TilesCoastalZxyPbfGetResponse]:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        shading : typing.Optional[GetTileV2TilesCoastalZxyPbfGetRequestShading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTileV2TilesCoastalZxyPbfGetResponse]
            The tile
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tiles/coastal/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "shading": convert_and_respect_annotation_metadata(
                    object_=shading, annotation=GetTileV2TilesCoastalZxyPbfGetRequestShading, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTileV2TilesCoastalZxyPbfGetResponse,
                    parse_obj_as(
                        type_=GetTileV2TilesCoastalZxyPbfGetResponse,
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

    def read_a_b_c_d_tile(
        self,
        a: str,
        b: str,
        *,
        palette: typing.Optional[ReadAbcdTileRequestPalette] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReadAbcdTileResponse]:
        """
        Parameters
        ----------
        a : str

        b : str

        palette : typing.Optional[ReadAbcdTileRequestPalette]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReadAbcdTileResponse]
            The tile
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tiles/{encode_path_param(a)}/{encode_path_param(b)}",
            method="GET",
            params={
                "palette": convert_and_respect_annotation_metadata(
                    object_=palette, annotation=ReadAbcdTileRequestPalette, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadAbcdTileResponse,
                    parse_obj_as(
                        type_=ReadAbcdTileResponse,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_tile_v2tiles_coastal_z_x_y_pbf_get(
        self,
        z: int,
        x: int,
        y: int,
        *,
        shading: typing.Optional[GetTileV2TilesCoastalZxyPbfGetRequestShading] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetTileV2TilesCoastalZxyPbfGetResponse]:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        shading : typing.Optional[GetTileV2TilesCoastalZxyPbfGetRequestShading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTileV2TilesCoastalZxyPbfGetResponse]
            The tile
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tiles/coastal/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "shading": convert_and_respect_annotation_metadata(
                    object_=shading, annotation=GetTileV2TilesCoastalZxyPbfGetRequestShading, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTileV2TilesCoastalZxyPbfGetResponse,
                    parse_obj_as(
                        type_=GetTileV2TilesCoastalZxyPbfGetResponse,
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

    async def read_a_b_c_d_tile(
        self,
        a: str,
        b: str,
        *,
        palette: typing.Optional[ReadAbcdTileRequestPalette] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReadAbcdTileResponse]:
        """
        Parameters
        ----------
        a : str

        b : str

        palette : typing.Optional[ReadAbcdTileRequestPalette]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReadAbcdTileResponse]
            The tile
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tiles/{encode_path_param(a)}/{encode_path_param(b)}",
            method="GET",
            params={
                "palette": convert_and_respect_annotation_metadata(
                    object_=palette, annotation=ReadAbcdTileRequestPalette, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadAbcdTileResponse,
                    parse_obj_as(
                        type_=ReadAbcdTileResponse,
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
