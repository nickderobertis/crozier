

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.httpapi_generic_resp_customer_delete_resp import HttpapiGenericRespCustomerDeleteResp
from ..types.httpapi_generic_resp_customer_insert_resp import HttpapiGenericRespCustomerInsertResp
from ..types.httpapi_generic_resp_customer_upsert_resp import HttpapiGenericRespCustomerUpsertResp
from ..types.search_params import SearchParams
from ..types.vector import Vector
from .raw_client import AsyncRawVectorOperationsV2Client, RawVectorOperationsV2Client
from .types.post_v2vectordb_entities_get_request_id import PostV2VectordbEntitiesGetRequestId
from .types.post_v2vectordb_entities_get_response import PostV2VectordbEntitiesGetResponse
from .types.post_v2vectordb_entities_insert_request_data import PostV2VectordbEntitiesInsertRequestData
from .types.post_v2vectordb_entities_query_response import PostV2VectordbEntitiesQueryResponse
from .types.post_v2vectordb_entities_search_response import PostV2VectordbEntitiesSearchResponse
from .types.post_v2vectordb_entities_upsert_request_data import PostV2VectordbEntitiesUpsertRequestData


OMIT = typing.cast(typing.Any, ...)


class VectorOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVectorOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVectorOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVectorOperationsV2Client
        """
        return self._raw_client

    def delete(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerDeleteResp:
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
        HttpapiGenericRespCustomerDeleteResp
            A dictionary contains the number of deleted entities.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.delete(
            collection_name="collectionName",
            filter="filter",
        )
        """
        _response = self._raw_client.delete(
            collection_name=collection_name,
            filter=filter,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    def insert(
        self,
        *,
        collection_name: str,
        data: PostV2VectordbEntitiesInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerInsertResp:
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
        HttpapiGenericRespCustomerInsertResp
            A dictionary contains information about the number of inserted entities.

        Examples
        --------
        from fern.vector_operations_v2 import (
            PostV2VectordbEntitiesInsertRequestDataZero,
        )

        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.insert(
            collection_name="collectionName",
            data=PostV2VectordbEntitiesInsertRequestDataZero(),
        )
        """
        _response = self._raw_client.insert(
            collection_name=collection_name,
            data=data,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    def query(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesQueryResponse:
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
        PostV2VectordbEntitiesQueryResponse
            A list of dictionaries with each dictionary representing a queried entity.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.query(
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.query(
            collection_name=collection_name,
            db_name=db_name,
            filter=filter,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    def upsert(
        self,
        *,
        collection_name: str,
        data: PostV2VectordbEntitiesUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerUpsertResp:
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
        HttpapiGenericRespCustomerUpsertResp
            A MutationResult object.

        Examples
        --------
        from fern.vector_operations_v2 import (
            PostV2VectordbEntitiesUpsertRequestDataZero,
        )

        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.upsert(
            collection_name="collectionName",
            data=PostV2VectordbEntitiesUpsertRequestDataZero(),
        )
        """
        _response = self._raw_client.upsert(
            collection_name=collection_name,
            data=data,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        *,
        collection_name: str,
        id: PostV2VectordbEntitiesGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesGetResponse:
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
        PostV2VectordbEntitiesGetResponse
            A list of dictionaries with each dictionary representing a queried entity.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.get(
            collection_name="collectionName",
            id=1,
        )
        """
        _response = self._raw_client.get(
            collection_name=collection_name,
            id=id,
            db_name=db_name,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    def search(
        self,
        *,
        collection_name: str,
        vector: typing.Sequence[Vector],
        search_params: SearchParams,
        db_name: typing.Optional[str] = OMIT,
        anns_field: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        grouping_field: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesSearchResponse:
        """
        This operation conducts a vector similarity search with an optional scalar filtering expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[Vector]
            A list of vector embeddings.
            <include target="milvus">Milvus</include><include target="zilliz">Zilliz Cloud</include> searches for the most similar vector embeddings to the specified ones.

        search_params : SearchParams
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
        PostV2VectordbEntitiesSearchResponse
            Returns the search results.

        Examples
        --------
        from fern import FernApi, SearchParams

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations_v2.search(
            collection_name="collectionName",
            vector=[[1]],
            search_params=SearchParams(),
        )
        """
        _response = self._raw_client.search(
            collection_name=collection_name,
            vector=vector,
            search_params=search_params,
            db_name=db_name,
            anns_field=anns_field,
            filter=filter,
            limit=limit,
            offset=offset,
            grouping_field=grouping_field,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data


class AsyncVectorOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVectorOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVectorOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVectorOperationsV2Client
        """
        return self._raw_client

    async def delete(
        self,
        *,
        collection_name: str,
        filter: str,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerDeleteResp:
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
        HttpapiGenericRespCustomerDeleteResp
            A dictionary contains the number of deleted entities.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.delete(
                collection_name="collectionName",
                filter="filter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            collection_name=collection_name,
            filter=filter,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    async def insert(
        self,
        *,
        collection_name: str,
        data: PostV2VectordbEntitiesInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerInsertResp:
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
        HttpapiGenericRespCustomerInsertResp
            A dictionary contains information about the number of inserted entities.

        Examples
        --------
        import asyncio

        from fern.vector_operations_v2 import (
            PostV2VectordbEntitiesInsertRequestDataZero,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.insert(
                collection_name="collectionName",
                data=PostV2VectordbEntitiesInsertRequestDataZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.insert(
            collection_name=collection_name,
            data=data,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    async def query(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesQueryResponse:
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
        PostV2VectordbEntitiesQueryResponse
            A list of dictionaries with each dictionary representing a queried entity.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.query(
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query(
            collection_name=collection_name,
            db_name=db_name,
            filter=filter,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    async def upsert(
        self,
        *,
        collection_name: str,
        data: PostV2VectordbEntitiesUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpapiGenericRespCustomerUpsertResp:
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
        HttpapiGenericRespCustomerUpsertResp
            A MutationResult object.

        Examples
        --------
        import asyncio

        from fern.vector_operations_v2 import (
            PostV2VectordbEntitiesUpsertRequestDataZero,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.upsert(
                collection_name="collectionName",
                data=PostV2VectordbEntitiesUpsertRequestDataZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            collection_name=collection_name,
            data=data,
            db_name=db_name,
            partition_name=partition_name,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        *,
        collection_name: str,
        id: PostV2VectordbEntitiesGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesGetResponse:
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
        PostV2VectordbEntitiesGetResponse
            A list of dictionaries with each dictionary representing a queried entity.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.get(
                collection_name="collectionName",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            collection_name=collection_name,
            id=id,
            db_name=db_name,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    async def search(
        self,
        *,
        collection_name: str,
        vector: typing.Sequence[Vector],
        search_params: SearchParams,
        db_name: typing.Optional[str] = OMIT,
        anns_field: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        grouping_field: typing.Optional[str] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbEntitiesSearchResponse:
        """
        This operation conducts a vector similarity search with an optional scalar filtering expression.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which this operation applies.

        vector : typing.Sequence[Vector]
            A list of vector embeddings.
            <include target="milvus">Milvus</include><include target="zilliz">Zilliz Cloud</include> searches for the most similar vector embeddings to the specified ones.

        search_params : SearchParams
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
        PostV2VectordbEntitiesSearchResponse
            Returns the search results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SearchParams

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations_v2.search(
                collection_name="collectionName",
                vector=[[1]],
                search_params=SearchParams(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            collection_name=collection_name,
            vector=vector,
            search_params=search_params,
            db_name=db_name,
            anns_field=anns_field,
            filter=filter,
            limit=limit,
            offset=offset,
            grouping_field=grouping_field,
            output_fields=output_fields,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data
