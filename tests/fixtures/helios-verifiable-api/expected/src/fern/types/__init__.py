



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_list import AccessList
    from .access_list_entry import AccessListEntry
    from .account_response import AccountResponse
    from .account_response_account import AccountResponseAccount
    from .address import Address
    from .addresses import Addresses
    from .authorization_list import AuthorizationList
    from .authorization_list_item import AuthorizationListItem
    from .block import Block
    from .block_number_or_tag_or_hash import BlockNumberOrTagOrHash
    from .block_receipts_response import BlockReceiptsResponse
    from .block_response import BlockResponse
    from .block_tag import BlockTag
    from .block_transactions import BlockTransactions
    from .byte import Byte
    from .bytes import Bytes
    from .bytes256 import Bytes256
    from .bytes32 import Bytes32
    from .bytes8 import Bytes8
    from .bytes_max32 import BytesMax32
    from .chain_id_response import ChainIdResponse
    from .error_response import ErrorResponse
    from .extended_access_list_response import ExtendedAccessListResponse
    from .filter import Filter
    from .filter_block_hash import FilterBlockHash
    from .filter_block_hash_address import FilterBlockHashAddress
    from .filter_changes_response import FilterChangesResponse
    from .filter_changes_response_hashes import FilterChangesResponseHashes
    from .filter_from_block import FilterFromBlock
    from .filter_from_block_address import FilterFromBlockAddress
    from .filter_logs_response import FilterLogsResponse
    from .filter_topic import FilterTopic
    from .filter_topics import FilterTopics
    from .generic_transaction import GenericTransaction
    from .get_eth_v1proof_logs_request_address import GetEthV1ProofLogsRequestAddress
    from .hash32 import Hash32
    from .log import Log
    from .logs_response import LogsResponse
    from .new_filter_request_kind import NewFilterRequestKind
    from .new_filter_response import NewFilterResponse
    from .new_filter_response_kind import NewFilterResponseKind
    from .receipt_info import ReceiptInfo
    from .receipt_proofs_map import ReceiptProofsMap
    from .send_raw_tx_response import SendRawTxResponse
    from .storage_proof import StorageProof
    from .transaction_info import TransactionInfo
    from .transaction_receipt import TransactionReceipt
    from .transaction_receipt_response import TransactionReceiptResponse
    from .uint import Uint
    from .uint256 import Uint256
    from .uint64 import Uint64
    from .uninstall_filter_response import UninstallFilterResponse
    from .withdrawal import Withdrawal
_dynamic_imports: typing.Dict[str, str] = {
    "AccessList": ".access_list",
    "AccessListEntry": ".access_list_entry",
    "AccountResponse": ".account_response",
    "AccountResponseAccount": ".account_response_account",
    "Address": ".address",
    "Addresses": ".addresses",
    "AuthorizationList": ".authorization_list",
    "AuthorizationListItem": ".authorization_list_item",
    "Block": ".block",
    "BlockNumberOrTagOrHash": ".block_number_or_tag_or_hash",
    "BlockReceiptsResponse": ".block_receipts_response",
    "BlockResponse": ".block_response",
    "BlockTag": ".block_tag",
    "BlockTransactions": ".block_transactions",
    "Byte": ".byte",
    "Bytes": ".bytes",
    "Bytes256": ".bytes256",
    "Bytes32": ".bytes32",
    "Bytes8": ".bytes8",
    "BytesMax32": ".bytes_max32",
    "ChainIdResponse": ".chain_id_response",
    "ErrorResponse": ".error_response",
    "ExtendedAccessListResponse": ".extended_access_list_response",
    "Filter": ".filter",
    "FilterBlockHash": ".filter_block_hash",
    "FilterBlockHashAddress": ".filter_block_hash_address",
    "FilterChangesResponse": ".filter_changes_response",
    "FilterChangesResponseHashes": ".filter_changes_response_hashes",
    "FilterFromBlock": ".filter_from_block",
    "FilterFromBlockAddress": ".filter_from_block_address",
    "FilterLogsResponse": ".filter_logs_response",
    "FilterTopic": ".filter_topic",
    "FilterTopics": ".filter_topics",
    "GenericTransaction": ".generic_transaction",
    "GetEthV1ProofLogsRequestAddress": ".get_eth_v1proof_logs_request_address",
    "Hash32": ".hash32",
    "Log": ".log",
    "LogsResponse": ".logs_response",
    "NewFilterRequestKind": ".new_filter_request_kind",
    "NewFilterResponse": ".new_filter_response",
    "NewFilterResponseKind": ".new_filter_response_kind",
    "ReceiptInfo": ".receipt_info",
    "ReceiptProofsMap": ".receipt_proofs_map",
    "SendRawTxResponse": ".send_raw_tx_response",
    "StorageProof": ".storage_proof",
    "TransactionInfo": ".transaction_info",
    "TransactionReceipt": ".transaction_receipt",
    "TransactionReceiptResponse": ".transaction_receipt_response",
    "Uint": ".uint",
    "Uint256": ".uint256",
    "Uint64": ".uint64",
    "UninstallFilterResponse": ".uninstall_filter_response",
    "Withdrawal": ".withdrawal",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccessList",
    "AccessListEntry",
    "AccountResponse",
    "AccountResponseAccount",
    "Address",
    "Addresses",
    "AuthorizationList",
    "AuthorizationListItem",
    "Block",
    "BlockNumberOrTagOrHash",
    "BlockReceiptsResponse",
    "BlockResponse",
    "BlockTag",
    "BlockTransactions",
    "Byte",
    "Bytes",
    "Bytes256",
    "Bytes32",
    "Bytes8",
    "BytesMax32",
    "ChainIdResponse",
    "ErrorResponse",
    "ExtendedAccessListResponse",
    "Filter",
    "FilterBlockHash",
    "FilterBlockHashAddress",
    "FilterChangesResponse",
    "FilterChangesResponseHashes",
    "FilterFromBlock",
    "FilterFromBlockAddress",
    "FilterLogsResponse",
    "FilterTopic",
    "FilterTopics",
    "GenericTransaction",
    "GetEthV1ProofLogsRequestAddress",
    "Hash32",
    "Log",
    "LogsResponse",
    "NewFilterRequestKind",
    "NewFilterResponse",
    "NewFilterResponseKind",
    "ReceiptInfo",
    "ReceiptProofsMap",
    "SendRawTxResponse",
    "StorageProof",
    "TransactionInfo",
    "TransactionReceipt",
    "TransactionReceiptResponse",
    "Uint",
    "Uint256",
    "Uint64",
    "UninstallFilterResponse",
    "Withdrawal",
]
