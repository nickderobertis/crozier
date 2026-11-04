

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawObjectStoreApiClient, RawObjectStoreApiClient


class ObjectStoreApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObjectStoreApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObjectStoreApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObjectStoreApiClient
        """
        return self._raw_client

    def simple_obj_get(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            success response body is payload, and metadata is HTTP headers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.object_store_api.simple_obj_get(
            bucket="bucket",
            key="key",
        )
        """
        with self._raw_client.simple_obj_get(bucket, key, meta_only=meta_only, request_options=request_options) as r:
            yield from r.data

    def simple_obj_put_entry(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        previous_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

        previous_revision : typing.Optional[int]
            the expected previous revision. If specified and the key is not at the specified revision the operation fails.

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
        client.object_store_api.simple_obj_put_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.simple_obj_put_entry(
            bucket, key, meta_only=meta_only, previous_revision=previous_revision, request_options=request_options
        )
        return _response.data

    def simple_obj_delete_entry(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

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
        client.object_store_api.simple_obj_delete_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.simple_obj_delete_entry(
            bucket, key, meta_only=meta_only, request_options=request_options
        )
        return _response.data


class AsyncObjectStoreApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObjectStoreApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObjectStoreApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObjectStoreApiClient
        """
        return self._raw_client

    async def simple_obj_get(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            success response body is payload, and metadata is HTTP headers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.object_store_api.simple_obj_get(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        async with self._raw_client.simple_obj_get(
            bucket, key, meta_only=meta_only, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def simple_obj_put_entry(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        previous_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

        previous_revision : typing.Optional[int]
            the expected previous revision. If specified and the key is not at the specified revision the operation fails.

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
            await client.object_store_api.simple_obj_put_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_obj_put_entry(
            bucket, key, meta_only=meta_only, previous_revision=previous_revision, request_options=request_options
        )
        return _response.data

    async def simple_obj_delete_entry(
        self,
        bucket: str,
        key: str,
        *,
        meta_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        meta_only : typing.Optional[bool]
            if true, only the metadata of the object is returned, the body will not contain any data

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
            await client.object_store_api.simple_obj_delete_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_obj_delete_entry(
            bucket, key, meta_only=meta_only, request_options=request_options
        )
        return _response.data
