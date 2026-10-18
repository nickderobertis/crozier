

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.item import Item
from ..types.list_namespace_response import ListNamespaceResponse
from ..types.search_items_response import SearchItemsResponse
from .types.store_put_request_index import StorePutRequestIndex
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        refresh_ttl: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Item]:
        """
        Parameters
        ----------
        key : str

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        refresh_ttl : typing.Optional[bool]
            Whether to refresh the TTL on this read operation. If not provided, uses the store's default behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Item]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "store/items",
            method="GET",
            params={
                "key": key,
                "namespace": namespace,
                "refresh_ttl": refresh_ttl,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Item,
                    parse_obj_as(
                        type_=Item,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_item(
        self,
        *,
        namespace: typing.Sequence[str],
        key: str,
        value: typing.Dict[str, typing.Any],
        index: typing.Optional[StorePutRequestIndex] = OMIT,
        ttl: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        namespace : typing.Sequence[str]
            A list of strings representing the namespace path.

        key : str
            The unique identifier for the item within the namespace.

        value : typing.Dict[str, typing.Any]
            A dictionary containing the item's data.

        index : typing.Optional[StorePutRequestIndex]
            Controls search indexing - null (use defaults), false (disable), or list of field paths to index.

        ttl : typing.Optional[float]
            Optional time-to-live in minutes for the item, or null for no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "store/items",
            method="PUT",
            json={
                "namespace": namespace,
                "key": key,
                "value": value,
                "index": convert_and_respect_annotation_metadata(
                    object_=index, annotation=typing.Optional[StorePutRequestIndex], direction="write"
                ),
                "ttl": ttl,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        key : str
            The unique identifier for the item.

        namespace : typing.Optional[typing.Sequence[str]]
            A list of strings representing the namespace path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "store/items",
            method="DELETE",
            json={
                "namespace": namespace,
                "key": key,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_items(
        self,
        *,
        namespace_prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        refresh_ttl: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchItemsResponse]:
        """
        Lists items ordered by last updated time. If a `query` is provided, performs a natural language search instead. Supports pagination via `limit` and `offset`, and filtering via `filter`.

        Parameters
        ----------
        namespace_prefix : typing.Optional[typing.Sequence[str]]
            List of strings representing the namespace prefix.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Optional dictionary of key-value pairs to filter results.

        limit : typing.Optional[int]
            Maximum number of items to return (default is 10).

        offset : typing.Optional[int]
            Number of items to skip before returning results (default is 0).

        query : typing.Optional[str]
            Optional natural language search query. If not provided, items are returned ordered by last updated time (listing mode). If provided, performs a natural language search over item contents.

        refresh_ttl : typing.Optional[bool]
            Whether to refresh the TTL on items returned by this search. If null, uses the store's default behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchItemsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "store/items/search",
            method="POST",
            json={
                "namespace_prefix": namespace_prefix,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "query": query,
                "refresh_ttl": refresh_ttl,
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
                    SearchItemsResponse,
                    parse_obj_as(
                        type_=SearchItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_namespaces(
        self,
        *,
        prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        suffix: typing.Optional[typing.Sequence[str]] = OMIT,
        max_depth: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListNamespaceResponse]:
        """
        Parameters
        ----------
        prefix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the prefix to filter namespaces.

        suffix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the suffix to filter namespaces.

        max_depth : typing.Optional[int]
            Optional integer specifying the maximum depth of namespaces to return.

        limit : typing.Optional[int]
            Maximum number of namespaces to return (default is 100).

        offset : typing.Optional[int]
            Number of namespaces to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListNamespaceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "store/namespaces",
            method="POST",
            json={
                "prefix": prefix,
                "suffix": suffix,
                "max_depth": max_depth,
                "limit": limit,
                "offset": offset,
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
                    ListNamespaceResponse,
                    parse_obj_as(
                        type_=ListNamespaceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawStoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        refresh_ttl: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Item]:
        """
        Parameters
        ----------
        key : str

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        refresh_ttl : typing.Optional[bool]
            Whether to refresh the TTL on this read operation. If not provided, uses the store's default behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Item]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "store/items",
            method="GET",
            params={
                "key": key,
                "namespace": namespace,
                "refresh_ttl": refresh_ttl,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Item,
                    parse_obj_as(
                        type_=Item,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_item(
        self,
        *,
        namespace: typing.Sequence[str],
        key: str,
        value: typing.Dict[str, typing.Any],
        index: typing.Optional[StorePutRequestIndex] = OMIT,
        ttl: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        namespace : typing.Sequence[str]
            A list of strings representing the namespace path.

        key : str
            The unique identifier for the item within the namespace.

        value : typing.Dict[str, typing.Any]
            A dictionary containing the item's data.

        index : typing.Optional[StorePutRequestIndex]
            Controls search indexing - null (use defaults), false (disable), or list of field paths to index.

        ttl : typing.Optional[float]
            Optional time-to-live in minutes for the item, or null for no expiration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "store/items",
            method="PUT",
            json={
                "namespace": namespace,
                "key": key,
                "value": value,
                "index": convert_and_respect_annotation_metadata(
                    object_=index, annotation=typing.Optional[StorePutRequestIndex], direction="write"
                ),
                "ttl": ttl,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        key : str
            The unique identifier for the item.

        namespace : typing.Optional[typing.Sequence[str]]
            A list of strings representing the namespace path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "store/items",
            method="DELETE",
            json={
                "namespace": namespace,
                "key": key,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_items(
        self,
        *,
        namespace_prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        refresh_ttl: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchItemsResponse]:
        """
        Lists items ordered by last updated time. If a `query` is provided, performs a natural language search instead. Supports pagination via `limit` and `offset`, and filtering via `filter`.

        Parameters
        ----------
        namespace_prefix : typing.Optional[typing.Sequence[str]]
            List of strings representing the namespace prefix.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Optional dictionary of key-value pairs to filter results.

        limit : typing.Optional[int]
            Maximum number of items to return (default is 10).

        offset : typing.Optional[int]
            Number of items to skip before returning results (default is 0).

        query : typing.Optional[str]
            Optional natural language search query. If not provided, items are returned ordered by last updated time (listing mode). If provided, performs a natural language search over item contents.

        refresh_ttl : typing.Optional[bool]
            Whether to refresh the TTL on items returned by this search. If null, uses the store's default behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchItemsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "store/items/search",
            method="POST",
            json={
                "namespace_prefix": namespace_prefix,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "query": query,
                "refresh_ttl": refresh_ttl,
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
                    SearchItemsResponse,
                    parse_obj_as(
                        type_=SearchItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_namespaces(
        self,
        *,
        prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        suffix: typing.Optional[typing.Sequence[str]] = OMIT,
        max_depth: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListNamespaceResponse]:
        """
        Parameters
        ----------
        prefix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the prefix to filter namespaces.

        suffix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the suffix to filter namespaces.

        max_depth : typing.Optional[int]
            Optional integer specifying the maximum depth of namespaces to return.

        limit : typing.Optional[int]
            Maximum number of namespaces to return (default is 100).

        offset : typing.Optional[int]
            Number of namespaces to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListNamespaceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "store/namespaces",
            method="POST",
            json={
                "prefix": prefix,
                "suffix": suffix,
                "max_depth": max_depth,
                "limit": limit,
                "offset": offset,
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
                    ListNamespaceResponse,
                    parse_obj_as(
                        type_=ListNamespaceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
