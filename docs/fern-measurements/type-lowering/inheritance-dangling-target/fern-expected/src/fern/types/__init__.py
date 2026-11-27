



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dial_control_gadget import DialControlGadget
    from .dial_control_gadget_kind import DialControlGadgetKind
    from .fan_gadget import FanGadget
    from .fan_gadget_kind import FanGadgetKind
    from .gadget import Gadget, Gadget_Dial, Gadget_Fan, Gadget_Lamp
    from .lamp_gadget import LampGadget
    from .lamp_gadget_kind import LampGadgetKind
    from .panel import Panel
    from .panel_gadgets_item import PanelGadgetsItem
_dynamic_imports: typing.Dict[str, str] = {
    "DialControlGadget": ".dial_control_gadget",
    "DialControlGadgetKind": ".dial_control_gadget_kind",
    "FanGadget": ".fan_gadget",
    "FanGadgetKind": ".fan_gadget_kind",
    "Gadget": ".gadget",
    "Gadget_Dial": ".gadget",
    "Gadget_Fan": ".gadget",
    "Gadget_Lamp": ".gadget",
    "LampGadget": ".lamp_gadget",
    "LampGadgetKind": ".lamp_gadget_kind",
    "Panel": ".panel",
    "PanelGadgetsItem": ".panel_gadgets_item",
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
    "DialControlGadget",
    "DialControlGadgetKind",
    "FanGadget",
    "FanGadgetKind",
    "Gadget",
    "Gadget_Dial",
    "Gadget_Fan",
    "Gadget_Lamp",
    "LampGadget",
    "LampGadgetKind",
    "Panel",
    "PanelGadgetsItem",
]
