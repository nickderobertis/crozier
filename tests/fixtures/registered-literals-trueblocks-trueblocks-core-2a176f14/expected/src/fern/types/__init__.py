



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abi import Abi
    from .addr_record import AddrRecord
    from .address import Address
    from .any import Any
    from .app_record import AppRecord
    from .appearance import Appearance
    from .appearance_table import AppearanceTable
    from .approval import Approval
    from .block import Block
    from .block_count import BlockCount
    from .bounds import Bounds
    from .cache_item import CacheItem
    from .chain import Chain
    from .chunk_address import ChunkAddress
    from .chunk_bloom import ChunkBloom
    from .chunk_index import ChunkIndex
    from .chunk_pin import ChunkPin
    from .chunk_record import ChunkRecord
    from .chunk_stats import ChunkStats
    from .contract import Contract
    from .count import Count
    from .destination import Destination
    from .function import Function
    from .hash import Hash
    from .ipfs_pin import IpfsPin
    from .light_block import LightBlock
    from .log import Log
    from .manifest import Manifest
    from .message import Message
    from .monitor import Monitor
    from .monitor_clean import MonitorClean
    from .name import Name
    from .named_block import NamedBlock
    from .parameter import Parameter
    from .range_dates import RangeDates
    from .receipt import Receipt
    from .report_check import ReportCheck
    from .response import Response
    from .result import Result
    from .slurp import Slurp
    from .state import State
    from .statement import Statement
    from .status import Status
    from .string import String
    from .timestamp import Timestamp
    from .token import Token
    from .token_type import TokenType
    from .topic import Topic
    from .trace import Trace
    from .trace_action import TraceAction
    from .trace_count import TraceCount
    from .trace_filter import TraceFilter
    from .trace_result import TraceResult
    from .transaction import Transaction
    from .transfer import Transfer
    from .uint64 import Uint64
    from .withdrawal import Withdrawal
_dynamic_imports: typing.Dict[str, str] = {
    "Abi": ".abi",
    "AddrRecord": ".addr_record",
    "Address": ".address",
    "Any": ".any",
    "AppRecord": ".app_record",
    "Appearance": ".appearance",
    "AppearanceTable": ".appearance_table",
    "Approval": ".approval",
    "Block": ".block",
    "BlockCount": ".block_count",
    "Bounds": ".bounds",
    "CacheItem": ".cache_item",
    "Chain": ".chain",
    "ChunkAddress": ".chunk_address",
    "ChunkBloom": ".chunk_bloom",
    "ChunkIndex": ".chunk_index",
    "ChunkPin": ".chunk_pin",
    "ChunkRecord": ".chunk_record",
    "ChunkStats": ".chunk_stats",
    "Contract": ".contract",
    "Count": ".count",
    "Destination": ".destination",
    "Function": ".function",
    "Hash": ".hash",
    "IpfsPin": ".ipfs_pin",
    "LightBlock": ".light_block",
    "Log": ".log",
    "Manifest": ".manifest",
    "Message": ".message",
    "Monitor": ".monitor",
    "MonitorClean": ".monitor_clean",
    "Name": ".name",
    "NamedBlock": ".named_block",
    "Parameter": ".parameter",
    "RangeDates": ".range_dates",
    "Receipt": ".receipt",
    "ReportCheck": ".report_check",
    "Response": ".response",
    "Result": ".result",
    "Slurp": ".slurp",
    "State": ".state",
    "Statement": ".statement",
    "Status": ".status",
    "String": ".string",
    "Timestamp": ".timestamp",
    "Token": ".token",
    "TokenType": ".token_type",
    "Topic": ".topic",
    "Trace": ".trace",
    "TraceAction": ".trace_action",
    "TraceCount": ".trace_count",
    "TraceFilter": ".trace_filter",
    "TraceResult": ".trace_result",
    "Transaction": ".transaction",
    "Transfer": ".transfer",
    "Uint64": ".uint64",
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
    "Abi",
    "AddrRecord",
    "Address",
    "Any",
    "AppRecord",
    "Appearance",
    "AppearanceTable",
    "Approval",
    "Block",
    "BlockCount",
    "Bounds",
    "CacheItem",
    "Chain",
    "ChunkAddress",
    "ChunkBloom",
    "ChunkIndex",
    "ChunkPin",
    "ChunkRecord",
    "ChunkStats",
    "Contract",
    "Count",
    "Destination",
    "Function",
    "Hash",
    "IpfsPin",
    "LightBlock",
    "Log",
    "Manifest",
    "Message",
    "Monitor",
    "MonitorClean",
    "Name",
    "NamedBlock",
    "Parameter",
    "RangeDates",
    "Receipt",
    "ReportCheck",
    "Response",
    "Result",
    "Slurp",
    "State",
    "Statement",
    "Status",
    "String",
    "Timestamp",
    "Token",
    "TokenType",
    "Topic",
    "Trace",
    "TraceAction",
    "TraceCount",
    "TraceFilter",
    "TraceResult",
    "Transaction",
    "Transfer",
    "Uint64",
    "Withdrawal",
]
