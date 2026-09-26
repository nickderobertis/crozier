

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_v2vectordb_indexes_create_request_index_params_item import (
    PostV2VectordbIndexesCreateRequestIndexParamsItem,
)
from .types.post_v2vectordb_indexes_create_response import PostV2VectordbIndexesCreateResponse
from .types.post_v2vectordb_indexes_describe_response import PostV2VectordbIndexesDescribeResponse
from .types.post_v2vectordb_indexes_drop_response import PostV2VectordbIndexesDropResponse
from .types.post_v2vectordb_indexes_list_response import PostV2VectordbIndexesListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIndexOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_index(
        self,
        *,
        collection_name: str,
        index_params: typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbIndexesCreateResponse]:
        """
        This creates a named index for a target field, which can either be a vector field or a scalar field.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_params : typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem]
              The parameters that apply to the index-building process.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbIndexesCreateResponse]
            A Status object indicating whether this operation succeeds.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexParams": convert_and_respect_annotation_metadata(
                    object_=index_params,
                    annotation=typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem],
                    direction="write",
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
                    PostV2VectordbIndexesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesCreateResponse,
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

    def drop_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbIndexesDropResponse]:
        """
        This operation deletes index from a specified collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_name : str
            The name fo the target index.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbIndexesDropResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexName": index_name,
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
                    PostV2VectordbIndexesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesDropResponse,
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

    def describe_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbIndexesDescribeResponse]:
        """
        This operation describes the current index.

        Parameters
        ----------
        collection_name : str
            The name of an the collection to which the index belongs.

        index_name : str
            The name of the index to describe.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbIndexesDescribeResponse]
            An object that contains the detailed description of the current index.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/describe",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexName": index_name,
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
                    PostV2VectordbIndexesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesDescribeResponse,
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

    def list_indexes(
        self,
        *,
        db_name: str,
        collection_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbIndexesListResponse]:
        """
        This operation lists all indexes of a specific collection.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        collection_name : typing.Optional[str]
            The name of an existing collection. Setting this to a non-existing collection leads to an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbIndexesListResponse]
            The names of all built indexes in a list.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/list",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
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
                    PostV2VectordbIndexesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesListResponse,
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


class AsyncRawIndexOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_index(
        self,
        *,
        collection_name: str,
        index_params: typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbIndexesCreateResponse]:
        """
        This creates a named index for a target field, which can either be a vector field or a scalar field.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_params : typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem]
              The parameters that apply to the index-building process.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbIndexesCreateResponse]
            A Status object indicating whether this operation succeeds.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexParams": convert_and_respect_annotation_metadata(
                    object_=index_params,
                    annotation=typing.Sequence[PostV2VectordbIndexesCreateRequestIndexParamsItem],
                    direction="write",
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
                    PostV2VectordbIndexesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesCreateResponse,
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

    async def drop_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbIndexesDropResponse]:
        """
        This operation deletes index from a specified collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_name : str
            The name fo the target index.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbIndexesDropResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexName": index_name,
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
                    PostV2VectordbIndexesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesDropResponse,
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

    async def describe_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbIndexesDescribeResponse]:
        """
        This operation describes the current index.

        Parameters
        ----------
        collection_name : str
            The name of an the collection to which the index belongs.

        index_name : str
            The name of the index to describe.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbIndexesDescribeResponse]
            An object that contains the detailed description of the current index.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/describe",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "indexName": index_name,
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
                    PostV2VectordbIndexesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesDescribeResponse,
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

    async def list_indexes(
        self,
        *,
        db_name: str,
        collection_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbIndexesListResponse]:
        """
        This operation lists all indexes of a specific collection.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        collection_name : typing.Optional[str]
            The name of an existing collection. Setting this to a non-existing collection leads to an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbIndexesListResponse]
            The names of all built indexes in a list.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/indexes/list",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
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
                    PostV2VectordbIndexesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbIndexesListResponse,
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
