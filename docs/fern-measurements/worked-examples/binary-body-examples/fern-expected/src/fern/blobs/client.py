

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.blob import Blob
from .raw_client import AsyncRawBlobsClient, RawBlobsClient


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

    def put_blob(
        self,
        blob_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok
        """
        _response = self._raw_client.put_blob(blob_id, request=request, request_options=request_options)
        return _response.data

    def upload_blob(self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None) -> Blob:
        """
        Parameters
        ----------
        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.blobs.upload_blob(
            request="string",
        )
        """
        _response = self._raw_client.upload_blob(request=request, request_options=request_options)
        return _response.data

    def attach_note(
        self, blob_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.blobs.attach_note(
            blob_id="blob_id",
            request='note "quoted" body',
        )
        """
        _response = self._raw_client.attach_note(blob_id, request=request, request_options=request_options)
        return _response.data

    def attach_receipt(
        self, blob_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.blobs.attach_receipt(
            blob_id="blob_id",
            request="café receipt",
        )
        """
        _response = self._raw_client.attach_receipt(blob_id, request=request, request_options=request_options)
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

    async def put_blob(
        self,
        blob_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok
        """
        _response = await self._raw_client.put_blob(blob_id, request=request, request_options=request_options)
        return _response.data

    async def upload_blob(self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None) -> Blob:
        """
        Parameters
        ----------
        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.blobs.upload_blob(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_blob(request=request, request_options=request_options)
        return _response.data

    async def attach_note(
        self, blob_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.blobs.attach_note(
                blob_id="blob_id",
                request='note "quoted" body',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach_note(blob_id, request=request, request_options=request_options)
        return _response.data

    async def attach_receipt(
        self, blob_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> Blob:
        """
        Parameters
        ----------
        blob_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Blob
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.blobs.attach_receipt(
                blob_id="blob_id",
                request="café receipt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach_receipt(blob_id, request=request, request_options=request_options)
        return _response.data
