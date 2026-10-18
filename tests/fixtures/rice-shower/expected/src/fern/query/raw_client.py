

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
from ..errors.internal_server_error import InternalServerError
from ..types.internal_server_error_body import InternalServerErrorBody
from .types.get_heater_metrics_request_time_end import GetHeaterMetricsRequestTimeEnd
from .types.get_heater_metrics_request_time_start import GetHeaterMetricsRequestTimeStart
from .types.get_heater_metrics_response import GetHeaterMetricsResponse
from .types.get_thermo_metrics_request_time_end import GetThermoMetricsRequestTimeEnd
from .types.get_thermo_metrics_request_time_start import GetThermoMetricsRequestTimeStart
from .types.get_thermo_metrics_response import GetThermoMetricsResponse
from pydantic import ValidationError


class RawQueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_thermo_metrics(
        self,
        system_id: str,
        *,
        time_start: GetThermoMetricsRequestTimeStart,
        time_end: GetThermoMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetThermoMetricsResponse]:
        """
        Query thermometer metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetThermoMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetThermoMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetThermoMetricsResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"query/thermo/{encode_path_param(system_id)}",
            method="GET",
            params={
                "channels": channels,
                "time_start": convert_and_respect_annotation_metadata(
                    object_=time_start, annotation=GetThermoMetricsRequestTimeStart, direction="write"
                ),
                "time_end": convert_and_respect_annotation_metadata(
                    object_=time_end, annotation=GetThermoMetricsRequestTimeEnd, direction="write"
                ),
                "interval": interval,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetThermoMetricsResponse,
                    parse_obj_as(
                        type_=GetThermoMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_heater_metrics(
        self,
        system_id: str,
        *,
        time_start: GetHeaterMetricsRequestTimeStart,
        time_end: GetHeaterMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetHeaterMetricsResponse]:
        """
        Query heater metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetHeaterMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetHeaterMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of heater channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetHeaterMetricsResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"query/heater/{encode_path_param(system_id)}",
            method="GET",
            params={
                "channels": channels,
                "time_start": convert_and_respect_annotation_metadata(
                    object_=time_start, annotation=GetHeaterMetricsRequestTimeStart, direction="write"
                ),
                "time_end": convert_and_respect_annotation_metadata(
                    object_=time_end, annotation=GetHeaterMetricsRequestTimeEnd, direction="write"
                ),
                "interval": interval,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeaterMetricsResponse,
                    parse_obj_as(
                        type_=GetHeaterMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_thermo_metrics(
        self,
        system_id: str,
        *,
        time_start: GetThermoMetricsRequestTimeStart,
        time_end: GetThermoMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetThermoMetricsResponse]:
        """
        Query thermometer metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetThermoMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetThermoMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetThermoMetricsResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"query/thermo/{encode_path_param(system_id)}",
            method="GET",
            params={
                "channels": channels,
                "time_start": convert_and_respect_annotation_metadata(
                    object_=time_start, annotation=GetThermoMetricsRequestTimeStart, direction="write"
                ),
                "time_end": convert_and_respect_annotation_metadata(
                    object_=time_end, annotation=GetThermoMetricsRequestTimeEnd, direction="write"
                ),
                "interval": interval,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetThermoMetricsResponse,
                    parse_obj_as(
                        type_=GetThermoMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_heater_metrics(
        self,
        system_id: str,
        *,
        time_start: GetHeaterMetricsRequestTimeStart,
        time_end: GetHeaterMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetHeaterMetricsResponse]:
        """
        Query heater metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetHeaterMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetHeaterMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of heater channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetHeaterMetricsResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"query/heater/{encode_path_param(system_id)}",
            method="GET",
            params={
                "channels": channels,
                "time_start": convert_and_respect_annotation_metadata(
                    object_=time_start, annotation=GetHeaterMetricsRequestTimeStart, direction="write"
                ),
                "time_end": convert_and_respect_annotation_metadata(
                    object_=time_end, annotation=GetHeaterMetricsRequestTimeEnd, direction="write"
                ),
                "interval": interval,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeaterMetricsResponse,
                    parse_obj_as(
                        type_=GetHeaterMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
