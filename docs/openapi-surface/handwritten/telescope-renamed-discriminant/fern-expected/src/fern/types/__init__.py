



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .galaxy_target import GalaxyTarget
    from .instrument import Instrument, Instrument_Lens, Instrument_Mirror
    from .reflector import Reflector
    from .refractor import Refractor
    from .star_target import StarTarget
    from .target import Target, Target_Galaxy, Target_Star
_dynamic_imports: typing.Dict[str, str] = {
    "GalaxyTarget": ".galaxy_target",
    "Instrument": ".instrument",
    "Instrument_Lens": ".instrument",
    "Instrument_Mirror": ".instrument",
    "Reflector": ".reflector",
    "Refractor": ".refractor",
    "StarTarget": ".star_target",
    "Target": ".target",
    "Target_Galaxy": ".target",
    "Target_Star": ".target",
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
    "GalaxyTarget",
    "Instrument",
    "Instrument_Lens",
    "Instrument_Mirror",
    "Reflector",
    "Refractor",
    "StarTarget",
    "Target",
    "Target_Galaxy",
    "Target_Star",
]
