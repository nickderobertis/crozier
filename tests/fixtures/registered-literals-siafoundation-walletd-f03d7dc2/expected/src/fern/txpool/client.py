

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chain_index import ChainIndex
from ..types.currency import Currency
from ..types.event import Event
from ..types.file_contract import FileContract
from ..types.file_contract_revision import FileContractRevision
from ..types.siacoin_input import SiacoinInput
from ..types.siacoin_output_with_id import SiacoinOutputWithId
from ..types.siafund_input import SiafundInput
from ..types.siafund_output_with_id import SiafundOutputWithId
from ..types.storage_proof import StorageProof
from ..types.transaction import Transaction
from ..types.transaction_id import TransactionId
from ..types.transaction_signature import TransactionSignature
from ..types.txpool_broadcast_response import TxpoolBroadcastResponse
from ..types.txpool_transactions_response import TxpoolTransactionsResponse
from ..types.txpool_update_v2transactions_response import TxpoolUpdateV2TransactionsResponse
from ..types.v2transaction import V2Transaction
from .raw_client import AsyncRawTxpoolClient, RawTxpoolClient


OMIT = typing.cast(typing.Any, ...)


class TxpoolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTxpoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTxpoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTxpoolClient
        """
        return self._raw_client

    def get_txpool_transactions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TxpoolTransactionsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolTransactionsResponse
            Current contents of the transaction pools.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.txpool.get_txpool_transactions()
        """
        _response = self._raw_client.get_txpool_transactions(request_options=request_options)
        return _response.data

    def post_txpool_v2transactions_basis(
        self,
        *,
        basis: ChainIndex,
        target: ChainIndex,
        transactions: typing.Sequence[V2Transaction],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxpoolUpdateV2TransactionsResponse:
        """
        Adjusts a v2 transaction set from one basis chain index to another. Use this to keep proofs and references valid when the chain advances.

        Parameters
        ----------
        basis : ChainIndex

        target : ChainIndex

        transactions : typing.Sequence[V2Transaction]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolUpdateV2TransactionsResponse
            Updated transaction set anchored at the target basis.

        Examples
        --------
        from fern import ChainIndex, FernApi, V2Transaction

        client = FernApi()
        client.txpool.post_txpool_v2transactions_basis(
            basis=ChainIndex(),
            target=ChainIndex(),
            transactions=[
                V2Transaction(
                    id="id",
                    miner_fee="minerFee",
                )
            ],
        )
        """
        _response = self._raw_client.post_txpool_v2transactions_basis(
            basis=basis, target=target, transactions=transactions, request_options=request_options
        )
        return _response.data

    def get_txpool_fee(self, *, request_options: typing.Optional[RequestOptions] = None) -> Currency:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Currency
            Fee rate recommended for prompt confirmation.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.txpool.get_txpool_fee()
        """
        _response = self._raw_client.get_txpool_fee(request_options=request_options)
        return _response.data

    def post_txpool_parents(
        self,
        *,
        id: TransactionId,
        siacoin_inputs: typing.Optional[typing.Sequence[SiacoinInput]] = OMIT,
        siacoin_outputs: typing.Optional[typing.Sequence[SiacoinOutputWithId]] = OMIT,
        file_contracts: typing.Optional[typing.Sequence[FileContract]] = OMIT,
        file_contract_revisions: typing.Optional[typing.Sequence[FileContractRevision]] = OMIT,
        storage_proofs: typing.Optional[typing.Sequence[StorageProof]] = OMIT,
        siafund_inputs: typing.Optional[typing.Sequence[SiafundInput]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[SiafundOutputWithId]] = OMIT,
        miner_fees: typing.Optional[typing.Sequence[Currency]] = OMIT,
        arbitrary_data: typing.Optional[typing.Sequence[str]] = OMIT,
        signatures: typing.Optional[typing.Sequence[TransactionSignature]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Transaction]:
        """
        Returns unconfirmed parent transactions required to validate the supplied transaction.

        Parameters
        ----------
        id : TransactionId

        siacoin_inputs : typing.Optional[typing.Sequence[SiacoinInput]]

        siacoin_outputs : typing.Optional[typing.Sequence[SiacoinOutputWithId]]

        file_contracts : typing.Optional[typing.Sequence[FileContract]]

        file_contract_revisions : typing.Optional[typing.Sequence[FileContractRevision]]

        storage_proofs : typing.Optional[typing.Sequence[StorageProof]]

        siafund_inputs : typing.Optional[typing.Sequence[SiafundInput]]

        siafund_outputs : typing.Optional[typing.Sequence[SiafundOutputWithId]]

        miner_fees : typing.Optional[typing.Sequence[Currency]]

        arbitrary_data : typing.Optional[typing.Sequence[str]]
            Arbitrary data entries encoded as base64 strings.

        signatures : typing.Optional[typing.Sequence[TransactionSignature]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Transaction]
            Parent transactions that must be included ahead of the supplied transaction.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.txpool.post_txpool_parents(
            id="id",
        )
        """
        _response = self._raw_client.post_txpool_parents(
            id=id,
            siacoin_inputs=siacoin_inputs,
            siacoin_outputs=siacoin_outputs,
            file_contracts=file_contracts,
            file_contract_revisions=file_contract_revisions,
            storage_proofs=storage_proofs,
            siafund_inputs=siafund_inputs,
            siafund_outputs=siafund_outputs,
            miner_fees=miner_fees,
            arbitrary_data=arbitrary_data,
            signatures=signatures,
            request_options=request_options,
        )
        return _response.data

    def post_txpool_broadcast(
        self,
        *,
        basis: typing.Optional[ChainIndex] = OMIT,
        transactions: typing.Optional[typing.Sequence[Transaction]] = OMIT,
        v2transactions: typing.Optional[typing.Sequence[V2Transaction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxpoolBroadcastResponse:
        """
        Broadcasts v1 or v2 transaction sets. Walletd may augment the submitted transactions with missing parents or overwritten proofs before sending them to peers.

        Parameters
        ----------
        basis : typing.Optional[ChainIndex]

        transactions : typing.Optional[typing.Sequence[Transaction]]
            v1 transactions to broadcast.

        v2transactions : typing.Optional[typing.Sequence[V2Transaction]]
            v2 transactions to broadcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolBroadcastResponse
            Transactions accepted by the pool and broadcast to peers.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.txpool.post_txpool_broadcast()
        """
        _response = self._raw_client.post_txpool_broadcast(
            basis=basis, transactions=transactions, v2transactions=v2transactions, request_options=request_options
        )
        return _response.data

    def get_txpool_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Event]:
        """
        Returns unconfirmed wallet events backed by transactions in the pool.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Pending wallet events derived from the transaction pool.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.txpool.get_txpool_events()
        """
        _response = self._raw_client.get_txpool_events(request_options=request_options)
        return _response.data


class AsyncTxpoolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTxpoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTxpoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTxpoolClient
        """
        return self._raw_client

    async def get_txpool_transactions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TxpoolTransactionsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolTransactionsResponse
            Current contents of the transaction pools.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.get_txpool_transactions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_txpool_transactions(request_options=request_options)
        return _response.data

    async def post_txpool_v2transactions_basis(
        self,
        *,
        basis: ChainIndex,
        target: ChainIndex,
        transactions: typing.Sequence[V2Transaction],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxpoolUpdateV2TransactionsResponse:
        """
        Adjusts a v2 transaction set from one basis chain index to another. Use this to keep proofs and references valid when the chain advances.

        Parameters
        ----------
        basis : ChainIndex

        target : ChainIndex

        transactions : typing.Sequence[V2Transaction]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolUpdateV2TransactionsResponse
            Updated transaction set anchored at the target basis.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChainIndex, V2Transaction

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.post_txpool_v2transactions_basis(
                basis=ChainIndex(),
                target=ChainIndex(),
                transactions=[
                    V2Transaction(
                        id="id",
                        miner_fee="minerFee",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_txpool_v2transactions_basis(
            basis=basis, target=target, transactions=transactions, request_options=request_options
        )
        return _response.data

    async def get_txpool_fee(self, *, request_options: typing.Optional[RequestOptions] = None) -> Currency:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Currency
            Fee rate recommended for prompt confirmation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.get_txpool_fee()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_txpool_fee(request_options=request_options)
        return _response.data

    async def post_txpool_parents(
        self,
        *,
        id: TransactionId,
        siacoin_inputs: typing.Optional[typing.Sequence[SiacoinInput]] = OMIT,
        siacoin_outputs: typing.Optional[typing.Sequence[SiacoinOutputWithId]] = OMIT,
        file_contracts: typing.Optional[typing.Sequence[FileContract]] = OMIT,
        file_contract_revisions: typing.Optional[typing.Sequence[FileContractRevision]] = OMIT,
        storage_proofs: typing.Optional[typing.Sequence[StorageProof]] = OMIT,
        siafund_inputs: typing.Optional[typing.Sequence[SiafundInput]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[SiafundOutputWithId]] = OMIT,
        miner_fees: typing.Optional[typing.Sequence[Currency]] = OMIT,
        arbitrary_data: typing.Optional[typing.Sequence[str]] = OMIT,
        signatures: typing.Optional[typing.Sequence[TransactionSignature]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Transaction]:
        """
        Returns unconfirmed parent transactions required to validate the supplied transaction.

        Parameters
        ----------
        id : TransactionId

        siacoin_inputs : typing.Optional[typing.Sequence[SiacoinInput]]

        siacoin_outputs : typing.Optional[typing.Sequence[SiacoinOutputWithId]]

        file_contracts : typing.Optional[typing.Sequence[FileContract]]

        file_contract_revisions : typing.Optional[typing.Sequence[FileContractRevision]]

        storage_proofs : typing.Optional[typing.Sequence[StorageProof]]

        siafund_inputs : typing.Optional[typing.Sequence[SiafundInput]]

        siafund_outputs : typing.Optional[typing.Sequence[SiafundOutputWithId]]

        miner_fees : typing.Optional[typing.Sequence[Currency]]

        arbitrary_data : typing.Optional[typing.Sequence[str]]
            Arbitrary data entries encoded as base64 strings.

        signatures : typing.Optional[typing.Sequence[TransactionSignature]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Transaction]
            Parent transactions that must be included ahead of the supplied transaction.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.post_txpool_parents(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_txpool_parents(
            id=id,
            siacoin_inputs=siacoin_inputs,
            siacoin_outputs=siacoin_outputs,
            file_contracts=file_contracts,
            file_contract_revisions=file_contract_revisions,
            storage_proofs=storage_proofs,
            siafund_inputs=siafund_inputs,
            siafund_outputs=siafund_outputs,
            miner_fees=miner_fees,
            arbitrary_data=arbitrary_data,
            signatures=signatures,
            request_options=request_options,
        )
        return _response.data

    async def post_txpool_broadcast(
        self,
        *,
        basis: typing.Optional[ChainIndex] = OMIT,
        transactions: typing.Optional[typing.Sequence[Transaction]] = OMIT,
        v2transactions: typing.Optional[typing.Sequence[V2Transaction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxpoolBroadcastResponse:
        """
        Broadcasts v1 or v2 transaction sets. Walletd may augment the submitted transactions with missing parents or overwritten proofs before sending them to peers.

        Parameters
        ----------
        basis : typing.Optional[ChainIndex]

        transactions : typing.Optional[typing.Sequence[Transaction]]
            v1 transactions to broadcast.

        v2transactions : typing.Optional[typing.Sequence[V2Transaction]]
            v2 transactions to broadcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxpoolBroadcastResponse
            Transactions accepted by the pool and broadcast to peers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.post_txpool_broadcast()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_txpool_broadcast(
            basis=basis, transactions=transactions, v2transactions=v2transactions, request_options=request_options
        )
        return _response.data

    async def get_txpool_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Event]:
        """
        Returns unconfirmed wallet events backed by transactions in the pool.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Pending wallet events derived from the transaction pool.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.txpool.get_txpool_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_txpool_events(request_options=request_options)
        return _response.data
