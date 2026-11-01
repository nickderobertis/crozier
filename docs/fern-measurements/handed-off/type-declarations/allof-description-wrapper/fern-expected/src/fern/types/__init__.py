



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .booking import Booking
    from .booking_backup import BookingBackup
    from .booking_booked_by import BookingBookedBy
    from .dome_name import DomeName
    from .hash import Hash
    from .night_count import NightCount
    from .observer import Observer
    from .slot_id import SlotId
    from .telescope import Telescope
_dynamic_imports: typing.Dict[str, str] = {
    "Booking": ".booking",
    "BookingBackup": ".booking_backup",
    "BookingBookedBy": ".booking_booked_by",
    "DomeName": ".dome_name",
    "Hash": ".hash",
    "NightCount": ".night_count",
    "Observer": ".observer",
    "SlotId": ".slot_id",
    "Telescope": ".telescope",
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
    "Booking",
    "BookingBackup",
    "BookingBookedBy",
    "DomeName",
    "Hash",
    "NightCount",
    "Observer",
    "SlotId",
    "Telescope",
]
