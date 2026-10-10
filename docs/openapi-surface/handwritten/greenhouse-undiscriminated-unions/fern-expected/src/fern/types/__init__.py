



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cutting import Cutting
    from .cutting_method import CuttingMethod
    from .origin import Origin
    from .propagation import Propagation
    from .schedule_planting_request import SchedulePlantingRequest
    from .seedling import Seedling
    from .seedling_method import SeedlingMethod
_dynamic_imports: typing.Dict[str, str] = {
    "Cutting": ".cutting",
    "CuttingMethod": ".cutting_method",
    "Origin": ".origin",
    "Propagation": ".propagation",
    "SchedulePlantingRequest": ".schedule_planting_request",
    "Seedling": ".seedling",
    "SeedlingMethod": ".seedling_method",
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


__all__ = ["Cutting", "CuttingMethod", "Origin", "Propagation", "SchedulePlantingRequest", "Seedling", "SeedlingMethod"]
