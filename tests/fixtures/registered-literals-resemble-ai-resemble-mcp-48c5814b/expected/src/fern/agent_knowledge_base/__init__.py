



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AttachKnowledgeItemToAgentResponse,
        CreateKnowledgeItemRequestSourceType,
        CreateKnowledgeItemResponse,
        DeleteKnowledgeItemResponse,
        DetachKnowledgeItemFromAgentResponse,
        GetKnowledgeItemResponse,
        GetKnowledgeItemResponseItem,
        GetKnowledgeItemResponseItemAgentsItem,
        GetKnowledgeItemResponseItemSourceType,
        GetKnowledgeItemResponseItemStatus,
        ListAgentKnowledgeItemsResponse,
        ListKnowledgeItemsRequestSourceType,
        ListKnowledgeItemsRequestStatus,
        ListKnowledgeItemsResponse,
        ListKnowledgeItemsResponseItemsItem,
        ListKnowledgeItemsResponseItemsItemSourceType,
        ListKnowledgeItemsResponseItemsItemStatus,
        ListKnowledgeItemsResponsePagination,
        ReingestKnowledgeItemResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AttachKnowledgeItemToAgentResponse": ".types",
    "CreateKnowledgeItemRequestSourceType": ".types",
    "CreateKnowledgeItemResponse": ".types",
    "DeleteKnowledgeItemResponse": ".types",
    "DetachKnowledgeItemFromAgentResponse": ".types",
    "GetKnowledgeItemResponse": ".types",
    "GetKnowledgeItemResponseItem": ".types",
    "GetKnowledgeItemResponseItemAgentsItem": ".types",
    "GetKnowledgeItemResponseItemSourceType": ".types",
    "GetKnowledgeItemResponseItemStatus": ".types",
    "ListAgentKnowledgeItemsResponse": ".types",
    "ListKnowledgeItemsRequestSourceType": ".types",
    "ListKnowledgeItemsRequestStatus": ".types",
    "ListKnowledgeItemsResponse": ".types",
    "ListKnowledgeItemsResponseItemsItem": ".types",
    "ListKnowledgeItemsResponseItemsItemSourceType": ".types",
    "ListKnowledgeItemsResponseItemsItemStatus": ".types",
    "ListKnowledgeItemsResponsePagination": ".types",
    "ReingestKnowledgeItemResponse": ".types",
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
    "AttachKnowledgeItemToAgentResponse",
    "CreateKnowledgeItemRequestSourceType",
    "CreateKnowledgeItemResponse",
    "DeleteKnowledgeItemResponse",
    "DetachKnowledgeItemFromAgentResponse",
    "GetKnowledgeItemResponse",
    "GetKnowledgeItemResponseItem",
    "GetKnowledgeItemResponseItemAgentsItem",
    "GetKnowledgeItemResponseItemSourceType",
    "GetKnowledgeItemResponseItemStatus",
    "ListAgentKnowledgeItemsResponse",
    "ListKnowledgeItemsRequestSourceType",
    "ListKnowledgeItemsRequestStatus",
    "ListKnowledgeItemsResponse",
    "ListKnowledgeItemsResponseItemsItem",
    "ListKnowledgeItemsResponseItemsItemSourceType",
    "ListKnowledgeItemsResponseItemsItemStatus",
    "ListKnowledgeItemsResponsePagination",
    "ReingestKnowledgeItemResponse",
]
