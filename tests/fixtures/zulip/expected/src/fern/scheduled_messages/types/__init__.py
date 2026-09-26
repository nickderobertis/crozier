



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_scheduled_message_request_to import CreateScheduledMessageRequestTo
    from .create_scheduled_message_request_type import CreateScheduledMessageRequestType
    from .create_scheduled_message_response import CreateScheduledMessageResponse
    from .get_scheduled_messages_response import GetScheduledMessagesResponse
    from .update_scheduled_message_request_to import UpdateScheduledMessageRequestTo
    from .update_scheduled_message_request_type import UpdateScheduledMessageRequestType
    from .update_scheduled_message_response import UpdateScheduledMessageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateScheduledMessageRequestTo": ".create_scheduled_message_request_to",
    "CreateScheduledMessageRequestType": ".create_scheduled_message_request_type",
    "CreateScheduledMessageResponse": ".create_scheduled_message_response",
    "GetScheduledMessagesResponse": ".get_scheduled_messages_response",
    "UpdateScheduledMessageRequestTo": ".update_scheduled_message_request_to",
    "UpdateScheduledMessageRequestType": ".update_scheduled_message_request_type",
    "UpdateScheduledMessageResponse": ".update_scheduled_message_response",
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
    "CreateScheduledMessageRequestTo",
    "CreateScheduledMessageRequestType",
    "CreateScheduledMessageResponse",
    "GetScheduledMessagesResponse",
    "UpdateScheduledMessageRequestTo",
    "UpdateScheduledMessageRequestType",
    "UpdateScheduledMessageResponse",
]
