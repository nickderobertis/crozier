

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block import Block
from .raw_client import AsyncRawBlocksClient, RawBlocksClient
from .types.get_block_request_id import GetBlockRequestId


class BlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBlocksClient
        """
        return self._raw_client

    def get_block(self, id: GetBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None) -> Block:
        """
        Parameters
        ----------
        id : GetBlockRequestId
            Block hash (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            The block.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.blocks.get_block(
            id="id",
        )
        """
        _response = self._raw_client.get_block(id, request_options=request_options)
        return _response.data


class AsyncBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBlocksClient
        """
        return self._raw_client

    async def get_block(
        self, id: GetBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Block:
        """
        Parameters
        ----------
        id : GetBlockRequestId
            Block hash (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            The block.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.blocks.get_block(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block(id, request_options=request_options)
        return _response.data
