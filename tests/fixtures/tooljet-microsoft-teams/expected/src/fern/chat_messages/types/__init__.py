



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_all_messages_for_user_request_model import GetAllMessagesForUserRequestModel
    from .get_all_messages_for_user_response import GetAllMessagesForUserResponse
    from .get_chat_message_request_expand import GetChatMessageRequestExpand
    from .list_chat_messages_response import ListChatMessagesResponse
    from .send_chat_message_request_body import SendChatMessageRequestBody
    from .send_chat_message_request_body_content_type import SendChatMessageRequestBodyContentType
    from .send_chat_message_request_hosted_contents_item import SendChatMessageRequestHostedContentsItem
    from .send_chat_message_request_importance import SendChatMessageRequestImportance
    from .send_chat_message_request_mentions_item import SendChatMessageRequestMentionsItem
    from .send_chat_message_request_mentions_item_mentioned import SendChatMessageRequestMentionsItemMentioned
    from .send_chat_message_request_mentions_item_mentioned_user import SendChatMessageRequestMentionsItemMentionedUser
    from .update_chat_message_request_body import UpdateChatMessageRequestBody
    from .update_chat_message_request_body_content_type import UpdateChatMessageRequestBodyContentType
_dynamic_imports: typing.Dict[str, str] = {
    "GetAllMessagesForUserRequestModel": ".get_all_messages_for_user_request_model",
    "GetAllMessagesForUserResponse": ".get_all_messages_for_user_response",
    "GetChatMessageRequestExpand": ".get_chat_message_request_expand",
    "ListChatMessagesResponse": ".list_chat_messages_response",
    "SendChatMessageRequestBody": ".send_chat_message_request_body",
    "SendChatMessageRequestBodyContentType": ".send_chat_message_request_body_content_type",
    "SendChatMessageRequestHostedContentsItem": ".send_chat_message_request_hosted_contents_item",
    "SendChatMessageRequestImportance": ".send_chat_message_request_importance",
    "SendChatMessageRequestMentionsItem": ".send_chat_message_request_mentions_item",
    "SendChatMessageRequestMentionsItemMentioned": ".send_chat_message_request_mentions_item_mentioned",
    "SendChatMessageRequestMentionsItemMentionedUser": ".send_chat_message_request_mentions_item_mentioned_user",
    "UpdateChatMessageRequestBody": ".update_chat_message_request_body",
    "UpdateChatMessageRequestBodyContentType": ".update_chat_message_request_body_content_type",
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
    "GetAllMessagesForUserRequestModel",
    "GetAllMessagesForUserResponse",
    "GetChatMessageRequestExpand",
    "ListChatMessagesResponse",
    "SendChatMessageRequestBody",
    "SendChatMessageRequestBodyContentType",
    "SendChatMessageRequestHostedContentsItem",
    "SendChatMessageRequestImportance",
    "SendChatMessageRequestMentionsItem",
    "SendChatMessageRequestMentionsItemMentioned",
    "SendChatMessageRequestMentionsItemMentionedUser",
    "UpdateChatMessageRequestBody",
    "UpdateChatMessageRequestBodyContentType",
]
