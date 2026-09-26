

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_v2vectordb_collections_create_request_index_params_item import (
    PostV2VectordbCollectionsCreateRequestIndexParamsItem,
)
from .types.post_v2vectordb_collections_create_request_params import PostV2VectordbCollectionsCreateRequestParams
from .types.post_v2vectordb_collections_create_request_schema import PostV2VectordbCollectionsCreateRequestSchema
from .types.post_v2vectordb_collections_create_response import PostV2VectordbCollectionsCreateResponse
from .types.post_v2vectordb_collections_describe_response import PostV2VectordbCollectionsDescribeResponse
from .types.post_v2vectordb_collections_drop_response import PostV2VectordbCollectionsDropResponse
from .types.post_v2vectordb_collections_get_load_state_response import PostV2VectordbCollectionsGetLoadStateResponse
from .types.post_v2vectordb_collections_get_stats_response import PostV2VectordbCollectionsGetStatsResponse
from .types.post_v2vectordb_collections_has_response import PostV2VectordbCollectionsHasResponse
from .types.post_v2vectordb_collections_list_response import PostV2VectordbCollectionsListResponse
from .types.post_v2vectordb_collections_load_response import PostV2VectordbCollectionsLoadResponse
from .types.post_v2vectordb_collections_release_response import PostV2VectordbCollectionsReleaseResponse
from .types.post_v2vectordb_collections_rename_response import PostV2VectordbCollectionsRenameResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCollectionOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def has_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbCollectionsHasResponse]:
        """
        This operation checks whether a collection exists.

        Parameters
        ----------
        db_name : str
            The name of the database in which to check the existence of a collection.

        collection_name : str
            The name of an existing collection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsHasResponse]
            A boolean value indicates whether the specified partition exists.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/has",
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
                    PostV2VectordbCollectionsHasResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsHasResponse,
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

    def rename_collection(
        self,
        *,
        collection_name: str,
        new_collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        new_db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsRenameResponse]:
        """
        This operation renames an existing collection and optionally moves the collection to a new database.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        new_collection_name : str
            The name of the target collection after this operation.
            Setting this to the value of **old_collection_name** results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        new_db_name : typing.Optional[str]
            The name of the database to which the collection belongs after this operation.
            The value defaults to **default**. Setting this to a database rather than the one the collection belongs to before this operation moves this collection to the specified database.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsRenameResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/rename",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "newDbName": new_db_name,
                "newCollectionName": new_collection_name,
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
                    PostV2VectordbCollectionsRenameResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsRenameResponse,
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

    def get_collection_stats(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbCollectionsGetStatsResponse]:
        """
        This operations gets the number of entities in a collection.

        Parameters
        ----------
        db_name : str
            The name of the database which the collection belongs to. Setting this to a non-existing database results in an error.

        collection_name : str
            The name of the collection to check.
            Setting this to a non-existing database results in an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsGetStatsResponse]
            The number of entities in a collection.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/get_stats",
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
                    PostV2VectordbCollectionsGetStatsResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsGetStatsResponse,
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

    def load_collection(
        self,
        *,
        request_header: int,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsLoadResponse]:
        """
        This operation loads the data of the current collection into memory.

        Parameters
        ----------
        request_header : int
            The timeout duration for this operation in seconds. Setting this to None indicates that this operation timeouts when any response arrives or any error occurs.

        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsLoadResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/load",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
            },
            headers={
                "content-type": "application/json",
                "Request-Header": str(request_header) if request_header is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbCollectionsLoadResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsLoadResponse,
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

    def release_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsReleaseResponse]:
        """
        This operation releases the data of the current collection from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target colletion.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the cpllection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsReleaseResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/release",
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
                    PostV2VectordbCollectionsReleaseResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsReleaseResponse,
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

    def create_collection(
        self,
        *,
        auto_id: str,
        db_name: typing.Optional[str] = OMIT,
        collection_name: typing.Optional[str] = OMIT,
        dimension: typing.Optional[int] = OMIT,
        metric_type: typing.Optional[str] = OMIT,
        id_type: typing.Optional[str] = OMIT,
        primary_field_name: typing.Optional[str] = OMIT,
        vector_field_name: typing.Optional[str] = OMIT,
        schema: typing.Optional[PostV2VectordbCollectionsCreateRequestSchema] = OMIT,
        index_params: typing.Optional[typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem]] = OMIT,
        params: typing.Optional[PostV2VectordbCollectionsCreateRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsCreateResponse]:
        """
        This operation creates a collection in a specified cluster.

        Parameters
        ----------
        auto_id : str
            Whether the primary field automatically increments. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        db_name : typing.Optional[str]
            The name of the database. <zilliz>This parameter applies only to dedicated clusters.</zilliz>

        collection_name : typing.Optional[str]
            The name of the collection to create.

        dimension : typing.Optional[int]
            The number of dimensions a vector value should have.
            This is required if **dtype** of this field is set to **DataType.FLOAT_VECTOR**.

        metric_type : typing.Optional[str]
            The metric type applied to this operation.
            Possible values are **L2**, **IP**, and **COSINE**.

        id_type : typing.Optional[str]
            The data type of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        primary_field_name : typing.Optional[str]
            The name of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        vector_field_name : typing.Optional[str]
            The name of the vector field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        schema : typing.Optional[PostV2VectordbCollectionsCreateRequestSchema]
            The schema is responsible for organizing data in the target collection. A valid schema should have multiple fields, which must include a primary key, a vector field, and several scalar fields.

        index_params : typing.Optional[typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem]]
            The parameters that apply to the index-building process.

        params : typing.Optional[PostV2VectordbCollectionsCreateRequestParams]
            Extra parameters for the collection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsCreateResponse]
            Returns A collection object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "dimension": dimension,
                "metricType": metric_type,
                "idType": id_type,
                "autoID": auto_id,
                "primaryFieldName": primary_field_name,
                "vectorFieldName": vector_field_name,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=PostV2VectordbCollectionsCreateRequestSchema, direction="write"
                ),
                "indexParams": convert_and_respect_annotation_metadata(
                    object_=index_params,
                    annotation=typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem],
                    direction="write",
                ),
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostV2VectordbCollectionsCreateRequestParams, direction="write"
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
                    PostV2VectordbCollectionsCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsCreateResponse,
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

    def get_collection_load_state(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsGetLoadStateResponse]:
        """
        This operation returns the load status of a specific collection.

        Parameters
        ----------
        collection_name : str
            The name of a collection.

        db_name : typing.Optional[str]
            The name of a database to which the collection belongs.

        partition_names : typing.Optional[str]
            A list of partition names. If any partition names are specified, releasing any of these partitions results in the return of a NotLoad state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsGetLoadStateResponse]
            A LoadState object that indicates the load status of the specified collection.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/get_load_state",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbCollectionsGetLoadStateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsGetLoadStateResponse,
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

    def list_collections(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbCollectionsListResponse]:
        """
        This operation lists all collections in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of an existing database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsListResponse]
            This operation lists all collections in the database used in the current connection.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/list",
            method="POST",
            json={
                "dbName": db_name,
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
                    PostV2VectordbCollectionsListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsListResponse,
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

    def describe_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbCollectionsDescribeResponse]:
        """
        Describes the details of a collection.

        Parameters
        ----------
        db_name : str
            The name of the database.

        collection_name : str
            The name of the collection to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsDescribeResponse]
            Returns the specified collection in detail.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/describe",
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
                    PostV2VectordbCollectionsDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsDescribeResponse,
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

    def drop_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbCollectionsDropResponse]:
        """
        This operation drops the current collection and all data within the collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbCollectionsDropResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/drop",
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
                    PostV2VectordbCollectionsDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsDropResponse,
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


class AsyncRawCollectionOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def has_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsHasResponse]:
        """
        This operation checks whether a collection exists.

        Parameters
        ----------
        db_name : str
            The name of the database in which to check the existence of a collection.

        collection_name : str
            The name of an existing collection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsHasResponse]
            A boolean value indicates whether the specified partition exists.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/has",
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
                    PostV2VectordbCollectionsHasResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsHasResponse,
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

    async def rename_collection(
        self,
        *,
        collection_name: str,
        new_collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        new_db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsRenameResponse]:
        """
        This operation renames an existing collection and optionally moves the collection to a new database.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        new_collection_name : str
            The name of the target collection after this operation.
            Setting this to the value of **old_collection_name** results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        new_db_name : typing.Optional[str]
            The name of the database to which the collection belongs after this operation.
            The value defaults to **default**. Setting this to a database rather than the one the collection belongs to before this operation moves this collection to the specified database.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsRenameResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/rename",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "newDbName": new_db_name,
                "newCollectionName": new_collection_name,
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
                    PostV2VectordbCollectionsRenameResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsRenameResponse,
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

    async def get_collection_stats(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsGetStatsResponse]:
        """
        This operations gets the number of entities in a collection.

        Parameters
        ----------
        db_name : str
            The name of the database which the collection belongs to. Setting this to a non-existing database results in an error.

        collection_name : str
            The name of the collection to check.
            Setting this to a non-existing database results in an error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsGetStatsResponse]
            The number of entities in a collection.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/get_stats",
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
                    PostV2VectordbCollectionsGetStatsResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsGetStatsResponse,
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

    async def load_collection(
        self,
        *,
        request_header: int,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsLoadResponse]:
        """
        This operation loads the data of the current collection into memory.

        Parameters
        ----------
        request_header : int
            The timeout duration for this operation in seconds. Setting this to None indicates that this operation timeouts when any response arrives or any error occurs.

        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsLoadResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/load",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
            },
            headers={
                "content-type": "application/json",
                "Request-Header": str(request_header) if request_header is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbCollectionsLoadResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsLoadResponse,
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

    async def release_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsReleaseResponse]:
        """
        This operation releases the data of the current collection from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target colletion.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the cpllection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsReleaseResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/release",
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
                    PostV2VectordbCollectionsReleaseResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsReleaseResponse,
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

    async def create_collection(
        self,
        *,
        auto_id: str,
        db_name: typing.Optional[str] = OMIT,
        collection_name: typing.Optional[str] = OMIT,
        dimension: typing.Optional[int] = OMIT,
        metric_type: typing.Optional[str] = OMIT,
        id_type: typing.Optional[str] = OMIT,
        primary_field_name: typing.Optional[str] = OMIT,
        vector_field_name: typing.Optional[str] = OMIT,
        schema: typing.Optional[PostV2VectordbCollectionsCreateRequestSchema] = OMIT,
        index_params: typing.Optional[typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem]] = OMIT,
        params: typing.Optional[PostV2VectordbCollectionsCreateRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsCreateResponse]:
        """
        This operation creates a collection in a specified cluster.

        Parameters
        ----------
        auto_id : str
            Whether the primary field automatically increments. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        db_name : typing.Optional[str]
            The name of the database. <zilliz>This parameter applies only to dedicated clusters.</zilliz>

        collection_name : typing.Optional[str]
            The name of the collection to create.

        dimension : typing.Optional[int]
            The number of dimensions a vector value should have.
            This is required if **dtype** of this field is set to **DataType.FLOAT_VECTOR**.

        metric_type : typing.Optional[str]
            The metric type applied to this operation.
            Possible values are **L2**, **IP**, and **COSINE**.

        id_type : typing.Optional[str]
            The data type of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        primary_field_name : typing.Optional[str]
            The name of the primary field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        vector_field_name : typing.Optional[str]
            The name of the vector field. This parameter is designed for the quick-setup of a collection and will be ignored if __schema__ is defined.

        schema : typing.Optional[PostV2VectordbCollectionsCreateRequestSchema]
            The schema is responsible for organizing data in the target collection. A valid schema should have multiple fields, which must include a primary key, a vector field, and several scalar fields.

        index_params : typing.Optional[typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem]]
            The parameters that apply to the index-building process.

        params : typing.Optional[PostV2VectordbCollectionsCreateRequestParams]
            Extra parameters for the collection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsCreateResponse]
            Returns A collection object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "dimension": dimension,
                "metricType": metric_type,
                "idType": id_type,
                "autoID": auto_id,
                "primaryFieldName": primary_field_name,
                "vectorFieldName": vector_field_name,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=PostV2VectordbCollectionsCreateRequestSchema, direction="write"
                ),
                "indexParams": convert_and_respect_annotation_metadata(
                    object_=index_params,
                    annotation=typing.Sequence[PostV2VectordbCollectionsCreateRequestIndexParamsItem],
                    direction="write",
                ),
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostV2VectordbCollectionsCreateRequestParams, direction="write"
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
                    PostV2VectordbCollectionsCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsCreateResponse,
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

    async def get_collection_load_state(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsGetLoadStateResponse]:
        """
        This operation returns the load status of a specific collection.

        Parameters
        ----------
        collection_name : str
            The name of a collection.

        db_name : typing.Optional[str]
            The name of a database to which the collection belongs.

        partition_names : typing.Optional[str]
            A list of partition names. If any partition names are specified, releasing any of these partitions results in the return of a NotLoad state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsGetLoadStateResponse]
            A LoadState object that indicates the load status of the specified collection.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/get_load_state",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbCollectionsGetLoadStateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsGetLoadStateResponse,
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

    async def list_collections(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsListResponse]:
        """
        This operation lists all collections in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of an existing database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsListResponse]
            This operation lists all collections in the database used in the current connection.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/list",
            method="POST",
            json={
                "dbName": db_name,
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
                    PostV2VectordbCollectionsListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsListResponse,
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

    async def describe_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsDescribeResponse]:
        """
        Describes the details of a collection.

        Parameters
        ----------
        db_name : str
            The name of the database.

        collection_name : str
            The name of the collection to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsDescribeResponse]
            Returns the specified collection in detail.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/describe",
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
                    PostV2VectordbCollectionsDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsDescribeResponse,
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

    async def drop_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbCollectionsDropResponse]:
        """
        This operation drops the current collection and all data within the collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbCollectionsDropResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/collections/drop",
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
                    PostV2VectordbCollectionsDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbCollectionsDropResponse,
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
