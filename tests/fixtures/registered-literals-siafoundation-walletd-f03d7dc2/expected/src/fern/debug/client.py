

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from .raw_client import AsyncRawDebugClient, RawDebugClient
from .types.get_pprof_data_request_handler import GetPprofDataRequestHandler


OMIT = typing.cast(typing.Any, ...)


class DebugClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDebugClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDebugClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDebugClient
        """
        return self._raw_client

    def post_debug_mine(
        self, *, blocks: int, address: Address, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mines the requested number of blocks to the supplied address using the integrated CPU miner. Only available when debug endpoints are enabled.

        Parameters
        ----------
        blocks : int
            Number of blocks to mine.

        address : Address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.debug.post_debug_mine(
            blocks=1,
            address="address",
        )
        """
        _response = self._raw_client.post_debug_mine(blocks=blocks, address=address, request_options=request_options)
        return _response.data

    def get_pprof_data(
        self, handler: GetPprofDataRequestHandler, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns profiling data for the specified handler. This is useful for debugging and performance analysis.

        Parameters
        ----------
        handler : GetPprofDataRequestHandler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Profiling data in binary format
        """
        with self._raw_client.get_pprof_data(handler, request_options=request_options) as r:
            yield from r.data


class AsyncDebugClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDebugClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDebugClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDebugClient
        """
        return self._raw_client

    async def post_debug_mine(
        self, *, blocks: int, address: Address, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mines the requested number of blocks to the supplied address using the integrated CPU miner. Only available when debug endpoints are enabled.

        Parameters
        ----------
        blocks : int
            Number of blocks to mine.

        address : Address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.debug.post_debug_mine(
                blocks=1,
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_debug_mine(
            blocks=blocks, address=address, request_options=request_options
        )
        return _response.data

    async def get_pprof_data(
        self, handler: GetPprofDataRequestHandler, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns profiling data for the specified handler. This is useful for debugging and performance analysis.

        Parameters
        ----------
        handler : GetPprofDataRequestHandler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Profiling data in binary format
        """
        async with self._raw_client.get_pprof_data(handler, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
