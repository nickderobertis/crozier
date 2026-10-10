



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .arrival import Arrival
    from .berth import Berth
    from .departure import Departure
    from .gangway_change import GangwayChange, GangwayChange_Lowered, GangwayChange_Raised
    from .lowered import Lowered
    from .movement import Movement, Movement_Arrived, Movement_Departed
    from .raised import Raised
_dynamic_imports: typing.Dict[str, str] = {
    "Arrival": ".arrival",
    "Berth": ".berth",
    "Departure": ".departure",
    "GangwayChange": ".gangway_change",
    "GangwayChange_Lowered": ".gangway_change",
    "GangwayChange_Raised": ".gangway_change",
    "Lowered": ".lowered",
    "Movement": ".movement",
    "Movement_Arrived": ".movement",
    "Movement_Departed": ".movement",
    "Raised": ".raised",
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
    "Arrival",
    "Berth",
    "Departure",
    "GangwayChange",
    "GangwayChange_Lowered",
    "GangwayChange_Raised",
    "Lowered",
    "Movement",
    "Movement_Arrived",
    "Movement_Departed",
    "Raised",
]
