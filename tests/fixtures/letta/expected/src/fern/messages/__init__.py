



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ListAllMessagesRequestOrder,
        ListBatchesRequestOrder,
        ListBatchesRequestOrderBy,
        ListMessagesForBatchRequestOrder,
        ListMessagesForBatchRequestOrderBy,
        SearchAllMessagesRequestSearchMode,
        SearchAllMessagesResponseItem,
        SearchAllMessagesResponseItem_AssistantMessage,
        SearchAllMessagesResponseItem_ReasoningMessage,
        SearchAllMessagesResponseItem_SystemMessage,
        SearchAllMessagesResponseItem_UserMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ListAllMessagesRequestOrder": ".types",
    "ListBatchesRequestOrder": ".types",
    "ListBatchesRequestOrderBy": ".types",
    "ListMessagesForBatchRequestOrder": ".types",
    "ListMessagesForBatchRequestOrderBy": ".types",
    "SearchAllMessagesRequestSearchMode": ".types",
    "SearchAllMessagesResponseItem": ".types",
    "SearchAllMessagesResponseItem_AssistantMessage": ".types",
    "SearchAllMessagesResponseItem_ReasoningMessage": ".types",
    "SearchAllMessagesResponseItem_SystemMessage": ".types",
    "SearchAllMessagesResponseItem_UserMessage": ".types",
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
