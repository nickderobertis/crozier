

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.get_surge_request_since import GetSurgeRequestSince
from .types.get_surge_response import GetSurgeResponse
from .types.get_tides_request_since import GetTidesRequestSince
from .types.get_tides_response import GetTidesResponse
from pydantic import ValidationError


class RawTidesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_tides(
        self,
        station_id: str,
        *,
        since: GetTidesRequestSince,
        step: float,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTidesResponse]:
        """
        Parameters
        ----------
        station_id : str

        since : GetTidesRequestSince

        step : float

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTidesResponse]
            Readings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(station_id)}",
            method="GET",
            params={
                "gauges": gauges,
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=GetTidesRequestSince, direction="write"
                ),
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTidesResponse,
                    parse_obj_as(
                        type_=GetTidesResponse,
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

    def get_surge(
        self,
        station_id: str,
        *,
        since: GetSurgeRequestSince,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSurgeResponse]:
        """
        Parameters
        ----------
        station_id : str

        since : GetSurgeRequestSince

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSurgeResponse]
            Readings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(station_id)}/surge",
            method="GET",
            params={
                "gauges": gauges,
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=GetSurgeRequestSince, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSurgeResponse,
                    parse_obj_as(
                        type_=GetSurgeResponse,
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


class AsyncRawTidesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_tides(
        self,
        station_id: str,
        *,
        since: GetTidesRequestSince,
        step: float,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetTidesResponse]:
        """
        Parameters
        ----------
        station_id : str

        since : GetTidesRequestSince

        step : float

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTidesResponse]
            Readings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(station_id)}",
            method="GET",
            params={
                "gauges": gauges,
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=GetTidesRequestSince, direction="write"
                ),
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTidesResponse,
                    parse_obj_as(
                        type_=GetTidesResponse,
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

    async def get_surge(
        self,
        station_id: str,
        *,
        since: GetSurgeRequestSince,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSurgeResponse]:
        """
        Parameters
        ----------
        station_id : str

        since : GetSurgeRequestSince

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSurgeResponse]
            Readings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(station_id)}/surge",
            method="GET",
            params={
                "gauges": gauges,
                "since": convert_and_respect_annotation_metadata(
                    object_=since, annotation=GetSurgeRequestSince, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSurgeResponse,
                    parse_obj_as(
                        type_=GetSurgeResponse,
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
