

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_v2vectordb_entities_delete_response import PostV2VectordbEntitiesDeleteResponse
from .types.post_v2vectordb_entities_get_request_id import PostV2VectordbEntitiesGetRequestId
from .types.post_v2vectordb_entities_get_response import PostV2VectordbEntitiesGetResponse
from .types.post_v2vectordb_entities_insert_request_data import PostV2VectordbEntitiesInsertRequestData
from .types.post_v2vectordb_entities_insert_response import PostV2VectordbEntitiesInsertResponse
from .types.post_v2vectordb_entities_query_response import PostV2VectordbEntitiesQueryResponse
from .types.post_v2vectordb_entities_search_request_search_params import PostV2VectordbEntitiesSearchRequestSearchParams
from .types.post_v2vectordb_entities_search_request_vector_item_item import (
    PostV2VectordbEntitiesSearchRequestVectorItemItem,
)
from .types.post_v2vectordb_entities_search_response import PostV2VectordbEntitiesSearchResponse
from .types.post_v2vectordb_entities_upsert_request_data import PostV2VectordbEntitiesUpsertRequestData
from .types.post_v2vectordb_entities_upsert_response import PostV2VectordbEntitiesUpsertResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVectorOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesDeleteResponse]:
        """
        This operation deletes entities by their IDs or with a boolean expression.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        filter : str
            A scalar filtering condition to filter matching entities.    The value defaults to an empty string, indicating that no condition applies. Setting both **id** and **filter** results in an error.
            You can set this parameter to an empty string to skip scalar filtering. To build a scalar filtering condition, refer to [Boolean Expression Rules](https://milvus.io/docs/boolean.md).

        db_name : typing.Optional[str]
            The name of the target database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be deleted from the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesDeleteResponse]
            A dictionary contains the number of deleted entities.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/delete",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "filter": filter,
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesDeleteResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesDeleteResponse,
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
        data: PostV2VectordbEntitiesInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesInsertResponse]:
        """
        This operation inserts data into a specific collection. You can insert a maximum of 100 entities at a time. To insert large volumes of data, please use [the bulk-insert API](https://docs.zilliz.com/docs/data-import).

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        data : PostV2VectordbEntitiesInsertRequestData
            The data to insert into the current collection.
            The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries.

        db_name : typing.Optional[str]
            The name of the target database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be inserted into the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesInsertResponse]
            A dictionary contains information about the number of inserted entities.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/insert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV2VectordbEntitiesInsertRequestData, direction="write"
                ),
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesInsertResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesInsertResponse,
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
        db_name: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesQueryResponse]:
        """
        This operation conducts a filtering on the scalar field with a specified boolean expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        db_name : typing.Optional[str]
            The name of the database.

        filter : typing.Optional[str]
            The filter used to find matches for the search.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesQueryResponse]
            A list of dictionaries with each dictionary representing a queried entity.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/query",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "filter": filter,
                "outputFields": output_fields,
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
                    PostV2VectordbEntitiesQueryResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesQueryResponse,
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
        data: PostV2VectordbEntitiesUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesUpsertResponse]:
        """
        This operation inserts new records into the database or updates existing ones.  Currently, this endpoint does not apply to the collections that have autoId enabled.

        Parameters
        ----------
        collection_name : str
            The name of the collection in which to upsert data.

        data : PostV2VectordbEntitiesUpsertRequestData
            The data to insert into the current collection.
            The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries.

        db_name : typing.Optional[str]
            The name of the database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be inserted into the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesUpsertResponse]
            A MutationResult object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/upsert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV2VectordbEntitiesUpsertRequestData, direction="write"
                ),
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesUpsertResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesUpsertResponse,
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
        id: PostV2VectordbEntitiesGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesGetResponse]:
        """
        This operation gets specific entities by their IDs.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV2VectordbEntitiesGetRequestId
            A specific entity ID or a list of entity IDs.

        db_name : typing.Optional[str]
            The name of the database.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesGetResponse]
            A list of dictionaries with each dictionary representing a queried entity.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/get",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV2VectordbEntitiesGetRequestId, direction="write"
                ),
                "outputFields": output_fields,
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
                    PostV2VectordbEntitiesGetResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesGetResponse,
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
        vector: typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]],
        search_params: PostV2VectordbEntitiesSearchRequestSearchParams,
        db_name: typing.Optional[str] = OMIT,
        anns_field: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        grouping_field: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbEntitiesSearchResponse]:
        """
        This operation conducts a vector similarity search with an optional scalar filtering expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]]
            A list of vector embeddings.
            <include target="milvus">Milvus</include><include target="zilliz">Zilliz Cloud</include> searches for the most similar vector embeddings to the specified ones.

        search_params : PostV2VectordbEntitiesSearchRequestSearchParams
             The parameter settings specific to this operation.
            - **metric_type** (*str*) -
              -   The metric type applied to this operation. This should be the same as the one used when you index the vector field specified above.
              -   Possible values are **L2**, **IP**, and **COSINE**.
            - **params** (dict) -
              -   Additional parameters
              - **radius** (float) -
                -    Determines the threshold of least similarity. When setting `metric_type` to `L2`, ensure that this value is greater than that of **range_filter**. Otherwise, this value should be lower than that of **range_filter**.
              - **range_filter**  (float) -
                -    Refines the search to vectors within a specific similarity range. When setting `metric_type` to `IP` or `COSINE`, ensure that this value is greater than that of **radius**. Otherwise, this value should be lower than that of **radius**.
            <include target="milvus">
            For details on other applicable search parameters, refer to [In-memory Index](https://milvus.io/docs/index.md) and [On-disk Index](https://milvus.io/docs/disk_index.md).
            </include>
            <include target="zilliz">
            For details on other applicable search parameters, read [AUTOINDEX Explained](https://docs.zilliz.com/docs/autoindex-explained) to get more.
            </include>

        db_name : typing.Optional[str]
            The name of the database.

        anns_field : typing.Optional[str]

        filter : typing.Optional[str]
            The filter used to find matches for the search.

        limit : typing.Optional[int]
            The total number of entities to return.
            You can use this parameter in combination with **offset** in **param** to enable pagination.
            The sum of this value and **offset** in **param** should be less than 16,384.

        offset : typing.Optional[int]
                The number of records to skip in the search result.      You can use this parameter in combination with limit to enable pagination.     The sum of this value and limit should be less than 16,384.

        grouping_field : typing.Optional[str]
            https://zilliverse.feishu.cn/docx/S3brdwmUHoG33dxhifpcruAYnsb

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbEntitiesSearchResponse]
            Returns the search results.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/search",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "vector": convert_and_respect_annotation_metadata(
                    object_=vector,
                    annotation=typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]],
                    direction="write",
                ),
                "annsField": anns_field,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "groupingField": grouping_field,
                "outputFields": output_fields,
                "searchParams": convert_and_respect_annotation_metadata(
                    object_=search_params, annotation=PostV2VectordbEntitiesSearchRequestSearchParams, direction="write"
                ),
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
                    PostV2VectordbEntitiesSearchResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesSearchResponse,
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


class AsyncRawVectorOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesDeleteResponse]:
        """
        This operation deletes entities by their IDs or with a boolean expression.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        filter : str
            A scalar filtering condition to filter matching entities.    The value defaults to an empty string, indicating that no condition applies. Setting both **id** and **filter** results in an error.
            You can set this parameter to an empty string to skip scalar filtering. To build a scalar filtering condition, refer to [Boolean Expression Rules](https://milvus.io/docs/boolean.md).

        db_name : typing.Optional[str]
            The name of the target database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be deleted from the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesDeleteResponse]
            A dictionary contains the number of deleted entities.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/delete",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "filter": filter,
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesDeleteResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesDeleteResponse,
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
        data: PostV2VectordbEntitiesInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesInsertResponse]:
        """
        This operation inserts data into a specific collection. You can insert a maximum of 100 entities at a time. To insert large volumes of data, please use [the bulk-insert API](https://docs.zilliz.com/docs/data-import).

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        data : PostV2VectordbEntitiesInsertRequestData
            The data to insert into the current collection.
            The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries.

        db_name : typing.Optional[str]
            The name of the target database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be inserted into the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesInsertResponse]
            A dictionary contains information about the number of inserted entities.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/insert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV2VectordbEntitiesInsertRequestData, direction="write"
                ),
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesInsertResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesInsertResponse,
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
        db_name: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesQueryResponse]:
        """
        This operation conducts a filtering on the scalar field with a specified boolean expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        db_name : typing.Optional[str]
            The name of the database.

        filter : typing.Optional[str]
            The filter used to find matches for the search.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesQueryResponse]
            A list of dictionaries with each dictionary representing a queried entity.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/query",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "filter": filter,
                "outputFields": output_fields,
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
                    PostV2VectordbEntitiesQueryResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesQueryResponse,
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
        data: PostV2VectordbEntitiesUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesUpsertResponse]:
        """
        This operation inserts new records into the database or updates existing ones.  Currently, this endpoint does not apply to the collections that have autoId enabled.

        Parameters
        ----------
        collection_name : str
            The name of the collection in which to upsert data.

        data : PostV2VectordbEntitiesUpsertRequestData
            The data to insert into the current collection.
            The data to insert should be a dictionary that matches the schema of the current collection or a list of such dictionaries.

        db_name : typing.Optional[str]
            The name of the database.

        partition_name : typing.Optional[str]
            The name of a partition in the current collection.
            If specified, the data is to be inserted into the specified partition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesUpsertResponse]
            A MutationResult object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/upsert",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PostV2VectordbEntitiesUpsertRequestData, direction="write"
                ),
                "partitionName": partition_name,
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
                    PostV2VectordbEntitiesUpsertResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesUpsertResponse,
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
        id: PostV2VectordbEntitiesGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesGetResponse]:
        """
        This operation gets specific entities by their IDs.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        id : PostV2VectordbEntitiesGetRequestId
            A specific entity ID or a list of entity IDs.

        db_name : typing.Optional[str]
            The name of the database.

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesGetResponse]
            A list of dictionaries with each dictionary representing a queried entity.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/get",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=PostV2VectordbEntitiesGetRequestId, direction="write"
                ),
                "outputFields": output_fields,
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
                    PostV2VectordbEntitiesGetResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesGetResponse,
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
        vector: typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]],
        search_params: PostV2VectordbEntitiesSearchRequestSearchParams,
        db_name: typing.Optional[str] = OMIT,
        anns_field: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        grouping_field: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbEntitiesSearchResponse]:
        """
        This operation conducts a vector similarity search with an optional scalar filtering expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]]
            A list of vector embeddings.
            <include target="milvus">Milvus</include><include target="zilliz">Zilliz Cloud</include> searches for the most similar vector embeddings to the specified ones.

        search_params : PostV2VectordbEntitiesSearchRequestSearchParams
             The parameter settings specific to this operation.
            - **metric_type** (*str*) -
              -   The metric type applied to this operation. This should be the same as the one used when you index the vector field specified above.
              -   Possible values are **L2**, **IP**, and **COSINE**.
            - **params** (dict) -
              -   Additional parameters
              - **radius** (float) -
                -    Determines the threshold of least similarity. When setting `metric_type` to `L2`, ensure that this value is greater than that of **range_filter**. Otherwise, this value should be lower than that of **range_filter**.
              - **range_filter**  (float) -
                -    Refines the search to vectors within a specific similarity range. When setting `metric_type` to `IP` or `COSINE`, ensure that this value is greater than that of **radius**. Otherwise, this value should be lower than that of **radius**.
            <include target="milvus">
            For details on other applicable search parameters, refer to [In-memory Index](https://milvus.io/docs/index.md) and [On-disk Index](https://milvus.io/docs/disk_index.md).
            </include>
            <include target="zilliz">
            For details on other applicable search parameters, read [AUTOINDEX Explained](https://docs.zilliz.com/docs/autoindex-explained) to get more.
            </include>

        db_name : typing.Optional[str]
            The name of the database.

        anns_field : typing.Optional[str]

        filter : typing.Optional[str]
            The filter used to find matches for the search.

        limit : typing.Optional[int]
            The total number of entities to return.
            You can use this parameter in combination with **offset** in **param** to enable pagination.
            The sum of this value and **offset** in **param** should be less than 16,384.

        offset : typing.Optional[int]
                The number of records to skip in the search result.      You can use this parameter in combination with limit to enable pagination.     The sum of this value and limit should be less than 16,384.

        grouping_field : typing.Optional[str]
            https://zilliverse.feishu.cn/docx/S3brdwmUHoG33dxhifpcruAYnsb

        output_fields : typing.Optional[typing.Sequence[str]]
            An array of fields to return along with the search results.

        partition_names : typing.Optional[typing.Sequence[str]]
            The name of the partitions to which this operation applies.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbEntitiesSearchResponse]
            Returns the search results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/entities/search",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "vector": convert_and_respect_annotation_metadata(
                    object_=vector,
                    annotation=typing.Sequence[typing.Sequence[PostV2VectordbEntitiesSearchRequestVectorItemItem]],
                    direction="write",
                ),
                "annsField": anns_field,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "groupingField": grouping_field,
                "outputFields": output_fields,
                "searchParams": convert_and_respect_annotation_metadata(
                    object_=search_params, annotation=PostV2VectordbEntitiesSearchRequestSearchParams, direction="write"
                ),
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
                    PostV2VectordbEntitiesSearchResponse,
                    parse_obj_as(
                        type_=PostV2VectordbEntitiesSearchResponse,
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
