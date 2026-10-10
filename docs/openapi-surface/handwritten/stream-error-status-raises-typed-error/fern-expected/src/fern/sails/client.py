

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.rotation import Rotation
from .raw_client import AsyncRawSailsClient, RawSailsClient


class SailsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSailsClient
        """
        return self._raw_client

    def stream_rotations(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[Rotation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[Rotation]
            One event per rotation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.sails.stream_rotations()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_rotations(request_options=request_options) as r:
            yield from r.data


class AsyncSailsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSailsClient
        """
        return self._raw_client

    async def stream_rotations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[Rotation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[Rotation]
            One event per rotation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.sails.stream_rotations()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_rotations(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
