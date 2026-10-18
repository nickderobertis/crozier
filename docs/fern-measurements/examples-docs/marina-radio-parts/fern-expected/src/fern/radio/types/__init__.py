



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .broadcast_request_message import BroadcastRequestMessage
    from .broadcast_request_message_parts_item import (
        BroadcastRequestMessagePartsItem,
        BroadcastRequestMessagePartsItem_Position,
        BroadcastRequestMessagePartsItem_Voice,
    )
    from .broadcast_request_message_parts_item_position import BroadcastRequestMessagePartsItemPosition
    from .broadcast_request_message_parts_item_voice import BroadcastRequestMessagePartsItemVoice
_dynamic_imports: typing.Dict[str, str] = {
    "BroadcastRequestMessage": ".broadcast_request_message",
    "BroadcastRequestMessagePartsItem": ".broadcast_request_message_parts_item",
    "BroadcastRequestMessagePartsItemPosition": ".broadcast_request_message_parts_item_position",
    "BroadcastRequestMessagePartsItemVoice": ".broadcast_request_message_parts_item_voice",
    "BroadcastRequestMessagePartsItem_Position": ".broadcast_request_message_parts_item",
    "BroadcastRequestMessagePartsItem_Voice": ".broadcast_request_message_parts_item",
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
    "BroadcastRequestMessage",
    "BroadcastRequestMessagePartsItem",
    "BroadcastRequestMessagePartsItemPosition",
    "BroadcastRequestMessagePartsItemVoice",
    "BroadcastRequestMessagePartsItem_Position",
    "BroadcastRequestMessagePartsItem_Voice",
]
