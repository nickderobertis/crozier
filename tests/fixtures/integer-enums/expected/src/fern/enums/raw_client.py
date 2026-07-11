

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.http_status import HttpStatus
from ..types.priority import Priority
from ..types.ticket import Ticket


OMIT = typing.cast(typing.Any, ...)


class RawEnumsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def setpriority(
        self, *, level: Priority, request: HttpStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Ticket]:
        """
        Parameters
        ----------
        level : Priority

        request : HttpStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ticket]

        """
        _response = self._client_wrapper.httpx_client.request(
            "priority",
            method="POST",
            params={
                "level": level,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEnumsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def setpriority(
        self, *, level: Priority, request: HttpStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Ticket]:
        """
        Parameters
        ----------
        level : Priority

        request : HttpStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ticket]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "priority",
            method="POST",
            params={
                "level": level,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
