

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLedgerClient, RawLedgerClient
from .types.get_block_response import GetBlockResponse


class LedgerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLedgerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLedgerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLedgerClient
        """
        return self._raw_client

    def get_block(self, height: int, *, request_options: typing.Optional[RequestOptions] = None) -> GetBlockResponse:
        """
        An unsigned 64-bit integer's placeholder.

        Parameters
        ----------
        height : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlockResponse
            The block

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ledger.get_block(
            height=1000000,
        )
        """
        _response = self._raw_client.get_block(height, request_options=request_options)
        return _response.data


class AsyncLedgerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLedgerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLedgerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLedgerClient
        """
        return self._raw_client

    async def get_block(
        self, height: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBlockResponse:
        """
        An unsigned 64-bit integer's placeholder.

        Parameters
        ----------
        height : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlockResponse
            The block

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ledger.get_block(
                height=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block(height, request_options=request_options)
        return _response.data
