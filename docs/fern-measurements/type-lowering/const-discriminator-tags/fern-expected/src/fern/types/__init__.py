



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .approval_envelope import ApprovalEnvelope
    from .event import Event
    from .event_vessel_arrived import EventVesselArrived
    from .event_vessel_arrived_type import EventVesselArrivedType
    from .event_vessel_departed import EventVesselDeparted
    from .event_vessel_departed_type import EventVesselDepartedType
    from .flag_signal import FlagSignal
    from .lamp_signal import LampSignal
    from .message_item import MessageItem
    from .note_item import NoteItem
    from .ping_envelope import PingEnvelope
    from .signal import Signal, Signal_Flag, Signal_Lamp
    from .text_envelope import TextEnvelope
    from .timeline import Timeline
    from .timeline_envelopes_item import (
        TimelineEnvelopesItem,
        TimelineEnvelopesItem_Approval,
        TimelineEnvelopesItem_Ping,
        TimelineEnvelopesItem_Text,
        TimelineEnvelopesItem_Tool,
    )
    from .timeline_items_item import (
        TimelineItemsItem,
        TimelineItemsItem_Message,
        TimelineItemsItem_Note,
        TimelineItemsItem_Tool,
    )
    from .tool_envelope import ToolEnvelope
    from .tool_item import ToolItem
_dynamic_imports: typing.Dict[str, str] = {
    "ApprovalEnvelope": ".approval_envelope",
    "Event": ".event",
    "EventVesselArrived": ".event_vessel_arrived",
    "EventVesselArrivedType": ".event_vessel_arrived_type",
    "EventVesselDeparted": ".event_vessel_departed",
    "EventVesselDepartedType": ".event_vessel_departed_type",
    "FlagSignal": ".flag_signal",
    "LampSignal": ".lamp_signal",
    "MessageItem": ".message_item",
    "NoteItem": ".note_item",
    "PingEnvelope": ".ping_envelope",
    "Signal": ".signal",
    "Signal_Flag": ".signal",
    "Signal_Lamp": ".signal",
    "TextEnvelope": ".text_envelope",
    "Timeline": ".timeline",
    "TimelineEnvelopesItem": ".timeline_envelopes_item",
    "TimelineEnvelopesItem_Approval": ".timeline_envelopes_item",
    "TimelineEnvelopesItem_Ping": ".timeline_envelopes_item",
    "TimelineEnvelopesItem_Text": ".timeline_envelopes_item",
    "TimelineEnvelopesItem_Tool": ".timeline_envelopes_item",
    "TimelineItemsItem": ".timeline_items_item",
    "TimelineItemsItem_Message": ".timeline_items_item",
    "TimelineItemsItem_Note": ".timeline_items_item",
    "TimelineItemsItem_Tool": ".timeline_items_item",
    "ToolEnvelope": ".tool_envelope",
    "ToolItem": ".tool_item",
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
    "Event",
    "EventVesselArrived",
    "EventVesselArrivedType",
    "EventVesselDeparted",
    "EventVesselDepartedType",
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
]
