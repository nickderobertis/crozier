

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.gauge_channel_two import GaugeChannelTwo
from ..types.reading import Reading
from ..types.station_code_one import StationCodeOne
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawReadingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def submit_reading(
        self,
        *,
        station_code: StationCodeOne,
        level_cm: float,
        channel: typing.Optional[GaugeChannelTwo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reading]:
        """
        Parameters
        ----------
        station_code : StationCodeOne

        level_cm : float

        channel : typing.Optional[GaugeChannelTwo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reading]
            The stored reading.
        """
        _response = self._client_wrapper.httpx_client.request(
            "readings",
            method="POST",
            json={
                "station_code": station_code,
                "channel": channel,
                "level_cm": level_cm,
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
                    Reading,
                    parse_obj_as(
                        type_=Reading,
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


class AsyncRawReadingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def submit_reading(
        self,
        *,
        station_code: StationCodeOne,
        level_cm: float,
        channel: typing.Optional[GaugeChannelTwo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reading]:
        """
        Parameters
        ----------
        station_code : StationCodeOne

        level_cm : float

        channel : typing.Optional[GaugeChannelTwo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reading]
            The stored reading.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "readings",
            method="POST",
            json={
                "station_code": station_code,
                "channel": channel,
                "level_cm": level_cm,
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
                    Reading,
                    parse_obj_as(
                        type_=Reading,
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
