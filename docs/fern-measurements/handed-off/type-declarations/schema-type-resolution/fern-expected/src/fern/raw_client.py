

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
from .types.alarm import Alarm
from .types.alarm_history import AlarmHistory
from .types.oven_status import OvenStatus
from .types.oven_status_trays_item import OvenStatusTraysItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_oven_status(
        self, oven_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OvenStatus]:
        """
        Parameters
        ----------
        oven_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OvenStatus]
            The status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ovens/{encode_path_param(oven_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OvenStatus,
                    parse_obj_as(
                        type_=OvenStatus,
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

    def replace_oven_status(
        self,
        oven_id: str,
        *,
        alarms: typing.Optional[typing.Sequence[Alarm]] = OMIT,
        trays: typing.Optional[typing.Sequence[OvenStatusTraysItem]] = OMIT,
        history: typing.Optional[AlarmHistory] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        oven_id : str

        alarms : typing.Optional[typing.Sequence[Alarm]]
            Alarms raised by the oven controller.

        trays : typing.Optional[typing.Sequence[OvenStatusTraysItem]]

        history : typing.Optional[AlarmHistory]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ovens/{encode_path_param(oven_id)}/status",
            method="PUT",
            json={
                "alarms": convert_and_respect_annotation_metadata(
                    object_=alarms, annotation=typing.Sequence[Alarm], direction="write"
                ),
                "trays": convert_and_respect_annotation_metadata(
                    object_=trays, annotation=typing.Sequence[OvenStatusTraysItem], direction="write"
                ),
                "history": convert_and_respect_annotation_metadata(
                    object_=history, annotation=AlarmHistory, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_oven_status(
        self, oven_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OvenStatus]:
        """
        Parameters
        ----------
        oven_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OvenStatus]
            The status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ovens/{encode_path_param(oven_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OvenStatus,
                    parse_obj_as(
                        type_=OvenStatus,
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

    async def replace_oven_status(
        self,
        oven_id: str,
        *,
        alarms: typing.Optional[typing.Sequence[Alarm]] = OMIT,
        trays: typing.Optional[typing.Sequence[OvenStatusTraysItem]] = OMIT,
        history: typing.Optional[AlarmHistory] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        oven_id : str

        alarms : typing.Optional[typing.Sequence[Alarm]]
            Alarms raised by the oven controller.

        trays : typing.Optional[typing.Sequence[OvenStatusTraysItem]]

        history : typing.Optional[AlarmHistory]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ovens/{encode_path_param(oven_id)}/status",
            method="PUT",
            json={
                "alarms": convert_and_respect_annotation_metadata(
                    object_=alarms, annotation=typing.Sequence[Alarm], direction="write"
                ),
                "trays": convert_and_respect_annotation_metadata(
                    object_=trays, annotation=typing.Sequence[OvenStatusTraysItem], direction="write"
                ),
                "history": convert_and_respect_annotation_metadata(
                    object_=history, annotation=AlarmHistory, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
