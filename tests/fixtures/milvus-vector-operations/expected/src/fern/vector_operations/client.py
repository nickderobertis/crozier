

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVectorOperationsClient, RawVectorOperationsClient
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


OMIT = typing.cast(typing.Any, ...)


class VectorOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVectorOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVectorOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVectorOperationsClient
        """
        return self._raw_client

    def delete(
        self,
        *,
        collection_name: str,
        id: PostV1VectorDeleteRequestId,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorDeleteResponse:
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
        PostV1VectorDeleteResponse
            Returns an empty object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.delete(
            db_name="default",
            collection_name="my_collection",
            id="4321034832910",
        )
        """
        _response = self._raw_client.delete(
            collection_name=collection_name, id=id, db_name=db_name, request_options=request_options
        )
        return _response.data

    def insert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorInsertResponse:
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
        PostV1VectorInsertResponse
            Returns the number of inserted entities and an array of their IDs.

        Examples
        --------
        from fern.vector_operations import PostV1VectorInsertRequestDataZero

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.insert(
            collection_name="my_collection",
            data=PostV1VectorInsertRequestDataZero(),
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

    def upsert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorUpsertResponse:
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
        PostV1VectorUpsertResponse
            Returns the number of inserted entities and an array of their IDs.

        Examples
        --------
        from fern.vector_operations import PostV1VectorUpsertRequestDataZero

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.upsert(
            collection_name="quick_setup",
            data=PostV1VectorUpsertRequestDataZero(),
        )
        """
        _response = self._raw_client.upsert(
            collection_name=collection_name, data=data, db_name=db_name, request_options=request_options
        )
        return _response.data

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
    ) -> PostV1VectorSearchResponse:
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
        PostV1VectorSearchResponse
            Returns the search results.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.search(
            collection_name="quick_setup",
            limit=3,
            output_fields=["color"],
            vector=[1.1],
        )
        """
        _response = self._raw_client.search(
            collection_name=collection_name,
            vector=vector,
            db_name=db_name,
            partition_names=partition_names,
            filter=filter,
            limit=limit,
            offset=offset,
            output_fields=output_fields,
            params=params,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostV1VectorQueryResponse:
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
        PostV1VectorQueryResponse
            Returns the query results.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.query(
            collection_name="medium_articles",
            filter="id in [443300716234671427, 443300716234671426]",
            limit=100,
            offset=0,
            output_fields=["id", "title", "link"],
        )
        """
        _response = self._raw_client.query(
            collection_name=collection_name,
            filter=filter,
            db_name=db_name,
            partition_names=partition_names,
            limit=limit,
            offset=offset,
            output_fields=output_fields,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        *,
        collection_name: str,
        id: PostV1VectorGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorGetResponse:
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
        PostV1VectorGetResponse
            Returns the query results.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_operations.get(
            collection_name="quick_setup",
            output_fields=["color"],
            id=[1, 3, 5],
        )
        """
        _response = self._raw_client.get(
            collection_name=collection_name,
            id=id,
            db_name=db_name,
            partition_names=partition_names,
            output_fields=output_fields,
            request_options=request_options,
        )
        return _response.data


class AsyncVectorOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVectorOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVectorOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVectorOperationsClient
        """
        return self._raw_client

    async def delete(
        self,
        *,
        collection_name: str,
        id: PostV1VectorDeleteRequestId,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorDeleteResponse:
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
        PostV1VectorDeleteResponse
            Returns an empty object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.delete(
                db_name="default",
                collection_name="my_collection",
                id="4321034832910",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            collection_name=collection_name, id=id, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def insert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorInsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        partition_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorInsertResponse:
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
        PostV1VectorInsertResponse
            Returns the number of inserted entities and an array of their IDs.

        Examples
        --------
        import asyncio

        from fern.vector_operations import PostV1VectorInsertRequestDataZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.insert(
                collection_name="my_collection",
                data=PostV1VectorInsertRequestDataZero(),
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

    async def upsert(
        self,
        *,
        collection_name: str,
        data: PostV1VectorUpsertRequestData,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorUpsertResponse:
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
        PostV1VectorUpsertResponse
            Returns the number of inserted entities and an array of their IDs.

        Examples
        --------
        import asyncio

        from fern.vector_operations import PostV1VectorUpsertRequestDataZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.upsert(
                collection_name="quick_setup",
                data=PostV1VectorUpsertRequestDataZero(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            collection_name=collection_name, data=data, db_name=db_name, request_options=request_options
        )
        return _response.data

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
    ) -> PostV1VectorSearchResponse:
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
        PostV1VectorSearchResponse
            Returns the search results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.search(
                collection_name="quick_setup",
                limit=3,
                output_fields=["color"],
                vector=[1.1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            collection_name=collection_name,
            vector=vector,
            db_name=db_name,
            partition_names=partition_names,
            filter=filter,
            limit=limit,
            offset=offset,
            output_fields=output_fields,
            params=params,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostV1VectorQueryResponse:
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
        PostV1VectorQueryResponse
            Returns the query results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.query(
                collection_name="medium_articles",
                filter="id in [443300716234671427, 443300716234671426]",
                limit=100,
                offset=0,
                output_fields=["id", "title", "link"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query(
            collection_name=collection_name,
            filter=filter,
            db_name=db_name,
            partition_names=partition_names,
            limit=limit,
            offset=offset,
            output_fields=output_fields,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        *,
        collection_name: str,
        id: PostV1VectorGetRequestId,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[typing.Sequence[str]] = OMIT,
        output_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1VectorGetResponse:
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
        PostV1VectorGetResponse
            Returns the query results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_operations.get(
                collection_name="quick_setup",
                output_fields=["color"],
                id=[1, 3, 5],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            collection_name=collection_name,
            id=id,
            db_name=db_name,
            partition_names=partition_names,
            output_fields=output_fields,
            request_options=request_options,
        )
        return _response.data
