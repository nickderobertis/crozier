

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.search_widgets_response import SearchWidgetsResponse


OMIT = typing.cast(typing.Any, ...)


class RawWidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_widgets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter_name: typing.Optional[str] = OMIT,
        filter_color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchWidgetsResponse]:
        """
        Parameters
        ----------
        page_size : typing.Optional[int]

        page_number : typing.Optional[int]

        filter_name : typing.Optional[str]

        filter_color : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchWidgetsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "widgets/search",
            method="POST",
            params={
                "page[size]": page_size,
                "page[number]": page_number,
            },
            data={
                "filter[name]": filter_name,
                "filter[color]": filter_color,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchWidgetsResponse,
                    parse_obj_as(
                        type_=SearchWidgetsResponse,
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

    async def search_widgets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter_name: typing.Optional[str] = OMIT,
        filter_color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchWidgetsResponse]:
        """
        Parameters
        ----------
        page_size : typing.Optional[int]

        page_number : typing.Optional[int]

        filter_name : typing.Optional[str]

        filter_color : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchWidgetsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "widgets/search",
            method="POST",
            params={
                "page[size]": page_size,
                "page[number]": page_number,
            },
            data={
                "filter[name]": filter_name,
                "filter[color]": filter_color,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchWidgetsResponse,
                    parse_obj_as(
                        type_=SearchWidgetsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
