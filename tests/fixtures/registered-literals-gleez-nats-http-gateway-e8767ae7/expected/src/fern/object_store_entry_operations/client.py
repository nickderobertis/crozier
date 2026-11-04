

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawObjectStoreEntryOperationsClient, RawObjectStoreEntryOperationsClient
from .types.obj_create_entry_response import ObjCreateEntryResponse


OMIT = typing.cast(typing.Any, ...)


class ObjectStoreEntryOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObjectStoreEntryOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObjectStoreEntryOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObjectStoreEntryOperationsClient
        """
        return self._raw_client

    def obj_get_entry(
        self, bucket: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

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
        client.object_store_entry_operations.obj_get_entry(
            bucket="bucket",
            key="key",
        )
        """
        with self._raw_client.obj_get_entry(bucket, key, request_options=request_options) as r:
            yield from r.data

    def obj_create_entry(
        self,
        bucket: str,
        key: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjCreateEntryResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjCreateEntryResponse
            ObjectInfo Response
        """
        _response = self._raw_client.obj_create_entry(bucket, key, request=request, request_options=request_options)
        return _response.data

    def obj_delete_entry(
        self,
        bucket: str,
        key: str,
        *,
        purge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        purge : typing.Optional[bool]
            Purges the deleted entry

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
        client.object_store_entry_operations.obj_delete_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.obj_delete_entry(bucket, key, purge=purge, request_options=request_options)
        return _response.data


class AsyncObjectStoreEntryOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObjectStoreEntryOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObjectStoreEntryOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObjectStoreEntryOperationsClient
        """
        return self._raw_client

    async def obj_get_entry(
        self, bucket: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

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
            await client.object_store_entry_operations.obj_get_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        async with self._raw_client.obj_get_entry(bucket, key, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def obj_create_entry(
        self,
        bucket: str,
        key: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObjCreateEntryResponse:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjCreateEntryResponse
            ObjectInfo Response
        """
        _response = await self._raw_client.obj_create_entry(
            bucket, key, request=request, request_options=request_options
        )
        return _response.data

    async def obj_delete_entry(
        self,
        bucket: str,
        key: str,
        *,
        purge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        purge : typing.Optional[bool]
            Purges the deleted entry

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
            await client.object_store_entry_operations.obj_delete_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obj_delete_entry(bucket, key, purge=purge, request_options=request_options)
        return _response.data
