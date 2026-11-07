

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKvManagementApiClient, RawKvManagementApiClient
from .types.add_kv_store_request_storage import AddKvStoreRequestStorage
from .types.add_kv_store_request_x_nats_kv_storage import AddKvStoreRequestXNatsKvStorage
from .types.kv_store_info_response import KvStoreInfoResponse
from .types.kv_store_watch_request_include import KvStoreWatchRequestInclude
from .types.kv_store_watch_response import KvStoreWatchResponse


OMIT = typing.cast(typing.Any, ...)


class KvManagementApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKvManagementApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKvManagementApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKvManagementApiClient
        """
        return self._raw_client

    def list_kv_stores(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of entity names

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.list_kv_stores()
        """
        _response = self._raw_client.list_kv_stores(request_options=request_options)
        return _response.data

    def kv_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KvStoreInfoResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvStoreInfoResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.kv_store_info(
            bucket="bucket",
        )
        """
        _response = self._raw_client.kv_store_info(bucket, request_options=request_options)
        return _response.data

    def add_kv_store(
        self,
        bucket: str,
        *,
        nats_kv_max_value_size: typing.Optional[float] = None,
        nats_kv_history: typing.Optional[float] = None,
        nats_kv_ttl: typing.Optional[float] = None,
        nats_kv_max_bytes: typing.Optional[float] = None,
        nats_kv_storage: typing.Optional[AddKvStoreRequestXNatsKvStorage] = None,
        nats_kv_replicas: typing.Optional[float] = None,
        nats_kv_compression: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[AddKvStoreRequestStorage] = OMIT,
        replicas: typing.Optional[float] = OMIT,
        compression: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        nats_kv_max_value_size : typing.Optional[float]
            the maximum size for an entry (only on application/text)

        nats_kv_history : typing.Optional[float]
            the number of possible history per key (only on application/text)

        nats_kv_ttl : typing.Optional[float]
            the amount of time entries live in the bucket in nanoseconds (only on application/text)

        nats_kv_max_bytes : typing.Optional[float]
            the maximum size of the KV in bytes (only on application/text)

        nats_kv_storage : typing.Optional[AddKvStoreRequestXNatsKvStorage]
            the underlying storage for the KV (only on application/text)

        nats_kv_replicas : typing.Optional[float]
            the underlying number of replicas (only on application/text)

        nats_kv_compression : typing.Optional[bool]
            compress the KV store (only on application/text)

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[AddKvStoreRequestStorage]

        replicas : typing.Optional[float]

        compression : typing.Optional[bool]

        metadata : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.add_kv_store(
            bucket="bucket",
        )
        """
        _response = self._raw_client.add_kv_store(
            bucket,
            nats_kv_max_value_size=nats_kv_max_value_size,
            nats_kv_history=nats_kv_history,
            nats_kv_ttl=nats_kv_ttl,
            nats_kv_max_bytes=nats_kv_max_bytes,
            nats_kv_storage=nats_kv_storage,
            nats_kv_replicas=nats_kv_replicas,
            nats_kv_compression=nats_kv_compression,
            description=description,
            max_value_size=max_value_size,
            history=history,
            ttl=ttl,
            max_bytes=max_bytes,
            storage=storage,
            replicas=replicas,
            compression=compression,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def kv_store_destroy(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.kv_store_destroy(
            bucket="bucket",
        )
        """
        _response = self._raw_client.kv_store_destroy(bucket, request_options=request_options)
        return _response.data

    def kv_store_purge(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.kv_store_purge(
            bucket="bucket",
        )
        """
        _response = self._raw_client.kv_store_purge(bucket, request_options=request_options)
        return _response.data

    def kv_store_keys(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of entity names

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_management_api.kv_store_keys(
            bucket="bucket",
        )
        """
        _response = self._raw_client.kv_store_keys(bucket, filter=filter, request_options=request_options)
        return _response.data

    def kv_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[KvStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[KvStoreWatchResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[KvStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[KvStoreWatchResponse]
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        response = client.kv_management_api.kv_store_watch(
            bucket="bucket",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.kv_store_watch(
            bucket,
            filter=filter,
            include=include,
            ignore_deletes=ignore_deletes,
            resume_revision=resume_revision,
            authorization=authorization,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncKvManagementApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKvManagementApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKvManagementApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKvManagementApiClient
        """
        return self._raw_client

    async def list_kv_stores(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of entity names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.list_kv_stores()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_kv_stores(request_options=request_options)
        return _response.data

    async def kv_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KvStoreInfoResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvStoreInfoResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.kv_store_info(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kv_store_info(bucket, request_options=request_options)
        return _response.data

    async def add_kv_store(
        self,
        bucket: str,
        *,
        nats_kv_max_value_size: typing.Optional[float] = None,
        nats_kv_history: typing.Optional[float] = None,
        nats_kv_ttl: typing.Optional[float] = None,
        nats_kv_max_bytes: typing.Optional[float] = None,
        nats_kv_storage: typing.Optional[AddKvStoreRequestXNatsKvStorage] = None,
        nats_kv_replicas: typing.Optional[float] = None,
        nats_kv_compression: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[AddKvStoreRequestStorage] = OMIT,
        replicas: typing.Optional[float] = OMIT,
        compression: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        nats_kv_max_value_size : typing.Optional[float]
            the maximum size for an entry (only on application/text)

        nats_kv_history : typing.Optional[float]
            the number of possible history per key (only on application/text)

        nats_kv_ttl : typing.Optional[float]
            the amount of time entries live in the bucket in nanoseconds (only on application/text)

        nats_kv_max_bytes : typing.Optional[float]
            the maximum size of the KV in bytes (only on application/text)

        nats_kv_storage : typing.Optional[AddKvStoreRequestXNatsKvStorage]
            the underlying storage for the KV (only on application/text)

        nats_kv_replicas : typing.Optional[float]
            the underlying number of replicas (only on application/text)

        nats_kv_compression : typing.Optional[bool]
            compress the KV store (only on application/text)

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[AddKvStoreRequestStorage]

        replicas : typing.Optional[float]

        compression : typing.Optional[bool]

        metadata : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.add_kv_store(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_kv_store(
            bucket,
            nats_kv_max_value_size=nats_kv_max_value_size,
            nats_kv_history=nats_kv_history,
            nats_kv_ttl=nats_kv_ttl,
            nats_kv_max_bytes=nats_kv_max_bytes,
            nats_kv_storage=nats_kv_storage,
            nats_kv_replicas=nats_kv_replicas,
            nats_kv_compression=nats_kv_compression,
            description=description,
            max_value_size=max_value_size,
            history=history,
            ttl=ttl,
            max_bytes=max_bytes,
            storage=storage,
            replicas=replicas,
            compression=compression,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def kv_store_destroy(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.kv_store_destroy(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kv_store_destroy(bucket, request_options=request_options)
        return _response.data

    async def kv_store_purge(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.kv_store_purge(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kv_store_purge(bucket, request_options=request_options)
        return _response.data

    async def kv_store_keys(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of entity names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_management_api.kv_store_keys(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kv_store_keys(bucket, filter=filter, request_options=request_options)
        return _response.data

    async def kv_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[KvStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[KvStoreWatchResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[KvStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[KvStoreWatchResponse]
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = client.kv_management_api.kv_store_watch(
                bucket="bucket",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.kv_store_watch(
            bucket,
            filter=filter,
            include=include,
            ignore_deletes=ignore_deletes,
            resume_revision=resume_revision,
            authorization=authorization,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
