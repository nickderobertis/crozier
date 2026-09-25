



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_message import ChatMessage
    from .error_response import ErrorResponse
    from .error_response_status import ErrorResponseStatus
    from .group import Group
    from .member import Member
    from .post import Post
    from .session import Session
    from .webhook import Webhook
    from .webhook_events_item import WebhookEventsItem
_dynamic_imports: typing.Dict[str, str] = {
    "ChatMessage": ".chat_message",
    "ErrorResponse": ".error_response",
    "ErrorResponseStatus": ".error_response_status",
    "Group": ".group",
    "Member": ".member",
    "Post": ".post",
    "Session": ".session",
    "Webhook": ".webhook",
    "WebhookEventsItem": ".webhook_events_item",
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
    "ChatMessage",
    "ErrorResponse",
    "ErrorResponseStatus",
    "Group",
    "Member",
    "Post",
    "Session",
    "Webhook",
    "WebhookEventsItem",
]
