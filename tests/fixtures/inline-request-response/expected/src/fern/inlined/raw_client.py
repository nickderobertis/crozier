

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.search_result import SearchResult
from .types.inlined_index_response import InlinedIndexResponse
from .types.inlined_search_request_filter import InlinedSearchRequestFilter
from .types.inlined_search_response import InlinedSearchResponse


OMIT = typing.cast(typing.Any, ...)


class RawInlinedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search(
        self,
        *,
        query: str,
        limit: typing.Optional[int] = OMIT,
        filter: typing.Optional[InlinedSearchRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InlinedSearchResponse]:
        """
        Parameters
        ----------
        query : str

        limit : typing.Optional[int]

        filter : typing.Optional[InlinedSearchRequestFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InlinedSearchResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "search",
            method="POST",
            json={
                "query": query,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=InlinedSearchRequestFilter, direction="write"
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
                _data = typing.cast(
                    InlinedSearchResponse,
                    parse_obj_as(
                        type_=InlinedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def index(
        self, *, document: SearchResult, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InlinedIndexResponse]:
        """
        Parameters
        ----------
        document : SearchResult

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InlinedIndexResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "index",
            method="POST",
            json={
                "document": convert_and_respect_annotation_metadata(
                    object_=document, annotation=SearchResult, direction="write"
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
                _data = typing.cast(
                    InlinedIndexResponse,
                    parse_obj_as(
                        type_=InlinedIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInlinedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search(
        self,
        *,
        query: str,
        limit: typing.Optional[int] = OMIT,
        filter: typing.Optional[InlinedSearchRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InlinedSearchResponse]:
        """
        Parameters
        ----------
        query : str

        limit : typing.Optional[int]

        filter : typing.Optional[InlinedSearchRequestFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InlinedSearchResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "search",
            method="POST",
            json={
                "query": query,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=InlinedSearchRequestFilter, direction="write"
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
                _data = typing.cast(
                    InlinedSearchResponse,
                    parse_obj_as(
                        type_=InlinedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def index(
        self, *, document: SearchResult, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InlinedIndexResponse]:
        """
        Parameters
        ----------
        document : SearchResult

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InlinedIndexResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "index",
            method="POST",
            json={
                "document": convert_and_respect_annotation_metadata(
                    object_=document, annotation=SearchResult, direction="write"
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
                _data = typing.cast(
                    InlinedIndexResponse,
                    parse_obj_as(
                        type_=InlinedIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
