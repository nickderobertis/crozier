



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .attach_knowledge_item_to_agent_response import AttachKnowledgeItemToAgentResponse
    from .create_knowledge_item_request_source_type import CreateKnowledgeItemRequestSourceType
    from .create_knowledge_item_response import CreateKnowledgeItemResponse
    from .delete_knowledge_item_response import DeleteKnowledgeItemResponse
    from .detach_knowledge_item_from_agent_response import DetachKnowledgeItemFromAgentResponse
    from .get_knowledge_item_response import GetKnowledgeItemResponse
    from .get_knowledge_item_response_item import GetKnowledgeItemResponseItem
    from .get_knowledge_item_response_item_agents_item import GetKnowledgeItemResponseItemAgentsItem
    from .get_knowledge_item_response_item_source_type import GetKnowledgeItemResponseItemSourceType
    from .get_knowledge_item_response_item_status import GetKnowledgeItemResponseItemStatus
    from .list_agent_knowledge_items_response import ListAgentKnowledgeItemsResponse
    from .list_knowledge_items_request_source_type import ListKnowledgeItemsRequestSourceType
    from .list_knowledge_items_request_status import ListKnowledgeItemsRequestStatus
    from .list_knowledge_items_response import ListKnowledgeItemsResponse
    from .list_knowledge_items_response_items_item import ListKnowledgeItemsResponseItemsItem
    from .list_knowledge_items_response_items_item_source_type import ListKnowledgeItemsResponseItemsItemSourceType
    from .list_knowledge_items_response_items_item_status import ListKnowledgeItemsResponseItemsItemStatus
    from .list_knowledge_items_response_pagination import ListKnowledgeItemsResponsePagination
    from .reingest_knowledge_item_response import ReingestKnowledgeItemResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AttachKnowledgeItemToAgentResponse": ".attach_knowledge_item_to_agent_response",
    "CreateKnowledgeItemRequestSourceType": ".create_knowledge_item_request_source_type",
    "CreateKnowledgeItemResponse": ".create_knowledge_item_response",
    "DeleteKnowledgeItemResponse": ".delete_knowledge_item_response",
    "DetachKnowledgeItemFromAgentResponse": ".detach_knowledge_item_from_agent_response",
    "GetKnowledgeItemResponse": ".get_knowledge_item_response",
    "GetKnowledgeItemResponseItem": ".get_knowledge_item_response_item",
    "GetKnowledgeItemResponseItemAgentsItem": ".get_knowledge_item_response_item_agents_item",
    "GetKnowledgeItemResponseItemSourceType": ".get_knowledge_item_response_item_source_type",
    "GetKnowledgeItemResponseItemStatus": ".get_knowledge_item_response_item_status",
    "ListAgentKnowledgeItemsResponse": ".list_agent_knowledge_items_response",
    "ListKnowledgeItemsRequestSourceType": ".list_knowledge_items_request_source_type",
    "ListKnowledgeItemsRequestStatus": ".list_knowledge_items_request_status",
    "ListKnowledgeItemsResponse": ".list_knowledge_items_response",
    "ListKnowledgeItemsResponseItemsItem": ".list_knowledge_items_response_items_item",
    "ListKnowledgeItemsResponseItemsItemSourceType": ".list_knowledge_items_response_items_item_source_type",
    "ListKnowledgeItemsResponseItemsItemStatus": ".list_knowledge_items_response_items_item_status",
    "ListKnowledgeItemsResponsePagination": ".list_knowledge_items_response_pagination",
    "ReingestKnowledgeItemResponse": ".reingest_knowledge_item_response",
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
