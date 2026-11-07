



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_siacoin_elements_response import AddressSiacoinElementsResponse
    from .address_siafund_elements_response import AddressSiafundElementsResponse
    from .apply_update import ApplyUpdate
    from .apply_update_data import ApplyUpdateData
    from .attestation import Attestation
    from .attestation_element import AttestationElement
    from .balance import Balance
    from .batch_addresses_request import BatchAddressesRequest
    from .block import Block
    from .block_height import BlockHeight
    from .block_id import BlockId
    from .chain_index import ChainIndex
    from .chain_index_element import ChainIndexElement
    from .check_addresses_response import CheckAddressesResponse
    from .consensus_checkpoint_response import ConsensusCheckpointResponse
    from .consensus_network import ConsensusNetwork
    from .consensus_network_hardfork_asic import ConsensusNetworkHardforkAsic
    from .consensus_network_hardfork_dev_addr import ConsensusNetworkHardforkDevAddr
    from .consensus_network_hardfork_foundation import ConsensusNetworkHardforkFoundation
    from .consensus_network_hardfork_oak import ConsensusNetworkHardforkOak
    from .consensus_network_hardfork_storage_proof import ConsensusNetworkHardforkStorageProof
    from .consensus_network_hardfork_tax import ConsensusNetworkHardforkTax
    from .consensus_network_hardfork_v2 import ConsensusNetworkHardforkV2
    from .consensus_siacoin_input import ConsensusSiacoinInput
    from .consensus_siacoin_output import ConsensusSiacoinOutput
    from .consensus_state import ConsensusState
    from .consensus_transaction import ConsensusTransaction
    from .consensus_updates_response import ConsensusUpdatesResponse
    from .consensus_v2block_data import ConsensusV2BlockData
    from .consensus_v2siacoin_input import ConsensusV2SiacoinInput
    from .consensus_v2transaction import ConsensusV2Transaction
    from .covered_fields import CoveredFields
    from .currency import Currency
    from .element_accumulator import ElementAccumulator
    from .element_spent_response import ElementSpentResponse
    from .event import Event
    from .event_index import EventIndex
    from .event_type import EventType
    from .file_contract import FileContract
    from .file_contract_element import FileContractElement
    from .file_contract_element_diff import FileContractElementDiff
    from .file_contract_element_diff_revision import FileContractElementDiffRevision
    from .file_contract_id import FileContractId
    from .file_contract_revision import FileContractRevision
    from .gateway_peer import GatewayPeer
    from .hash256 import Hash256
    from .index_mode import IndexMode
    from .public_key import PublicKey
    from .rescan_response import RescanResponse
    from .revert_update import RevertUpdate
    from .revert_update_data import RevertUpdateData
    from .satisfied_policy import SatisfiedPolicy
    from .siacoin_element import SiacoinElement
    from .siacoin_element_diff import SiacoinElementDiff
    from .siacoin_input import SiacoinInput
    from .siacoin_origin import SiacoinOrigin
    from .siacoin_origin_source import SiacoinOriginSource
    from .siacoin_output import SiacoinOutput
    from .siacoin_output_id import SiacoinOutputId
    from .siacoin_output_with_id import SiacoinOutputWithId
    from .siafund_element import SiafundElement
    from .siafund_element_diff import SiafundElementDiff
    from .siafund_input import SiafundInput
    from .siafund_output import SiafundOutput
    from .siafund_output_id import SiafundOutputId
    from .siafund_output_with_id import SiafundOutputWithId
    from .signature import Signature
    from .spend_policy import SpendPolicy
    from .spend_policy_type import SpendPolicyType
    from .state_element import StateElement
    from .state_response import StateResponse
    from .storage_proof import StorageProof
    from .transaction import Transaction
    from .transaction_id import TransactionId
    from .transaction_signature import TransactionSignature
    from .txpool_broadcast_response import TxpoolBroadcastResponse
    from .txpool_transactions_response import TxpoolTransactionsResponse
    from .txpool_update_v2transactions_response import TxpoolUpdateV2TransactionsResponse
    from .unlock_conditions import UnlockConditions
    from .unlock_key import UnlockKey
    from .unspent_siacoin_element import UnspentSiacoinElement
    from .unspent_siacoin_elements_response import UnspentSiacoinElementsResponse
    from .unspent_siafund_element import UnspentSiafundElement
    from .unspent_siafund_elements_response import UnspentSiafundElementsResponse
    from .v2block_data import V2BlockData
    from .v2file_contract import V2FileContract
    from .v2file_contract_element import V2FileContractElement
    from .v2file_contract_element_diff import V2FileContractElementDiff
    from .v2file_contract_element_diff_resolution import V2FileContractElementDiffResolution
    from .v2file_contract_element_diff_revision import V2FileContractElementDiffRevision
    from .v2file_contract_expiration import V2FileContractExpiration
    from .v2file_contract_renewal import V2FileContractRenewal
    from .v2file_contract_resolution import V2FileContractResolution
    from .v2file_contract_resolution_resolution import V2FileContractResolutionResolution
    from .v2file_contract_resolution_type import V2FileContractResolutionType
    from .v2file_contract_revision import V2FileContractRevision
    from .v2siacoin_input import V2SiacoinInput
    from .v2siafund_input import V2SiafundInput
    from .v2storage_proof import V2StorageProof
    from .v2transaction import V2Transaction
    from .wallet import Wallet
    from .wallet_address import WalletAddress
    from .wallet_construct_request import WalletConstructRequest
    from .wallet_construct_response import WalletConstructResponse
    from .wallet_construct_v2response import WalletConstructV2Response
    from .wallet_fund_response import WalletFundResponse
    from .wallet_update_request import WalletUpdateRequest
    from .work import Work
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressSiacoinElementsResponse": ".address_siacoin_elements_response",
    "AddressSiafundElementsResponse": ".address_siafund_elements_response",
    "ApplyUpdate": ".apply_update",
    "ApplyUpdateData": ".apply_update_data",
    "Attestation": ".attestation",
    "AttestationElement": ".attestation_element",
    "Balance": ".balance",
    "BatchAddressesRequest": ".batch_addresses_request",
    "Block": ".block",
    "BlockHeight": ".block_height",
    "BlockId": ".block_id",
    "ChainIndex": ".chain_index",
    "ChainIndexElement": ".chain_index_element",
    "CheckAddressesResponse": ".check_addresses_response",
    "ConsensusCheckpointResponse": ".consensus_checkpoint_response",
    "ConsensusNetwork": ".consensus_network",
    "ConsensusNetworkHardforkAsic": ".consensus_network_hardfork_asic",
    "ConsensusNetworkHardforkDevAddr": ".consensus_network_hardfork_dev_addr",
    "ConsensusNetworkHardforkFoundation": ".consensus_network_hardfork_foundation",
    "ConsensusNetworkHardforkOak": ".consensus_network_hardfork_oak",
    "ConsensusNetworkHardforkStorageProof": ".consensus_network_hardfork_storage_proof",
    "ConsensusNetworkHardforkTax": ".consensus_network_hardfork_tax",
    "ConsensusNetworkHardforkV2": ".consensus_network_hardfork_v2",
    "ConsensusSiacoinInput": ".consensus_siacoin_input",
    "ConsensusSiacoinOutput": ".consensus_siacoin_output",
    "ConsensusState": ".consensus_state",
    "ConsensusTransaction": ".consensus_transaction",
    "ConsensusUpdatesResponse": ".consensus_updates_response",
    "ConsensusV2BlockData": ".consensus_v2block_data",
    "ConsensusV2SiacoinInput": ".consensus_v2siacoin_input",
    "ConsensusV2Transaction": ".consensus_v2transaction",
    "CoveredFields": ".covered_fields",
    "Currency": ".currency",
    "ElementAccumulator": ".element_accumulator",
    "ElementSpentResponse": ".element_spent_response",
    "Event": ".event",
    "EventIndex": ".event_index",
    "EventType": ".event_type",
    "FileContract": ".file_contract",
    "FileContractElement": ".file_contract_element",
    "FileContractElementDiff": ".file_contract_element_diff",
    "FileContractElementDiffRevision": ".file_contract_element_diff_revision",
    "FileContractId": ".file_contract_id",
    "FileContractRevision": ".file_contract_revision",
    "GatewayPeer": ".gateway_peer",
    "Hash256": ".hash256",
    "IndexMode": ".index_mode",
    "PublicKey": ".public_key",
    "RescanResponse": ".rescan_response",
    "RevertUpdate": ".revert_update",
    "RevertUpdateData": ".revert_update_data",
    "SatisfiedPolicy": ".satisfied_policy",
    "SiacoinElement": ".siacoin_element",
    "SiacoinElementDiff": ".siacoin_element_diff",
    "SiacoinInput": ".siacoin_input",
    "SiacoinOrigin": ".siacoin_origin",
    "SiacoinOriginSource": ".siacoin_origin_source",
    "SiacoinOutput": ".siacoin_output",
    "SiacoinOutputId": ".siacoin_output_id",
    "SiacoinOutputWithId": ".siacoin_output_with_id",
    "SiafundElement": ".siafund_element",
    "SiafundElementDiff": ".siafund_element_diff",
    "SiafundInput": ".siafund_input",
    "SiafundOutput": ".siafund_output",
    "SiafundOutputId": ".siafund_output_id",
    "SiafundOutputWithId": ".siafund_output_with_id",
    "Signature": ".signature",
    "SpendPolicy": ".spend_policy",
    "SpendPolicyType": ".spend_policy_type",
    "StateElement": ".state_element",
    "StateResponse": ".state_response",
    "StorageProof": ".storage_proof",
    "Transaction": ".transaction",
    "TransactionId": ".transaction_id",
    "TransactionSignature": ".transaction_signature",
    "TxpoolBroadcastResponse": ".txpool_broadcast_response",
    "TxpoolTransactionsResponse": ".txpool_transactions_response",
    "TxpoolUpdateV2TransactionsResponse": ".txpool_update_v2transactions_response",
    "UnlockConditions": ".unlock_conditions",
    "UnlockKey": ".unlock_key",
    "UnspentSiacoinElement": ".unspent_siacoin_element",
    "UnspentSiacoinElementsResponse": ".unspent_siacoin_elements_response",
    "UnspentSiafundElement": ".unspent_siafund_element",
    "UnspentSiafundElementsResponse": ".unspent_siafund_elements_response",
    "V2BlockData": ".v2block_data",
    "V2FileContract": ".v2file_contract",
    "V2FileContractElement": ".v2file_contract_element",
    "V2FileContractElementDiff": ".v2file_contract_element_diff",
    "V2FileContractElementDiffResolution": ".v2file_contract_element_diff_resolution",
    "V2FileContractElementDiffRevision": ".v2file_contract_element_diff_revision",
    "V2FileContractExpiration": ".v2file_contract_expiration",
    "V2FileContractRenewal": ".v2file_contract_renewal",
    "V2FileContractResolution": ".v2file_contract_resolution",
    "V2FileContractResolutionResolution": ".v2file_contract_resolution_resolution",
    "V2FileContractResolutionType": ".v2file_contract_resolution_type",
    "V2FileContractRevision": ".v2file_contract_revision",
    "V2SiacoinInput": ".v2siacoin_input",
    "V2SiafundInput": ".v2siafund_input",
    "V2StorageProof": ".v2storage_proof",
    "V2Transaction": ".v2transaction",
    "Wallet": ".wallet",
    "WalletAddress": ".wallet_address",
    "WalletConstructRequest": ".wallet_construct_request",
    "WalletConstructResponse": ".wallet_construct_response",
    "WalletConstructV2Response": ".wallet_construct_v2response",
    "WalletFundResponse": ".wallet_fund_response",
    "WalletUpdateRequest": ".wallet_update_request",
    "Work": ".work",
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
    "Address",
    "AddressSiacoinElementsResponse",
    "AddressSiafundElementsResponse",
    "ApplyUpdate",
    "ApplyUpdateData",
    "Attestation",
    "AttestationElement",
    "Balance",
    "BatchAddressesRequest",
    "Block",
    "BlockHeight",
    "BlockId",
    "ChainIndex",
    "ChainIndexElement",
    "CheckAddressesResponse",
    "ConsensusCheckpointResponse",
    "ConsensusNetwork",
    "ConsensusNetworkHardforkAsic",
    "ConsensusNetworkHardforkDevAddr",
    "ConsensusNetworkHardforkFoundation",
    "ConsensusNetworkHardforkOak",
    "ConsensusNetworkHardforkStorageProof",
    "ConsensusNetworkHardforkTax",
    "ConsensusNetworkHardforkV2",
    "ConsensusSiacoinInput",
    "ConsensusSiacoinOutput",
    "ConsensusState",
    "ConsensusTransaction",
    "ConsensusUpdatesResponse",
    "ConsensusV2BlockData",
    "ConsensusV2SiacoinInput",
    "ConsensusV2Transaction",
    "CoveredFields",
    "Currency",
    "ElementAccumulator",
    "ElementSpentResponse",
    "Event",
    "EventIndex",
    "EventType",
    "FileContract",
    "FileContractElement",
    "FileContractElementDiff",
    "FileContractElementDiffRevision",
    "FileContractId",
    "FileContractRevision",
    "GatewayPeer",
    "Hash256",
    "IndexMode",
    "PublicKey",
    "RescanResponse",
    "RevertUpdate",
    "RevertUpdateData",
    "SatisfiedPolicy",
    "SiacoinElement",
    "SiacoinElementDiff",
    "SiacoinInput",
    "SiacoinOrigin",
    "SiacoinOriginSource",
    "SiacoinOutput",
    "SiacoinOutputId",
    "SiacoinOutputWithId",
    "SiafundElement",
    "SiafundElementDiff",
    "SiafundInput",
    "SiafundOutput",
    "SiafundOutputId",
    "SiafundOutputWithId",
    "Signature",
    "SpendPolicy",
    "SpendPolicyType",
    "StateElement",
    "StateResponse",
    "StorageProof",
    "Transaction",
    "TransactionId",
    "TransactionSignature",
    "TxpoolBroadcastResponse",
    "TxpoolTransactionsResponse",
    "TxpoolUpdateV2TransactionsResponse",
    "UnlockConditions",
    "UnlockKey",
    "UnspentSiacoinElement",
    "UnspentSiacoinElementsResponse",
    "UnspentSiafundElement",
    "UnspentSiafundElementsResponse",
    "V2BlockData",
    "V2FileContract",
    "V2FileContractElement",
    "V2FileContractElementDiff",
    "V2FileContractElementDiffResolution",
    "V2FileContractElementDiffRevision",
    "V2FileContractExpiration",
    "V2FileContractRenewal",
    "V2FileContractResolution",
    "V2FileContractResolutionResolution",
    "V2FileContractResolutionType",
    "V2FileContractRevision",
    "V2SiacoinInput",
    "V2SiafundInput",
    "V2StorageProof",
    "V2Transaction",
    "Wallet",
    "WalletAddress",
    "WalletConstructRequest",
    "WalletConstructResponse",
    "WalletConstructV2Response",
    "WalletFundResponse",
    "WalletUpdateRequest",
    "Work",
]
