



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_firing_response import GetFiringResponse
    from .get_schedule_response import GetScheduleResponse
    from .get_state_response import GetStateResponse
    from .start_firing_response import StartFiringResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetFiringResponse": ".get_firing_response",
    "GetScheduleResponse": ".get_schedule_response",
    "GetStateResponse": ".get_state_response",
    "StartFiringResponse": ".start_firing_response",
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


__all__ = ["GetFiringResponse", "GetScheduleResponse", "GetStateResponse", "StartFiringResponse"]
