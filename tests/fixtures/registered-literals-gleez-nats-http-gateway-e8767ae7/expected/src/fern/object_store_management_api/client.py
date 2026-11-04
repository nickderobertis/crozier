

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawObjectStoreManagementApiClient, RawObjectStoreManagementApiClient
from .types.obj_store_watch_request_include import ObjStoreWatchRequestInclude
from .types.obj_store_watch_response import ObjStoreWatchResponse
from .types.objm_store_add_request_storage import ObjmStoreAddRequestStorage
from .types.objm_store_info_response import ObjmStoreInfoResponse


OMIT = typing.cast(typing.Any, ...)


class ObjectStoreManagementApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObjectStoreManagementApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObjectStoreManagementApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObjectStoreManagementApiClient
        """
        return self._raw_client

    def objm_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
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
        client.object_store_management_api.objm_list()
        """
        _response = self._raw_client.objm_list(request_options=request_options)
        return _response.data

    def objm_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObjmStoreInfoResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjmStoreInfoResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.object_store_management_api.objm_store_info(
            bucket="bucket",
        )
        """
        _response = self._raw_client.objm_store_info(bucket, request_options=request_options)
        return _response.data

    def objm_store_add(
        self,
        bucket: str,
        *,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[ObjmStoreAddRequestStorage] = OMIT,
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

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[ObjmStoreAddRequestStorage]

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
        client.object_store_management_api.objm_store_add(
            bucket="bucket",
        )
        """
        _response = self._raw_client.objm_store_add(
            bucket,
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

    def objm_store_destroy(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.object_store_management_api.objm_store_destroy(
            bucket="bucket",
        )
        """
        _response = self._raw_client.objm_store_destroy(bucket, request_options=request_options)
        return _response.data

    def obj_store_keys(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

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
        client.object_store_management_api.obj_store_keys(
            bucket="bucket",
        )
        """
        _response = self._raw_client.obj_store_keys(bucket, request_options=request_options)
        return _response.data

    def obj_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[ObjStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[ObjStoreWatchResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[ObjStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[ObjStoreWatchResponse]
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        response = client.object_store_management_api.obj_store_watch(
            bucket="bucket",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.obj_store_watch(
            bucket,
            filter=filter,
            include=include,
            ignore_deletes=ignore_deletes,
            resume_revision=resume_revision,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncObjectStoreManagementApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObjectStoreManagementApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObjectStoreManagementApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObjectStoreManagementApiClient
        """
        return self._raw_client

    async def objm_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
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
            await client.object_store_management_api.objm_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.objm_list(request_options=request_options)
        return _response.data

    async def objm_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObjmStoreInfoResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjmStoreInfoResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.object_store_management_api.objm_store_info(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.objm_store_info(bucket, request_options=request_options)
        return _response.data

    async def objm_store_add(
        self,
        bucket: str,
        *,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[ObjmStoreAddRequestStorage] = OMIT,
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

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[ObjmStoreAddRequestStorage]

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
            await client.object_store_management_api.objm_store_add(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.objm_store_add(
            bucket,
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

    async def objm_store_destroy(self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.object_store_management_api.objm_store_destroy(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.objm_store_destroy(bucket, request_options=request_options)
        return _response.data

    async def obj_store_keys(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

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
            await client.object_store_management_api.obj_store_keys(
                bucket="bucket",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obj_store_keys(bucket, request_options=request_options)
        return _response.data

    async def obj_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[ObjStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[ObjStoreWatchResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[ObjStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[ObjStoreWatchResponse]
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = client.object_store_management_api.obj_store_watch(
                bucket="bucket",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.obj_store_watch(
            bucket,
            filter=filter,
            include=include,
            ignore_deletes=ignore_deletes,
            resume_revision=resume_revision,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
