



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_conversation_request_properties import CreateConversationRequestProperties
    from .create_conversation_response import CreateConversationResponse
    from .list_conversations_request_order import ListConversationsRequestOrder
    from .list_conversations_response import ListConversationsResponse
    from .list_conversations_response_embedded import ListConversationsResponseEmbedded
    from .list_conversations_response_embedded_conversations_item import (
        ListConversationsResponseEmbeddedConversationsItem,
    )
    from .list_conversations_response_embedded_conversations_item_links import (
        ListConversationsResponseEmbeddedConversationsItemLinks,
    )
    from .list_conversations_response_embedded_conversations_item_links_self import (
        ListConversationsResponseEmbeddedConversationsItemLinksSelf,
    )
    from .replace_conversation_request_properties import ReplaceConversationRequestProperties
    from .replace_conversation_response import ReplaceConversationResponse
    from .retrieve_conversation_response import RetrieveConversationResponse
    from .retrieve_conversation_response_members_item import RetrieveConversationResponseMembersItem
    from .retrieve_conversation_response_numbers import RetrieveConversationResponseNumbers
    from .retrieve_conversation_response_properties import RetrieveConversationResponseProperties
_dynamic_imports: typing.Dict[str, str] = {
    "CreateConversationRequestProperties": ".create_conversation_request_properties",
    "CreateConversationResponse": ".create_conversation_response",
    "ListConversationsRequestOrder": ".list_conversations_request_order",
    "ListConversationsResponse": ".list_conversations_response",
    "ListConversationsResponseEmbedded": ".list_conversations_response_embedded",
    "ListConversationsResponseEmbeddedConversationsItem": ".list_conversations_response_embedded_conversations_item",
    "ListConversationsResponseEmbeddedConversationsItemLinks": ".list_conversations_response_embedded_conversations_item_links",
    "ListConversationsResponseEmbeddedConversationsItemLinksSelf": ".list_conversations_response_embedded_conversations_item_links_self",
    "ReplaceConversationRequestProperties": ".replace_conversation_request_properties",
    "ReplaceConversationResponse": ".replace_conversation_response",
    "RetrieveConversationResponse": ".retrieve_conversation_response",
    "RetrieveConversationResponseMembersItem": ".retrieve_conversation_response_members_item",
    "RetrieveConversationResponseNumbers": ".retrieve_conversation_response_numbers",
    "RetrieveConversationResponseProperties": ".retrieve_conversation_response_properties",
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
    "CreateConversationRequestProperties",
    "CreateConversationResponse",
    "ListConversationsRequestOrder",
    "ListConversationsResponse",
    "ListConversationsResponseEmbedded",
    "ListConversationsResponseEmbeddedConversationsItem",
    "ListConversationsResponseEmbeddedConversationsItemLinks",
    "ListConversationsResponseEmbeddedConversationsItemLinksSelf",
    "ReplaceConversationRequestProperties",
    "ReplaceConversationResponse",
    "RetrieveConversationResponse",
    "RetrieveConversationResponseMembersItem",
    "RetrieveConversationResponseNumbers",
    "RetrieveConversationResponseProperties",
]
