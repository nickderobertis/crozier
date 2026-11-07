

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCoreReferenceClient, RawCoreReferenceClient


class CoreReferenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreReferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreReferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreReferenceClient
        """
        return self._raw_client

    def preview(
        self, reference_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        reference_id : str
            the reference cache key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Preview returned
        """
        with self._raw_client.preview(reference_id, request_options=request_options) as r:
            yield from r.data


class AsyncCoreReferenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreReferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreReferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreReferenceClient
        """
        return self._raw_client

    async def preview(
        self, reference_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        reference_id : str
            the reference cache key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Preview returned
        """
        async with self._raw_client.preview(reference_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
