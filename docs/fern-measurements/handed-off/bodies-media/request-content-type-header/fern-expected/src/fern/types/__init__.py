



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bell import Bell
    from .bell_cast import BellCast
    from .cast_order import CastOrder, CastOrder_Bell, CastOrder_Handbell
    from .handbell_cast import HandbellCast
    from .recast_order import RecastOrder, RecastOrder_Bell, RecastOrder_Handbell
_dynamic_imports: typing.Dict[str, str] = {
    "Bell": ".bell",
    "BellCast": ".bell_cast",
    "CastOrder": ".cast_order",
    "CastOrder_Bell": ".cast_order",
    "CastOrder_Handbell": ".cast_order",
    "HandbellCast": ".handbell_cast",
    "RecastOrder": ".recast_order",
    "RecastOrder_Bell": ".recast_order",
    "RecastOrder_Handbell": ".recast_order",
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
    "Bell",
    "BellCast",
    "CastOrder",
    "CastOrder_Bell",
    "CastOrder_Handbell",
    "HandbellCast",
    "RecastOrder",
    "RecastOrder_Bell",
    "RecastOrder_Handbell",
]
