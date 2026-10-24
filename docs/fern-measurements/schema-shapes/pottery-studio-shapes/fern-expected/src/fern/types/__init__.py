



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cone_number import ConeNumber
    from .cooled import Cooled
    from .firing_booking import FiringBooking
    from .firing_booking_ending import FiringBookingEnding, FiringBookingEnding_Cooled, FiringBookingEnding_Vented
    from .firing_booking_shelf import FiringBookingShelf
    from .firing_booking_shelf_level import FiringBookingShelfLevel
    from .target_cone import TargetCone
    from .vented import Vented
_dynamic_imports: typing.Dict[str, str] = {
    "ConeNumber": ".cone_number",
    "Cooled": ".cooled",
    "FiringBooking": ".firing_booking",
    "FiringBookingEnding": ".firing_booking_ending",
    "FiringBookingEnding_Cooled": ".firing_booking_ending",
    "FiringBookingEnding_Vented": ".firing_booking_ending",
    "FiringBookingShelf": ".firing_booking_shelf",
    "FiringBookingShelfLevel": ".firing_booking_shelf_level",
    "TargetCone": ".target_cone",
    "Vented": ".vented",
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
    "ConeNumber",
    "Cooled",
    "FiringBooking",
    "FiringBookingEnding",
    "FiringBookingEnding_Cooled",
    "FiringBookingEnding_Vented",
    "FiringBookingShelf",
    "FiringBookingShelfLevel",
    "TargetCone",
    "Vented",
]
