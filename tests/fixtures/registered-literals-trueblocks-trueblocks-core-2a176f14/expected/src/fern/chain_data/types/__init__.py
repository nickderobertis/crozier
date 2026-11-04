



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chaindata_blocks_request_flow import ChaindataBlocksRequestFlow
    from .chaindata_blocks_response import ChaindataBlocksResponse
    from .chaindata_blocks_response_data_item import ChaindataBlocksResponseDataItem
    from .chaindata_logs_response import ChaindataLogsResponse
    from .chaindata_logs_response_data_item import ChaindataLogsResponseDataItem
    from .chaindata_receipts_response import ChaindataReceiptsResponse
    from .chaindata_receipts_response_data_item import ChaindataReceiptsResponseDataItem
    from .chaindata_traces_response import ChaindataTracesResponse
    from .chaindata_traces_response_data_item import ChaindataTracesResponseDataItem
    from .chaindata_transactions_request_flow import ChaindataTransactionsRequestFlow
    from .chaindata_transactions_response import ChaindataTransactionsResponse
    from .chaindata_transactions_response_data_item import ChaindataTransactionsResponseDataItem
    from .chaindata_when_response import ChaindataWhenResponse
    from .chaindata_when_response_data_item import ChaindataWhenResponseDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "ChaindataBlocksRequestFlow": ".chaindata_blocks_request_flow",
    "ChaindataBlocksResponse": ".chaindata_blocks_response",
    "ChaindataBlocksResponseDataItem": ".chaindata_blocks_response_data_item",
    "ChaindataLogsResponse": ".chaindata_logs_response",
    "ChaindataLogsResponseDataItem": ".chaindata_logs_response_data_item",
    "ChaindataReceiptsResponse": ".chaindata_receipts_response",
    "ChaindataReceiptsResponseDataItem": ".chaindata_receipts_response_data_item",
    "ChaindataTracesResponse": ".chaindata_traces_response",
    "ChaindataTracesResponseDataItem": ".chaindata_traces_response_data_item",
    "ChaindataTransactionsRequestFlow": ".chaindata_transactions_request_flow",
    "ChaindataTransactionsResponse": ".chaindata_transactions_response",
    "ChaindataTransactionsResponseDataItem": ".chaindata_transactions_response_data_item",
    "ChaindataWhenResponse": ".chaindata_when_response",
    "ChaindataWhenResponseDataItem": ".chaindata_when_response_data_item",
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
    "ChaindataBlocksRequestFlow",
    "ChaindataBlocksResponse",
    "ChaindataBlocksResponseDataItem",
    "ChaindataLogsResponse",
    "ChaindataLogsResponseDataItem",
    "ChaindataReceiptsResponse",
    "ChaindataReceiptsResponseDataItem",
    "ChaindataTracesResponse",
    "ChaindataTracesResponseDataItem",
    "ChaindataTransactionsRequestFlow",
    "ChaindataTransactionsResponse",
    "ChaindataTransactionsResponseDataItem",
    "ChaindataWhenResponse",
    "ChaindataWhenResponseDataItem",
]
