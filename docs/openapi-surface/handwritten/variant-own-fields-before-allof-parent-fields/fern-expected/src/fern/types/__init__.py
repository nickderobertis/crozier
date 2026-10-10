



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .embankment import Embankment
    from .gravity import Gravity
    from .inspected import Inspected
    from .wall import Wall, Wall_Embankment, Wall_Gravity
_dynamic_imports: typing.Dict[str, str] = {
    "Embankment": ".embankment",
    "Gravity": ".gravity",
    "Inspected": ".inspected",
    "Wall": ".wall",
    "Wall_Embankment": ".wall",
    "Wall_Gravity": ".wall",
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


__all__ = ["Embankment", "Gravity", "Inspected", "Wall", "Wall_Embankment", "Wall_Gravity"]
