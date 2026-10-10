



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .harbor_berth_assignment import HarborBerthAssignment
    from .harbor_closed import HarborClosed
    from .harbor_event import HarborEvent, HarborEvent_Closed, HarborEvent_Opened
    from .harbor_opened import HarborOpened
    from .harbor_voyage import HarborVoyage
_dynamic_imports: typing.Dict[str, str] = {
    "HarborBerthAssignment": ".harbor_berth_assignment",
    "HarborClosed": ".harbor_closed",
    "HarborEvent": ".harbor_event",
    "HarborEvent_Closed": ".harbor_event",
    "HarborEvent_Opened": ".harbor_event",
    "HarborOpened": ".harbor_opened",
    "HarborVoyage": ".harbor_voyage",
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
    "HarborBerthAssignment",
    "HarborClosed",
    "HarborEvent",
    "HarborEvent_Closed",
    "HarborEvent_Opened",
    "HarborOpened",
    "HarborVoyage",
]
