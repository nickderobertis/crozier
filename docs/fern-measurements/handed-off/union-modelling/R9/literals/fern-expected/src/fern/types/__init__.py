



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cover import Cover
    from .cover_role import CoverRole
    from .handover_shift import HandoverShift
    from .leave import Leave
    from .leave_role import LeaveRole
    from .shift import Shift
    from .shift_assignment import ShiftAssignment
    from .shift_backup import ShiftBackup
    from .training import Training
    from .training_role import TrainingRole
_dynamic_imports: typing.Dict[str, str] = {
    "Cover": ".cover",
    "CoverRole": ".cover_role",
    "HandoverShift": ".handover_shift",
    "Leave": ".leave",
    "LeaveRole": ".leave_role",
    "Shift": ".shift",
    "ShiftAssignment": ".shift_assignment",
    "ShiftBackup": ".shift_backup",
    "Training": ".training",
    "TrainingRole": ".training_role",
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
    "Cover",
    "CoverRole",
    "HandoverShift",
    "Leave",
    "LeaveRole",
    "Shift",
    "ShiftAssignment",
    "ShiftBackup",
    "Training",
    "TrainingRole",
]
