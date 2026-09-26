

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.index_param import IndexParam
from .raw_client import AsyncRawIndexOperationsV2Client, RawIndexOperationsV2Client
from .types.post_v2vectordb_indexes_describe_response import PostV2VectordbIndexesDescribeResponse
from .types.post_v2vectordb_indexes_list_response import PostV2VectordbIndexesListResponse


OMIT = typing.cast(typing.Any, ...)


class IndexOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndexOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndexOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndexOperationsV2Client
        """
        return self._raw_client

    def create_index(
        self,
        *,
        collection_name: str,
        index_params: typing.Sequence[IndexParam],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This creates a named index for a target field, which can either be a vector field or a scalar field.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_params : typing.Sequence[IndexParam]
              The parameters that apply to the index-building process.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            A Status object indicating whether this operation succeeds.

        Examples
        --------
        from fern import FernApi, IndexParam

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.index_operations_v2.create_index(
            collection_name="collectionName",
            index_params=[
                IndexParam(
                    metric_type="metricType",
                    field_name="fieldName",
                    index_name="indexName",
                ),
                IndexParam(
                    metric_type="metricType",
                    field_name="fieldName",
                    index_name="indexName",
                ),
            ],
        )
        """
        _response = self._raw_client.create_index(
            collection_name=collection_name, index_params=index_params, db_name=db_name, request_options=request_options
        )
        return _response.data

    def drop_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.index_operations_v2.drop_index(
            collection_name="collectionName",
            index_name="indexName",
        )
        """
        _response = self._raw_client.drop_index(
            collection_name=collection_name, index_name=index_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    def describe_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbIndexesDescribeResponse:
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
        PostV2VectordbIndexesDescribeResponse
            An object that contains the detailed description of the current index.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.index_operations_v2.describe_index(
            collection_name="collectionName",
            index_name="indexName",
        )
        """
        _response = self._raw_client.describe_index(
            collection_name=collection_name, index_name=index_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    def list_indexes(
        self,
        *,
        db_name: str,
        collection_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbIndexesListResponse:
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
        PostV2VectordbIndexesListResponse
            The names of all built indexes in a list.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.index_operations_v2.list_indexes(
            db_name="dbName",
        )
        """
        _response = self._raw_client.list_indexes(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data


class AsyncIndexOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndexOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndexOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndexOperationsV2Client
        """
        return self._raw_client

    async def create_index(
        self,
        *,
        collection_name: str,
        index_params: typing.Sequence[IndexParam],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This creates a named index for a target field, which can either be a vector field or a scalar field.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        index_params : typing.Sequence[IndexParam]
              The parameters that apply to the index-building process.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            A Status object indicating whether this operation succeeds.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IndexParam

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.index_operations_v2.create_index(
                collection_name="collectionName",
                index_params=[
                    IndexParam(
                        metric_type="metricType",
                        field_name="fieldName",
                        index_name="indexName",
                    ),
                    IndexParam(
                        metric_type="metricType",
                        field_name="fieldName",
                        index_name="indexName",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_index(
            collection_name=collection_name, index_params=index_params, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def drop_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
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
            await client.index_operations_v2.drop_index(
                collection_name="collectionName",
                index_name="indexName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_index(
            collection_name=collection_name, index_name=index_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def describe_index(
        self,
        *,
        collection_name: str,
        index_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbIndexesDescribeResponse:
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
        PostV2VectordbIndexesDescribeResponse
            An object that contains the detailed description of the current index.

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
            await client.index_operations_v2.describe_index(
                collection_name="collectionName",
                index_name="indexName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_index(
            collection_name=collection_name, index_name=index_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def list_indexes(
        self,
        *,
        db_name: str,
        collection_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbIndexesListResponse:
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
        PostV2VectordbIndexesListResponse
            The names of all built indexes in a list.

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
            await client.index_operations_v2.list_indexes(
                db_name="dbName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_indexes(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data
