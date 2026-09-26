

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.has import Has
from .raw_client import AsyncRawPartitionOperationsV2Client, RawPartitionOperationsV2Client
from .types.post_v2vectordb_partitions_list_response import PostV2VectordbPartitionsListResponse


OMIT = typing.cast(typing.Any, ...)


class PartitionOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPartitionOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPartitionOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPartitionOperationsV2Client
        """
        return self._raw_client

    def list_partitions(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbPartitionsListResponse:
        """
        This operation lists all partitions in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of the target database.

        collection_name : str
            The name of the target collection to which the partition belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbPartitionsListResponse
            A list of partition names.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.partition_operations_v2.list_partitions(
            db_name="dbName",
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.list_partitions(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    def create_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation creates a partition in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

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
        client.partition_operations_v2.create_partition(
            collection_name="collectionName",
            partition_name="partitionName",
        )
        """
        _response = self._raw_client.create_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def drop_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation drops the current partition.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

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
        client.partition_operations_v2.drop_partition(
            collection_name="collectionName",
            partition_name="partitionName",
        )
        """
        _response = self._raw_client.drop_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def load_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation loads the data of the current partition into memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

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
        client.partition_operations_v2.load_partitions(
            collection_name="collectionName",
            partition_names=["partitionNames", "partitionNames"],
        )
        """
        _response = self._raw_client.load_partitions(
            collection_name=collection_name,
            partition_names=partition_names,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def release_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation releases the data of the current partition from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

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
        client.partition_operations_v2.release_partitions(
            collection_name="collectionName",
            partition_names=["partitionNames", "partitionNames"],
        )
        """
        _response = self._raw_client.release_partitions(
            collection_name=collection_name,
            partition_names=partition_names,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def has_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Has:
        """
        This operation checks whether a partition exists.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the partition to test.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Has
            A boolean value indicating whether the specified partition exists.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.partition_operations_v2.has_partition(
            collection_name="collectionName",
            partition_name="partitionName",
        )
        """
        _response = self._raw_client.has_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    def get_partition_statistics(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operations gets the number of entities in a partition.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the target partition of this operation.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            成功

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.partition_operations_v2.get_partition_statistics(
            collection_name="collectionName",
            partition_name="partitionName",
        )
        """
        _response = self._raw_client.get_partition_statistics(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data


class AsyncPartitionOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPartitionOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPartitionOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPartitionOperationsV2Client
        """
        return self._raw_client

    async def list_partitions(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbPartitionsListResponse:
        """
        This operation lists all partitions in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of the target database.

        collection_name : str
            The name of the target collection to which the partition belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbPartitionsListResponse
            A list of partition names.

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
            await client.partition_operations_v2.list_partitions(
                db_name="dbName",
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_partitions(
            db_name=db_name, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    async def create_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation creates a partition in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

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
            await client.partition_operations_v2.create_partition(
                collection_name="collectionName",
                partition_name="partitionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def drop_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation drops the current partition.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

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
            await client.partition_operations_v2.drop_partition(
                collection_name="collectionName",
                partition_name="partitionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def load_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation loads the data of the current partition into memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

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
            await client.partition_operations_v2.load_partitions(
                collection_name="collectionName",
                partition_names=["partitionNames", "partitionNames"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_partitions(
            collection_name=collection_name,
            partition_names=partition_names,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def release_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation releases the data of the current partition from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

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
            await client.partition_operations_v2.release_partitions(
                collection_name="collectionName",
                partition_names=["partitionNames", "partitionNames"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_partitions(
            collection_name=collection_name,
            partition_names=partition_names,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def has_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Has:
        """
        This operation checks whether a partition exists.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the partition to test.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Has
            A boolean value indicating whether the specified partition exists.

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
            await client.partition_operations_v2.has_partition(
                collection_name="collectionName",
                partition_name="partitionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.has_partition(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data

    async def get_partition_statistics(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operations gets the number of entities in a partition.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the target partition of this operation.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            成功

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
            await client.partition_operations_v2.get_partition_statistics(
                collection_name="collectionName",
                partition_name="partitionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_partition_statistics(
            collection_name=collection_name,
            partition_name=partition_name,
            db_name=db_name,
            request_options=request_options,
        )
        return _response.data
