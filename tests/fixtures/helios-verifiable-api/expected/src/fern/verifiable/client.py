

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_response import AccountResponse
from ..types.address import Address
from ..types.block_number_or_tag_or_hash import BlockNumberOrTagOrHash
from ..types.bytes_max32 import BytesMax32
from ..types.extended_access_list_response import ExtendedAccessListResponse
from ..types.filter_changes_response import FilterChangesResponse
from ..types.filter_logs_response import FilterLogsResponse
from ..types.filter_topic import FilterTopic
from ..types.generic_transaction import GenericTransaction
from ..types.get_eth_v1proof_logs_request_address import GetEthV1ProofLogsRequestAddress
from ..types.hash32 import Hash32
from ..types.logs_response import LogsResponse
from ..types.transaction_receipt_response import TransactionReceiptResponse
from ..types.uint import Uint
from .raw_client import AsyncRawVerifiableClient, RawVerifiableClient


OMIT = typing.cast(typing.Any, ...)


class VerifiableClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVerifiableClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVerifiableClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVerifiableClient
        """
        return self._raw_client

    def get_account_information(
        self,
        address: Address,
        *,
        include_code: typing.Optional[bool] = None,
        storage_slots: typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]] = None,
        block: typing.Optional[BlockNumberOrTagOrHash] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Returns information about an address along with its EIP-1186 account proof.
        ### Why is this useful?
        Replaces the `eth_getProof`, `eth_getTransactionCount`, `eth_getBalance`, `eth_getCode`, and `eth_getStorageAt` RPC methods.
        ### How to verify response?
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`, verify the given leaf’s Merkle Proof against the `storageHash`

        Parameters
        ----------
        address : Address
            The address of the account.

        include_code : typing.Optional[bool]
            A flag indicating whether to include the account's code.

        storage_slots : typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]]
            A list of storage positions (in hex) to include in the proof.

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.get_account_information(
            address="address",
        )
        """
        _response = self._raw_client.get_account_information(
            address,
            include_code=include_code,
            storage_slots=storage_slots,
            block=block,
            request_options=request_options,
        )
        return _response.data

    def get_transaction_receipt(
        self, tx_hash: Hash32, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransactionReceiptResponse:
        """
        Returns the receipt of a transaction along with a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getTransactionReceipt` RPC method.
        ### How to verify response?
        - RLP encode the given receipt and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        tx_hash : Hash32
            The hash of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionReceiptResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.get_transaction_receipt(
            tx_hash="txHash",
        )
        """
        _response = self._raw_client.get_transaction_receipt(tx_hash, request_options=request_options)
        return _response.data

    def get_logs(
        self,
        *,
        from_block: typing.Optional[Uint] = None,
        to_block: typing.Optional[Uint] = None,
        block_hash: typing.Optional[Hash32] = None,
        address: typing.Optional[GetEthV1ProofLogsRequestAddress] = None,
        topic0: typing.Optional[FilterTopic] = None,
        topic1: typing.Optional[FilterTopic] = None,
        topic2: typing.Optional[FilterTopic] = None,
        topic3: typing.Optional[FilterTopic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogsResponse:
        """
        Returns an array of all logs matching the given filter object.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        from_block : typing.Optional[Uint]
            Starting block number or tag.

        to_block : typing.Optional[Uint]
            Ending block number or tag.

        block_hash : typing.Optional[Hash32]
            Block hash. If present, fromBlock and toBlock are not allowed.

        address : typing.Optional[GetEthV1ProofLogsRequestAddress]
            Contract address or a list of addresses from which logs should originate.

        topic0 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic1 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic2 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic3 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogsResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.get_logs()
        """
        _response = self._raw_client.get_logs(
            from_block=from_block,
            to_block=to_block,
            block_hash=block_hash,
            address=address,
            topic0=topic0,
            topic1=topic1,
            topic2=topic2,
            topic3=topic3,
            request_options=request_options,
        )
        return _response.data

    def get_filter_logs(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilterLogsResponse:
        """
        Returns an array of all logs matching the filter with given id.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilterLogsResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.get_filter_logs(
            filter_id="filterId",
        )
        """
        _response = self._raw_client.get_filter_logs(filter_id, request_options=request_options)
        return _response.data

    def get_filter_changes(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilterChangesResponse:
        """
        Returns the changes since the last poll for a given filter id. If filter is of logs type, then corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterChanges` RPC method.
        ### How to verify response?
        > Note: Only applicable for filters of logs type.

        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilterChangesResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.get_filter_changes(
            filter_id="filterId",
        )
        """
        _response = self._raw_client.get_filter_changes(filter_id, request_options=request_options)
        return _response.data

    def create_extended_access_list(
        self,
        *,
        tx: typing.Optional[GenericTransaction] = OMIT,
        validate_tx: typing.Optional[bool] = OMIT,
        block: typing.Optional[BlockNumberOrTagOrHash] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtendedAccessListResponse:
        """
        Returns a list of all addresses and storage keys (along with their EIP-1186 proofs) that are accessed by a given transaction.

        It's an extended list because it includes the `from`, `to` and `block.beneficiary` addresses as well.
        ### Why is this useful?
        Replaces the `eth_createAccessList` RPC method.
        ### How to verify response?
        For each account:
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`: verify the given leaf’s Merkle Proof against the `storageHash`.

        Parameters
        ----------
        tx : typing.Optional[GenericTransaction]

        validate_tx : typing.Optional[bool]
            A flag indicating whether to validate the transaction (such as enforcing gas limit).

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtendedAccessListResponse
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.verifiable.create_extended_access_list()
        """
        _response = self._raw_client.create_extended_access_list(
            tx=tx, validate_tx=validate_tx, block=block, request_options=request_options
        )
        return _response.data


class AsyncVerifiableClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVerifiableClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVerifiableClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVerifiableClient
        """
        return self._raw_client

    async def get_account_information(
        self,
        address: Address,
        *,
        include_code: typing.Optional[bool] = None,
        storage_slots: typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]] = None,
        block: typing.Optional[BlockNumberOrTagOrHash] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Returns information about an address along with its EIP-1186 account proof.
        ### Why is this useful?
        Replaces the `eth_getProof`, `eth_getTransactionCount`, `eth_getBalance`, `eth_getCode`, and `eth_getStorageAt` RPC methods.
        ### How to verify response?
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`, verify the given leaf’s Merkle Proof against the `storageHash`

        Parameters
        ----------
        address : Address
            The address of the account.

        include_code : typing.Optional[bool]
            A flag indicating whether to include the account's code.

        storage_slots : typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]]
            A list of storage positions (in hex) to include in the proof.

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.get_account_information(
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_information(
            address,
            include_code=include_code,
            storage_slots=storage_slots,
            block=block,
            request_options=request_options,
        )
        return _response.data

    async def get_transaction_receipt(
        self, tx_hash: Hash32, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransactionReceiptResponse:
        """
        Returns the receipt of a transaction along with a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getTransactionReceipt` RPC method.
        ### How to verify response?
        - RLP encode the given receipt and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        tx_hash : Hash32
            The hash of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionReceiptResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.get_transaction_receipt(
                tx_hash="txHash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transaction_receipt(tx_hash, request_options=request_options)
        return _response.data

    async def get_logs(
        self,
        *,
        from_block: typing.Optional[Uint] = None,
        to_block: typing.Optional[Uint] = None,
        block_hash: typing.Optional[Hash32] = None,
        address: typing.Optional[GetEthV1ProofLogsRequestAddress] = None,
        topic0: typing.Optional[FilterTopic] = None,
        topic1: typing.Optional[FilterTopic] = None,
        topic2: typing.Optional[FilterTopic] = None,
        topic3: typing.Optional[FilterTopic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogsResponse:
        """
        Returns an array of all logs matching the given filter object.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        from_block : typing.Optional[Uint]
            Starting block number or tag.

        to_block : typing.Optional[Uint]
            Ending block number or tag.

        block_hash : typing.Optional[Hash32]
            Block hash. If present, fromBlock and toBlock are not allowed.

        address : typing.Optional[GetEthV1ProofLogsRequestAddress]
            Contract address or a list of addresses from which logs should originate.

        topic0 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic1 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic2 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic3 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogsResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.get_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs(
            from_block=from_block,
            to_block=to_block,
            block_hash=block_hash,
            address=address,
            topic0=topic0,
            topic1=topic1,
            topic2=topic2,
            topic3=topic3,
            request_options=request_options,
        )
        return _response.data

    async def get_filter_logs(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilterLogsResponse:
        """
        Returns an array of all logs matching the filter with given id.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilterLogsResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.get_filter_logs(
                filter_id="filterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_filter_logs(filter_id, request_options=request_options)
        return _response.data

    async def get_filter_changes(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilterChangesResponse:
        """
        Returns the changes since the last poll for a given filter id. If filter is of logs type, then corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterChanges` RPC method.
        ### How to verify response?
        > Note: Only applicable for filters of logs type.

        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilterChangesResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.get_filter_changes(
                filter_id="filterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_filter_changes(filter_id, request_options=request_options)
        return _response.data

    async def create_extended_access_list(
        self,
        *,
        tx: typing.Optional[GenericTransaction] = OMIT,
        validate_tx: typing.Optional[bool] = OMIT,
        block: typing.Optional[BlockNumberOrTagOrHash] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtendedAccessListResponse:
        """
        Returns a list of all addresses and storage keys (along with their EIP-1186 proofs) that are accessed by a given transaction.

        It's an extended list because it includes the `from`, `to` and `block.beneficiary` addresses as well.
        ### Why is this useful?
        Replaces the `eth_createAccessList` RPC method.
        ### How to verify response?
        For each account:
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`: verify the given leaf’s Merkle Proof against the `storageHash`.

        Parameters
        ----------
        tx : typing.Optional[GenericTransaction]

        validate_tx : typing.Optional[bool]
            A flag indicating whether to validate the transaction (such as enforcing gas limit).

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtendedAccessListResponse
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verifiable.create_extended_access_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_extended_access_list(
            tx=tx, validate_tx=validate_tx, block=block, request_options=request_options
        )
        return _response.data
