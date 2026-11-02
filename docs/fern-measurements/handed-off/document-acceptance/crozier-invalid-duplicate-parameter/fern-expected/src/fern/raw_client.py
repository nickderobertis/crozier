

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.alert_payload_chime import AlertPayloadChime
from .types.queued_alert import QueuedAlert
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send_alert(
        self,
        device_id: str,
        *,
        deliver_at: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        muted: typing.Optional[str] = OMIT,
        chime: typing.Optional[AlertPayloadChime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueuedAlert]:
        """
        Parameters
        ----------
        device_id : str

        deliver_at : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        message : typing.Optional[str]

        muted : typing.Optional[str]

        chime : typing.Optional[AlertPayloadChime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueuedAlert]
            The alert was queued
        """
        _response = self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(device_id)}/alerts",
            method="POST",
            json={
                "deliverAt": deliver_at,
                "headline": headline,
                "message": message,
                "muted": muted,
                "chime": chime,
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
                    QueuedAlert,
                    parse_obj_as(
                        type_=QueuedAlert,
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

    async def send_alert(
        self,
        device_id: str,
        *,
        deliver_at: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        muted: typing.Optional[str] = OMIT,
        chime: typing.Optional[AlertPayloadChime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueuedAlert]:
        """
        Parameters
        ----------
        device_id : str

        deliver_at : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        message : typing.Optional[str]

        muted : typing.Optional[str]

        chime : typing.Optional[AlertPayloadChime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueuedAlert]
            The alert was queued
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(device_id)}/alerts",
            method="POST",
            json={
                "deliverAt": deliver_at,
                "headline": headline,
                "message": message,
                "muted": muted,
                "chime": chime,
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
                    QueuedAlert,
                    parse_obj_as(
                        type_=QueuedAlert,
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
