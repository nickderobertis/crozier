



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_all_messages_request_order import ListAllMessagesRequestOrder
    from .list_batches_request_order import ListBatchesRequestOrder
    from .list_batches_request_order_by import ListBatchesRequestOrderBy
    from .list_messages_for_batch_request_order import ListMessagesForBatchRequestOrder
    from .list_messages_for_batch_request_order_by import ListMessagesForBatchRequestOrderBy
    from .search_all_messages_request_search_mode import SearchAllMessagesRequestSearchMode
    from .search_all_messages_response_item import (
        SearchAllMessagesResponseItem,
        SearchAllMessagesResponseItem_AssistantMessage,
        SearchAllMessagesResponseItem_ReasoningMessage,
        SearchAllMessagesResponseItem_SystemMessage,
        SearchAllMessagesResponseItem_UserMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ListAllMessagesRequestOrder": ".list_all_messages_request_order",
    "ListBatchesRequestOrder": ".list_batches_request_order",
    "ListBatchesRequestOrderBy": ".list_batches_request_order_by",
    "ListMessagesForBatchRequestOrder": ".list_messages_for_batch_request_order",
    "ListMessagesForBatchRequestOrderBy": ".list_messages_for_batch_request_order_by",
    "SearchAllMessagesRequestSearchMode": ".search_all_messages_request_search_mode",
    "SearchAllMessagesResponseItem": ".search_all_messages_response_item",
    "SearchAllMessagesResponseItem_AssistantMessage": ".search_all_messages_response_item",
    "SearchAllMessagesResponseItem_ReasoningMessage": ".search_all_messages_response_item",
    "SearchAllMessagesResponseItem_SystemMessage": ".search_all_messages_response_item",
    "SearchAllMessagesResponseItem_UserMessage": ".search_all_messages_response_item",
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
    "ListAllMessagesRequestOrder",
    "ListBatchesRequestOrder",
    "ListBatchesRequestOrderBy",
    "ListMessagesForBatchRequestOrder",
    "ListMessagesForBatchRequestOrderBy",
    "SearchAllMessagesRequestSearchMode",
    "SearchAllMessagesResponseItem",
    "SearchAllMessagesResponseItem_AssistantMessage",
    "SearchAllMessagesResponseItem_ReasoningMessage",
    "SearchAllMessagesResponseItem_SystemMessage",
    "SearchAllMessagesResponseItem_UserMessage",
]
