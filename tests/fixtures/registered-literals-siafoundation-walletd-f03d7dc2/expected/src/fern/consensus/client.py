

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block import Block
from ..types.chain_index import ChainIndex
from ..types.consensus_checkpoint_response import ConsensusCheckpointResponse
from ..types.consensus_network import ConsensusNetwork
from ..types.consensus_state import ConsensusState
from ..types.consensus_updates_response import ConsensusUpdatesResponse
from .raw_client import AsyncRawConsensusClient, RawConsensusClient
from .types.get_consensus_block_request_id import GetConsensusBlockRequestId
from .types.get_consensus_checkpoint_request_id import GetConsensusCheckpointRequestId


class ConsensusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsensusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsensusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsensusClient
        """
        return self._raw_client

    def get_consensus_network(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConsensusNetwork:
        """
        Returns consensus parameters for the active network.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusNetwork
            Consensus network parameters.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_network()
        """
        _response = self._raw_client.get_consensus_network(request_options=request_options)
        return _response.data

    def get_consensus_tip(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChainIndex:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIndex
            Current best chain index.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_tip()
        """
        _response = self._raw_client.get_consensus_tip(request_options=request_options)
        return _response.data

    def get_consensus_tip_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConsensusState:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusState
            Consensus state at the current tip.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_tip_state()
        """
        _response = self._raw_client.get_consensus_tip_state(request_options=request_options)
        return _response.data

    def get_consensus_checkpoint(
        self, id: GetConsensusCheckpointRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsensusCheckpointResponse:
        """
        Returns the consensus state and block associated with the supplied block ID or height.

        Parameters
        ----------
        id : GetConsensusCheckpointRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusCheckpointResponse
            Consensus checkpoint for the supplied block.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_checkpoint(
            id="id",
        )
        """
        _response = self._raw_client.get_consensus_checkpoint(id, request_options=request_options)
        return _response.data

    def get_consensus_block(
        self, id: GetConsensusBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Block:
        """
        Parameters
        ----------
        id : GetConsensusBlockRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Block data.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_block(
            id="id",
        )
        """
        _response = self._raw_client.get_consensus_block(id, request_options=request_options)
        return _response.data

    def get_consensus_updates(
        self,
        index: ChainIndex,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsensusUpdatesResponse:
        """
        Returns the set of reverted and applied updates needed to move from the supplied chain index to the current tip.

        Parameters
        ----------
        index : ChainIndex
            Starting chain index.

        limit : typing.Optional[int]
            Maximum number of updates to return (default 10, max 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusUpdatesResponse
            Consensus updates needed to synchronize the supplied index.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_updates(
            index="index",
        )
        """
        _response = self._raw_client.get_consensus_updates(index, limit=limit, request_options=request_options)
        return _response.data

    def get_consensus_index_by_height(
        self, height: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChainIndex:
        """
        Parameters
        ----------
        height : int
            Block height to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIndex
            Chain index at the requested height.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.consensus.get_consensus_index_by_height(
            height=1000000,
        )
        """
        _response = self._raw_client.get_consensus_index_by_height(height, request_options=request_options)
        return _response.data


class AsyncConsensusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsensusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsensusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsensusClient
        """
        return self._raw_client

    async def get_consensus_network(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsensusNetwork:
        """
        Returns consensus parameters for the active network.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusNetwork
            Consensus network parameters.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_network()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_network(request_options=request_options)
        return _response.data

    async def get_consensus_tip(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChainIndex:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIndex
            Current best chain index.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_tip()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_tip(request_options=request_options)
        return _response.data

    async def get_consensus_tip_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsensusState:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusState
            Consensus state at the current tip.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_tip_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_tip_state(request_options=request_options)
        return _response.data

    async def get_consensus_checkpoint(
        self, id: GetConsensusCheckpointRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsensusCheckpointResponse:
        """
        Returns the consensus state and block associated with the supplied block ID or height.

        Parameters
        ----------
        id : GetConsensusCheckpointRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusCheckpointResponse
            Consensus checkpoint for the supplied block.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_checkpoint(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_checkpoint(id, request_options=request_options)
        return _response.data

    async def get_consensus_block(
        self, id: GetConsensusBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Block:
        """
        Parameters
        ----------
        id : GetConsensusBlockRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Block data.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_block(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_block(id, request_options=request_options)
        return _response.data

    async def get_consensus_updates(
        self,
        index: ChainIndex,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsensusUpdatesResponse:
        """
        Returns the set of reverted and applied updates needed to move from the supplied chain index to the current tip.

        Parameters
        ----------
        index : ChainIndex
            Starting chain index.

        limit : typing.Optional[int]
            Maximum number of updates to return (default 10, max 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsensusUpdatesResponse
            Consensus updates needed to synchronize the supplied index.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_updates(
                index="index",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_updates(index, limit=limit, request_options=request_options)
        return _response.data

    async def get_consensus_index_by_height(
        self, height: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChainIndex:
        """
        Parameters
        ----------
        height : int
            Block height to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChainIndex
            Chain index at the requested height.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.consensus.get_consensus_index_by_height(
                height=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consensus_index_by_height(height, request_options=request_options)
        return _response.data
