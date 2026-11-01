

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSpecimensClient, RawSpecimensClient


OMIT = typing.cast(typing.Any, ...)


class SpecimensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpecimensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpecimensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpecimensClient
        """
        return self._raw_client

    def render_scan(
        self, specimen_id: str, *, dpi: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        specimen_id : str

        dpi : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The scan bytes, or its metadata.
        """
        with self._raw_client.render_scan(specimen_id, dpi=dpi, request_options=request_options) as r:
            yield from r.data


class AsyncSpecimensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpecimensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpecimensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpecimensClient
        """
        return self._raw_client

    async def render_scan(
        self, specimen_id: str, *, dpi: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        specimen_id : str

        dpi : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The scan bytes, or its metadata.
        """
        async with self._raw_client.render_scan(specimen_id, dpi=dpi, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
