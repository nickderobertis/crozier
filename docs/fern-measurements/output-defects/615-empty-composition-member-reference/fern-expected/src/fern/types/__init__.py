



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .kiln import Kiln
    from .load import Load
    from .load_noted_kiln import LoadNotedKiln
    from .load_reserved_kiln import LoadReservedKiln
_dynamic_imports: typing.Dict[str, str] = {
    "Kiln": ".kiln",
    "Load": ".load",
    "LoadNotedKiln": ".load_noted_kiln",
    "LoadReservedKiln": ".load_reserved_kiln",
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


__all__ = ["Kiln", "Load", "LoadNotedKiln", "LoadReservedKiln"]
