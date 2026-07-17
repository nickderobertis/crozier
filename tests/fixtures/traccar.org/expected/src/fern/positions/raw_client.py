

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.position import Position
from pydantic import ValidationError


class RawPositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetches_a_list_of_positions(
        self,
        *,
        device_id: typing.Optional[int] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Position]]:
        """
        We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_.

        Parameters
        ----------
        device_id : typing.Optional[int]
            _deviceId_ is optional, but requires the _from_ and _to_ parameters when used

        from_ : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]
            To fetch one or more positions. Multiple params can be passed like `id=31&id=42`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Position]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "positions",
            method="GET",
            params={
                "deviceId": device_id,
                "from": serialize_datetime(from_) if from_ is not None else None,
                "to": serialize_datetime(to) if to is not None else None,
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Position],
                    parse_obj_as(
                        type_=typing.List[Position],
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


class AsyncRawPositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetches_a_list_of_positions(
        self,
        *,
        device_id: typing.Optional[int] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Position]]:
        """
        We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_.

        Parameters
        ----------
        device_id : typing.Optional[int]
            _deviceId_ is optional, but requires the _from_ and _to_ parameters when used

        from_ : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]
            To fetch one or more positions. Multiple params can be passed like `id=31&id=42`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Position]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "positions",
            method="GET",
            params={
                "deviceId": device_id,
                "from": serialize_datetime(from_) if from_ is not None else None,
                "to": serialize_datetime(to) if to is not None else None,
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Position],
                    parse_obj_as(
                        type_=typing.List[Position],
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
