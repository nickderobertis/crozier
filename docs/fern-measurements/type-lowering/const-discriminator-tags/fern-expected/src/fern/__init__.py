



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ApprovalEnvelope,
        Event,
        EventVesselArrived,
        EventVesselArrivedType,
        EventVesselDeparted,
        EventVesselDepartedType,
        FlagSignal,
        LampSignal,
        MessageItem,
        NoteItem,
        PingEnvelope,
        Signal,
        Signal_Flag,
        Signal_Lamp,
        TextEnvelope,
        Timeline,
        TimelineEnvelopesItem,
        TimelineEnvelopesItem_Approval,
        TimelineEnvelopesItem_Ping,
        TimelineEnvelopesItem_Text,
        TimelineEnvelopesItem_Tool,
        TimelineItemsItem,
        TimelineItemsItem_Message,
        TimelineItemsItem_Note,
        TimelineItemsItem_Tool,
        ToolEnvelope,
        ToolItem,
    )
    from . import radio
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApprovalEnvelope": ".types",
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Event": ".types",
    "EventVesselArrived": ".types",
    "EventVesselArrivedType": ".types",
    "EventVesselDeparted": ".types",
    "EventVesselDepartedType": ".types",
    "FernApi": ".client",
    "FlagSignal": ".types",
    "LampSignal": ".types",
    "MessageItem": ".types",
    "NoteItem": ".types",
    "PingEnvelope": ".types",
    "Signal": ".types",
    "Signal_Flag": ".types",
    "Signal_Lamp": ".types",
    "TextEnvelope": ".types",
    "Timeline": ".types",
    "TimelineEnvelopesItem": ".types",
    "TimelineEnvelopesItem_Approval": ".types",
    "TimelineEnvelopesItem_Ping": ".types",
    "TimelineEnvelopesItem_Text": ".types",
    "TimelineEnvelopesItem_Tool": ".types",
    "TimelineItemsItem": ".types",
    "TimelineItemsItem_Message": ".types",
    "TimelineItemsItem_Note": ".types",
    "TimelineItemsItem_Tool": ".types",
    "ToolEnvelope": ".types",
    "ToolItem": ".types",
    "__version__": ".version",
    "radio": ".radio",
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
    "ApprovalEnvelope",
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Event",
    "EventVesselArrived",
    "EventVesselArrivedType",
    "EventVesselDeparted",
    "EventVesselDepartedType",
    "FernApi",
    "FlagSignal",
    "LampSignal",
    "MessageItem",
    "NoteItem",
    "PingEnvelope",
    "Signal",
    "Signal_Flag",
    "Signal_Lamp",
    "TextEnvelope",
    "Timeline",
    "TimelineEnvelopesItem",
    "TimelineEnvelopesItem_Approval",
    "TimelineEnvelopesItem_Ping",
    "TimelineEnvelopesItem_Text",
    "TimelineEnvelopesItem_Tool",
    "TimelineItemsItem",
    "TimelineItemsItem_Message",
    "TimelineItemsItem_Note",
    "TimelineItemsItem_Tool",
    "ToolEnvelope",
    "ToolItem",
    "__version__",
    "radio",
]
