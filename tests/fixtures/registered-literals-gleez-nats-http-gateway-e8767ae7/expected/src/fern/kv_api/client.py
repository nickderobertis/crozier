

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKvApiClient, RawKvApiClient


class KvApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKvApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKvApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKvApiClient
        """
        return self._raw_client

    def simple_kv_get(
        self,
        bucket: str,
        key: str,
        *,
        revision: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        revision : typing.Optional[float]
            the value of the key at the specified revision. Note the revision may not be available.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            success response body is payload, and metadata is HTTP headers. On JSON responses the value property is base64 encoded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_api.simple_kv_get(
            bucket="bucket",
            key="key",
        )
        """
        with self._raw_client.simple_kv_get(bucket, key, revision=revision, request_options=request_options) as r:
            yield from r.data

    def simple_kv_create_entry(
        self, bucket: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_api.simple_kv_create_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.simple_kv_create_entry(bucket, key, request_options=request_options)
        return _response.data

    def simple_kv_put_entry(
        self,
        bucket: str,
        key: str,
        *,
        previous_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        previous_revision : typing.Optional[int]
            the expected previous revision. If specified and the key is not at the specified revision the operation fails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.kv_api.simple_kv_put_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.simple_kv_put_entry(
            bucket, key, previous_revision=previous_revision, request_options=request_options
        )
        return _response.data

    def simple_kv_delete_entry(
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
        client.kv_api.simple_kv_delete_entry(
            bucket="bucket",
            key="key",
        )
        """
        _response = self._raw_client.simple_kv_delete_entry(bucket, key, purge=purge, request_options=request_options)
        return _response.data


class AsyncKvApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKvApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKvApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKvApiClient
        """
        return self._raw_client

    async def simple_kv_get(
        self,
        bucket: str,
        key: str,
        *,
        revision: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        revision : typing.Optional[float]
            the value of the key at the specified revision. Note the revision may not be available.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            success response body is payload, and metadata is HTTP headers. On JSON responses the value property is base64 encoded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_api.simple_kv_get(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        async with self._raw_client.simple_kv_get(bucket, key, revision=revision, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def simple_kv_create_entry(
        self, bucket: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_api.simple_kv_create_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_kv_create_entry(bucket, key, request_options=request_options)
        return _response.data

    async def simple_kv_put_entry(
        self,
        bucket: str,
        key: str,
        *,
        previous_revision: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        key : str
            Key name

        previous_revision : typing.Optional[int]
            the expected previous revision. If specified and the key is not at the specified revision the operation fails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.kv_api.simple_kv_put_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_kv_put_entry(
            bucket, key, previous_revision=previous_revision, request_options=request_options
        )
        return _response.data

    async def simple_kv_delete_entry(
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
            await client.kv_api.simple_kv_delete_entry(
                bucket="bucket",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_kv_delete_entry(
            bucket, key, purge=purge, request_options=request_options
        )
        return _response.data
