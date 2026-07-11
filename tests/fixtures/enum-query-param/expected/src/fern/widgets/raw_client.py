

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.list_widgets_request_level import ListWidgetsRequestLevel
from .types.list_widgets_response import ListWidgetsResponse


class RawWidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_widgets(
        self,
        *,
        level: typing.Optional[ListWidgetsRequestLevel] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWidgetsResponse]:
        """
        Parameters
        ----------
        level : typing.Optional[ListWidgetsRequestLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWidgetsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "widgets",
            method="GET",
            params={
                "level": level,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWidgetsResponse,
                    parse_obj_as(
                        type_=ListWidgetsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWidgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_widgets(
        self,
        *,
        level: typing.Optional[ListWidgetsRequestLevel] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWidgetsResponse]:
        """
        Parameters
        ----------
        level : typing.Optional[ListWidgetsRequestLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWidgetsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "widgets",
            method="GET",
            params={
                "level": level,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWidgetsResponse,
                    parse_obj_as(
                        type_=ListWidgetsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
