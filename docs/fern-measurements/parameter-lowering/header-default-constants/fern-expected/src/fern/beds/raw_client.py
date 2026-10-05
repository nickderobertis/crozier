

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.list_beds_request_x_vent_mode import ListBedsRequestXVentMode
from pydantic import ValidationError


class RawBedsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_beds(
        self,
        *,
        section: str,
        lamp_watts: int,
        vent_mode: ListBedsRequestXVentMode,
        fan_speed: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        section : str

        lamp_watts : int

        vent_mode : ListBedsRequestXVentMode

        fan_speed : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Beds.
        """
        _response = self._client_wrapper.httpx_client.request(
            "beds",
            method="GET",
            params={
                "section": section,
            },
            headers={
                "X-Lamp-Watts": str(lamp_watts) if lamp_watts is not None else None,
                "X-Fan-Speed": str(fan_speed) if fan_speed is not None else None,
                "X-Vent-Mode": vent_mode.value if vent_mode is not None else None,
                "X-Valve-Mode": "drip",
                "X-Mist-Mode": "fine",
                "X-Hatch-Mode": "down",
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_bed(self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            One bed.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"beds/{encode_path_param(bed_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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


class AsyncRawBedsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_beds(
        self,
        *,
        section: str,
        lamp_watts: int,
        vent_mode: ListBedsRequestXVentMode,
        fan_speed: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        section : str

        lamp_watts : int

        vent_mode : ListBedsRequestXVentMode

        fan_speed : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Beds.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "beds",
            method="GET",
            params={
                "section": section,
            },
            headers={
                "X-Lamp-Watts": str(lamp_watts) if lamp_watts is not None else None,
                "X-Fan-Speed": str(fan_speed) if fan_speed is not None else None,
                "X-Vent-Mode": vent_mode.value if vent_mode is not None else None,
                "X-Valve-Mode": "drip",
                "X-Mist-Mode": "fine",
                "X-Hatch-Mode": "down",
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_bed(
        self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            One bed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"beds/{encode_path_param(bed_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
