



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .conversation import Conversation
    from .delta import Delta
    from .delta_event import DeltaEvent
    from .done import Done
    from .done_event import DoneEvent
    from .done_finish_reason import DoneFinishReason
    from .error_event import ErrorEvent
    from .message import Message
    from .message_role import MessageRole
    from .message_status import MessageStatus
    from .model_alias import ModelAlias
    from .problem import Problem
    from .stream_event import StreamEvent, StreamEvent_Delta, StreamEvent_Done, StreamEvent_Error, StreamEvent_Usage
    from .usage import Usage
    from .usage_event import UsageEvent
_dynamic_imports: typing.Dict[str, str] = {
    "Conversation": ".conversation",
    "Delta": ".delta",
    "DeltaEvent": ".delta_event",
    "Done": ".done",
    "DoneEvent": ".done_event",
    "DoneFinishReason": ".done_finish_reason",
    "ErrorEvent": ".error_event",
    "Message": ".message",
    "MessageRole": ".message_role",
    "MessageStatus": ".message_status",
    "ModelAlias": ".model_alias",
    "Problem": ".problem",
    "StreamEvent": ".stream_event",
    "StreamEvent_Delta": ".stream_event",
    "StreamEvent_Done": ".stream_event",
    "StreamEvent_Error": ".stream_event",
    "StreamEvent_Usage": ".stream_event",
    "Usage": ".usage",
    "UsageEvent": ".usage_event",
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
    "Conversation",
    "Delta",
    "DeltaEvent",
    "Done",
    "DoneEvent",
    "DoneFinishReason",
    "ErrorEvent",
    "Message",
    "MessageRole",
    "MessageStatus",
    "ModelAlias",
    "Problem",
    "StreamEvent",
    "StreamEvent_Delta",
    "StreamEvent_Done",
    "StreamEvent_Error",
    "StreamEvent_Usage",
    "Usage",
    "UsageEvent",
]
