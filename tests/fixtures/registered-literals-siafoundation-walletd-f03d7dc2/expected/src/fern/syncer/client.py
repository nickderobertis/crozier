

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block_id import BlockId
from ..types.consensus_transaction import ConsensusTransaction
from ..types.consensus_v2block_data import ConsensusV2BlockData
from ..types.gateway_peer import GatewayPeer
from ..types.siacoin_output import SiacoinOutput
from .raw_client import AsyncRawSyncerClient, RawSyncerClient


OMIT = typing.cast(typing.Any, ...)


class SyncerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSyncerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSyncerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSyncerClient
        """
        return self._raw_client

    def post_syncer_connect(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Attempts to connect to the supplied peer address.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.syncer.post_syncer_connect(
            request="string",
        )
        """
        _response = self._raw_client.post_syncer_connect(request=request, request_options=request_options)
        return _response.data

    def get_syncer_peers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[GatewayPeer]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GatewayPeer]
            Connected peers and their metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.syncer.get_syncer_peers()
        """
        _response = self._raw_client.get_syncer_peers(request_options=request_options)
        return _response.data

    def post_syncer_broadcast_block(
        self,
        *,
        id: BlockId,
        parent_id: BlockId,
        nonce: int,
        timestamp: dt.datetime,
        miner_payouts: typing.Sequence[SiacoinOutput],
        transactions: typing.Sequence[ConsensusTransaction],
        v2: typing.Optional[ConsensusV2BlockData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds the supplied block to the local chain (if valid) and broadcasts it to peers. When broadcasting a v2 block, walletd sends the block outline.

        Parameters
        ----------
        id : BlockId

        parent_id : BlockId

        nonce : int

        timestamp : dt.datetime

        miner_payouts : typing.Sequence[SiacoinOutput]

        transactions : typing.Sequence[ConsensusTransaction]

        v2 : typing.Optional[ConsensusV2BlockData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import ConsensusTransaction, FernApi, SiacoinOutput

        client = FernApi()
        client.syncer.post_syncer_broadcast_block(
            id="id",
            parent_id="parentID",
            nonce=1000000,
            timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            miner_payouts=[
                SiacoinOutput(
                    value="value",
                    address="address",
                )
            ],
            transactions=[
                ConsensusTransaction(
                    id="id",
                )
            ],
        )
        """
        _response = self._raw_client.post_syncer_broadcast_block(
            id=id,
            parent_id=parent_id,
            nonce=nonce,
            timestamp=timestamp,
            miner_payouts=miner_payouts,
            transactions=transactions,
            v2=v2,
            request_options=request_options,
        )
        return _response.data


class AsyncSyncerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSyncerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSyncerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSyncerClient
        """
        return self._raw_client

    async def post_syncer_connect(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Attempts to connect to the supplied peer address.

        Parameters
        ----------
        request : str

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
            await client.syncer.post_syncer_connect(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_syncer_connect(request=request, request_options=request_options)
        return _response.data

    async def get_syncer_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GatewayPeer]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GatewayPeer]
            Connected peers and their metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.syncer.get_syncer_peers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_syncer_peers(request_options=request_options)
        return _response.data

    async def post_syncer_broadcast_block(
        self,
        *,
        id: BlockId,
        parent_id: BlockId,
        nonce: int,
        timestamp: dt.datetime,
        miner_payouts: typing.Sequence[SiacoinOutput],
        transactions: typing.Sequence[ConsensusTransaction],
        v2: typing.Optional[ConsensusV2BlockData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds the supplied block to the local chain (if valid) and broadcasts it to peers. When broadcasting a v2 block, walletd sends the block outline.

        Parameters
        ----------
        id : BlockId

        parent_id : BlockId

        nonce : int

        timestamp : dt.datetime

        miner_payouts : typing.Sequence[SiacoinOutput]

        transactions : typing.Sequence[ConsensusTransaction]

        v2 : typing.Optional[ConsensusV2BlockData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, ConsensusTransaction, SiacoinOutput

        client = AsyncFernApi()


        async def main() -> None:
            await client.syncer.post_syncer_broadcast_block(
                id="id",
                parent_id="parentID",
                nonce=1000000,
                timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                miner_payouts=[
                    SiacoinOutput(
                        value="value",
                        address="address",
                    )
                ],
                transactions=[
                    ConsensusTransaction(
                        id="id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_syncer_broadcast_block(
            id=id,
            parent_id=parent_id,
            nonce=nonce,
            timestamp=timestamp,
            miner_payouts=miner_payouts,
            transactions=transactions,
            v2=v2,
            request_options=request_options,
        )
        return _response.data
