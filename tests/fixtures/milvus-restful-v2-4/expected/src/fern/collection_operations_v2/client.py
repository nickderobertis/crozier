

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCollectionOperationsV2Client, RawCollectionOperationsV2Client
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


OMIT = typing.cast(typing.Any, ...)


class CollectionOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionOperationsV2Client
        """
        return self._raw_client

    def has_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsHasResponse:
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
        PostV2VectordbCollectionsHasResponse
            A boolean value indicates whether the specified partition exists.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.has_collection(
            db_name="dbName",
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.has_collection(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    def rename_collection(
        self,
        *,
        collection_name: str,
        new_collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        new_db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsRenameResponse:
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
        PostV2VectordbCollectionsRenameResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.rename_collection(
            collection_name="collectionName",
            new_collection_name="newCollectionName",
        )
        """
        _response = self._raw_client.rename_collection(
            collection_name=collection_name,
            new_collection_name=new_collection_name,
            db_name=db_name,
            new_db_name=new_db_name,
            request_options=request_options,
        )
        return _response.data

    def get_collection_stats(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsGetStatsResponse:
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
        PostV2VectordbCollectionsGetStatsResponse
            The number of entities in a collection.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.get_collection_stats(
            db_name="dbName",
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.get_collection_stats(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    def load_collection(
        self,
        *,
        request_header: int,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsLoadResponse:
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
        PostV2VectordbCollectionsLoadResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.load_collection(
            request_header=1,
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.load_collection(
            request_header=request_header,
            collection_name=collection_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def release_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsReleaseResponse:
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
        PostV2VectordbCollectionsReleaseResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.release_collection(
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.release_collection(
            collection_name=collection_name, db_name=db_name, request_options=request_options
        )
        return _response.data

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
    ) -> PostV2VectordbCollectionsCreateResponse:
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
        PostV2VectordbCollectionsCreateResponse
            Returns A collection object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.create_collection(
            auto_id="autoID",
        )
        """
        _response = self._raw_client.create_collection(
            auto_id=auto_id,
            db_name=db_name,
            collection_name=collection_name,
            dimension=dimension,
            metric_type=metric_type,
            id_type=id_type,
            primary_field_name=primary_field_name,
            vector_field_name=vector_field_name,
            schema=schema,
            index_params=index_params,
            params=params,
            request_options=request_options,
        )
        return _response.data

    def get_collection_load_state(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsGetLoadStateResponse:
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
        PostV2VectordbCollectionsGetLoadStateResponse
            A LoadState object that indicates the load status of the specified collection.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.get_collection_load_state(
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.get_collection_load_state(
            collection_name=collection_name,
            db_name=db_name,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    def list_collections(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsListResponse:
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
        PostV2VectordbCollectionsListResponse
            This operation lists all collections in the database used in the current connection.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.list_collections(
            db_name="dbName",
        )
        """
        _response = self._raw_client.list_collections(db_name=db_name, request_options=request_options)
        return _response.data

    def describe_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsDescribeResponse:
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
        PostV2VectordbCollectionsDescribeResponse
            Returns the specified collection in detail.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.describe_collection(
            db_name="dbName",
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.describe_collection(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    def drop_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsDropResponse:
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
        PostV2VectordbCollectionsDropResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.collection_operations_v2.drop_collection(
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.drop_collection(
            collection_name=collection_name, db_name=db_name, request_options=request_options
        )
        return _response.data


class AsyncCollectionOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionOperationsV2Client
        """
        return self._raw_client

    async def has_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsHasResponse:
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
        PostV2VectordbCollectionsHasResponse
            A boolean value indicates whether the specified partition exists.

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
            await client.collection_operations_v2.has_collection(
                db_name="dbName",
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.has_collection(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    async def rename_collection(
        self,
        *,
        collection_name: str,
        new_collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        new_db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsRenameResponse:
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
        PostV2VectordbCollectionsRenameResponse
            None

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
            await client.collection_operations_v2.rename_collection(
                collection_name="collectionName",
                new_collection_name="newCollectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename_collection(
            collection_name=collection_name,
            new_collection_name=new_collection_name,
            db_name=db_name,
            new_db_name=new_db_name,
            request_options=request_options,
        )
        return _response.data

    async def get_collection_stats(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsGetStatsResponse:
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
        PostV2VectordbCollectionsGetStatsResponse
            The number of entities in a collection.

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
            await client.collection_operations_v2.get_collection_stats(
                db_name="dbName",
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_stats(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    async def load_collection(
        self,
        *,
        request_header: int,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsLoadResponse:
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
        PostV2VectordbCollectionsLoadResponse
            None

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
            await client.collection_operations_v2.load_collection(
                request_header=1,
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_collection(
            request_header=request_header,
            collection_name=collection_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def release_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsReleaseResponse:
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
        PostV2VectordbCollectionsReleaseResponse
            None

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
            await client.collection_operations_v2.release_collection(
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_collection(
            collection_name=collection_name, db_name=db_name, request_options=request_options
        )
        return _response.data

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
    ) -> PostV2VectordbCollectionsCreateResponse:
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
        PostV2VectordbCollectionsCreateResponse
            Returns A collection object.

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
            await client.collection_operations_v2.create_collection(
                auto_id="autoID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            auto_id=auto_id,
            db_name=db_name,
            collection_name=collection_name,
            dimension=dimension,
            metric_type=metric_type,
            id_type=id_type,
            primary_field_name=primary_field_name,
            vector_field_name=vector_field_name,
            schema=schema,
            index_params=index_params,
            params=params,
            request_options=request_options,
        )
        return _response.data

    async def get_collection_load_state(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        partition_names: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsGetLoadStateResponse:
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
        PostV2VectordbCollectionsGetLoadStateResponse
            A LoadState object that indicates the load status of the specified collection.

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
            await client.collection_operations_v2.get_collection_load_state(
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_load_state(
            collection_name=collection_name,
            db_name=db_name,
            partition_names=partition_names,
            request_options=request_options,
        )
        return _response.data

    async def list_collections(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsListResponse:
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
        PostV2VectordbCollectionsListResponse
            This operation lists all collections in the database used in the current connection.

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
            await client.collection_operations_v2.list_collections(
                db_name="dbName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_collections(db_name=db_name, request_options=request_options)
        return _response.data

    async def describe_collection(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbCollectionsDescribeResponse:
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
        PostV2VectordbCollectionsDescribeResponse
            Returns the specified collection in detail.

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
            await client.collection_operations_v2.describe_collection(
                db_name="dbName",
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_collection(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    async def drop_collection(
        self,
        *,
        collection_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbCollectionsDropResponse:
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
        PostV2VectordbCollectionsDropResponse
            None

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
            await client.collection_operations_v2.drop_collection(
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_collection(
            collection_name=collection_name, db_name=db_name, request_options=request_options
        )
        return _response.data
