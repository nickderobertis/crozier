

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_v1vector_delete_request_id import PostV1VectorDeleteRequestId
from .types.post_v1vector_delete_response import PostV1VectorDeleteResponse
from .types.post_v1vector_get_request_id import PostV1VectorGetRequestId
from .types.post_v1vector_get_response import PostV1VectorGetResponse
from .types.post_v1vector_insert_request_data import PostV1VectorInsertRequestData
from .types.post_v1vector_insert_response import PostV1VectorInsertResponse
from .types.post_v1vector_query_response import PostV1VectorQueryResponse
from .types.post_v1vector_search_request_params import PostV1VectorSearchRequestParams
from .types.post_v1vector_search_response import PostV1VectorSearchResponse
from .types.post_v1vector_upsert_request_data import PostV1VectorUpsertRequestData
from .types.post_v1vector_upsert_response import PostV1VectorUpsertResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVectorOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete(
        self,
        *,
        collection_name: str,
        id: PostV1VectorDeleteRequestId,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorDeleteResponse]:
        """
        Deletes one or more entities from a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV1VectorDeleteRequestId

        db_name : typing.Optional[str]
            The name of the database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorDeleteResponse]
            Returns an empty object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/delete",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV1VectorDeleteRequestId, direction="write"
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
                    PostV1VectorDeleteResponse,
                    parse_obj_as(
                        type_=PostV1VectorDeleteResponse,
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

    def insert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorInsertResponse]:
        """
        Inserts one or more entities into a collection. You can add a maximum of 100 entities at a time. To insert large volumn of data, you are advised to use the bulk-insert API. For details, refer to [Data Import](/docs/data-import).

        Parameters
        ----------
        collection_name : str
            The name of the collection to which entities will be inserted.

        data : PostV1VectorInsertRequestData
            An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema

        db_name : typing.Optional[str]
            The name of the database.

        partition_name : typing.Optional[str]
            The name of the partition to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorInsertResponse]
            Returns the number of inserted entities and an array of their IDs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/insert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV1VectorInsertRequestData, direction="write"
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
                    PostV1VectorInsertResponse,
                    parse_obj_as(
                        type_=PostV1VectorInsertResponse,
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

    def upsert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorUpsertResponse]:
        """
        Upserts one or more entities into a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which entities will be upserted.

        data : PostV1VectorUpsertRequestData
            An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema

        db_name : typing.Optional[str]
            The name of the database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorUpsertResponse]
            Returns the number of inserted entities and an array of their IDs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/upsert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV1VectorUpsertRequestData, direction="write"
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
                    PostV1VectorUpsertResponse,
                    parse_obj_as(
                        type_=PostV1VectorUpsertResponse,
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

    def search(
        self,
        *,
        collection_name: str,
        vector: typing.Sequence[float],
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        params: typing.Optional[PostV1VectorSearchRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorSearchResponse]:
        """
        Conducts a similarity search on the vector field in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[float]
            The query vector in the form of a list of floating numbers. The length of the query vector should match the dimension of the vector field in the collection.

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies. Setting this parameter indicates that the search scope should be limited to the specified partitions. If not specified, the search scope is the entire collection.

        filter : typing.Optional[str]
            The filter used to find matches for the search

        limit : typing.Optional[int]
            The maximum number of entities to return.
            The sum of this value of that of `offset` should be less than **16,384**.

        offset : typing.Optional[int]
            The number of entities to skip in the search results.<br>The sum of this value and that of `limit` should not be greater than **16,384**.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        params : typing.Optional[PostV1VectorSearchRequestParams]
            List of search parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorSearchResponse]
            Returns the search results.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/search",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "outputFields": output_fields,
                "vector": vector,
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostV1VectorSearchRequestParams, direction="write"
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
                    PostV1VectorSearchResponse,
                    parse_obj_as(
                        type_=PostV1VectorSearchResponse,
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

    def query(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorQueryResponse]:
        """
        Conducts a query on scalar fields in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        filter : str
            The filter used to find matches for the query.

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        limit : typing.Optional[int]
            The maximum number of entities to return.<br/>The sum of this value and that of `offset` should be less than **16384**.

        offset : typing.Optional[int]
            The number of entities to skip in the search results.<br/>The sum of this value and that of `limit` should be less than **16384**.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results. When setting this to `count(*)`, you need to set `limit` to 0 to get the total count of the entities that match the filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorQueryResponse]
            Returns the query results.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/query",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "outputFields": output_fields,
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
                    PostV1VectorQueryResponse,
                    parse_obj_as(
                        type_=PostV1VectorQueryResponse,
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

    def get(
        self,
        *,
        collection_name: str,
        id: PostV1VectorGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1VectorGetResponse]:
        """
        Gets entities by the specified IDs. You can set an ID in string or integer or set a set of IDs in a list of strings or a list of integers as shown in the four types of request bodies below.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV1VectorGetRequestId

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies. Setting this indicates that the operation should be applied to only these partitions. If not set, the operation will be applied to all partitions in the collection.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the query results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1VectorGetResponse]
            Returns the query results.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector/get",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "outputFields": output_fields,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV1VectorGetRequestId, direction="write"
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
                    PostV1VectorGetResponse,
                    parse_obj_as(
                        type_=PostV1VectorGetResponse,
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


class AsyncRawVectorOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete(
        self,
        *,
        collection_name: str,
        id: PostV1VectorDeleteRequestId,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorDeleteResponse]:
        """
        Deletes one or more entities from a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV1VectorDeleteRequestId

        db_name : typing.Optional[str]
            The name of the database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorDeleteResponse]
            Returns an empty object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/delete",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV1VectorDeleteRequestId, direction="write"
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
                    PostV1VectorDeleteResponse,
                    parse_obj_as(
                        type_=PostV1VectorDeleteResponse,
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

    async def insert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorInsertResponse]:
        """
        Inserts one or more entities into a collection. You can add a maximum of 100 entities at a time. To insert large volumn of data, you are advised to use the bulk-insert API. For details, refer to [Data Import](/docs/data-import).

        Parameters
        ----------
        collection_name : str
            The name of the collection to which entities will be inserted.

        data : PostV1VectorInsertRequestData
            An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema

        db_name : typing.Optional[str]
            The name of the database.

        partition_name : typing.Optional[str]
            The name of the partition to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorInsertResponse]
            Returns the number of inserted entities and an array of their IDs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/insert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV1VectorInsertRequestData, direction="write"
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
                    PostV1VectorInsertResponse,
                    parse_obj_as(
                        type_=PostV1VectorInsertResponse,
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

    async def upsert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorUpsertResponse]:
        """
        Upserts one or more entities into a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which entities will be upserted.

        data : PostV1VectorUpsertRequestData
            An entity object or an array of entity objects. Note that the keys in an entity object should match the collection schema

        db_name : typing.Optional[str]
            The name of the database.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorUpsertResponse]
            Returns the number of inserted entities and an array of their IDs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/upsert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV1VectorUpsertRequestData, direction="write"
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
                    PostV1VectorUpsertResponse,
                    parse_obj_as(
                        type_=PostV1VectorUpsertResponse,
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

    async def search(
        self,
        *,
        collection_name: str,
        vector: typing.Sequence[float],
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        params: typing.Optional[PostV1VectorSearchRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorSearchResponse]:
        """
        Conducts a similarity search on the vector field in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[float]
            The query vector in the form of a list of floating numbers. The length of the query vector should match the dimension of the vector field in the collection.

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies. Setting this parameter indicates that the search scope should be limited to the specified partitions. If not specified, the search scope is the entire collection.

        filter : typing.Optional[str]
            The filter used to find matches for the search

        limit : typing.Optional[int]
            The maximum number of entities to return.
            The sum of this value of that of `offset` should be less than **16,384**.

        offset : typing.Optional[int]
            The number of entities to skip in the search results.<br>The sum of this value and that of `limit` should not be greater than **16,384**.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        params : typing.Optional[PostV1VectorSearchRequestParams]
            List of search parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorSearchResponse]
            Returns the search results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/search",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "outputFields": output_fields,
                "vector": vector,
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostV1VectorSearchRequestParams, direction="write"
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
                    PostV1VectorSearchResponse,
                    parse_obj_as(
                        type_=PostV1VectorSearchResponse,
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

    async def query(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorQueryResponse]:
        """
        Conducts a query on scalar fields in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        filter : str
            The filter used to find matches for the query.

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        limit : typing.Optional[int]
            The maximum number of entities to return.<br/>The sum of this value and that of `offset` should be less than **16384**.

        offset : typing.Optional[int]
            The number of entities to skip in the search results.<br/>The sum of this value and that of `limit` should be less than **16384**.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results. When setting this to `count(*)`, you need to set `limit` to 0 to get the total count of the entities that match the filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorQueryResponse]
            Returns the query results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/query",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "outputFields": output_fields,
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
                    PostV1VectorQueryResponse,
                    parse_obj_as(
                        type_=PostV1VectorQueryResponse,
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

    async def get(
        self,
        *,
        collection_name: str,
        id: PostV1VectorGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1VectorGetResponse]:
        """
        Gets entities by the specified IDs. You can set an ID in string or integer or set a set of IDs in a list of strings or a list of integers as shown in the four types of request bodies below.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV1VectorGetRequestId

        db_name : typing.Optional[str]
            The name of the database.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies. Setting this indicates that the operation should be applied to only these partitions. If not set, the operation will be applied to all partitions in the collection.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the query results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1VectorGetResponse]
            Returns the query results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector/get",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
                "outputFields": output_fields,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV1VectorGetRequestId, direction="write"
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
                    PostV1VectorGetResponse,
                    parse_obj_as(
                        type_=PostV1VectorGetResponse,
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
