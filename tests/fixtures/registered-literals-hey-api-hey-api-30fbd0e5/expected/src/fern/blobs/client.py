

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBlobsClient, RawBlobsClient
from .types.v1blobs_list_response_item import V1BlobsListResponseItem
from .types.v1blobs_store_response import V1BlobsStoreResponse
from .types.v2blobs_list_response_item import V2BlobsListResponseItem
from .types.v2blobs_store_response import V2BlobsStoreResponse


OMIT = typing.cast(typing.Any, ...)


class BlobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBlobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBlobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBlobsClient
        """
        return self._raw_client

    def v1blobs_list(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1BlobsListResponseItem]:
        """
        List blobs in your account

        Parameters
        ----------
        prefix : typing.Optional[str]
            If specified, only include blobs that start with this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1BlobsListResponseItem]
            List of blobs that you’ve stored

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v1blobs_list()
        """
        _response = self._raw_client.v1blobs_list(prefix=prefix, request_options=request_options)
        return _response.data

    def v1blobs_get(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get a blob’s contents.

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Binary contents of the returned file
        """
        with self._raw_client.v1blobs_get(key, request_options=request_options) as r:
            yield from r.data

    def v1blobs_store(
        self, key: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BlobsStoreResponse:
        """
        Store data in blob storage

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BlobsStoreResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v1blobs_store(
            key="key",
            request="string",
        )
        """
        _response = self._raw_client.v1blobs_store(key, request=request, request_options=request_options)
        return _response.data

    def v1blobs_delete(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a blob

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v1blobs_delete(
            key="key",
        )
        """
        _response = self._raw_client.v1blobs_delete(key, request_options=request_options)
        return _response.data

    def v2blobs_list(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V2BlobsListResponseItem]:
        """
        List blobs in your account

        Parameters
        ----------
        prefix : typing.Optional[str]
            If specified, only include blobs that start with this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V2BlobsListResponseItem]
            List of blobs that you’ve stored

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v2blobs_list()
        """
        _response = self._raw_client.v2blobs_list(prefix=prefix, request_options=request_options)
        return _response.data

    def v2blobs_get(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get a blob’s contents.

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Binary contents of the returned file
        """
        with self._raw_client.v2blobs_get(key, request_options=request_options) as r:
            yield from r.data

    def v2blobs_store(
        self, key: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> V2BlobsStoreResponse:
        """
        Store data in blob storage

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BlobsStoreResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v2blobs_store(
            key="key",
            request="string",
        )
        """
        _response = self._raw_client.v2blobs_store(key, request=request, request_options=request_options)
        return _response.data

    def v2blobs_delete(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a blob

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.blobs.v2blobs_delete(
            key="key",
        )
        """
        _response = self._raw_client.v2blobs_delete(key, request_options=request_options)
        return _response.data


class AsyncBlobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBlobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBlobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBlobsClient
        """
        return self._raw_client

    async def v1blobs_list(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1BlobsListResponseItem]:
        """
        List blobs in your account

        Parameters
        ----------
        prefix : typing.Optional[str]
            If specified, only include blobs that start with this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1BlobsListResponseItem]
            List of blobs that you’ve stored

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v1blobs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.v1blobs_list(prefix=prefix, request_options=request_options)
        return _response.data

    async def v1blobs_get(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a blob’s contents.

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Binary contents of the returned file
        """
        async with self._raw_client.v1blobs_get(key, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def v1blobs_store(
        self, key: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BlobsStoreResponse:
        """
        Store data in blob storage

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BlobsStoreResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v1blobs_store(
                key="key",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1blobs_store(key, request=request, request_options=request_options)
        return _response.data

    async def v1blobs_delete(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a blob

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v1blobs_delete(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1blobs_delete(key, request_options=request_options)
        return _response.data

    async def v2blobs_list(
        self, *, prefix: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V2BlobsListResponseItem]:
        """
        List blobs in your account

        Parameters
        ----------
        prefix : typing.Optional[str]
            If specified, only include blobs that start with this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V2BlobsListResponseItem]
            List of blobs that you’ve stored

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v2blobs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.v2blobs_list(prefix=prefix, request_options=request_options)
        return _response.data

    async def v2blobs_get(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a blob’s contents.

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Binary contents of the returned file
        """
        async with self._raw_client.v2blobs_get(key, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def v2blobs_store(
        self, key: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> V2BlobsStoreResponse:
        """
        Store data in blob storage

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BlobsStoreResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v2blobs_store(
                key="key",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2blobs_store(key, request=request, request_options=request_options)
        return _response.data

    async def v2blobs_delete(self, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a blob

        Parameters
        ----------
        key : str
            Key that uniquely identifies this blob

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blobs.v2blobs_delete(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2blobs_delete(key, request_options=request_options)
        return _response.data
