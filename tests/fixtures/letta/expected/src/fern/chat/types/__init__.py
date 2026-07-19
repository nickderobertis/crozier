



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_completion_request_messages_item import (
        ChatCompletionRequestMessagesItem,
        ChatCompletionRequestMessagesItem_Assistant,
        ChatCompletionRequestMessagesItem_Developer,
        ChatCompletionRequestMessagesItem_Function,
        ChatCompletionRequestMessagesItem_System,
        ChatCompletionRequestMessagesItem_Tool,
        ChatCompletionRequestMessagesItem_User,
    )
    from .chat_completion_request_stop import ChatCompletionRequestStop
_dynamic_imports: typing.Dict[str, str] = {
    "ChatCompletionRequestMessagesItem": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Assistant": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Developer": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Function": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_System": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Tool": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_User": ".chat_completion_request_messages_item",
    "ChatCompletionRequestStop": ".chat_completion_request_stop",
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
    "ChatCompletionRequestMessagesItem",
    "ChatCompletionRequestMessagesItem_Assistant",
    "ChatCompletionRequestMessagesItem_Developer",
    "ChatCompletionRequestMessagesItem_Function",
    "ChatCompletionRequestMessagesItem_System",
    "ChatCompletionRequestMessagesItem_Tool",
    "ChatCompletionRequestMessagesItem_User",
    "ChatCompletionRequestStop",
]
