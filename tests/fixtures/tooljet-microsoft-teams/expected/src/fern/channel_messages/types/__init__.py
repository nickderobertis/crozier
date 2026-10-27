



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_channel_message_request_expand import GetChannelMessageRequestExpand
    from .list_channel_messages_request_expand import ListChannelMessagesRequestExpand
    from .list_channel_messages_response import ListChannelMessagesResponse
    from .send_channel_message_request_body import SendChannelMessageRequestBody
    from .send_channel_message_request_body_content_type import SendChannelMessageRequestBodyContentType
    from .send_channel_message_request_hosted_contents_item import SendChannelMessageRequestHostedContentsItem
    from .send_channel_message_request_importance import SendChannelMessageRequestImportance
    from .send_channel_message_request_mentions_item import SendChannelMessageRequestMentionsItem
    from .send_channel_message_request_mentions_item_mentioned import SendChannelMessageRequestMentionsItemMentioned
    from .send_channel_message_request_mentions_item_mentioned_user import (
        SendChannelMessageRequestMentionsItemMentionedUser,
    )
    from .update_channel_message_request_body import UpdateChannelMessageRequestBody
    from .update_channel_message_request_body_content_type import UpdateChannelMessageRequestBodyContentType
_dynamic_imports: typing.Dict[str, str] = {
    "GetChannelMessageRequestExpand": ".get_channel_message_request_expand",
    "ListChannelMessagesRequestExpand": ".list_channel_messages_request_expand",
    "ListChannelMessagesResponse": ".list_channel_messages_response",
    "SendChannelMessageRequestBody": ".send_channel_message_request_body",
    "SendChannelMessageRequestBodyContentType": ".send_channel_message_request_body_content_type",
    "SendChannelMessageRequestHostedContentsItem": ".send_channel_message_request_hosted_contents_item",
    "SendChannelMessageRequestImportance": ".send_channel_message_request_importance",
    "SendChannelMessageRequestMentionsItem": ".send_channel_message_request_mentions_item",
    "SendChannelMessageRequestMentionsItemMentioned": ".send_channel_message_request_mentions_item_mentioned",
    "SendChannelMessageRequestMentionsItemMentionedUser": ".send_channel_message_request_mentions_item_mentioned_user",
    "UpdateChannelMessageRequestBody": ".update_channel_message_request_body",
    "UpdateChannelMessageRequestBodyContentType": ".update_channel_message_request_body_content_type",
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
    "GetChannelMessageRequestExpand",
    "ListChannelMessagesRequestExpand",
    "ListChannelMessagesResponse",
    "SendChannelMessageRequestBody",
    "SendChannelMessageRequestBodyContentType",
    "SendChannelMessageRequestHostedContentsItem",
    "SendChannelMessageRequestImportance",
    "SendChannelMessageRequestMentionsItem",
    "SendChannelMessageRequestMentionsItemMentioned",
    "SendChannelMessageRequestMentionsItemMentionedUser",
    "UpdateChannelMessageRequestBody",
    "UpdateChannelMessageRequestBodyContentType",
]
