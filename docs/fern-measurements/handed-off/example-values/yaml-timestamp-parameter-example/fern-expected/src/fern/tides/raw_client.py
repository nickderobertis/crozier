

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_gauge_response import GetGaugeResponse
from pydantic import ValidationError


class RawTidesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tides(
        self,
        *,
        since: dt.datetime,
        recorded_on: str,
        until: typing.Optional[dt.datetime] = None,
        logged_after: typing.Optional[str] = None,
        station: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[float]]:
        """
        Parameters
        ----------
        since : dt.datetime

        recorded_on : str

        until : typing.Optional[dt.datetime]

        logged_after : typing.Optional[str]

        station : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[float]]
            Readings
        """
        _response = self._client_wrapper.httpx_client.request(
            "tides",
            method="GET",
            params={
                "since": serialize_datetime(since),
                "until": serialize_datetime(until) if until is not None else None,
                "loggedAfter": logged_after,
                "recordedOn": recorded_on,
                "station": station,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[float],
                    parse_obj_as(
                        type_=typing.List[float],
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

    def get_gauge(
        self,
        gauge_id: str,
        *,
        as_of: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetGaugeResponse]:
        """
        Parameters
        ----------
        gauge_id : str

        as_of : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGaugeResponse]
            The gauge
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(gauge_id)}",
            method="GET",
            params={
                "asOf": serialize_datetime(as_of) if as_of is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGaugeResponse,
                    parse_obj_as(
                        type_=GetGaugeResponse,
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

    async def list_tides(
        self,
        *,
        since: dt.datetime,
        recorded_on: str,
        until: typing.Optional[dt.datetime] = None,
        logged_after: typing.Optional[str] = None,
        station: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[float]]:
        """
        Parameters
        ----------
        since : dt.datetime

        recorded_on : str

        until : typing.Optional[dt.datetime]

        logged_after : typing.Optional[str]

        station : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[float]]
            Readings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tides",
            method="GET",
            params={
                "since": serialize_datetime(since),
                "until": serialize_datetime(until) if until is not None else None,
                "loggedAfter": logged_after,
                "recordedOn": recorded_on,
                "station": station,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[float],
                    parse_obj_as(
                        type_=typing.List[float],
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

    async def get_gauge(
        self,
        gauge_id: str,
        *,
        as_of: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetGaugeResponse]:
        """
        Parameters
        ----------
        gauge_id : str

        as_of : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGaugeResponse]
            The gauge
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tides/{encode_path_param(gauge_id)}",
            method="GET",
            params={
                "asOf": serialize_datetime(as_of) if as_of is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGaugeResponse,
                    parse_obj_as(
                        type_=GetGaugeResponse,
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
