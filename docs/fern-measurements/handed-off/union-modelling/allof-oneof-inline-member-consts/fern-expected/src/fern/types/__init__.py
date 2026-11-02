



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .handover_any_of_const import HandoverAnyOfConst
    from .handover_any_of_const_mode import HandoverAnyOfConstMode
    from .handover_any_of_const_slots_value import HandoverAnyOfConstSlotsValue
    from .handover_any_of_enum import HandoverAnyOfEnum
    from .handover_any_of_enum_mode import HandoverAnyOfEnumMode
    from .handover_any_of_enum_slots_value import HandoverAnyOfEnumSlotsValue
    from .handover_one_of_const import HandoverOneOfConst
    from .handover_one_of_const_mode import HandoverOneOfConstMode
    from .handover_one_of_const_slots_value import HandoverOneOfConstSlotsValue
    from .handover_one_of_enum import HandoverOneOfEnum
    from .handover_one_of_enum_mode import HandoverOneOfEnumMode
    from .handover_one_of_enum_slots_value import HandoverOneOfEnumSlotsValue
    from .order import Order
_dynamic_imports: typing.Dict[str, str] = {
    "HandoverAnyOfConst": ".handover_any_of_const",
    "HandoverAnyOfConstMode": ".handover_any_of_const_mode",
    "HandoverAnyOfConstSlotsValue": ".handover_any_of_const_slots_value",
    "HandoverAnyOfEnum": ".handover_any_of_enum",
    "HandoverAnyOfEnumMode": ".handover_any_of_enum_mode",
    "HandoverAnyOfEnumSlotsValue": ".handover_any_of_enum_slots_value",
    "HandoverOneOfConst": ".handover_one_of_const",
    "HandoverOneOfConstMode": ".handover_one_of_const_mode",
    "HandoverOneOfConstSlotsValue": ".handover_one_of_const_slots_value",
    "HandoverOneOfEnum": ".handover_one_of_enum",
    "HandoverOneOfEnumMode": ".handover_one_of_enum_mode",
    "HandoverOneOfEnumSlotsValue": ".handover_one_of_enum_slots_value",
    "Order": ".order",
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
    "HandoverAnyOfConst",
    "HandoverAnyOfConstMode",
    "HandoverAnyOfConstSlotsValue",
    "HandoverAnyOfEnum",
    "HandoverAnyOfEnumMode",
    "HandoverAnyOfEnumSlotsValue",
    "HandoverOneOfConst",
    "HandoverOneOfConstMode",
    "HandoverOneOfConstSlotsValue",
    "HandoverOneOfEnum",
    "HandoverOneOfEnumMode",
    "HandoverOneOfEnumSlotsValue",
    "Order",
]
