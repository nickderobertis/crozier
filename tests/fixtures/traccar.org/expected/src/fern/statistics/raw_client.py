

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
from ..types.statistics import Statistics
from pydantic import ValidationError


class RawStatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_server_statistics(
        self, *, from_: dt.datetime, to: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Statistics]]:
        """
        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Statistics]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "statistics",
            method="GET",
            params={
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Statistics],
                    parse_obj_as(
                        type_=typing.List[Statistics],
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


class AsyncRawStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_server_statistics(
        self, *, from_: dt.datetime, to: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Statistics]]:
        """
        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Statistics]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "statistics",
            method="GET",
            params={
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Statistics],
                    parse_obj_as(
                        type_=typing.List[Statistics],
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
