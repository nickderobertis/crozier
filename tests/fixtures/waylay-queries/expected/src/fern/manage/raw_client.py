

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.delete_response import DeleteResponse
from ..types.http_validation_error import HttpValidationError
from ..types.queries_list_response import QueriesListResponse
from ..types.query_input import QueryInput
from ..types.query_response import QueryResponse
from .types.update_query_queries_v1query_query_name_put_request_body import (
    UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_queries(
        self,
        *,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueriesListResponse]:
        """
        List named queries.

        Parameters
        ----------
        q : typing.Optional[str]
            The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater.

        limit : typing.Optional[int]
            Maximal number of items return in one response.

        offset : typing.Optional[int]
            Numbers of items to skip before listing results in the response page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueriesListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries/v1/query",
            method="GET",
            params={
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueriesListResponse,
                    parse_obj_as(
                        type_=QueriesListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def post_query(
        self,
        *,
        name: str,
        query: QueryInput,
        meta: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryResponse]:
        """
        Create a new named query.

        Parameters
        ----------
        name : str
            Name of the stored query definition.

        query : QueryInput

        meta : typing.Optional[typing.Dict[str, typing.Any]]
            User metadata for the query definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries/v1/query",
            method="POST",
            json={
                "name": name,
                "meta": meta,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=QueryInput, direction="write"
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
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[QueryResponse]:
        """
        Get the definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_query(
        self,
        query_name: str,
        *,
        request: UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryResponse]:
        """
        Create or update a named query definition.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request : UpdateQueryQueriesV1QueryQueryNamePutRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateQueryQueriesV1QueryQueryNamePutRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def remove_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteResponse]:
        """
        Remove definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteResponse,
                    parse_obj_as(
                        type_=DeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawManageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_queries(
        self,
        *,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueriesListResponse]:
        """
        List named queries.

        Parameters
        ----------
        q : typing.Optional[str]
            The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater.

        limit : typing.Optional[int]
            Maximal number of items return in one response.

        offset : typing.Optional[int]
            Numbers of items to skip before listing results in the response page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueriesListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries/v1/query",
            method="GET",
            params={
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueriesListResponse,
                    parse_obj_as(
                        type_=QueriesListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def post_query(
        self,
        *,
        name: str,
        query: QueryInput,
        meta: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryResponse]:
        """
        Create a new named query.

        Parameters
        ----------
        name : str
            Name of the stored query definition.

        query : QueryInput

        meta : typing.Optional[typing.Dict[str, typing.Any]]
            User metadata for the query definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries/v1/query",
            method="POST",
            json={
                "name": name,
                "meta": meta,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=QueryInput, direction="write"
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
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[QueryResponse]:
        """
        Get the definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_query(
        self,
        query_name: str,
        *,
        request: UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryResponse]:
        """
        Create or update a named query definition.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request : UpdateQueryQueriesV1QueryQueryNamePutRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateQueryQueriesV1QueryQueryNamePutRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def remove_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteResponse]:
        """
        Remove definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/v1/query/{encode_path_param(query_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteResponse,
                    parse_obj_as(
                        type_=DeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
